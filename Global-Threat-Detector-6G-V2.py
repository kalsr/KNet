#6G-V2
# Global-Threat-Detector-6g-V2 

import streamlit as st
import pandas as pd
import random
import numpy as np
from fpdf import FPDF

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Global Threat Detector", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
.header {
    background: linear-gradient(90deg,#0b5ed7,#4dabf7);
    padding: 20px;
    border-radius: 14px;
    text-align: center;
    color: white;
}
.block-btn button {
    width: 100%;
    font-weight: bold;
    height: 55px;
}
.reset button {
    background-color: #dc3545 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header">
    <h1>Global Real-Time Threat Detection and Analysis</h1>
    <h3>Designed & Developed by Randy Singh</h3>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- SESSION STATE ----------------
if "raw_data" not in st.session_state:
    st.session_state.raw_data = None

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

# ---------------- DATA GENERATOR ----------------
def generate_data(n):
    random.seed()  # ensures new data every run
    countries = ["USA", "China", "Russia", "Iran", "North Korea", "India"]
    threats = []

    for _ in range(n):
        threats.append({
            "Latitude": random.uniform(-90, 90),
            "Longitude": random.uniform(-180, 180),
            "Country": random.choice(countries),
            "Threat Type": random.choice(["Missile", "Cyber", "Drone"]),
            "Severity": random.choice(["Low", "Medium", "High"]),
            "Risk Score": random.randint(20, 95),
            "Hour": random.randint(0, 23)
        })
    return pd.DataFrame(threats)

# ---------------- CONTROLS ----------------
c1, c2, c3 = st.columns([2,2,1])

with c1:
    records = st.slider("Threat Records", 5, 200, 25)

with c2:
    if st.button("Generate / Preview Data"):
        st.session_state.raw_data = generate_data(records)
        st.session_state.analysis_done = False

with c3:
    with st.container():
        st.markdown('<div class="reset">', unsafe_allow_html=True)
        if st.button("RESET"):
            st.session_state.raw_data = None
            st.session_state.analysis_done = False
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- DISPLAY RAW DATA ----------------
if st.session_state.raw_data is not None:
    st.subheader("📋 Preview Threat Data")
    st.dataframe(st.session_state.raw_data, use_container_width=True)

# ---------------- FEATURE BUTTONS ----------------
st.markdown("### Analysis Modules")
b1, b2, b3, b4 = st.columns(4)

with b1:
    ml_btn = st.button(" ML Risk Scoring")
with b2:
    time_btn = st.button(" Time-Based Simulation")
with b3:
    country_btn = st.button(" Country Aggregation")
with b4:
    llm_btn = st.button(" LLM Explanation")

# ---------------- RUN ANALYSIS ----------------
if st.session_state.raw_data is not None and (ml_btn or time_btn or country_btn or llm_btn):
    df = st.session_state.raw_data
    st.session_state.analysis_done = True

    st.markdown("---")

    if ml_btn:
        st.subheader(" ML Threat Risk Scoring")
        st.bar_chart(df["Risk Score"])

    if time_btn:
        st.subheader("⏱ Time-Based Attack Simulation")
        st.line_chart(df.groupby("Hour").size())

    if country_btn:
        st.subheader(" Country-Level Aggregation")
        st.bar_chart(df["Country"].value_counts())

    if llm_btn:
        st.subheader(" LLM-Based Threat Explanation")
        st.info("""
        Based on detected threat patterns, elevated risks are observed in
        regions with high severity cyber and missile activities.
        Immediate mitigation and monitoring recommended.
        """)

# ---------------- EXPORT ----------------
if st.session_state.analysis_done:
    st.markdown("---")
    e1, e2 = st.columns(2)

    with e1:
        st.download_button(
            "⬇ Export CSV",
            st.session_state.raw_data.to_csv(index=False),
            "threats.csv",
            "text/csv"
        )

    with e2:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, "Global Threat Report", ln=True)
        path = "/tmp/report.pdf"
        pdf.output(path)

        with open(path, "rb") as f:
            st.download_button("⬇ Export PDF", f, "threat_report.pdf")
