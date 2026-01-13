

# ============================================================
# API Simulation & Security Analytics Platform
# Developed by Randy Singh
# Kalsnet (KNet) Consulting Group
# ============================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
import tempfile
import random

# ------------------------------------------------------------
# Page Config
# ------------------------------------------------------------
st.set_page_config(page_title="API Simulation Platform", layout="wide")

# ------------------------------------------------------------
# Custom CSS
# ------------------------------------------------------------
st.markdown("""
<style>
.title-bar {
    font-size: 38px;
    font-weight: 800;
    color: #0B5ED7;
}
.reset-btn button {
    background-color: #DC3545 !important;
    color: white !important;
    font-weight: bold;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# Title
# ------------------------------------------------------------
st.markdown(
    '<div class="title-bar">🔐 API Simulation & Security Analytics Platform</div>',
    unsafe_allow_html=True
)
st.markdown(
    "**Developed by Randy Singh – Kalsnet (KNet) Consulting Group**"
)
st.divider()

# ------------------------------------------------------------
# Session State
# ------------------------------------------------------------
if "df" not in st.session_state:
    st.session_state.df = None

if "mode" not in st.session_state:
    st.session_state.mode = None  # "synthetic" or "upload"

# ------------------------------------------------------------
# Sidebar Controls
# ------------------------------------------------------------
st.sidebar.header("⚙️ Controls")

synthetic_count = st.sidebar.slider(
    "Generate Synthetic Records",
    min_value=0,
    max_value=100,
    step=10,
    value=0
)

uploaded_file = st.sidebar.file_uploader(
    "Upload API Log File (.txt)",
    type=["txt"]
)

# RESET BUTTON
with st.sidebar.container():
    st.markdown('<div class="reset-btn">', unsafe_allow_html=True)
    if st.button("RESET APPLICATION"):
        st.session_state.df = None
        st.session_state.mode = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------------------
# Synthetic Data Generator (ANOMALY HEAVY)
# ------------------------------------------------------------
def generate_synthetic_data(n):
    endpoints = [
        "/api/login", "/api/data", "/api/user", "/api/admin",
        "/api/delete", "/api/update", "/api/unknown"
    ]
    statuses = ["200", "401", "403", "404", "500"]

    records = []

    for i in range(n):
        endpoint = random.choice(endpoints)

        # Bias toward anomalies
        if endpoint in ["/api/admin", "/api/unknown"]:
            status = random.choice(["401", "403", "404"])
        elif endpoint == "/api/login":
            status = random.choice(["200", "401", "401", "401"])
        else:
            status = random.choice(statuses)

        response = {
            "200": "OK",
            "401": "Unauthorized",
            "403": "Forbidden",
            "404": "Not Found",
            "500": "Server Error"
        }[status]

        records.append({
            "Request": f"GET {endpoint}",
            "Response": f"{status} {response}",
            "Status": status
        })

    return pd.DataFrame(records)

# ------------------------------------------------------------
# Load Uploaded Log Data
# ------------------------------------------------------------
def load_log_data(file):
    rows = []
    for line in file:
        line = line.decode("utf-8").strip()
        if "|" not in line:
            continue
        req, res = line.split("|", 1)
        status = res.strip().split()[0]
        rows.append({
            "Request": req.strip(),
            "Response": res.strip(),
            "Status": status
        })
    return pd.DataFrame(rows)

# ------------------------------------------------------------
# Anomaly Detection
# ------------------------------------------------------------
def detect_anomalies(df):
    findings = []

    if (df["Status"] == "404").sum() >= 5:
        findings.append(
            " Caution - Endpoint enumeration detected (many 404s). "
            "Fix: Disable unused endpoints, add WAF, rate limit."
        )

    if df["Request"].str.contains("/login").sum() >= 4:
        findings.append(
            " Caution - Brute-force login behavior detected. "
            "Fix: MFA, CAPTCHA, account lockout."
        )

    if len(df[df["Status"].isin(["401", "403", "500"])]) / len(df) > 0.4:
        findings.append(
            "Caution - High error rate indicates abuse or misconfiguration. "
            "Fix: Improve authentication, monitoring, alerts."
        )

    return findings

# ------------------------------------------------------------
# PDF Export
# ------------------------------------------------------------
def export_pdf(text):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    c = canvas.Canvas(tmp.name, pagesize=LETTER)
    t = c.beginText(40, 750)
    t.setFont("Helvetica", 10)
    for line in text.split("\n"):
        t.textLine(line)
    c.drawText(t)
    c.showPage()
    c.save()
    return tmp.name

# ------------------------------------------------------------
# DATA MODE SELECTION
# ------------------------------------------------------------
if uploaded_file:
    st.session_state.df = load_log_data(uploaded_file)
    st.session_state.mode = "upload"

elif synthetic_count > 0:
    st.session_state.df = generate_synthetic_data(synthetic_count)
    st.session_state.mode = "synthetic"

# ------------------------------------------------------------
# RENDER UI ONLY IF DATA EXISTS
# ------------------------------------------------------------
if st.session_state.df is None:
    st.info("Use the slider to generate synthetic data or upload a log file.")
else:
    df = st.session_state.df

    st.subheader(" API Records")
    st.dataframe(df, use_container_width=True)

    st.subheader("Analysis -  API Analytics")
    status_counts = df["Status"].value_counts()

    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots()
        status_counts.plot(kind="bar", ax=ax1)
        ax1.set_xlabel("Status Code")
        ax1.set_ylabel("Count")
        st.pyplot(fig1)

    with col2:
        fig2, ax2 = plt.subplots()
        ax2.pie(
            status_counts,
            labels=status_counts.index,
            autopct="%1.1f%%",
            startangle=90
        )
        ax2.axis("equal")
        st.pyplot(fig2)

    st.subheader(" Anomaly & Fraud Detection")
    anomalies = detect_anomalies(df)

    for a in anomalies:
        st.warning(a)

    st.subheader(" Export")

    st.download_button(
        "Download CSV",
        df.to_csv(index=False).encode("utf-8"),
        "api_logs.csv",
        "text/csv"
    )

    pdf_text = f"""
API SECURITY REPORT
-------------------
Mode: {st.session_state.mode}
Records: {len(df)}

Status Distribution:
{status_counts.to_string()}

Anomalies:
{chr(10).join(anomalies)}
"""
    pdf_path = export_pdf(pdf_text)

    with open(pdf_path, "rb") as f:
        st.download_button(
            "Download Security Report (PDF)",
            f,
            "api_security_report.pdf",
            "application/pdf"
        )

# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------
st.divider()
st.caption("© Kalsnet (KNet) Consulting Group – API Simulation Platform")

