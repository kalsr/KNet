

# =========================================================
# AEGIS-6X | 6G AI/ML Threat Intelligence Platform
# Designed & Developed by Randy Singh – KNet Consulting
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import json
from datetime import datetime
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import pairwise_distances
import plotly.express as px
from fpdf import FPDF

# ---------------- PAGE CONFIG ----------------
st.set_page_config(layout="wide", page_title="AEGIS-6X | DISA 6G AI Platform")

# ---------------- STYLES ----------------
st.markdown("""
<style>
.header {
    background: linear-gradient(90deg,#002868,#005ea2);
    padding:20px;
    border-radius:12px;
    color:white;
    text-align:center;
}
.stButton button {
    font-size:16px;
    font-weight:700;
    padding:10px 26px;
    border-radius:6px;
    background-color:#005ea2;
    color:white;
}
.reset-btn button {
    background-color:#dc3545 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header">
<h2>AEGIS-6X | 6G AI/ML Threat Intelligence Platform</h2>
<p>DISA / JADC2 / NATO-Aligned | Randy Singh – KNet Consulting</p>
</div>
""", unsafe_allow_html=True)

# ---------------- RBAC ----------------
ROLES = ["Analyst", "Commander", "Admin"]

if "role" not in st.session_state:
    st.session_state.role = None

if st.session_state.role is None:
    role = st.selectbox("Select Role", ROLES)
    if st.button("Login"):
        st.session_state.role = role
        st.rerun()
    st.stop()

# ---------------- LOGOUT ----------------
with st.sidebar:
    st.markdown(f"### Role: {st.session_state.role}")
    if st.button("🔄 Logout / Switch Role"):
        st.session_state.clear()
        st.rerun()

# ---------------- DATA GENERATOR ----------------
def generate_data(n):
    df = pd.DataFrame({
        "Latitude": np.random.uniform(-60, 75, n),
        "Longitude": np.random.uniform(-180, 180, n),
        "Country": np.random.choice(["US","CN","RU","IR","IN","KP"], n),
        "Threat": np.random.choice(["Cyber","Drone","SIGINT","Missile"], n),
        "Edge_Risk": np.random.randint(10,70,n),
        "Core_Risk": np.random.randint(20,95,n),
        "Timestamp": datetime.utcnow()
    })
    return df

if "data" not in st.session_state:
    st.session_state.data = generate_data(50)

# ---------------- CONTROLS ----------------
c1, c2, c3, c4 = st.columns([2,2,2,2])

with c1:
    n = st.slider("Threat Events", 10, 500, 50)

with c2:
    if st.button("Generate Sample Data"):
        st.session_state.data = generate_data(n)

with c3:
    upload = st.file_uploader("Upload CSV", type=["csv"])
    if upload:
        st.session_state.data = pd.read_csv(upload)

with c4:
    st.markdown('<div class="reset-btn">', unsafe_allow_html=True)
    if st.button("RESET DATA"):
        st.session_state.data = generate_data(50)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- ML PIPELINE ----------------
scaler = StandardScaler()
X = scaler.fit_transform(st.session_state.data[["Edge_Risk","Core_Risk"]])

model = IsolationForest(contamination=0.15, random_state=42)
st.session_state.data["anomaly"] = model.fit_predict(X)
st.session_state.data["risk_score"] = -model.decision_function(X)
st.session_state.data["confidence"] = np.clip(
    1 - (st.session_state.data["risk_score"] / st.session_state.data["risk_score"].max()),
    0.1, 0.99
)

# ✅ FIX: create proper color column
st.session_state.data["Risk_Label"] = st.session_state.data["anomaly"].map(
    {-1: "High Risk", 1: "Normal"}
)

# ---------------- DASHBOARD ----------------
st.subheader("📊 Threat Intelligence Dashboard")
st.dataframe(st.session_state.data, use_container_width=True)

fig = px.scatter(
    st.session_state.data,
    x="Edge_Risk",
    y="Core_Risk",
    color="Risk_Label",
    size="risk_score",
    hover_name="Country",
    hover_data=["Threat","confidence"],
    title="Edge vs Core Risk (Anomaly Detection)"
)
st.plotly_chart(fig, use_container_width=True)

# ---------------- MAP ----------------
st.subheader("🌍 Global Threat Map (Satellite View)")

map_fig = px.scatter_geo(
    st.session_state.data,
    lat="Latitude",
    lon="Longitude",
    color="Risk_Label",
    size="risk_score",
    hover_name="Country",
    projection="natural earth"
)

map_fig.update_layout(height=700)
st.plotly_chart(map_fig, use_container_width=True)

# ---------------- ANALYTICS ----------------
c1, c2, c3 = st.columns(3)
c1.metric("High-Risk Events", (st.session_state.data["anomaly"]==-1).sum())
c2.metric("Avg Confidence", f"{st.session_state.data['confidence'].mean():.2f}")
c3.metric("Total Events", len(st.session_state.data))

pie = st.session_state.data["Risk_Label"].value_counts()
st.plotly_chart(px.pie(
    values=pie.values,
    names=pie.index,
    title="Risk Distribution"
), use_container_width=True)

# ---------------- EXPORT ----------------
st.subheader("📤 Export Intelligence")

csv = st.session_state.data.to_csv(index=False).encode()
st.download_button("Download CSV", csv, "threat_data.csv")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=10)
pdf.cell(0,10,"AEGIS-6X Threat Intelligence Report", ln=True)
for _, r in st.session_state.data.iterrows():
    pdf.multi_cell(
        0,8,
        f"{r['Country']} | {r['Threat']} | {r['Risk_Label']} | Confidence {r['confidence']:.2f}"
    )
pdf_bytes = pdf.output(dest="S").encode("latin1")
st.download_button("Download PDF", pdf_bytes, "AEGIS_Report.pdf")
