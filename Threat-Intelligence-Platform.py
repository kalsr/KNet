

# =========================================================
# AEGIS-6X | 6G AI/ML Threat Intelligence Platform
# Designed & Developed by Randy Singh – KNet Consulting
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import json
from datetime import datetime
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import pairwise_distances
from sklearn.linear_model import LinearRegression
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(layout="wide", page_title="AEGIS-6X | DISA 6G AI Platform")

# ---------------- LLM SAFE INITIALIZATION ----------------
USE_LLM = False
client = None

try:
    if "OPENAI_API_KEY" in st.secrets:
        from openai import OpenAI
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        USE_LLM = True
except Exception:
    USE_LLM = False

# ---------------- AUDIT LOG ----------------
def audit_log(event, detail):
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event,
        "detail": detail,
        "user": st.session_state.get("role", "UNKNOWN")
    }
    with open("audit_log.jsonl", "a") as f:
        f.write(json.dumps(record) + "\n")

# ---------------- HEADER ----------------
st.markdown("""
<div style="background:#003A8F;padding:18px;border-radius:10px;color:white;text-align:center">
<h2>AEGIS-6X | 6G AI/ML Threat Intelligence Platform</h2>
<p>Human-in-the-Loop | NATO-Aligned | DISA / JADC2 Ready</p>
<p><b>Developed by Randy Singh – KNet Consulting Group</b></p>
</div>
""", unsafe_allow_html=True)

# ---------------- RBAC ----------------
ROLES = {"Analyst": 1, "Commander": 2, "Admin": 3}

if "role" not in st.session_state:
    st.session_state.role = None

if not st.session_state.role:
    role = st.selectbox("Select Role", ROLES)
    if st.button("Login"):
        st.session_state.role = role
        audit_log("LOGIN", role)
        st.rerun()
    st.stop()

# ---------------- DATA GENERATOR ----------------
def generate_data(n):
    return pd.DataFrame({
        "Edge_Risk": np.random.randint(10, 70, n),
        "Core_Risk": np.random.randint(20, 95, n),
        "Threat": np.random.choice(["Cyber", "Drone", "SIGINT", "Missile"], n),
        "Country": np.random.choice(["US", "CN", "RU", "IR", "KP"], n),
        "Timestamp": datetime.utcnow()
    })

if "data" not in st.session_state:
    st.session_state.data = generate_data(100)

# ---------------- ML PIPELINE ----------------
def run_ml(df):
    scaler = StandardScaler()
    X = scaler.fit_transform(df[["Edge_Risk", "Core_Risk"]])

    model = IsolationForest(contamination=0.15, random_state=42)
    df["anomaly"] = model.fit_predict(X)
    df["risk_score"] = -model.decision_function(X)

    df["confidence"] = np.clip(
        1 - (df["risk_score"] / df["risk_score"].max()),
        0.1, 0.99
    )

    audit_log("ML_INFERENCE", "IsolationForest executed")
    return df, X.mean(axis=0)

st.session_state.data, baseline_vector = run_ml(st.session_state.data)

# ---------------- DRIFT DETECTION ----------------
def detect_drift(baseline, current):
    return pairwise_distances([baseline], [current.mean(axis=0)])[0][0]

drift_score = detect_drift(
    baseline_vector,
    st.session_state.data[["Edge_Risk", "Core_Risk"]].values
)

# ---------------- DIGITAL TWIN ----------------
def forecast(df):
    df = df.reset_index()
    model = LinearRegression()
    model.fit(df[["index"]], df["risk_score"])
    future = pd.DataFrame({"index": [len(df)+5, len(df)+15]})
    future["Projected_Risk"] = model.predict(future)
    return future

forecast_df = forecast(st.session_state.data)

# ---------------- LLM SUMMARY (SAFE) ----------------
def llm_summary(df):
    if not USE_LLM:
        return "🔒 LLM disabled — running in air-gapped / secure mode."

    high = df[df["anomaly"] == -1].head(20)
    prompt = f"""
You are a defense intelligence analyst.
Summarize threat patterns, geographic risk,
confidence levels, and analytic limitations.

Data:
{high[['Country','Threat','risk_score','confidence']].to_string(index=False)}
"""
    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    audit_log("LLM_SUMMARY", "Generated analyst brief")
    return resp.choices[0].message.content

# ---------------- UI ----------------
st.subheader("📊 Threat Intelligence Dashboard")
st.dataframe(st.session_state.data, use_container_width=True)

fig = px.scatter(
    st.session_state.data,
    x="Edge_Risk",
    y="Core_Risk",
    color=st.session_state.data["anomaly"].map({-1: "High Risk", 1: "Normal"}),
    size="risk_score",
    hover_data=["Country", "Threat", "confidence"]
)
st.plotly_chart(fig, use_container_width=True)

c1, c2, c3 = st.columns(3)
c1.metric("Data Drift Score", f"{drift_score:.3f}")
c2.metric("Avg Model Confidence", f"{st.session_state.data['confidence'].mean():.2f}")
c3.metric("LLM Status", "Enabled" if USE_LLM else "Disabled")

st.subheader("🧠 AI Intelligence Brief")
st.markdown(llm_summary(st.session_state.data))

st.subheader("🔮 Digital Twin Forecast")
st.line_chart(forecast_df.set_index("index"))
