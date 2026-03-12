

# ==========================================================
# AGENTIC AI CYBER RANGE PLATFORM – Advanced
# Developed by Randy Singh – Kalsnet (KNet) Consulting Group
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io

st.set_page_config(layout="wide")

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown("""
<h1 style='background-color:#0b3d91;color:white;padding:15px;text-align:center'>
Agentic AI Cyber Range Platform – Advanced
<br>
AI Cyber Defense Training Environment
<br>
Developed by Randy Singh – Kalsnet (KNet) Consulting Group
</h1>
""", unsafe_allow_html=True)

# -------------------------------------------------
# ATTACK LIBRARY (TOP 10 ATTACKS)
# -------------------------------------------------

attack_library = {

"Phishing Attack":{
"goal":"Steal employee login credentials.",
"target":"Corporate email accounts and VPN credentials.",
"description":"Attackers send fraudulent emails impersonating trusted entities to trick employees into entering their credentials.",
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
"target":"File servers, backups and endpoint systems.",
"description":"Malware spreads through the network encrypting business critical files.",
"entry":"Malicious email attachment",
"vulnerability":"Unpatched endpoint vulnerability"
},

"Privilege Escalation":{
"goal":"Gain administrator privileges.",
"target":"Domain controllers and identity systems.",
"description":"Attackers exploit vulnerabilities to escalate privileges and control the network.",
"entry":"Compromised user credentials",
"vulnerability":"Weak access controls"
},

"DDoS Attack":{
"goal":"Disrupt online services.",
"target":"Public web servers.",
"description":"Attackers flood systems with massive traffic.",
"entry":"Botnet traffic",
"vulnerability":"Lack of traffic filtering"
},

"Data Exfiltration":{
"goal":"Steal confidential corporate data.",
"target":"Sensitive databases and file storage.",
"description":"Attackers secretly transfer large volumes of sensitive data outside the network.",
"entry":"Compromised internal account",
"vulnerability":"Insufficient monitoring"
},

"Supply Chain Attack":{
"goal":"Insert malicious code into trusted software.",
"target":"Enterprise software update mechanisms.",
"description":"Attackers compromise vendors or update processes.",
"entry":"Compromised vendor system",
"vulnerability":"Lack of vendor security validation"
},

"Cloud Account Compromise":{
"goal":"Take control of cloud infrastructure.",
"target":"Cloud admin accounts.",
"description":"Attackers steal cloud credentials and access resources.",
"entry":"Leaked API keys",
"vulnerability":"Improper IAM controls"
},

"Insider Threat":{
"goal":"Abuse legitimate access to steal data.",
"target":"Internal systems and intellectual property.",
"description":"A trusted employee abuses access privileges.",
"entry":"Authorized employee login",
"vulnerability":"Lack of monitoring"
},

"AI Model Poisoning":{
"goal":"Manipulate machine learning security systems.",
"target":"AI-based security analytics platforms.",
"description":"Attackers inject malicious data into training datasets.",
"entry":"Compromised training data pipeline",
"vulnerability":"Lack of AI data validation"
}

}

# -------------------------------------------------
# SESSION STORAGE
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
# BLUE TEAM DETECTION
# -------------------------------------------------

with col2:

    if st.button("Blue Team Detect & Mitigate"):

        attack = st.session_state.current_attack

        if attack:

            info = attack_library[attack]

            st.success(f"Blue Team Detection: {attack}")

            st.write("### Detection Methods")

            st.write(f"""
Security monitoring platforms such as **SIEM systems (Splunk, Sentinel)** detected abnormal behavior associated with the **{attack}**.

Security alerts triggered when logs showed indicators consistent with this attack type.
Network monitoring tools identified suspicious activity related to the attack entry method: **{info['entry']}**.

Endpoint Detection and Response (EDR) systems analyzed system processes and detected malicious behavior associated with the attack.
""")

            st.write("### Mitigation Actions")

            st.write(f"""
Security teams immediately initiated mitigation procedures for the **{attack}**.

• Security tools blocked malicious traffic associated with the attack entry point.  
• Compromised credentials or accounts were disabled.  
• Vulnerability exploited (**{info['vulnerability']}**) was patched across systems.  
• Firewall and endpoint protection rules were updated.  
• Additional monitoring was activated to ensure no further malicious activity.

These actions successfully contained and mitigated the **{attack}** before further damage occurred.
""")

            st.session_state.logs.append({
            "Team":"Blue Team",
            "Action":"Detection & Mitigation",
            "Attack":attack,
            "Details":"Blue team mitigated attack"
            })


