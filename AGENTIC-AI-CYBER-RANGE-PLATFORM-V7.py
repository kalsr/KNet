

# ==========================================================
# AGENTIC AI CYBER RANGE PLATFORM – VERSION 7
# Developed by Randy Singh – Kalsnet (KNet) Consulting Group
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import random
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
from sklearn.ensemble import IsolationForest

st.set_page_config(layout="wide")

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.markdown("""
<h1 style='background-color:#0b3d91;color:white;padding:15px;text-align:center'>
Agentic AI Cyber Range Platform – Version 7
<br>
AI Cyber Defense Training Environment
<br>
Developed by Randy Singh – Kalsnet (KNet) Consulting Group
</h1>
""",unsafe_allow_html=True)

# -------------------------------------------------
# ATTACK DEFINITIONS
# -------------------------------------------------

attack_library = {

"Phishing":"Email based social engineering used to steal credentials.",
"Brute Force":"Automated password guessing attack against login systems.",
"SQL Injection":"Injection of malicious SQL into database queries.",
"DDoS":"Distributed network flooding to overwhelm servers.",
"Privilege Escalation":"Gaining higher access rights in a system.",
"Lateral Movement":"Moving across network after initial compromise.",
"Malware":"Malicious software execution on endpoints.",
"Ransomware":"Encryption of systems to demand ransom payment.",
"Zero Day":"Exploitation of unknown software vulnerability.",
"Supply Chain Attack":"Compromise through trusted third party software."

}

mitre_map = {

"Phishing":"T1566",
"Brute Force":"T1110",
"SQL Injection":"T1190",
"DDoS":"T1499",
"Privilege Escalation":"T1068",
"Lateral Movement":"T1021",
"Malware":"T1204",
"Ransomware":"T1486",
"Zero Day":"T1203",
"Supply Chain Attack":"T1195"

}

severity_levels=["Low","Medium","High","Critical"]

# -------------------------------------------------
# DATA GENERATOR
# -------------------------------------------------

def generate_data(n):

    rows=[]

    for i in range(n):

        attack=random.choice(list(attack_library.keys()))
        severity=random.choice(severity_levels)

        likelihood=random.randint(1,5)
        impact=random.randint(1,5)
        weight=random.randint(1,5)

        risk=likelihood*impact*weight

        rows.append([

            attack,
            severity,
            likelihood,
            impact,
            weight,
            risk,
            mitre_map[attack]

        ])

    return pd.DataFrame(rows,columns=[

        "Attack",
        "Severity",
        "Likelihood",
        "Impact",
        "Severity Weight",
        "Risk Score",
        "MITRE Technique"

    ])

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.header("Cyber Range Controls")

records=st.sidebar.slider("Synthetic Logs",10,500,100)

if st.sidebar.button("Generate Data"):

    st.session_state["data"]=generate_data(records)

# -------------------------------------------------
# DATA
# -------------------------------------------------

df=None

if "data" in st.session_state:
    df=st.session_state["data"]

# -------------------------------------------------
# CYBER EVENT LOG
# -------------------------------------------------

st.header("Cyber Event Logs")

if df is not None:

    st.dataframe(df)

    st.info("""
Cyber Event Logs simulate SIEM logs.

Fields Explained:

Attack → type of cyber attack observed.

Severity → impact classification.

Likelihood → probability of attack success.

Impact → damage potential.

Severity Weight → security priority factor.

Risk Score = Likelihood × Impact × Weight.

MITRE Technique → mapping to MITRE ATT&CK framework.
""")

# -------------------------------------------------
# ANOMALY DETECTION
# -------------------------------------------------

if df is not None:

    st.header("AI Anomaly Detection")

    model=IsolationForest(contamination=0.1)

    df["anomaly"]=model.fit_predict(df[["Risk Score"]])

    anomalies=df[df["anomaly"]==-1]

    st.dataframe(anomalies)

    st.info("""
AI anomaly detection uses machine learning to find abnormal risk patterns.

Purpose:

Identify unusual attacks

Detect insider threats

Detect previously unseen attacks

Benefit:

Early threat detection beyond traditional rule-based systems.
""")

