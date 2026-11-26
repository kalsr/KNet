

# Deepfake and Impersonation Verification Console (DIVC)
# Developed by Randy Singh from Kalsnet (KNet) Consulting Group

# Purpose
    # A decision support prototype that scores voice calls, video calls, recorded
    # media and recruiting interviews for impersonation and deepfake risk. It
    # combines content provenance (C2PA content credentials), out of band
    # confirmation, liveness, media artifact signals, metadata consistency,
    # behavioral red flags and caller ID checks into one explainable risk score.


# Important note
    # This is a prototype. The liveness and artifact scores are inputs that would
    # come from accredited detection models in production. The app does not
    # claim to detect deepfakes on its own; it fuses signals and enforces a
    # verification workflow so that no single signal decides the outcome.


import io
import hashlib
import secrets
import datetime

import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

# Optional libraries. The app still runs if any of these are missing.
try:
    import docx
    HAVE_DOCX = True
except ImportError:
    HAVE_DOCX = False

try:
    from pypdf import PdfReader
    HAVE_PYPDF = True
except ImportError:
    HAVE_PYPDF = False

try:
    from fpdf import FPDF
    HAVE_FPDF = True
except ImportError:
    HAVE_FPDF = False

try:
    from PIL import Image
    from PIL.ExifTags import TAGS
    HAVE_PIL = True
except ImportError:
    HAVE_PIL = False

try:
    import c2pa
    HAVE_C2PA = True
except ImportError:
    HAVE_C2PA = False


# --------------------------------------------------------------------------
# Constants, field dictionary and model parameters
# --------------------------------------------------------------------------

APP_TITLE = "Deepfake and Impersonation Verification Console"
APP_SUBTITLE = "Developed by Randy Singh from Kalsnet (KNet) Consulting Group"

ROLES = ["Commander", "Vendor", "Applicant", "Staff officer"]
CHANNELS = ["Voice call", "Video call", "Recorded media", "Applicant interview"]
REQUEST_TYPES = ["Routine", "Credential request", "Orders change", "Funds transfer"]
C2PA_STATES = ["Valid", "Missing", "Invalid"]
OOB_STATES = ["Confirmed", "Not attempted", "Failed"]

# Risk value (0 means safe, 1 means maximum risk) for each categorical state
PROVENANCE_RISK = {"Valid": 0.0, "Missing": 0.6, "Invalid": 1.0}
OOB_RISK = {"Confirmed": 0.0, "Not attempted": 0.7, "Failed": 1.0}

# Impact multiplier: higher consequence requests need stronger evidence
REQUEST_FACTOR = {
    "Routine": 1.00,
    "Credential request": 1.15,
    "Orders change": 1.20,
    "Funds transfer": 1.25,
}
URGENCY_STEP = 0.03

# Component weights. They must add up to 1.0
WEIGHTS = {
    "provenance": 0.20,
    "out_of_band": 0.25,
    "liveness": 0.15,
    "artifact": 0.15,
    "metadata": 0.10,
    "behavior": 0.10,
    "caller_id": 0.05,
}

# Decision bands on the final 0 to 100 score
PROCEED_BELOW = 30
BLOCK_AT_OR_ABOVE = 60

# Hard rules applied after the weighted score
FLOOR_C2PA_INVALID = 70
FLOOR_OOB_FAILED = 80
CAP_STRONG_EVIDENCE = 40

# Known markers that generative tools write into file metadata
AI_GENERATOR_MARKERS = [
    "trainedAlgorithmicMedia",
    "compositeWithTrainedAlgorithmicMedia",
    "Stable Diffusion",
    "Midjourney",
    "DALL-E",
    "DALLE",
    "Adobe Firefly",
    "Imagen",
    "Sora",
    "ElevenLabs",
]

FIELD_DICTIONARY = [
    ("case_id", "Text", "Unique ID of the call, media item or interview",
     "Links evidence, out of band logs and reports to one case"),
    ("claimed_identity", "Text", "Name the person claims to be",
     "The identity that must be proven; checked against the trusted directory"),
    ("claimed_role", "Category", ", ".join(ROLES),
     "Impersonators target authority roles because people obey them quickly"),
    ("channel", "Category", ", ".join(CHANNELS),
     "Decides which liveness signals apply; voice calls have no face signal"),
    ("request_type", "Category", ", ".join(REQUEST_TYPES),
     "Sets the impact multiplier; money and credentials raise the stakes"),
    ("urgency_level", "Integer 1 to 5", "How much time pressure the requester applies",
     "Manufactured urgency is a classic social engineering tactic"),
    ("c2pa_status", "Category", ", ".join(C2PA_STATES),
     "Result of checking signed content credentials on the media"),
    ("oob_status", "Category", ", ".join(OOB_STATES),
     "Result of calling the person back on a number from a trusted directory"),
    ("caller_id_match", "Yes or No", "Does the incoming number match the directory entry",
     "Weak signal because caller ID can be spoofed, so it has a small weight"),
    ("voice_liveness", "Number 0 to 1", "Detector confidence that the voice is a live human",
     "Synthetic voices often fail challenge and response or spectral tests"),
    ("face_liveness", "Number 0 to 1 or blank", "Detector confidence that the face is live",
     "Blank for voice only channels; checks blinking, lip sync and depth"),
    ("artifact_score", "Number 0 to 1", "Detector score for generation artifacts",
     "Higher means more visual or audio traces of synthesis"),
    ("metadata_consistency", "Number 0 to 1", "How well time, device, location and codec data agree",
     "Edited or generated media often has inconsistent metadata"),
    ("behavior_anomaly", "Number 0 to 1", "Analyst rating of red flags in the request",
     "Requests for secrecy, bypassing process or new payment details"),
    ("ground_truth", "Optional label", "Genuine or Deepfake, only in test data",
     "Used to measure precision and recall; never used in scoring"),
]

REQUIRED_COLUMNS = [f[0] for f in FIELD_DICTIONARY if f[0] != "ground_truth"]


# --------------------------------------------------------------------------
# Scoring engine
# --------------------------------------------------------------------------

def clip01(value, default=0.5):
    """Return a number between 0 and 1. Missing values become the default."""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    if np.isnan(number):
        return default
    return float(min(1.0, max(0.0, number)))


def is_missing(value):
    """True when a value is blank or not a number."""
    if value is None:
        return True
    try:
        return bool(pd.isna(value))
    except (TypeError, ValueError):
        return False


