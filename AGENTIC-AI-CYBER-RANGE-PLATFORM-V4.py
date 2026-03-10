

# ============================================================
# AGENTIC AI CYBER RANGE PLATFORM – VERSION 4
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
Agentic AI Cyber Range Platform – Version 4
<br>
Developed by Randy Singh – Kalsnet (KNet) Consulting Group
</h1>
""",unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR DATA CONTROLS
# ---------------------------------------------------------

st.sidebar.header("Cyber Data Controls")

data_mode = st.sidebar.radio(
    "Select Data Source",
    ["Synthetic Data","Upload Real Data"]
)

records = st.sidebar.slider("Synthetic Records",10,500,100)

generate = st.sidebar.button("Generate Synthetic Data")
reset = st.sidebar.button("Reset Data")

uploaded_file=None

if data_mode=="Upload Real Data":

    uploaded_file = st.sidebar.file_uploader(
        "Upload Cyber Dataset CSV",
        type=["csv"]
    )

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
# RESPONSE MAP
# ---------------------------------------------------------

response_map={

"Phishing":{

"blue":"Block phishing domain and reset user credentials.",
"soc":"Analyze email gateway logs.",
"ir":"Quarantine infected workstation.",
"hunter":"Search enterprise logs for similar campaigns."

},

"Brute Force":{

"blue":"Enable account lockout and block IP.",
"soc":"Investigate authentication failures.",
"ir":"Reset compromised accounts.",
"hunter":"Scan identity logs."

},

"DDoS":{

"blue":"Activate rate limiting and firewall filtering.",
"soc":"Monitor abnormal traffic spikes.",
"ir":"Coordinate with ISP mitigation.",
"hunter":"Identify botnet sources."

},

"SQL Injection":{

"blue":"Deploy WAF rules.",
"soc":"Analyze application logs.",
"ir":"Patch vulnerable input validation.",
"hunter":"Search DB access anomalies."
}

}

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
            attack,severity,src,dst,
            likelihood,impact,weight,
            risk,mitre_map[attack]
        ])

    return pd.DataFrame(rows,columns=[

        "Attack","Severity","Source IP","Target IP",
        "Likelihood","Impact","Severity Weight",
        "Risk Score","MITRE Technique"

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

# ---------------------------------------------------------
# DATA DISPLAY
# ---------------------------------------------------------

df=None

if "data" in st.session_state:
    df=st.session_state["data"]

if df is not None and not df.empty:

    st.subheader("Cyber Event Logs")
    st.dataframe(df)

    # -----------------------------------------------------
    # AI ANOMALY DETECTION
    # -----------------------------------------------------

    st.subheader("AI Anomaly Detection")

    if "Risk Score" in df.columns:

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

    if "Risk Score" in df.columns:
        c2.metric("High Risk Events",len(df[df["Risk Score"]>40]))
    else:
        c2.metric("High Risk Events","N/A")

    c3.metric("Attack Types",df["Attack"].nunique())

    c4.metric("Unique Sources",df["Source IP"].nunique())

# ---------------------------------------------------------
# ATTACK DISTRIBUTION
# ---------------------------------------------------------

st.subheader("Attack Distribution")

if df is not None and not df.empty and "Attack" in df.columns:

    col1,col2=st.columns(2)

    fig=px.bar(df,x="Attack",title="Attack Distribution")
    col1.plotly_chart(fig,use_container_width=True)

    if "Severity" in df.columns:
        fig2=px.pie(df,names="Severity",title="Severity Distribution")
        col2.plotly_chart(fig2,use_container_width=True)

else:

    st.info("Generate synthetic data or upload dataset.")

# ---------------------------------------------------------
# MITRE ATTACK HEATMAP
# ---------------------------------------------------------

st.subheader("MITRE ATT&CK Heatmap")

tech=list(mitre_map.values())

heat=pd.DataFrame(np.random.randint(0,10,(1,len(tech))),columns=tech)

fig=px.imshow(heat)

st.plotly_chart(fig,use_container_width=True)

# ---------------------------------------------------------
# NETWORK ATTACK GRAPH
# ---------------------------------------------------------

st.subheader("Network Attack Graph")

G=nx.Graph()

for i in range(20):

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

st.subheader("3D Cyber Attack Kill Chain")

stages=["Recon","Access","Privilege","Lateral","Exfiltration"]

fig=go.Figure(data=[go.Scatter3d(

x=[1,2,3,4,5],
y=[1,1,1,1,1],
z=[1,2,3,4,5],
mode='markers+lines',
text=stages

)])

st.plotly_chart(fig,use_container_width=True)

# ---------------------------------------------------------
# THREAT INTEL FEED
# ---------------------------------------------------------

st.subheader("Threat Intelligence Feed")

intel=[

"APT group targeting finance sector",
"Zero day vulnerability discovered",
"Credential stuffing attacks increasing",
"Malicious IP scanning activity",
"Ransomware campaign detected"

]

for i in range(4):
    st.warning(random.choice(intel))

# ---------------------------------------------------------
# AUTONOMOUS CYBER AGENTS
# ---------------------------------------------------------

st.subheader("Autonomous Cyber Agents")

col1,col2,col3,col4,col5=st.columns(5)

with col1:

    if st.button("Red Team Attack"):

        attack=random.choice(attack_types)

        st.session_state["last_attack"]=attack

        st.error(f"Red Team Attack: {attack}")

with col2:

    if st.button("Blue Team") and "last_attack" in st.session_state:

        attack=st.session_state["last_attack"]

        st.info(response_map.get(attack,{}).get("blue"))

with col3:

    if st.button("SOC Copilot") and "last_attack" in st.session_state:

        attack=st.session_state["last_attack"]

        st.warning(response_map.get(attack,{}).get("soc"))

with col4:

    if st.button("Incident Response") and "last_attack" in st.session_state:

        attack=st.session_state["last_attack"]

        st.success(response_map.get(attack,{}).get("ir"))

with col5:

    if st.button("Threat Hunter") and "last_attack" in st.session_state:

        attack=st.session_state["last_attack"]

        st.success(response_map.get(attack,{}).get("hunter"))

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

        elements.append(Paragraph(str(row.to_dict()),styles["BodyText"]))

    doc=SimpleDocTemplate(buffer)

    doc.build(elements)

    st.download_button("Download PDF",buffer.getvalue(),"cyber_report.pdf")