

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
.big-title {
    font-size:48px;
    font-weight:800;
    color:#0B5ED7;
    text-align:center;
}
.subtitle {
    text-align:center;
    font-size:18px;
}
.reset-btn button {
    background-color:red !important;
    color:white !important;
    font-weight:bold;
}
.layer-iam button { background:#0d6efd; color:white; }
.layer-fw button { background:#198754; color:white; }
.layer-edr button { background:#6f42c1; color:white; }
.layer-ids button { background:#dc3545; color:white; }
.layer-siem button { background:#fd7e14; color:white; }
.layer-cloud button { background:#20c997; color:white; }
.layer-dlp button { background:#6610f2; color:white; }
.layer-ir button { background:#0dcaf0; color:black; }
.layer-awareness button { background:#adb5bd; color:black; }
</style>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------
st.markdown('<div class="big-title">Defense-in-Depth Cybersecurity Strategy Demo</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Developed by <b>Randy Singh</b> | Kalsnet (KNet) Consulting Group</div><hr>',
    unsafe_allow_html=True
)

# -------------------------------
# SESSION STATE
# -------------------------------
if "df" not in st.session_state:
    st.session_state.df = None

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.header(" Control Panel")

dashboard_mode = st.sidebar.radio(
    "Dashboard Mode",
    ["Technical / SOC View", "Executive / DoD View"]
)

data_mode = st.sidebar.radio(
    "Data Source",
    ["Generate Synthetic Data", "Upload My Own Data"]
)

# -------------------------------
# RESET BUTTON (FIXED)
# -------------------------------
with st.sidebar.container():
    st.markdown('<div class="reset-btn">', unsafe_allow_html=True)
    if st.button(" RESET & REGENERATE DATA"):
        st.session_state.clear()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# DATA GENERATION
# -------------------------------
if data_mode == "Generate Synthetic Data":
    records = st.sidebar.slider("Number of Records", 10, 200, 50)

    st.session_state.df = pd.DataFrame({
        "User": [f"user{i}" for i in range(records)],
        "Login_Attempts": np.random.randint(1, 20, records),
        "Firewall_Blocks": np.random.randint(0, 25, records),
        "Threat_Level": np.random.choice(["Low", "Medium", "High"], records),
        "Cloud_Activity": np.random.choice(["Normal", "Suspicious"], records),
        "DLP_Alerts": np.random.randint(0, 12, records)
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
# EXECUTIVE / DOD DASHBOARD
# -------------------------------
if df is not None and dashboard_mode == "Executive / DoD View":

    st.markdown("##  Executive Cyber Posture Overview")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Users", len(df))
    c2.metric("High Risk Users", len(df[df["Risk_Category"] == "High"]))
    c3.metric("Critical Threats", len(df[df["Risk_Category"] == "Critical"]))
    c4.metric("Suspicious Cloud Events", len(df[df["Cloud_Activity"] == "Suspicious"]))

    fig, ax = plt.subplots()
    df["Risk_Category"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    ax.set_title("Mission Risk Distribution")
    st.pyplot(fig)

# -------------------------------
# TECHNICAL / SOC VIEW
# -------------------------------
elif df is not None:

    st.subheader(" Active Security Dataset")
    st.dataframe(df)

# -------------------------------
# DEFENSE-IN-DEPTH SECURITY LAYERS (RESTORED)
# -------------------------------
if df is not None:
    st.markdown("##  Defense-in-Depth Security Layers")

    layers = [
        (" IAM (Identity & Access Management)", "layer-iam"),
        (" Firewalls", "layer-fw"),
        (" EDR & NDR", "layer-edr"),
        (" IDS / IPS", "layer-ids"),
        (" SIEM", "layer-siem"),
        (" Cloud Security", "layer-cloud"),
        (" DLP (Data Loss Prevention)", "layer-dlp"),
        (" Incident Response", "layer-ir"),
        (" Security Awareness", "layer-awareness")
    ]

    cols = st.columns(3)
    selected_layer = None

    for i, (layer, css) in enumerate(layers):
        with cols[i % 3]:
            st.markdown(f'<div class="{css}">', unsafe_allow_html=True)
            if st.button(layer, use_container_width=True):
                selected_layer = layer
            st.markdown('</div>', unsafe_allow_html=True)

    if selected_layer:
        st.markdown(f"###  Selected Layer: {selected_layer}")

        if "IAM" in selected_layer:
            st.success("IAM: Analyzing authentication abuse")
            st.write(df.sort_values("Login_Attempts", ascending=False))

        elif "Firewalls" in selected_layer:
            st.warning("Firewall: Reviewing blocked traffic")
            st.write(df.sort_values("Firewall_Blocks", ascending=False))

        elif "EDR" in selected_layer:
            st.info("EDR/NDR: Endpoint behavior monitoring")
            st.write(df.sample(5))

        elif "IDS" in selected_layer:
            st.error("IDS/IPS: High-confidence intrusion alerts")
            st.write(df[df["Threat_Level"] == "High"])

        elif "SIEM" in selected_layer:
            st.info("SIEM: Event correlation")
            st.write(df.groupby("Threat_Level").count())

        elif "Cloud" in selected_layer:
            st.warning("Cloud Security: Suspicious workloads")
            st.write(df[df["Cloud_Activity"] == "Suspicious"])

        elif "DLP" in selected_layer:
            st.error("DLP: Data exfiltration risk")
            st.write(df[df["DLP_Alerts"] > 5])

        elif "Incident" in selected_layer:
            st.success("Incident Response Activated")
            st.write("Identify → Contain → Eradicate → Recover → Lessons Learned")

        elif "Awareness" in selected_layer:
            st.info("Security Awareness Program")
            st.write("Continuous training reduces human-based risk")

# -------------------------------
# MITRE ATT&CK
# -------------------------------
if df is not None:
    st.markdown("##  MITRE ATT&CK Mapping")

    mitre = pd.DataFrame({
        "Indicator": [
            "Brute-force logins",
            "Suspicious cloud traffic",
            "Firewall exploit attempts",
            "Data exfiltration alerts"
        ],
        "Tactic": [
            "Credential Access",
            "Command & Control",
            "Initial Access",
            "Exfiltration"
        ],
        "Technique": [
            "T1110 – Brute Force",
            "T1071 – App Layer Protocol",
            "T1190 – Exploit Public-Facing App",
            "T1041 – Exfiltration Over C2"
        ]
    })

    st.dataframe(mitre)

# -------------------------------
# EXPORT
# -------------------------------
st.markdown("---")
if df is not None:
    st.download_button(
        "⬇ Download Full CSV",
        df.to_csv(index=False),
        "cyber_defense_output.csv",
        "text/csv"
    )

