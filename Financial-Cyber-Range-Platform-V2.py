# Financial-Cyber-Range-Platform-V2.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
import random

# -----------------------------
# TITLE (BOLD BLUE ENHANCED)
# -----------------------------
st.markdown(
    "<h1 style='color:#0033cc; text-align:center; font-weight:900; font-size:40px;'>"
    "AI-Powered Financial Cyber Range Platform - Developed by Randy Singh Kalsnet (KNet) Consulting Group.<br>"
    "Red Team | Blue Team | SOC | Threat Hunting | AI Detection"
    "</h1>",
    unsafe_allow_html=True
)

# -----------------------------
# SESSION STATE
# -----------------------------
if "data" not in st.session_state:
    st.session_state.data = None

if "attack_log" not in st.session_state:
    st.session_state.attack_log = []

if "alerts" not in st.session_state:
    st.session_state.alerts = []

# -----------------------------
# DATA GENERATION
# -----------------------------
def generate_data(n):
    df = pd.DataFrame({
        "Account_ID": range(1, n+1),
        "Balance": np.random.randint(1000, 50000, n),
        "Transactions": np.random.randint(1, 50, n),
        "Status": ["Normal"] * n
    })
    return df

# -----------------------------
# 🔴 RED TEAM (ATTACK ENGINE)
# -----------------------------
def red_team_attack(df):
    attacked = df.copy()
    log = []

    indices = np.random.choice(df.index, size=max(1, int(len(df)*0.3)), replace=False)

    for i in indices:
        orig = attacked.loc[i, "Balance"]
        loss_factor = random.uniform(0.3, 0.7)
        new = int(orig * loss_factor)
        loss = orig - new

        attacked.loc[i, "Balance"] = new
        attacked.loc[i, "Status"] = "Compromised"

        log.append({
            "Account_ID": int(attacked.loc[i, "Account_ID"]),
            "Loss": loss,
            "Attack_Type": random.choice([
                "Phishing", "Malware", "API Breach", "Insider Threat"
            ])
        })

    return attacked, log

# -----------------------------
# 🔵 BLUE TEAM (DEFENSE ENGINE)
# -----------------------------
def blue_team_defense(df):
    secured = df.copy()

    # Detect compromised accounts
    compromised_accounts = secured["Status"] == "Compromised"

    # Simulate mitigation actions
    secured.loc[compromised_accounts, "Status"] = "Recovered"

    # Financial recovery simulation
    secured.loc[compromised_accounts, "Balance"] *= 1.15

    return secured

# -----------------------------
#  AI FRAUD DETECTION
# -----------------------------
def ai_fraud_detection(df):
    alerts = []

    for _, row in df.iterrows():
        if row["Transactions"] > 40 or row["Balance"] < 2000:
            alerts.append({
                "Account_ID": row["Account_ID"],
                "Risk": "High",
                "Reason": "Unusual Transactions or Low Balance"
            })

    return alerts

# -----------------------------
#  THREAT HUNTING
# -----------------------------
def threat_hunting(df):
    suspicious = df[df["Transactions"] > 30]
    return suspicious

# -----------------------------
#  SOC DASHBOARD
# -----------------------------
def soc_dashboard(alerts):
    if alerts:
        st.error(" SOC ALERTS DETECTED")
        st.dataframe(pd.DataFrame(alerts))
    else:
        st.success(" No Threats Detected")

# -----------------------------
# UI CONTROLS
# -----------------------------
st.sidebar.header(" Controls")

num_records = st.sidebar.slider("Select Data Size", 10, 200, 50)

if st.sidebar.button("Generate Data"):
    st.session_state.data = generate_data(num_records)
    st.session_state.attack_log = []
    st.session_state.alerts = []

if st.sidebar.button("Reset Data"):
    st.session_state.data = generate_data(num_records)
    st.session_state.attack_log = []
    st.session_state.alerts = []

# -----------------------------
# MAIN DISPLAY
# -----------------------------
if st.session_state.data is not None:

    st.subheader(" Financial Dataset")
    st.dataframe(st.session_state.data)

    colA, colB, colC, colD = st.columns(4)

    # 🔴 RED TEAM BUTTON
    if colA.button("🔴 Red Team Attack"):
        attacked, log = red_team_attack(st.session_state.data)
        st.session_state.data = attacked
        st.session_state.attack_log = log

    # 🔵 BLUE TEAM BUTTON
    if colB.button("🔵 Blue Team Defense"):
        st.session_state.data = blue_team_defense(st.session_state.data)

    #  AI DETECTION
    if colC.button(" AI Fraud Detection"):
        st.session_state.alerts = ai_fraud_detection(st.session_state.data)

    #  THREAT HUNTING
    if colD.button(" Threat Hunting"):
        suspicious = threat_hunting(st.session_state.data)
        st.subheader("Suspicious Accounts Identified")
        st.dataframe(suspicious)

    # -----------------------------
    # METRICS
    # -----------------------------
    total_balance = st.session_state.data["Balance"].sum()
    compromised = (st.session_state.data["Status"] == "Compromised").sum()

    total_loss = sum([x["Loss"] for x in st.session_state.attack_log]) if st.session_state.attack_log else 0

    col1, col2, col3 = st.columns(3)
    col1.metric(" Total Balance", f"${total_balance:,.0f}")
    col2.metric(" Compromised Accounts", compromised)
    col3.metric(" Total Loss", f"${total_loss:,.0f}")

    # -----------------------------
    # SOC DASHBOARD
    # -----------------------------
    st.subheader(" SOC Analyst Dashboard")
    soc_dashboard(st.session_state.alerts)

    # -----------------------------
    # GRAPH
    # -----------------------------
    st.subheader(" Attack Impact Visualization")

    fig, ax = plt.subplots()
    status_counts = st.session_state.data["Status"].value_counts()
    ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%')
    st.pyplot(fig)

    # -----------------------------
    # ATTACK LOG
    # -----------------------------
    if st.session_state.attack_log:
        st.subheader(" Attack Details")
        st.dataframe(pd.DataFrame(st.session_state.attack_log))

    # -----------------------------
    # COUNTER ATTACK EXPLANATION
    # -----------------------------
    st.subheader(" How Counter Attack Works")

    st.write("""
    The Blue Team Counter Attack - simulates real-world incident response and cyber defense operations. 
    Once an attack is detected, the system identifies all compromised accounts and immediately applies containment and remediation strategies. 
    These include isolating affected accounts, stopping further unauthorized transactions, and marking them as -Recovered-. 
    Financial recovery is simulated by partially restoring lost funds, representing fraud reimbursement, insurance claims, or rollback mechanisms. 
    In real-world environments, this process would involve Security Operations Center (SOC) monitoring, automated response systems (SOAR), 
    endpoint isolation, credential resets, and deployment of patches or security controls. 
    The goal of the counter attack is to -minimize financial damage, restore system integrity, and prevent future breaches- 
    by strengthening defenses such as Multi-Factor Authentication, Anomaly Detection, and Continuous Monitoring.
    """)
