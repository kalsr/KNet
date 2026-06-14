import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random
import json
import io
from datetime import datetime, timedelta

# ─── Optional export dependencies ─────────────────────────────────────────────
try:
    from fpdf import FPDF
    FPDF_AVAILABLE = True
except ImportError:
    FPDF_AVAILABLE = False

try:
    from docx import Document as DocxDocument
    from docx.shared import RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    DOCX_AVAILABLE = True
except ImportError:
    DOCX_AVAILABLE = False

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE CONFIG
# ══════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Zero-Trust Framework | KNet Consulting",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════════════════════
#  GLOBAL STYLES — Enhanced Deep Blue Federal Theme
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    """
<style>
  body {
      background-color: #f4f7fc;
      font-family: "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  }
  .zt-title {
      text-align: center; font-size: 3.0rem; font-weight: 1000;
      color: #002b80; letter-spacing: 1.5px; margin-bottom: 0;
  }
  .zt-subtitle {
      text-align: center; font-size: 1.25rem; font-weight: 800;
      color: #0047AB; margin-top: 6px; margin-bottom: 8px;
  }
  .zt-tagline {
      text-align: center; color: #444; font-size: 1rem; margin-bottom: 24px;
  }
  .zt-hr { border: 3px solid #003087; margin: 12px 0 26px 0; }

  .section-header {
      background: linear-gradient(90deg, #002b80 0%, #1a6fe8 100%);
      color: white; padding: 14px 22px; border-radius: 10px;
      font-weight: 800; font-size: 1.25rem; margin: 18px 0 12px 0;
      box-shadow: 0 3px 8px rgba(0,0,0,0.22);
  }

  .req-card, .rec-card, .sol-card {
      border-radius: 10px; padding: 12px 16px; margin: 8px 0;
      font-size: 0.95rem; box-shadow: 0 2px 6px rgba(0,0,0,0.10);
  }
  .req-card { background: #e8f0ff; border-left: 5px solid #0047AB; }
  .rec-card { background: #fff4d6; border-left: 5px solid #f0a500; }
  .sol-card { background: #e6f7e9; border-left: 5px solid #2e7d32; }

  div[data-testid="metric-container"] {
      background: #f0f6ff; border: 1px solid #c2d9ff;
      border-radius: 12px; padding: 14px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.10);
  }

  section[data-testid="stSidebar"] {
      background: #001a6b;
  }
  section[data-testid="stSidebar"] * {
      color: #e8f0ff !important;
  }

  .sidebar-box {
      background: rgba(255,255,255,0.08);
      padding: 12px 14px;
      border-radius: 10px;
      margin-bottom: 14px;
      border: 1px solid rgba(255,255,255,0.15);
  }

  .sidebar-footer {
      font-size: 0.8rem;
      color: #cbd4ff;
      text-align: center;
      margin-top: 12px;
  }
</style>
""",
    unsafe_allow_html=True,
)

