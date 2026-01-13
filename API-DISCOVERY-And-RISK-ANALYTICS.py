# ============================================================
# API Simulation & Security Analytics Platform
# Developed by Randy Singh
# Kalsnet (KNet) Consulting Group
# ============================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
import tempfile
import random
import uuid

# ------------------------------------------------------------
# Page Config
# ------------------------------------------------------------
st.set_page_config(page_title="API Security Analytics", layout="wide")

# ------------------------------------------------------------
# Custom CSS
# ------------------------------------------------------------
st.markdown("""
<style>
.title-bar {
    font-size: 40px;
    font-weight: 800;
    color: #0B5ED7;
}
.subtitle {
    font-size: 16px;
    font-weight: 600;
    color: #333;
    border-bottom: 2px solid #0B5ED7;
    padding-bottom: 8px;
}
.reset-btn button {
    background-color: #DC3545 !important;
    color: white !important;
    font-weight: bold;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# Title
# ------------------------------------------------------------
st.markdown('<div class="title-bar">🔐 API Simulation & Risk Analytics Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Developed by Randy Singh — Kalsnet (KNet) Consulting Group</div>', unsafe_allow_html=True)

st.divider()

# ------------------------------------------------------------
# Session State
# ------------------------------------------------------------
if "df" not in st.session_state:
    st.session_state.df = None
if "mode" not in st.session_state:
    st.session_state.mode = None
if "data_version" not in st.session_state:
    st.session_state.data_version = uuid.uuid4().hex
if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = uuid.uuid4().hex

# ------------------------------------------------------------
# Sidebar Controls
# ------------------------------------------------------------
st.sidebar.header("⚙️ Data Controls")

record_count = st.sidebar.slider(
    "Generate Synthetic API Records",
    0, 100, step=10, value=0
)

uploaded_file = st.sidebar.file_uploader(
    "Upload API Log File (.txt)",
    type=["txt"],
    key=st.session_state.uploader_key
)

with st.sidebar.container():
    st.markdown('<div class="reset-btn">', unsafe_allow_html=True)
    if st.button("RESET APPLICATION"):
        st.session_state.df = None
        st.session_state.mode = None
        st.session_state.data_version = uuid.uuid4().hex
        st.session_state.uploader_key = uuid.uuid4().hex
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------------------
# Synthetic Data Generator
# ------------------------------------------------------------
def generate_synthetic_data(n, seed):
    random.seed(seed)
    endpoints = [
        "/api/login", "/api/logout", "/api/data", "/api/user",
        "/api/admin", "/api/delete", "/api/update", "/api/search",
        "/api/report", "/api/unknown"
    ]
    statuses = ["200", "401", "403", "404", "500"]

    anomaly_ratio = random.choice([0, 0.2, 0.4, 0.6])
    records = []

    for _ in range(n):
        endpoint = random.choice(endpoints)
        if random.random() < anomaly_ratio:
            status = random.choice(statuses[1:])
        else:
            status = "200"

        records.append({
            "Request": f"GET {endpoint}",
            "Endpoint": endpoint,
            "Status": status
        })

    return pd.DataFrame(records)

# ------------------------------------------------------------
# Load Uploaded Logs + API Discovery
# ------------------------------------------------------------
def load_uploaded_logs(file):
    rows = []
    discovered_apis = set()

    for line in file:
        line = line.decode("utf-8").strip()
        if "|" not in line:
            continue

        req, res = line.split("|", 1)
        status = res.strip().split()[0]

        endpoint = req.strip().split(" ", 1)[1]
        discovered_apis.add(endpoint)

        rows.append({
            "Request": req.strip(),
            "Endpoint": endpoint,
            "Status": status
        })

    df = pd.DataFrame(rows)
    return df, sorted(discovered_apis)

# ------------------------------------------------------------
# Anomaly & Risk Detection
# ------------------------------------------------------------
def detect_risks(df):
    risks = []

    if (df["Status"] == "404").sum() > 5:
        risks.append("🔍 API Enumeration detected (multiple 404s). Use WAF and disable unused endpoints.")

    if df["Endpoint"].str.contains("admin").sum() > 0:
        risks.append("🔐 Admin endpoint exposure. Restrict by IP, role-based access.")

    if (df["Status"] == "401").sum() > 3:
        risks.append("⚠️ Brute-force authentication attempts. Enable MFA and rate limiting.")

    if (df["Status"] == "500").sum() > 2:
        risks.append("🔥 Backend instability detected. Improve exception handling and monitoring.")

    return risks

# ------------------------------------------------------------
# Data Selection Logic
# ------------------------------------------------------------
discovered_apis = None

if uploaded_file:
    st.session_state.df, discovered_apis = load_uploaded_logs(uploaded_file)
    st.session_state.mode = "uploaded"

elif record_count > 0:
    st.session_state.df = generate_synthetic_data(
        record_count,
        st.session_state.data_version
    )
    st.session_state.mode = "synthetic"

# ------------------------------------------------------------
# Display Section
# ------------------------------------------------------------
if st.session_state.df is None:
    st.info("Use the slider to generate synthetic data or upload a log file for API discovery.")
else:
    df = st.session_state.df

    st.subheader("📄 API Records")
    st.dataframe(df, use_container_width=True)

    if discovered_apis:
        st.subheader("🧭 Discovered APIs from Uploaded Logs")
        st.write(", ".join(discovered_apis))

    st.subheader("📊 API Status Analytics")
    status_counts = df["Status"].value_counts()

    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots()
        status_counts.plot(kind="bar", ax=ax1)
        st.pyplot(fig1)

    with col2:
        fig2, ax2 = plt.subplots()
        ax2.pie(status_counts, labels=status_counts.index, autopct="%1.1f%%")
        ax2.axis("equal")
        st.pyplot(fig2)

    st.subheader("🚨 Risk & Vulnerability Analysis")
    findings = detect_risks(df)

    if findings:
        for f in findings:
            st.warning(f)
    else:
        st.success("✅ No major risks detected.")

st.divider()
st.caption("© Kalsnet (KNet) Consulting Group — API Security & Simulation Platform")
