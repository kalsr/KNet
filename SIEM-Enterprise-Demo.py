

 # SIEM_Enterprise_Demo.py

 # SOC training

 # DoD / NIST / FedRAMP demos

 # Executive briefings




import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

import random

from datetime import datetime

import time

import io

from reportlab.platypus import SimpleDocTemplate, Paragraph

from reportlab.lib.styles import getSampleStyleSheet



# ------------------------------------------------

st.set_page_config(layout="wide", page_title="SIEM Enterprise Demo")



st.markdown("""

<h1 style='color:#0A3D91; text-align:center;'>

This application developed by Randy Singh from Kalsnet (KNet)

</h1>

""", unsafe_allow_html=True)



st.markdown("---")



# ------------------------------------------------

# SIDEBAR CONTROLS

st.sidebar.header("SIEM Controls")



records = st.sidebar.slider("Synthetic Log Records", 0, 200, 50)

cloud_mode = st.sidebar.toggle("☁️ Cloud SIEM Mode")

realtime = st.sidebar.toggle("📡 Real-Time Simulation")



if st.sidebar.button("🔄 Reset & Refresh Data"):

    st.session_state.clear()

    st.experimental_rerun()



# ------------------------------------------------

# DATA GENERATION

def generate_logs(n, cloud=False):

    events = []

    for _ in range(n):

        event_type = random.choice(["LOGIN", "PRIV_ESC", "NETWORK"])

        status = random.choice(["SUCCESS", "FAILED"])

        source = random.choice(["AWS", "Azure", "On-Prem"]) if cloud else "On-Prem"

        events.append([

            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            f"192.168.1.{random.randint(1,10)}",

            "10.0.0.5",

            f"user{random.randint(1,5)}",

            event_type,

            status,

            source

        ])

    return pd.DataFrame(events, columns=[

        "timestamp","source_ip","destination_ip","username","event_type","status","log_source"

    ])



df = generate_logs(records, cloud_mode)



# ------------------------------------------------

st.subheader("📥 Collected & Normalized Logs")

st.dataframe(df.head(15))



# ------------------------------------------------

# CORRELATION & ALERTS

alerts = []



failed = df[df["status"] == "FAILED"].groupby("source_ip").size()

for ip, count in failed.items():

    if count >= 5:

        alerts.append([

            "Brute Force Attempt", ip, "High",

            "Detect", "T1110"

        ])



for ip in df[df["event_type"] == "PRIV_ESC"]["source_ip"].unique():

    alerts.append([

        "Privilege Escalation", ip, "Critical",

        "Respond", "T1068"

    ])



traffic = df.groupby("source_ip").size()

for ip, count in traffic.items():

    if count > 40:

        alerts.append([

            "Suspicious Traffic Volume", ip, "Medium",

            "Detect", "T1046"

        ])



alert_df = pd.DataFrame(alerts, columns=[

    "Alert Type","Source IP","Severity","NIST CSF","MITRE ATT&CK"

])



# ------------------------------------------------

st.subheader("🚨 Alerts with NIST & MITRE Mapping")

st.dataframe(alert_df)



# ------------------------------------------------

# VISUALS

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



# ------------------------------------------------

# AUTOMATED RESPONSE

st.subheader("🤖 Automated Response & Containment")

for _, r in alert_df.iterrows():

    if r["Severity"] in ["High","Critical"]:

        st.warning(f"Blocking IP {r['Source IP']} due to {r['Alert Type']}")



# ------------------------------------------------

# EXPLANATION SECTION

st.subheader("📘 How Security Calculations Work")



with st.expander("Brute Force Detection Formula"):

    st.markdown("""

**Rule:**  

If failed_logins_per_IP ≥ 5  



**Formula:**  

`COUNT(status == FAILED) GROUP BY source_ip`



**MITRE:** T1110  

**NIST:** Detect

""")



with st.expander("Privilege Escalation Detection"):

    st.markdown("""

**Rule:**  

event_type == PRIV_ESC  



**MITRE:** T1068  

**NIST:** Respond

""")



with st.expander("Suspicious Traffic Detection"):

    st.markdown("""

**Rule:**  

events_per_IP > 40  



**MITRE:** T1046  

**NIST:** Detect

""")



# ------------------------------------------------

# EXPORTS

st.subheader("📤 Export Reports")



csv_buf = io.StringIO()

alert_df.to_csv(csv_buf, index=False)



st.download_button("⬇️ Download Alerts CSV", csv_buf.getvalue(), "siem_alerts.csv")



def pdf_report(df):

    buf = io.BytesIO()

    doc = SimpleDocTemplate(buf)

    styles = getSampleStyleSheet()

    story = [Paragraph("SIEM Incident Report – Kalsnet (KNet)", styles["Title"])]



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



# ------------------------------------------------

# REAL-TIME SIMULATION

if realtime:

    st.info("📡 Real-Time Log Simulation Running")

    time.sleep(2)

    st.experimental_rerun()