# -------------------------------------------------
# SOC ANALYST
# -------------------------------------------------

with col3:

    if st.button("SOC Analyst Investigation"):

        attack = st.session_state.current_attack

        if attack:

            info = attack_library[attack]

            st.warning(f"SOC Investigation for {attack}")

            st.write("### SOC Investigation Steps")

            st.write(f"""
1. **Alert Review**
SOC analysts reviewed alerts generated by the SIEM platform indicating suspicious activity related to the **{attack}**.

2. **Log Analysis**
Security logs from authentication systems, network devices, and endpoint security tools were examined to confirm the attack behavior.

3. **Identify Indicators of Compromise**
Indicators associated with the attack were identified including unusual login activity and abnormal system processes.

4. **Attack Timeline Reconstruction**
SOC analysts reconstructed the attack timeline to understand when the attacker first gained access and what actions were performed.

5. **Affected Systems Identification**
Systems identified as targets include: **{info['target']}**.

6. **Root Cause Analysis**
The attack originated through **{info['entry']}** exploiting the vulnerability **{info['vulnerability']}**.

7. **Escalation**
Based on investigation results, the incident was escalated to the Incident Response Team for containment and remediation.
""")

            st.session_state.logs.append({
            "Team":"SOC Analyst",
            "Action":"Investigation",
            "Attack":attack,
            "Details":"SOC investigation completed"
            })


# -------------------------------------------------
# INCIDENT RESPONSE
# -------------------------------------------------

with col4:

    if st.button("Incident Response Actions"):

        attack = st.session_state.current_attack

        if attack:

            info = attack_library[attack]

            st.error(f"Incident Response for {attack}")

            st.write("### Incident Findings")

            st.write(f"""
The investigation confirmed that a **{attack}** occurred within the enterprise network.

Attack analysis revealed that the attacker entered the system through **{info['entry']}** and exploited the vulnerability **{info['vulnerability']}**.

Systems impacted include **{info['target']}**.

The attacker attempted to achieve the objective of **{info['goal']}**.
""")

            st.write("### Containment and Recovery")

            st.write(f"""
Incident response teams isolated compromised systems and blocked attacker access.

Security patches were applied to remove the exploited vulnerability.

User credentials potentially compromised during the **{attack}** were reset.

Systems were restored to secure operational state and continuous monitoring was implemented to prevent recurrence.
""")

            st.session_state.logs.append({
            "Team":"Incident Response",
            "Action":"Containment",
            "Attack":attack,
            "Details":"Incident contained"
            })


# -------------------------------------------------
# THREAT HUNTING
# -------------------------------------------------

with col5:

    if st.button("Threat Hunting Operation"):

        attack = st.session_state.current_attack

        if attack:

            info = attack_library[attack]

            st.info(f"Threat Hunting for {attack}")

            st.write("### Threat Hunting Activities")

            st.write(f"""
Threat hunters proactively searched the enterprise environment for indicators associated with the **{attack}**.

• Endpoint systems were scanned for malicious artifacts related to the attack entry method **{info['entry']}**.  
• Network telemetry was analyzed to detect additional attacker communication attempts.  
• Analysts searched for persistence mechanisms attackers might have deployed.  
• Historical log data was reviewed to ensure no earlier attack attempts occurred.  
• Additional compromised systems were investigated across the enterprise network.

Threat hunting confirmed that no additional attacker presence remained after mitigation actions.
""")

            st.session_state.logs.append({
            "Team":"Threat Hunting",
            "Action":"Proactive Search",
            "Attack":attack,
            "Details":"Threat hunting completed"
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
