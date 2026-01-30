

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from fpdf import FPDF

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Defense-in-Depth Cybersecurity Demo",
    layout="wide"
)

# -------------------------------
# CUSTOM CSS
# -------------------------------
st.markdown("""
<style>
.big-title { font-size:48px; font-weight:800; color:#0B5ED7; text-align:center; }
.subtitle { text-align:center; font-size:18px; }
.kpi { font-size:32px; font-weight:700; }
.reset-btn button { background:red!important; color:white!important; font-weight:bold; }
</style>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------
st.markdown('<div class="big-title">Defense-in-Depth Cybersecurity Strategy Demo</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Developed by <b>Randy Singh</b> | Kalsnet (KNet) Consulting Group</div><hr>', unsafe_allow_html=True)

# -------------------------------
# SESSION STATE
# -------------------------------
if "df" not in st.session_state:
    st.session_state.df = None

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.header("⚙ Control Panel")

dashboard_mode = st.sidebar.radio(
    "Dashboard Mode",
    ["Technical / SOC View", "Executive / DoD View"]
)

data_mode = st.sidebar.radio(
    "Data Source",
    ["Generate Synthetic Data", "Upload My Own Data"]
)

with st.sidebar.container():
    st.markdown('<div class="reset-btn">', unsafe_allow_html=True)
    if st.button("🔴 RESET & REGENERATE"):
        st.session_state.df = None
        st.experimental_rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# DATA GENERATION
# -------------------------------
if data_mode == "Generate Synthetic Data":
    count = st.sidebar.slider("Number of Records", 10, 200, 50)

    st.session_state.df = pd.DataFrame({
        "User": [f"user{i}" for i in range(count)],
        "Login_Attempts": np.random.randint(1, 20, count),
        "Firewall_Blocks": np.random.randint(0, 25, count),
        "Threat_Level": np.random.choice(["Low", "Medium", "High"], count),
        "Cloud_Activity": np.random.choice(["Normal", "Suspicious"], count),
        "DLP_Alerts": np.random.randint(0, 12, count)
    })

else:
    upload = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    if upload:
        st.session_state.df = pd.read_csv(upload)

df = st.session_state.df

# -------------------------------
# RISK SCORE ENGINE
# -------------------------------
def calculate_risk(row):
    score = (
        row["Login_Attempts"] * 2 +
        row["Firewall_Blocks"] * 1.5 +
        row["DLP_Alerts"] * 3
    )

    if row["Threat_Level"] == "High":
        score += 25
    elif row["Threat_Level"] == "Medium":
        score += 10

    if row["Cloud_Activity"] == "Suspicious":
        score += 20

    return score

if df is not None:
    df["Risk_Score"] = df.apply(calculate_risk, axis=1)

    df["Risk_Category"] = pd.cut(
        df["Risk_Score"],
        bins=[0, 30, 60, 90, 999],
        labels=["Low", "Medium", "High", "Critical"]
    )

# -------------------------------
# EXECUTIVE DASHBOARD
# -------------------------------
if df is not None and dashboard_mode == "Executive / DoD View":

    st.markdown("## 🛡 Executive Cyber Posture Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Users", len(df))
    c2.metric("High Risk Users", len(df[df["Risk_Category"] == "High"]))
    c3.metric("Critical Threats", len(df[df["Risk_Category"] == "Critical"]))
    c4.metric("Suspicious Cloud Events", len(df[df["Cloud_Activity"] == "Suspicious"]))

    st.markdown("### 🎯 Mission Risk Distribution")
    fig, ax = plt.subplots()
    df["Risk_Category"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    st.pyplot(fig)

    st.markdown("### 🔝 Top Critical Entities")
    st.dataframe(df.sort_values("Risk_Score", ascending=False).head(10))

# -------------------------------
# TECHNICAL VIEW
# -------------------------------
elif df is not None:

    st.subheader("📋 Active Security Dataset")
    st.dataframe(df)

    st.markdown("## 📊 Threat & Cloud Visibility")

    c1, c2 = st.columns(2)

    with c1:
        fig, ax = plt.subplots()
        df["Threat_Level"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
        ax.set_title("Threat Levels")
        ax.set_ylabel("")
        st.pyplot(fig)

    with c2:
        fig, ax = plt.subplots()
        df["Cloud_Activity"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
        ax.set_title("Cloud Activity")
        ax.set_ylabel("")
        st.pyplot(fig)

# -------------------------------
# MITRE ATT&CK MAPPING
# -------------------------------
if df is not None:
    st.markdown("## 🧩 MITRE ATT&CK Technique Mapping")

    mitre_map = pd.DataFrame({
        "Observed Indicator": [
            "Excessive Login Attempts",
            "Suspicious Cloud Activity",
            "High Firewall Blocks",
            "High DLP Alerts"
        ],
        "MITRE Tactic": [
            "Credential Access",
            "Command & Control",
            "Initial Access",
            "Exfiltration"
        ],
        "Technique ID": [
            "T1110 – Brute Force",
            "T1071 – Application Layer Protocol",
            "T1190 – Exploit Public-Facing App",
            "T1041 – Exfiltration Over C2 Channel"
        ]
    })

    st.dataframe(mitre_map)

# -------------------------------
# EXPORT
# -------------------------------
st.markdown("---")
st.markdown("## 📤 Export Intelligence")

if df is not None:
    st.download_button(
        "⬇ Download CSV",
        df.to_csv(index=False),
        "cyber_defense_full_output.csv",
        "text/csv"
    )
else:
    st.info("Generate or upload data to enable exports.")
