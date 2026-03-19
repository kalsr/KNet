]# Cyber-Range-Modified

import streamlit as st

import pandas as pd

import numpy as np

import random

import time

import hashlib

from sklearn.ensemble import IsolationForest



# ----------------------------------

# PAGE CONFIG

# ----------------------------------

st.set_page_config(layout="wide")



# ----------------------------------

# CUSTOM UI (TITLE + COLORS)

# ----------------------------------

st.markdown("""

<style>

.title {

    font-size:38px;

    font-weight:bold;

    color:blue;

    text-align:center;

}

.card {

    padding:10px;

    border-radius:10px;

    background-color:#f5f7fa;

}

.stButton>button {

    background-color:#007BFF;

    color:white;

    font-weight:bold;

    border-radius:8px;

    padding:8px;

}

</style>

""", unsafe_allow_html=True)



st.markdown('<div class="title">KALSNET CYBER RANGE DASHBOARD<br>Developed by Tandy Singh (KNet Consulting Group)</div>', unsafe_allow_html=True)



# ----------------------------------

# AUTH SYSTEM (MULTI USER)

# ----------------------------------

def hash_pw(pw):

    return hashlib.sha256(pw.encode()).hexdigest()



USERS = {

    "admin": {"pw": hash_pw("admin123"), "role": "Admin"},

    "analyst": {"pw": hash_pw("analyst123"), "role": "Analyst"},

    "viewer": {"pw": hash_pw("viewer123"), "role": "Viewer"}

}



if "user" not in st.session_state:

    st.session_state.user = None



st.sidebar.title("🔐 Login")



username = st.sidebar.text_input("Username")

password = st.sidebar.text_input("Password", type="password")



if st.sidebar.button("Login"):

    if username in USERS and USERS[username]["pw"] == hash_pw(password):

        st.session_state.user = username

        st.session_state.role = USERS[username]["role"]

    else:

        st.sidebar.error("Invalid login")



if not st.session_state.user:

    st.stop()



role = st.session_state.role

st.sidebar.success(f"Logged in: {st.session_state.user} ({role})")



# ----------------------------------

# SESSION STATE

# ----------------------------------

if "logs" not in st.session_state:

    st.session_state.logs = []



if "traffic" not in st.session_state:

    st.session_state.traffic = []



# ----------------------------------

# LOGGING

# ----------------------------------

def log(msg, sev):

    st.session_state.logs.append({

        "Time": time.strftime("%H:%M:%S"),

        "Event": msg,

        "Severity": sev

    })



# ----------------------------------

# ATTACK FUNCTIONS

# ----------------------------------

def phishing():

    log("Phishing campaign launched", "HIGH")



def brute():

    for _ in range(5):

        log("Failed login attempt", "CRITICAL")



def ransomware():

    log("Ransomware encryption behavior detected", "CRITICAL")



def exfiltration():

    log("Data exfiltration detected", "HIGH")



def insider():

    log("Insider unauthorized access", "HIGH")



# ----------------------------------

# DEFENSE ACTIONS

# ----------------------------------

def block_ip():

    log("Blocked malicious IP", "MEDIUM")



def lock_account():

    log("User account locked", "MEDIUM")



def isolate_device():

    log("Device isolated", "HIGH")



def reset_pw():

    log("Password reset", "LOW")



# ----------------------------------

# AI ANOMALY DETECTION

# ----------------------------------

def anomaly_score(data):

    if len(data) < 10: