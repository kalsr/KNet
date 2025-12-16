

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

from openai import OpenAI

import plotly.express as px



# ---------------- CONFIG ----------------

st.set_page_config(layout="wide", page_title="AEGIS-6X | DISA 6G AI Platform")



USE_LLM = True  # toggle for air-gapped deployments



# ---------------- LLM CLIENT ----------------

if USE_LLM:

    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])



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

ROLES = {"Analyst":1, "Commander":2, "Admin":3}

if "role" not in st.session_state:

    st.session_state.role = None



if not st.session_state.role:

    role = st.selectbox("Select Role", ROLES)

    if st.button("Login"):

        st.session_state.role = role

        audit_log("LOGIN", role)

        st.rerun()



# ---------------- DATA ----------------

def generate_data(n):

    df = pd.DataFrame({

        "Edge_Risk": np.random.randint(10,70,n),

        "Core_Risk": np.random.randint(20,95,n),

        "Threat": np.random.choice(["Cyber","Drone","SIGINT","Missile"],n),

        "Country": np.random.choice(["US","CN","RU","IR","KP"],n),

        "Timestamp": datetime.utcnow()

    })

    return df



if "data" not in st.session_state:

    st.session_state.data = generate_data(100)



# ---------------- REAL ML ----------------

def run_ml(df):

    features = df[["Edge_Risk","Core_Risk"]]

    scaler = StandardScaler()

    X = scaler.fit_transform(features)



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

    dist = pairwise_distances([baseline], [current.mean(axis=0)])[0][0]

    return dist



drift_score = detect_drift(baseline_vector, 

                           st.session_state.data[["Edge_Risk","Core_Risk"]].values)



# ---------------- DIGITAL TWIN ----------------

def forecast(df):

    df = df.reset_index()

    model = LinearRegression()

    model.fit(df[["index"]], df["risk_score"])

    future = pd.DataFrame({"index":[len(df)+5,len(df)+15]})

    future["Projected_Risk"] = model.predict(future)

    return future



forecast_df = forecast(st.session_state.data)



# ---------------- LLM ANALYSIS ----------------

def llm_summary(df):

    high = df[df["anomaly"]==-1].head(20)

    prompt = f"""

    You are a defense intelligence analyst.

    Summarize threat patterns, geographic risk,

    confidence levels, and analytic limitations.



    Data:

    {high[['Country','Threat','risk_score','confidence']].to_string(index=False)}

    """

    resp = client.chat.completions.create(

        model="gpt-4o",

        messages=[{"role":"user","content":prompt}],

        temperature=0.2

    )

    audit_log("LLM_SUMMARY","Generated analyst brief")

    return resp.choices[0].message.content



# ---------------- UI ----------------

st.subheader("📊 Threat Intelligence Dashboard")

st.dataframe(st.session_state.data)



fig = px.scatter(

    st.session_state.data,

    x="Edge_Risk",

    y="Core_Risk",

    color=st.session_state.data["anomaly"].map({-1:"High Risk",1:"Normal"}),

    size="risk_score"

)

st.plotly_chart(fig, use_container_width=True)



st.metric("Data Drift Score", f"{drift_score:.3f}")

st.metric("Avg Model Confidence", 

          f"{st.session_state.data['confidence'].mean():.2f}")



st.subheader("🧠 AI Intelligence Brief (LLM)")

if USE_LLM:

    st.markdown(llm_summary(st.session_state.data))

else:

    st.info("LLM disabled – air-gapped mode")



st.subheader("🔮 Digital Twin Forecast")

st.line_chart(forecast_df.set_index("index"))