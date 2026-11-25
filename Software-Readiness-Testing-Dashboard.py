

# Continuous Software Test and Evaluation Readiness Dashboard
# Developed by Randy Singh from Kalsnet (KNet) Consulting Group

# Purpose
    # Software can now be fielded faster than it can be objectively assessed.
    # This dashboard turns continuous test, security scan, performance and
    # stability evidence into one explainable readiness score for each release,
    # scales the remaining risk by mission criticality, applies hard release
    # gates and recommends Approve, Conditional approval or Not ready.


# Important note
    # This is a decision support prototype. Weights, thresholds and gates are
    # configurable starting points and must be tuned and accredited by the
    # responsible test and evaluation authority before operational use.


import io
import json
import math
import datetime
import xml.etree.ElementTree as ET

import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

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


# --------------------------------------------------------------------------
# Constants and model parameters
# --------------------------------------------------------------------------

APP_TITLE = "Continuous Software Test and Evaluation Readiness Dashboard"
APP_SUBTITLE = "Developed by Randy Singh from Kalsnet (KNet) Consulting Group"

CRITICALITY = ["Low", "Moderate", "High", "Critical"]
ENVIRONMENTS = ["Development", "Test", "Staging", "Operational"]

# Pillar weights for the overall readiness score. They add up to 1.0
PILLAR_WEIGHTS = {"test": 0.35, "security": 0.30, "performance": 0.15, "stability": 0.20}

# Test quality sub weights
W_PASS = 0.50
W_COVERAGE = 0.30
W_TRACE = 0.20
SKIP_PENALTY = 0.50

# Security model
SEVERITY_POINTS = {"critical": 10.0, "high": 5.0, "medium": 1.0, "low": 0.2}
SECURITY_SCALE = 25.0
SBOM_PENALTY = 10.0
UNSIGNED_PENALTY = 10.0

# Stability model
CHANGE_SIZE_REFERENCE = 50000.0
CHANGE_SIZE_WEIGHT = 0.30

# Mission criticality settings
CRITICALITY_FACTOR = {"Low": 0.6, "Moderate": 0.8, "High": 1.0, "Critical": 1.2}
REQUIRED_READINESS = {"Low": 60, "Moderate": 70, "High": 80, "Critical": 85}
THREAD_STEP = 0.05
CONDITIONAL_MARGIN = 10

# Hard gates
MIN_PASS_RATE = 0.90
MIN_COVERAGE_CRITICAL = 0.60

FIELD_DICTIONARY = [
    ("release_id", "Text", "Unique ID of the release candidate",
     "Links all evidence and the decision to one build"),
    ("system_name", "Text", "Name of the software system",
     "Groups releases so trends can be tracked per system"),
    ("version", "Text", "Version label of the build", "Identifies exactly what was assessed"),
    ("release_date", "Date", "Date the candidate was submitted",
     "Used for trend charts and assessment cycle time"),
    ("mission_criticality", "Category", ", ".join(CRITICALITY),
     "Sets the required readiness bar and scales mission impact"),
    ("target_environment", "Category", ", ".join(ENVIRONMENTS),
     "Where the release will run; operational fielding needs the strongest evidence"),
    ("mission_threads", "Integer 1 or more", "Number of mission threads the software supports",
     "More threads means a defect can affect more operations"),
    ("tests_passed", "Integer", "Automated tests that passed", "Core evidence of correct behavior"),
    ("tests_failed", "Integer", "Automated tests that failed or errored",
     "Direct evidence of defects in the candidate"),
    ("tests_skipped", "Integer", "Tests that did not run",
     "Skipped tests are untested risk, so they reduce the test score"),
    ("code_coverage", "Number 0 to 1", "Share of code executed by the tests",
     "Low coverage means passing tests say little about untested code"),
    ("requirements_traced", "Number 0 to 1", "Share of requirements linked to a passing test",
     "Connects testing to what the mission actually needs"),
    ("vuln_critical", "Integer", "Critical findings from security scans",
     "Exploitable weaknesses; any critical finding blocks high criticality releases"),
    ("vuln_high", "Integer", "High severity findings", "Serious weaknesses that need fixes or waivers"),
    ("vuln_medium", "Integer", "Medium severity findings", "Moderate weaknesses"),
    ("vuln_low", "Integer", "Low severity findings", "Minor weaknesses, small effect on score"),
    ("stig_compliance", "Number 0 to 1", "Share of security configuration checks passed",
     "Measures hardening against the required security baseline"),
    ("sbom_complete", "Yes or No", "Is a complete software bill of materials provided",
     "Needed to track third party components and supply chain risk"),
    ("artifact_signed", "Yes or No", "Is the build artifact cryptographically signed",
     "Proves the fielded build is the one that was tested"),
    ("latency_p95_ms", "Number", "95th percentile response time measured in load tests",
     "Shows how the system performs for nearly all users under load"),
    ("latency_requirement_ms", "Number", "Required maximum response time",
     "The performance threshold from the requirements"),
    ("change_failure_rate", "Number 0 to 1", "Share of recent deployments that caused a failure",
     "Historical stability of the delivery pipeline"),
    ("lines_changed", "Integer", "Lines of code changed since the last approved release",
     "Bigger changes carry more risk of undiscovered defects"),
    ("field_outcome", "Optional label", "Incident or No incident after fielding",
     "Only in historical or test data, used to validate the model"),
]

NUMERIC_COLUMNS = ["mission_threads", "tests_passed", "tests_failed", "tests_skipped",
                   "code_coverage", "requirements_traced", "vuln_critical", "vuln_high",
                   "vuln_medium", "vuln_low", "stig_compliance", "latency_p95_ms",
                   "latency_requirement_ms", "change_failure_rate", "lines_changed"]

DEFAULTS = {
    "system_name": "Unknown system", "version": "1.0.0", "mission_criticality": "High",
    "target_environment": "Operational", "mission_threads": 1, "tests_passed": 0,
    "tests_failed": 0, "tests_skipped": 0, "code_coverage": 0.0,
    "requirements_traced": 0.0, "vuln_critical": 0, "vuln_high": 0, "vuln_medium": 0,
    "vuln_low": 0, "stig_compliance": 0.0, "sbom_complete": "No", "artifact_signed": "No",
    "latency_p95_ms": 1000.0, "latency_requirement_ms": 500.0,
    "change_failure_rate": 0.5, "lines_changed": 10000,
}


