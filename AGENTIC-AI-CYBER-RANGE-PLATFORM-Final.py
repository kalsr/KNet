# ==========================================================
# AGENTIC AI CYBER RANGE PLATFORM – VERSION(FINAL)
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
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io

st.set_page_config(layout="wide")

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown("""
<h1 style='background-color:#0b3d91;color:white;padding:15px;text-align:center'>
Agentic AI Cyber Range Platform – Version 8
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
    "Phishing":"Email social engineering attack stealing credentials.",
    "Brute Force":"Automated password guessing attack.",
    "SQL Injection":"Malicious SQL commands injected into databases.",
    "DDoS":"Mass traffic flooding server infrastructure.",
    "Privilege Escalation":"Attacker gains higher system privileges.",
    "Lateral Movement":"Attacker spreads across network.",
    "Malware":"Malicious software executed on host.",
    "Ransomware":"System files encrypted for ransom payment.",
    "Zero Day":"Unknown vulnerability exploited.",
    "Supply Chain Attack":"Compromise via trusted vendor software."
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

severity_levels = ["Low","Medium","High","Critical"]

# -------------------------------------------------
# SYNTHETIC DATA GENERATOR
# -------------------------------------------------
def generate_data(n):
    rows = []
    for i in range(n):
        attack = random.choice(list(attack_library.keys()))
        severity = random.choice(severity_levels)
        likelihood = random.randint(1,5)
        impact = random.randint(1,5)
        weight = random.randint(1,5)
        risk = likelihood * impact * weight
        rows.append([
            attack,
            severity,
            likelihood,
            impact,
            weight,
            risk,
            mitre_map[attack]
        ])
    return pd.DataFrame(rows, columns=[
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
records = st.sidebar.slider("Synthetic Logs", 10, 500, 100)

if st.sidebar.button("Generate Synthetic Data"):
    st.session_state["data"] = generate_data(records)

uploaded_file = st.sidebar.file_uploader("Upload Real Cyber Dataset (CSV)", type=["csv"])
if uploaded_file is not None:
    st.session_state["data"] = pd.read_csv(uploaded_file)

# -------------------------------------------------
# DATA
# -------------------------------------------------
df = None
if "data" in st.session_state:
    df = st.session_state["data"]

# -------------------------------------------------
# SUMMARY STATISTICS
# -------------------------------------------------
if df is not None:
    st.header("Cyber Range Summary")
    total_records = len(df)
    st.metric("Total Records", total_records)

    # Anomaly Detection
    model = IsolationForest(contamination=0.1)
    df["anomaly"] = model.fit_predict(df[["Risk Score"]])
    total_anomalies = len(df[df["anomaly"] == -1])
    st.metric("Total Anomalies Detected", total_anomalies)

    st.subheader("Records by Severity")
    severity_counts = df["Severity"].value_counts()
    st.bar_chart(severity_counts)

    st.subheader("Records by Attack Type")
    attack_counts = df["Attack"].value_counts()
    st.bar_chart(attack_counts)

# -------------------------------------------------
# CYBER EVENT LOG
# -------------------------------------------------
st.header("Cyber Event Logs")
if df is not None:
    st.dataframe(df)

# -------------------------------------------------
# AI ANOMALY DETECTION
# -------------------------------------------------
if df is not None:
    st.header("AI Anomaly Detection")
    anomalies = df[df["anomaly"] == -1]
    st.dataframe(anomalies)

# -------------------------------------------------
# ATTACK DISTRIBUTION
# -------------------------------------------------
if df is not None:
    st.header("Attack Distribution")
    fig = px.histogram(df, x="Attack", color="Severity", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Attack Explanation & Benefits")
    for attack, desc in attack_library.items():
        st.write(f"**{attack}** – {desc} Simulation helps trainees understand how attackers compromise systems and how defenses mitigate risks.")

# -------------------------------------------------
# MITRE ATTACK HEATMAP
# -------------------------------------------------
st.header("MITRE ATT&CK Heatmap")
tech = list(mitre_map.values())
heat = pd.DataFrame(np.random.randint(0,10,(1,len(tech))), columns=tech)
fig = px.imshow(heat, text_auto=True, aspect="auto")
st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# NETWORK ATTACK GRAPH
# -------------------------------------------------
st.header("Network Attack Graph")
G = nx.erdos_renyi_graph(20,0.15)
pos = nx.spring_layout(G)
edge_x, edge_y = [], []
for edge in G.edges():
    x0,y0 = pos[edge[0]]
    x1,y1 = pos[edge[1]]
    edge_x.extend([x0,x1,None])
    edge_y.extend([y0,y1,None])
edge_trace = go.Scatter(x=edge_x, y=edge_y, mode="lines", line=dict(color='blue', width=1))
node_x, node_y = [], []
for node in G.nodes():
    x,y = pos[node]
    node_x.append(x)
    node_y.append(y)
node_trace = go.Scatter(x=node_x, y=node_y, mode="markers", marker=dict(size=10, color='red'))
fig = go.Figure(data=[edge_trace, node_trace])
st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# ATTACK PROPAGATION
# -------------------------------------------------
st.header("Attack Propagation Simulation")
steps = 10
x = list(range(steps))
y = [random.randint(1,5) for _ in range(steps)]
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode="lines+markers"))
st.plotly_chart(fig, use_container_width=True)
st.markdown("Simulates how attacks move through the network over time. Useful for understanding propagation speed and containment strategies.")

# -------------------------------------------------
# CYBER KILL CHAIN
# -------------------------------------------------
st.header("3D Cyber Kill Chain")
stages = ["Recon","Weaponization","Delivery","Exploitation","Installation","Command Control","Exfiltration"]
fig = go.Figure(data=[go.Scatter3d(
    x=list(range(len(stages))),
    y=[1]*len(stages),
    z=list(range(len(stages))),
    text=stages,
    mode="markers+lines",
    marker=dict(size=5, color='green')
)])
st.plotly_chart(fig, use_container_width=True)
st.markdown("Demonstrates the stages of a cyber attack and helps trainees visualize mitigation points at each stage.")

# -------------------------------------------------
# CYBER DEFENSE OPERATIONS PANEL
# -------------------------------------------------
st.header("Cyber Operations Simulation")
col1,col2,col3,col4,col5 = st.columns(5)
if "current_attack" not in st.session_state:
    st.session_state["current_attack"] = None

# ---------------- RED TEAM ----------------
with col1:
    if st.button("Red Team Attack"):
        attack = random.choice(list(attack_library.keys()))
        st.session_state["current_attack"] = attack
        st.error(f"Red Team launched: {attack}")
        st.write(attack_library[attack])

# ---------------- BLUE TEAM ----------------
with col2:
    if st.button("Blue Team Defense"):
        attack = st.session_state["current_attack"]
        if attack:
            st.success("Blue Team Activated")
            st.write("""
Mitigation Actions:
• Block malicious IPs  
• Patch vulnerabilities  
• Enable firewall rules  
• Reset compromised credentials
""")

# ---------------- SOC ANALYST ----------------
with col3:
    if st.button("SOC Analyst Investigation"):
        attack = st.session_state["current_attack"]
        if attack:
            st.warning("SOC Analyst Investigation")
            st.write("""
SOC Tasks:
• Review SIEM logs  
• Correlate alerts  
• Identify Indicators of Compromise (IOCs)  
• Escalate incident severity
""")

# ---------------- INCIDENT RESPONSE ----------------
with col4:
    if st.button("Incident Response"):
        attack = st.session_state["current_attack"]
        if attack:
            st.error("Incident Response Initiated")
            st.write("""
Incident Response Steps:
• Isolate infected systems  
• Perform forensic analysis  
• Remove malware persistence  
• Restore systems from backups
""")

# ---------------- THREAT HUNTING ----------------
with col5:
    if st.button("Threat Hunting"):
        attack = st.session_state["current_attack"]
        if attack:
            st.info("Threat Hunting Operation")
            st.write("""
Threat Hunting Activities:
• Search network for similar attack patterns  
• Analyze endpoint telemetry  
• Identify lateral movement attempts  
• Detect hidden persistence mechanisms
""")

# -------------------------------------------------
# EXPORT RESULTS
# -------------------------------------------------
st.header("Export Cyber Range Results")
if df is not None:
    csv = df.to_csv(index=False).encode()
    st.download_button("Download CSV", csv, "cyber_results.csv")
    json = df.to_json()
    st.download_button("Download JSON", json, "cyber_results.json")
    buffer = io.BytesIO()
    styles = getSampleStyleSheet()
    elements = [Paragraph("Cyber Range Report", styles['Title']), Spacer(1,20)]
    for i,row in df.iterrows():
        elements.append(Paragraph(str(row.to_dict()), styles['BodyText']))
    doc = SimpleDocTemplate(buffer)
    doc.build(elements)
    st.download_button("Download PDF", buffer.getvalue(), "cyber_report.pdf")