# -------------------------------------------------
# ATTACK DISTRIBUTION
# -------------------------------------------------

if df is not None:

    st.header("Attack Distribution")

    fig=px.histogram(df,x="Attack")

    st.plotly_chart(fig,use_container_width=True)

    st.info("""
Attack Distribution shows frequency of attack types.

Purpose:

Identify most common attack vectors.

Benefit:

Security teams can prioritize defenses for the most frequent attacks.
""")

# -------------------------------------------------
# MITRE ATTACK HEATMAP
# -------------------------------------------------

st.header("MITRE ATT&CK Heatmap")

tech=list(mitre_map.values())

heat=pd.DataFrame(np.random.randint(0,10,(1,len(tech))),columns=tech)

fig=px.imshow(heat)

st.plotly_chart(fig,use_container_width=True)

st.info("""
MITRE ATT&CK heatmap maps attacks to real-world adversary techniques.

Purpose:

Understand attacker tactics.

Benefit:

Align defensive strategies with known adversary behaviors.
""")

# -------------------------------------------------
# NETWORK ATTACK GRAPH
# -------------------------------------------------

st.header("Network Attack Graph")

G=nx.erdos_renyi_graph(20,0.15)

pos=nx.spring_layout(G)

edge_x=[]
edge_y=[]

for edge in G.edges():

    x0,y0=pos[edge[0]]
    x1,y1=pos[edge[1]]

    edge_x.extend([x0,x1,None])
    edge_y.extend([y0,y1,None])

edge_trace=go.Scatter(x=edge_x,y=edge_y,mode="lines")

node_x=[]
node_y=[]

for node in G.nodes():

    x,y=pos[node]
    node_x.append(x)
    node_y.append(y)

node_trace=go.Scatter(x=node_x,y=node_y,mode="markers+text")

fig=go.Figure(data=[edge_trace,node_trace])

st.plotly_chart(fig,use_container_width=True)

st.info("""
Network Attack Graph shows relationships between network nodes.

Purpose:

Visualize attacker movement.

Benefit:

Detect lateral movement and compromised systems.
""")

# -------------------------------------------------
# ATTACK PROPAGATION
# -------------------------------------------------

st.header("Attack Propagation Simulation")

steps=10
x=list(range(steps))
y=[random.randint(1,5) for i in range(steps)]

fig=go.Figure()

fig.add_trace(go.Scatter(x=x,y=y,mode="lines+markers"))

st.plotly_chart(fig,use_container_width=True)

st.info("""
Attack propagation simulation shows how an attack spreads.

Purpose:

Understand infection spread patterns.

Benefit:

Train analysts to contain attacks quickly.
""")

# -------------------------------------------------
# CYBER KILL CHAIN
# -------------------------------------------------

st.header("3D Cyber Kill Chain")

stages=["Recon","Weaponization","Delivery","Exploitation","Installation","Command Control","Exfiltration"]

fig=go.Figure(data=[go.Scatter3d(

x=list(range(len(stages))),
y=[1]*len(stages),
z=list(range(len(stages))),
text=stages,
mode="markers+lines"

)])

st.plotly_chart(fig,use_container_width=True)

st.info("""
Cyber Kill Chain explains attack lifecycle.

Stages:

Recon → attacker gathers intelligence

Weaponization → malware prepared

Delivery → attack delivered

Exploitation → vulnerability exploited

Installation → malware installed

C2 → attacker control channel

Exfiltration → data stolen

Benefit:

Helps defenders stop attacks at earlier stages.
""")

# -------------------------------------------------
# AUTONOMOUS DEFENSE AGENTS
# -------------------------------------------------

st.header("Autonomous Cyber Defense Agents")

if st.button("Simulate Attack"):

    attack=random.choice(list(attack_library.keys()))

    st.error(f"Attack Detected: {attack}")

    st.write(attack_library[attack])

    st.info("""
Blue Team Response:

Block malicious IP

Reset compromised credentials

Patch vulnerability

SOC Analyst Actions:

Investigate logs

Correlate events

Trigger alerts

Incident Response:

Isolate infected systems

Deploy forensic analysis

Threat Hunting:

Search for similar indicators across systems.
""")