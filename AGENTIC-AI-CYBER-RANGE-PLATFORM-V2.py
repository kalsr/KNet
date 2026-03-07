

# ============================================================
# AGENTIC AI CYBER RANGE PLATFORM
# Developed by Randy Singh – Kalsnet (KNet) Consulting Group
# ============================================================

import streamlit as st
import pandas as pd
import random
import numpy as np
import io
import time

import plotly.express as px
import plotly.graph_objects as go

import networkx as nx

from sklearn.ensemble import IsolationForest

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(layout="wide")

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown("""
<h1 style='background-color:#0b3d91;color:white;padding:15px;text-align:center'>
Agentic AI Cyber Range Platform
<br>
Developed by Randy Singh – Kalsnet (KNet) Consulting Group
</h1>
""",unsafe_allow_html=True)

# ---------------------------------------------------------
# BUTTON COLORS
# ---------------------------------------------------------

st.markdown("""
<style>
#red button {background-color:#c62828;color:white}
#blue button {background-color:#1565c0;color:white}
#orange button {background-color:#ef6c00;color:white}
#purple button {background-color:#6a1b9a;color:white}
#green button {background-color:#2e7d32;color:white}
</style>
""",unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR DATA GENERATOR
# ---------------------------------------------------------

st.sidebar.header("Synthetic Cyber Data Generator")

records = st.sidebar.slider("Number of Records",0,200,50)

generate = st.sidebar.button("Generate Data")
reset = st.sidebar.button("Reset Data")

# ---------------------------------------------------------
# MITRE ATTACK MAP
# ---------------------------------------------------------

mitre_map = {

"Phishing":"T1566",
"Brute Force":"T1110",
"Privilege Escalation":"T1068",
"Lateral Movement":"T1021",
"Malware":"T1204",
"SQL Injection":"T1190",
"DDoS":"T1499",
"Recon":"T1595"
}

attack_types=list(mitre_map.keys())
severity_levels=["Low","Medium","High","Critical"]

# ---------------------------------------------------------
# SYNTHETIC DATA GENERATOR
# ---------------------------------------------------------

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

if generate:
    st.session_state["data"]=generate_data(records)

if reset:
    st.session_state["data"]=pd.DataFrame()

# ---------------------------------------------------------
# DATA DISPLAY
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
    # SOC DASHBOARD
    # -----------------------------------------------------

    st.subheader("SOC Security Dashboard")

    c1,c2,c3,c4=st.columns(4)

    c1.metric("Total Events",len(df))
    c2.metric("High Risk Events",len(df[df["Risk Score"]>40]))
    c3.metric("Anomalies",len(anomalies))
    c4.metric("Attack Types",df["Attack"].nunique())

    # -----------------------------------------------------
    # ATTACK DISTRIBUTION
    # -----------------------------------------------------

    col1,col2=st.columns(2)

    with col1:
        fig=px.bar(df,x="Attack",title="Attack Distribution")
        st.plotly_chart(fig,use_container_width=True)

    with col2:
        fig2=px.pie(df,names="Severity",title="Severity Distribution")
        st.plotly_chart(fig2,use_container_width=True)

# ---------------------------------------------------------
# MITRE ATTACK HEATMAP
# ---------------------------------------------------------

st.subheader("MITRE ATT&CK Heatmap")

tech=list(mitre_map.values())

heat=pd.DataFrame(np.random.randint(0,10,(1,len(tech))),columns=tech)

fig=px.imshow(heat,labels=dict(x="Technique",color="Activity"))

st.plotly_chart(fig,use_container_width=True)

# ---------------------------------------------------------
# NETWORK ATTACK GRAPH
# ---------------------------------------------------------

st.subheader("Network Attack Graph")

G=nx.Graph()

for i in range(10):
    src=f"192.168.1.{random.randint(1,20)}"
    dst=f"10.0.0.{random.randint(1,20)}"
    G.add_edge(src,dst)

pos=nx.spring_layout(G)

edge_x=[]
edge_y=[]

for edge in G.edges():
    x0,y0=pos[edge[0]]
    x1,y1=pos[edge[1]]

    edge_x.extend([x0,x1,None])
    edge_y.extend([y0,y1,None])

edge_trace=go.Scatter(x=edge_x,y=edge_y,mode='lines')

node_x=[]
node_y=[]

for node in G.nodes():
    x,y=pos[node]
    node_x.append(x)
    node_y.append(y)

node_trace=go.Scatter(x=node_x,y=node_y,mode='markers+text',text=list(G.nodes()))

fig=go.Figure(data=[edge_trace,node_trace])

st.plotly_chart(fig,use_container_width=True)

# ---------------------------------------------------------
# 3D CYBER ATTACK SIMULATION
# ---------------------------------------------------------

st.subheader("3D Cyber Attack Simulation")

stages=["Recon","Access","Privilege","Lateral","Exfiltration"]

fig=go.Figure(data=[go.Scatter3d(

x=[1,2,3,4,5],
y=[1,1,1,1,1],
z=[1,2,3,4,5],
mode='markers+lines',
text=stages

)])

fig.update_layout(title="Cyber Kill Chain 3D")

st.plotly_chart(fig,use_container_width=True)

# ---------------------------------------------------------
# LIVE THREAT INTEL FEED
# ---------------------------------------------------------

st.subheader("Live Threat Intelligence Feed")

intel=[

"New ransomware campaign detected",
"Zero-day vulnerability discovered",
"Malicious IP scanning networks",
"Credential stuffing attacks increasing",
"APT group targeting finance sector"
]

for i in range(3):
    st.info(random.choice(intel))

# ---------------------------------------------------------
# AUTONOMOUS AGENTIC LOOP
# ---------------------------------------------------------

st.subheader("Autonomous Cyber Agents")

col1,col2,col3,col4,col5=st.columns(5)

# RED TEAM

with col1:
    st.markdown('<div id="red">',unsafe_allow_html=True)
    red=st.button("Red Team")
    st.markdown('</div>',unsafe_allow_html=True)

    if red:

        attack=random.choice(attack_types)

        st.error(f"""
RED TEAM ATTACK

Attack Type: {attack}

MITRE Technique: {mitre_map[attack]}

Action:
Recon → Exploit → Privilege Escalation
""")

# BLUE TEAM

with col2:

    st.markdown('<div id="blue">',unsafe_allow_html=True)
    blue=st.button("Blue Team")
    st.markdown('</div>',unsafe_allow_html=True)

    if blue:

        st.info("""
BLUE TEAM RESPONSE

Firewall rule deployed
Malicious IP blocked
Endpoint security activated
""")

# SOC COPILOT

with col3:

    st.markdown('<div id="orange">',unsafe_allow_html=True)
    soc=st.button("SOC Copilot")
    st.markdown('</div>',unsafe_allow_html=True)

    if soc:

        report=f"""
SOC AI REPORT

Multiple suspicious indicators detected.

Possible coordinated intrusion attempt.

Recommended actions:
1. escalate incident
2. isolate affected host
3. initiate incident response
"""

        st.warning(report)

# INCIDENT RESPONSE

with col4:

    st.markdown('<div id="purple">',unsafe_allow_html=True)
    ir=st.button("Incident Response")
    st.markdown('</div>',unsafe_allow_html=True)

    if ir:

        st.success("""
Incident Response Steps

Containment
Eradication
Recovery
Lessons Learned
""")

# THREAT HUNTER

with col5:

    st.markdown('<div id="green">',unsafe_allow_html=True)
    hunter=st.button("Threat Hunter")
    st.markdown('</div>',unsafe_allow_html=True)

    if hunter:

        st.success("""
Threat Hunting Results

Suspicious lateral movement detected.

Possible APT behavior identified.
""")

# ---------------------------------------------------------
# EXPORT RESULTS
# ---------------------------------------------------------

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