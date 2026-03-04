# Cyber_Range_App.py

# Structured UI

# Data science logic

# Risk scoring model

# Charts

# Export options

# Real data capability

# Field documentation




import streamlit as st

import pandas as pd

import numpy as np

import random

from faker import Faker

import datetime

import matplotlib.pyplot as plt

import json

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table

from reportlab.lib import colors

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib import pagesizes



fake = Faker()



st.set_page_config(page_title="Cyber Range Demo", layout="wide")



# -----------------------------

# Professional Header

# -----------------------------

st.markdown(

    """

    <h1 style='text-align: center; color: #0A3D91;'>

    Cyber Range Simulation Platform <br>

    Developed by Randy Singh – KNet Consulting Group

    </h1>

    """,

    unsafe_allow_html=True

)



st.markdown("---")



# -----------------------------

# Sidebar Controls

# -----------------------------

st.sidebar.header("Simulation Controls")



data_option = st.sidebar.radio(

    "Select Data Source",

    ["Generate Synthetic Data", "Upload Real CSV Data"]

)



attack_types = [

    "Brute Force",

    "SQL Injection",

    "DDoS",

    "Phishing",

    "Ransomware"

]



# -----------------------------

# Synthetic Data Generator

# -----------------------------

def generate_data(records=100):



    severity_map = {

        "Low": 1,

        "Medium": 2,

        "High": 3,

        "Critical": 4

    }



    data = []



    for _ in range(records):



        severity = random.choice(list(severity_map.keys()))

        status = random.choice(["Blocked", "Successful"])

        response_time = random.randint(50, 500)



        severity_weight = severity_map[severity]

        success_factor = 1 if status == "Blocked" else 2

        delay_factor = response_time / 100



        risk_score = severity_weight * success_factor * delay_factor



        data.append({

            "Timestamp": fake.date_time_this_year(),

            "Source IP": fake.ipv4(),

            "Destination IP": fake.ipv4(),

            "Attack Type": random.choice(attack_types),

            "Severity": severity,

            "Status": status,

            "Response Time (ms)": response_time,

            "Risk Score": round(risk_score, 2)

        })



    return pd.DataFrame(data)



# -----------------------------

# Data Loading

# -----------------------------

if data_option == "Generate Synthetic Data":

    record_count = st.sidebar.slider("Number of Records", 50, 200, 100)

    df = generate_data(record_count)



else:

    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file:

        df = pd.read_csv(uploaded_file)

    else:

        st.warning("Please upload a CSV file.")

        st.stop()



# -----------------------------

# Attack Launcher

# -----------------------------

st.subheader("Launch Cyber Attack Simulation")



selected_attack = st.selectbox("Select Attack Type", attack_types)



if st.button("Launch Attack"):



    st.success(f"{selected_attack} simulation launched successfully!")



# -----------------------------

# Display Data

# -----------------------------

st.subheader("Attack Log Data")

st.dataframe(df)



# -----------------------------

# Pie Chart - Attack Type

# -----------------------------

st.subheader("Attack Distribution")



attack_counts = df["Attack Type"].value_counts()



fig1, ax1 = plt.subplots()

ax1.pie(attack_counts, labels=attack_counts.index, autopct='%1.1f%%')

ax1.set_title("Attack Type Distribution")

st.pyplot(fig1)



# -----------------------------

# Pie Chart - Severity

# -----------------------------

st.subheader("Severity Distribution")



severity_counts = df["Severity"].value_counts()



fig2, ax2 = plt.subplots()

ax2.pie(severity_counts, labels=severity_counts.index, autopct='%1.1f%%')

ax2.set_title("Severity Breakdown")

st.pyplot(fig2)



# -----------------------------

# Field Explanation Section

# -----------------------------

st.subheader("Field Explanation")



st.markdown("""

- **Timestamp** → Identifies when the attack occurred.

- **Source IP** → Helps trace attacker origin.

- **Destination IP** → Identifies targeted asset.

- **Attack Type** → Classifies type of cyber threat.

- **Severity** → Indicates criticality level.

- **Status** → Shows whether attack was blocked or successful.

- **Response Time** → Measures detection and mitigation speed.

- **Risk Score** → Calculated risk metric based on severity, success & delay.

""")



# -----------------------------

# Export Section

# -----------------------------

st.subheader("Export Results")



# CSV

csv = df.to_csv(index=False).encode("utf-8")

st.download_button("Download CSV", csv, "cyber_range_results.csv", "text/csv")



# JSON

json_data = df.to_json(orient="records")

st.download_button("Download JSON", json_data, "cyber_range_results.json", "application/json")



# PDF

def create_pdf(dataframe):



    doc = SimpleDocTemplate("cyber_range_report.pdf", pagesize=pagesizes.letter)

    elements = []

    styles = getSampleStyleSheet()



    elements.append(Paragraph("Cyber Range Simulation Report", styles['Heading1']))

    elements.append(Spacer(1, 12))



    table_data = [dataframe.columns.tolist()] + dataframe.values.tolist()

    table = Table(table_data)

    table.setStyle([

        ('BACKGROUND', (0,0), (-1,0), colors.grey),

        ('GRID', (0,0), (-1,-1), 1, colors.black)

    ])



    elements.append(table)

    doc.build(elements)



create_pdf(df)



with open("cyber_range_report.pdf", "rb") as f:

    st.download_button("Download PDF", f, "cyber_range_report.pdf", "application/pdf")

