# ==========================================================
# AGENTIC AI CYBER RANGE PLATFORM – VERSION(Super-FINAL)
# Developed by Randy Singh – Kalsnet (KNet) Consulting Group
# ==========================================================

import streamlit as st
import pandas as pd
import random
import plotly.express as px
import plotly.graph_objects as go
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
# ATTACK LIBRARY WITH GOALS
# -------------------------------------------------
attack_library = {

"Phishing Attack":{
"goal":"Steal employee login credentials and gain unauthorized access.",
"target":"User credentials, email accounts, internal systems.",
"description":"Attackers send fraudulent emails designed to trick employees into entering their login credentials on fake websites."
},

"SQL Injection":{
"goal":"Access or manipulate sensitive database information.",
"target":"Customer records, financial data, authentication databases.",
"description":"Malicious SQL commands are inserted into application input fields to retrieve or manipulate database data."
},

"Ransomware Attack":{
"goal":"Encrypt organizational data and demand ransom payment.",
"target":"File servers, databases, and backups.",
"description":"Malware encrypts critical files preventing access until ransom payment is made."
},

"Privilege Escalation":{
"goal":"Gain administrator privileges inside the network.",
"target":"System administration rights and security controls.",
"description":"Attackers exploit vulnerabilities to escalate from normal user privileges to administrator access."
},

"DDoS Attack":{
"goal":"Disrupt service availability by overwhelming servers.",
"target":"Public web services and infrastructure.",
"description":"Attackers flood servers with massive traffic causing service outages."
}

}

# -------------------------------------------------
# SESSION STORAGE
# -------------------------------------------------
if "logs" not in st.session_state:
    st.session_state.logs = []

if "current_attack" not in st.session_state:
    st.session_state.current_attack = None

# -------------------------------------------------
# CYBER OPERATIONS PANEL
# -------------------------------------------------
st.header("Cyber Operations Simulation")

col1,col2,col3,col4,col5 = st.columns(5)

# -------------------------------------------------
# RED TEAM
# -------------------------------------------------
with col1:
    if st.button("Red Team Launch Attack"):

        attack = random.choice(list(attack_library.keys()))
        st.session_state.current_attack = attack

        attack_info = attack_library[attack]

        st.error(f"Red Team launched: {attack}")

        st.write("### Attack Description")
        st.write(attack_info["description"])

        st.write("### Attack Goal")
        st.write(attack_info["goal"])

        st.write("### Target Information")
        st.write(attack_info["target"])

        st.session_state.logs.append({
        "Team":"Red Team",
        "Action":"Launch Attack",
        "Attack":attack,
        "Details":attack_info["goal"]
        })

# -------------------------------------------------
# BLUE TEAM
# -------------------------------------------------
with col2:

    if st.button("Blue Team Detect & Mitigate"):

        attack = st.session_state.current_attack

        if attack:

            st.success("Blue Team Detection Activated")

            mitigation = """
Detection Methods:
• SIEM alerts triggered by abnormal activity
• Intrusion Detection System identified malicious traffic
• Log correlation revealed suspicious authentication attempts

Mitigation Actions:
• Block malicious IP addresses
• Patch exploited vulnerabilities
• Reset compromised credentials
• Apply firewall and endpoint protection rules
"""

            st.write(mitigation)

            st.session_state.logs.append({
            "Team":"Blue Team",
            "Action":"Mitigation",
            "Attack":attack,
            "Details":"Attack detected via SIEM and mitigated through security controls"
            })

# -------------------------------------------------
# SOC ANALYST
# -------------------------------------------------
with col3:

    if st.button("SOC Analyst Investigation"):

        attack = st.session_state.current_attack

        if attack:

            st.warning("SOC Investigation in Progress")

            investigation = """
SOC Investigation Steps:

1. Review SIEM alerts and security logs
2. Identify Indicators of Compromise (IOCs)
3. Correlate events across multiple systems
4. Trace attacker activity timeline
5. Determine impacted systems and accounts
6. Escalate confirmed incident to Incident Response Team
"""

            st.write(investigation)

            st.session_state.logs.append({
            "Team":"SOC Analyst",
            "Action":"Investigation",
            "Attack":attack,
            "Details":"SOC performed event correlation and IOC identification"
            })

# -------------------------------------------------
# INCIDENT RESPONSE
# -------------------------------------------------
with col4:

    if st.button("Incident Response Actions"):

        attack = st.session_state.current_attack

        if attack:

            st.error("Incident Response Activated")

            response = """
Incident Findings:

• Attack vector identified and contained
• Compromised systems isolated from network
• Malware artifacts removed
• Security patches applied
• System integrity validated

Final Response Actions:

• Restore affected systems
• Reset affected user credentials
• Implement additional monitoring
• Document lessons learned
"""

            st.write(response)

            st.session_state.logs.append({
            "Team":"Incident Response",
            "Action":"Containment",
            "Attack":attack,
            "Details":"Incident contained and systems restored"
            })

# -------------------------------------------------
# THREAT HUNTING
# -------------------------------------------------
with col5:

    if st.button("Threat Hunting Operation"):

        attack = st.session_state.current_attack

        if attack:

            st.info("Threat Hunting Initiated")

            hunting = """
Threat Hunting Activities:

• Search endpoints for similar indicators
• Analyze network telemetry
• Identify lateral movement attempts
• Detect persistence mechanisms
• Investigate suspicious processes
• Validate system integrity across network
"""

            st.write(hunting)

            st.session_state.logs.append({
            "Team":"Threat Hunting",
            "Action":"Proactive Search",
            "Attack":attack,
            "Details":"Network-wide search for hidden threats"
            })

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
