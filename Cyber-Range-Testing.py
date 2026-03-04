# Cyber-Range-Testing.py

import streamlit as st

import pandas as pd

import numpy as np

import random

from faker import Faker

from sklearn.ensemble import IsolationForest

import matplotlib.pyplot as plt

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table

from reportlab.lib import colors

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib import pagesizes

import datetime

import json

import os



# -------------------------------------------------------

# CONFIGURATION

# -------------------------------------------------------

st.set_page_config(page_title="KNet Cyber Range SaaS", layout="wide")

fake = Faker()



# -------------------------------------------------------

# PROFESSIONAL HEADER

# -------------------------------------------------------

st.markdown("""

<h1 style='text-align:center; color:#0A3D91;'>

KNet Enterprise Cyber Range Platform<br>
A Simulated Controlled Virtual Environment<br>
A Platform to Practice Cyber Security Skills Safely<br>

Developed by Randy Singh – KNet Consulting Group

</h1>

""", unsafe_allow_html=True)



st.markdown("---")



# -------------------------------------------------------

# SESSION STATE FOR MULTI-TENANT SIMULATION

# -------------------------------------------------------

if "tenant" not in st.session_state:

    st.session_state.tenant = "Tenant_A"



if "role" not in st.session_state:

    st.session_state.role = "Analyst"



# -------------------------------------------------------

# SIDEBAR CONTROLS

# -------------------------------------------------------

st.sidebar.header("SaaS Controls")



st.session_state.tenant = st.sidebar.selectbox(

    "Select Tenant",

    ["Tenant_A", "Tenant_B", "Tenant_Gov"]

)



st.session_state.role = st.sidebar.selectbox(

    "Select Role",

    ["Admin", "Instructor", "Analyst"]

)



data_option = st.sidebar.radio(

    "Data Source",

    ["Generate Synthetic Data", "Upload CSV"]

)



record_count = st.sidebar.slider("Synthetic Records", 50, 200, 100)



attack_types = ["Brute Force", "SQL Injection", "DDoS", "Phishing", "Ransomware"]



mitre_map = {

    "Brute Force": "Credential Access - T1110",

    "SQL Injection": "Initial Access - T1190",

    "DDoS": "Impact - T1498",

    "Phishing": "Initial Access - T1566",

    "Ransomware": "Impact - T1486"

}



severity_weights = {"Low":1, "Medium":2, "High":3, "Critical":4}



# -------------------------------------------------------

# DATA GENERATION

# -------------------------------------------------------

def generate_data(records):

    data = []

    for _ in range(records):



        severity = random.choice(list(severity_weights.keys()))

        status = random.choice(["Blocked", "Successful"])

        response_time = random.randint(50,500)



        risk_score = (

            severity_weights[severity] *

            (1 if status=="Blocked" else 2) *

            (response_time/100)

        )



        data.append({

            "Tenant": st.session_state.tenant,

            "Timestamp": fake.date_time_this_year(),

            "Source_IP": fake.ipv4(),

            "Destination_IP": fake.ipv4(),

            "Attack_Type": random.choice(attack_types),

            "MITRE_Mapping": mitre_map[random.choice(attack_types)],

            "Severity": severity,

            "Status": status,

            "Response_Time_ms": response_time,

            "Risk_Score": round(risk_score,2)

        })

    return pd.DataFrame(data)



# -------------------------------------------------------

# LOAD DATA

# -------------------------------------------------------

if data_option == "Generate Synthetic Data":

    df = generate_data(record_count)

else:

    uploaded = st.sidebar.file_uploader("Upload CSV", type=["csv"])

    if uploaded:

        df = pd.read_csv(uploaded)

    else:

        st.warning("Upload CSV file")

        st.stop()



# -------------------------------------------------------

# AI ANOMALY DETECTION

# -------------------------------------------------------

def run_ai_model(df):

    model = IsolationForest(contamination=0.05, random_state=42)

    features = df[["Response_Time_ms","Risk_Score"]]

    model.fit(features)

    df["Anomaly"] = model.predict(features)

    df["Anomaly"] = df["Anomaly"].apply(lambda x: "Suspicious" if x==-1 else "Normal")

    return df



df = run_ai_model(df)



# -------------------------------------------------------

# DASHBOARD METRICS

# -------------------------------------------------------

st.subheader("Enterprise SOC Dashboard")



col1, col2, col3, col4 = st.columns(4)



col1.metric("Total Attacks", len(df))

col2.metric("High/Critical",

            len(df[df["Severity"].isin(["High","Critical"])]))

col3.metric("Successful",

            len(df[df["Status"]=="Successful"]))

col4.metric("AI Suspicious",

            len(df[df["Anomaly"]=="Suspicious"]))



st.markdown("---")



# -------------------------------------------------------

# ATTACK LAUNCH SIMULATION

# -------------------------------------------------------

st.subheader("Attack Simulation Launcher")



selected_attack = st.selectbox("Select Attack", attack_types)



if st.button("Launch Attack"):

    st.success(f"{selected_attack} simulation executed for {st.session_state.tenant}")



# -------------------------------------------------------

# DATA TABLE

# -------------------------------------------------------

st.subheader("Attack Log Table")

st.dataframe(df, use_container_width=True)



# -------------------------------------------------------

# PIE CHARTS

# -------------------------------------------------------

st.subheader("Attack Distribution")



fig1, ax1 = plt.subplots()

df["Attack_Type"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax1)

st.pyplot(fig1)



st.subheader("Severity Breakdown")



fig2, ax2 = plt.subplots()

df["Severity"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax2)

st.pyplot(fig2)



# -------------------------------------------------------

# FIELD EXPLANATION

# -------------------------------------------------------

st.subheader("Field Explanation")



st.markdown("""

**Tenant** – Organization isolation for SaaS multi-tenancy.  

**Timestamp** – When attack occurred.  

**Source_IP** – Attacker origin.  

**Destination_IP** – Target system.  

**Attack_Type** – Classification of threat.  

**MITRE_Mapping** – Mapped technique for compliance.  

**Severity** – Risk criticality level.  

**Status** – Blocked or Successful.  

**Response_Time_ms** – Detection latency.  

**Risk_Score** – Calculated metric (Severity × Success × Delay).  

**Anomaly** – AI-detected suspicious behavior.  

""")



# -------------------------------------------------------

# EXPORT OPTIONS

# -------------------------------------------------------

st.subheader("Export Reports")



# CSV

csv = df.to_csv(index=False).encode("utf-8")

st.download_button("Download CSV", csv, "knet_cyber_range.csv", "text/csv")



# JSON

json_data = df.to_json(orient="records")

st.download_button("Download JSON", json_data, "knet_cyber_range.json", "application/json")



# PDF

def create_pdf(dataframe):

    filename = "knet_cyber_range_report.pdf"

    doc = SimpleDocTemplate(filename, pagesize=pagesizes.letter)

    elements = []

    styles = getSampleStyleSheet()

    elements.append(Paragraph("KNet Cyber Range Enterprise Report", styles['Heading1']))

    elements.append(Spacer(1,12))

    table_data = [dataframe.columns.tolist()] + dataframe.values.tolist()

    table = Table(table_data)

    table.setStyle([

        ('BACKGROUND',(0,0),(-1,0),colors.grey),

        ('GRID',(0,0),(-1,-1),1,colors.black)

    ])

    elements.append(table)

    doc.build(elements)

    return filename



pdf_file = create_pdf(df)

with open(pdf_file,"rb") as f:

    st.download_button("Download PDF", f, pdf_file, "application/pdf")



st.success("Enterprise Cyber Range SaaS Demo Running Successfully")

