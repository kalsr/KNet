###6GGGG

# Global-Threat-Detector-6g (FIXED + ENHANCED)

import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
from fpdf import FPDF

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Global Threat Detector",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.title-box {
    background: linear-gradient(90deg,#0a63c7,#3fa9ff);
    padding: 18px;
    border-radius: 14px;
    text-align: center;
    color: white;
}
.title-box h1 {
    font-size: 36px;
    margin-bottom: 4px;
}
.title-box h3 {
    font-weight: 400;
    font-size: 18px;
}
.reset-btn {
    background-color: #ff4b4b !important;
    color: white !important;
    font-weight: bold !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="title-box">
    <h1>Global Real-Time Threat Detection and Analysis</h1>
    <h3>Designed & Developed By Randy Singh</h3>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- SAMPLE DATA GENERATOR ----------------
def generate_sample_data(n):
    threats = []
    for _ in range(n):
        threats.append({
            "Latitude": random.uniform(-90, 90),
            "Longitude": random.uniform(-180, 180),
            "Threat Type": random.choice(["Missile Launch", "Cyber-Attack", "Drone Infiltration"]),
            "Severity": random.choice(["Low", "Medium", "High"])
        })
    return pd.DataFrame(threats)

# ---------------- PDF EXPORT ----------------
def export_pdf(df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Global Threat Detection Report", ln=True, align="C")
    pdf.ln(5)

    pdf.set_font("Arial", size=10)
    for _, r in df.iterrows():
        pdf.multi_cell(
            0, 8,
            f"Threat: {r['Threat Type']}\n"
            f"Location: ({r['Latitude']:.2f}, {r['Longitude']:.2f})\n"
            f"Severity: {r['Severity']}\n"
        )
        pdf.ln(2)

    path = "/tmp/threat_report.pdf"
    pdf.output(path)
    return path

# ---------------- SESSION STATE ----------------
if "data" not in st.session_state:
    st.session_state.data = None

# ---------------- CONTROLS ----------------
col1, col2, col3 = st.columns([2,2,1])

with col1:
    record_count = st.slider(
        "Generate Sample Threat Records",
        5, 200, 20
    )

with col2:
    run_analysis = st.button("🚀 Run Analysis")

with col3:
    reset = st.button("🔴 RESET", key="reset")

# ---------------- RESET ----------------
if reset:
    st.session_state.data = None
    st.experimental_rerun()

# ---------------- RUN ANALYSIS ----------------
if run_analysis:
    st.session_state.data = generate_sample_data(record_count)

# ---------------- DISPLAY RESULTS ----------------
if st.session_state.data is not None:
    df = st.session_state.data

    st.subheader("📋 Threat Data")
    st.dataframe(df)

    st.subheader("🌍 Global Threat Map")
    st.map(df.rename(columns={"Latitude": "lat", "Longitude": "lon"}))

    colA, colB = st.columns(2)

    with colA:
        st.subheader("Threat Type Distribution")
        st.bar_chart(df["Threat Type"].value_counts())

    with colB:
        st.subheader("Severity Breakdown")
        st.bar_chart(df["Severity"].value_counts())

    st.markdown("---")

    colX, colY = st.columns(2)

    with colX:
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Export CSV",
            csv,
            file_name="global_threats.csv",
            mime="text/csv"
        )

    with colY:
        pdf_path = export_pdf(df)
        with open(pdf_path, "rb") as f:
            st.download_button(
                "⬇️ Export PDF",
                f,
                file_name="global_threat_report.pdf",
                mime="application/pdf"
            )