# --------------------------------------------------------------------------
# Scoring engine
# --------------------------------------------------------------------------

def num(value, default=0.0):
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    if math.isnan(number):
        return default
    return number


def clip(value, low=0.0, high=1.0):
    return max(low, min(high, value))


def yes(value):
    if isinstance(value, (bool, np.bool_)):
        return bool(value)
    return str(value).strip().lower() in ("yes", "true", "1", "y")


def score_release(row):
    """Score one release. Returns every intermediate value for transparency."""
    passed = max(0.0, num(row.get("tests_passed")))
    failed = max(0.0, num(row.get("tests_failed")))
    skipped = max(0.0, num(row.get("tests_skipped")))
    executed = passed + failed
    total = executed + skipped
    pass_rate = passed / executed if executed else 0.0
    skip_ratio = skipped / total if total else 1.0
    coverage = clip(num(row.get("code_coverage")))
    trace = clip(num(row.get("requirements_traced")))

    # Pillar 1: test quality
    test_raw = W_PASS * pass_rate + W_COVERAGE * coverage + W_TRACE * trace
    test_score = 100.0 * test_raw * (1.0 - SKIP_PENALTY * skip_ratio)

    # Pillar 2: security
    crit = max(0.0, num(row.get("vuln_critical")))
    high = max(0.0, num(row.get("vuln_high")))
    med = max(0.0, num(row.get("vuln_medium")))
    low = max(0.0, num(row.get("vuln_low")))
    weighted_vulns = (SEVERITY_POINTS["critical"] * crit + SEVERITY_POINTS["high"] * high
                      + SEVERITY_POINTS["medium"] * med + SEVERITY_POINTS["low"] * low)
    vuln_score = 100.0 * math.exp(-weighted_vulns / SECURITY_SCALE)
    stig = clip(num(row.get("stig_compliance")))
    security_score = 0.8 * vuln_score + 20.0 * stig
    sbom = yes(row.get("sbom_complete"))
    signed = yes(row.get("artifact_signed"))
    if not sbom:
        security_score -= SBOM_PENALTY
    if not signed:
        security_score -= UNSIGNED_PENALTY
    security_score = clip(security_score, 0.0, 100.0)

    # Pillar 3: performance
    latency = max(1.0, num(row.get("latency_p95_ms"), 1000.0))
    requirement = max(1.0, num(row.get("latency_requirement_ms"), 500.0))
    performance_score = 100.0 * min(1.0, requirement / latency)

    # Pillar 4: stability
    cfr = clip(num(row.get("change_failure_rate"), 0.5))
    lines = max(0.0, num(row.get("lines_changed")))
    change_risk = min(1.0, lines / CHANGE_SIZE_REFERENCE)
    stability_score = 100.0 * (1.0 - cfr) * (1.0 - CHANGE_SIZE_WEIGHT * change_risk)

    pillars = {"test": test_score, "security": security_score,
               "performance": performance_score, "stability": stability_score}
    readiness = sum(PILLAR_WEIGHTS[k] * v for k, v in pillars.items())

    criticality = str(row.get("mission_criticality", "High"))
    if criticality not in CRITICALITY_FACTOR:
        criticality = "High"
    threads = max(1, int(num(row.get("mission_threads"), 1)))
    impact_factor = CRITICALITY_FACTOR[criticality] * (1.0 + THREAD_STEP * (threads - 1))
    mission_risk = min(100.0, (100.0 - readiness) * impact_factor)
    required = REQUIRED_READINESS[criticality]

    gates = []
    if crit > 0 and criticality in ("High", "Critical"):
        gates.append("Open critical vulnerability on a high or critical system")
    if executed and pass_rate < MIN_PASS_RATE:
        gates.append("Test pass rate below 90 percent")
    if executed == 0:
        gates.append("No executed tests")
    if criticality == "Critical" and coverage < MIN_COVERAGE_CRITICAL:
        gates.append("Coverage below 60 percent on a critical system")
    if str(row.get("target_environment")) == "Operational" and not signed:
        gates.append("Unsigned artifact for operational fielding")

    if readiness >= required and not gates:
        decision = "Approve"
    elif readiness >= required - CONDITIONAL_MARGIN and len(gates) <= 1 and \
            not any("critical vulnerability" in g for g in gates):
        decision = "Conditional approval"
    else:
        decision = "Not ready"

    return {
        "pass_rate": pass_rate, "skip_ratio": skip_ratio, "test_raw": test_raw,
        "weighted_vulns": weighted_vulns, "vuln_score": vuln_score,
        "change_risk": change_risk, "pillars": pillars, "readiness": readiness,
        "impact_factor": impact_factor, "mission_risk": mission_risk,
        "required": required, "gates": gates, "decision": decision,
    }


def score_frame(frame):
    results = [score_release(r) for _, r in frame.iterrows()]
    out = frame.copy()
    out["test_score"] = [round(r["pillars"]["test"], 1) for r in results]
    out["security_score"] = [round(r["pillars"]["security"], 1) for r in results]
    out["performance_score"] = [round(r["pillars"]["performance"], 1) for r in results]
    out["stability_score"] = [round(r["pillars"]["stability"], 1) for r in results]
    out["readiness_score"] = [round(r["readiness"], 1) for r in results]
    out["required_readiness"] = [r["required"] for r in results]
    out["mission_risk"] = [round(r["mission_risk"], 1) for r in results]
    out["gates_failed"] = ["; ".join(r["gates"]) for r in results]
    out["decision"] = [r["decision"] for r in results]
    return out


