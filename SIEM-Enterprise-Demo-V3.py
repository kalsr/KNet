

# ============================================================
# SIEM Enterprise Demo
# SOC Training | DoD / NIST / FedRAMP Demonstrations
# Developed by Randy Singh – Kalsnet (KNet)
# ============================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime
import time
import io

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------
st.set_page_config(
    layout="wide",
    page_title="SIEM Enterprise Demo",
    page_icon="🛡️"
)

# ------------------------------------------------------------
# TOP BANNER
# ------------------------------------------------------------
st.markdown("""
<div style="background-color:#0A3D91;padding:20px;border-radius:14px;">
<h1 style="color:white;text-align:center;font-weight:800;">
SIEM Enterprise Demo
</h1>
<h3 style="color:#D6E4FF;text-align:center;font-weight:600;">
Developed by Randy Singh – Kalsnet (KNet)
</h3>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ------------------------------------------------------------
# SIDEBAR CONTROLS
# ------------------------------------------------------------
st.sidebar.header("🛠️ SIEM Controls")

records = st.sidebar.slider("Synthetic Log Records", 10, 300, 50)
cloud_mode = st.sidebar.toggle("☁️ Cloud SIEM Mode")
realtime = st.sidebar.toggle("📡 Real-Time Simulation (Controlled)")

uploaded_file = st.sidebar.file_uploader(
    "📂 Upload Log Data (CSV)",
    type=["csv"]
)

if st.sidebar.button("🔄 Reset & Refresh"):
    st.session_state.clear()
    st.rerun()

# ------------------------------------------------------------
# DATA INGESTION
# ------------------------------------------------------------
def generate_logs(n, cloud=False):
    events = []
    for _ in range(n):
        events.append([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            f"192.168.1.{random.randint(1, 25)}",
            "10.0.0.5",
            f"user{random.randint(1, 10)}",
            random.choice(["LOGIN", "PRIV_ESC", "NETWORK"]),
            random.choice(["SUCCESS", "FAILED"]),
            random.choice(["AWS", "Azure", "On-Prem"]) if cloud else "On-Prem"
        ])
    return pd.DataFrame(events, columns=[
        "timestamp","source_ip","destination_ip",
        "username","event_type","status","log_source"
    ])

# Load user data or synthetic data
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ External log data successfully loaded")
else:
    df = generate_logs(records, cloud_mode)

# ------------------------------------------------------------
# LOG VIEW
# ------------------------------------------------------------
st.subheader("📥 Collected & Normalized Logs")
st.dataframe(df, use_container_width=True)

# ------------------------------------------------------------
# DETECTION LOGIC
# ------------------------------------------------------------
alerts = []

# --- Brute Force Detection ---
failed_logins = df[df["status"] == "FAILED"].groupby("source_ip").size()
for ip, count in failed_logins.items():
    if count >= 5:
        alerts.append(["Brute Force Attack", ip, "High", "Detect", "T1110"])

# --- Privilege Escalation ---
for ip in df[df["event_type"] == "PRIV_ESC"]["source_ip"].unique():
    alerts.append(["Privilege Escalation", ip, "Critical", "Respond", "T1068"])

# --- Suspicious Traffic ---
traffic = df.groupby("source_ip").size()
for ip, count in traffic.items():
    if count > 40:
        alerts.append(["Suspicious Traffic Volume", ip, "Medium", "Detect", "T1046"])

alert_df = pd.DataFrame(alerts, columns=[
    "Alert Type","Source IP","Severity","NIST CSF","MITRE ATT&CK"
])

# ------------------------------------------------------------
# ALERTS
# ------------------------------------------------------------
st.subheader("🚨 Security Alerts")

if alert_df.empty:
    st.success("✅ No active threats detected")
else:
    st.dataframe(alert_df, use_container_width=True)

# ------------------------------------------------------------
# VISUAL ANALYTICS
# ------------------------------------------------------------
st.subheader("📊 Security Analytics")

c1, c2 = st.columns(2)

with c1:
    fig, ax = plt.subplots()
    df["event_type"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    st.pyplot(fig)

with c2:
    if not alert_df.empty:
        fig2, ax2 = plt.subplots()
        alert_df["Severity"].value_counts().plot(kind="bar", ax=ax2)
        st.pyplot(fig2)

# ------------------------------------------------------------
# EXPLANATION PANEL (CLEAR + TRAINING FRIENDLY)
# ------------------------------------------------------------
st.subheader("📘 Detection Logic Explained")

with st.expander("🔐 Brute Force Attack Detection"):
    st.markdown("""
**What is analyzed:**  
Login failures grouped by source IP  

**How detection works:**  
If **5 or more failed logins** originate from the same IP within the dataset  

**Why it matters:**  
Indicates password guessing or credential stuffing  

**MITRE:** T1110  
**NIST CSF:** Detect
""")

with st.expander("⬆️ Privilege Escalation Detection"):
    st.markdown("""
**What is analyzed:**  
Event type labeled `PRIV_ESC`  

**How detection works:**  
Any event indicating unauthorized elevation of privileges  

**Why it matters:**  
Attackers gaining admin/root access can fully compromise systems  

**MITRE:** T1068  
**NIST CSF:** Respond
""")

with st.expander("🌐 Suspicious Traffic Detection"):
    st.markdown("""
**What is analyzed:**  
Total event volume per source IP  

**How detection works:**  
If events from a single IP exceed **40 events**  

**Why it matters:**  
May indicate scanning, beaconing, or DDoS activity  

**MITRE:** T1046  
**NIST CSF:** Detect
""")

# ------------------------------------------------------------
# AUTOMATED RESPONSE
# ------------------------------------------------------------
st.subheader("🤖 Automated Response")

for _, r in alert_df.iterrows():
    if r["Severity"] in ["High","Critical"]:
        st.warning(f"🚫 Blocking IP {r['Source IP']} ({r['Alert Type']})")

# ------------------------------------------------------------
# EXPORTS
# ------------------------------------------------------------
st.subheader("📤 Export Reports")

csv_buf = io.StringIO()
alert_df.to_csv(csv_buf, index=False)

st.download_button("⬇️ Download Alerts CSV", csv_buf.getvalue(), "alerts.csv")

def pdf_report(df):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf)
    styles = getSampleStyleSheet()
    story = [Paragraph("SIEM Incident Report – Kalsnet", styles["Title"])]

    for _, r in df.iterrows():
        story.append(Paragraph(
            f"{r['Alert Type']} | {r['Source IP']} | {r['Severity']} | {r['MITRE ATT&CK']}",
            styles["Normal"]
        ))

    doc.build(story)
    buf.seek(0)
    return buf

st.download_button(
    "⬇️ Download Incident Report PDF",
    pdf_report(alert_df),
    "siem_report.pdf"
)

# ------------------------------------------------------------
# CONTROLLED REAL-TIME SIMULATION
# ------------------------------------------------------------
if realtime:
    if "tick" not in st.session_state:
        st.session_state.tick = 0

    st.session_state.tick += 1
    st.info(f"📡 Real-Time Simulation Cycle: {st.session_state.tick}")

    if st.session_state.tick <= 5:
        time.sleep(1)
        st.rerun()
    else:
        st.success("✅ Real-Time Simulation Completed")
