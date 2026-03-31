

# Finacial-Cyber-Attack-Simulator-V1.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
import json
import random

# -----------------------------
# TITLE
# -----------------------------
st.markdown(
    "<h1 style='color:blue; text-align:center;'>"
    "Financial Cyber Attack Simulator<br>"
    "Developed by Randy Singh (Kalsnet - KNet Consulting Group)"
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

# -----------------------------
# SYNTHETIC DATA GENERATOR
# -----------------------------
def generate_data(n):
    data = pd.DataFrame({
        "Account_ID": range(1, n + 1),
        "Balance": np.random.randint(1000, 50000, n),
        "Transactions": np.random.randint(1, 50, n),
        "Status": ["Normal"] * n
    })
    return data

# -----------------------------
# ATTACK SIMULATION (ENHANCED)
# -----------------------------
def launch_attack(df):
    attacked = df.copy()
    attack_details = []

    if len(df) == 0:
        return attacked, attack_details

    indices = np.random.choice(df.index, size=max(1, int(len(df) * 0.3)), replace=False)

    for i in indices:
        original_balance = attacked.loc[i, "Balance"]
        loss_factor = random.uniform(0.2, 0.6)
        new_balance = int(original_balance * loss_factor)
        loss_amount = original_balance - new_balance

        attacked.loc[i, "Balance"] = new_balance
        attacked.loc[i, "Status"] = "Compromised"

        attack_details.append({
            "Account_ID": int(attacked.loc[i, "Account_ID"]),
            "Original_Balance": int(original_balance),
            "Compromised_Balance": int(new_balance),
            "Amount_Compromised": int(loss_amount),
            "Attack_Vector": random.choice([
                "Phishing Attack",
                "Credential Stuffing",
                "Malware Injection",
                "Insider Threat",
                "API Exploit"
            ])
        })

    return attacked, attack_details

# -----------------------------
# COUNTERMEASURE
# -----------------------------
def counter_attack(df):
    secured = df.copy()

    secured.loc[secured["Status"] == "Compromised", "Status"] = "Recovered"
    secured["Balance"] = secured["Balance"] * 1.1  # partial recovery

    return secured

# -----------------------------
# EXPORT FUNCTIONS
# -----------------------------
def export_pdf(df, attack_log):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    pdf.cell(200, 10, txt="Financial Cyber Attack Report", ln=True)

    pdf.cell(200, 10, txt="--- Dataset ---", ln=True)
    for _, row in df.iterrows():
        pdf.cell(200, 8, txt=str(row.to_dict()), ln=True)

    if attack_log:
        pdf.cell(200, 10, txt="--- Compromised Accounts ---", ln=True)
        for item in attack_log:
            pdf.cell(200, 8, txt=str(item), ln=True)

    file_path = "report.pdf"
    pdf.output(file_path)
    return file_path

# -----------------------------
# UI CONTROLS
# -----------------------------
st.sidebar.header("Controls")

num_records = st.sidebar.slider("Select Data Size", 0, 100, 50)

if st.sidebar.button("Generate Data"):
    st.session_state.data = generate_data(num_records)
    st.session_state.attack_log = []

# ✅ MODIFIED RESET BUTTON
if st.sidebar.button("Reset Data"):
    st.session_state.data = generate_data(num_records)
    st.session_state.attack_log = []

# -----------------------------
# DISPLAY DATA
# -----------------------------
if st.session_state.data is not None:

    st.subheader("📊 Financial Dataset")
    st.dataframe(st.session_state.data)

    # -----------------------------
    # ATTACK BUTTON
    # -----------------------------
    if st.button("🚨 Launch Cyber Attack"):
        attacked_data, details = launch_attack(st.session_state.data)
        st.session_state.data = attacked_data
        st.session_state.attack_log = details

    # -----------------------------
    # COUNTER BUTTON
    # -----------------------------
    if st.button("🛡️ Counter Attack"):
        st.session_state.data = counter_attack(st.session_state.data)

    # -----------------------------
    # METRICS
    # -----------------------------
    total_balance = st.session_state.data["Balance"].sum()
    compromised_count = (st.session_state.data["Status"] == "Compromised").sum()

    total_compromised_amount = sum(
        [x["Amount_Compromised"] for x in st.session_state.attack_log]
    ) if st.session_state.attack_log else 0

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Balance", f"${total_balance:,.0f}")
    col2.metric("Compromised Accounts", compromised_count)
    col3.metric("Total Amount Compromised", f"${total_compromised_amount:,.0f}")

    # -----------------------------
    # ATTACK DETAILS TABLE
    # -----------------------------
    if st.session_state.attack_log:
        st.subheader("🚨 Compromised Account Details")

        attack_df = pd.DataFrame(st.session_state.attack_log)
        st.dataframe(attack_df)

    # -----------------------------
    # GRAPH
    # -----------------------------
    st.subheader("📉 Damage Visualization")

    fig, ax = plt.subplots()
    status_counts = st.session_state.data["Status"].value_counts()
    ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%')
    st.pyplot(fig)

    # -----------------------------
    # DAMAGE EXPLANATION
    # -----------------------------
    st.subheader("📘 Damage Explanation")

    st.write("""
    **How Accounts Were Compromised:**
    - Attackers used phishing emails to steal credentials
    - Credential stuffing exploited reused passwords
    - Malware enabled unauthorized access to systems
    - APIs were exploited due to weak validation controls

    **Why Accounts Were Targeted:**
    - High-value accounts yield maximum financial gain
    - Weak passwords and lack of MFA
    - Limited monitoring and detection controls

    **What Should Be Done to Prevent It:**
    - Enforce Multi-Factor Authentication (MFA)
    - Deploy real-time anomaly detection systems
    - Conduct regular red team / penetration testing
    - Implement strong password policies
    - Secure APIs with tokens and rate limiting
    - Integrate SOC monitoring and alerting systems

    **Impact:**
    - Direct financial loss
    - Reputational damage
    - Compliance and regulatory risk
    """)

    # -----------------------------
    # EXPORT OPTIONS
    # -----------------------------
    st.subheader("📁 Export Results")

    csv = st.session_state.data.to_csv(index=False)
    st.download_button("Download CSV", csv, "data.csv")

    json_data = st.session_state.data.to_json()
    st.download_button("Download JSON", json_data, "data.json")

    if st.button("Generate PDF Report"):
        file_path = export_pdf(st.session_state.data, st.session_state.attack_log)
        with open(file_path, "rb") as f:
            st.download_button("Download PDF", f, "report.pdf")