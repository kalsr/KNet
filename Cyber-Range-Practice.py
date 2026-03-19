# Cyber-Range-Practice

import streamlit as st

import pandas as pd

import numpy as np

import time

import random

from sklearn.ensemble import IsolationForest



# -------------------------------

# PAGE CONFIG

# -------------------------------

st.set_page_config(layout="wide")



# -------------------------------

# CUSTOM CSS (Blue Title + Buttons)

# -------------------------------

st.markdown("""

<style>

.title {

    font-size:40px;

    font-weight:bold;

    color:blue;

    text-align:center;

}

.stButton>button {

    background-color:#007BFF;

    color:white;

    font-weight:bold;

    border-radius:10px;

    padding:10px;

}

</style>

""", unsafe_allow_html=True)



# -------------------------------

# TITLE

# -------------------------------

st.markdown('<div class="title">KALSNET CYBER RANGE DASHBOARD<br>Developed by Randy Singh (Kalsnet - Consulting Group)</div>', unsafe_allow_html=True)



st.write("---")



# -------------------------------

# SESSION STATE

# -------------------------------

if "logs" not in st.session_state:

    st.session_state.logs = []



if "traffic" not in st.session_state:

    st.session_state.traffic = []



# -------------------------------

# HELPER FUNCTIONS

# -------------------------------

def log_event(message, severity):

    st.session_state.logs.append({

        "time": time.strftime("%H:%M:%S"),

        "event": message,

        "severity": severity

    })



def generate_traffic():

    val = random.randint(50, 200)

    st.session_state.traffic.append(val)

    if len(st.session_state.traffic) > 30:

        st.session_state.traffic.pop(0)



# -------------------------------

# AI ANOMALY DETECTION

# -------------------------------

def detect_anomaly(data):

    if len(data) < 10:

        return "Not enough data"



    model = IsolationForest(contamination=0.1)

    X = np.array(data).reshape(-1,1)

    model.fit(X)

    preds = model.predict(X)



    anomalies = sum(preds == -1)

    return f"Anomaly Score: {anomalies}"



# -------------------------------

# TOP METRICS

# -------------------------------

col1, col2, col3, col4 = st.columns(4)



col1.metric("Threat Level", random.choice(["LOW", "MEDIUM", "HIGH", "CRITICAL"]))

col2.metric("Active Incidents", random.randint(1, 10))

col3.metric("Alerts (24h)", random.randint(50, 200))

col4.metric("Blocked Attacks", random.randint(100, 500))



st.write("---")



# -------------------------------

# ATTACK CONTROL PANEL

# -------------------------------

st.subheader("🎮 Attack Simulation Controls")



col1, col2, col3, col4, col5 = st.columns(5)



# 1 Phishing

if col1.button("📧 Phishing Attack"):

    log_event("Phishing email campaign launched", "HIGH")



# 2 Brute Force

if col2.button("🔐 Brute Force Attack"):

    for _ in range(5):

        log_event("Multiple failed login attempts detected", "CRITICAL")



# 3 Ransomware

if col3.button("🦠 Ransomware Simulation"):

    log_event("File encryption activity detected!", "CRITICAL")



# 4 Data Exfiltration

if col4.button("📡 Data Exfiltration"):

    log_event("Large outbound data transfer detected", "HIGH")



# 5 Insider Threat

if col5.button("🧠 Insider Threat"):

    log_event("Unauthorized sensitive file access", "HIGH")



st.write("---")



# -------------------------------

# DEFENSE ACTIONS

# -------------------------------

st.subheader("🛡️ Defense Controls")



col1, col2, col3, col4 = st.columns(4)



if col1.button("🚫 Block IP"):

    log_event("Malicious IP blocked", "MEDIUM")



if col2.button("🔒 Lock Account"):

    log_event("User account locked", "MEDIUM")



if col3.button("📴 Isolate Device"):

    log_event("Endpoint isolated from network", "HIGH")



if col4.button("🔄 Reset Password"):

    log_event("Password reset triggered", "LOW")



st.write("---")



# -------------------------------

# NETWORK TRAFFIC

# -------------------------------

st.subheader("📊 Network Traffic")



generate_traffic()

traffic_df = pd.DataFrame({"Traffic": st.session_state.traffic})

st.line_chart(traffic_df)



# -------------------------------

# AI PANEL

# -------------------------------

st.subheader("🧠 AI Anomaly Detection")



anomaly_score = detect_anomaly(st.session_state.traffic)

st.write(anomaly_score)



# -------------------------------

# ALERTS PANEL

# -------------------------------

st.subheader("🚨 Live Alerts Feed")



log_df = pd.DataFrame(st.session_state.logs)



if not log_df.empty:

    st.dataframe(log_df.tail(10))

else:

    st.write("No alerts yet")



# -------------------------------

# AUTO REFRESH

# -------------------------------

time.sleep(2)

st.rerun()