def to_bool(value):
    """Convert Yes, True, 1 and similar values to a boolean."""
    if isinstance(value, (bool, np.bool_)):
        return bool(value)
    text = str(value).strip().lower()
    return text in ("yes", "true", "1", "y", "match")


def score_case(row):
    """Score one case. Returns a dictionary with every intermediate value."""
    c2pa_state = str(row.get("c2pa_status", "Missing"))
    oob_state = str(row.get("oob_status", "Not attempted"))
    request = str(row.get("request_type", "Routine"))
    channel = str(row.get("channel", "Voice call"))

    # Component 1: provenance risk from content credentials
    r_provenance = PROVENANCE_RISK.get(c2pa_state, 0.6)

    # Component 2: out of band confirmation risk
    r_oob = OOB_RISK.get(oob_state, 0.7)

    # Component 3: liveness risk is one minus the mean of available liveness scores
    live_values = []
    if not is_missing(row.get("voice_liveness")):
        live_values.append(clip01(row.get("voice_liveness")))
    if channel != "Voice call" and not is_missing(row.get("face_liveness")):
        live_values.append(clip01(row.get("face_liveness")))
    if live_values:
        r_liveness = 1.0 - float(np.mean(live_values))
    else:
        r_liveness = 0.5

    # Components 4 to 7
    r_artifact = clip01(row.get("artifact_score"))
    r_metadata = 1.0 - clip01(row.get("metadata_consistency"))
    r_behavior = clip01(row.get("behavior_anomaly"))
    r_caller = 0.0 if to_bool(row.get("caller_id_match", False)) else 1.0

    components = {
        "provenance": r_provenance,
        "out_of_band": r_oob,
        "liveness": r_liveness,
        "artifact": r_artifact,
        "metadata": r_metadata,
        "behavior": r_behavior,
        "caller_id": r_caller,
    }

    contributions = {k: 100.0 * WEIGHTS[k] * v for k, v in components.items()}
    base_score = sum(contributions.values())

    try:
        urgency = int(float(row.get("urgency_level", 1)))
    except (TypeError, ValueError):
        urgency = 1
    urgency = min(5, max(1, urgency))
    multiplier = REQUEST_FACTOR.get(request, 1.0) + URGENCY_STEP * (urgency - 1)

    adjusted = min(100.0, base_score * multiplier)

    rules = []
    final_score = adjusted
    if c2pa_state == "Invalid" and final_score < FLOOR_C2PA_INVALID:
        final_score = FLOOR_C2PA_INVALID
        rules.append("Invalid content credentials raise the score to at least 70")
    if oob_state == "Failed" and final_score < FLOOR_OOB_FAILED:
        final_score = FLOOR_OOB_FAILED
        rules.append("Failed out of band confirmation raises the score to at least 80")
    if (oob_state == "Confirmed" and c2pa_state == "Valid"
            and final_score > CAP_STRONG_EVIDENCE):
        final_score = CAP_STRONG_EVIDENCE
        rules.append("Confirmed callback plus valid credentials cap the score at 40")

    if final_score < PROCEED_BELOW:
        decision = "Proceed"
    elif final_score < BLOCK_AT_OR_ABOVE:
        decision = "Hold and verify"
    else:
        decision = "Block and escalate"

    # Evidence completeness: share of the seven signals that were actually observed
    observed = 0
    observed += 0 if c2pa_state == "Missing" else 1
    observed += 0 if oob_state == "Not attempted" else 1
    observed += 1 if live_values else 0
    observed += 0 if is_missing(row.get("artifact_score")) else 1
    observed += 0 if is_missing(row.get("metadata_consistency")) else 1
    observed += 0 if is_missing(row.get("behavior_anomaly")) else 1
    observed += 1
    completeness = observed / 7.0

    top = sorted(contributions.items(), key=lambda item: item[1], reverse=True)[:3]
    reasons = [f"{name.replace('_', ' ')} adds {points:.1f} points" for name, points in top]

    return {
        "components": components,
        "contributions": contributions,
        "base_score": base_score,
        "multiplier": multiplier,
        "adjusted_score": adjusted,
        "final_score": round(final_score, 1),
        "decision": decision,
        "rules": rules,
        "completeness": completeness,
        "reasons": reasons,
    }


def score_frame(frame):
    """Score every row of a data frame and append result columns."""
    results = [score_case(row) for _, row in frame.iterrows()]
    out = frame.copy()
    out["base_score"] = [round(r["base_score"], 1) for r in results]
    out["multiplier"] = [round(r["multiplier"], 2) for r in results]
    out["risk_score"] = [r["final_score"] for r in results]
    out["decision"] = [r["decision"] for r in results]
    out["evidence_completeness"] = [round(r["completeness"], 2) for r in results]
    out["rules_applied"] = ["; ".join(r["rules"]) for r in results]
    out["top_reasons"] = ["; ".join(r["reasons"]) for r in results]
    return out


def evaluation_metrics(scored, threshold):
    """Confusion matrix and quality metrics when ground truth labels exist."""
    if "ground_truth" not in scored.columns:
        return None
    labels = scored["ground_truth"].astype(str).str.strip().str.lower()
    if not labels.isin(["deepfake", "genuine"]).any():
        return None
    actual = labels == "deepfake"
    flagged = scored["risk_score"] >= threshold
    tp = int((actual & flagged).sum())
    fp = int((~actual & flagged).sum())
    tn = int((~actual & ~flagged).sum())
    fn = int((actual & ~flagged).sum())
    total = tp + fp + tn + fn
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    accuracy = (tp + tn) / total if total else 0.0
    fpr = fp / (fp + tn) if (fp + tn) else 0.0
    return {"TP": tp, "FP": fp, "TN": tn, "FN": fn, "Precision": precision,
            "Recall": recall, "F1": f1, "Accuracy": accuracy,
            "False positive rate": fpr}


# --------------------------------------------------------------------------
# Synthetic data and file handling
# --------------------------------------------------------------------------

FIRST_NAMES = ["Alex", "Jordan", "Morgan", "Taylor", "Casey", "Riley", "Avery",
               "Quinn", "Drew", "Reese", "Parker", "Hayden"]
LAST_NAMES = ["Carter", "Nguyen", "Patel", "Brooks", "Ramirez", "Kim", "Okafor",
              "Hughes", "Silva", "Novak", "Grant", "Ellis"]


