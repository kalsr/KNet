# Kalsnet_Compliance-Soc_Dashboard.py

import streamlit as st

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from datetime import datetime

from fpdf import FPDF

import time



# ==========================================================

# PAGE CONFIGURATION

# ==========================================================

st.set_page_config(

    page_title="KNet Compliance SOC Dashboard",

    layout="wide"

)



# ==========================================================

# HEADER BRANDING

# ==========================================================

st.markdown("""

<h1 style="text-align:center; color:blue; font-size:46px;">

KNet SOC Dashboard – Threat Monitoring + Compliance Mapping

</h1>



<h3 style="text-align:center;">

Designed & Developed by <b>Randy Singh</b><br>

Kalsnet (KNet) Consulting Group

</h3>

<hr>

""", unsafe_allow_html=True)



# ==========================================================

# ATTACKS + MITRE ATT&CK MAPPING

# ==========================================================

attack_map = {

    "🎣 Phishing": ("T1566", "Phishing"),

    "🔒 Ransomware": ("T1486", "Data Encrypted for Impact"),

    "🚫 DoS Attack": ("T1499", "Denial of Service"),

    "🕵️ MitM": ("T1557", "Adversary-in-the-Middle"),

    "🗄 SQL Injection": ("T1190", "Exploit Public-Facing App"),

    "💻 XSS": ("T1059", "Command & Scripting Interpreter"),

    "⏳ Zero-Day": ("T1203", "Client Execution Exploit"),

    "🌍 DNS Spoofing": ("T1565", "Data Manipulation")

}



# ==========================================================

# NIST / FedRAMP CONTROL MAPPING (DEMO)

# ==========================================================

nist_controls = {

    "🎣 Phishing": ["AT-2 Security Awareness", "IA-2 Identification"],

    "🔒 Ransomware": ["CP-9 Backups", "IR-4 Incident Handling"],

    "🚫 DoS Attack": ["SC-5 Denial of Service Protection"],

    "🕵️ MitM": ["SC-8 Transmission Confidentiality"],

    "🗄 SQL Injection": ["SI-10 Input Validation", "SC-7 Boundary Protection"],

    "💻 XSS": ["SI-10 Input Validation"],

    "⏳ Zero-Day": ["SI-2 Flaw Remediation", "RA-5 Vulnerability Scanning"],

    "🌍 DNS Spoofing": ["SC-20 Secure Name Resolution"]

}



# ==========================================================

# SIDEBAR CONTROLS

# ==========================================================

st.sidebar.header("⚙ SOC Configuration")



mode = st.sidebar.radio(

    "Select Demo Mode:",

    ["FedRAMP / DoD Compliance SOC", "Commercial SOC (Bank/Healthcare)"]

)



records = st.sidebar.slider("Synthetic Threat Events (0–100)", 10, 100, 50)



refresh = st.sidebar.slider("Auto Refresh (Seconds)", 2, 6, 3)



uploaded = st.sidebar.file_uploader("Upload Customer Log CSV", type=["csv"])



# ==========================================================

# DATA GENERATION OR UPLOAD

# ==========================================================

if uploaded:

    df = pd.read_csv(uploaded)

else:

    df = pd.DataFrame({

        "Time": [datetime.now().strftime("%H:%M:%S") for _ in range(records)],

        "Attack_Type": np.random.choice(list(attack_map.keys()), records),

        "Severity": np.random.choice(["Low", "Medium", "High", "Critical"], records),

        "Source_IP": [

            f"10.{np.random.randint(1,255)}.{np.random.randint(1,255)}.{np.random.randint(1,255)}"

            for _ in range(records)

        ],

        "Detected": np.random.choice(["Yes", "No"], records)

    })



# ==========================================================

# THREAT SCORING ENGINE

# ==========================================================

def score_event(row):

    base = {"Low": 15, "Medium": 35, "High": 65, "Critical": 90}

    score = base[row["Severity"]]



    if row["Detected"] == "No":

        score += 15



    return min(100, score)



df["Threat_Score"] = df.apply(score_event, axis=1)



# ==========================================================

# EXECUTIVE DASHBOARD METRICS

# ==========================================================

st.subheader("📡 Executive SOC Threat Overview")



c1, c2, c3, c4 = st.columns(4)



c1.metric("Total Events", len(df))

c2.metric("Critical Events", len(df[df["Severity"] == "Critical"]))

...

Show trimmed content