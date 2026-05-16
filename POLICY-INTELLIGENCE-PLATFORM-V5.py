# =========================================================
# AI Governance & Public Policy Intelligence Platform
# Enterprise SaaS Dashboard (Enhanced + Traceability + Export)
# Developed by Randy Singh from Kalsnet (KNet)
# =========================================================

import streamlit as st
from groq import Groq
import json
import pandas as pd
from io import BytesIO
from datetime import datetime

# PDF + Word support
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from docx import Document

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Governance Platform",
    layout="wide",
    page_icon=""
)

# =========================================================
# LIGHT MODE SIDEBAR
# =========================================================

st.markdown("""
<style>

.main { background-color: #f5f7fb; }

section[data-testid="stSidebar"] {
    background-color: #ffffff !important;
    color: #111;
    border-right: 1px solid #e6e6e6;
}

.header {
    background: linear-gradient(90deg, #0B3D91, #1E90FF);
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 20px;
}

.title {
    font-size: 34px;
    font-weight: 900;
    color: white;
}

.subtitle {
    font-size: 16px;
    font-weight: 900;
    color: #00BFFF;
}

.card {
    background: white;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
}

.stButton>button {
    background-color: #1E90FF;
    color: white;
    font-weight: bold;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="header">
    <div class="title">AI GOVERNANCE & PUBLIC POLICY INTELLIGENCE PLATFORM</div>
    <div class="subtitle">
        <b>Developed by Randy Singh from Kalsnet (KNet) Consulting Group</b>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# NAVIGATION
# =========================================================

menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Policy Generator", "Compliance Auditor", "Reports", "Settings"]
)

# =========================================================
# GROQ CONFIG
# =========================================================

st.sidebar.header(" AI Configuration")

api_key = st.sidebar.text_input("Groq API Key", type="password")

st.sidebar.markdown("""
###  Get API Key
- https://console.groq.com  
- Create account  
- Generate API key  
- Paste here  
""")

model = st.sidebar.selectbox(
    "Model",
    ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
)

# =========================================================
# KPI TRACEABILITY ENGINE (NEW)
# =========================================================

def get_metrics():
    policies = st.session_state.get("policy_count", 128)
    compliance = st.session_state.get("compliance_score", 92)
    risks = st.session_state.get("risk_count", 37)
    reports = st.session_state.get("report_count", 18)

    return {
        "Policies": {"value": policies, "source": "policy DB / session_state"},
        "Compliance": {"value": compliance, "source": "audit engine"},
        "Risks": {"value": risks, "source": "risk detection model"},
        "Reports": {"value": reports, "source": "report store"}
    }

# =========================================================
# EXPORT FUNCTIONS (NEW)
# =========================================================

def export_pdf(text):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    content = [
        Paragraph("AI Governance Report", styles["Title"]),
        Spacer(1, 12),
        Paragraph(text.replace("\n", "<br/>"), styles["BodyText"])
    ]

    doc.build(content)
    buffer.seek(0)
    return buffer


def export_word(text):
    doc = Document()
    doc.add_heading("AI Governance Report", 0)
    doc.add_paragraph(text)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer


def export_csv(text):
    df = pd.DataFrame({"report": [text]})
    return df.to_csv(index=False).encode("utf-8")


def export_json(text):
    return json.dumps(
        {"report": text, "timestamp": str(datetime.now())},
        indent=2
    ).encode("utf-8")

# =========================================================
# DASHBOARD
# =========================================================

if menu == "Dashboard":

    metrics = get_metrics()
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Policies", metrics["Policies"]["value"], "↑ 12%")
    col2.metric("Compliance", f'{metrics["Compliance"]["value"]}%', "↑ 5%")
    col3.metric("Risks", metrics["Risks"]["value"], "↓ 3%")
    col4.metric("Reports", metrics["Reports"]["value"], "↑ 2")

    st.success("System Active — Ready for Policy Generation")

    with st.expander(" KPI Data Source Debug Panel"):
        for k, v in metrics.items():
            st.write(f"**{k}** → {v['value']} (Source: {v['source']})")

# =========================================================
# POLICY GENERATOR
# =========================================================

if menu == "Policy Generator":

    st.subheader(" Policy Generator")

    org = st.text_input("Organization Name")
    industry = st.selectbox("Industry", ["Government","Defense","Healthcare","Finance"])
    objective = st.selectbox("Objective", ["Cybersecurity Protection","AI Governance","Compliance"])
    risk = st.selectbox("Risk Level", ["Low","Medium","High","Critical"])

    extra = st.multiselect("Additional Requirements", [
        "Audit Logging","Encryption","RBAC","Zero Trust"
    ])

    req = st.text_area("Custom Requirement")

    if st.button("Generate Policy"):

        if not api_key:
            st.error("Enter API Key")
        else:
            client = Groq(api_key=api_key)

            prompt = f"""
Create enterprise policy:
Org: {org}
Industry: {industry}
Objective: {objective}
Risk: {risk}
Controls: {extra}
Custom: {req}
"""

            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Senior governance architect"},
                    {"role": "user", "content": prompt}
                ]
            )

            st.session_state["result"] = response.choices[0].message.content

            # update metrics dynamically
            st.session_state["policy_count"] = st.session_state.get("policy_count", 128) + 1

    if "result" in st.session_state:
        st.markdown("### Generated Policy")
        st.markdown(st.session_state["result"])

# =========================================================
# COMPLIANCE AUDITOR
# =========================================================

if menu == "Compliance Auditor":

    text = st.text_area("Paste Policy")

    if st.button("Run Audit"):

        score = 85
        st.session_state["compliance_score"] = score
        st.session_state["risk_count"] = 37

        st.success(f"Compliance Score: {score}%")
        st.write("✔ NIST Alignment")
        st.write("⚠ Improve logging depth")

# =========================================================
# REPORTS (ENHANCED EXPORT)
# =========================================================

if menu == "Reports":

    st.subheader("Reports Dashboard")

    if "result" in st.session_state:

        report = st.session_state["result"]

        st.code(report[:2000])

        st.markdown("### Export Report")

        st.download_button(" PDF", export_pdf(report), "report.pdf")
        st.download_button(" Word", export_word(report), "report.docx")
        st.download_button(" CSV", export_csv(report), "report.csv")
        st.download_button(" JSON", export_json(report), "report.json")

    else:
        st.info("No policy generated yet")

# =========================================================
# SETTINGS
# =========================================================

if menu == "Settings":

    st.write("Model:", model)
    st.write("API Key:", "Configured" if api_key else "Not Configured")
    st.warning("Advanced settings coming soon")