def generate_synthetic(n_cases, deepfake_rate, seed):
    """Create labeled synthetic cases. Deepfakes draw from riskier distributions."""
    rng = np.random.default_rng(seed)
    rows = []
    for i in range(n_cases):
        fake = rng.random() < deepfake_rate
        role = rng.choice(ROLES, p=[0.35, 0.30, 0.25, 0.10])
        channel = "Applicant interview" if role == "Applicant" else rng.choice(
            ["Voice call", "Video call", "Recorded media"], p=[0.45, 0.40, 0.15])
        if fake:
            request = rng.choice(REQUEST_TYPES, p=[0.10, 0.30, 0.20, 0.40])
            urgency = int(rng.choice([2, 3, 4, 5], p=[0.10, 0.20, 0.35, 0.35]))
            c2pa_state = rng.choice(C2PA_STATES, p=[0.05, 0.75, 0.20])
            oob_state = rng.choice(OOB_STATES, p=[0.05, 0.50, 0.45])
            caller = bool(rng.random() < 0.35)
            voice = rng.beta(2.5, 4.0)
            face = rng.beta(2.5, 4.0)
            artifact = rng.beta(4.0, 2.5)
            metadata = rng.beta(2.5, 3.5)
            behavior = rng.beta(4.0, 2.0)
        else:
            request = rng.choice(REQUEST_TYPES, p=[0.55, 0.20, 0.15, 0.10])
            urgency = int(rng.choice([1, 2, 3, 4], p=[0.40, 0.35, 0.20, 0.05]))
            c2pa_state = rng.choice(C2PA_STATES, p=[0.45, 0.53, 0.02])
            oob_state = rng.choice(OOB_STATES, p=[0.55, 0.43, 0.02])
            caller = bool(rng.random() < 0.90)
            voice = rng.beta(6.0, 1.8)
            face = rng.beta(6.0, 1.8)
            artifact = rng.beta(1.5, 6.0)
            metadata = rng.beta(6.0, 1.8)
            behavior = rng.beta(1.5, 6.0)
        rows.append({
            "case_id": f"CASE{1000 + i}",
            "claimed_identity": f"{rng.choice(FIRST_NAMES)} {rng.choice(LAST_NAMES)}",
            "claimed_role": role,
            "channel": channel,
            "request_type": request,
            "urgency_level": urgency,
            "c2pa_status": c2pa_state,
            "oob_status": oob_state,
            "caller_id_match": "Yes" if caller else "No",
            "voice_liveness": round(float(voice), 3),
            "face_liveness": np.nan if channel == "Voice call" else round(float(face), 3),
            "artifact_score": round(float(artifact), 3),
            "metadata_consistency": round(float(metadata), 3),
            "behavior_anomaly": round(float(behavior), 3),
            "ground_truth": "Deepfake" if fake else "Genuine",
        })
    return pd.DataFrame(rows)


def clean_uploaded_cases(frame):
    """Validate an uploaded case table and fill safe defaults where needed."""
    frame = frame.copy()
    frame.columns = [str(c).strip().lower().replace(" ", "_") for c in frame.columns]
    missing = [c for c in REQUIRED_COLUMNS if c not in frame.columns]
    defaults = {
        "claimed_role": "Vendor", "channel": "Voice call", "request_type": "Routine",
        "urgency_level": 1, "c2pa_status": "Missing", "oob_status": "Not attempted",
        "caller_id_match": "No", "voice_liveness": np.nan, "face_liveness": np.nan,
        "artifact_score": np.nan, "metadata_consistency": np.nan,
        "behavior_anomaly": np.nan,
    }
    for col in missing:
        if col == "case_id":
            frame[col] = [f"UPLOAD{i + 1}" for i in range(len(frame))]
        elif col == "claimed_identity":
            frame[col] = "Unknown"
        else:
            frame[col] = defaults[col]
    for col in ["voice_liveness", "face_liveness", "artifact_score",
                "metadata_consistency", "behavior_anomaly"]:
        frame[col] = pd.to_numeric(frame[col], errors="coerce").clip(0, 1)
    frame["urgency_level"] = pd.to_numeric(frame["urgency_level"], errors="coerce") \
        .fillna(1).clip(1, 5).astype(int)
    for col, allowed, fallback in [("c2pa_status", C2PA_STATES, "Missing"),
                                   ("oob_status", OOB_STATES, "Not attempted"),
                                   ("request_type", REQUEST_TYPES, "Routine"),
                                   ("channel", CHANNELS, "Voice call")]:
        lookup = {a.lower(): a for a in allowed}
        frame[col] = frame[col].astype(str).str.strip().str.lower().map(lookup).fillna(fallback)
    return frame, missing


def read_uploaded_document(uploaded):
    """Return a tuple of (kind, content) for a PDF, Word, text or CSV upload."""
    name = uploaded.name.lower()
    data = uploaded.getvalue()
    if name.endswith(".csv"):
        return "table", pd.read_csv(io.BytesIO(data))
    if name.endswith(".txt"):
        return "text", data.decode("utf-8", errors="replace")
    if name.endswith(".pdf"):
        if not HAVE_PYPDF:
            return "text", "Install pypdf to read PDF files."
        reader = PdfReader(io.BytesIO(data))
        pages = [p.extract_text() or "" for p in reader.pages]
        return "text", "\n\n".join(f"Page {i + 1}\n{t}" for i, t in enumerate(pages))
    if name.endswith(".docx"):
        if not HAVE_DOCX:
            return "text", "Install python-docx to read Word files."
        document = docx.Document(io.BytesIO(data))
        parts = [p.text for p in document.paragraphs if p.text.strip()]
        tables = []
        for table in document.tables:
            grid = [[cell.text for cell in r.cells] for r in table.rows]
            if len(grid) > 1:
                tables.append(pd.DataFrame(grid[1:], columns=grid[0]))
        return "docx", ("\n".join(parts), tables)
    return "text", "Unsupported file type."


# --------------------------------------------------------------------------
# Media provenance inspection
# --------------------------------------------------------------------------