# ══════════════════════════════════════════════════════════════════════════════
#  HEADER — Enhanced
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<p class="zt-title">ZERO-TRUST FRAMEWORK APPLICATION</p>', unsafe_allow_html=True)
st.markdown('<p class="zt-subtitle">Developed by Randy Singh | KalSnet (KNet) Consulting Group</p>', unsafe_allow_html=True)
st.markdown('<p class="zt-tagline">Based on DISA/BDE5 ZTA Working Group Requirements & Use Cases | Originally authored April 2019</p>', unsafe_allow_html=True)
st.markdown('<hr class="zt-hr">', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  DATA DEFINITIONS (YOUR ORIGINAL CONTENT)
# ══════════════════════════════════════════════════════════════════════════════

# (KEEP YOUR FUNCTIONAL_REQUIREMENTS, USE_CASES, ARCHITECTURAL_REQUIREMENTS, EVALUATION_CRITERIA HERE)
# I am not repeating them to save space — paste them exactly as in your file.

# ══════════════════════════════════════════════════════════════════════════════
#  SYNTHETIC DATA GENERATOR
# ══════════════════════════════════════════════════════════════════════════════
@st.cache_data
def generate_synthetic_data(n: int) -> pd.DataFrame:
    random.seed(42)
    pillars = ["Identity & Auth", "Health & Compliance", "Authorization", "Accounting", "Segmentation", "Orchestration"]
    device_types = ["Workstation", "Server", "Mobile", "IoT Sensor", "Network Device", "Cloud VM"]
    departments = ["CYBERCOM", "DISA/BDE5", "TRANSCOM", "DIA", "NSA", "SOCOM", "CENTCOM", "EUCOM"]
    statuses = ["Compliant", "Non-Compliant", "Remediation", "Pending Review"]
    status_weights = [0.60, 0.20, 0.12, 0.08]
    os_list = ["Windows 11 STIG", "RHEL 9 STIG", "macOS Ventura", "Ubuntu 22.04 LTS", "Windows Server 2022"]
    base_date = datetime(2024, 1, 1)
    records = []

    for i in range(1, n + 1):
        status = random.choices(statuses, weights=status_weights)[0]
        score = random.randint(60, 100) if status == "Compliant" else random.randint(20, 59)
        records.append({
            "Record_ID": f"ZT-{i:04d}",
            "Timestamp": base_date + timedelta(days=random.randint(0, 364), hours=random.randint(0, 23)),
            "Pillar": random.choice(pillars),
            "Device_Type": random.choice(device_types),
            "Department": random.choice(departments),
            "OS": random.choice(os_list),
            "Compliance_Status": status,
            "STIG_Score": score,
            "Auth_Latency_ms": random.randint(45, 380),
            "Patch_Age_Days": random.randint(0, 90),
            "MFA_Enabled": random.choice([True, True, True, False]),
            "Segmentation_Policy_Applied": random.choice([True, True, False]),
            "Incident_Flagged": status == "Non-Compliant" and random.random() < 0.4,
        })
    return pd.DataFrame(records)

# ══════════════════════════════════════════════════════════════════════════════
#  EXPORT HELPERS — FIXED PDF GENERATOR
# ══════════════════════════════════════════════════════════════════════════════
def _pdf_safe(text: str) -> str:
    replacements = [
        ("\u2013", "-"), ("\u2014", "--"), ("\u2018", "'"), ("\u2019", "'"),
        ("\u201c", '"'), ("\u201d", '"'), ("\u2026", "..."), ("\u2022", "*"),
        ("\u00a0", " "), ("\u2265", ">="), ("\u2264", "<=")
    ]
    for char, replacement in replacements:
        text = text.replace(char, replacement)
    return text.encode("latin-1", errors="ignore").decode("latin-1")

def build_text_report(category, content):
    lines = [f"ZERO TRUST REPORT — {category}", "="*60, ""]
    for k, v in content.items():
        lines.append(f"[{k}]")
        if isinstance(v, list):
            for item in v:
                lines.append(f" - {item}")
        elif isinstance(v, dict):
            for k2, v2 in v.items():
                lines.append(f"  {k2}: {v2}")
        else:
            lines.append(str(v))
        lines.append("")
    return "\n".join(lines)

def build_json_report(category, content):
    return json.dumps({"category": category, "data": content}, indent=2)

def build_pdf_bytes(category, content):
    if not FPDF_AVAILABLE:
        return b""
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 16)
        pdf.multi_cell(0, 10, _pdf_safe(f"ZERO TRUST REPORT — {category}"))
        pdf.set_font("Helvetica", "", 11)

        for k, v in content.items():
            pdf.ln(4)
            pdf.set_font("Helvetica", "B", 12)
            pdf.multi_cell(0, 8, _pdf_safe(str(k)))
            pdf.set_font("Helvetica", "", 10)

            if isinstance(v, list):
                for item in v:
                    pdf.multi_cell(0, 6, _pdf_safe(f" - {item}"))
            elif isinstance(v, dict):
                for k2, v2 in v.items():
                    pdf.multi_cell(0, 6, _pdf_safe(f"{k2}: {v2}"))
            else:
                pdf.multi_cell(0, 6, _pdf_safe(str(v)))

        return pdf.output(dest="S").encode("latin-1", "ignore")
    except:
        return b"%PDF-1.4\n%EOF"

def build_docx_bytes(category, content):
    if not DOCX_AVAILABLE:
        return b""
    doc = DocxDocument()
    doc.add_heading(f"ZERO TRUST REPORT — {category}", 0)
    for k, v in content.items():
        doc.add_heading(str(k), level=2)
        if isinstance(v, list):
            for item in v:
                doc.add_paragraph(str(item), style="List Bullet")
        elif isinstance(v, dict):
            for k2, v2 in v.items():
                doc.add_paragraph(f"{k2}: {v2}")
        else:
            doc.add_paragraph(str(v))
    buf = io.BytesIO()
    doc.save(buf)
    return buf.getvalue()

