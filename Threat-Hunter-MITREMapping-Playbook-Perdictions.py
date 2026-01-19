

# ============================================================
# KNet Cyber Threat Hunting Studio – Enterprise AI Edition
# Designed & Developed by Randy Singh
# Kalsnet (KNet) Consulting Group
# ============================================================

import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import io

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="KNet Cyber Threat Hunting Studio",
    layout="wide"
)

# ---------------- PROFESSIONAL CSS ----------------
st.markdown("""
<style>
body { background-color: #f8f9fa; }
.top-bar {
    background: linear-gradient(90deg, #0A3D62, #1B4F72);
    padding: 20px;
    border-radius: 10px;
    color: white;
    font-size: 32px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 25px;
}
.section-title {
    font-size: 22px;
    font-weight: 700;
    color: #0A3D62;
    margin-top: 25px;
}
.card {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="top-bar"> Kalsnet (KNet) Cyber Threat Hunting Studio – AI/ML Enterprise Platform</div>',
    unsafe_allow_html=True
)

# ---------------- MITRE ATT&CK MAP ----------------
MITRE_MAP = {
    "Suspicious Login": ("Credential Access", "T1110", "Brute Force"),
    "API Abuse": ("Impact", "T1499", "Endpoint Denial of Service"),
    "Command Abuse": ("Execution", "T1059", "Command-Line Interface"),
    "Data Exfiltration": ("Exfiltration", "T1041", "Exfiltration Over C2 Channel")
}

# ---------------- SESSION STATE ----------------
for key in ["data", "results", "ml_results"]:
    if key not in st.session_state:
        st.session_state[key] = None if key != "data" else pd.DataFrame()

# ---------------- DATA GENERATION ----------------
def generate_synthetic_data(count):
    return pd.DataFrame([{
        "user": random.choice(["alice", "bob", "charlie", "admin", "service"]),
        "login_hour": random.randint(0, 23),
        "failed_attempts": random.randint(0, 10),
        "api_calls": random.randint(10, 500),
        "command_entropy": round(random.uniform(1.0, 7.5), 2),
        "data_out_mb": random.randint(1, 1200)
    } for _ in range(count)])

# ---------------- RULE-BASED THREAT HUNTING ----------------
def hunt_threats(df):
    return {
        "Suspicious Login": df[(df.login_hour < 6) | (df.failed_attempts > 5)],
        "API Abuse": df[df.api_calls > 300],
        "Command Abuse": df[df.command_entropy > 6.0],
        "Data Exfiltration": df[df.data_out_mb > 700]
    }

# ---------------- ML PREDICTIONS ----------------
def run_ml_predictions(df):
    features = df[
        ["login_hour", "failed_attempts", "api_calls", "command_entropy", "data_out_mb"]
    ]

    model = IsolationForest(
        n_estimators=150,
        contamination=0.15,
        random_state=42
    )

    preds = model.fit_predict(features)
    scores = model.decision_function(features)

    df_ml = df.copy()
    df_ml["ML_Prediction"] = ["Anomalous" if p == -1 else "Normal" for p in preds]
    df_ml["Anomaly_Score"] = scores

    return df_ml

# ---------------- RECORD EXPLANATION ----------------
def explain_record(r):
    reasons = []
    if r.login_hour < 6 or r.failed_attempts > 5:
        reasons.append("Abnormal login timing or repeated authentication failures")
    if r.api_calls > 300:
        reasons.append("Excessive API request volume")
    if r.command_entropy > 6.0:
        reasons.append("High command entropy indicating automation or obfuscation")
    if r.data_out_mb > 700:
        reasons.append("Large outbound data transfer volume")
    return reasons or ["No risk indicators detected"]

# ---------------- AI REMEDIATION PLAYBOOKS ----------------
def ai_playbook(threat):
    playbooks = {
        "Suspicious Login": "Enforce MFA, lock accounts, review auth logs, rotate credentials.",
        "API Abuse": "Enable rate limiting, rotate API keys, enforce OAuth scopes.",
        "Command Abuse": "Isolate host, enable EDR, block unauthorized shells.",
        "Data Exfiltration": "Enable DLP, block egress traffic, assess data exposure."
    }
    return playbooks.get(threat, "No remediation guidance available.")

# ---------------- PDF REPORT ----------------
def generate_pdf(results):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    content = [Paragraph("KNet Executive Cyber Threat Report", styles["Title"])]

    for threat, records in results.items():
        if not records.empty:
            tactic, tid, name = MITRE_MAP[threat]
            content.append(
                Paragraph(
                    f"<b>{threat}</b><br/>"
                    f"Records: {len(records)}<br/>"
                    f"MITRE: {tactic} – {tid} ({name})",
                    styles["Normal"]
                )
            )

    doc.build(content)
    buffer.seek(0)
    return buffer

# ====================== UI ======================

st.markdown('<div class="section-title"> Data Ingestion</div>', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)

with c1:
    count = st.slider("Synthetic Records", 50, 500, 150)

with c2:
    if st.button("Generate Data"):
        st.session_state.data = generate_synthetic_data(count)
        st.session_state.results = None
        st.session_state.ml_results = None

with c3:
    upload = st.file_uploader("Upload CSV", type="csv")
    if upload:
        st.session_state.data = pd.read_csv(upload)
        st.session_state.results = None
        st.session_state.ml_results = None

with c4:
    if st.button("Reset Platform"):
        st.session_state.data = pd.DataFrame()
        st.session_state.results = None
        st.session_state.ml_results = None
        st.rerun()

# ---------------- DATA DISPLAY ----------------
if not st.session_state.data.empty:
    st.markdown('<div class="section-title"> Loaded Records</div>', unsafe_allow_html=True)
    st.dataframe(st.session_state.data, use_container_width=True, height=300)

    c5, c6 = st.columns(2)
    with c5:
        if st.button(" Run Threat Hunting"):
            st.session_state.results = hunt_threats(st.session_state.data)
    with c6:
        if st.button(" Run AI/ML Predictions"):
            st.session_state.ml_results = run_ml_predictions(st.session_state.data)

# ---------------- THREAT RESULTS ----------------
if st.session_state.results:
    st.markdown('<div class="section-title"> Threat Distribution</div>', unsafe_allow_html=True)

    labels = []
    sizes = []
    for k, v in st.session_state.results.items():
        if not v.empty:
            labels.append(f"{k} ({len(v)})")
            sizes.append(len(v))

    if sizes:
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

    st.markdown('<div class="section-title"> MITRE ATT&CK Mapping</div>', unsafe_allow_html=True)
    for threat, records in st.session_state.results.items():
        if not records.empty:
            tactic, tid, name = MITRE_MAP[threat]
            st.markdown(
                f"**{threat}** → {tactic} | {tid} | {name}  \n"
                f"**Records:** {list(records.index)}"
            )

    st.markdown('<div class="section-title"> AI Remediation Playbooks</div>', unsafe_allow_html=True)
    for threat, records in st.session_state.results.items():
        if not records.empty:
            st.markdown(f"**{threat}:** {ai_playbook(threat)}")

# ---------------- ML RESULTS ----------------
if st.session_state.ml_results is not None:
    st.markdown('<div class="section-title"> AI/ML Anomaly Predictions</div>', unsafe_allow_html=True)
    st.dataframe(st.session_state.ml_results, use_container_width=True, height=300)

    anomalies = st.session_state.ml_results[
        st.session_state.ml_results["ML_Prediction"] == "Anomalous"
    ]
    if not anomalies.empty:
        st.warning(f" Anomalous Records Detected: {list(anomalies.index)}")
    else:
        st.success(" No anomalies detected by ML model.")

# ---------------- RECORD EXPLANATION ----------------
if not st.session_state.data.empty:
    st.markdown('<div class="section-title"> Explain a Record</div>', unsafe_allow_html=True)
    idx = st.selectbox("Select Record #", st.session_state.data.index)
    st.write(explain_record(st.session_state.data.loc[idx]))

# ---------------- PDF ----------------
if st.session_state.results:
    st.markdown('<div class="section-title"> Executive Report</div>', unsafe_allow_html=True)
    pdf = generate_pdf(st.session_state.results)
    st.download_button(
        "Download Executive PDF Report",
        pdf,
        file_name="KNet_Executive_Threat_Report.pdf"
    )

st.markdown("---")
st.markdown("**© Randy Singh – Kalsnet (KNet) Consulting Group**")

