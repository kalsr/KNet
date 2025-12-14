# Real 6G

# This platform demonstrates 6G-aligned AI threat intelligence, 
# integrating dense sensor simulation, 
# Feeds edge/core AI decisions, 
# network slicing, 
# real-time geo-visualization, 
# SIGINT-style
# NATO-formatted reporting, 
# and secure role-based access.
# It models the intelligence architecture that 6G is designed to enable, not just radio theory.

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
.role-box {
    background-color: #f1f3f5;
    padding: 10px;
    border-radius: 8px;
}
.reset button {
    background-color: #dc3545 !important;
    color: white !important;
    font-weight: bold;
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

if st.session_state.role is None:
    st.markdown("### 🔐 Secure Access")
    role = st.selectbox("Select Role", list(ROLES.keys()))
    if st.button("Login"):
        st.session_state.role = role
        st.rerun()

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
    countries = ["USA", "China", "Russia", "Iran", "India", "North Korea"]
    rows = []
    for _ in range(n):
        rows.append({
            "Latitude": random.uniform(-70, 70),
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
    st.subheader("📋 Active Threat Data")
    st.dataframe(st.session_state.data, use_container_width=True)

# ---------------- LIVE MAP ----------------
if st.session_state.data is not None:
    st.subheader("🛰 Live Global Threat Map (Satellite View)")
    fig = px.scatter_geo(
        st.session_state.data,
        lat="Latitude",
        lon="Longitude",
        color="Severity",
        size="Final Risk",
        hover_name="Threat",
        projection="natural earth",
        title="Global Threat Overlay"
    )
    st.plotly_chart(fig, use_container_width=True)

# ---------------- SIGINT / CYBER FEED ----------------
st.subheader("📡 Live SIGINT / Cyber Feed (Simulated)")
feed = []
for i in range(5):
    feed.append({
        "Time": datetime.utcnow() - timedelta(minutes=i*2),
        "Event": random.choice([
            "Suspicious C2 traffic detected",
            "Encrypted burst transmission",
            "Malware beacon identified",
            "Radar illumination spike",
            "Drone telemetry anomaly"
        ])
    })
st.table(pd.DataFrame(feed))

# ---------------- 6G ANALYTICS ----------------
st.subheader("⚡ 6G Intelligence Analytics")
b1, b2, b3 = st.columns(3)

with b1:
    st.metric("Avg Latency (ms)", "8.3")

with b2:
    st.metric("Edge Decisions (%)", "62%")

with b3:
    st.metric("Mission-Critical Slice", "High")

# ---------------- DIGITAL TWIN ----------------
st.subheader("🔮 Digital Twin Forecast")
forecast = pd.DataFrame({
    "Time": ["Now", "T+5", "T+15"],
    "Projected Risk": [40, 55, 72]
})
st.line_chart(forecast.set_index("Time"))

# ---------------- EXPORT ----------------
if st.session_state.data is not None and "export" in ROLES[st.session_state.role]:
    st.markdown("### 📤 STANAG-Compliant Export")

    st.download_button(
        "Export CSV",
        st.session_state.data.to_csv(index=False),
        "STANAG_threats.csv"
    )

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0,10,"STANAG 4774 Threat Intelligence Report", ln=True)
    pdf.multi_cell(0,8,f"Generated: {datetime.utcnow()}")
    path = "/tmp/stanag_report.pdf"
    pdf.output(path)

    with open(path, "rb") as f:
        st.download_button("Export PDF", f, "STANAG_Report.pdf")
