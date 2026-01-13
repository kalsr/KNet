

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
# Session State (SINGLE SOURCE OF TRUTH)
# ------------------------------------------------------------
if "df" not in st.session_state:
    st.session_state.df = None

# ------------------------------------------------------------
# Sidebar Controls
# ------------------------------------------------------------
st.sidebar.header("⚙️ Controls")

uploaded_file = st.sidebar.file_uploader(
    "Upload API Log File (.txt)", type=["txt"]
)

record_limit = st.sidebar.slider(
    "Records to Display",
    min_value=10,
    max_value=100,
    step=10,
    value=20
)

# RESET BUTTON — HARD RESET
with st.sidebar.container():
    st.markdown('<div class="reset-btn">', unsafe_allow_html=True)
    if st.button("RESET APPLICATION"):
        st.session_state.df = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------------------
# Load Log Data
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

    if (df["Status"] == "404").sum() >= 3:
        findings.append(
            "🔎 Excessive 404 responses indicate API endpoint probing. "
            "Mitigation: Hide endpoint structure, add WAF & rate limiting."
        )

    if df["Request"].str.contains("/login", case=False).sum() >= 3:
        findings.append(
            "🔐 Multiple login attempts detected. "
            "Mitigation: Enable MFA, account lockouts, CAPTCHA."
        )

    if len(df[df["Status"].isin(["401", "403", "500"])]) / len(df) > 0.3:
        findings.append(
            "⚠️ High error rate suggests abuse or misconfiguration. "
            "Mitigation: Improve monitoring and alerting."
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
# MAIN RENDER LOGIC (THIS IS THE FIX)
# ------------------------------------------------------------
if uploaded_file:
    st.session_state.df = load_log_data(uploaded_file)

# 🚨 NOTHING IS RENDERED UNLESS DATA EXISTS
if st.session_state.df is None:
    st.info("No data loaded. Upload a log file to begin.")
else:
    df = st.session_state.df

    # ✅ SLIDER CONTROLS WHAT IS DISPLAYED
    df_display = df.sample(
        min(record_limit, len(df)),
        random_state=random.randint(1, 100000)
    )

    # -------------------------------
    # Display Records
    # -------------------------------
    st.subheader("📄 API Log Records")
    st.dataframe(df_display, use_container_width=True)

    # -------------------------------
    # Analytics
    # -------------------------------
    st.subheader("📊 API Analytics")

    status_counts = df_display["Status"].value_counts()

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

    # -------------------------------
    # Anomaly Detection
    # -------------------------------
    st.subheader("🚨 Anomaly & Fraud Detection")

    anomalies = detect_anomalies(df_display)

    if anomalies:
        for a in anomalies:
            st.warning(a)
    else:
        st.success("No anomalies detected in this data slice.")

    # -------------------------------
    # Export
    # -------------------------------
    st.subheader("📤 Export")

    st.download_button(
        "Download Displayed Records (CSV)",
        df_display.to_csv(index=False).encode("utf-8"),
        "api_logs_displayed.csv",
        "text/csv"
    )

    summary = f"""
API SECURITY REPORT
-------------------
Displayed Records: {len(df_display)}

Status Distribution:
{status_counts.to_string()}

Anomalies:
{chr(10).join(anomalies) if anomalies else 'None detected'}
"""
    pdf_path = export_pdf(summary)

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
st.caption("© Kalsnet (KNet) Consulting Group – API Security Platform")