def validation_metrics(scored):
    """Compare decisions with real field outcomes when that label exists."""
    if "field_outcome" not in scored.columns:
        return None
    outcome = scored["field_outcome"].astype(str).str.strip().str.lower()
    known = outcome.isin(["incident", "no incident"])
    if not known.any():
        return None
    data = scored[known].copy()
    data["incident"] = outcome[known] == "incident"
    approved = data["decision"] == "Approve"
    blocked = data["decision"] == "Not ready"
    rate_approved = data.loc[approved, "incident"].mean() if approved.any() else 0.0
    rate_blocked = data.loc[blocked, "incident"].mean() if blocked.any() else 0.0
    incidents = data["incident"].sum()
    caught = data.loc[~approved, "incident"].sum()
    capture = caught / incidents if incidents else 0.0
    return {"Incident rate when approved": rate_approved,
            "Incident rate when not ready": rate_blocked,
            "Incident capture rate": capture,
            "Releases with outcomes": int(len(data))}


# --------------------------------------------------------------------------
# Synthetic data, uploads and evidence parsers
# --------------------------------------------------------------------------

SYSTEMS = ["Mission Planning Suite", "Logistics Tracker", "Maintenance Predictor",
           "Secure Messaging Gateway", "Sensor Data Fusion", "Personnel Readiness Portal"]


def generate_synthetic(n_releases, weak_share, seed):
    rng = np.random.default_rng(seed)
    start = datetime.date(2026, 1, 5)
    rows = []
    for i in range(n_releases):
        weak = rng.random() < weak_share
        system = SYSTEMS[i % len(SYSTEMS)]
        crit = rng.choice(CRITICALITY, p=[0.15, 0.30, 0.35, 0.20])
        tests_total = int(rng.integers(300, 4000))
        if weak:
            fail_rate = rng.beta(2, 18)
            skip_rate = rng.beta(2, 12)
            coverage = rng.beta(4, 5)
            trace = rng.beta(4, 4)
            vc = int(rng.poisson(0.8))
            vh = int(rng.poisson(3))
            vm = int(rng.poisson(9))
            vl = int(rng.poisson(15))
            stig = rng.beta(5, 3)
            sbom = rng.random() < 0.5
            signed = rng.random() < 0.6
            req = float(rng.choice([200, 300, 500]))
            lat = req * rng.uniform(0.8, 1.9)
            cfr = rng.beta(3, 7)
            lines = int(rng.integers(8000, 70000))
        else:
            fail_rate = rng.beta(1, 120)
            skip_rate = rng.beta(1, 60)
            coverage = rng.beta(9, 2.5)
            trace = rng.beta(10, 2)
            vc = 0
            vh = int(rng.poisson(0.4))
            vm = int(rng.poisson(2))
            vl = int(rng.poisson(5))
            stig = rng.beta(14, 1.5)
            sbom = rng.random() < 0.95
            signed = rng.random() < 0.97
            req = float(rng.choice([200, 300, 500]))
            lat = req * rng.uniform(0.5, 1.05)
            cfr = rng.beta(1.2, 12)
            lines = int(rng.integers(500, 25000))
        skipped = int(tests_total * skip_rate)
        failed = int((tests_total - skipped) * fail_rate)
        passed = tests_total - skipped - failed
        incident_prob = 0.45 if weak else 0.06
        rows.append({
            "release_id": f"REL{2000 + i}",
            "system_name": system,
            "version": f"{1 + i // 12}.{i % 12}.{int(rng.integers(0, 9))}",
            "release_date": str(start + datetime.timedelta(days=int(i * 3))),
            "mission_criticality": crit,
            "target_environment": rng.choice(ENVIRONMENTS, p=[0.10, 0.20, 0.25, 0.45]),
            "mission_threads": int(rng.integers(1, 7)),
            "tests_passed": passed, "tests_failed": failed, "tests_skipped": skipped,
            "code_coverage": round(float(coverage), 3),
            "requirements_traced": round(float(trace), 3),
            "vuln_critical": vc, "vuln_high": vh, "vuln_medium": vm, "vuln_low": vl,
            "stig_compliance": round(float(stig), 3),
            "sbom_complete": "Yes" if sbom else "No",
            "artifact_signed": "Yes" if signed else "No",
            "latency_p95_ms": round(float(lat), 1),
            "latency_requirement_ms": req,
            "change_failure_rate": round(float(cfr), 3),
            "lines_changed": lines,
            "field_outcome": "Incident" if rng.random() < incident_prob else "No incident",
        })
    return pd.DataFrame(rows)


def clean_uploaded(frame):
    frame = frame.copy()
    frame.columns = [str(c).strip().lower().replace(" ", "_") for c in frame.columns]
    missing = []
    if "release_id" not in frame.columns:
        frame["release_id"] = [f"UPLOAD{i + 1}" for i in range(len(frame))]
        missing.append("release_id")
    if "release_date" not in frame.columns:
        frame["release_date"] = str(datetime.date.today())
        missing.append("release_date")
    for col, value in DEFAULTS.items():
        if col not in frame.columns:
            frame[col] = value
            missing.append(col)
    for col in NUMERIC_COLUMNS:
        frame[col] = pd.to_numeric(frame[col], errors="coerce").fillna(DEFAULTS[col])
    for col in ["code_coverage", "requirements_traced", "stig_compliance",
                "change_failure_rate"]:
        frame[col] = frame[col].clip(0, 1)
    lookup = {c.lower(): c for c in CRITICALITY}
    frame["mission_criticality"] = frame["mission_criticality"].astype(str).str.strip() \
        .str.lower().map(lookup).fillna("High")
    return frame, missing


def parse_junit(data):
    """Count passed, failed and skipped test cases in a JUnit XML report."""
    root = ET.fromstring(data)
    passed = failed = skipped = 0
    for case in root.iter("testcase"):
        tags = {child.tag for child in case}
        if "failure" in tags or "error" in tags:
            failed += 1
        elif "skipped" in tags:
            skipped += 1
        else:
            passed += 1
    return {"tests_passed": passed, "tests_failed": failed, "tests_skipped": skipped}


def severity_from_score(score):
    if score >= 9.0:
        return "critical"
    if score >= 7.0:
        return "high"
    if score >= 4.0:
        return "medium"
    return "low"


