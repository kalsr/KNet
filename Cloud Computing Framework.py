# Cloud Computing Framework


import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
import plotly.express as px
import random
import json

# Export libs
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from docx import Document
from pptx import Presentation

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(page_title="KNet Cloud Intelligence Platform", layout="wide")

st.title("☁ KNet Cloud Intelligence Platform")
st.markdown("### Enterprise Cloud Taxonomy | MITRE | Zero Trust | AI Engine")

# -----------------------------
# ROLES
# -----------------------------
role = st.sidebar.selectbox("Select Role", ["Admin", "Analyst", "Viewer"])

st.sidebar.markdown("### Role Permissions")
st.sidebar.write(f"Current Role: {role}")

# -----------------------------
# DATA STORE
# -----------------------------
if "nodes" not in st.session_state:
    st.session_state.nodes = []

# -----------------------------
# CLOUD NODE INPUT
# -----------------------------
st.sidebar.header("Cloud Builder")

node_name = st.sidebar.text_input("Node Name")
cloud_type = st.sidebar.selectbox("Cloud Type", ["IaaS", "PaaS", "SaaS"])

mitre = st.sidebar.selectbox(
    "MITRE Technique",
    ["T1078 - Valid Accounts", "T1190 - Exploit Public App", "T1059 - Command Execution"]
)

risk = st.sidebar.slider("Risk Score", 0, 100, 50)

zero_trust = st.sidebar.selectbox(
    "Zero Trust Layer",
    ["Identity", "Device", "Network", "Application", "Data"]
)

# -----------------------------
# ADD NODE
# -----------------------------
if st.sidebar.button("➕ Add Node"):
    st.session_state.nodes.append({
        "name": node_name,
        "type": cloud_type,
        "mitre": mitre,
        "risk": risk,
        "zt": zero_trust
    })

# -----------------------------
# RESET
# -----------------------------
if st.sidebar.button("🔄 Reset"):
    st.session_state.nodes = []

# -----------------------------
# AI RECOMMENDATION ENGINE
# -----------------------------
def ai_recommend(nodes):
    if not nodes:
        return "No data"

    avg_risk = sum(n["risk"] for n in nodes) / len(nodes)

    if avg_risk > 70:
        return "High Risk: Recommend Zero Trust Hardening + PaaS migration"
    elif avg_risk > 40:
        return "Medium Risk: Add IAM + Network segmentation"
    else:
        return "Low Risk: Optimize SaaS consolidation"

st.subheader("🤖 AI Recommendation Engine")
st.info(ai_recommend(st.session_state.nodes))

# -----------------------------
# TABLE VIEW
# -----------------------------
df = pd.DataFrame(st.session_state.nodes)

st.subheader("📊 Cloud Nodes")
if not df.empty:
    st.dataframe(df, use_container_width=True)

# -----------------------------
# NETWORK GRAPH (REAL ARCHITECTURE)
# -----------------------------
st.subheader("🌐 Cloud Architecture Graph")

def build_graph(data):
    G = nx.Graph()

    for n in data:
        G.add_node(n["name"], label=n["type"])

        G.add_edge(n["name"], n["type"])
        G.add_edge(n["name"], n["mitre"])
        G.add_edge(n["name"], n["zt"])

    return G

if st.button("📡 Generate Network Graph"):
    if df.empty:
        st.warning("No nodes")
    else:
        G = build_graph(st.session_state.nodes)

        net = Network(height="500px", width="100%", bgcolor="#0b1a2f", font_color="white")

        for node in G.nodes:
            net.add_node(node)

        for edge in G.edges:
            net.add_edge(edge[0], edge[1])

        net.save_graph("graph.html")

        with open("graph.html", "r", encoding="utf-8") as f:
            st.components.v1.html(f.read(), height=500)

# -----------------------------
# DRAG & DROP BUILDER SIMULATION
# -----------------------------
st.subheader("🧩 Drag & Drop Cloud Builder (Simulated)")

col1, col2, col3 = st.columns(3)

with col1:
    st.button("☁ Add IaaS Block")
with col2:
    st.button("⚙ Add PaaS Block")
with col3:
    st.button("📦 Add SaaS Block")

st.info("Drag & Drop UI can be upgraded using Streamlit components or React frontend.")

# -----------------------------
# MITRE + ZERO TRUST VIEW
# -----------------------------
st.subheader("🛡 MITRE + Zero Trust Mapping")

if not df.empty:
    fig = px.histogram(df, x="zt", color="type", title="Zero Trust Distribution")
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# EXPORT FUNCTIONS
# -----------------------------

def export_pdf(data):
    doc = SimpleDocTemplate("cloud_report.pdf")
    styles = getSampleStyleSheet()
    content = [Paragraph(str(data), styles["Normal"])]
    doc.build(content)

def export_word(data):
    doc = Document()
    doc.add_heading("Cloud Report", 0)
    doc.add_paragraph(str(data))
    doc.save("cloud_report.docx")

def export_ppt(data):
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "Cloud Report"
    slide.placeholders[1].text = str(data)
    prs.save("cloud_report.pptx")

# -----------------------------
# EXPORT BUTTONS
# -----------------------------
st.subheader("📄 Export Reports")

if st.button("Export PDF"):
    export_pdf(st.session_state.nodes)
    st.success("PDF generated")

if st.button("Export Word"):
    export_word(st.session_state.nodes)
    st.success("Word doc generated")

if st.button("Export PowerPoint"):
    export_ppt(st.session_state.nodes)
    st.success("PPT generated")

# -----------------------------
# JSON EXPORT
# -----------------------------
st.download_button(
    "⬇ Export JSON",
    json.dumps(st.session_state.nodes, indent=2),
    file_name="cloud_intelligence.json"
)