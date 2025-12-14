# This system demonstrates 6G-enabled, 
# role-secured, 
# AI-driven threat intelligence, 

# edge/core AI decisioning, 
# network slicing, 
# digital-twin forecasting, and 
# NATO-aligned reporting  
# suitable for DISA, JADC2, and 
# coalition environments.

# 6G-DISA-Threat-Intelligence-Platform
# Designed & Developed by Randy Singh – KNet Consulting

import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from fpdf import FPDF
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="DISA 6G Threat Intelligence", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
.header {
    background: linear-gradient(90deg,#002868,#005ea2);
    padding: 20px;
    border-radius: 12px;
    color: white;
    text-align: center;
}
.explain-box {
    background-color:#f4f6f9;
    padding:12px;
    border-left:5px solid #005ea2;
    border-radius:6px;
    font-size:14px;
}
.reset button {
    background-color: #dc3545 !important;
    color: white !important;
    font-weight: bold;
}
.logout button {
    background-color: #6c757d !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- RBAC ----------------
ROLES = {
    "Analyst": ["view", "analyze"],
    "Commander": ["view", "analyze", "export"],
    "Admin": ["view", "analyze", "export", "configure"]
}

if "role" not in st.session_state:
    st.session_state.role = None

# ---------------- LOGIN / LOGOUT ----------------
if st.session_state.role is None:
    st.markdown("###  Secure Role-Based Access")
    role = st.selectbox("Select Role", list(ROLES.keys()))
    if st.button("Login"):
        st.session_state.role = role
        st.rerun()
else:
    with st.sidebar:
        st.markdown(f"**Logged in as:** {st.session_state.role}")
        st.markdown('<div class="logout">', unsafe_allow_html=True)
        if st.button("Log out / Switch Role"):
            st.session_state.role = None
            st.session_state.data = None
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- HEADER ----------------
if st.session_state.role:
    st.markdown(f"""
    <div class="header">
    <h1>DISA / DoD 6G AI Threat Intelligence Platform</h1>
    <h3>Role: {st.session_state.role} | Designed & Developed by Randy Singh</h3>
    </div>
    """, unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "data" not in st.session_state:
    st.session_state.data = None

# ---------------- DATA GENERATOR ----------------
def generate_data(n):
    countries = ["United States", "China", "Russia", "Iran", "India", "North Korea"]
    rows = []
    for _ in range(n):
        rows.append({
            "Latitude": random.uniform(-60, 75),
            "Longitude": random.uniform(-180, 180),
            "Country": random.choice(countries),
            "Threat": random.choice(["Cyber", "Missile", "Drone", "SIGINT"]),
            "Severity": random.choice(["Low", "Medium", "High"]),
            "Edge Risk": random.randint(10, 70),
            "Core Risk": random.randint(20, 95),
            "Timestamp": datetime.utcnow()
        })
    df = pd.DataFrame(rows)
    df["Final Risk"] = (df["Edge Risk"] * 0.5 + df["Core Risk"] * 0.5).round(2)
    return df

# ---------------- CONTROLS ----------------
c1, c2, c3, c4 = st.columns([2,2,2,1])

with c1:
    count = st.slider("Threat Events", 10, 500, 50)

with c2:
    if st.button("Generate Sample Data"):
        st.session_state.data = generate_data(count)

with c3:
    upload = st.file_uploader("Upload CSV", type=["csv"])
    if upload:
        st.session_state.data = pd.read_csv(upload)

with c4:
    st.markdown('<div class="reset">', unsafe_allow_html=True)
    if st.button("RESET"):
        st.session_state.data = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- DISPLAY DATA ----------------
if st.session_state.data is not None:
    st.subheader(" Active Threat Data")
    st.dataframe(st.session_state.data, use_container_width=True)

# ---------------- LIVE MAP ----------------
if st.session_state.data is not None:
    st.subheader(" Live Global Threat Map (Satellite View)")
    fig = px.scatter_geo(
        st.session_state.data,
        lat="Latitude",
        lon="Longitude",
        color="Severity",
        size="Final Risk",
        hover_name="Country",
        hover_data=["Threat","Severity","Final Risk"],
        text="Country",
        projection="natural earth",
        title="Global Threat Overlay (Country + Severity)"
    )
    fig.update_traces(textposition="top center")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- SIGINT / CYBER FEED ----------------
st.subheader(" Live SIGINT / Cyber Feed (Simulated)")
feed = [{
    "Time": datetime.utcnow() - timedelta(minutes=i*3),
    "Event": random.choice([
        "Encrypted burst transmission detected",
        "Suspicious C2 beacon identified",
        "Radar illumination anomaly",
        "Drone telemetry deviation",
        "Cyber lateral movement detected"
    ])
} for i in range(5)]
st.table(pd.DataFrame(feed))

# ---------------- 6G ANALYTICS ----------------
st.subheader(" 6G Intelligence Analytics")

m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Avg Latency (ms)", "8.3")
with m2:
    st.metric("Edge Decisions (%)", "62%")
with m3:
    st.metric("Mission-Critical Slice", "High")

st.markdown("""
<div class="explain-box">
<b>Why these 6G metrics matter:</b><br><br>

<b>Avg Latency (ms):</b>  
Ultra-low latency enables near-instant detection and response across dense sensor networks — critical for missile, cyber, and drone threats.

<b>Edge Decisions (%):</b>  
Shows how much AI processing occurs at the edge (sensors, forward bases).  
Higher edge decision rates reduce response time and core-network load.

<b>Mission-Critical Slice:</b>  
6G network slicing prioritizes high-risk threats over routine traffic, ensuring survivability and command continuity.
</div>
""", unsafe_allow_html=True)

# ---------------- DIGITAL TWIN ----------------
st.subheader(" 6G Digital Twin Threat Forecast")
forecast = pd.DataFrame({
    "Time": ["Now", "T+5 min", "T+15 min"],
    "Projected Risk": [42, 58, 75]
})
st.line_chart(forecast.set_index("Time"))

# ---------------- EXPORT ----------------
if st.session_state.data is not None and "export" in ROLES[st.session_state.role]:
    st.subheader(" STANAG-Compliant Export")

    st.download_button(
        "Export CSV",
        st.session_state.data.to_csv(index=False),
        "STANAG_threats.csv"
    )

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0,10,"STANAG 4774 / DISA Threat Intelligence Report", ln=True)
    pdf.multi_cell(0,8,f"Generated: {datetime.utcnow()}")
    path = "/tmp/stanag_report.pdf"
    pdf.output(path)

    with open(path, "rb") as f:
        st.download_button("Export PDF", f, "STANAG_Report.pdf")

