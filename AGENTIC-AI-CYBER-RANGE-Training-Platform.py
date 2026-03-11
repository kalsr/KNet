# ==========================================================
# AGENTIC AI CYBER RANGE PLATFORM – Training-Platform)
# Developed by Randy Singh – Kalsnet (KNet) Consulting Group
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import random
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io
from datetime import datetime

st.set_page_config(layout="wide")

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.markdown("""
<h1 style='background-color:#0b3d91;color:white;padding:15px;text-align:center'>
Agentic AI Cyber Range Platform – Version 9
<br>
AI Cyber Defense Training Environment
<br>
Developed by Randy Singh – Kalsnet (KNet) Consulting Group
</h1>
""", unsafe_allow_html=True)


# -------------------------------------------------
# RED TEAM ATTACK LIBRARY (TOP 10 ATTACKS)
# -------------------------------------------------

attack_library = {

"Ransomware Deployment":{

"description":"Malware encrypts enterprise data across servers and endpoints.",
"goal":"Encrypt enterprise systems and demand ransom payment.",
"entry":"Phishing email containing malicious attachment.",
"vulnerability":"Unpatched endpoint vulnerability.",
"target":"File Servers, Domain Controllers, Backup Servers",

"mitre":"T1486 Data Encrypted for Impact",
"nist":"PR.IP, DE.CM, RS.MI",

"logs":[
"Multiple file rename operations detected",
"EDR alert for suspicious PowerShell execution",
"Mass encryption activity detected"
]

},

"Active Directory Domain Takeover":{

"description":"Attacker escalates privileges to obtain domain administrator access.",
"goal":"Gain full control over enterprise network.",
"entry":"Compromised user credentials.",
"vulnerability":"Weak credential policies.",

"target":"Domain Controllers, Identity Servers",

"mitre":"T1078 Valid Accounts",
"nist":"PR.AC, DE.CM",

"logs":[
"Multiple Kerberos authentication failures",
"Privileged account creation detected",
"Abnormal admin login detected"
]

},

"Data Exfiltration":{

"description":"Sensitive data is transferred outside the network.",
"goal":"Steal intellectual property and sensitive records.",
"entry":"Compromised VPN credentials.",
"vulnerability":"Weak network monitoring.",

"target":"Database Servers",

"mitre":"T1041 Exfiltration Over C2 Channel",
"nist":"DE.CM, PR.DS",

"logs":[
"Large outbound data transfer detected",
"Database export logs triggered",
"Encrypted external traffic spike"
]

},

"DDoS Attack":{

"description":"Attackers flood the server with traffic causing outage.",
"goal":"Disrupt services and cause downtime.",
"entry":"Botnet traffic.",
"vulnerability":"Lack of rate limiting.",

"target":"Public Web Servers",

"mitre":"T1498 Network Denial of Service",
"nist":"DE.CM, PR.PT",

"logs":[
"Traffic spike detected",
"WAF alerts triggered",
"Server CPU overload logs"
]

},

"Cloud Account Compromise":{

"description":"Unauthorized access to cloud infrastructure.",
"goal":"Steal cloud resources and data.",
"entry":"Stolen API keys.",
"vulnerability":"Improper IAM permissions.",

"target":"AWS/Azure cloud accounts",

"mitre":"T1078 Cloud Accounts",
"nist":"PR.AC",

"logs":[
"Unauthorized API calls detected",
"New instance creation alert",
"Abnormal login location detected"
]

}

}


