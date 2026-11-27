

# CareBridge 360 — Streamlit app addressing five gaps in today's healthcare system.

  # Use case 1  AI Documentation & Admin Automation          (gap: clinician burnout)
  # Use case 2  Remote Patient Monitoring for Chronic Disease (gap: late detection)
  # Use case 3  Telehealth & Virtual Care for Underserved Areas (gap: access)
  # Use case 4  Accessible Mental Health Support              (gap: therapist shortage)
  # Use case 5  Interoperable Records & Care Coordination     (gap: siloed data)

# Every module has three tabs:
#  1. Learn     – plain-language explanation, concept diagram, formulas
#  2. Try it    – synthetic demo data OR upload your own file
#  3. Download  – results as PDF, Word (.docx), plain text and CSV

# All demo data is SYNTHETIC. This is a demonstration prototype, not a medical device.

# Optional: set ANTHROPIC_API_KEY to enable AI-drafted SOAP notes in use case 1.


import io
import json
import os
import re
from datetime import date, datetime, timedelta
from xml.sax.saxutils import escape

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

APP_NAME = "CareBridge 360"
APP_TAGLINE = "Closing the Gaps in Modern Healthcare"
DEVELOPER = "Developed by Randy Singh from Kalsnet (KNet) Consulting Group"

st.set_page_config(page_title=f"{APP_NAME}: {APP_TAGLINE}", page_icon="🩺", layout="wide")