# ══════════════════════════════════════════════════════════════════════════════
#  SIDEBAR — NAVIGATION
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("## ZTA Navigator")
    st.markdown("---")

    category = st.radio(
        "Select Framework Category",
        [
            "Overview & Architecture Diagram",
            "1. Functional Requirements",
            "2. Proposed Use Cases",
            "3. Architectural Requirements",
            "4. Evaluation Criteria",
            "Synthetic Data & Analytics",
        ],
        index=0,
    )

    st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
    st.markdown("**About**")
    st.markdown("Randy Singh  \nComputer Scientist  \nDISA / BDE5  \nKalSnet (KNet) Consulting")
    st.markdown("`(301) 225-9535`")
    st.markdown("</div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  MAIN CONTENT RENDERING
# ══════════════════════════════════════════════════════════════════════════════
export_payload = {}

# ─── Overview & Architecture Diagram ──────────────────────────────────────────
if category == "Overview & Architecture Diagram":
    st.markdown('<div class="section-header">Zero-Trust Overview & Reference Architecture</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1.4, 1])

    with col1:
        st.markdown("""
### Zero-Trust Tenets
- **Never trust, always verify**
- **Assume breach**
- **Least privilege**
- **Data-centric security**

### DISA / BDE5 Context
This framework aligns with DISA/BDE5 ZTA Working Group guidance and DoD reference architectures.
""")

    with col2:
        st.markdown("""
### Logical Architecture Layers
- Identity & Authentication  
- Health & Compliance  
- Authorization & Accounting  
- Segmentation & Orchestration  
""")

    st.markdown('<div class="section-header">High-Level Architecture Diagram</div>', unsafe_allow_html=True)

    arch_fig = go.Figure()

    arch_fig.add_trace(go.Scatter(
        x=[1, 2, 3, 4],
        y=[4, 4, 4, 4],
        mode="markers+text",
        text=["Identity Provider", "MFA / PKI", "NAC / EDR", "PAM / JIT"],
        textposition="top center",
        marker=dict(size=28, color="#003087"),
        textfont=dict(size=14, color="black")
    ))

    arch_fig.add_trace(go.Scatter(
        x=[1, 2, 3],
        y=[2, 2, 2],
        mode="markers+text",
        text=["SDN / Micro-Segmentation", "Policy Engine", "SIEM / UEBA"],
        textposition="top center",
        marker=dict(size=28, color="#f0a500"),
        textfont=dict(size=14, color="black")
    ))

    arch_fig.update_layout(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        height=450,
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor="#f4f7fc",
        paper_bgcolor="#f4f7fc",
    )

    st.plotly_chart(arch_fig, use_container_width=True)

    export_payload = {"Overview": ["Zero-Trust Architecture Overview"]}

# ─── Functional Requirements ──────────────────────────────────────────────────
elif category == "1. Functional Requirements":
    st.markdown('<div class="section-header">Zero-Trust Functional Requirements</div>', unsafe_allow_html=True)

    for pillar, details in FUNCTIONAL_REQUIREMENTS.items():
        st.markdown(f"## {pillar}")
        st.markdown(f'<div class="req-card"><b>Requirement:</b> {details["requirement"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="sol-card"><b>Solution:</b> {details["solution"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="rec-card"><b>Recommendation:</b> {details["recommendation"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="req-card"><b>Example:</b> {details["example"]}</div>', unsafe_allow_html=True)

    export_payload = FUNCTIONAL_REQUIREMENTS

# ─── Proposed Use Cases ───────────────────────────────────────────────────────
elif category == "2. Proposed Use Cases":
    st.markdown('<div class="section-header">Proposed Zero-Trust Use Cases</div>', unsafe_allow_html=True)

    for uc_name, steps in USE_CASES.items():
        st.markdown(f"## {uc_name}")
        for step in steps:
            st.markdown(f"- {step}")

    export_payload = USE_CASES

# ─── Architectural Requirements ───────────────────────────────────────────────
elif category == "3. Architectural Requirements":
    st.markdown('<div class="section-header">Architectural Requirements</div>', unsafe_allow_html=True)

    for req_group, items in ARCHITECTURAL_REQUIREMENTS.items():
        st.markdown(f"## {req_group}")
        for item in items:
            st.markdown(f"- {item}")

    export_payload = ARCHITECTURAL_REQUIREMENTS

# ─── Evaluation Criteria ──────────────────────────────────────────────────────
elif category == "4. Evaluation Criteria":
    st.markdown('<div class="section-header">Evaluation Criteria</div>', unsafe_allow_html=True)

    for key, crit in EVALUATION_CRITERIA.items():
        st.markdown(f"## {key}")
        st.markdown(f"**Definition:** {crit['definition']}")
        st.markdown("**Metrics:**")
        for m in crit["metrics"]:
            st.markdown(f"- {m}")
        st.markdown(f"**Target:** {crit['target']}")
        st.markdown(f"**Recommendation:** {crit['recommendation']}")

    export_payload = EVALUATION_CRITERIA

# ─── Synthetic Data & Analytics ───────────────────────────────────────────────
elif category == "Synthetic Data & Analytics":
    st.markdown('<div class="section-header">Synthetic ZTA Telemetry
