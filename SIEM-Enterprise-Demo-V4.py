


# ============================================================
# SIEM ENTERPRISE PLATFORM
# SOC | UEBA | RMF | FedRAMP | Cloud SIEM
# Developed by Randy Singh – Kalsnet (KNet)
# ============================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime
import time
import io
import numpy as np

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------
st.set_page_config(
    layout="wide",
    page_title="SIEM Enterprise Platform",
    page_icon="🛡️"
)

# ------------------------------------------------------------
# RBAC
# ------------------------------------------------------------
ROLES = ["Admin", "SOC Analyst", "Viewer"]
role = st.sidebar.selectbox("🔐 Select Role", ROLES)

def require_role(allowed):
    return role in allowed

# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------
st.markdown("""
<div style="background:#0A3D91;padding:20px;border-radius:14px;">
<h1 style="color:white;text-align:center;font-weight:800;">
SIEM Enterprise Platform
</h1>
<h3 style="color:#D6E4FF;text-align:center;">
SOC • UEBA • RMF • FedRAMP • Cloud SIEM
</h3>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ------------------------------------------------------------
# SIDEBAR CONTROLS
# ------------------------------------------------------------
st.sidebar.header("🛠️ Controls")

records = st.sidebar.slider("Synthetic Events", 50, 500, 100)
cloud_source = st.sidebar.selectbox(
    "📡 Ingestion Source",
    ["Synthetic", "Kafka", "AWS CloudWatch", "Azure Sentinel"]
)

realtime = st.sidebar.toggle("📡 Controlled Real-Time Simulation")

if require_role(["Admin"]):
    uploaded_file = st.sidebar.file_uploader("📂 Upload Logs (CSV)", type=["csv"])
else:
    uploaded_file = None

if require_role(["Admin"]) and st.sidebar.button("🔄 Reset System"):
    st.session_state.clear()
    st.rerun()

# ------------------------------------------------------------
# DATA INGESTION LAYER
# ------------------------------------------------------------
def ingest_logs(n, source):
    logs = []
    for _ in range(n):
        logs.append([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            f"192.168.1.{random.randint(1,50)}",
            f"user{random.randint(1,15)}",
            random.choice(["LOGIN","PRIV_ESC","NETWORK"]),
            random.choice(["SUCCESS","FAILED"]),
            source
        ])
    return pd.DataFrame(logs, columns=[
        "timestamp","source_ip","username",
        "event_type","status","ingestion_source"
    ])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = ingest_logs(records, cloud_source)

# ------------------------------------------------------------
# LOG DISPLAY
# ------------------------------------------------------------
st.subheader("📥 Security Events")
st.dataframe(df, use_container_width=True)

# ------------------------------------------------------------
# UEBA SCORING (ML-LITE)
# ------------------------------------------------------------
st.subheader("🧠 UEBA Risk Scoring")

ueba = df.groupby("username").agg(
    failed_logins=("status", lambda x: (x=="FAILED").sum()),
    event_volume=("event_type","count"),
    priv_events=("event_type", lambda x: (x=="PRIV_ESC").sum())
).reset_index()

ueba["risk_score"] = (
    ueba["failed_logins"] * 2 +
    ueba["event_volume"] * 0.2 +
    ueba["priv_events"] * 5
)

st.dataframe(ueba, use_container_width=True)

# ------------------------------------------------------------
# ALERT GENERATION
# ------------------------------------------------------------
alerts = []

for _, r in ueba.iterrows():
    if r["risk_score"] >= 25:
        alerts.append([
            "UEBA Anomaly",
            r["username"],
            "Critical",
            "IR-5, AU-6",
            "T1078"
        ])

alert_df = pd.DataFrame(alerts, columns=[
    "Alert Type","Entity","Severity","NIST 800-53","MITRE ATT&CK"
])

st.subheader("🚨 Alerts")
st.dataframe(alert_df, use_container_width=True)

# ------------------------------------------------------------
# RMF / ATO MAPPING
# ------------------------------------------------------------
st.subheader("🧾 RMF / ATO Control Traceability")

rmf = pd.DataFrame([
    ["Log Collection","AU-2","FedRAMP Moderate"],
    ["Correlation","AU-6","FedRAMP Moderate"],
    ["UEBA","IR-5","High Impact"],
    ["Response","IR-4","ATO Required"]
], columns=["Capability","NIST Control","ATO Impact"])

st.dataframe(rmf, use_container_width=True)

# ------------------------------------------------------------
# EXPORTS
# ------------------------------------------------------------
if require_role(["Admin","SOC Analyst"]):
    st.subheader("📤 Compliance Exports")

    csv_buf = io.StringIO()
    rmf.to_csv(csv_buf, index=False)

    st.download_button(
        "⬇️ Download RMF CTM (CSV)",
        csv_buf.getvalue(),
        "rmf_ctm.csv"
    )

    def pdf_report():
        buf = io.BytesIO()
        doc = SimpleDocTemplate(buf)
        styles = getSampleStyleSheet()
        story = [Paragraph("ATO Security Report – Kalsnet", styles["Title"])]

        for _, r in rmf.iterrows():
            story.append(Paragraph(
                f"{r['Capability']} → {r['NIST Control']} ({r['ATO Impact']})",
                styles["Normal"]
            ))

        doc.build(story)
        buf.seek(0)
        return buf

    st.download_button(
        "⬇️ Download ATO PDF",
        pdf_report(),
        "ato_report.pdf"
    )

# ------------------------------------------------------------
# REAL-TIME SIMULATION (CONTROLLED)
# ------------------------------------------------------------
if realtime:
    if "ticks" not in st.session_state:
        st.session_state.ticks = 0

    st.session_state.ticks += 1
    st.info(f"📡 Simulation Cycle {st.session_state.ticks}")

    if st.session_state.ticks < 4:
        time.sleep(1)
        st.rerun()
    else:
        st.success("✅ Real-Time Simulation Completed")
