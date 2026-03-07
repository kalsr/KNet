


# ==========================================================
# AGENTIC AI CYBER RANGE PLATFORM
# Developed by Randy Singh – Kalsnet (KNet) Consulting Group
# ==========================================================
# This application can be used for:

# SOC analyst training

# cyber defense demonstrations

# cyber warfare simulation

# AI cybersecurity education

# government cyber training labs

# red vs blue exercises

# program currently uses:

# scikit-learn IsolationForest

# synthetic event generation

# anomaly detection

# This is AI, but not full Agentic AI.

import streamlit as st
import pandas as pd
import numpy as np
import random
import json
import io

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

import plotly.express as px

from sklearn.ensemble import IsolationForest


st.set_page_config(layout="wide")

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
"""
<h1 style='background-color:#0b3d91;color:white;padding:15px;text-align:center'>
Agentic AI Cyber Range Platform
<br>
Developed by Randy Singh – Kalsnet (KNet) Consulting Group
</h1>
""",
unsafe_allow_html=True
)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.header("Synthetic Cyber Data Generator")

records = st.sidebar.slider("Number of Records",0,200,50)

generate = st.sidebar.button("Generate Data")
reset = st.sidebar.button("Reset Data")

# ---------------------------------------------------------
# ATTACK LIBRARY
# ---------------------------------------------------------

attack_types={

"Vulnerability Scanning":{
"impact":"Attackers scan networks to identify exposed services and weaknesses.",
"mitigation":"Run vulnerability scans regularly and apply security patches."
},

"Password Brute Force":{
"impact":"Attackers repeatedly guess passwords to gain unauthorized access.",
"mitigation":"Use MFA and account lockout policies."
},

"Lateral Movement":{
"impact":"Attackers move from one compromised system to another inside the network.",
"mitigation":"Use network segmentation and Zero Trust architecture."
},

"Privilege Escalation":{
"impact":"Attackers gain administrator or root privileges.",
"mitigation":"Patch OS vulnerabilities and monitor privilege changes."
},

"Malware Deployment":{
"impact":"Malicious software deployed to steal data or encrypt systems.",
"mitigation":"Use EDR solutions and endpoint monitoring."
},

"Phishing":{
"impact":"Users tricked into revealing credentials.",
"mitigation":"Security awareness training and email filtering."
},

"SQL Injection":{
"impact":"Attackers manipulate database queries.",
"mitigation":"Use parameterized queries and input validation."
},

"DDoS":{
"impact":"Large traffic overwhelms systems causing outages.",
"mitigation":"Use traffic filtering and CDN protection."
}
}

severity_levels=["Low","Medium","High","Critical"]

# ---------------------------------------------------------
# DATA GENERATOR
# ---------------------------------------------------------

def generate_data(n):

    rows=[]

    for i in range(n):

        attack=random.choice(list(attack_types.keys()))
        severity=random.choice(severity_levels)

        source=f"192.168.1.{random.randint(1,254)}"
        target=f"10.0.0.{random.randint(1,254)}"

        likelihood=random.randint(1,5)
        impact=random.randint(1,5)
        severity_weight=random.randint(1,5)

        risk_score=severity_weight*likelihood*impact

        rows.append([attack,severity,source,target,likelihood,impact,severity_weight,risk_score])

    df=pd.DataFrame(rows,columns=[
    "Attack","Severity","Source IP","Target IP","Likelihood","Impact","Severity Weight","Risk Score"
    ])

    return df

# ---------------------------------------------------------
# GENERATE / RESET
# ---------------------------------------------------------

if generate:

    df=generate_data(records)
    st.session_state["data"]=df

if reset:
    st.session_state["data"]=pd.DataFrame()

# ---------------------------------------------------------
# DATA VIEW
# ---------------------------------------------------------

if "data" in st.session_state and not st.session_state["data"].empty:

    df=st.session_state["data"]

    st.subheader("Cyber Event Logs")

    st.dataframe(df)

    # -----------------------------------------------------
    # AI ANOMALY DETECTION
    # -----------------------------------------------------

    st.subheader("AI Anomaly Detection")

    model=IsolationForest(contamination=0.1)

    df["anomaly"]=model.fit_predict(df[["Risk Score"]])

    anomalies=df[df["anomaly"]==-1]

    st.write("Detected anomalies:",len(anomalies))

    st.dataframe(anomalies)

    # -----------------------------------------------------
    # VISUALIZATIONS
    # -----------------------------------------------------

    col1,col2=st.columns(2)

    with col1:

        fig=px.bar(df,x="Attack",title="Attack Distribution")
        st.plotly_chart(fig)

    with col2:

        fig2=px.pie(df,names="Severity",title="Severity Distribution")
        st.plotly_chart(fig2)

# ---------------------------------------------------------
# AGENTIC CYBER OPERATIONS
# ---------------------------------------------------------

st.subheader("Agentic Cyber Defense & Attack Simulation")

