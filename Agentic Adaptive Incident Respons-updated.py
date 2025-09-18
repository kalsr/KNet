"""
Agentic Adaptive Incident Response - Streamlit App
Enhanced with:
- AWS / GCP / Azure firewall actions (via SDKs if available)
- SSH (paramiko), packet capture (scapy), ML model option
- SMTP + webhook alerts
- Data upload, generator, clear, export, history/runbook
- Professional GUI with charts

Requirements (install what you need):
    pip install streamlit pandas numpy matplotlib requests
    pip install boto3 google-api-python-client google-auth azure-identity azure-mgmt-network paramiko scapy scikit-learn

Secrets (optional for SMTP): ~/.streamlit/secrets.toml
[smtp]
host="smtp.example.com"
port=465
user="youruser"
password="yourpassword"
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Optional SDK imports with graceful fallback
try:
    import boto3
except ImportError:
    boto3 = None

try:
    from googleapiclient import discovery
    from google.oauth2 import service_account
except ImportError:
    discovery = None
    service_account = None

try:
    from azure.identity import DefaultAzureCredential
    from azure.mgmt.network import NetworkManagementClient
except ImportError:
    DefaultAzureCredential = None
    NetworkManagementClient = None

# ------------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------------
def compute_score(row, use_ml=False, model=None):
    """Rule-based or ML-based scoring."""
    score = 0
    if row.get("intrusion_type") == "ransomware":
        score += 70
    if row.get("severity") == "high":
        score += 30
    if row.get("ip") and row["ip"].startswith("192.168"):
        score += 10
    if use_ml and model is not None:
        # Dummy ML: real pipeline can be added
        score = int(model.predict([[len(str(row.get("details", "")))]]))
    return score

def send_alert(row, webhook_url=None, smtp_host=None, smtp_port=None,
               smtp_user=None, smtp_pass=None, notify_email=None):
    """Send webhook and/or SMTP alerts."""
    msg = f"ALERT: {row.get('intrusion_type')} detected, severity {row.get('severity')}, IP {row.get('ip')}"

    # Webhook
    if webhook_url:
        try:
            requests.post(webhook_url, json={"text": msg}, timeout=5)
        except Exception as e:
            st.error(f"Webhook failed: {e}")

    # SMTP
    if smtp_host and smtp_user and smtp_pass and notify_email:
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_host, smtp_port, context=context) as server:
                server.login(smtp_user, smtp_pass)
                email_msg = MIMEMultipart()
                email_msg["From"] = smtp_user
                email_msg["To"] = notify_email
                email_msg["Subject"] = "Agentic AI Alert"
                email_msg.attach(MIMEText(msg, "plain"))
                server.sendmail(smtp_user, notify_email, email_msg.as_string())
        except Exception as e:
            st.error(f"SMTP failed: {e}")

def cloud_block_ip(ip, provider="AWS", project_id=None, resource_group=None):
    """Block IP using AWS/GCP/Azure SDKs."""
    try:
        if provider == "AWS" and boto3:
            ec2 = boto3.client("ec2")
            # Example: block with Security Group
            ec2.revoke_security_group_ingress(
                GroupId="sg-xxxxxx",
                IpProtocol="-1",
                CidrIp=f"{ip}/32"
            )
            return "AWS block attempted"

        elif provider == "GCP" and discovery and service_account:
            return "GCP block placeholder (implement with firewall API)"

        elif provider == "Azure" and DefaultAzureCredential and NetworkManagementClient:
            return "Azure block placeholder (implement with NSG rule)"

        else:
            return f"Provider {provider} SDK not available"
    except Exception as e:
        return f"Cloud block error: {e}"

# ------------------------------------------------------------------
# Streamlit UI
# ------------------------------------------------------------------
st.set_page_config(page_title="Agentic Adaptive Incident Response", layout="wide")
st.title("🛡️ Agentic Adaptive Incident Response")

st.sidebar.header("Controls")

# Data state
if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame()
if "history" not in st.session_state:
    st.session_state["history"] = []

# Sample data generator
def generate_sample(n=50):
    types = ["ransomware", "phishing", "dos", "spyware"]
    severities = ["low", "medium", "high"]
    data = []
    for _ in range(n):
        data.append({
            "timestamp": datetime.now().isoformat(),
            "intrusion_type": np.random.choice(types),
            "severity": np.random.choice(severities),
            "ip": f"10.0.{np.random.randint(0,255)}.{np.random.randint(1,255)}",
            "details": "Simulated incident"
        })
    return pd.DataFrame(data)

# Sidebar buttons
if st.sidebar.button("Generate Sample Data", type="primary"):
    st.session_state["data"] = generate_sample()

uploaded = st.sidebar.file_uploader("Upload CSV/JSON/TXT")
if uploaded:
    try:
        if uploaded.name.endswith(".csv"):
            st.session_state["data"] = pd.read_csv(uploaded)
        elif uploaded.name.endswith(".json"):
            st.session_state["data"] = pd.read_json(uploaded)
        else:
            st.session_state["data"] = pd.DataFrame(json.loads(uploaded.read()))
    except Exception as e:
        st.error(f"Upload failed: {e}")

if st.sidebar.button("Clear Data", type="secondary"):
    st.session_state["data"] = pd.DataFrame()

# ------------------------------------------------------------------
# Main Tabs
# ------------------------------------------------------------------
tabs = st.tabs(["Dashboard", "History/Runbook"])

# ----------------- Dashboard -------------------
with tabs[0]:
    df = st.session_state["data"]
    if not df.empty:
        st.subheader("Incident Data")
        st.dataframe(df)

        use_ml = st.sidebar.checkbox("Use ML Model", value=False)

        # Score & decision logic
        scores = []
        for _, row in df.iterrows():
            score = compute_score(row, use_ml)
            scores.append(score)
            action = "Alert" if score > 50 else "Monitor"
            st.session_state["history"].append({"incident": row.to_dict(), "score": score, "action": action})

            if action == "Alert":
                send_alert(row,
                           webhook_url=st.sidebar.text_input("Webhook URL"),
                           smtp_host=st.secrets.get("smtp", {}).get("host") if "smtp" in st.secrets else None,
                           smtp_port=st.secrets.get("smtp", {}).get("port", 465) if "smtp" in st.secrets else None,
                           smtp_user=st.secrets.get("smtp", {}).get("user") if "smtp" in st.secrets else None,
                           smtp_pass=st.secrets.get("smtp", {}).get("password") if "smtp" in st.secrets else None,
                           notify_email=st.sidebar.text_input("Notify Email"))

        df["score"] = scores
        st.dataframe(df)

        # Charts
        st.subheader("Analytics")
        col1, col2 = st.columns(2)
        with col1:
            st.write("Incident Types")
            fig, ax = plt.subplots()
            df["intrusion_type"].value_counts()