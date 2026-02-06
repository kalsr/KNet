

# ============================================================
# SIEM ENTERPRISE PLATFORM
# SOC | UEBA | RMF | FedRAMP | Cloud SIEM
# Developed by Randy Singh
# Kalsnet (KNet) Consulting Group
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
    page_title="SIEM Enterprise Platform | Kalsnet (KNet)",
    page_icon=""
)

# ------------------------------------------------------------
# HEADER / TITLE BAR
# ------------------------------------------------------------
st.markdown("""
<div style="background:#0A3D91;padding:22px;border-radius:16px;">
<h1 style="color:white;text-align:center;font-weight:800;margin-bottom:4px;">
SIEM Enterprise Platform
</h1>
<h3 style="color:#D6E4FF;text-align:center;margin-top:0;">
Developed by Randy Singh – Kalsnet (KNet) Consulting Group
</h3>
<h4 style="color:#BFD4FF;text-align:center;margin-top:4px;">
SOC Operations • UEBA • RMF / ATO • FedRAMP • Cloud SIEM
</h4>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ------------------------------------------------------------
# RBAC
# ------------------------------------------------------------
ROLES = ["Admin", "SOC Analyst", "Viewer"]
role = st.sidebar.selectbox(" Select Role", ROLES)

def allow(roles):
    return role in roles

# ------------------------------------------------------------
# SIDEBAR CONTROLS
# ------------------------------------------------------------
st.sidebar.header(" SIEM Controls")

records = st.sidebar.slider("Synthetic Events", 50, 500, 100)

ingestion_source = st.sidebar.selectbox(
    " Data Ingestion Source",
    ["Synthetic", "Kafka", "AWS CloudWatch", "Azure Sentinel"]
)

realtime = st.sidebar.toggle(" Controlled Real-Time Simulation")

if allow(["Admin"]):
    uploaded_file = st.sidebar.file_uploader(" Upload Log Data (CSV)", type=["csv"])
else:
    uploaded_file = None

if allow(["Admin"]) and st.sidebar.button(" Reset Platform"):
    st.session_state.clear()
    st.rerun()

# ------------------------------------------------------------
# DATA INGESTION
# ------------------------------------------------------------
def ingest_logs(n, source):
    data = []
    for _ in range(n):
        data.append([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            f"192.168.1.{random.randint(1,50)}",
            f"user{random.randint(1,15)}",
            random.choice(["LOGIN","PRIV_ESC","NETWORK"]),
            random.choice(["SUCCESS","FAILED"]),
            source
        ])
    return pd.DataFrame(data, columns=[
        "timestamp","source_ip","username",
        "event_type","status","ingestion_source"
    ])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = ingest_logs(records, ingestion_source)

# ------------------------------------------------------------
# LOG DISPLAY
# ------------------------------------------------------------
st.subheader(" Security Event Logs")
st.dataframe(df, use_container_width=True)

# ------------------------------------------------------------
# INGESTION VISUAL
# ------------------------------------------------------------
st.subheader(" Data Ingestion Overview")

fig_src, ax_src = plt.subplots()
df["ingestion_source"].value_counts().plot.pie(
    autopct="%1.1f%%", ax=ax_src
)
ax_src.set_ylabel("")
st.pyplot(fig_src)

# ------------------------------------------------------------
# UEBA SCORING
# ------------------------------------------------------------
st.subheader(" UEBA (User & Entity Behavior Analytics)")

ueba = df.groupby("username").agg(
    failed_logins=("status", lambda x: (x == "FAILED").sum()),
    total_events=("event_type", "count"),
    priv_events=("event_type", lambda x: (x == "PRIV_ESC").sum())
).reset_index()

ueba["risk_score"] = (
    ueba["failed_logins"] * 2 +
    ueba["total_events"] * 0.2 +
    ueba["priv_events"] * 5
)

st.dataframe(ueba, use_container_width=True)

# UEBA GRAPH
fig_ueba, ax_ueba = plt.subplots()
ax_ueba.bar(ueba["username"], ueba["risk_score"])
ax_ueba.set_ylabel("Risk Score")
ax_ueba.set_title("UEBA Risk Scores by User")
plt.xticks(rotation=45)
st.pyplot(fig_ueba)

# ------------------------------------------------------------
# ALERT GENERATION
# ------------------------------------------------------------
alerts = []

for _, r in ueba.iterrows():
    if r["risk_score"] >= 25:
        alerts.append([
            "UEBA Behavioral Anomaly",
            r["username"],
            "Critical",
            "IR-5, AU-6",
            "T1078"
        ])

alert_df = pd.DataFrame(alerts, columns=[
    "Alert Type","Entity","Severity","NIST 800-53","MITRE ATT&CK"
])

st.subheader(" Security Alerts")

if alert_df.empty:
    st.success(" No high-risk behavior detected")
else:
    st.dataframe(alert_df, use_container_width=True)

# ALERT SEVERITY PIE
if not alert_df.empty:
    fig_alert, ax_alert = plt.subplots()
    alert_df["Severity"].value_counts().plot.pie(
        autopct="%1.1f%%", ax=ax_alert
    )
    ax_alert.set_ylabel("")
    st.pyplot(fig_alert)

# ------------------------------------------------------------
# RMF / ATO TRACEABILITY
# ------------------------------------------------------------
st.subheader(" RMF / ATO Control Traceability")

rmf = pd.DataFrame([
    ["Log Collection","AU-2","FedRAMP Moderate"],
    ["Event Correlation","AU-6","FedRAMP Moderate"],
    ["UEBA Analytics","IR-5","High Impact"],
    ["Automated Response","IR-4","ATO Required"]
], columns=["Capability","NIST 800-53 Control","ATO Impact"])

st.dataframe(rmf, use_container_width=True)

# ------------------------------------------------------------
# EXPLANATION SECTION (GUI)
# ------------------------------------------------------------
st.subheader(" How This Platform Works")

with st.expander(" UEBA Risk Scoring Explained"):
    st.markdown("""
UEBA assigns a **risk score per user** using behavioral patterns:

• Failed login attempts  
• Event frequency over time  
• Privilege escalation activity  

Each factor is weighted to reflect real-world insider threat and account compromise risk.
Higher scores indicate anomalous behavior requiring investigation.
""")

with st.expander(" Alert Generation Explained"):
    st.markdown("""
Alerts are triggered when behavioral or correlation thresholds are exceeded.

Example:
• UEBA risk score ≥ 25 → Critical alert  
• Privilege escalation → Immediate response  

Alerts are mapped directly to **MITRE ATT&CK** and **NIST 800-53** controls.
""")

with st.expander(" RMF / ATO Control Traceability Explained"):
    st.markdown("""
Each SIEM capability is mapped to compliance controls:

• AU-2 → Log collection & auditability  
• AU-6 → Correlation & anomaly detection  
• IR-5 → Incident monitoring  
• IR-4 → Response automation  

This mapping supports **ATO packages, SSPs, and FedRAMP audits**.
""")

with st.expander(" Kafka vs AWS CloudWatch vs Azure Sentinel"):
    st.markdown("""
**Kafka**  
• High-throughput event streaming  
• Ideal for large-scale enterprise pipelines  

**AWS CloudWatch**  
• Native AWS telemetry (logs, metrics, alarms)  
• Best for cloud-native SOC operations  

**Azure Sentinel**  
• Cloud-native SIEM & SOAR  
• Deep integration with Microsoft security stack  

This platform normalizes all sources into a **common SIEM schema**.
""")

# ------------------------------------------------------------
# EXPORTS
# ------------------------------------------------------------
if allow(["Admin","SOC Analyst"]):
    st.subheader(" Compliance & Reporting Exports")

    csv_buf = io.StringIO()
    rmf.to_csv(csv_buf, index=False)

    st.download_button(
        "⬇️ Download RMF / ATO CTM (CSV)",
        csv_buf.getvalue(),
        "rmf_ctm.csv"
    )

    def pdf_report():
        buf = io.BytesIO()
        doc = SimpleDocTemplate(buf)
        styles = getSampleStyleSheet()
        story = [Paragraph(
            "SIEM ATO Compliance Report – Kalsnet (KNet)",
            styles["Title"]
        )]

        for _, r in rmf.iterrows():
            story.append(Paragraph(
                f"{r['Capability']} → {r['NIST 800-53 Control']} ({r['ATO Impact']})",
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
# CONTROLLED REAL-TIME SIMULATION
# ------------------------------------------------------------
if realtime:
    if "ticks" not in st.session_state:
        st.session_state.ticks = 0

    st.session_state.ticks += 1
    st.info(f" Real-Time Simulation Cycle {st.session_state.ticks}")

    if st.session_state.ticks < 4:
        time.sleep(1)
        st.rerun()
    else:
        st.success(" Real-Time Simulation Completed")