st.markdown("""
<style>
.red-btn button {background-color:#c62828;color:white}
.blue-btn button {background-color:#1565c0;color:white}
.orange-btn button {background-color:#ef6c00;color:white}
.purple-btn button {background-color:#6a1b9a;color:white}
.green-btn button {background-color:#2e7d32;color:white}
</style>
""",unsafe_allow_html=True)

col1,col2,col3,col4,col5=st.columns(5)

# ---------------- RED TEAM ----------------

with col1:

    st.markdown('<div class="red-btn">',unsafe_allow_html=True)
    red=st.button("Red Team")
    st.markdown('</div>',unsafe_allow_html=True)

    if red:

        attack=random.choice(list(attack_types.keys()))

        st.error("RED TEAM ATTACK SIMULATION")

        st.write(f"""
Attack Executed: **{attack}**

Step 1: Reconnaissance and vulnerability scanning  
Step 2: Exploit vulnerability in target system  
Step 3: Gain unauthorized access  

Attacker Objective:
Gain network foothold and escalate privileges.
""")

# ---------------- BLUE TEAM ----------------

with col2:

    st.markdown('<div class="blue-btn">',unsafe_allow_html=True)
    blue=st.button("Blue Team")
    st.markdown('</div>',unsafe_allow_html=True)

    if blue:

        st.info("BLUE TEAM DEFENSE ACTIONS")

        st.write("""
Security Monitoring Detected Suspicious Behavior

Blue Team Actions:

• Monitored network logs  
• Detected abnormal risk score  
• Blocked malicious IP  
• Applied system patch  

Result:
Attack mitigated and system secured.
""")

# ---------------- SOC ANALYST ----------------

with col3:

    st.markdown('<div class="orange-btn">',unsafe_allow_html=True)
    soc=st.button("SOC Analyst")
    st.markdown('</div>',unsafe_allow_html=True)

    if soc:

        st.warning("SOC ANALYST INVESTIGATION")

        st.write("""
Alert Investigation Steps

1. Alert received from AI anomaly detection
2. Correlated multiple attack indicators
3. Analyzed event logs

SOC Conclusion:

Potential coordinated attack campaign detected.
Incident severity classified as HIGH.
""")

# ---------------- INCIDENT RESPONSE ----------------

with col4:

    st.markdown('<div class="purple-btn">',unsafe_allow_html=True)
    ir=st.button("Incident Response")
    st.markdown('</div>',unsafe_allow_html=True)

    if ir:

        st.success("INCIDENT RESPONSE ACTIONS")

        st.write("""
Incident Response Lifecycle

1. Containment
Affected host isolated from network.

2. Eradication
Malware removed and credentials reset.

3. Recovery
System restored from backup.

4. Lessons Learned
Security policies updated.
""")

# ---------------- THREAT HUNTER ----------------

with col5:

    st.markdown('<div class="green-btn">',unsafe_allow_html=True)
    hunter=st.button("Threat Hunter")
    st.markdown('</div>',unsafe_allow_html=True)

    if hunter:

        st.success("THREAT HUNTING RESULTS")

        st.write("""
Threat Hunting Analysis

Behavioral Indicators Found:

• Repeated authentication failures
• Suspicious lateral movement
• Privilege escalation patterns

Threat Hunter Conclusion:

Possible Advanced Persistent Threat (APT) activity detected.
Further monitoring recommended.
""")

# ---------------------------------------------------------
# KNOWLEDGE BASE
# ---------------------------------------------------------

st.subheader("Cyber Attack Knowledge Base")

selected_attack=st.selectbox("Select Attack Type",list(attack_types.keys()))

st.write("Impact")
st.info(attack_types[selected_attack]["impact"])

st.write("Mitigation Strategy")
st.success(attack_types[selected_attack]["mitigation"])

# ---------------------------------------------------------
# RISK FORMULA
# ---------------------------------------------------------

st.subheader("Risk Calculation Model")

st.code("Risk Score = Severity Weight × Likelihood × Impact")

# ---------------------------------------------------------
# EXPORT RESULTS
# ---------------------------------------------------------

st.subheader("Export Results")

if "data" in st.session_state and not st.session_state["data"].empty:

    df=st.session_state["data"]

    # CSV

    csv=df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="cyber_range_data.csv",
        mime="text/csv"
    )

    # JSON

    json_data=df.to_json(orient="records")

    st.download_button(
        label="Download JSON",
        data=json_data,
        file_name="cyber_range_data.json",
        mime="application/json"
    )

    # PDF

    buffer=io.BytesIO()

    styles=getSampleStyleSheet()

    elements=[]

    elements.append(Paragraph("KNet Cyber Range Report",styles["Title"]))
    elements.append(Spacer(1,20))

    for i,row in df.iterrows():

        elements.append(Paragraph(str(row.to_dict()),styles["BodyText"]))
        elements.append(Spacer(1,10))

    doc=SimpleDocTemplate(buffer)
    doc.build(elements)

    pdf=buffer.getvalue()

    st.download_button(
        label="Download PDF",
        data=pdf,
        file_name="cyber_range_report.pdf",
        mime="application/pdf"
    )