def parse_sarif(data):
    """Count findings by severity in a SARIF security scan report."""
    report = json.loads(data)
    counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    level_map = {"error": "high", "warning": "medium", "note": "low", "none": "low"}
    for run in report.get("runs", []):
        rule_scores = {}
        driver = run.get("tool", {}).get("driver", {})
        for rule in driver.get("rules", []):
            value = rule.get("properties", {}).get("security-severity")
            if value is not None:
                rule_scores[rule.get("id")] = num(value)
        for result in run.get("results", []):
            value = result.get("properties", {}).get("security-severity")
            if value is None:
                value = rule_scores.get(result.get("ruleId"))
            if value is not None:
                counts[severity_from_score(num(value))] += 1
            else:
                counts[level_map.get(result.get("level", "warning"), "medium")] += 1
    return {f"vuln_{k}": v for k, v in counts.items()}


def parse_vuln_csv(data):
    """Count findings by severity from a scanner CSV with a severity column."""
    frame = pd.read_csv(io.BytesIO(data))
    column = next((c for c in frame.columns if c.strip().lower() == "severity"), None)
    if column is None:
        raise ValueError("The CSV needs a column named severity")
    values = frame[column].astype(str).str.strip().str.lower()
    return {f"vuln_{k}": int((values == k).sum())
            for k in ["critical", "high", "medium", "low"]}


def read_uploaded_document(uploaded):
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
        return "text", "\n\n".join(f"Page {i + 1}\n{p.extract_text() or ''}"
                                   for i, p in enumerate(reader.pages))
    if name.endswith(".docx"):
        if not HAVE_DOCX:
            return "text", "Install python-docx to read Word files."
        document = docx.Document(io.BytesIO(data))
        text = "\n".join(p.text for p in document.paragraphs if p.text.strip())
        tables = []
        for table in document.tables:
            grid = [[c.text for c in r.cells] for r in table.rows]
            if len(grid) > 1:
                tables.append(pd.DataFrame(grid[1:], columns=grid[0]))
        return "docx", (text, tables)
    return "text", "Unsupported file type."


# --------------------------------------------------------------------------
# Report exports
# --------------------------------------------------------------------------

REPORT_COLUMNS = ["release_id", "system_name", "version", "mission_criticality",
                  "readiness_score", "required_readiness", "mission_risk", "decision",
                  "gates_failed"]


def summary_lines(scored):
    counts = scored["decision"].value_counts().to_dict()
    return [
        APP_TITLE, APP_SUBTITLE,
        f"Report generated: {datetime.datetime.now():%Y-%m-%d %H:%M}", "",
        f"Releases assessed: {len(scored)}",
        f"Average readiness score: {scored['readiness_score'].mean():.1f}",
        f"Approve: {counts.get('Approve', 0)}",
        f"Conditional approval: {counts.get('Conditional approval', 0)}",
        f"Not ready: {counts.get('Not ready', 0)}",
    ]


def export_txt(scored):
    lines = summary_lines(scored) + ["", "Release results"]
    for _, r in scored.iterrows():
        lines.append(" | ".join(str(r[c]) for c in REPORT_COLUMNS))
    return "\n".join(lines).encode("utf-8")


