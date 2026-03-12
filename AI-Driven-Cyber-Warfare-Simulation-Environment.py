

# ==========================================================
# AI-Driven-Cyber-wWrfare-Simulation-Environment.
# Developed by Randy Singh – Kalsnet (KNet) Consulting Group
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
import random
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io

st.set_page_config(layout="wide")

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.markdown("""
<h1 style='background-color:#0b3d91;color:white;padding:15px;text-align:center'>
Agentic AI Cyber Range Platform – With Red & Blue Teams
<br>
AI Cyber Defense Training Environment
<br>
Developed by Randy Singh – Kalsnet (KNet) Consulting Group
</h1>
""", unsafe_allow_html=True)

# -------------------------------------------------
# ATTACK LIBRARY
# -------------------------------------------------

attack_library = {

"Phishing Attack":{
"goal":"Steal employee login credentials.",
"target":"Corporate email accounts and VPN credentials.",
"description":"Attackers send fraudulent emails impersonating trusted entities to trick employees into entering credentials.",
"entry":"Email phishing campaign",
"vulnerability":"Lack of phishing awareness training"
},

"SQL Injection":{
"goal":"Extract sensitive data from enterprise databases.",
"target":"Customer records and financial databases.",
"description":"Attackers insert malicious SQL commands into vulnerable application input fields.",
"entry":"Web application login form",
"vulnerability":"Improper input validation"
},

"Ransomware Attack":{
"goal":"Encrypt enterprise files and demand ransom.",
"target":"File servers and endpoints.",
"description":"Malware spreads encrypting business critical files.",
"entry":"Malicious attachment",
"vulnerability":"Unpatched endpoint vulnerability"
},

"Privilege Escalation":{
"goal":"Gain administrator privileges.",
"target":"Domain controllers.",
"description":"Attackers exploit vulnerabilities to gain admin access.",
"entry":"Compromised credentials",
"vulnerability":"Weak access control"
},

"DDoS Attack":{
"goal":"Disrupt online services.",
"target":"Web infrastructure.",
"description":"Attackers flood servers with massive traffic.",
"entry":"Botnet",
"vulnerability":"Lack of traffic filtering"
},

"Data Exfiltration":{
"goal":"Steal confidential corporate data.",
"target":"Sensitive databases.",
"description":"Attackers secretly transfer large volumes of data.",
"entry":"Compromised internal account",
"vulnerability":"Insufficient monitoring"
},

"Supply Chain Attack":{
"goal":"Insert malicious code into trusted software.",
"target":"Software update systems.",
"description":"Attackers compromise vendor pipelines.",
"entry":"Vendor compromise",
"vulnerability":"Weak vendor validation"
},

"Cloud Account Compromise":{
"goal":"Take control of cloud infrastructure.",
"target":"Cloud admin accounts.",
"description":"Attackers steal cloud credentials.",
"entry":"Leaked API keys",
"vulnerability":"Improper IAM configuration"
},

"Insider Threat":{
"goal":"Abuse legitimate access.",
"target":"Internal intellectual property.",
"description":"Trusted employee steals data.",
"entry":"Authorized login",
"vulnerability":"Lack of monitoring"
},

"AI Model Poisoning":{
"goal":"Manipulate ML security systems.",
"target":"AI analytics platforms.",
"description":"Attackers inject malicious training data.",
"entry":"Compromised training pipeline",
"vulnerability":"Lack of data validation"
}

}

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------

if "logs" not in st.session_state:
    st.session_state.logs=[]

if "current_attack" not in st.session_state:
    st.session_state.current_attack=None

# -------------------------------------------------
# CYBER OPERATIONS PANEL
# -------------------------------------------------

st.header("Cyber Operations Simulation")

col1,col2,col3,col4,col5 = st.columns(5)

# -------------------------------------------------
# RED TEAM
# -------------------------------------------------

with col1:

    attack_choice = st.selectbox("Select Red Team Attack", list(attack_library.keys()))

    if st.button("Launch Selected Attack"):

        attack = attack_choice
        st.session_state.current_attack=attack
        info = attack_library[attack]

        st.error(f"Red Team launched attack: {attack}")

        st.write("### Attack Description")
        st.write(info["description"])

        st.write("### Attack Goal")
        st.write(info["goal"])

        st.write("### Target Systems")
        st.write(info["target"])

        st.session_state.logs.append({
        "Team":"Red Team",
        "Action":"Attack Launch",
        "Attack":attack,
        "Details":info["goal"]
        })

# -------------------------------------------------
# BLUE TEAM
# -------------------------------------------------

with col2:

    if st.button("Blue Team Detect & Mitigate"):

        attack = st.session_state.current_attack

        if attack:

            st.success(f"Blue Team detected {attack}")

            st.write("""
Security monitoring systems detected abnormal behavior.

Mitigation actions:
• Block malicious traffic
• Disable compromised accounts
• Patch exploited vulnerabilities
• Increase monitoring
""")

            st.session_state.logs.append({
            "Team":"Blue Team",
            "Action":"Mitigation",
            "Attack":attack,
            "Details":"Attack mitigated"
            })

# -------------------------------------------------
# SOC ANALYST
# -------------------------------------------------

