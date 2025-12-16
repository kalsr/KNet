
# Advanced Enterprise Global Intelligence System
# =========================================================
# AEGIS-6X | 6G AI/ML Threat Intelligence Platform
# Designed & Developed by Randy Singh Computer Scientist.
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import plotly.express as px
from fpdf import FPDF

# ---------------- PAGE CONFIG ----------------
st.set_page_config(layout="wide", page_title="AEGIS-6X | 6G AI Platform")

# ---------------- STYLES ----------------
st.markdown("""
<style>
.header {
    background: linear-gradient(90deg,#002868,#005ea2);
    padding:22px;
    border-radius:12px;
    color:white;
    text-align:center;
}
.stButton button {
    font-size:16px;
    font-weight:700;
    padding:10px 28px;
    border-radius:6px;
    background-color:#005ea2;
    color:white;
}
.reset button {
    background-color:#dc3545 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header">
<h2>AEGIS-6X | 6G AI/ML Threat Intelligence Platform</h2>
<p>DISA / NATO-Aligned | Randy Singh – Computer Scientist</p>
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
        st.session_state.data = None
        st.rerun()
    st.stop()

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
        "Country": np.random.choice(
            ["United States","China","Russia","Iran","India","North Korea"], n
        ),
        "Threat": np.random.choice(
            ["Cyber","Drone","SIGINT","Missile"], n
        ),
        "Edge_Risk": np.random.randint(10,70,n),
        "Core_Risk": np.random.randint(20,95,n),
        "Timestamp": datetime.utcnow()
    })
    return df

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
    st.markdown('<div class="reset">', unsafe_allow_html=True)
    if st.button("RESET DATA"):
        st.session_state.data = generate_data(n)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- ENSURE DATA ----------------
if st.session_state.data is None or st.session_state.data.empty:
    st.info("No data loaded yet.")
    st.stop()

df = st.session_state.data.copy()

# ---------------- ML PIPELINE ----------------
scaler = StandardScaler()
X = scaler.fit_transform(df[["Edge_Risk","Core_Risk"]])

model = IsolationForest(contamination=0.15, random_state=42)
df["anomaly"] = model.fit_predict(X)

df["risk_score"] = (-model.decision_function(X)).clip(0.01)
df["confidence"] = np.clip(
    1 - (df["risk_score"] / df["risk_score"].max()),
    0.1, 0.99
)

df["Risk_Label"] = df["anomaly"].map({-1:"High Risk",1:"Normal"}).astype(str)

#  CRITICAL: Remove bad rows
df = df.dropna(subset=["risk_score","Risk_Label"])

st.session_state.data = df

# ---------------- DASHBOARD ----------------
st.subheader(" THREAT INTELLIGENCE DASHBOARD")
st.dataframe(df, use_container_width=True)

fig = px.scatter(
    df,
    x="Edge_Risk",
    y="Core_Risk",
    color="Risk_Label",
    size="risk_score",
    hover_name="Country",
    hover_data=["Threat","confidence"],
    title="Edge vs Core Risk (AI Anomaly Detection)",
    size_max=40
)
st.plotly_chart(fig, use_container_width=True)

# ---------------- MAP ----------------
st.subheader(" Global Threat Map (Satellite View)")

map_fig = px.scatter_geo(
    df,
    lat="Latitude",
    lon="Longitude",
    color="Risk_Label",
    size="risk_score",
    hover_name="Country",
    hover_data=["Threat","confidence"],
    projection="natural earth",
    title="Global Threat Overlay"
)
map_fig.update_layout(height=700)
st.plotly_chart(map_fig, use_container_width=True)

# ---------------- ANALYTICS ----------------
c1, c2, c3 = st.columns(3)
c1.metric("High-Risk Events", int((df["anomaly"]==-1).sum()))
c2.metric("Avg Confidence", f"{df['confidence'].mean():.2f}")
c3.metric("Total Events", len(df))

pie = df["Risk_Label"].value_counts()
st.plotly_chart(
    px.pie(values=pie.values, names=pie.index, title="Risk Distribution"),
    use_container_width=True
)

# ---------------- EXPORT ----------------
st.subheader("📤 Export Intelligence")

csv = df.to_csv(index=False).encode()
st.download_button("Download CSV", csv, "threat_data.csv")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=10)
pdf.cell(0,10,"AEGIS-6X Threat Intelligence Report", ln=True)
for _, r in df.iterrows():
    pdf.multi_cell(
        0,8,
        f"{r['Country']} | {r['Threat']} | {r['Risk_Label']} | Confidence {r['confidence']:.2f}"
    )
pdf_bytes = pdf.output(dest="S").encode("latin1")
st.download_button("Download PDF", pdf_bytes, "AEGIS_Report.pdf")