# -------------------------------------------------
# SESSION VARIABLES
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

        info = attack_library[attack]

        st.error(f"Red Team launched: {attack}")

        st.write("### Attack Goal")
        st.write(info["goal"])

        st.write("### Attack Description")
        st.write(info["description"])

        st.write("### Entry Method")
        st.write(info["entry"])

        st.write("### Vulnerability Exploited")
        st.write(info["vulnerability"])

        st.write("### Target Systems")
        st.write(info["target"])

        st.session_state.logs.append({

        "Time":datetime.now(),
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

            st.success("Blue Team Detection Activated")

            st.write("### Security Monitoring Alerts")

            for log in info["logs"]:
                st.write("•",log)

            st.write("### Detection Tools")

            st.write("""
SIEM Platform: Splunk / Microsoft Sentinel  
Endpoint Detection: CrowdStrike / Defender  
Network Monitoring: IDS/IPS
""")

            st.write("### MITRE ATT&CK Mapping")
            st.write(info["mitre"])

            st.write("### NIST Cybersecurity Framework")
            st.write(info["nist"])

            st.write("### Mitigation Steps")

            st.write("""
• Block malicious IP addresses  
• Isolate infected systems  
• Reset compromised credentials  
• Apply security patches  
• Increase monitoring
""")

            st.session_state.logs.append({

            "Time":datetime.now(),
            "Team":"Blue Team",
            "Action":"Attack Detection",
            "Attack":attack,
            "Details":"Attack detected via SIEM logs"

            })


# -------------------------------------------------
# SOC ANALYST
# -------------------------------------------------

with col3:

    if st.button("SOC Analyst Investigation"):

        attack = st.session_state.current_attack

        if attack:

            info = attack_library[attack]

            st.warning("SOC Investigation Started")

            severity = random.choice(["Medium","High","Critical"])

            st.write("### Tools Used")

            st.write("""
• Splunk SIEM
• ELK Stack
• CrowdStrike EDR
""")

            st.write("### Severity Level")
            st.write(severity)

            st.write("### Systems Affected")
            st.write(info["target"])

            st.write("### Logs Examined")

            for log in info["logs"]:
                st.write("•",log)

            st.write("### Entry Point")
            st.write(info["entry"])

            st.write("### Vulnerability Exploited")
            st.write(info["vulnerability"])

            st.write("### Attack Timeline")

            st.write("""
1. Initial intrusion detected  
2. Privilege escalation attempt  
3. Malicious activity execution  
""")

            st.write("### Attacker Status")
            st.write("Attacker activity blocked and monitored")

            if severity == "Critical":

                st.error("Incident escalated to Incident Response Team")

            st.session_state.logs.append({

            "Time":datetime.now(),
            "Team":"SOC Analyst",
            "Action":"Investigation",
            "Attack":attack,
            "Details":"SOC completed investigation"

            })


# -------------------------------------------------
# INCIDENT RESPONSE
# -------------------------------------------------

with col4:

    if st.button("Incident Response Actions"):

        attack = st.session_state.current_attack

        if attack:

            info = attack_library[attack]

            st.error("Incident Response Activated")

            st.write("### Containment Actions")

            st.write("""
• Isolate compromised systems
• Remove malicious artifacts
• Block attacker IP addresses
• Reset compromised credentials
""")

            st.write("### Recovery")

            st.write("""
• Restore systems from backups
• Apply security patches
• Verify system integrity
""")

            st.session_state.logs.append({

            "Time":datetime.now(),
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

            st.info("Threat Hunting Initiated")

            st.write("### Threat Hunting Activities")

            for log in info["logs"]:
                st.write("Searching endpoints for indicator:",log)

            st.write("### Network Scan Results")

            st.write("No additional compromised systems detected")

            st.session_state.logs.append({

            "Time":datetime.now(),
            "Team":"Threat Hunting",
            "Action":"Threat Search",
            "Attack":attack,
            "Details":"Environment scanned"

            })


# -------------------------------------------------
# VISUALIZATION
# -------------------------------------------------

st.header("Cyber Attack & Defense Visualization")

if st.session_state.logs:

    df = pd.DataFrame(st.session_state.logs)

    st.dataframe(df)

    fig = px.pie(df,names="Team",title="Team Activity Distribution")
    st.plotly_chart(fig,use_container_width=True)

    fig2 = px.histogram(df,x="Attack",color="Team",title="Attack Response Timeline")
    st.plotly_chart(fig2,use_container_width=True)


# -------------------------------------------------
# EXPORT REPORTS
# -------------------------------------------------

st.header("Export Cyber Range Results")

if st.session_state.logs:

    df = pd.DataFrame(st.session_state.logs)

    csv = df.to_csv(index=False).encode()
    st.download_button("Download CSV",csv,"cyber_range_results.csv")

    json = df.to_json()
    st.download_button("Download JSON",json,"cyber_range_results.json")

    buffer = io.BytesIO()

    styles = getSampleStyleSheet()

    elements = [Paragraph("SOC Incident Investigation Report",styles['Title']),Spacer(1,20)]

    for i,row in df.iterrows():
        elements.append(Paragraph(str(row.to_dict()),styles['BodyText']))
        elements.append(Spacer(1,10))

    doc = SimpleDocTemplate(buffer)
    doc.build(elements)

    st.download_button("Download PDF Report",buffer.getvalue(),"cyber_range_report.pdf")