def inspect_media(uploaded):
    """Hash the file, look for C2PA manifests and AI generator metadata."""
    data = uploaded.getvalue()
    report = {
        "file_name": uploaded.name,
        "size_bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "c2pa_library": "available" if HAVE_C2PA else "not installed",
        "c2pa_status": "Missing",
        "c2pa_detail": "",
        "ai_markers": [],
        "exif_software": "",
    }

    marker_present = (b"c2pa" in data) or (b"jumb" in data and b"c2cl" in data)

    if HAVE_C2PA:
        mime = uploaded.type or "application/octet-stream"
        try:
            reader = c2pa.Reader(mime, io.BytesIO(data))
            manifest_json = reader.json()
            if "validation_status" in manifest_json and '"code"' in manifest_json \
                    and "Failure" in manifest_json:
                report["c2pa_status"] = "Invalid"
                report["c2pa_detail"] = "Manifest found but validation reported failures"
            else:
                report["c2pa_status"] = "Valid"
                report["c2pa_detail"] = "Manifest found and signature validated"
        except Exception as error:
            if marker_present:
                report["c2pa_status"] = "Invalid"
                report["c2pa_detail"] = f"Manifest markers present but could not validate: {error}"
            else:
                report["c2pa_detail"] = "No content credentials found"
    else:
        if marker_present:
            report["c2pa_status"] = "Missing"
            report["c2pa_detail"] = ("Manifest markers found but not cryptographically "
                                     "validated. Install c2pa-python to validate.")
        else:
            report["c2pa_detail"] = "No content credentials found"

    text_view = data.decode("latin-1", errors="ignore")
    report["ai_markers"] = [m for m in AI_GENERATOR_MARKERS if m.lower() in text_view.lower()]

    if HAVE_PIL and (uploaded.type or "").startswith("image"):
        try:
            image = Image.open(io.BytesIO(data))
            exif = image.getexif()
            for tag_id, value in exif.items():
                if TAGS.get(tag_id) == "Software":
                    report["exif_software"] = str(value)
            report["dimensions"] = f"{image.width} by {image.height}"
        except Exception:
            pass
    return report


# --------------------------------------------------------------------------
# Report exports
# --------------------------------------------------------------------------

def summary_lines(scored):
    counts = scored["decision"].value_counts().to_dict()
    lines = [
        APP_TITLE,
        APP_SUBTITLE,
        f"Report generated: {datetime.datetime.now():%Y-%m-%d %H:%M}",
        "",
        f"Cases scored: {len(scored)}",
        f"Average risk score: {scored['risk_score'].mean():.1f}",
        f"Proceed: {counts.get('Proceed', 0)}",
        f"Hold and verify: {counts.get('Hold and verify', 0)}",
        f"Block and escalate: {counts.get('Block and escalate', 0)}",
    ]
    return lines


REPORT_COLUMNS = ["case_id", "claimed_identity", "claimed_role", "channel",
                  "request_type", "risk_score", "decision", "top_reasons"]


def export_txt(scored):
    lines = summary_lines(scored) + ["", "Case results"]
    for _, r in scored.iterrows():
        lines.append(f"{r['case_id']} | {r['claimed_identity']} | {r['claimed_role']} | "
                     f"{r['request_type']} | score {r['risk_score']} | {r['decision']} | "
                     f"{r['top_reasons']}")
    return "\n".join(lines).encode("utf-8")


def export_docx(scored):
    document = docx.Document()
    lines = summary_lines(scored)
    document.add_heading(lines[0], level=0)
    document.add_paragraph(lines[1])
    for line in lines[2:]:
        if line:
            document.add_paragraph(line)
    document.add_heading("Case results", level=1)
    table = document.add_table(rows=1, cols=len(REPORT_COLUMNS))
    table.style = "Light Grid Accent 1"
    for i, col in enumerate(REPORT_COLUMNS):
        table.rows[0].cells[i].text = col.replace("_", " ").title()
    for _, r in scored.iterrows():
        cells = table.add_row().cells
        for i, col in enumerate(REPORT_COLUMNS):
            cells[i].text = str(r[col])
    buffer = io.BytesIO()
    document.save(buffer)
    return buffer.getvalue()


def latin(text):
    return str(text).encode("latin-1", errors="replace").decode("latin-1")


def export_pdf(scored):
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=12)
    pdf.add_page()
    pdf.set_text_color(13, 71, 161)
    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 10, latin(APP_TITLE), new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, latin(APP_SUBTITLE), new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", "", 11)
    for line in summary_lines(scored)[2:]:
        pdf.cell(0, 6, latin(line), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)
    widths = [22, 38, 28, 34, 34, 16, 34, 71]
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_fill_color(227, 236, 250)
    for w, col in zip(widths, REPORT_COLUMNS):
        pdf.cell(w, 7, latin(col.replace("_", " ").title()), border=1, fill=True)
    pdf.ln()
    pdf.set_font("Helvetica", "", 8)
    for _, r in scored.iterrows():
        for w, col in zip(widths, REPORT_COLUMNS):
            value = latin(r[col])
            limit = int(w / 1.7)
            if len(value) > limit:
                value = value[: limit - 2] + ".."
            pdf.cell(w, 6, value, border=1)
        pdf.ln()
    return bytes(pdf.output())


# --------------------------------------------------------------------------
# Diagrams (Graphviz DOT, rendered by Streamlit in the browser)
# --------------------------------------------------------------------------

DOT_STYLE = """
    graph [rankdir=LR, bgcolor=transparent, fontname=Helvetica, nodesep=0.35];
    node  [shape=box, style="rounded,filled", fillcolor="#E3ECFA", color="#0D47A1",
           fontname=Helvetica, fontsize=11];
    edge  [color="#0D47A1", fontname=Helvetica, fontsize=10];
"""

DIAGRAM_WORKFLOW = "digraph G {" + DOT_STYLE + """
    A [label="Incoming call, media\\nor interview"];
    B [label="Capture evidence\\n(media file, caller ID)"];
    C [label="C2PA content\\ncredential check"];
    D [label="Liveness and\\nartifact detectors"];
    E [label="Out of band\\ncallback"];
    F [label="Analyst review of\\nbehavior red flags"];
    G [label="Risk fusion engine\\n(weighted score)", fillcolor="#BBDEFB"];
    H [label="Decision\\nProceed, Hold, Block", fillcolor="#BBDEFB"];
    I [label="Report and\\naudit trail"];
    A -> B; B -> C; B -> D; B -> E; B -> F;
    C -> G; D -> G; E -> G; F -> G; G -> H; H -> I;
}"""

DIAGRAM_SCORING = "digraph G {" + DOT_STYLE + """
    S1 [label="Seven risk components\\neach 0 to 1"];
    S2 [label="Multiply by weights\\nand by 100"];
    S3 [label="Base score\\n0 to 100"];
    S4 [label="Multiply by impact\\n(request type and urgency)"];
    S5 [label="Apply hard rules\\nfloors and cap"];
    S6 [label="Final risk score", fillcolor="#BBDEFB"];
    S1 -> S2 -> S3 -> S4 -> S5 -> S6;
}"""

