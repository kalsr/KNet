



# ============================================================
# AGENTIC AI CYBER RANGE PLATFORM
# Developed by Randy Singh – Kalsnet (KNet) Consulting Group
# ============================================================

import streamlit as st
import pandas as pd
import random
import io
import plotly.express as px
import plotly.graph_objects as go

from sklearn.ensemble import IsolationForest

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(layout="wide")

# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------

st.markdown("""
<h1 style='background-color:#0b3d91;color:white;padding:15px;text-align:center'>
Agentic AI Cyber Range Platform
<br>
Developed by Randy Singh – Kalsnet (KNet) Consulting Group
</h1>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# BUTTON COLORS (WORKING VERSION)
# ------------------------------------------------------------

st.markdown("""
<style>
div.stButton > button[kind="primary"] {
    background-color: #1565c0;
    color:white;
}

#red button {background-color:#c62828;color:white}
#blue button {background-color:#1565c0;color:white}
#orange button {background-color:#ef6c00;color:white}
#purple button {background-color:#6a1b9a;color:white}
#green button {background-color:#2e7d32;color:white}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------

st.sidebar.header("Synthetic Cyber Data Generator")

records = st.sidebar.slider("Number of Records",0,200,50)

generate = st.sidebar.button("Generate Data")
reset = st.sidebar.button("Reset Data")

# ------------------------------------------------------------
# MITRE ATTACK MAPPING
# ------------------------------------------------------------

mitre_map = {

"Phishing":"Initial Access – T1566",
"Password Brute Force":"Credential Access – T1110",
"Privilege Escalation":"Privilege Escalation – T1068",
"Lateral Movement":"Lateral Movement – T1021",
"Malware Deployment":"Execution – T1204",
"SQL Injection":"Initial Access – T1190",
"Vulnerability Scanning":"Reconnaissance – T1595",
"DDoS":"Impact – T1499"
}

# ------------------------------------------------------------
# ATTACK LIBRARY
# ------------------------------------------------------------

attack_types=list(mitre_map.keys())
severity_levels=["Low","Medium","High","Critical"]

# ------------------------------------------------------------
# DATA GENERATOR
# ------------------------------------------------------------

def generate_data(n):

    rows=[]

    for i in range(n):

        attack=random.choice(attack_types)

        severity=random.choice(severity_levels)

        source=f"192.168.1.{random.randint(1,254)}"
        target=f"10.0.0.{random.randint(1,254)}"

        likelihood=random.randint(1,5)
        impact=random.randint(1,5)
        weight=random.randint(1,5)

        risk=likelihood*impact*weight

        rows.append([attack,severity,source,target,likelihood,impact,weight,risk,mitre_map[attack]])

    df=pd.DataFrame(rows,columns=[
        "Attack","Severity","Source IP","Target IP",
        "Likelihood","Impact","Severity Weight","Risk Score","MITRE Technique"
    ])

    return df

# ------------------------------------------------------------
# GENERATE / RESET
# ------------------------------------------------------------

if generate:

    st.session_state["data"]=generate_data(records)

if reset:

    st.session_state["data"]=pd.DataFrame()

# ------------------------------------------------------------
# DATA VIEW
# ------------------------------------------------------------

if "data" in st.session_state and not st.session_state["data"].empty:

    df=st.session_state["data"]

    st.subheader("Cyber Event Logs")

    st.dataframe(df)

    # --------------------------------------------------------
    # AI ANOMALY DETECTION
    # --------------------------------------------------------

    st.subheader("AI Anomaly Detection")

    model=IsolationForest(contamination=0.1)

    df["anomaly"]=model.fit_predict(df[["Risk Score"]])

    anomalies=df[df["anomaly"]==-1]

    st.write("Detected anomalies:",len(anomalies))

    st.dataframe(anomalies)

    # --------------------------------------------------------
    # SOC DASHBOARD
    # --------------------------------------------------------

    st.subheader("SOC Security Dashboard")

    c1,c2,c3,c4=st.columns(4)

    c1.metric("Total Events",len(df))
    c2.metric("High Risk Events",len(df[df["Risk Score"]>40]))
    c3.metric("Detected Anomalies",len(anomalies))
    c4.metric("Unique Attack Types",df["Attack"].nunique())

    # --------------------------------------------------------
    # VISUALIZATIONS
    # --------------------------------------------------------

    col1,col2=st.columns(2)

    with col1:

        fig=px.bar(df,x="Attack",title="Attack Distribution")
        st.plotly_chart(fig,use_container_width=True)

    with col2:

        fig2=px.pie(df,names="Severity",title="Severity Distribution")
        st.plotly_chart(fig2,use_container_width=True)

# ------------------------------------------------------------
# ATTACK PATH VISUALIZATION
# ------------------------------------------------------------

st.subheader("Attack Path Visualization")

path=["Recon","Initial Access","Privilege Escalation","Lateral Movement","Data Exfiltration"]

fig=go.Figure()

fig.add_trace(go.Scatter(
x=list(range(len(path))),
y=[1]*len(path),
mode="markers+lines+text",
text=path,
textposition="top center"
))

fig.update_layout(title="Cyber Attack Kill Chain")

st.plotly_chart(fig,use_container_width=True)

# ------------------------------------------------------------
# AUTONOMOUS CYBER AGENTS
# ------------------------------------------------------------

st.subheader("Autonomous Cyber Agents")

col1,col2,col3,col4,col5=st.columns(5)

# RED TEAM

with col1:

    st.markdown('<div id="red">',unsafe_allow_html=True)
    red=st.button("Red Team Agent")
    st.markdown('</div>',unsafe_allow_html=True)

    if red:

        attack=random.choice(attack_types)

        st.error("RED TEAM AUTONOMOUS ATTACK")

        st.write(f"""
Attack Executed: **{attack}**

MITRE Mapping: **{mitre_map[attack]}**

Actions:
• Performed reconnaissance  
• Exploited vulnerability  
• Attempted lateral movement
""")

# BLUE TEAM

with col2:

    st.markdown('<div id="blue">',unsafe_allow_html=True)
    blue=st.button("Blue Team Agent")
    st.markdown('</div>',unsafe_allow_html=True)

    if blue:

        st.info("""
BLUE TEAM DEFENSE ACTIONS

• Firewall rules deployed  
• Suspicious IP blocked  
• Endpoint detection triggered  
• System patches applied
""")

# SOC ANALYST

with col3:

    st.markdown('<div id="orange">',unsafe_allow_html=True)
    soc=st.button("SOC Analyst")
    st.markdown('</div>',unsafe_allow_html=True)

    if soc:

        st.warning("SOC Investigation")

        report=f"""
SOC ANALYST REPORT

Multiple alerts correlated across systems.

Observed attack patterns suggest coordinated intrusion attempt.

MITRE techniques identified in event logs.

Recommendation:
Escalate to Incident Response team.
"""

        st.text(report)

# INCIDENT RESPONSE

with col4:

    st.markdown('<div id="purple">',unsafe_allow_html=True)
    ir=st.button("Incident Response")
    st.markdown('</div>',unsafe_allow_html=True)

    if ir:

        st.success("""
INCIDENT RESPONSE ACTIONS

1. Host isolated
2. Malware removed
3. Credentials reset
4. System restored
5. Security controls updated
""")

# THREAT HUNTER

with col5:

    st.markdown('<div id="green">',unsafe_allow_html=True)
    hunter=st.button("Threat Hunter")
    st.markdown('</div>',unsafe_allow_html=True)

    if hunter:

        st.success("""
THREAT HUNTING RESULTS

Indicators Detected:

• Abnormal login patterns
• Privilege escalation attempts
• Suspicious network movement

Possible Advanced Persistent Threat identified.
""")

# ------------------------------------------------------------
# EXPORT
# ------------------------------------------------------------

st.subheader("Export Results")

if "data" in st.session_state and not st.session_state["data"].empty:

    df=st.session_state["data"]

    csv=df.to_csv(index=False).encode()

    st.download_button("Download CSV",csv,"cyber_range.csv")

    st.download_button("Download JSON",df.to_json(),"cyber_range.json")

    buffer=io.BytesIO()

    styles=getSampleStyleSheet()

    elements=[Paragraph("Cyber Range Report",styles["Title"]),Spacer(1,20)]

    for i,row in df.iterrows():

        elements.append(Paragraph(str(row.to_dict()),styles["BodyText"]))

    doc=SimpleDocTemplate(buffer)

    doc.build(elements)

    st.download_button("Download PDF",buffer.getvalue(),"cyber_report.pdf")