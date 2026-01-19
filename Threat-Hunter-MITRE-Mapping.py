

# KNet Cyber Threat Hunting Studio – Enterprise Edition
# Designed by Randy Singh – Kalsnet (KNet) Consulting Group

import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import io

# ---------------- MITRE ATT&CK MAP ----------------

MITRE_MAP = {
    "Suspicious Login": ("Credential Access", "T1110", "Brute Force"),
    "API Abuse": ("Impact", "T1499", "Endpoint DoS"),
    "Command Abuse": ("Execution", "T1059", "Command-Line Interface"),
    "Data Exfiltration": ("Exfiltration", "T1041", "Exfiltration Over C2 Channel")
}

# ---------------- DATA ENGINE ----------------

def generate_synthetic_data(count):
    data = []
    for _ in range(count):
        data.append({
            "user": random.choice(["alice", "bob", "charlie", "admin"]),
            "login_hour": random.randint(0, 23),
            "failed_attempts": random.randint(0, 10),
            "api_calls": random.randint(10, 500),
            "command_entropy": round(random.uniform(1.0, 7.5), 2),
            "data_out_mb": random.randint(1, 1000)
        })
    return pd.DataFrame(data)

# ---------------- THREAT HUNTS ----------------

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
        reasons.append("Suspicious Login: abnormal login time or failed attempts")
    if record.api_calls > 300:
        reasons.append("API Abuse: excessive API calls")
    if record.command_entropy > 6.0:
        reasons.append("Command Abuse: high command entropy")
    if record.data_out_mb > 700:
        reasons.append("Data Exfiltration: large outbound data transfer")

    return reasons or ["No threat conditions triggered"]

# ---------------- AI PLAYBOOK ----------------

def ai_playbook(threat):
    return f"""
###  AI Remediation Playbook – {threat}

**Detect**
- Monitor indicators related to {threat}

**Contain**
- Isolate impacted accounts or services
- Apply temporary restrictions

**Remediate**
- Apply security controls aligned to policy
- Patch, reset credentials, or throttle activity

**Prevent**
- Enforce least privilege
- Continuous monitoring & alerting
- Automate detection rules
"""

# ---------------- PDF REPORT ----------------

def generate_pdf(results):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("KNet Executive Threat Report", styles["Title"]))

    for threat, records in results.items():
        if len(records) > 0:
            tactic, tid, name = MITRE_MAP[threat]
            content.append(Paragraph(
                f"<b>{threat}</b><br/>"
                f"Impacted Records: {len(records)}<br/>"
                f"MITRE: {tactic} – {tid} ({name})",
                styles["Normal"]
            ))

    doc.build(content)
    buffer.seek(0)
    return buffer

# ---------------- STREAMLIT UI ----------------

st.set_page_config(layout="wide")
st.title(" KNet Cyber Threat Hunting Studio – Enterprise")

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame()

col1, col2, col3, col4 = st.columns(4)

with col1:
    count = st.slider("Synthetic Records", 10, 500, 100)
with col2:
    if st.button("Generate Data"):
        st.session_state.data = generate_synthetic_data(count)
with col3:
    file = st.file_uploader("Upload CSV", type=["csv"])
with col4:
    if st.button("Reset"):
        st.session_state.data = pd.DataFrame()
        st.experimental_rerun()

if file:
    st.session_state.data = pd.read_csv(file)

# ---------------- MAIN DISPLAY ----------------

if not st.session_state.data.empty:
    st.subheader(" Records")
    st.dataframe(st.session_state.data, use_container_width=True)

    results = hunt_threats(st.session_state.data)

    # ---------- PIE ----------
    st.subheader(" Threat Distribution")
    labels = [f"{k} ({len(v)})" for k, v in results.items() if len(v) > 0]
    sizes = [len(v) for v in results.values() if len(v) > 0]

    if sizes:
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct="%1.1f%%")
        st.pyplot(fig)

    # ---------- FINDINGS ----------
    st.subheader(" MITRE ATT&CK Mapping")
    for k, v in results.items():
        if len(v) > 0:
            tactic, tid, name = MITRE_MAP[k]
            st.markdown(f"**{k}** → {tactic} | {tid} | {name}")

    # ---------- RECORD EXPLAIN ----------
    st.subheader(" Explain a Record")
    idx = st.selectbox("Select Record #", st.session_state.data.index)
    record = st.session_state.data.loc[idx]
    st.write(explain_record(record))

    # ---------- AI PLAYBOOK ----------
    st.subheader(" AI Remediation Playbooks")
    for threat, recs in results.items():
        if len(recs) > 0:
            st.markdown(ai_playbook(threat))

    # ---------- PDF ----------
    st.subheader(" Executive Report")
    pdf = generate_pdf(results)
    st.download_button("Download PDF Report", pdf, file_name="KNet_Executive_Report.pdf")

else:
    st.info("Generate or upload data to begin.")

st.markdown("---")
st.markdown("**Designed by Randy Singh – Kalsnet (KNet) Consulting Group**")