DIAGRAM_DECISION = """digraph G {
    graph [rankdir=TB, bgcolor=transparent, fontname=Helvetica];
    node  [fontname=Helvetica, fontsize=11, style="rounded,filled", color="#0D47A1"];
    edge  [color="#0D47A1", fontname=Helvetica, fontsize=10];
    Q1 [shape=diamond, label="Score below 30?", fillcolor="#E3ECFA"];
    Q2 [shape=diamond, label="Score below 60?", fillcolor="#E3ECFA"];
    P  [shape=box, label="Proceed\\nlog the case", fillcolor="#C8E6C9"];
    H  [shape=box, label="Hold and verify\\nrequire callback and second approver", fillcolor="#FFF59D"];
    B  [shape=box, label="Block and escalate\\nnotify security office", fillcolor="#FFCDD2"];
    Q1 -> P [label="Yes"]; Q1 -> Q2 [label="No"];
    Q2 -> H [label="Yes"]; Q2 -> B [label="No"];
}"""

DIAGRAM_OOB = "digraph G {" + DOT_STYLE + """
    O1 [label="Request received\\nfrom claimed person"];
    O2 [label="End the session\\ndo not use supplied number"];
    O3 [label="Look up number in\\ntrusted directory"];
    O4 [label="Call back and read\\none time challenge code"];
    O5 [shape=diamond, label="Person confirms\\nrequest and code?", fillcolor="#FFFFFF"];
    O6 [label="Confirmed", fillcolor="#C8E6C9"];
    O7 [label="Failed", fillcolor="#FFCDD2"];
    O1 -> O2 -> O3 -> O4 -> O5;
    O5 -> O6 [label="Yes"]; O5 -> O7 [label="No"];
}"""

DIAGRAM_C2PA = "digraph G {" + DOT_STYLE + """
    M1 [label="Media file"];
    M2 [label="Compute SHA256\\nfingerprint"];
    M3 [shape=diamond, label="C2PA manifest\\npresent?", fillcolor="#FFFFFF"];
    M4 [shape=diamond, label="Signature and hash\\nvalidate?", fillcolor="#FFFFFF"];
    M5 [label="Valid\\nrisk 0.0", fillcolor="#C8E6C9"];
    M6 [label="Invalid\\nrisk 1.0", fillcolor="#FFCDD2"];
    M7 [label="Missing\\nrisk 0.6", fillcolor="#FFF59D"];
    M8 [label="Scan metadata for\\nAI generator markers"];
    M1 -> M2 -> M3;
    M3 -> M4 [label="Yes"]; M3 -> M7 [label="No"];
    M4 -> M5 [label="Yes"]; M4 -> M6 [label="No"];
    M2 -> M8;
}"""

DIAGRAM_SCREENING = "digraph G {" + DOT_STYLE + """
    R1 [label="Applicant interview\\n(video)"];
    R2 [label="Live challenge\\nturn head, read random words"];
    R3 [label="Face and voice\\nliveness scores"];
    R4 [label="Match ID document\\nto live face"];
    R5 [label="Check references through\\ntrusted contacts"];
    R6 [label="Risk fusion engine", fillcolor="#BBDEFB"];
    R1 -> R2 -> R3 -> R6; R1 -> R4 -> R6; R1 -> R5 -> R6;
}"""


# --------------------------------------------------------------------------
# User interface helpers
# --------------------------------------------------------------------------