def export_docx(scored):
    document = docx.Document()
    lines = summary_lines(scored)
    document.add_heading(lines[0], level=0)
    document.add_paragraph(lines[1])
    for line in lines[2:]:
        if line:
            document.add_paragraph(line)
    document.add_heading("Release results", level=1)
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
    pdf.set_font("Helvetica", "B", 17)
    pdf.cell(0, 10, latin(APP_TITLE), new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, latin(APP_SUBTITLE), new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", "", 11)
    for line in summary_lines(scored)[2:]:
        pdf.cell(0, 6, latin(line), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)
    widths = [20, 44, 16, 22, 20, 20, 18, 30, 87]
    headers = ["Release", "System", "Version", "Criticality", "Readiness",
               "Required", "Risk", "Decision", "Gates failed"]
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_fill_color(227, 236, 250)
    for w, h in zip(widths, headers):
        pdf.cell(w, 7, h, border=1, fill=True)
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
# Diagrams in Graphviz DOT
# --------------------------------------------------------------------------

DOT_STYLE = """
    graph [rankdir=LR, bgcolor=transparent, fontname=Helvetica, nodesep=0.35];
    node  [shape=box, style="rounded,filled", fillcolor="#E3ECFA", color="#0D47A1",
           fontname=Helvetica, fontsize=11];
    edge  [color="#0D47A1", fontname=Helvetica, fontsize=10];
"""

DIAGRAM_PIPELINE = "digraph G {" + DOT_STYLE + """
    A [label="Developer commits\\ncode change"];
    B [label="Build and sign\\nartifact, create SBOM"];
    C [label="Automated tests\\nunit, integration, system"];
    D [label="Security scans\\ncode, dependencies, config"];
    E [label="Performance and\\nload tests"];
    F [label="Delivery history\\nchange failure rate"];
    G [label="Readiness engine\\nfour pillar score", fillcolor="#BBDEFB"];
    H [label="Mission impact and\\nrelease gates", fillcolor="#BBDEFB"];
    I [label="Decision and\\nevidence report"];
    J [label="Field and\\nmonitor"];
    A -> B; B -> C; B -> D; B -> E; B -> F;
    C -> G; D -> G; E -> G; F -> G; G -> H; H -> I; I -> J;
    J -> A [style=dashed, label="feedback"];
}"""

DIAGRAM_PILLARS = "digraph G {" + DOT_STYLE + """
    T [label="Test quality\\nweight 0.35"];
    S [label="Security\\nweight 0.30"];
    P [label="Performance\\nweight 0.15"];
    R [label="Stability\\nweight 0.20"];
    X [label="Readiness score\\n0 to 100", fillcolor="#BBDEFB"];
    T -> X; S -> X; P -> X; R -> X;
}"""

DIAGRAM_DECISION = """digraph G {
    graph [rankdir=TB, bgcolor=transparent, fontname=Helvetica];
    node  [fontname=Helvetica, fontsize=11, style="rounded,filled", color="#0D47A1"];
    edge  [color="#0D47A1", fontname=Helvetica, fontsize=10];
    Q1 [shape=diamond, label="Readiness at or above\\nrequired bar and\\nno gate failed?", fillcolor="#E3ECFA"];
    Q2 [shape=diamond, label="Within 10 points,\\nat most one gate failed,\\nno critical vulnerability?", fillcolor="#E3ECFA"];
    A  [shape=box, label="Approve\\nfield the release", fillcolor="#C8E6C9"];
    C  [shape=box, label="Conditional approval\\nfix list and limited fielding", fillcolor="#FFF59D"];
    N  [shape=box, label="Not ready\\nreturn to developers", fillcolor="#FFCDD2"];
    Q1 -> A [label="Yes"]; Q1 -> Q2 [label="No"];
    Q2 -> C [label="Yes"]; Q2 -> N [label="No"];
}"""

DIAGRAM_SECURITY = "digraph G {" + DOT_STYLE + """
    V [label="Findings by severity\\ncritical, high, medium, low"];
    W [label="Weighted findings\\n10, 5, 1, 0.2 points"];
    E [label="Decay curve\\n100 times e to the\\nminus W over 25"];
    K [label="Add STIG compliance\\n0.8 times decay plus\\n20 times compliance"];
    P [label="Subtract 10 for no SBOM\\nand 10 if unsigned"];
    S [label="Security score", fillcolor="#BBDEFB"];
    V -> W -> E -> K -> P -> S;
}"""

DIAGRAM_EVIDENCE = "digraph G {" + DOT_STYLE + """
    J [label="JUnit XML\\ntest report"];
    F [label="SARIF scan or\\nscanner CSV"];
    M [label="Manual entry\\ncoverage, latency, history"];
    R [label="Release record"];
    E [label="Scoring engine", fillcolor="#BBDEFB"];
    J -> R; F -> R; M -> R; R -> E;
}"""


# --------------------------------------------------------------------------
# User interface helpers
# --------------------------------------------------------------------------

def render_header():
    st.markdown(
        f"""
        <div style="padding: 14px 20px; border-bottom: 3px solid #0D47A1;
                    margin-bottom: 18px; background-color: #F4F8FE; border-radius: 6px;">
            <div style="color: #0D47A1; font-size: 32px; font-weight: 800;
                        line-height: 1.2;">{APP_TITLE}</div>
            <div style="color: #1565C0; font-size: 24px; font-weight: 700;
                        line-height: 1.3; margin-top: 4px;">{APP_SUBTITLE}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


DECISION_COLORS = {"Approve": "#2E7D32", "Conditional approval": "#F9A825",
                   "Not ready": "#C62828"}


def show_decision_card(result):
    color = DECISION_COLORS[result["decision"]]
    st.markdown(
        f"""
        <div style="border-left: 8px solid {color}; padding: 12px 16px;
                    background-color: #FAFAFA; border-radius: 4px;">
            <div style="font-size: 15px; color: #555;">Readiness score</div>
            <div style="font-size: 40px; font-weight: 800; color: {color};">
                {result['readiness']:.1f} of 100</div>
            <div style="font-size: 15px; color: #555;">Required for this criticality:
                {result['required']}</div>
            <div style="font-size: 22px; font-weight: 700; color: {color};">
                {result['decision']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def init_state():
    if "releases" not in st.session_state:
        st.session_state["releases"] = generate_synthetic(72, 0.30, 11)
        st.session_state["data_source"] = "Synthetic (default, 72 releases)"
    if "evidence" not in st.session_state:
        st.session_state["evidence"] = {}


# --------------------------------------------------------------------------
# Tabs
# --------------------------------------------------------------------------

def tab_guide():
    st.subheader("How the dashboard works")
    st.write(
        "Modern pipelines can ship new software every day, but traditional test and "
        "evaluation reviews take weeks. This dashboard closes the gap by collecting the "
        "evidence a pipeline already produces, scoring it the same way every time, and "
        "showing exactly why a release is or is not ready. Reviewers spend their time on "
        "the exceptions instead of rebuilding the evidence by hand."
    )
    st.graphviz_chart(DIAGRAM_PIPELINE, use_container_width=True)

    st.markdown("#### Key concepts")
    with st.expander("Continuous test and evaluation", expanded=True):
        st.write(
            "Instead of one large test event before fielding, every build is tested "
            "automatically and the evidence accumulates release by release. Assessment "
            "becomes a running measurement rather than a one time gate."
        )
    with st.expander("Four evidence pillars"):
        st.write(
            "Test quality asks whether the software does what it should. Security asks "
            "whether it can be attacked. Performance asks whether it is fast enough under "
            "load. Stability asks whether the delivery process itself is reliable. Each "
            "pillar is scored from 0 to 100 and combined with weights."
        )
        st.graphviz_chart(DIAGRAM_PILLARS, use_container_width=True)
    with st.expander("Security scanning, SBOM and signing"):
        st.write(
            "Static analysis and dependency scans report weaknesses by severity. A "
            "software bill of materials lists every third party component so new "
            "vulnerabilities can be traced. A signed artifact proves that the build in the "
            "field is the exact build that was tested. STIG compliance measures security "
            "hardening against the required configuration baseline."
        )
        st.graphviz_chart(DIAGRAM_SECURITY, use_container_width=True)
    with st.expander("Mission impact"):
        st.write(
            "The same defect matters more in a critical targeting or logistics system than "
            "in an internal portal. Mission criticality raises the readiness bar and scales "
            "the remaining risk, and the number of mission threads adds further weight."
        )
    with st.expander("Release gates"):
        st.write(
            "Some conditions block approval no matter how good the average looks, for "
            "example an open critical vulnerability on a high criticality system or an "
            "unsigned artifact headed for operational use. Gates keep a strong score in one "
            "pillar from hiding a serious problem in another."
        )
        st.graphviz_chart(DIAGRAM_DECISION, use_container_width=True)
    with st.expander("Importing real evidence"):
        st.write(
            "The Evidence import tab reads standard pipeline outputs: JUnit XML test "
            "reports, SARIF security scan reports and scanner CSV files with a severity "
            "column. Values that tools do not produce, such as coverage or latency, are "
            "entered in the release evaluation form."
        )
        st.graphviz_chart(DIAGRAM_EVIDENCE, use_container_width=True)

    st.markdown("#### Field dictionary")
    st.dataframe(pd.DataFrame(FIELD_DICTIONARY, columns=[
        "Field", "Type", "Meaning or allowed values", "Relevance to the application"]),
        use_container_width=True, hide_index=True)

    st.markdown("#### Calculations and formulas")
    st.markdown("**Pillar 1. Test quality**")
    st.latex(r"\text{pass rate} = \frac{\text{passed}}{\text{passed} + \text{failed}}"
             r"\qquad \text{skip ratio} = \frac{\text{skipped}}{\text{passed} + "
             r"\text{failed} + \text{skipped}}")
    st.latex(r"T = 100 \times (0.5\,\text{pass rate} + 0.3\,\text{coverage} + "
             r"0.2\,\text{traced}) \times (1 - 0.5\,\text{skip ratio})")
    st.write("Pass rate carries the most weight. Coverage and requirement traceability show "
             "how much of the code and of the mission needs the tests actually exercise. "
             "Skipped tests cut the score because they are risk that was never measured.")

    st.markdown("**Pillar 2. Security**")
    st.latex(r"W = 10\,c + 5\,h + 1\,m + 0.2\,l")
    st.latex(r"S = 0.8 \times 100\,e^{-W/25} + 20 \times \text{STIG} "
             r"- 10\,[\text{no SBOM}] - 10\,[\text{unsigned}]")
    st.write("c, h, m and l are counts of critical, high, medium and low findings. The "
             "exponential curve means the first serious findings cost the most points, and "
             "the score never goes below zero. One critical finding alone removes about a "
             "third of the vulnerability component.")

    st.markdown("**Pillar 3. Performance**")
    st.latex(r"P = 100 \times \min\left(1,\ \frac{\text{latency requirement}}"
             r"{\text{measured p95 latency}}\right)")
    st.write("Meeting the requirement scores 100. Being twice as slow as required scores 50.")

    st.markdown("**Pillar 4. Stability**")
    st.latex(r"\text{change risk} = \min\left(1,\ \frac{\text{lines changed}}{50000}\right)")
    st.latex(r"R = 100 \times (1 - \text{change failure rate}) \times "
             r"(1 - 0.3 \times \text{change risk})")

    st.markdown("**Overall readiness**")
    st.latex(r"\text{Readiness} = 0.35\,T + 0.30\,S + 0.15\,P + 0.20\,R")

    st.markdown("**Mission risk**")
    st.latex(r"\text{Mission risk} = \min\left(100,\ (100 - \text{Readiness}) \times "
             r"F_{crit} \times (1 + 0.05\,(\text{threads} - 1))\right)")
    st.dataframe(pd.DataFrame({
        "Criticality": CRITICALITY,
        "Factor": [CRITICALITY_FACTOR[c] for c in CRITICALITY],
        "Required readiness": [REQUIRED_READINESS[c] for c in CRITICALITY]}),
        hide_index=True, use_container_width=True)

    st.markdown("**Release gates**")
    st.write("Open critical vulnerability on a high or critical system. Pass rate below "
             "90 percent. No executed tests. Coverage below 60 percent on a critical system. "
             "Unsigned artifact for operational fielding.")

    st.markdown("**Model validation against field outcomes**")
    st.latex(r"\text{Incident capture rate} = \frac{\text{incidents in releases not approved}}"
             r"{\text{all incidents}}")
    st.write("When historical data records whether a fielded release caused an incident, "
             "the dashboard compares incident rates for approved and rejected releases. A "
             "useful model shows a much lower incident rate for approved releases.")


def tab_data():
    st.subheader("Choose a data source")
    source = st.radio("Data source", ["Generate synthetic data",
                                      "Upload real release data (CSV)"], horizontal=True)
    if source == "Generate synthetic data":
        a, b, c = st.columns(3)
        n = a.number_input("Number of releases", 10, 5000, 120, step=10,
                           help="How many release candidates to create")
        weak = b.slider("Share of weak releases", 0.0, 1.0, 0.30, 0.05,
                        help="Fraction drawn from poorer quality distributions")
        seed = c.number_input("Random seed", 0, 99999, 11,
                              help="Same seed gives the same data for repeatable demos")
        if st.button("Generate synthetic data", type="primary"):
            st.session_state["releases"] = generate_synthetic(int(n), float(weak), int(seed))
            st.session_state["data_source"] = f"Synthetic ({int(n)} releases, seed {int(seed)})"
            st.success("Synthetic data generated.")
    else:
        template = generate_synthetic(3, 0.33, 2).drop(columns=["field_outcome"])
        st.download_button("Download CSV template", template.to_csv(index=False).encode(),
                           "release_template.csv", "text/csv")
        uploaded = st.file_uploader("Upload release data", type=["csv"])
        if uploaded is not None:
            try:
                cleaned, missing = clean_uploaded(pd.read_csv(uploaded))
                st.session_state["releases"] = cleaned
                st.session_state["data_source"] = f"Uploaded file {uploaded.name}"
                st.success(f"Loaded {len(cleaned)} releases.")
                if missing:
                    st.warning("Columns filled with defaults: " + ", ".join(missing))
            except Exception as error:
                st.error(f"Could not read the file: {error}")
    st.caption(f"Current data: {st.session_state['data_source']}")
    st.dataframe(st.session_state["releases"], use_container_width=True, height=320)


def tab_evidence():
    st.subheader("Import evidence from pipeline tools")
    st.graphviz_chart(DIAGRAM_EVIDENCE, use_container_width=True)
    a, b = st.columns(2)
    with a:
        junit = st.file_uploader("JUnit XML test report", type=["xml"])
        if junit is not None:
            try:
                counts = parse_junit(junit.getvalue())
                st.session_state["evidence"].update(counts)
                st.success("Test counts imported.")
                st.json(counts)
            except Exception as error:
                st.error(f"Could not parse JUnit XML: {error}")
    with b:
        scan = st.file_uploader("Security scan (SARIF or CSV with severity column)",
                                type=["sarif", "json", "csv"])
        if scan is not None:
            try:
                if scan.name.lower().endswith(".csv"):
                    counts = parse_vuln_csv(scan.getvalue())
                else:
                    counts = parse_sarif(scan.getvalue())
                st.session_state["evidence"].update(counts)
                st.success("Vulnerability counts imported.")
                st.json(counts)
            except Exception as error:
                st.error(f"Could not parse scan: {error}")
    if st.session_state["evidence"]:
        st.info("Imported values now prefill the Release evaluation tab.")
        if st.button("Clear imported evidence"):
            st.session_state["evidence"] = {}


def tab_release():
    st.subheader("Evaluate a single release candidate")
    ev = st.session_state["evidence"]
    with st.form("release"):
        a, b, c = st.columns(3)
        release_id = a.text_input("Release ID", "REL9001")
        system = b.text_input("System name", "Mission Planning Suite")
        version = c.text_input("Version", "4.2.0")
        crit = a.selectbox("Mission criticality", CRITICALITY, index=2)
        env = b.selectbox("Target environment", ENVIRONMENTS, index=3)
        threads = c.number_input("Mission threads", 1, 50, 3)
        passed = a.number_input("Tests passed", 0, 10000000, int(ev.get("tests_passed", 1840)))
        failed = b.number_input("Tests failed", 0, 10000000, int(ev.get("tests_failed", 22)))
        skipped = c.number_input("Tests skipped", 0, 10000000, int(ev.get("tests_skipped", 40)))
        coverage = a.slider("Code coverage", 0.0, 1.0, 0.74, 0.01)
        trace = b.slider("Requirements traced", 0.0, 1.0, 0.82, 0.01)
        stig = c.slider("STIG compliance", 0.0, 1.0, 0.91, 0.01)
        vc = a.number_input("Critical findings", 0, 10000, int(ev.get("vuln_critical", 0)))
        vh = b.number_input("High findings", 0, 10000, int(ev.get("vuln_high", 2)))
        vm = c.number_input("Medium findings", 0, 10000, int(ev.get("vuln_medium", 6)))
        vl = a.number_input("Low findings", 0, 10000, int(ev.get("vuln_low", 11)))
        sbom = b.selectbox("SBOM complete", ["Yes", "No"])
        signed = c.selectbox("Artifact signed", ["Yes", "No"])
        latency = a.number_input("Measured p95 latency in ms", 1.0, 100000.0, 340.0)
        requirement = b.number_input("Latency requirement in ms", 1.0, 100000.0, 300.0)
        cfr = c.slider("Change failure rate", 0.0, 1.0, 0.12, 0.01)
        lines = a.number_input("Lines changed", 0, 10000000, 18000, step=500)
        submitted = st.form_submit_button("Assess release", type="primary")

    row = {"release_id": release_id, "system_name": system, "version": version,
           "release_date": str(datetime.date.today()), "mission_criticality": crit,
           "target_environment": env, "mission_threads": threads, "tests_passed": passed,
           "tests_failed": failed, "tests_skipped": skipped, "code_coverage": coverage,
           "requirements_traced": trace, "vuln_critical": vc, "vuln_high": vh,
           "vuln_medium": vm, "vuln_low": vl, "stig_compliance": stig,
           "sbom_complete": sbom, "artifact_signed": signed, "latency_p95_ms": latency,
           "latency_requirement_ms": requirement, "change_failure_rate": cfr,
           "lines_changed": lines}
    result = score_release(row)

    left, right = st.columns([1, 2])
    with left:
        show_decision_card(result)
        st.metric("Mission risk", f"{result['mission_risk']:.1f}")
        if result["gates"]:
            st.error("Gates failed: " + "; ".join(result["gates"]))
        else:
            st.success("All release gates passed")
    with right:
        pillars = pd.DataFrame({
            "pillar": ["Test quality", "Security", "Performance", "Stability"],
            "score": list(result["pillars"].values())})
        bars = alt.Chart(pillars).mark_bar(color="#1565C0").encode(
            x=alt.X("score:Q", scale=alt.Scale(domain=[0, 100]), title="Pillar score"),
            y=alt.Y("pillar:N", title=None, sort=None),
            tooltip=["pillar", alt.Tooltip("score:Q", format=".1f")])
        rule = alt.Chart(pd.DataFrame({"x": [result["required"]]})).mark_rule(
            color="#C62828", strokeDash=[6, 4], size=2).encode(x="x:Q")
        st.altair_chart((bars + rule).properties(height=230), use_container_width=True)
        st.caption("Red dashed line shows the required readiness for this criticality.")

    p = result["pillars"]
    lines_out = [
        f"Pass rate equals {passed} over {passed + failed} equals {result['pass_rate']:.3f}",
        f"Skip ratio equals {result['skip_ratio']:.3f}",
        f"Test score equals 100 times ({result['test_raw']:.3f}) times "
        f"(1 minus 0.5 times {result['skip_ratio']:.3f}) equals {p['test']:.1f}",
        f"Weighted findings W equals {result['weighted_vulns']:.1f}, decay part equals "
        f"{result['vuln_score']:.1f}",
        f"Security score equals {p['security']:.1f}",
        f"Performance score equals 100 times min(1, {requirement:.0f} over {latency:.0f}) "
        f"equals {p['performance']:.1f}",
        f"Stability score equals 100 times (1 minus {cfr:.2f}) times (1 minus 0.3 times "
        f"{result['change_risk']:.2f}) equals {p['stability']:.1f}",
        f"Readiness equals 0.35 times {p['test']:.1f} plus 0.30 times {p['security']:.1f} "
        f"plus 0.15 times {p['performance']:.1f} plus 0.20 times {p['stability']:.1f} "
        f"equals {result['readiness']:.1f}",
        f"Mission risk equals (100 minus {result['readiness']:.1f}) times "
        f"{result['impact_factor']:.2f} equals {result['mission_risk']:.1f}",
        f"Decision: {result['decision']}",
    ]
    st.markdown("**Worked calculation for this release**")
    st.code("\n".join(lines_out), language=None)

    if submitted:
        st.session_state["releases"] = pd.concat(
            [st.session_state["releases"], pd.DataFrame([row])], ignore_index=True)
        st.success(f"Release {release_id} added to the portfolio.")


def tab_portfolio():
    st.subheader("Portfolio dashboard")
    scored = score_frame(st.session_state["releases"])
    st.session_state["scored"] = scored
    counts = scored["decision"].value_counts()
    k = st.columns(5)
    k[0].metric("Releases", len(scored))
    k[1].metric("Approve", int(counts.get("Approve", 0)))
    k[2].metric("Conditional", int(counts.get("Conditional approval", 0)))
    k[3].metric("Not ready", int(counts.get("Not ready", 0)))
    k[4].metric("Average readiness", f"{scored['readiness_score'].mean():.1f}")

    color = alt.Color("decision:N", title="Decision", scale=alt.Scale(
        domain=list(DECISION_COLORS), range=list(DECISION_COLORS.values())))
    a, b = st.columns(2)
    with a:
        scatter = alt.Chart(scored).mark_circle(size=70, opacity=0.8).encode(
            x=alt.X("readiness_score:Q", title="Readiness score"),
            y=alt.Y("mission_risk:Q", title="Mission risk"),
            color=color,
            tooltip=["release_id", "system_name", "version", "mission_criticality",
                     "readiness_score", "mission_risk", "decision", "gates_failed"],
        ).properties(height=300, title="Readiness against mission risk")
        st.altair_chart(scatter, use_container_width=True)
    with b:
        melted = scored.groupby("system_name")[
            ["test_score", "security_score", "performance_score", "stability_score"]] \
            .mean().reset_index().melt("system_name", var_name="pillar", value_name="score")
        heat = alt.Chart(melted).mark_rect().encode(
            x=alt.X("pillar:N", title=None),
            y=alt.Y("system_name:N", title=None),
            color=alt.Color("score:Q", scale=alt.Scale(scheme="blues", domain=[0, 100]),
                            title="Average"),
            tooltip=["system_name", "pillar", alt.Tooltip("score:Q", format=".1f")],
        ).properties(height=300, title="Average pillar score by system")
        st.altair_chart(heat, use_container_width=True)

    if "release_date" in scored.columns:
        trend = scored.copy()
        trend["release_date"] = pd.to_datetime(trend["release_date"], errors="coerce")
        line = alt.Chart(trend.dropna(subset=["release_date"])).mark_line(point=True).encode(
            x=alt.X("release_date:T", title="Release date"),
            y=alt.Y("readiness_score:Q", title="Readiness score"),
            color=alt.Color("system_name:N", title="System"),
            tooltip=["release_id", "version", "readiness_score", "decision"],
        ).properties(height=280, title="Readiness trend by system")
        st.altair_chart(line, use_container_width=True)

    metrics = validation_metrics(scored)
    if metrics:
        st.markdown("**Validation against field outcomes**")
        m = st.columns(4)
        m[0].metric("Incident rate when approved",
                    f"{metrics['Incident rate when approved']:.0%}")
        m[1].metric("Incident rate when not ready",
                    f"{metrics['Incident rate when not ready']:.0%}")
        m[2].metric("Incident capture rate", f"{metrics['Incident capture rate']:.0%}")
        m[3].metric("Releases with outcomes", metrics["Releases with outcomes"])

    gate_series = scored["gates_failed"].str.split("; ").explode()
    gate_series = gate_series[gate_series.str.len() > 0]
    if len(gate_series):
        gate_counts = gate_series.value_counts().reset_index()
        gate_counts.columns = ["gate", "releases"]
        st.altair_chart(alt.Chart(gate_counts).mark_bar(color="#C62828").encode(
            x=alt.X("releases:Q", title="Releases"), y=alt.Y("gate:N", sort="-x", title=None)
        ).properties(height=200, title="Most common gate failures"), use_container_width=True)

    choice = st.multiselect("Show decisions", list(DECISION_COLORS),
                            default=["Conditional approval", "Not ready"])
    st.dataframe(scored[scored["decision"].isin(choice)].sort_values("mission_risk",
                 ascending=False), use_container_width=True, height=340)


def tab_reports():
    st.subheader("Export results")
    scored = st.session_state.get("scored")
    if scored is None:
        scored = score_frame(st.session_state["releases"])
    c = st.columns(4)
    c[0].download_button("Download CSV", scored.to_csv(index=False).encode(),
                         "te_results.csv", "text/csv")
    c[1].download_button("Download text", export_txt(scored), "te_results.txt", "text/plain")
    if HAVE_DOCX:
        c[2].download_button("Download Word", export_docx(scored), "te_results.docx",
                             "application/vnd.openxmlformats-officedocument."
                             "wordprocessingml.document")
    if HAVE_FPDF:
        c[3].download_button("Download PDF", export_pdf(scored), "te_results.pdf",
                             "application/pdf")
    st.subheader("View an existing result file")
    uploaded = st.file_uploader("Upload a PDF, Word, text or CSV result file",
                                type=["pdf", "docx", "txt", "csv"], key="report_upload")
    if uploaded is not None:
        kind, content = read_uploaded_document(uploaded)
        if kind == "table":
            st.dataframe(content, use_container_width=True)
            if "readiness_score" in content.columns:
                st.bar_chart(content["readiness_score"])
        elif kind == "docx":
            text, tables = content
            st.text_area("Document text", text, height=220)
            for table in tables:
                st.dataframe(table, use_container_width=True)
        else:
            st.text_area("File contents", content, height=360)


def main():
    st.set_page_config(page_title=APP_TITLE, layout="wide")
    init_state()
    render_header()
    with st.sidebar:
        st.markdown("### Session")
        st.write(f"Data: {st.session_state['data_source']}")
        st.write(f"Releases loaded: {len(st.session_state['releases'])}")
        st.markdown("### Required readiness")
        for c in CRITICALITY:
            st.write(f"{c}: {REQUIRED_READINESS[c]}")
        st.markdown("### Pillar weights")
        for k, v in PILLAR_WEIGHTS.items():
            st.write(f"{k.title()}: {v:.2f}")
        st.caption("Decision support prototype. Weights and gates must be tuned and "
                   "accredited by the test and evaluation authority.")

    tabs = st.tabs(["Guide and concepts", "Data", "Evidence import", "Release evaluation",
                    "Portfolio dashboard", "Reports"])
    with tabs[0]:
        tab_guide()
    with tabs[1]:
        tab_data()
    with tabs[2]:
        tab_evidence()
    with tabs[3]:
        tab_release()
    with tabs[4]:
        tab_portfolio()
    with tabs[5]:
        tab_reports()


if __name__ == "__main__":
    main()