def brand_banner():
    """Large bold-blue app title + developer credit, shown at the top of every page."""
    st.markdown(
        f"""
        <div style="text-align:center; padding:18px 10px 14px 10px; margin-bottom:12px;
                    border-bottom:3px solid #0b5ed7;">
          <div style="font-size:3.2rem; font-weight:800; color:#0b5ed7; line-height:1.1;">
            🩺 {APP_NAME}
          </div>
          <div style="font-size:1.6rem; font-weight:700; color:#0b5ed7; margin-top:4px;">
            {APP_TAGLINE}
          </div>
          <div style="font-size:1.5rem; font-weight:800; color:#0b5ed7; margin-top:10px;">
            {DEVELOPER}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

DISCLAIMER = (
    "Prototype for demonstration and education only. Demo data is synthetic (made up). "
    "Not a medical device and not for real clinical decisions."
)


# ============================================================================
# SHARED UI HELPERS
# ============================================================================
def disclaimer():
    st.caption("⚠️ " + DISCLAIMER)


def page_header(n, title, gap, solution, benefit):
    """The title block shown at the top of every use-case page."""
    st.caption(f"USE CASE {n} OF 5")
    st.title(title)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.error(f"**🚧 The gap**\n\n{gap}")
    with c2:
        st.info(f"**🛠️ What this module does**\n\n{solution}")
    with c3:
        st.success(f"**🌍 Real-world benefit**\n\n{benefit}")
    disclaimer()


def explain(what, why, how, analogy=None):
    with st.expander("🧒 Explain it simply (start here)", expanded=True):
        st.markdown(f"**What is it?** {what}")
        st.markdown(f"**Why does it matter?** {why}")
        st.markdown("**How does it work, step by step?**")
        st.markdown("\n".join(f"{i}. {s}" for i, s in enumerate(how, 1)))
        if analogy:
            st.markdown(f"**Everyday analogy:** {analogy}")


def glossary(terms: dict):
    with st.expander("📖 Jargon buster (glossary)"):
        for term, meaning in terms.items():
            st.markdown(f"- **{term}**: {meaning}")


def concept_diagram(dot: str, caption: str):
    st.subheader("🗺️ Concept diagram")
    st.graphviz_chart(dot)
    st.caption(caption)


def formulas(items):
    """items: list of (name, latex, plain-English explanation)."""
    st.subheader("🧮 Formulas explained")
    for name, latex, plain in items:
        with st.container(border=True):
            st.markdown(f"**{name}**")
            st.latex(latex)
            st.markdown(f"👉 *In plain words:* {plain}")


def privacy_note():
    st.caption(
        "🔒 Files are processed only inside this running app session and are not stored. "
        "Do not upload real patient data unless the app is deployed in a HIPAA/GDPR-compliant environment."
    )


def data_source(key, template: pd.DataFrame, required, help_md, loader, what="data"):
    """Lets the user choose demo data or upload a CSV. Returns (DataFrame, source label)."""
    mode = st.radio(
        f"Where should the {what} come from?",
        ["Use demo (synthetic) data", "Upload my own CSV"],
        key=f"{key}_mode", horizontal=True,
    )
    if mode.startswith("Use demo"):
        st.info("Using **made-up demo data**: no real people. Switch to *Upload* to analyse your own file.")
        return loader(), "synthetic demo data"

    st.markdown(help_md)
    st.download_button("⬇️ Download a blank template (CSV)", template.to_csv(index=False),
                       f"{key}_template.csv", key=f"{key}_tpl")
    privacy_note()
    up = st.file_uploader("Upload CSV", type=["csv"], key=f"{key}_up")
    if up is None:
        st.warning("No file uploaded yet, so the demo data is shown for now.")
        return loader(), "synthetic demo data"
    try:
        df = pd.read_csv(up)
    except Exception as e:  # noqa: BLE001
        st.error(f"Could not read that file ({e}). Showing demo data instead.")
        return loader(), "synthetic demo data"
    df.columns = [str(c).strip().lower() for c in df.columns]
    missing = [c for c in required if c not in df.columns]
    if missing:
        st.error(f"Your file is missing these required columns: {missing}. Showing demo data instead.")
        return loader(), "synthetic demo data"
    st.success(f"✅ Loaded {len(df)} rows from **{up.name}**")
    return df, up.name


def read_text_file(up) -> str:
    if up.name.lower().endswith(".docx"):
        from docx import Document
        return "\n".join(p.text for p in Document(up).paragraphs)
    return up.read().decode("utf-8", errors="replace")


# ============================================================================
# EXPORT HELPERS — PDF, Word, TXT, CSV
# ============================================================================
ASCII_MAP = {
    "≥": ">=", "≤": "<=", "✔": "[x]", "✘": "[ ]", "—": "-", "–": "-", "₂": "2", "→": "->",
    "↑": "up", "↓": "down", "•": "-", "’": "'", "‘": "'", "“": '"', "”": '"', "…": "...",
    "×": "x", "°": " deg", "Δ": "change ",
}


def to_latin1(s) -> str:
    """Core PDF fonts only support Latin-1, so swap common symbols and drop emoji."""
    s = str(s)
    for k, v in ASCII_MAP.items():
        s = s.replace(k, v)
    return s.encode("latin-1", "ignore").decode("latin-1").strip()


def _cell(v):
    if isinstance(v, (list, tuple, set)):
        return ", ".join(map(str, v))
    try:
        if pd.isna(v):
            return ""
    except (TypeError, ValueError):
        pass
    return str(v)


def build_txt(title, sections, tables) -> str:
    out = [f"{APP_NAME}: {APP_TAGLINE}", DEVELOPER, "", title, "=" * len(title), f"Generated: {datetime.now():%Y-%m-%d %H:%M}", DISCLAIMER, ""]
    for h, body in sections:
        out += [h, "-" * len(h), body, ""]
    for name, df in tables.items():
        out += [name, "-" * len(name), "No rows." if df.empty else df.to_string(index=False), ""]
    return "\n".join(out)


def build_docx(title, sections, tables) -> bytes:
    from docx import Document
    from docx.shared import Pt, RGBColor

    doc = Document()
    doc.styles["Normal"].font.size = Pt(10)
    for txt, size in ((f"{APP_NAME}: {APP_TAGLINE}", 20), (DEVELOPER, 13)):
        r_ = doc.add_paragraph().add_run(txt)
        r_.bold = True
        r_.font.size = Pt(size)
        r_.font.color.rgb = RGBColor(0x0B, 0x5E, 0xD7)
    doc.add_heading(title, 1)
    doc.add_paragraph(f"Generated: {datetime.now():%Y-%m-%d %H:%M}")
    doc.add_paragraph().add_run(DISCLAIMER).italic = True
    for h, body in sections:
        doc.add_heading(h, 1)
        for para in body.split("\n"):
            doc.add_paragraph(para)
    for name, df in tables.items():
        doc.add_heading(name, 1)
        if df.empty:
            doc.add_paragraph("No rows.")
            continue
        d = df.head(500)
        t = doc.add_table(rows=1, cols=len(d.columns))
        t.style = "Table Grid"
        for i, c in enumerate(d.columns):
            t.rows[0].cells[i].text = str(c)
            for r in t.rows[0].cells[i].paragraphs[0].runs:
                r.bold = True
        for row in d.itertuples(index=False):
            cells = t.add_row().cells
            for i, v in enumerate(row):
                cells[i].text = _cell(v)
        if len(df) > 500:
            doc.add_paragraph(f"(First 500 of {len(df)} rows shown — see the CSV for everything.)")
    buf = io.BytesIO()
    doc.save(buf)
    return buf.getvalue()


def build_pdf(title, sections, tables) -> bytes:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import landscape, letter
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=landscape(letter), leftMargin=36, rightMargin=36,
                            topMargin=36, bottomMargin=36, title=to_latin1(title))
    ss = getSampleStyleSheet()
    cell = ParagraphStyle("cell", parent=ss["BodyText"], fontSize=7.5, leading=9)
    head = ParagraphStyle("head", parent=cell, textColor=colors.white, fontName="Helvetica-Bold")
    P = lambda txt, style: Paragraph(escape(to_latin1(txt)), style)  # noqa: E731

    brand = ParagraphStyle("brand", parent=ss["Title"], textColor=colors.HexColor("#0b5ed7"), fontSize=22, leading=26)
    dev = ParagraphStyle("dev", parent=ss["Heading2"], textColor=colors.HexColor("#0b5ed7"), alignment=1)
    story = [P(f"{APP_NAME}: {APP_TAGLINE}", brand), P(DEVELOPER, dev), P(title, ss["Heading1"]), P(f"Generated: {datetime.now():%Y-%m-%d %H:%M}", ss["Normal"]),
             P(DISCLAIMER, ss["Italic"]), Spacer(1, 10)]
    for h, body in sections:
        story.append(P(h, ss["Heading2"]))
        for para in body.split("\n"):
            if para.strip():
                story.append(P(para, ss["BodyText"]))
    for name, df in tables.items():
        story.append(P(name, ss["Heading2"]))
        if df.empty:
            story.append(P("No rows.", ss["BodyText"]))
            continue
        d = df.head(200)
        data = [[P(c, head) for c in d.columns]]
        data += [[P(_cell(v), cell) for v in row] for row in d.itertuples(index=False)]
        t = Table(data, repeatRows=1, colWidths=[doc.width / len(d.columns)] * len(d.columns))
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f4e79")),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#eef3f8")]),
            ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#b0b8c4")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]))
        story.append(t)
        if len(df) > 200:
            story.append(P(f"(First 200 of {len(df)} rows shown — see the CSV for everything.)", ss["Italic"]))
        story.append(Spacer(1, 8))
    doc.build(story)
    return buf.getvalue()


def export_panel(key, title, sections, tables):
    """Download buttons for PDF / Word / TXT plus one CSV per table."""
    st.subheader("📤 Download your results")
    st.markdown(
        "- **PDF**: a formatted report to print or email\n"
        "- **Word**: an editable report you can change in Microsoft Word or Google Docs\n"
        "- **Text**: plain text that opens anywhere\n"
        "- **CSV**: raw tables that open in Excel or Google Sheets"
    )
    c1, c2, c3 = st.columns(3)
    c1.download_button("📄 PDF report", build_pdf(title, sections, tables), f"{key}_report.pdf",
                       mime="application/pdf", key=f"{key}_pdf", width="stretch")
    c2.download_button("📝 Word report (.docx)", build_docx(title, sections, tables), f"{key}_report.docx",
                       mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                       key=f"{key}_docx", width="stretch")
    c3.download_button("🗒️ Text report (.txt)", build_txt(title, sections, tables).encode("utf-8"),
                       f"{key}_report.txt", mime="text/plain", key=f"{key}_txt", width="stretch")
    if tables:
        cols = st.columns(min(len(tables), 4))
        for i, (name, df) in enumerate(tables.items()):
            slug = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")
            cols[i % len(cols)].download_button(f"📊 CSV: {name}", df.to_csv(index=False), f"{key}_{slug}.csv",
                                                mime="text/csv", key=f"{key}_csv_{slug}", width="stretch")
    with st.expander("👀 Preview of what's in the report"):
        for h, body in sections:
            st.markdown(f"**{h}**")
            st.text(body)
        for name, df in tables.items():
            st.markdown(f"**{name}**")
            st.dataframe(df, hide_index=True, width="stretch")


# ============================================================================
# OPTIONAL LLM
# ============================================================================
def llm_available() -> bool:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return False
    try:
        import anthropic  # noqa: F401
        return True
    except ImportError:
        return False


def ask_claude(prompt: str, max_tokens: int = 1200) -> str:
    import anthropic

    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=os.environ.get("CLAUDE_MODEL", "claude-sonnet-5-5"),
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")


# ============================================================================
# HOME — overview, architecture, impact estimator
# ============================================================================
ARCH_DOT = """
digraph {
  rankdir=LR; bgcolor="transparent";
  node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, fillcolor="#e8f1fb", color="#1f4e79"];
  edge [color="#555555"];
  data [label="Your data\\n(or synthetic demo data)", fillcolor="#fff4d6"];
  subgraph cluster_mods { label="CareBridge 360"; style="rounded,dashed"; color="#888888"; fontname="Helvetica";
    m1 [label="1  AI documentation\\n& admin automation"];
    m2 [label="2  Remote patient\\nmonitoring"];
    m3 [label="3  Telehealth &\\nvirtual care"];
    m4 [label="4  Mental health\\nsupport"];
    m5 [label="5  Records &\\ncare coordination"];
  }
  out [label="Results\\nPDF • Word • TXT • CSV", fillcolor="#dff3e4"];
  people [label="Clinicians, care teams\\n& managers decide", fillcolor="#fde2e1"];
  data -> m1; data -> m2; data -> m3; data -> m4; data -> m5;
  m1 -> out; m2 -> out; m3 -> out; m4 -> out; m5 -> out;
  out -> people;
}
"""


def page_home():
    st.caption("OVERVIEW")
    st.markdown("#### Five working tools that tackle the biggest gaps in today's healthcare system")
    disclaimer()

    overview = pd.DataFrame([
        ["1", "AI Documentation & Admin Automation", "Clinician burnout from paperwork", "Drafts notes & prior-auth letters"],
        ["2", "Remote Patient Monitoring for Chronic Disease", "Problems caught too late", "Flags worrying home readings early"],
        ["3", "Telehealth & Virtual Care for Underserved Areas", "Long waits, long drives, few specialists", "Triage + virtual visit booking"],
        ["4", "Accessible Mental Health Support", "Too few therapists for the need", "Screening + stepped care routing"],
        ["5", "Interoperable Records & Care Coordination", "Patient data stuck in separate systems", "Merges records, finds safety issues"],
    ], columns=["#", "Use case", "Gap it addresses", "What the tool does"])
    st.dataframe(overview, hide_index=True, width="stretch")

    explain(
        what="A set of five small apps in one. Each one targets a known weak spot in healthcare, such as paperwork, "
             "late warnings, access, mental health and scattered records.",
        why="These gaps waste clinician time, cost money, and sometimes harm patients. Software can't fix healthcare "
            "alone, but it can take over repetitive work and surface problems sooner.",
        how=["Pick a use case from the menu on the left.",
             "Read the **Learn** tab: a plain-language explanation, a picture of how it works, and the maths behind it.",
             "Open **Try it**: play with the synthetic demo data, or upload your own file.",
             "Open **Download** to save the results as PDF, Word, text or CSV."],
        analogy="Think of it as a toolbox. Each tool fixes one specific kind of problem, and you pick the one you need.",
    )
    concept_diagram(ARCH_DOT, "Data goes into any of the five modules; each one produces downloadable results "
                              "that people (not the software) act on.")

    st.divider()
    st.header("💰 Impact estimator: what could this be worth?")
    st.markdown("Change the numbers to match your organisation. **Every default value is only an assumption.**")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Documentation (use case 1)**")
        N = st.number_input("Number of clinicians (N)", 1, 10000, 50)
        m = st.number_input("Minutes saved per clinician per day (m)", 0, 240, 30)
        r = st.number_input("Clinician cost per hour, $ (r)", 0, 1000, 150)
        D = st.number_input("Working days per year (D)", 0, 365, 220)
    with c2:
        st.markdown("**Remote monitoring (use case 2)**")
        P = st.number_input("Patients enrolled (P)", 0, 100000, 500)
        a = st.slider("Yearly hospital admission rate, % (a)", 0, 100, 20)
        q = st.slider("Assumed drop in admissions, % (q)", 0, 100, 15)
        C = st.number_input("Cost per admission, $ (C)", 0, 200000, 15000)
    with c3:
        st.markdown("**Care coordination (use case 5)**")
        T = st.number_input("Duplicate tests avoided per month (T)", 0, 100000, 100)
        c = st.number_input("Average cost per test, $ (c)", 0, 10000, 120)

    hours = N * m / 60 * D
    v_doc = hours * r
    adm = P * a / 100 * q / 100
    v_rpm = adm * C
    v_dup = T * 12 * c
    total = v_doc + v_rpm + v_dup

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Clinician hours freed / yr", f"{hours:,.0f}", f"${v_doc:,.0f}")
    k2.metric("Admissions avoided / yr", f"{adm:,.1f}", f"${v_rpm:,.0f}")
    k3.metric("Duplicate-test savings / yr", f"${v_dup:,.0f}")
    k4.metric("Total estimated value / yr", f"${total:,.0f}")
    st.caption("Gross value only: does not subtract software, staff, training or integration costs.")

    formulas([
        ("Clinician time freed", r"H = \frac{N \times m \times D}{60}, \qquad V_{doc} = H \times r",
         "Multiply clinicians by minutes saved per day and working days, then divide by 60 to get hours. "
         "Multiply hours by hourly cost to get dollars."),
        ("Hospital admissions avoided", r"A = P \times \frac{a}{100} \times \frac{q}{100}, \qquad V_{rpm} = A \times C",
         "Out of P patients, a% would normally be admitted. If monitoring prevents q% of those, A admissions are avoided."),
        ("Duplicate-test savings", r"V_{dup} = T \times 12 \times c",
         "Tests avoided each month × 12 months × cost per test."),
        ("Total", r"V_{total} = V_{doc} + V_{rpm} + V_{dup}", "Add the three together."),
    ])

    glossary({
        "EHR": "Electronic Health Record: the computer system where a hospital keeps patient charts.",
        "Synthetic data": "Realistic-looking but completely made-up data, safe for demos.",
        "FHIR": "A worldwide standard format that lets different health systems share data.",
        "Triage": "Sorting patients by how urgently they need care.",
        "HIPAA": "US law protecting patient health information privacy.",
    })

    st.divider()
    export_panel(
        "impact", f"{APP_NAME}: Impact Estimate",
        [("Assumptions", f"Clinicians N={N}, minutes saved/day m={m}, cost/hr r=${r}, days/yr D={D}\n"
                         f"Monitored patients P={P}, admission rate a={a}%, reduction q={q}%, cost/admission C=${C}\n"
                         f"Duplicate tests avoided/month T={T}, cost/test c=${c}"),
         ("Results", f"Clinician hours freed per year: {hours:,.0f} (worth ${v_doc:,.0f})\n"
                     f"Hospital admissions avoided per year: {adm:,.1f} (worth ${v_rpm:,.0f})\n"
                     f"Duplicate-test savings per year: ${v_dup:,.0f}\n"
                     f"TOTAL estimated gross value per year: ${total:,.0f}"),
         ("How it was calculated", "H = N x m x D / 60;  V_doc = H x r\nA = P x a% x q%;  V_rpm = A x C\n"
                                   "V_dup = T x 12 x c;  Total = V_doc + V_rpm + V_dup")],
        {"Impact summary": pd.DataFrame([
            ["Documentation", f"{hours:,.0f} hours", round(v_doc)],
            ["Remote monitoring", f"{adm:,.1f} admissions", round(v_rpm)],
            ["Care coordination", f"{T * 12:,} tests", round(v_dup)],
            ["Total", "-", round(total)],
        ], columns=["Area", "Units (hours / admissions / tests)", "Value ($/yr)"])},
    )


# ============================================================================
# USE CASE 1 — AI DOCUMENTATION & ADMIN AUTOMATION
# ============================================================================
SAMPLE_TRANSCRIPT = (
    "Patient is a 58-year-old here for diabetes and blood pressure follow-up. "
    "She reports feeling more tired over the last month and some tingling in her feet. "
    "She denies chest pain or shortness of breath. "
    "She says she has been missing doses of metformin 500 mg. "
    "Blood pressure today is 152/94, heart rate 82. "
    "Weight is 92 kg. "
    "Her A1c came back at 8.9. "
    "Foot exam shows decreased sensation in both feet. "
    "This is consistent with uncontrolled type 2 diabetes with likely early peripheral neuropathy. "
    "Hypertension is also not at goal. "
    "We will increase metformin to 1000 mg twice daily and start lisinopril 10 mg daily. "
    "I will order a urine microalbumin and refer her to podiatry. "
    "Follow up in 3 months to recheck A1c."
)

SOAP_KEYWORDS = {
    "Subjective": ["here for", "feel", "feeling", "complains", "reports", "pain", "since", "history",
                   "says", "denies", "worse", "better", "tired", "cough", "missing doses"],
    "Objective": ["bp", "blood pressure", "heart rate", "hr", "pulse", "temp", "temperature", "exam",
                  "lungs", "weight", "spo2", "a1c", "glucose", "labs", "came back"],
    "Assessment": ["likely", "consistent with", "diagnosis", "assessment", "suspect", "impression",
                   "uncontrolled", "controlled", "not at goal", "at goal"],
    "Plan": ["start", "increase", "decrease", "continue", "refer", "order", "follow up", "follow-up",
             "schedule", "prescribe", "recheck", "return"],
}

KNOWN_MEDS = ["metformin", "lisinopril", "amlodipine", "atorvastatin", "insulin", "metoprolol",
              "furosemide", "semaglutide", "sertraline", "warfarin", "aspirin", "losartan",
              "simvastatin", "spironolactone", "albuterol"]

ICD_HINTS = {
    "type 2 diabetes": ("E11.9", "Type 2 diabetes mellitus without complications"),
    "neuropathy": ("E11.42", "Type 2 DM with diabetic polyneuropathy"),
    "hypertension": ("I10", "Essential (primary) hypertension"),
    "heart failure": ("I50.9", "Heart failure, unspecified"),
    "depression": ("F32.A", "Depression, unspecified"),
    "asthma": ("J45.909", "Unspecified asthma, uncomplicated"),
}

PRIOR_AUTH = {
    "MRI lumbar spine (CPT 72148)": [
        "≥6 weeks of conservative therapy documented",
        "Neurological deficit or red-flag symptoms documented",
        "Clinical exam note within last 30 days",
    ],
    "GLP-1 agonist for type 2 diabetes": [
        "Diagnosis of type 2 diabetes (E11.x) on file",
        "A1c ≥ 7% within last 90 days",
        "Documented trial or intolerance of metformin",
    ],
    "Sleep study / polysomnography (CPT 95810)": [
        "Epworth Sleepiness Scale score documented",
        "BMI and neck circumference documented",
        "Symptoms (snoring, witnessed apnoea, daytime sleepiness) documented",
    ],
}

DOC_DOT = """
digraph {
  rankdir=LR; bgcolor="transparent";
  node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, fillcolor="#e8f1fb", color="#1f4e79"];
  A [label="Doctor-patient\\nconversation", fillcolor="#fff4d6"];
  B [label="Transcript\\n(text)"];
  C [label="Split into\\nsentences"];
  D [label="Score each sentence\\nagainst S / O / A / P\\nkeyword lists"];
  E [label="Draft SOAP note"];
  G [label="Pick out vitals,\\nmedicines, codes"];
  H [label="Prior-auth checklist\\n+ letter"];
  F [label="Clinician reviews,\\nedits & signs", fillcolor="#fde2e1"];
  A -> B -> C -> D -> E -> F;
  B -> G -> E;
  G -> H -> F;
}
"""


def sentence_scores(sentence: str) -> dict:
    s = sentence.lower()
    return {sec: sum(1 for kw in kws if re.search(r"\b" + re.escape(kw) + r"\b", s))
            for sec, kws in SOAP_KEYWORDS.items()}


def classify_sentence(sentence: str) -> str:
    scores = sentence_scores(sentence)
    best = max(scores.values())
    if best == 0:
        return "Subjective"
    return [k for k in SOAP_KEYWORDS if scores[k] == best][-1]  # ties -> later section


def extract_entities(text: str) -> pd.DataFrame:
    t = text.lower()
    rows = []
    if m := re.search(r"(\d{2,3})\s*/\s*(\d{2,3})", t):
        rows.append(("Vital", "Blood pressure", f"{m.group(1)}/{m.group(2)} mmHg"))
    if m := re.search(r"(?:heart rate|\bhr\b|pulse)\D{0,10}(\d{2,3})", t):
        rows.append(("Vital", "Heart rate", f"{m.group(1)} bpm"))
    if m := re.search(r"(\d{2,3}(?:\.\d)?)\s*(kg|lbs?|pounds)\b", t):
        rows.append(("Vital", "Weight", f"{m.group(1)} {m.group(2)}"))
    if m := re.search(r"a1c\D{0,15}(\d{1,2}(?:\.\d)?)", t):
        rows.append(("Lab", "HbA1c", f"{m.group(1)} %"))
    meds = set()
    for med in KNOWN_MEDS:
        for mm in re.finditer(r"\b" + med + r"\b(?:\s+(?:to\s+)?(\d+\s*(?:mg|units|mcg)))?", t):
            meds.add(f"{med} {mm.group(1) or ''}".strip())
    rows += [("Medication", m_, "") for m_ in sorted(meds)]
    rows += [("Suggested code (verify)", code, desc) for kw, (code, desc) in ICD_HINTS.items() if kw in t]
    return pd.DataFrame(rows, columns=["Type", "Item", "Value / description"])


def page_documentation():
    page_header(
        1, "AI Documentation & Admin Automation",
        "Doctors spend hours a day typing notes and filling in insurance forms instead of seeing patients. "
        "This is a leading cause of burnout.",
        "Turns a visit conversation into a structured SOAP note, picks out vitals, medicines and billing codes, "
        "and builds a prior-authorization letter with a criteria checklist.",
        "Less typing and fewer rejected insurance requests mean more time with patients and lower admin costs.",
    )
    learn, tryit, dl = st.tabs(["1️⃣ Learn the concept", "2️⃣ Try it", "3️⃣ Download results"])

    with learn:
        explain(
            what="A digital assistant that reads what was said during a doctor's visit and writes the first draft "
                 "of the medical note, plus the insurance paperwork.",
            why="Every hour spent typing is an hour not spent with patients. Insurance approvals (\"prior auth\") are "
                "often rejected just because a required item was missing from the paperwork.",
            how=["The visit conversation is turned into text (a *transcript*).",
                 "The text is cut into individual sentences.",
                 "Each sentence is compared with four keyword lists (S, O, A, P). It goes into the section with the most matches.",
                 "Numbers such as blood pressure, weight and lab results are picked out automatically.",
                 "For insurance, a checklist shows which required items are documented, and a letter is drafted.",
                 "**The doctor always reviews and signs.** The computer drafts; the human decides."],
            analogy="Like a helpful assistant who sits in on the visit, takes notes, and sorts them into the "
                    "right folders, so the doctor only has to check and sign.",
        )
        glossary({
            "SOAP note": "The standard layout of a medical note: **S**ubjective (what the patient says), "
                         "**O**bjective (what's measured), **A**ssessment (the doctor's conclusion), **P**lan (next steps).",
            "Transcript": "A written record of a spoken conversation.",
            "Prior authorization": "Permission an insurer must give before it will pay for certain tests or medicines.",
            "ICD-10 code": "A standard code for a diagnosis (e.g. I10 = high blood pressure), used for billing.",
            "CPT code": "A standard code for a procedure or test (e.g. 72148 = lower-back MRI).",
        })
        concept_diagram(DOC_DOT, "The software drafts. The clinician (pink box) always has the final word.")
        formulas([
            ("Sentence section score",
             r"S_k(s) = \sum_{w \in K_k} \mathbf{1}[\,w \text{ appears in } s\,], \quad k \in \{S,O,A,P\}",
             "For a sentence s, count how many keywords from each section's list K appear in it. "
             "The 1[...] simply means 'count 1 if true, 0 if not'."),
            ("Which section the sentence goes in",
             r"\text{section}(s) = \arg\max_k S_k(s)",
             "Pick the section with the highest count. 'argmax' just means 'the winner'. "
             "No matches → Subjective; ties → the later section (Plan beats Assessment, and so on)."),
            ("Prior-auth completeness",
             r"C = \frac{\text{criteria documented}}{\text{criteria required}} \times 100\%",
             "If 2 out of 3 required items are documented, the request is 67% complete, and likely to be rejected."),
        ])

    with tryit:
        st.subheader("📂 Step 1: Choose the visit transcript")
        src = st.radio("Where should the transcript come from?",
                       ["Use demo (synthetic) transcript", "Upload a .txt or .docx file", "Paste my own text"],
                       key="doc_src", horizontal=True)
        transcript, source_label = SAMPLE_TRANSCRIPT, "synthetic demo transcript"
        if src.startswith("Upload"):
            privacy_note()
            up = st.file_uploader("Transcript file", type=["txt", "docx"], key="doc_up")
            if up:
                transcript, source_label = read_text_file(up), up.name
                st.success(f"✅ Loaded {up.name}")
            else:
                st.warning("No file yet, so the demo transcript is shown.")
        elif src.startswith("Paste"):
            pasted = st.text_area("Paste a transcript", "", height=180, key="doc_paste")
            if pasted.strip():
                transcript, source_label = pasted, "pasted text"
            else:
                st.warning("Nothing pasted yet, so the demo transcript is shown.")
        else:
            st.info("Using a **made-up** visit between a doctor and a 58-year-old patient with diabetes.")
        with st.expander("Show the transcript being analysed"):
            st.write(transcript)

        st.subheader("🧠 Step 2: The draft SOAP note")
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", transcript.strip()) if s.strip()]
        rows = []
        for s in sentences:
            sc = sentence_scores(s)
            rows.append({"sentence": s, **sc, "placed in": classify_sentence(s)})
        scores_df = pd.DataFrame(rows, columns=["sentence", *SOAP_KEYWORDS, "placed in"])
        soap = {k: [r["sentence"] for r in rows if r["placed in"] == k] for k in SOAP_KEYWORDS}
        note_text = "\n\n".join(f"{k.upper()}:\n{' '.join(v) if v else '(nothing captured)'}" for k, v in soap.items())

        if llm_available():
            if st.button("✨ Draft with Claude instead (AI)", key="doc_ai"):
                with st.spinner("Drafting with Claude…"):
                    st.session_state["doc_ai_note"] = ask_claude(
                        "Convert this clinical visit transcript into a concise SOAP note with headings "
                        "Subjective, Objective, Assessment, Plan. Do not invent facts.\n\n" + transcript)
        else:
            st.caption("Running in rule-based mode. Set ANTHROPIC_API_KEY to unlock an AI-drafted version.")
        if st.session_state.get("doc_ai_note"):
            note_text = st.session_state["doc_ai_note"]
            st.markdown(note_text)
        else:
            cols = st.columns(4)
            for col, (sec, lines) in zip(cols, soap.items()):
                with col.container(border=True):
                    st.markdown(f"**{sec}**")
                    st.write(" ".join(lines) if lines else "_Nothing captured._")

        with st.expander("🔍 Why did each sentence go where it did? (keyword scores)"):
            st.dataframe(scores_df, hide_index=True, width="stretch")
            st.caption("Each number is how many keywords from that section matched. The highest number wins.")

        ents = extract_entities(transcript)
        st.markdown("**Automatically extracted facts**")
        st.dataframe(ents, hide_index=True, width="stretch")

        st.subheader("📋 Step 3: Prior-authorization assistant")
        proc = st.selectbox("What is being requested from the insurer?", list(PRIOR_AUTH))
        c1, c2 = st.columns(2)
        patient = c1.text_input("Patient name", "Jane Doe (synthetic)")
        dx = c2.text_input("Diagnosis / ICD-10", "E11.9 Type 2 diabetes mellitus")
        st.markdown("Tick each item that is documented in the chart:")
        met = [st.checkbox(req, key=f"pa_{proc}_{i}") for i, req in enumerate(PRIOR_AUTH[proc])]
        pct = sum(met) / len(met)
        st.progress(pct, text=f"Completeness C = {sum(met)}/{len(met)} = {pct:.0%}")
        if pct < 1:
            st.warning("⚠️ Missing items are a common reason insurers reject requests. Complete them first.")
        else:
            st.success("✅ All criteria documented. Ready to submit.")
        letter = (
            f"Date: {date.today():%B %d, %Y}\nRE: Prior authorization request: {proc}\n"
            f"Patient: {patient}\nDiagnosis: {dx}\n\nTo the Utilization Review Team,\n\n"
            f"I am requesting authorization for {proc} for the above patient. "
            "The following criteria are documented in the medical record:\n"
            + "\n".join(f"  {'[x]' if ok else '[ ]'} {req}" for ok, req in zip(met, PRIOR_AUTH[proc]))
            + "\n\nThis service is medically necessary for diagnosis and management of the patient's condition. "
              "Supporting documentation is attached.\n\nSincerely,\n[Clinician name, credentials, NPI]"
        )
        st.text_area("Draft letter (editable after download)", letter, height=280)

    with dl:
        export_panel(
            "documentation", "Use Case 1: AI Documentation & Admin Automation",
            [("Data source", source_label),
             ("Draft SOAP note", note_text),
             ("Prior-authorization status", f"Request: {proc}\nCompleteness: {sum(met)}/{len(met)} ({pct:.0%})"),
             ("Prior-authorization letter", letter),
             ("How it was calculated",
              "Each sentence was scored by counting keyword matches for S, O, A and P; the highest score wins "
              "(no match = Subjective; ties go to the later section). Completeness = documented / required x 100%.")],
            {"SOAP sentence scores": scores_df, "Extracted facts": ents,
             "Prior-auth checklist": pd.DataFrame({"criterion": PRIOR_AUTH[proc],
                                                   "documented": ["yes" if x else "no" for x in met]})},
        )


# ============================================================================
# USE CASE 2 — REMOTE PATIENT MONITORING
# ============================================================================
RPM_PATIENTS = [
    ("P-1001", "Maria G.", "Hypertension"), ("P-1002", "James O.", "Type 2 diabetes"),
    ("P-1003", "Linda K.", "Heart failure"), ("P-1004", "Robert T.", "Hypertension"),
    ("P-1005", "Aisha M.", "Hypertension + diabetes"), ("P-1006", "Wei C.", "Heart failure"),
    ("P-1007", "Carlos R.", "Type 2 diabetes"), ("P-1008", "Emma S.", "COPD"),
]
METRICS = ["systolic", "glucose", "weight_kg", "heart_rate", "spo2"]
THRESHOLDS = {
    "systolic": {"high": 160, "low": 90, "unit": "mmHg", "label": "Systolic blood pressure"},
    "glucose": {"high": 250, "low": 70, "unit": "mg/dL", "label": "Blood glucose"},
    "spo2": {"low": 92, "unit": "%", "label": "Oxygen saturation (SpO₂)"},
    "weight_kg": {"unit": "kg", "label": "Body weight"},
    "heart_rate": {"high": 110, "low": 50, "unit": "bpm", "label": "Heart rate"},
}

RPM_DOT = """
digraph {
  rankdir=LR; bgcolor="transparent";
  node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, fillcolor="#e8f1fb", color="#1f4e79"];
  dev [label="Home devices\\nBP cuff • glucose meter\\nscale • pulse oximeter", fillcolor="#fff4d6"];
  read [label="Daily readings\\nsent automatically"];
  rules [label="Rules engine", shape=component];
  r1 [label="1. Fixed safety limits\\n(e.g. BP ≥ 160)"];
  r2 [label="2. Trends\\n(weight +2 kg in 3 days)"];
  r3 [label="3. Personal baseline\\n(unusual for THIS patient)"];
  q [label="Alert queue\\nsorted by risk"];
  nurse [label="Nurse reviews &\\ncalls patient", fillcolor="#fde2e1"];
  act [label="Adjust medicine /\\nbook visit early", fillcolor="#dff3e4"];
  dev -> read -> rules; rules -> r1; rules -> r2; rules -> r3;
  r1 -> q; r2 -> q; r3 -> q; q -> nurse -> act;
}
"""

RPM_TEMPLATE = pd.DataFrame(columns=["patient_id", "name", "condition", "date", *METRICS])


@st.cache_data
def make_rpm_data(days: int = 30, seed: int = 7) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    start = date.today() - timedelta(days=days - 1)
    rows = []
    for pid, name, cond in RPM_PATIENTS:
        base_sbp = rng.normal(132, 8)
        base_glu = rng.normal(165, 15) if "diabetes" in cond.lower() else rng.normal(100, 8)
        base_wt, base_hr = rng.normal(84, 10), rng.normal(74, 6)
        base_spo2 = 93.5 if cond == "COPD" else 97
        for d in range(days):
            rows.append(dict(
                patient_id=pid, name=name, condition=cond, date=start + timedelta(days=d),
                systolic=round(base_sbp + rng.normal(0, 6)), glucose=round(base_glu + rng.normal(0, 18)),
                weight_kg=round(base_wt + rng.normal(0, 0.3), 1), heart_rate=round(base_hr + rng.normal(0, 4)),
                spo2=int(min(100, round(base_spo2 + rng.normal(0, 1)))),
            ))
    df = pd.DataFrame(rows)
    last = df["date"].max()
    # realistic deterioration scenarios
    hf = (df.patient_id == "P-1003") & (df.date > last - timedelta(days=4))
    df.loc[hf, "weight_kg"] += np.linspace(0.8, 3.0, hf.sum()).round(1)
    df.loc[hf & (df.date == last), "spo2"] = 90
    df.loc[(df.patient_id == "P-1002") & (df.date == last), "glucose"] = 287
    bp = (df.patient_id == "P-1005") & (df.date > last - timedelta(days=3))
    df.loc[bp, "systolic"] = [166, 171, 174][: bp.sum()]
    df.loc[(df.patient_id == "P-1007") & (df.date == last), "glucose"] = 62
    return df


def normalise_rpm(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col in METRICS:
        df[col] = pd.to_numeric(df[col], errors="coerce") if col in df.columns else np.nan
    df["name"] = df["name"].fillna("") if "name" in df.columns else ""
    df["condition"] = df["condition"].fillna("Unknown") if "condition" in df.columns else "Unknown"
    df["patient_id"] = df["patient_id"].astype(str)
    df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.normalize()
    return df.dropna(subset=["date"]).sort_values(["patient_id", "date"])


def compute_alerts(df: pd.DataFrame) -> pd.DataFrame:
    alerts = []
    for pid, g in df.groupby("patient_id"):
        g = g.sort_values("date")
        latest = g.iloc[-1]
        name, cond = latest["name"], latest["condition"]
        flagged = set()

        def add(sev, rule, msg, metric):
            alerts.append(dict(patient_id=pid, name=name, condition=cond, severity=sev, rule=rule, alert=msg))
            flagged.add(metric)

        for metric in ["systolic", "glucose", "spo2", "heart_rate"]:
            v, th = latest[metric], THRESHOLDS[metric]
            if pd.isna(v):
                continue
            sev = "Medium" if metric == "heart_rate" else "High"
            too_high = "high" in th and v >= th["high"]
            too_low = "low" in th and (v < th["low"] if metric == "spo2" else v <= th["low"])
            if too_high:
                add(sev, "Safety limit", f"{th['label']} high: {v:g} {th['unit']} (limit {th['high']})", metric)
            elif too_low:
                add(sev, "Safety limit", f"{th['label']} low: {v:g} {th['unit']} (limit {th['low']})", metric)

        w = g["weight_kg"].dropna()
        if len(w) >= 4 and w.iloc[-1] - w.iloc[-4] >= 2.0:
            gain = w.iloc[-1] - w.iloc[-4]
            add("High" if "heart failure" in str(cond).lower() else "Medium", "Trend",
                f"Weight up {gain:.1f} kg in 3 readings (possible fluid build-up)", "weight_kg")

        sbp7 = g["systolic"].tail(7).dropna()
        if len(sbp7) >= 5 and (sbp7 >= 140).sum() >= 5:
            add("Medium", "Trend", f"Systolic ≥140 on {(sbp7 >= 140).sum()} of last {len(sbp7)} readings", "systolic_trend")

        for metric in ["systolic", "glucose", "heart_rate"]:
            hist = g[metric].iloc[:-1].dropna()
            v = latest[metric]
            if metric in flagged or pd.isna(v) or len(hist) < 7 or hist.std() == 0:
                continue
            z = (v - hist.mean()) / hist.std()
            if abs(z) >= 3:
                add("Medium", "Personal baseline",
                    f"{THRESHOLDS[metric]['label']} {v:g} is unusual for this patient (z = {z:+.1f})", metric)
    return pd.DataFrame(alerts, columns=["patient_id", "name", "condition", "severity", "rule", "alert"])


def risk_table(df, alerts):
    pts = df.groupby("patient_id").agg(name=("name", "last"), condition=("condition", "last"),
                                       readings=("date", "count"), last_reading=("date", "max")).reset_index()
    counts = alerts.pivot_table(index="patient_id", columns="severity", values="alert",
                                aggfunc="count", fill_value=0) if not alerts.empty else pd.DataFrame()
    pts["high_alerts"] = pts.patient_id.map(counts.get("High", pd.Series(dtype=int))).fillna(0).astype(int)
    pts["medium_alerts"] = pts.patient_id.map(counts.get("Medium", pd.Series(dtype=int))).fillna(0).astype(int)
    pts["risk_score"] = 3 * pts.high_alerts + pts.medium_alerts
    pts["priority"] = np.select([pts.risk_score >= 3, pts.risk_score >= 1], ["🔴 Call today", "🟠 Review this week"],
                                "🟢 Routine")
    pts["last_reading"] = pts.last_reading.dt.date
    return pts.sort_values("risk_score", ascending=False)


def page_rpm():
    page_header(
        2, "Remote Patient Monitoring for Chronic Disease",
        "Long-term conditions (high blood pressure, diabetes, heart failure) are checked only at short visits months "
        "apart, so warning signs are often missed until the patient lands in the emergency room.",
        "Collects daily home readings, checks them against safety limits, trends and each patient's own normal, "
        "and produces a prioritised call list for the care team.",
        "Catching problems days earlier can prevent emergency visits and hospital admissions.",
    )
    learn, tryit, dl = st.tabs(["1️⃣ Learn the concept", "2️⃣ Try it", "3️⃣ Download results"])

    with learn:
        explain(
            what="Patients use simple devices at home (blood-pressure cuff, glucose meter, bathroom scale, finger "
                 "oxygen clip). Readings are sent automatically to a care team, which watches for warning signs.",
            why="Problems usually build up over days. For example, a heart-failure patient gains water weight before "
                "they struggle to breathe. If someone notices early, a phone call or a medicine change can prevent a hospital stay.",
            how=["Each patient takes their readings at home every day.",
                 "Rule 1 (safety limits): is any reading dangerously high or low?",
                 "Rule 2 (trends): is something steadily getting worse, like weight rising fast?",
                 "Rule 3 (personal baseline): is today's reading very unusual *for this particular person*?",
                 "Alerts are scored and sorted so the nurse calls the most at-risk patients first."],
            analogy="Like a smoke detector for health: it doesn't put out fires, but it warns you while the fire is still small.",
        )
        glossary({
            "Systolic blood pressure": "The top number in a reading like 120/80; ≥160 is considered very high.",
            "SpO₂": "Percentage of oxygen in the blood; healthy is usually 95–100%, below 92% is concerning.",
            "Heart failure": "The heart doesn't pump strongly enough; fluid can build up, showing as quick weight gain.",
            "Baseline": "What is normal for a specific person.",
            "z-score": "How many 'typical wobbles' a reading is away from the person's average.",
        })
        concept_diagram(RPM_DOT, "Three types of checks feed one prioritised list; a human makes the call.")
        formulas([
            ("Rule 1: Safety limit",
             r"\text{alert if } x_t \ge \text{upper limit} \;\; \text{or} \;\; x_t \le \text{lower limit}",
             "x_t is today's reading. Example limits used: systolic BP 160/90, glucose 250/70 mg/dL, SpO₂ < 92%, heart rate 110/50."),
            ("Rule 2: Weight trend (fluid build-up)",
             r"\Delta W = W_t - W_{t-3} \;\ge\; 2\ \text{kg}",
             "Compare today's weight with the weight 3 readings ago. Gaining 2 kg or more that fast often means fluid, not fat."),
            ("Rule 3: Personal baseline (z-score)",
             r"z = \frac{x_t - \mu}{\sigma}, \qquad \text{alert if } |z| \ge 3",
             "μ (mu) is the patient's own average and σ (sigma) is how much their readings normally wobble. "
             "z = 3 means today is three 'normal wobbles' away from usual, which is very unusual for them."),
            ("Patient risk score",
             r"R = 3 \times (\#\text{High alerts}) + 1 \times (\#\text{Medium alerts})",
             "Serious alerts count three times as much. R ≥ 3 → call today; R ≥ 1 → review this week; R = 0 → routine."),
        ])

    with tryit:
        st.subheader("📂 Step 1: Choose the readings")
        raw, source_label = data_source(
            "rpm", RPM_TEMPLATE, ["patient_id", "date"],
            "**Your CSV needs** `patient_id` and `date` (YYYY-MM-DD), plus any of: "
            "`systolic`, `glucose`, `weight_kg`, `heart_rate`, `spo2`. Optional: `name`, `condition`. "
            "One row per patient per day.",
            make_rpm_data, "readings",
        )
        df = normalise_rpm(raw)
        if df.empty:
            st.error("No usable rows (check the date column).")
            return
        alerts = compute_alerts(df)
        risks = risk_table(df, alerts)

        st.subheader("📊 Step 2: Results")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Patients monitored", df.patient_id.nunique())
        c2.metric("Readings analysed", len(df))
        c3.metric("High-severity alerts", int((alerts.severity == "High").sum()))
        c4.metric("Patients to call today", int((risks.risk_score >= 3).sum()))

        st.markdown("**📞 Who should the nurse call first?**")
        st.dataframe(risks, hide_index=True, width="stretch")
        st.markdown("**🚨 Alert details**")
        if alerts.empty:
            st.success("No alerts: everyone looks stable.")
        else:
            st.dataframe(alerts.sort_values("severity"), hide_index=True, width="stretch")

        st.subheader("📈 Step 3: Look at one patient's trend")
        ids = risks.patient_id.tolist()
        pick = st.selectbox("Patient", ids, format_func=lambda p: f"{p}  {risks.set_index('patient_id').loc[p, 'name']}")
        metric = st.radio("Measurement", METRICS, horizontal=True, format_func=lambda m: THRESHOLDS[m]["label"])
        g = df[df.patient_id == pick]
        fig = go.Figure(go.Scatter(x=g.date, y=g[metric], mode="lines+markers", name="reading"))
        if g[metric].notna().sum() >= 7:
            fig.add_hline(y=g[metric].mean(), line_dash="dot", line_color="gray", annotation_text="personal average μ")
        th = THRESHOLDS[metric]
        for k, colr in (("high", "red"), ("low", "orange")):
            if k in th:
                fig.add_hline(y=th[k], line_dash="dash", line_color=colr, annotation_text=f"{k} limit {th[k]}")
        fig.update_layout(height=380, yaxis_title=th["unit"], margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig, width="stretch")
        st.caption("Dots are daily readings. Dashed lines are safety limits; the dotted line is this patient's own average.")

    with dl:
        top = risks.head(5)
        export_panel(
            "rpm", "Use Case 2: Remote Patient Monitoring Report",
            [("Data source", source_label),
             ("Summary", f"Patients: {df.patient_id.nunique()}; readings: {len(df)}; "
                         f"high alerts: {int((alerts.severity == 'High').sum())}; "
                         f"medium alerts: {int((alerts.severity == 'Medium').sum())}.\n"
                         "Top priorities: " + "; ".join(f"{r.patient_id} {r.name} (R={r.risk_score})" for r in top.itertuples())),
             ("How it was calculated",
              "Rule 1 safety limits (systolic 160/90, glucose 250/70, SpO2 < 92, HR 110/50). "
              "Rule 2 weight gain >= 2 kg over 3 readings; systolic >= 140 on 5 of last 7. "
              "Rule 3 z = (today - personal mean)/personal SD, |z| >= 3. Risk R = 3 x High + 1 x Medium.")],
            {"Patient priority list": risks, "Alerts": alerts, "All readings": df.assign(date=df.date.dt.date)},
        )


# ============================================================================
# USE CASE 3 — TELEHEALTH & VIRTUAL CARE
# ============================================================================
RED_FLAGS = [
    "Chest pain or pressure", "Severe difficulty breathing",
    "Face drooping, arm weakness or slurred speech", "Severe bleeding",
    "Loss of consciousness / fainting", "Thoughts of harming self or others",
]
SYMPTOMS = {
    "Fever": 2, "Cough": 1, "Sore throat": 1, "Rash": 1, "Ear pain": 1, "Urinary pain/burning": 2,
    "Abdominal pain": 2, "Vomiting / diarrhoea": 2, "Headache": 1, "Back pain": 1,
    "Anxiety / low mood": 1, "Medication refill": 0, "Skin lesion check": 1, "Joint swelling": 2,
}
PROVIDERS = [("Dr. Patel", "Primary care"), ("Dr. Nguyen", "Primary care"), ("NP Johnson", "Urgent care"),
             ("Dr. Alvarez", "Dermatology"), ("Dr. Kim", "Behavioural health")]
VIRTUAL_LEVELS = {"SOON", "ROUTINE", "SELF-CARE"}

TELE_DOT = """
digraph {
  rankdir=TB; bgcolor="transparent";
  node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, fillcolor="#e8f1fb", color="#1f4e79"];
  intake [label="Patient fills in\\nonline symptom form", fillcolor="#fff4d6"];
  flag [label="Any red-flag\\nsymptom?", shape=diamond, fillcolor="#fde2e1"];
  er [label="EMERGENCY\\nCall 911 / go to ER", fillcolor="#f8b4b4"];
  score [label="Add up triage score T\\n(symptoms + severity + age + risk)"];
  lvl [label="Map score to care level"];
  u [label="URGENT\\nIn-person within 24 h"];
  s [label="SOON\\nVideo visit today/tomorrow", fillcolor="#dff3e4"];
  r [label="ROUTINE\\nVideo visit in a few days", fillcolor="#dff3e4"];
  sc [label="SELF-CARE\\nAdvice / e-visit", fillcolor="#dff3e4"];
  book [label="Match specialty &\\nbook a virtual slot"];
  intake -> flag; flag -> er [label=" yes"]; flag -> score [label=" no"];
  score -> lvl; lvl -> u; lvl -> s; lvl -> r; lvl -> sc;
  s -> book; r -> book; sc -> book;
}
"""
TELE_TEMPLATE = pd.DataFrame(columns=["patient_id", "age", "symptoms", "days", "severity", "chronic",
                                      "red_flags", "distance_miles"])


def triage(age, symptoms, days, severity, flags, chronic):
    """Returns (level, advice, specialty, score)."""
    if flags:
        return "EMERGENCY", "Call 911 or go to the nearest emergency department now.", None, None
    score = sum(SYMPTOMS.get(s, 1) for s in symptoms) + severity // 3
    score += 2 if (age >= 65 or age < 2) else 0
    score += 1 if chronic else 0
    score += 1 if days > 7 else 0
    if symptoms == ["Anxiety / low mood"]:
        return "ROUTINE", "Virtual behavioural-health visit recommended.", "Behavioural health", score
    if "Skin lesion check" in symptoms or ("Rash" in symptoms and score < 5):
        return "ROUTINE", "Tele-dermatology visit (photo upload) recommended.", "Dermatology", score
    if score >= 8:
        return "URGENT", "In-person urgent care within 24 hours.", "Urgent care", score
    if score >= 4:
        return "SOON", "Same/next-day video visit recommended.", "Urgent care", score
    if score >= 1:
        return "ROUTINE", "Video visit with primary care in the next few days.", "Primary care", score
    return "SELF-CARE", "Self-care guidance or asynchronous e-visit.", "Primary care", score


@st.cache_data
def make_slots(seed: int = 3) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    base = datetime.combine(date.today() + timedelta(days=1), datetime.min.time())
    rows = [dict(time=base + timedelta(days=d, hours=h, minutes=m), provider=p, specialty=s)
            for d in range(3) for h in range(9, 17) for m in (0, 30) for p, s in PROVIDERS if rng.random() < 0.25]
    return pd.DataFrame(rows).sort_values("time").reset_index(drop=True)


@st.cache_data
def demo_intakes() -> pd.DataFrame:
    rng = np.random.default_rng(11)
    syms = list(SYMPTOMS)
    rows = []
    for i in range(15):
        s = [str(x) for x in rng.choice(syms, int(rng.integers(1, 4)), replace=False)]
        rows.append(dict(patient_id=f"T-{2001 + i}", age=int(rng.integers(1, 90)), symptoms=";".join(s),
                         days=int(rng.integers(0, 14)), severity=int(rng.integers(1, 10)),
                         chronic=int(rng.random() < 0.3),
                         red_flags="Chest pain or pressure" if i in (4, 11) else "",
                         distance_miles=round(float(rng.uniform(3, 70)), 1)))
    return pd.DataFrame(rows)


def _split(v):
    return [] if pd.isna(v) or str(v).strip() == "" else [x.strip() for x in str(v).split(";") if x.strip()]


def _num(v, default=0):
    v = pd.to_numeric(v, errors="coerce")
    return default if pd.isna(v) else v


def triage_batch(df: pd.DataFrame) -> pd.DataFrame:
    out = []
    for _, r in df.iterrows():
        chronic = str(r.get("chronic", "0")).strip().lower() in {"1", "yes", "y", "true"}
        level, advice, spec, score = triage(int(_num(r.get("age"))), _split(r.get("symptoms")), int(_num(r.get("days"))),
                                            int(_num(r.get("severity"))), _split(r.get("red_flags")), chronic)
        dist = float(_num(r.get("distance_miles")))
        out.append(dict(patient_id=r["patient_id"], age=int(_num(r.get("age"))), symptoms=r.get("symptoms"),
                        triage_score=score, level=level, advice=advice, specialty=spec or "Emergency",
                        miles_saved=round(2 * dist, 1) if level in VIRTUAL_LEVELS else 0.0))
    return pd.DataFrame(out)


def page_telehealth():
    page_header(
        3, "Telehealth & Virtual Care for Underserved Areas",
        "Rural clinics are closing and specialists are scarce, so patients face long drives and weeks-long waits, "
        "or they skip care altogether.",
        "Asks patients about their symptoms online, sorts them by urgency (sending emergencies to the ER), and books "
        "a video visit with the right type of clinician when it's safe to do so.",
        "Faster access to care without travel, and in-person slots freed up for people who truly need them.",
    )
    learn, tryit, dl = st.tabs(["1️⃣ Learn the concept", "2️⃣ Try it", "3️⃣ Download results"])

    with learn:
        explain(
            what="An online front door to the clinic. A patient answers a few questions, and the tool decides how "
                 "urgently they need care and whether a video visit is suitable.",
            why="Many health problems can be handled safely by video, saving a long drive. Sorting patients correctly "
                "means emergencies get to the ER fast, and clinics aren't clogged with visits that could be virtual.",
            how=["The patient picks their symptoms, how bad they are (0–10), and how long they've had them.",
                 "**Safety first:** any red-flag symptom (like chest pain) immediately says 'go to the ER'.",
                 "Otherwise, points are added up: each symptom has a weight, plus extra points for severity, "
                 "very young/old age, chronic illness or long duration.",
                 "The total score decides the care level: urgent, soon, routine or self-care.",
                 "The right specialty is matched (e.g. skin → dermatology) and a video slot can be booked."],
            analogy="Like an airport check-in kiosk: it sorts travellers to the right line so the staff can focus where they're needed.",
        )
        glossary({
            "Triage": "Sorting patients by how urgently they need care.",
            "Telehealth": "Healthcare delivered by video, phone or messaging instead of in person.",
            "Red flag": "A warning symptom that needs emergency care straight away.",
            "Asynchronous e-visit": "The patient sends information and the clinician replies later, like email.",
        })
        concept_diagram(TELE_DOT, "Red flags are checked first. Only safe cases are routed to virtual care (green).")
        formulas([
            ("Triage score",
             r"T = \sum_{i} w_i \;+\; \left\lfloor \frac{\text{severity}}{3} \right\rfloor \;+\; 2\cdot[\text{age}\ge65 \text{ or } <2] \;+\; [\text{chronic}] \;+\; [\text{days}>7]",
             "Add each symptom's weight w (fever = 2, cough = 1, …), plus severity divided by 3 (rounded down), plus 2 "
             "points for babies or older adults, plus 1 for a chronic illness, plus 1 if it's lasted over a week. "
             "[…] means 1 if true, 0 if false."),
            ("Care level",
             r"\text{Level} = \begin{cases} \text{EMERGENCY} & \text{any red flag} \\ \text{URGENT} & T \ge 8 \\ \text{SOON} & 4 \le T < 8 \\ \text{ROUTINE} & 1 \le T < 4 \\ \text{SELF-CARE} & T = 0 \end{cases}",
             "Higher score means more urgent. Red flags always override the score."),
            ("Travel saved",
             r"\text{Miles saved} = 2 \times d \quad \text{(if routed to virtual care)}",
             "d is the one-way distance to the clinic; a video visit saves the round trip."),
        ])

    with tryit:
        st.subheader("🅰️ One patient: interactive symptom checker")
        st.session_state.setdefault("bookings", [])
        with st.form("intake"):
            c1, c2 = st.columns(2)
            with c1:
                age = st.number_input("Age", 0, 120, 34)
                symptoms = st.multiselect("Symptoms", list(SYMPTOMS), default=["Fever", "Cough"])
                days = st.number_input("Days with symptoms", 0, 365, 3)
            with c2:
                severity = st.slider("How bad is it? (0 = barely, 10 = worst ever)", 0, 10, 5)
                chronic = st.checkbox("Has a long-term condition (diabetes, heart/lung disease, weak immune system)")
                flags = st.multiselect("Any of these RIGHT NOW? (red flags)", RED_FLAGS)
            submitted = st.form_submit_button("Check urgency", type="primary")
        if submitted:
            st.session_state["triage"] = triage(age, symptoms, days, severity, flags, chronic)

        if "triage" in st.session_state:
            level, advice, specialty, score = st.session_state["triage"]
            box = {"EMERGENCY": st.error, "URGENT": st.warning, "SOON": st.warning}.get(level, st.success)
            box(f"**{level}**: {advice}" + ("" if score is None else f"  \n(Triage score T = {score})"))
            if specialty and level != "URGENT":
                slots = make_slots()
                booked = {b["slot_id"] for b in st.session_state["bookings"]}
                avail = slots[(slots.specialty == specialty) & (~slots.index.isin(booked))].head(6)
                st.markdown(f"**Next available video slots: {specialty}**")
                for idx, row in avail.iterrows():
                    cc1, cc2 = st.columns([4, 1])
                    cc1.write(f"🗓️ {row.time:%a %b %d, %I:%M %p} with {row.provider}")
                    if cc2.button("Book", key=f"book_{idx}"):
                        st.session_state["bookings"].append(
                            dict(slot_id=idx, time=row.time, provider=row.provider, specialty=specialty))
                        st.rerun()
        if st.session_state["bookings"]:
            st.markdown("**📅 Booked visits**")
            st.dataframe(pd.DataFrame(st.session_state["bookings"]).drop(columns="slot_id"), hide_index=True)

        st.divider()
        st.subheader("🅱️ Many patients: batch triage")
        raw, source_label = data_source(
            "tele", TELE_TEMPLATE, ["patient_id", "age", "symptoms"],
            "**Your CSV needs** `patient_id`, `age`, `symptoms` (separate several with `;`, e.g. `Fever;Cough`). "
            "Optional: `days`, `severity` (0–10), `chronic` (1/0), `red_flags` (`;`-separated), `distance_miles`.",
            demo_intakes, "intake forms",
        )
        results = triage_batch(raw)
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Patients triaged", len(results))
        c2.metric("Sent to emergency", int((results.level == "EMERGENCY").sum()))
        virt = results.level.isin(VIRTUAL_LEVELS)
        c3.metric("Suitable for virtual care", f"{virt.mean():.0%}")
        c4.metric("Round-trip miles saved", f"{results.miles_saved.sum():,.0f}")
        order = ["EMERGENCY", "URGENT", "SOON", "ROUTINE", "SELF-CARE"]
        st.bar_chart(results.level.value_counts().reindex(order, fill_value=0))
        st.dataframe(results.sort_values("level", key=lambda s: s.map({k: i for i, k in enumerate(order)})),
                     hide_index=True, width="stretch")

    with dl:
        single = st.session_state.get("triage")
        bookings = pd.DataFrame(st.session_state.get("bookings", []))
        export_panel(
            "telehealth", "Use Case 3: Telehealth Triage Report",
            [("Data source (batch)", source_label),
             ("Single-patient result", "Not run yet." if not single else f"{single[0]}: {single[1]} (score {single[3]})"),
             ("Batch summary", f"Patients: {len(results)}; emergencies: {int((results.level == 'EMERGENCY').sum())}; "
                               f"virtual-eligible: {virt.mean():.0%}; round-trip miles saved: {results.miles_saved.sum():,.0f}"),
             ("How it was calculated",
              "Red flag -> EMERGENCY. Otherwise T = sum of symptom weights + floor(severity/3) + 2 if age >= 65 or < 2 "
              "+ 1 if chronic + 1 if > 7 days. T >= 8 URGENT; 4-7 SOON; 1-3 ROUTINE; 0 SELF-CARE. "
              "Miles saved = 2 x distance for virtual levels.")],
            {"Batch triage results": results,
             "Booked visits": bookings.drop(columns="slot_id") if not bookings.empty else bookings},
        )


# ============================================================================
# USE CASE 4 — ACCESSIBLE MENTAL HEALTH SUPPORT
# ============================================================================
PHQ9 = [
    "Little interest or pleasure in doing things",
    "Feeling down, depressed, or hopeless",
    "Trouble falling or staying asleep, or sleeping too much",
    "Feeling tired or having little energy",
    "Poor appetite or overeating",
    "Feeling bad about yourself — or that you are a failure or have let yourself or your family down",
    "Trouble concentrating on things, such as reading or watching television",
    "Moving or speaking so slowly that other people could have noticed, or the opposite — being so fidgety or restless",
    "Thoughts that you would be better off dead, or of hurting yourself",
]
GAD7 = [
    "Feeling nervous, anxious, or on edge", "Not being able to stop or control worrying",
    "Worrying too much about different things", "Trouble relaxing",
    "Being so restless that it is hard to sit still", "Becoming easily annoyed or irritable",
    "Feeling afraid, as if something awful might happen",
]
OPTIONS = ["Not at all (0)", "Several days (1)", "More than half the days (2)", "Nearly every day (3)"]
MH_TEMPLATE = pd.DataFrame(columns=["patient_id", "date", *[f"phq{i}" for i in range(1, 10)],
                                    *[f"gad{i}" for i in range(1, 8)]])

MH_DOT = """
digraph {
  rankdir=LR; bgcolor="transparent";
  node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, fillcolor="#e8f1fb", color="#1f4e79"];
  q [label="Short questionnaire\\nPHQ-9 (mood) + GAD-7 (worry)", fillcolor="#fff4d6"];
  sum [label="Add up the answers\\n(0-3 each)"];
  safe [label="Item 9 > 0?\\n(self-harm thoughts)", shape=diamond, fillcolor="#fde2e1"];
  now [label="Same-day clinician\\nfollow-up + 988", fillcolor="#f8b4b4"];
  band [label="Severity band\\nminimal → severe"];
  s0 [label="Watch & rescreen"];
  s1 [label="Step 1: Digital CBT /\\nguided self-help", fillcolor="#dff3e4"];
  s2 [label="Step 2: Care manager\\n+ brief therapy", fillcolor="#dff3e4"];
  s3 [label="Step 3: Psychiatrist /\\ntherapist referral", fillcolor="#dff3e4"];
  q -> sum -> safe; safe -> now [label=" yes"]; safe -> band [label=" no / also"];
  band -> s0; band -> s1; band -> s2; band -> s3;
}
"""


def phq9_band(s):
    return ("Minimal" if s <= 4 else "Mild" if s <= 9 else "Moderate" if s <= 14
            else "Moderately severe" if s <= 19 else "Severe")


def gad7_band(s):
    return "Minimal" if s <= 4 else "Mild" if s <= 9 else "Moderate" if s <= 14 else "Severe"


def stepped_care(phq, gad):
    worst = max(phq, gad * 27 / 21)
    if worst >= 15:
        return "Step 3: Refer to psychiatry / licensed therapist; consider medication review."
    if worst >= 10:
        return "Step 2: Collaborative care: care-manager follow-up + brief therapy (CBT); review in 4 weeks."
    if worst >= 5:
        return "Step 1: Guided self-help / digital CBT programme; rescreen in 4–6 weeks."
    return "Watchful waiting: rescreen at next routine visit."


@st.cache_data
def demo_screenings() -> pd.DataFrame:
    rng = np.random.default_rng(5)
    rows = []
    level = [2.2, 1.7, 1.2, 0.7, 0.3, 1.5]
    for p, mu in enumerate(level):
        for visit in range(3):
            m = max(0.0, mu - 0.35 * visit)
            phq = np.clip(np.round(rng.normal(m, 0.6, 9)), 0, 3).astype(int)
            gad = np.clip(np.round(rng.normal(m * 0.9, 0.6, 7)), 0, 3).astype(int)
            phq[8] = 1 if (p == 0 and visit == 0) else 0
            rows.append(dict(patient_id=f"M-{301 + p}", date=str(date.today() - timedelta(weeks=8 - 4 * visit)),
                             **{f"phq{i + 1}": int(v) for i, v in enumerate(phq)},
                             **{f"gad{i + 1}": int(v) for i, v in enumerate(gad)}))
    return pd.DataFrame(rows)


def _item(v):
    v = pd.to_numeric(v, errors="coerce")
    return 0 if pd.isna(v) else int(np.clip(v, 0, 3))


def score_batch(df: pd.DataFrame) -> pd.DataFrame:
    out = []
    for _, r in df.iterrows():
        phq = [_item(r.get(f"phq{i}")) for i in range(1, 10)]
        gad = [_item(r.get(f"gad{i}")) for i in range(1, 8)]
        p, g = sum(phq), sum(gad)
        out.append(dict(patient_id=r["patient_id"], date=r.get("date", ""), phq9=p, phq9_band=phq9_band(p),
                        gad7=g, gad7_band=gad7_band(g), safety_flag="YES: follow up today" if phq[8] > 0 else "",
                        pathway=stepped_care(p, g)))
    return pd.DataFrame(out)


def page_mental_health():
    page_header(
        4, "Accessible Mental Health Support",
        "Far more people need mental-health care than there are therapists, so waits stretch for months and many "
        "people are never assessed at all.",
        "Uses two short, widely used questionnaires (PHQ-9 and GAD-7) to measure mood and anxiety, flags safety "
        "concerns immediately, and routes each person to the right level of support.",
        "Specialists see the people who need them most; others start effective lighter-touch help (like digital CBT) right away.",
    )
    learn, tryit, dl = st.tabs(["1️⃣ Learn the concept", "2️⃣ Try it", "3️⃣ Download results"])

    with learn:
        explain(
            what="A quick questionnaire, about 3 minutes, that measures how much low mood and worry are affecting someone, "
                 "followed by a suggestion for the right level of help.",
            why="Not everyone needs a psychiatrist. With *stepped care*, most people start with lighter help and "
                "step up if needed, so scarce specialists can focus on the most serious cases.",
            how=["The person answers 9 mood questions (PHQ-9) and 7 worry questions (GAD-7).",
                 "Each answer scores 0 (not at all) to 3 (nearly every day).",
                 "The answers are added up, and the total falls into a band from 'minimal' to 'severe'.",
                 "**Safety check:** if question 9 (thoughts of self-harm) is above 0, a clinician must follow up the same day.",
                 "The worse of the two scores decides the step of care.",
                 "Re-screening every few weeks shows whether the person is getting better."],
            analogy="Like a thermometer for mood: it doesn't diagnose by itself, but it tells you how high the 'temperature' is "
                    "and whether it's going down with treatment.",
        )
        glossary({
            "PHQ-9": "Patient Health Questionnaire, 9 items. A free, validated screen for depression (score 0–27).",
            "GAD-7": "Generalised Anxiety Disorder scale, 7 items. A free, validated screen for anxiety (score 0–21).",
            "Stepped care": "Start with the least intensive effective help, and step up only if needed.",
            "CBT": "Cognitive Behavioural Therapy, a practical talking therapy that can also be delivered digitally.",
            "988": "The US Suicide & Crisis Lifeline. Call or text 988, any time.",
        })
        concept_diagram(MH_DOT, "The safety check runs on every screening, whatever the total score.")
        formulas([
            ("PHQ-9 score", r"\text{PHQ9} = \sum_{i=1}^{9} q_i, \quad q_i \in \{0,1,2,3\}",
             "Add the nine answers. 0–4 minimal, 5–9 mild, 10–14 moderate, 15–19 moderately severe, 20–27 severe."),
            ("GAD-7 score", r"\text{GAD7} = \sum_{j=1}^{7} g_j",
             "Add the seven answers. 0–4 minimal, 5–9 mild, 10–14 moderate, 15–21 severe."),
            ("Putting both on the same scale", r"\text{Worst} = \max\!\left(\text{PHQ9},\ \text{GAD7} \times \tfrac{27}{21}\right)",
             "GAD-7 tops out at 21 and PHQ-9 at 27, so GAD-7 is stretched to match. Then we take whichever is worse."),
            ("Step of care",
             r"\text{Step} = \begin{cases} 3 & \text{Worst} \ge 15 \\ 2 & 10 \le \text{Worst} < 15 \\ 1 & 5 \le \text{Worst} < 10 \\ 0 & \text{Worst} < 5 \end{cases}",
             "Higher score → more intensive help. Separately, any answer above 0 on question 9 triggers a same-day safety follow-up."),
        ])

    with tryit:
        st.subheader("🅰️ One person: take the screening")
        st.markdown("_Over the **last 2 weeks**, how often have you been bothered by…_")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**PHQ-9 (mood)**")
            phq = [OPTIONS.index(st.radio(q, OPTIONS, key=f"phq{i}")) for i, q in enumerate(PHQ9)]
        with c2:
            st.markdown("**GAD-7 (worry)**")
            gad = [OPTIONS.index(st.radio(q, OPTIONS, key=f"gad{i}")) for i, q in enumerate(GAD7)]
        p_s, g_s = sum(phq), sum(gad)
        m1, m2 = st.columns(2)
        m1.metric("PHQ-9", f"{p_s}/27", phq9_band(p_s), delta_color="off")
        m2.metric("GAD-7", f"{g_s}/21", gad7_band(g_s), delta_color="off")
        if phq[8] > 0:
            st.error("**Safety flag:** question 9 was answered above zero. A clinician should follow up today. "
                     "If you're in the US and struggling, you can call or text **988** (Suicide & Crisis Lifeline) any time.")
        single_path = stepped_care(p_s, g_s)
        st.info(f"**Suggested pathway:** {single_path}")

        st.divider()
        st.subheader("🅱️ Many people: batch scoring & progress tracking")
        raw, source_label = data_source(
            "mh", MH_TEMPLATE, ["patient_id", *[f"phq{i}" for i in range(1, 10)], *[f"gad{i}" for i in range(1, 8)]],
            "**Your CSV needs** `patient_id`, `phq1`…`phq9` and `gad1`…`gad7` (each 0–3). Optional: `date`. "
            "One row per screening; repeat a patient on different dates to track progress.",
            demo_screenings, "screenings",
        )
        batch = score_batch(raw)
        flagged = int((batch.safety_flag != "").sum())
        c1, c2, c3 = st.columns(3)
        c1.metric("Screenings scored", len(batch))
        c2.metric("Moderate or worse (PHQ-9 ≥ 10)", int((batch.phq9 >= 10).sum()))
        c3.metric("Safety flags", flagged)
        if flagged:
            st.error(f"{flagged} screening(s) need same-day clinician follow-up (question 9 > 0).")
        st.dataframe(batch, hide_index=True, width="stretch")
        if batch["date"].astype(str).str.len().gt(0).any() and batch.patient_id.duplicated().any():
            st.markdown("**Progress over time (lower = better)**")
            trend = batch.assign(date=pd.to_datetime(batch["date"], errors="coerce")).dropna(subset=["date"])
            fig = go.Figure()
            for pid, g in trend.groupby("patient_id"):
                fig.add_trace(go.Scatter(x=g.date, y=g.phq9, mode="lines+markers", name=str(pid)))
            for y, lab in ((5, "mild"), (10, "moderate"), (15, "mod. severe")):
                fig.add_hline(y=y, line_dash="dot", line_color="gray", annotation_text=lab)
            fig.update_layout(height=360, yaxis_title="PHQ-9 score", margin=dict(l=10, r=10, t=30, b=10))
            st.plotly_chart(fig, width="stretch")

    with dl:
        export_panel(
            "mental_health", "Use Case 4: Mental Health Screening Report",
            [("Data source (batch)", source_label),
             ("Single screening", f"PHQ-9 {p_s}/27 ({phq9_band(p_s)}); GAD-7 {g_s}/21 ({gad7_band(g_s)}); "
                                  f"safety flag: {'YES' if phq[8] > 0 else 'no'}.\nPathway: {single_path}"),
             ("Batch summary", f"Screenings: {len(batch)}; PHQ-9 >= 10: {int((batch.phq9 >= 10).sum())}; "
                               f"safety flags: {flagged}."),
             ("How it was calculated",
              "PHQ-9 = sum of 9 items (0-3); GAD-7 = sum of 7 items (0-3). Worst = max(PHQ-9, GAD-7 x 27/21). "
              "Step 3 if >= 15, Step 2 if >= 10, Step 1 if >= 5, else watchful waiting. Item 9 > 0 = same-day safety follow-up."),
             ("Crisis resource", "US: call or text 988 (Suicide & Crisis Lifeline).")],
            {"Batch screening results": batch},
        )


# ============================================================================
# USE CASE 5 — INTEROPERABLE RECORDS & CARE COORDINATION
# ============================================================================
SOURCES = {
    "St. Mary's Hospital (EHR A)": {
        "patient": {"name": "Daniel Brooks", "dob": "1956-03-14", "mrn": "SM-55821"},
        "meds": [("warfarin", "5 mg daily"), ("metoprolol", "50 mg twice daily"), ("atorvastatin", "40 mg nightly")],
        "labs": [("HbA1c", "2026-11-02", "7.4 %"), ("Lipid panel", "2026-11-02", "LDL 98"),
                 ("Basic metabolic panel", "2026-11-10", "K 4.9")],
        "allergies": ["Penicillin"],
    },
    "Riverside Family Clinic (EHR B)": {
        "patient": {"name": "Dan Brooks", "dob": "1956-03-14", "mrn": "RFC-00912"},
        "meds": [("metoprolol", "25 mg twice daily"), ("lisinopril", "20 mg daily"),
                 ("aspirin", "81 mg daily"), ("spironolactone", "25 mg daily")],
        "labs": [("HbA1c", "2026-11-18", "7.3 %"), ("Basic metabolic panel", "2026-11-19", "K 5.2")],
        "allergies": ["Penicillin", "Sulfa drugs"],
    },
    "CityPharm (pharmacy claims)": {
        "patient": {"name": "Daniel J Brooks", "dob": "1956-03-14", "mrn": "CP-7741"},
        "meds": [("warfarin", "5 mg daily"), ("clarithromycin", "500 mg twice daily"), ("simvastatin", "20 mg nightly")],
        "labs": [],
        "allergies": [],
    },
}
INTERACTIONS = [
    ({"warfarin", "aspirin"}, "High", "Increased bleeding risk"),
    ({"warfarin", "clarithromycin"}, "High", "Clarithromycin raises warfarin effect (INR ↑)"),
    ({"simvastatin", "clarithromycin"}, "High", "Contraindicated: risk of severe muscle damage (rhabdomyolysis)"),
    ({"lisinopril", "spironolactone"}, "Medium", "High potassium risk: monitor potassium"),
    ({"atorvastatin", "simvastatin"}, "Medium", "Therapeutic duplication: two statins"),
    ({"metoprolol", "verapamil"}, "High", "Very slow heart rate / heart block"),
    ({"sertraline", "tramadol"}, "High", "Serotonin syndrome risk"),
    ({"lisinopril", "losartan"}, "Medium", "Dual RAAS blockade: kidney & potassium risk"),
]
DUP_WINDOW_DAYS = 30
MEDS_TEMPLATE = pd.DataFrame(columns=["source", "drug", "dose"])
LABS_TEMPLATE = pd.DataFrame(columns=["source", "test", "date", "result"])

COORD_DOT = """
digraph {
  rankdir=LR; bgcolor="transparent";
  node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, fillcolor="#e8f1fb", color="#1f4e79"];
  h [label="Hospital EHR", fillcolor="#fff4d6"];
  c [label="Family clinic EHR", fillcolor="#fff4d6"];
  p [label="Pharmacy records", fillcolor="#fff4d6"];
  id [label="Match identity\\n(same person?\\nname + date of birth)"];
  m [label="Merge into one list\\nmeds • labs • allergies"];
  chk [label="Safety checks", shape=component];
  k1 [label="Drug interactions"];
  k2 [label="Dose mismatches"];
  k3 [label="Duplicate tests\\n(≤30 days apart)"];
  u [label="One unified record\\n+ FHIR export", fillcolor="#dff3e4"];
  doc [label="Care team fixes\\nthe issues", fillcolor="#fde2e1"];
  h -> id; c -> id; p -> id; id -> m -> chk; chk -> k1; chk -> k2; chk -> k3;
  k1 -> u; k2 -> u; k3 -> u; u -> doc;
}
"""


@st.cache_data
def demo_meds():
    return pd.DataFrame([dict(source=s, drug=d, dose=dose) for s, r in SOURCES.items() for d, dose in r["meds"]])


@st.cache_data
def demo_labs():
    return pd.DataFrame([dict(source=s, test=t, date=dt, result=res) for s, r in SOURCES.items()
                         for t, dt, res in r["labs"]])


def find_issues(meds: pd.DataFrame, labs: pd.DataFrame) -> pd.DataFrame:
    issues = []
    if not meds.empty:
        for drug, g in meds.groupby("drug"):
            if g.dose.nunique() > 1:
                issues.append(dict(type="Dose mismatch", severity="Medium",
                                   detail=f"{drug}: " + " vs ".join(f"{d} ({s})" for d, s in zip(g.dose, g.source))))
        drugs = set(meds.drug)
        for pair, sev, msg in INTERACTIONS:
            if pair <= drugs:
                issues.append(dict(type="Drug interaction", severity=sev, detail=f"{' + '.join(sorted(pair))}: {msg}"))
    if not labs.empty:
        for test, g in labs.dropna(subset=["date"]).sort_values("date").groupby("test"):
            d, s = g.date.tolist(), g.source.tolist()
            for i in range(1, len(d)):
                gap = (d[i] - d[i - 1]).days
                if gap <= DUP_WINDOW_DAYS and s[i] != s[i - 1]:
                    issues.append(dict(type="Duplicate test", severity="Low",
                                       detail=f"{test} repeated after {gap} days ({s[i - 1]} → {s[i]})"))
    return pd.DataFrame(issues, columns=["type", "severity", "detail"])


def to_fhir_bundle(meds, labs, allergies, patient):
    entries = [{"resource": {"resourceType": "Patient", "name": [{"text": patient.get("name", "Unknown")}],
                             "birthDate": patient.get("dob", "")}}]
    for m in meds.drop_duplicates(["drug", "dose"]).itertuples():
        entries.append({"resource": {"resourceType": "MedicationStatement", "status": "active",
                                     "medicationCodeableConcept": {"text": m.drug},
                                     "dosage": [{"text": m.dose}], "informationSource": {"display": m.source}}})
    for lab in labs.itertuples():
        entries.append({"resource": {"resourceType": "Observation", "status": "final", "code": {"text": lab.test},
                                     "effectiveDateTime": "" if pd.isna(lab.date) else lab.date.strftime("%Y-%m-%d"),
                                     "valueString": str(lab.result), "performer": [{"display": lab.source}]}})
    for a in allergies:
        entries.append({"resource": {"resourceType": "AllergyIntolerance", "code": {"text": a}}})
    return {"resourceType": "Bundle", "type": "collection", "entry": entries}


def page_coordination():
    page_header(
        5, "Interoperable Records & Care Coordination",
        "A patient's information is scattered across hospitals, clinics and pharmacies that don't talk to each "
        "other. This leads to repeated tests, conflicting prescriptions and dangerous drug combinations.",
        "Pulls the records together into one list, checks for drug interactions, dose mismatches and duplicate "
        "tests, and exports a single record in the FHIR standard format.",
        "Fewer medication errors, fewer wasted tests, and every clinician seeing the same complete picture.",
    )
    learn, tryit, dl = st.tabs(["1️⃣ Learn the concept", "2️⃣ Try it", "3️⃣ Download results"])

    with learn:
        explain(
            what="A tool that gathers a patient's records from different places into one combined view, then "
                 "double-checks it for safety problems.",
            why="If the hospital, the GP and the pharmacy each see only part of the picture, nobody notices that two "
                "prescriptions clash, or that the same blood test was done twice in two weeks.",
            how=["Records arrive from each source: the hospital, the clinic and the pharmacy.",
                 "The tool checks they belong to the same person (name variants + same date of birth).",
                 "All medicines, lab tests and allergies are merged into one list, with their source labelled.",
                 "Three safety checks run: risky drug pairs, the same drug at different doses, and the same test repeated within 30 days.",
                 "Results are shown to the care team, and the unified record can be exported in the FHIR standard."],
            analogy="Like combining three people's shopping lists before going to the store: you spot the duplicates "
                    "and the things that shouldn't go together.",
        )
        glossary({
            "Interoperability": "The ability of different computer systems to exchange and use each other's data.",
            "Medication reconciliation": "Comparing all medicine lists to produce one correct, up-to-date list.",
            "Drug interaction": "When two medicines together cause a harmful effect.",
            "FHIR": "Fast Healthcare Interoperability Resources, the modern standard format for sharing health data.",
            "MRN": "Medical Record Number: each system's own ID for a patient.",
        })
        concept_diagram(COORD_DOT, "Three separate sources become one checked record.")
        formulas([
            ("Drug-interaction check",
             r"\text{flag if } \{a, b\} \subseteq \text{AllDrugs} \text{ for a known risky pair } (a,b)",
             "If both medicines of a known dangerous pair appear anywhere in the combined list (even from different "
             "prescribers), raise an alert. ⊆ means 'is contained in'."),
            ("Dose-mismatch check",
             r"\text{flag if } \left|\{\text{doses of drug } d \text{ across sources}\}\right| > 1",
             "If different sources list different doses of the same drug, someone needs to confirm the right one."),
            ("Duplicate-test check",
             r"\text{flag if same test},\ \ |t_2 - t_1| \le 30 \text{ days},\ \ \text{source}_1 \ne \text{source}_2",
             "The same test done twice within 30 days at different places is probably unnecessary."),
            ("Savings from avoided duplicates",
             r"\$ \text{saved} = n_{\text{duplicates}} \times \text{cost per test}",
             "Count the duplicate tests found and multiply by their average cost."),
        ])

    with tryit:
        st.subheader("📂 Step 1: Medication lists")
        meds_raw, meds_label = data_source(
            "meds", MEDS_TEMPLATE, ["source", "drug", "dose"],
            "**Your CSV needs** `source` (where the record came from), `drug`, `dose`. One row per medicine per source.",
            demo_meds, "medication lists",
        )
        st.subheader("📂 Step 2: Lab tests (optional)")
        labs_raw, labs_label = data_source(
            "labs", LABS_TEMPLATE, ["source", "test", "date"],
            "**Your CSV needs** `source`, `test`, `date` (YYYY-MM-DD). Optional: `result`.",
            demo_labs, "lab results",
        )
        meds = meds_raw.copy()
        meds["drug"] = meds["drug"].astype(str).str.strip().str.lower()
        meds["dose"] = meds["dose"].astype(str).str.strip()
        labs = labs_raw.copy()
        if "result" not in labs.columns:
            labs["result"] = ""
        labs["date"] = pd.to_datetime(labs["date"], errors="coerce")
        using_demo = meds_label.startswith("synthetic")

        if using_demo:
            st.markdown("**🪪 Identity match:** same date of birth, three name spellings → treated as one person")
            st.dataframe(pd.DataFrame([{"source": s, **SOURCES[s]["patient"]} for s in SOURCES]), hide_index=True)
            allergies = sorted({a for r in SOURCES.values() for a in r["allergies"]})
            patient = SOURCES[next(iter(SOURCES))]["patient"]
        else:
            allergies, patient = [], {"name": "Uploaded patient", "dob": ""}

        issues = find_issues(meds, labs)
        n_dup = int((issues.type == "Duplicate test").sum())

        st.subheader("📊 Step 3: Results")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Sources combined", meds.source.nunique())
        c2.metric("Unique medicines", meds.drug.nunique())
        c3.metric("High-severity issues", int((issues.severity == "High").sum()))
        cost = c4.number_input("Cost per test ($)", 0, 5000, 120, key="coord_cost")
        st.metric("Duplicate tests found → money saved", f"{n_dup} → ${n_dup * cost:,}")

        st.markdown("**⚠️ Safety & reconciliation issues**")
        if issues.empty:
            st.success("No issues found.")
        else:
            order = {"High": 0, "Medium": 1, "Low": 2}
            issues = issues.sort_values("severity", key=lambda s: s.map(order))
            st.dataframe(issues, hide_index=True, width="stretch")
        t1, t2, t3 = st.tabs(["💊 Unified medication list", "🧪 Lab timeline", "🚫 Allergies"])
        t1.dataframe(meds.sort_values("drug"), hide_index=True, width="stretch")
        t2.dataframe(labs.sort_values("date").assign(date=lambda d: d.date.dt.date), hide_index=True, width="stretch")
        t3.write(", ".join(allergies) or "None recorded / not provided")
        bundle = to_fhir_bundle(meds, labs, allergies, patient)
        st.download_button("⬇️ Export unified record (FHIR R4 Bundle, JSON)", json.dumps(bundle, indent=2),
                           "unified_record_fhir.json", mime="application/json")

    with dl:
        export_panel(
            "care_coordination", "Use Case 5: Care Coordination Report",
            [("Data sources", f"Medications: {meds_label}\nLabs: {labs_label}"),
             ("Summary", f"Sources: {meds.source.nunique()}; unique medicines: {meds.drug.nunique()}; "
                         f"issues: {len(issues)} (high: {int((issues.severity == 'High').sum())}); "
                         f"duplicate tests: {n_dup}, estimated saving ${n_dup * cost:,}.\n"
                         f"Allergies: {', '.join(allergies) or 'not provided'}"),
             ("How it was calculated",
              "Interaction: both drugs of a known risky pair present in the combined list. Dose mismatch: >1 distinct "
              "dose for the same drug. Duplicate test: same test <= 30 days apart at different sources. "
              "Saving = duplicates x cost per test.")],
            {"Issues": issues, "Unified medication list": meds,
             "Lab timeline": labs.assign(date=labs.date.dt.date)},
        )


# ============================================================================
# ROUTER
# ============================================================================
PAGES = {
    "🏠 Overview & impact": page_home,
    "1 · 📝 AI documentation & admin": page_documentation,
    "2 · 📈 Remote patient monitoring": page_rpm,
    "3 · 💻 Telehealth & virtual care": page_telehealth,
    "4 · 🧠 Mental health support": page_mental_health,
    "5 · 🔗 Records & care coordination": page_coordination,
}

with st.sidebar:
    st.markdown(f"<div style='font-size:1.6rem;font-weight:800;color:#0b5ed7;'>🩺 {APP_NAME}</div>"
                f"<div style='font-weight:700;color:#0b5ed7;'>{DEVELOPER}</div>", unsafe_allow_html=True)
    st.caption("Pick a use case:")
    page = st.radio("Module", list(PAGES), label_visibility="collapsed")
    st.divider()
    st.markdown("**Each page has 3 tabs:**\n\n1️⃣ Learn · 2️⃣ Try it · 3️⃣ Download")
    st.divider()
    st.caption(DISCLAIMER)

brand_banner()
PAGES[page]()