def render_header():
    st.markdown(
        f"""
        <div style="padding: 14px 20px; border-bottom: 3px solid #0D47A1;
                    margin-bottom: 18px; background-color: #F4F8FE; border-radius: 6px;">
            <div style="color: #0D47A1; font-size: 34px; font-weight: 800;
                        line-height: 1.2;">{APP_TITLE}</div>
            <div style="color: #1565C0; font-size: 24px; font-weight: 700;
                        line-height: 1.3; margin-top: 4px;">{APP_SUBTITLE}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def decision_color(decision):
    return {"Proceed": "#2E7D32", "Hold and verify": "#F9A825",
            "Block and escalate": "#C62828"}.get(decision, "#555555")


def show_decision_card(result):
    color = decision_color(result["decision"])
    st.markdown(
        f"""
        <div style="border-left: 8px solid {color}; padding: 12px 16px;
                    background-color: #FAFAFA; border-radius: 4px;">
            <div style="font-size: 15px; color: #555;">Final risk score</div>
            <div style="font-size: 40px; font-weight: 800; color: {color};">
                {result['final_score']:.1f} of 100</div>
            <div style="font-size: 20px; font-weight: 700; color: {color};">
                {result['decision']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def contribution_chart(result):
    data = pd.DataFrame({
        "component": [k.replace("_", " ").title() for k in result["contributions"]],
        "points": list(result["contributions"].values()),
    })
    chart = alt.Chart(data).mark_bar(color="#1565C0").encode(
        x=alt.X("points:Q", title="Points added to base score"),
        y=alt.Y("component:N", sort="-x", title=None),
        tooltip=["component", alt.Tooltip("points:Q", format=".1f")],
    ).properties(height=240)
    st.altair_chart(chart, use_container_width=True)


def init_state():
    if "cases" not in st.session_state:
        st.session_state["cases"] = generate_synthetic(60, 0.30, 7)
        st.session_state["data_source"] = "Synthetic (default, 60 cases)"
    if "oob_log" not in st.session_state:
        st.session_state["oob_log"] = []
    if "media_c2pa" not in st.session_state:
        st.session_state["media_c2pa"] = None


# --------------------------------------------------------------------------
# Tabs
# --------------------------------------------------------------------------

def tab_guide():
    st.subheader("How the application works")
    st.write(
        "Deepfakes let an attacker sound or look like a commander, a vendor or a job "
        "applicant. No single detector is reliable on its own, so this console fuses "
        "several independent signals into one explainable risk score and then enforces "
        "a verification workflow. The diagram below shows the end to end flow."
    )
    st.graphviz_chart(DIAGRAM_WORKFLOW, use_container_width=True)

    st.markdown("#### Key concepts")
    with st.expander("Deepfake and impersonation", expanded=True):
        st.write(
            "A deepfake is audio, video or an image produced or altered by a generative "
            "model so that it appears to show a real person. Impersonation is the wider "
            "attack: using a deepfake, a spoofed phone number or a stolen identity to "
            "make someone act on a false request, such as moving money, sharing "
            "credentials or changing orders."
        )
    with st.expander("C2PA content credentials"):
        st.write(
            "The Coalition for Content Provenance and Authenticity standard attaches a "
            "cryptographically signed manifest to a media file. The manifest records who "
            "created the file, with what device or software, and every edit. If the file "
            "is altered after signing, the hash no longer matches and validation fails. "
            "Valid credentials are strong evidence of origin. Missing credentials are "
            "common today and only mildly suspicious. Invalid credentials are a serious "
            "warning sign because they indicate tampering."
        )
        st.graphviz_chart(DIAGRAM_C2PA, use_container_width=True)
    with st.expander("Out of band confirmation"):
        st.write(
            "The most reliable defense. The verifier ends the session and contacts the "
            "person through a separate channel that the attacker does not control, using "
            "a number from a trusted directory, never one supplied by the caller. A one "
            "time challenge code proves both sides are on the same verified line."
        )
        st.graphviz_chart(DIAGRAM_OOB, use_container_width=True)
    with st.expander("Liveness and artifact detection"):
        st.write(
            "Liveness tests ask whether a real human is present right now: random phrase "
            "challenges for voice, and head turns, blink patterns, lip sync and depth cues "
            "for video. Artifact detectors look for traces of synthesis such as spectral "
            "gaps in audio or blending seams in video. In production these scores come "
            "from accredited detection models; in this prototype they are inputs."
        )
    with st.expander("Recruiting and applicant screening"):
        st.write(
            "Fraudulent applicants use real time face swaps and voice clones in remote "
            "interviews to gain insider access. The same engine scores interviews, with "
            "extra steps for live challenges, ID document matching and reference checks "
            "through trusted contacts."
        )
        st.graphviz_chart(DIAGRAM_SCREENING, use_container_width=True)

    st.markdown("#### Field dictionary")
    st.dataframe(
        pd.DataFrame(FIELD_DICTIONARY,
                     columns=["Field", "Type", "Meaning or allowed values",
                              "Relevance to the application"]),
        use_container_width=True, hide_index=True,
    )

    st.markdown("#### Calculations and formulas")
    st.graphviz_chart(DIAGRAM_SCORING, use_container_width=True)

    st.markdown("**Step 1. Convert every signal into a risk value between 0 and 1**")
    st.latex(r"r_{prov} = \begin{cases}0.0 & \text{Valid}\\0.6 & \text{Missing}\\"
             r"1.0 & \text{Invalid}\end{cases}\qquad "
             r"r_{oob} = \begin{cases}0.0 & \text{Confirmed}\\0.7 & \text{Not attempted}\\"
             r"1.0 & \text{Failed}\end{cases}")
    st.latex(r"r_{live} = 1 - \text{mean}(\text{voice liveness},\ \text{face liveness})")
    st.latex(r"r_{art} = \text{artifact score}\qquad r_{meta} = 1 - \text{metadata consistency}"
             r"\qquad r_{beh} = \text{behavior anomaly}")
    st.latex(r"r_{cid} = \begin{cases}0 & \text{caller ID matches}\\1 & \text{otherwise}\end{cases}")
    st.write(
        "Face liveness is ignored for voice calls. If no liveness value exists, the "
        "liveness risk is set to 0.5, meaning unknown. Blank numeric values also default "
        "to 0.5 so that missing evidence is never treated as safe."
    )

    st.markdown("**Step 2. Weighted base score**")
    st.latex(r"\text{Base} = 100 \times \sum_{i} w_i \, r_i \qquad \sum_i w_i = 1")
    st.dataframe(
        pd.DataFrame({"Component": [k.replace("_", " ").title() for k in WEIGHTS],
                      "Weight": list(WEIGHTS.values()),
                      "Maximum points": [100 * w for w in WEIGHTS.values()]}),
        hide_index=True, use_container_width=True,
    )
    st.write(
        "Out of band confirmation carries the largest weight because it is the hardest "
        "signal for an attacker to fake. Caller ID carries the smallest weight because "
        "numbers are easy to spoof."
    )

    st.markdown("**Step 3. Impact multiplier for consequence and pressure**")
    st.latex(r"M = F_{request} + 0.03 \times (\text{urgency} - 1)")
    st.latex(r"\text{Adjusted} = \min(100,\ \text{Base} \times M)")
    st.dataframe(pd.DataFrame({"Request type": list(REQUEST_FACTOR),
                               "Factor": list(REQUEST_FACTOR.values())}),
                 hide_index=True, use_container_width=True)

    st.markdown("**Step 4. Hard rules**")
    st.write(
        "Invalid credentials raise the score to at least 70. A failed callback raises it "
        "to at least 80. A confirmed callback together with valid credentials caps the "
        "score at 40, so strong independent proof cannot be outvoted by a noisy detector."
    )

    st.markdown("**Step 5. Decision bands**")
    st.graphviz_chart(DIAGRAM_DECISION, use_container_width=True)

    st.markdown("**Evidence completeness**")
    st.latex(r"\text{Completeness} = \frac{\text{signals actually observed}}{7}")
    st.write(
        "A low score with low completeness is weak assurance. Analysts should gather "
        "more evidence before trusting it."
    )

    st.markdown("**Model quality metrics (only when ground truth labels exist)**")
    st.latex(r"\text{Precision} = \frac{TP}{TP + FP}\qquad "
             r"\text{Recall} = \frac{TP}{TP + FN}\qquad "
             r"F_1 = \frac{2PR}{P + R}")
    st.latex(r"\text{Accuracy} = \frac{TP + TN}{TP + FP + TN + FN}\qquad "
             r"\text{FPR} = \frac{FP}{FP + TN}")
    st.write(
        "TP are deepfakes that were flagged, FP are genuine cases flagged by mistake, "
        "TN are genuine cases correctly passed, and FN are deepfakes that slipped "
        "through. For security use, recall matters most because a missed deepfake is "
        "costlier than an extra callback."
    )


def tab_data():
    st.subheader("Choose a data source")
    source = st.radio("Data source", ["Generate synthetic data", "Upload real case data (CSV)"],
                      horizontal=True)
    if source == "Generate synthetic data":
        c1, c2, c3 = st.columns(3)
        n_cases = c1.number_input("Number of cases", 10, 5000, 200, step=10,
                                  help="How many synthetic calls, media items or interviews to create")
        rate = c2.slider("Share of deepfake attempts", 0.0, 1.0, 0.30, 0.05,
                         help="Fraction of cases generated from the attacker distributions")
        seed = c3.number_input("Random seed", 0, 99999, 7,
                               help="Same seed gives the same data, which makes demos repeatable")
        if st.button("Generate synthetic data", type="primary"):
            st.session_state["cases"] = generate_synthetic(int(n_cases), float(rate), int(seed))
            st.session_state["data_source"] = f"Synthetic ({int(n_cases)} cases, seed {int(seed)})"
            st.success("Synthetic data generated.")
    else:
        st.write("Upload a CSV with the columns listed in the field dictionary. Missing "
                 "columns are filled with cautious defaults and reported below.")
        template = generate_synthetic(3, 0.33, 1).drop(columns=["ground_truth"])
        st.download_button("Download CSV template", template.to_csv(index=False).encode(),
                           "case_template.csv", "text/csv")
        uploaded = st.file_uploader("Upload case data", type=["csv"])
        if uploaded is not None:
            try:
                raw = pd.read_csv(uploaded)
                cleaned, missing = clean_uploaded_cases(raw)
                st.session_state["cases"] = cleaned
                st.session_state["data_source"] = f"Uploaded file {uploaded.name}"
                st.success(f"Loaded {len(cleaned)} cases from {uploaded.name}.")
                if missing:
                    st.warning("Columns filled with defaults: " + ", ".join(missing))
            except Exception as error:
                st.error(f"Could not read the file: {error}")

    st.caption(f"Current data: {st.session_state['data_source']}")
    st.dataframe(st.session_state["cases"], use_container_width=True, height=320)


def tab_single_case():
    st.subheader("Verify a single call, media item or interview")
    c2pa_default = st.session_state.get("media_c2pa") or "Missing"
    with st.form("single_case"):
        a, b, c = st.columns(3)
        case_id = a.text_input("Case ID", "LIVE001")
        identity = b.text_input("Claimed identity", "Col. Jordan Ellis")
        role = c.selectbox("Claimed role", ROLES)
        channel = a.selectbox("Channel", CHANNELS, index=1)
        request = b.selectbox("Request type", REQUEST_TYPES, index=3)
        urgency = c.slider("Urgency level", 1, 5, 4)
        c2pa_state = a.selectbox("C2PA status", C2PA_STATES,
                                 index=C2PA_STATES.index(c2pa_default))
        oob_state = b.selectbox("Out of band status", OOB_STATES, index=1)
        caller = c.selectbox("Caller ID matches directory", ["No", "Yes"])
        voice = a.slider("Voice liveness", 0.0, 1.0, 0.45, 0.01)
        face = b.slider("Face liveness", 0.0, 1.0, 0.40, 0.01)
        artifact = c.slider("Artifact score", 0.0, 1.0, 0.62, 0.01)
        metadata = a.slider("Metadata consistency", 0.0, 1.0, 0.50, 0.01)
        behavior = b.slider("Behavior anomaly", 0.0, 1.0, 0.75, 0.01)
        submitted = st.form_submit_button("Score this case", type="primary")

    row = {"case_id": case_id, "claimed_identity": identity, "claimed_role": role,
           "channel": channel, "request_type": request, "urgency_level": urgency,
           "c2pa_status": c2pa_state, "oob_status": oob_state, "caller_id_match": caller,
           "voice_liveness": voice, "face_liveness": face, "artifact_score": artifact,
           "metadata_consistency": metadata, "behavior_anomaly": behavior}
    result = score_case(row)

    left, right = st.columns([1, 2])
    with left:
        show_decision_card(result)
        st.metric("Evidence completeness", f"{result['completeness']:.0%}")
    with right:
        contribution_chart(result)

    st.markdown("**Worked calculation for this case**")
    lines = []
    for k, v in result["components"].items():
        lines.append(f"{k.replace('_', ' ')}: risk {v:.2f} times weight {WEIGHTS[k]:.2f} "
                     f"times 100 equals {result['contributions'][k]:.1f}")
    lines.append(f"Base score equals {result['base_score']:.1f}")
    lines.append(f"Multiplier equals {REQUEST_FACTOR[request]:.2f} plus 0.03 times "
                 f"{urgency - 1} equals {result['multiplier']:.2f}")
    lines.append(f"Adjusted score equals {result['adjusted_score']:.1f}")
    for rule in result["rules"]:
        lines.append(f"Rule applied: {rule}")
    lines.append(f"Final score equals {result['final_score']:.1f}, decision {result['decision']}")
    st.code("\n".join(lines), language=None)

    if submitted:
        new = pd.DataFrame([row])
        st.session_state["cases"] = pd.concat([st.session_state["cases"], new],
                                              ignore_index=True)
        st.success(f"Case {case_id} added to the current data set.")


def tab_dashboard():
    st.subheader("Batch results and dashboard")
    scored = score_frame(st.session_state["cases"])
    st.session_state["scored"] = scored

    counts = scored["decision"].value_counts()
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Cases", len(scored))
    k2.metric("Proceed", int(counts.get("Proceed", 0)))
    k3.metric("Hold and verify", int(counts.get("Hold and verify", 0)))
    k4.metric("Block and escalate", int(counts.get("Block and escalate", 0)))

    c1, c2 = st.columns(2)
    with c1:
        hist = alt.Chart(scored).mark_bar().encode(
            x=alt.X("risk_score:Q", bin=alt.Bin(step=5), title="Risk score"),
            y=alt.Y("count():Q", title="Cases"),
            color=alt.Color("decision:N", scale=alt.Scale(
                domain=["Proceed", "Hold and verify", "Block and escalate"],
                range=["#2E7D32", "#F9A825", "#C62828"]), title="Decision"),
        ).properties(height=280, title="Risk score distribution")
        st.altair_chart(hist, use_container_width=True)
    with c2:
        by_role = alt.Chart(scored).mark_bar().encode(
            x=alt.X("claimed_role:N", title="Claimed role"),
            y=alt.Y("mean(risk_score):Q", title="Average risk score"),
            color=alt.value("#1565C0"),
        ).properties(height=280, title="Average risk by claimed role")
        st.altair_chart(by_role, use_container_width=True)

    threshold = st.slider("Flag threshold used for quality metrics", 0, 100,
                          PROCEED_BELOW, help="Cases at or above this score count as flagged")
    metrics = evaluation_metrics(scored, threshold)
    if metrics:
        st.markdown("**Detection quality against ground truth labels**")
        m = st.columns(5)
        m[0].metric("Precision", f"{metrics['Precision']:.2f}")
        m[1].metric("Recall", f"{metrics['Recall']:.2f}")
        m[2].metric("F1", f"{metrics['F1']:.2f}")
        m[3].metric("Accuracy", f"{metrics['Accuracy']:.2f}")
        m[4].metric("False positive rate", f"{metrics['False positive rate']:.2f}")
        st.dataframe(pd.DataFrame(
            [[metrics["TP"], metrics["FN"]], [metrics["FP"], metrics["TN"]]],
            index=["Actual deepfake", "Actual genuine"],
            columns=["Flagged", "Not flagged"]), use_container_width=False)
    else:
        st.info("Quality metrics appear when the data has a ground_truth column.")

    decision_filter = st.multiselect("Show decisions",
                                     ["Proceed", "Hold and verify", "Block and escalate"],
                                     default=["Hold and verify", "Block and escalate"])
    view = scored[scored["decision"].isin(decision_filter)].sort_values(
        "risk_score", ascending=False)
    st.dataframe(view, use_container_width=True, height=360)


def tab_media():
    st.subheader("Media provenance check")
    st.write("Upload an image, audio or video file. The app fingerprints it, checks for "
             "C2PA content credentials and scans metadata for AI generator markers.")
    if not HAVE_C2PA:
        st.info("The c2pa-python library is not installed, so manifests are detected but "
                "not cryptographically validated. Install it with pip install c2pa-python.")
    uploaded = st.file_uploader("Upload media", type=["jpg", "jpeg", "png", "webp", "heic",
                                                      "mp4", "mov", "wav", "mp3", "m4a"])
    if uploaded is not None:
        report = inspect_media(uploaded)
        a, b = st.columns(2)
        a.metric("C2PA status", report["c2pa_status"])
        b.metric("AI generator markers", len(report["ai_markers"]))
        st.json(report)
        if report["ai_markers"]:
            st.warning("Metadata names a generative tool: " + ", ".join(report["ai_markers"]))
        if st.button("Use this C2PA status in the single case form"):
            st.session_state["media_c2pa"] = report["c2pa_status"]
            st.success("Saved. Open the Single case tab to continue.")


def tab_oob():
    st.subheader("Out of band confirmation workflow")
    st.graphviz_chart(DIAGRAM_OOB, use_container_width=True)
    with st.form("oob"):
        a, b = st.columns(2)
        case_id = a.text_input("Case ID", "LIVE001")
        identity = b.text_input("Person to confirm", "Col. Jordan Ellis")
        directory_number = a.text_input("Number from trusted directory",
                                        help="Never use a number supplied by the caller")
        method = b.selectbox("Channel used", ["Directory phone callback", "In person",
                                              "Secure messaging", "Chain of command relay"])
        code = st.session_state.setdefault("challenge_code", secrets.token_hex(3).upper())
        st.text_input("One time challenge code to read aloud", code, disabled=True)
        outcome = st.radio("Outcome", ["Confirmed", "Failed"], horizontal=True)
        notes = st.text_area("Notes")
        logged = st.form_submit_button("Log result", type="primary")
    if logged:
        st.session_state["oob_log"].append({
            "time": f"{datetime.datetime.now():%Y-%m-%d %H:%M}", "case_id": case_id,
            "person": identity, "directory_number": directory_number, "method": method,
            "challenge_code": code, "outcome": outcome, "notes": notes})
        cases = st.session_state["cases"]
        match = cases["case_id"].astype(str) == case_id
        if match.any():
            st.session_state["cases"].loc[match, "oob_status"] = outcome
            st.success(f"Case {case_id} updated to {outcome}.")
        else:
            st.info("Result logged. No matching case ID in the current data.")
        st.session_state["challenge_code"] = secrets.token_hex(3).upper()
    if st.session_state["oob_log"]:
        st.dataframe(pd.DataFrame(st.session_state["oob_log"]), use_container_width=True)


def tab_reports():
    st.subheader("Export results")
    scored = st.session_state.get("scored")
    if scored is None:
        scored = score_frame(st.session_state["cases"])
    c1, c2, c3, c4 = st.columns(4)
    c1.download_button("Download CSV", scored.to_csv(index=False).encode(),
                       "verification_results.csv", "text/csv")
    c2.download_button("Download text", export_txt(scored), "verification_results.txt",
                       "text/plain")
    if HAVE_DOCX:
        c3.download_button("Download Word", export_docx(scored), "verification_results.docx",
                           "application/vnd.openxmlformats-officedocument."
                           "wordprocessingml.document")
    if HAVE_FPDF:
        c4.download_button("Download PDF", export_pdf(scored), "verification_results.pdf",
                           "application/pdf")

    st.subheader("View an existing result file")
    uploaded = st.file_uploader("Upload a PDF, Word, text or CSV result file",
                                type=["pdf", "docx", "txt", "csv"], key="report_upload")
    if uploaded is not None:
        kind, content = read_uploaded_document(uploaded)
        if kind == "table":
            st.dataframe(content, use_container_width=True)
            if "risk_score" in content.columns:
                st.bar_chart(content["risk_score"])
        elif kind == "docx":
            text, tables = content
            st.text_area("Document text", text, height=220)
            for table in tables:
                st.dataframe(table, use_container_width=True)
        else:
            st.text_area("File contents", content, height=360)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    st.set_page_config(page_title=APP_TITLE, layout="wide")
    init_state()
    render_header()

    with st.sidebar:
        st.markdown("### Session")
        st.write(f"Data: {st.session_state['data_source']}")
        st.write(f"Cases loaded: {len(st.session_state['cases'])}")
        st.markdown("### Decision bands")
        st.write(f"Proceed: below {PROCEED_BELOW}")
        st.write(f"Hold and verify: {PROCEED_BELOW} to {BLOCK_AT_OR_ABOVE - 1}")
        st.write(f"Block and escalate: {BLOCK_AT_OR_ABOVE} and above")
        st.caption("Prototype for decision support. Detection scores are inputs from "
                   "accredited models in production.")

    tabs = st.tabs(["Guide and concepts", "Data", "Single case", "Dashboard",
                    "Media provenance", "Out of band", "Reports"])
    with tabs[0]:
        tab_guide()
    with tabs[1]:
        tab_data()
    with tabs[2]:
        tab_single_case()
    with tabs[3]:
        tab_dashboard()
    with tabs[4]:
        tab_media()
    with tabs[5]:
        tab_oob()
    with tabs[6]:
        tab_reports()


if __name__ == "__main__":
    main()