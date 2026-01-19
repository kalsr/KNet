# ============================================================
# KNet Cyber Threat Hunting Studio – Enterprise Edition
# Designed by Randy Singh – Kalsnet (KNet) Consulting Group
# ============================================================

import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import io

# ---------------- PAGE CONFIG ----------------
st.set_page_config(layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.top-bar {
    background-color:#0A3D62;
    padding:18px;
    border-radius:8px;
    color:white;
    font-size:30px;
    font-weight:800;
    text-align:center;
}
.section {
    margin-top:30px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="top-bar"> KNet Cyber Threat Hunting Studio</div>', unsafe_allow_html=True)

# ---------------- MITRE ATT&CK MAP ----------------
MITRE_MAP = {
    "Suspicious Login": ("Credential Access", "T1110", "Brute Force"),
    "API Abuse": ("Impact", "T1499", "Endpoint DoS"),
    "Command Abuse": ("Execution", "T1059", "Command-Line Interface"),
    "Data Exfiltration": ("Exfiltration", "T1041", "Exfiltration Over C2 Channel")
}

# ---------------- SESSION STATE ----------------
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame()

if "results" not in st.session_state:
    st.session_state.results = None

# ---------------- DATA GENERATION ----------------
def generate_synthetic_data(count):
    return pd.DataFrame([{
        "user": random.choice(["alice", "bob", "charlie", "admin"]),
        "login_hour": random.randint(0, 23),
        "failed_attempts": random.randint(0, 10),
        "api_calls": random.randint(10, 500),
        "command_entropy": round(random.uniform(1.0, 7.5), 2),
        "data_out_mb": random.randint(1, 1000)
    } for _ in range(count)])

# ---------------- THREAT HUNTING ----------------
def hunt_threats(df):
    return {
        "Suspicious Login": df[(df.login_hour < 6) | (df.failed_attempts > 5)],
        "API Abuse": df[df.api_calls > 300],
        "Command Abuse": df[df.command_entropy > 6.0],
        "Data Exfiltration": df[df.data_out_mb > 700]
    }

# ---------------- RECORD EXPLANATION ----------------
def explain_record(record):
    reasons = []
    if record.login_hour < 6 or record.failed_attempts > 5:
        reasons.append("Abnormal login time or excessive failures")
    if record.api_calls > 300:
        reasons.append("Excessive API calls")
    if record.command_entropy > 6.0:
        reasons.append("High command entropy")
    if record.data_out_mb > 700:
        reasons.append("Large outbound data transfer")
    return reasons or ["No threat indicators detected"]

# ---------------- PDF REPORT ----------------
def generate_pdf(results):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    content = [Paragraph("KNet Executive Threat Report", styles["Title"])]

    for threat, records in results.items():
        if len(records) > 0:
            tactic, tid, name = MITRE_MAP[threat]
            content.append(Paragraph(
                f"<b>{threat}</b><br/>"
                f"Records: {len(records)}<br/>"
                f"MITRE: {tactic} – {tid} ({name})",
                styles["Normal"]
            ))

    doc.build(content)
    buffer.seek(0)
    return buffer

# ---------------- DATA CONTROLS ----------------
st.markdown("###  Data Ingestion")

col1, col2, col3, col4 = st.columns(4)

with col1:
    record_count = st.slider("Synthetic Records", 50, 500, 150)

with col2:
    if st.button("Generate Data"):
        st.session_state.data = generate_synthetic_data(record_count)
        st.session_state.results = None

with col3:
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        st.session_state.data = pd.read_csv(uploaded)
        st.session_state.results = None

with col4:
    if st.button("Reset"):
        st.session_state.data = pd.DataFrame()
        st.session_state.results = None
        st.rerun()   #  FIXED

# ---------------- DISPLAY DATA ----------------
if not st.session_state.data.empty:
    st.markdown("###  Loaded Records")
    st.dataframe(st.session_state.data, use_container_width=True)

    if st.button(" Run Threat Hunting"):
        st.session_state.results = hunt_threats(st.session_state.data)

# ---------------- RESULTS ----------------
if st.session_state.results:
    results = st.session_state.results

    st.markdown("###  Threat Distribution")
    labels = [f"{k} ({len(v)})" for k, v in results.items() if len(v) > 0]
    sizes = [len(v) for v in results.values() if len(v) > 0]

    if sizes:
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct="%1.1f%%")
        st.pyplot(fig)

    st.markdown("### 🧩 MITRE ATT&CK Mapping")
    for threat, records in results.items():
        if len(records) > 0:
            tactic, tid, name = MITRE_MAP[threat]
            st.markdown(f"**{threat}** → {tactic} | {tid} | {name} | Records: {list(records.index)}")

    st.markdown("###  Explain a Record")
    selected = st.selectbox("Select Record #", st.session_state.data.index)
    st.write(explain_record(st.session_state.data.loc[selected]))

    st.markdown("### 📄 Executive Report")
    pdf = generate_pdf(results)
    st.download_button("Download PDF Report", pdf, file_name="KNet_Executive_Report.pdf")

else:
    st.info(" Generate or upload records, then click **Run Threat Hunting**.")

st.markdown("---")
st.markdown("**© Randy Singh – Kalsnet (KNet) Consulting Group**")