with col3:

    if st.button("SOC Investigation"):

        attack = st.session_state.current_attack

        if attack:

            st.warning(f"SOC Investigation for {attack}")

            st.write("""
SOC Steps:

1. Alert review
2. Log analysis
3. Identify indicators
4. Timeline reconstruction
5. Escalation
""")

            st.session_state.logs.append({
            "Team":"SOC",
            "Action":"Investigation",
            "Attack":attack,
            "Details":"SOC analysis complete"
            })

# -------------------------------------------------
# INCIDENT RESPONSE
# -------------------------------------------------

with col4:

    if st.button("Incident Response"):

        attack = st.session_state.current_attack

        if attack:

            st.error(f"Incident Response activated for {attack}")

            st.write("""
Containment actions:

• isolate compromised systems
• reset credentials
• apply patches
• restore systems
""")

            st.session_state.logs.append({
            "Team":"Incident Response",
            "Action":"Containment",
            "Attack":attack,
            "Details":"Systems secured"
            })

# -------------------------------------------------
# THREAT HUNTING
# -------------------------------------------------

with col5:

    if st.button("Threat Hunting"):

        attack = st.session_state.current_attack

        if attack:

            st.info("Threat hunters scanning enterprise environment")

            st.session_state.logs.append({
            "Team":"Threat Hunting",
            "Action":"Proactive Search",
            "Attack":attack,
            "Details":"Hunt completed"
            })

# -------------------------------------------------
# REAL-TIME ATTACK TIMELINE
# -------------------------------------------------

st.header("Real-Time Attack Simulation Timeline")

timeline = [
"Initial Access",
"Execution",
"Privilege Escalation",
"Lateral Movement",
"Data Exfiltration"
]

if st.button("Start Attack Simulation"):

    progress = st.progress(0)

    for i,step in enumerate(timeline):

        st.write("Current Stage:", step)
        progress.progress((i+1)/len(timeline))
        time.sleep(1)

# -------------------------------------------------
# MITRE ATT&CK MATRIX
# -------------------------------------------------

st.header("MITRE ATT&CK Matrix Overview")

tactics = [
"Initial Access","Execution","Persistence","Privilege Escalation",
"Defense Evasion","Credential Access","Discovery",
"Lateral Movement","Collection","Command & Control",
"Exfiltration","Impact","Reconnaissance","Resource Development"
]

technique_count = [random.randint(10,25) for i in tactics]

df_mitre = pd.DataFrame({
"Tactic":tactics,
"Techniques":technique_count
})

fig = px.bar(df_mitre,x="Tactic",y="Techniques",
title="MITRE ATT&CK Tactics Coverage")

st.plotly_chart(fig,use_container_width=True)

# -------------------------------------------------
# AI THREAT HUNTING ENGINE
# -------------------------------------------------

st.header("AI Threat Hunting Engine")

query = st.text_input("Ask AI to hunt threats")

if query and st.session_state.current_attack:

    attack = st.session_state.current_attack
    info = attack_library[attack]

    st.success(f"""
AI Threat Hunting Result

Possible attack pattern detected related to **{attack}**

Indicators searched:
• abnormal authentication logs
• suspicious network traffic
• unauthorized data transfers

Recommended actions:
• search SIEM for {info['entry']}
• inspect endpoints
• monitor systems: {info['target']}
""")

# -------------------------------------------------
# AUTONOMOUS BLUE TEAM AGENT
# -------------------------------------------------

st.header("Autonomous Blue Team Response Agent")

if st.button("Activate Autonomous Defense"):

    attack = st.session_state.current_attack

    if attack:

        st.success("AI Defense Agent Activated")

        responses = [
        "Blocking malicious IP addresses",
        "Disabling compromised accounts",
        "Applying security patches",
        "Isolating infected endpoints",
        "Deploying additional monitoring rules"
        ]

        for r in responses:

            st.write("AI Action:",r)
            time.sleep(0.5)

# -------------------------------------------------
# VISUALIZATION
# -------------------------------------------------

st.header("Cyber Attack & Defense Visualization")

if st.session_state.logs:

    df = pd.DataFrame(st.session_state.logs)

    st.dataframe(df)

    fig = px.pie(df, names="Team", title="Team Activity Distribution")
    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.histogram(df, x="Attack", color="Team", title="Attack Response Timeline")
    st.plotly_chart(fig2, use_container_width=True)

# -------------------------------------------------
# EXPORT RESULTS
# -------------------------------------------------

st.header("Export Cyber Range Results")

if st.session_state.logs:

    df = pd.DataFrame(st.session_state.logs)

    csv = df.to_csv(index=False).encode()
    st.download_button("Download CSV", csv, "cyber_range_results.csv")

    json = df.to_json()
    st.download_button("Download JSON", json, "cyber_range_results.json")

    buffer = io.BytesIO()
    styles = getSampleStyleSheet()

    elements = [Paragraph("Cyber Range Incident Report", styles['Title']), Spacer(1,20)]

    for i,row in df.iterrows():
        elements.append(Paragraph(str(row.to_dict()), styles['BodyText']))

    doc = SimpleDocTemplate(buffer)
    doc.build(elements)

    st.download_button("Download PDF", buffer.getvalue(), "cyber_range_report.pdf")