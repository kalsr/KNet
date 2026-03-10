

# ============================================================
# AGENTIC AI CYBER RANGE PLATFORM – VERSION 5
# Developed by Randy Singh – Kalsnet (KNet) Consulting Group
# ============================================================

import streamlit as st
import pandas as pd
import random
import numpy as np
import io
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
Agentic AI Cyber Range Platform – Version 5
<br>
Advanced Cyber Defense Simulation Environment
<br>
Developed by Randy Singh – Kalsnet (KNet) Consulting Group
</h1>
""",unsafe_allow_html=True)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.header("Cyber Range Controls")

data_mode = st.sidebar.radio(
    "Select Data Source",
    ["Synthetic Data","Upload Real Data"]
)

records = st.sidebar.slider("Synthetic Records",10,500,100)

generate = st.sidebar.button("Generate Synthetic Data")
reset = st.sidebar.button("Reset Data")

uploaded_file=None

if data_mode=="Upload Real Data":

    uploaded_file=st.sidebar.file_uploader(
        "Upload Cyber Dataset CSV",
        type=["csv"]
    )


# ---------------------------------------------------------
# MITRE ATTACK MAP
# ---------------------------------------------------------

mitre_map={

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

        src=f"192.168.1.{random.randint(1,254)}"
        dst=f"10.0.0.{random.randint(1,254)}"

        likelihood=random.randint(1,5)
        impact=random.randint(1,5)
        weight=random.randint(1,5)

        risk=likelihood*impact*weight

        rows.append([

            attack,
            severity,
            src,
            dst,
            likelihood,
            impact,
            weight,
            risk,
            mitre_map[attack]

        ])

    return pd.DataFrame(rows,columns=[

        "Attack",
        "Severity",
        "Source IP",
        "Target IP",
        "Likelihood",
        "Impact",
        "Severity Weight",
        "Risk Score",
        "MITRE Technique"

    ])


# ---------------------------------------------------------
# DATA MANAGEMENT
# ---------------------------------------------------------

if reset:
    st.session_state["data"]=None

if data_mode=="Synthetic Data":

    if generate:
        st.session_state["data"]=generate_data(records)

elif data_mode=="Upload Real Data":

    if uploaded_file is not None:

        df=pd.read_csv(uploaded_file)

        st.session_state["data"]=df


df=None

if "data" in st.session_state:

    df=st.session_state["data"]


# ---------------------------------------------------------
# DATA DISPLAY
# ---------------------------------------------------------

if df is not None and not df.empty:

    st.subheader("Cyber Event Logs")

    st.dataframe(df)

# ---------------------------------------------------------
# SOC DASHBOARD
# ---------------------------------------------------------

if df is not None and not df.empty:

    st.subheader("SOC Security Dashboard")

    col1,col2,col3,col4=st.columns(4)

    col1.metric("Total Events",len(df))

    col2.metric("Attack Types",df["Attack"].nunique())

    col3.metric("Unique Sources",df["Source IP"].nunique())

    if "Risk Score" in df.columns:
        col4.metric("High Risk",len(df[df["Risk Score"]>40]))
    else:
        col4.metric("High Risk","N/A")


# ---------------------------------------------------------
# AI ANOMALY DETECTION
# ---------------------------------------------------------

if df is not None and not df.empty and "Risk Score" in df.columns:

    st.subheader("AI Anomaly Detection")

    model=IsolationForest(contamination=0.1)

    df["anomaly"]=model.fit_predict(df[["Risk Score"]])

    anomalies=df[df["anomaly"]==-1]

    st.write("Detected anomalies:",len(anomalies))

    st.dataframe(anomalies)


# ---------------------------------------------------------
# ATTACK DISTRIBUTION
# ---------------------------------------------------------

st.subheader("Attack Distribution")

if df is not None and not df.empty and "Attack" in df.columns:

    fig=px.histogram(df,x="Attack")

    st.plotly_chart(fig,use_container_width=True)

else:

    st.info("Generate or upload data")


# ---------------------------------------------------------
# MITRE ATT&CK HEATMAP
# ---------------------------------------------------------

st.subheader("MITRE ATT&CK Heatmap")

tech=list(mitre_map.values())

heat=pd.DataFrame(

    np.random.randint(0,10,(1,len(tech))),
    columns=tech

)

fig=px.imshow(heat)

st.plotly_chart(fig,use_container_width=True)


# ---------------------------------------------------------
# NETWORK ATTACK GRAPH
# ---------------------------------------------------------

st.subheader("Network Attack Graph")

G=nx.Graph()

for i in range(25):

    src=f"192.168.1.{random.randint(1,25)}"
    dst=f"10.0.0.{random.randint(1,25)}"

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

node_trace=go.Scatter(

    x=node_x,
    y=node_y,
    mode='markers+text',
    text=list(G.nodes())

)

fig=go.Figure(data=[edge_trace,node_trace])

st.plotly_chart(fig,use_container_width=True)


# ---------------------------------------------------------
# ATTACK PROPAGATION SIMULATION
# ---------------------------------------------------------

st.subheader("Attack Propagation Simulation")

steps=10

x=list(range(steps))

y=[random.randint(1,5) for i in range(steps)]

fig=go.Figure()

fig.add_trace(go.Scatter(

    x=x,
    y=y,
    mode="lines+markers"

))

st.plotly_chart(fig,use_container_width=True)


# ---------------------------------------------------------
# 3D CYBER KILL CHAIN
# ---------------------------------------------------------

st.subheader("3D Cyber Kill Chain Simulation")

stages=["Recon","Access","Privilege","Lateral","Exfiltration"]

fig=go.Figure(data=[go.Scatter3d(

    x=[1,2,3,4,5],
    y=[1,1,1,1,1],
    z=[1,2,3,4,5],
    mode="markers+lines",
    text=stages

)])

st.plotly_chart(fig,use_container_width=True)


# ---------------------------------------------------------
# APT CAMPAIGN SIMULATOR
# ---------------------------------------------------------

st.subheader("APT Campaign Simulator")

if st.button("Simulate APT Attack"):

    apt=random.choice(attack_types)

    st.error(f"APT Campaign Detected: {apt}")

    st.write("Technique:",mitre_map[apt])


# ---------------------------------------------------------
# THREAT INTELLIGENCE FEED
# ---------------------------------------------------------

st.subheader("Threat Intelligence Feed")

intel=[

"Ransomware campaign spreading globally",
"New zero day vulnerability detected",
"Credential stuffing attacks increasing",
"APT group targeting financial sector",
"Mass phishing campaign discovered"

]

for i in range(4):

    st.warning(random.choice(intel))


# ---------------------------------------------------------
# AUTONOMOUS CYBER AGENTS
# ---------------------------------------------------------

st.subheader("Autonomous Cyber Defense Agents")

col1,col2,col3,col4,col5=st.columns(5)

with col1:

    if st.button("Red Team Attack"):

        attack=random.choice(attack_types)

        st.session_state["last_attack"]=attack

        st.error(f"Red Team Attack: {attack}")

with col2:

    if st.button("Blue Team") and "last_attack" in st.session_state:

        st.success("Blue Team Containment Activated")

with col3:

    if st.button("SOC Copilot") and "last_attack" in st.session_state:

        st.warning("SOC AI analyzing event")

with col4:

    if st.button("Incident Response") and "last_attack" in st.session_state:

        st.success("Incident Response procedures launched")

with col5:

    if st.button("Threat Hunter") and "last_attack" in st.session_state:

        st.info("Threat hunting across network logs")


# ---------------------------------------------------------
# EXPORT RESULTS
# ---------------------------------------------------------

st.subheader("Export Results")

if df is not None and not df.empty:

    csv=df.to_csv(index=False).encode()

    st.download_button("Download CSV",csv,"cyber_range.csv")

    st.download_button("Download JSON",df.to_json(),"cyber_range.json")

    buffer=io.BytesIO()

    styles=getSampleStyleSheet()

    elements=[Paragraph("Cyber Range Report",styles["Title"]),Spacer(1,20)]

    for i,row in df.iterrows():

        elements.append(
            Paragraph(str(row.to_dict()),styles["BodyText"])
        )

    doc=SimpleDocTemplate(buffer)

    doc.build(elements)

    st.download_button("Download PDF",buffer.getvalue(),"cyber_report.pdf")