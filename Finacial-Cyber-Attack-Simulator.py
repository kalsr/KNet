# Finacial-Cyber-Attack-Simulator.py

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



# -----------------------------

# SYNTHETIC DATA GENERATOR

# -----------------------------

def generate_data(n):

    data = pd.DataFrame({

        "Account_ID": range(1, n+1),

        "Balance": np.random.randint(1000, 50000, n),

        "Transactions": np.random.randint(1, 50, n),

        "Status": ["Normal"] * n

    })

    return data



# -----------------------------

# ATTACK SIMULATION

# -----------------------------

def launch_attack(df):

    attacked = df.copy()

    

    # Random accounts compromised

    indices = np.random.choice(df.index, size=int(len(df)*0.3), replace=False)

    

    for i in indices:

        attacked.loc[i, "Balance"] *= random.uniform(0.2, 0.6)  # Loss

        attacked.loc[i, "Status"] = "Compromised"

    

    return attacked



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

def export_pdf(df):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=10)

    

    for i, row in df.iterrows():

        pdf.cell(200, 8, txt=str(row.to_dict()), ln=True)

    

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



if st.sidebar.button("Reset Data"):

    st.session_state.data = None



# -----------------------------

# DISPLAY DATA

# -----------------------------

if st.session_state.data is not None:

    st.subheader("📊 Financial Dataset")

    st.dataframe(st.session_state.data)



    # ATTACK BUTTON

    if st.button("🚨 Launch Cyber Attack"):

        st.session_state.data = launch_attack(st.session_state.data)



    # COUNTER BUTTON

    if st.button("🛡️ Counter Attack"):

        st.session_state.data = counter_attack(st.session_state.data)



    # -----------------------------

    # METRICS

    # -----------------------------

    total_balance = st.session_state.data["Balance"].sum()

    compromised = (st.session_state.data["Status"] == "Compromised").sum()



    col1, col2 = st.columns(2)

    col1.metric("Total Balance", f"${total_balance:,.0f}")

    col2.metric("Compromised Accounts", compromised)



    # -----------------------------

    # GRAPH

    # -----------------------------

    st.subheader("📉 Damage Visualization")



    fig, ax = plt.subplots()

    status_counts = st.session_state.data["Status"].value_counts()

    ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%')

    st.pyplot(fig)



    # -----------------------------

    # EXPLANATION

    # -----------------------------

    st.subheader("📘 Damage Explanation")



    st.write("""

    - **Compromised Accounts**: Accounts impacted by unauthorized access

    - **Balance Reduction**: Simulated financial theft or fraud

    - **Recovered Accounts**: Accounts restored after defense actions

    - **System Impact**: Loss of integrity, confidentiality, and availability

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

        file_path = export_pdf(st.session_state.data)

        with open(file_path, "rb") as f:

            st.download_button("Download PDF", f, "report.pdf")