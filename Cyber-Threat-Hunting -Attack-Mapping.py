# Cyber Threat Hunting & Attack Mapping

# Use Case:

# Graph-based reasoning to link attacker behaviors (MITRE ATT&CK, logs, alerts)

# LLM explanations to describe anomalies and suggest remediation

# THIS APPLICATION IS DESIGNED & DEVELOPED BY RANDY SINGH FROM KNet CONSULTING GROUP.


import streamlit as st

import pandas as pd

import numpy as np

import networkx as nx

from pyvis.network import Network

import streamlit.components.v1 as components

import json

import random

from datetime import datetime, timedelta

import os



# Optional OpenAI

try:

    import openai

    OPENAI_AVAILABLE = True

except Exception:

    OPENAI_AVAILABLE = False





# ----------------------------

# Generate synthetic log events

# ----------------------------

def generate_sample_data(n=200):

    users = [f"user{i}" for i in range(1, 11)]

    hosts = [f"host{i}.corp.local" for i in range(1, 6)]

    ips = [f"10.0.{i}.{j}" for i in range(1, 3) for j in range(1, 20)]

    actions = ["login", "file_access", "cmd_exec"]

    results = ["success", "failure"]



    events = []

    ts = datetime.utcnow() - timedelta(days=1)

    for _ in range(n):

        ts += timedelta(seconds=random.randint(30, 300))

        events.append({

            "timestamp": ts.isoformat(),

            "src_ip": random.choice(ips),

            "dest_host": random.choice(hosts),

            "user": random.choice(users),

            "action": random.choice(actions),

            "result": random.choice(results),

        })

    return pd.DataFrame(events)





# ----------------------------

# Graph builder

# ----------------------------

def build_graph(df):

    G = nx.DiGraph()

    for _, row in df.iterrows():

        ip = f"IP:{row['src_ip']}"

        user = f"User:{row['user']}"

        host = f"Host:{row['dest_host']}"

        G.add_node(ip, label=row['src_ip'], ntype="ip")

        G.add_node(user, label=row['user'], ntype="user")

        G.add_node(host, label=row['dest_host'], ntype="host")

        G.add_edge(ip, user, action=row['action'], result=row['result'])

        G.add_edge(user, host, action=row['action'], result=row['result'])

    return G





# ----------------------------

# Simple detection rules

# ----------------------------

def detect_credential_stuffing(df):

    detections = []

    failed = df[(df["action"] == "login") & (df["result"] == "failure")]

    for ip, group in failed.groupby("src_ip"):

        if group["user"].nunique() > 5:

            detections.append(f"Credential Stuffing from {ip}")

    return detections





# ----------------------------

# LLM explanation (fallback rule-based if no API key)

# ----------------------------

def explain_detection(text, api_key=None, model="gpt-4o-mini"):

    if OPENAI_AVAILABLE and (api_key or os.getenv("OPENAI_API_KEY")):

        openai.api_key = api_key or os.getenv("OPENAI_API_KEY")

        try:

            resp = openai.ChatCompletion.create(

                model=model,

                messages=[

                    {"role": "system", "content": "You are a SOC assistant."},

                    {"role": "user", "content": f"Explain this detection: {text}"}

                ],

                max_tokens=200

            )

            return resp["choices"][0]["message"]["content"]

        except Exception as e:

            return f"LLM error: {e}"

    else:

        return f"Rule-based explanation: {text} likely indicates brute-force or credential-stuffing. Mitigate by blocking IP, enabling MFA, and monitoring logs."





# ----------------------------

# Visualization with pyvis

# ----------------------------

def visualize_graph(G):

    net = Network(height="500px", width="100%", bgcolor="#0f172a", font_color="white", directed=True)

    for node, data in G.nodes(data=True):

        color = "#60a5fa" if data["ntype"] == "ip" else "#34d399" if data["ntype"] == "user" else "#fbbf24"

        net.add_node(node, label=data["label"], color=color)

    for u, v, d in G.edges(data=True):

        net.add_edge(u, v, label=d.get("action", ""))

    net.save_graph("graph.html")

    with open("graph.html", "r", encoding="utf-8") as f:

        html = f.read()

    components.html(html, height=550, scrolling=True)





# ----------------------------

# Streamlit app

# ----------------------------

def main():

    st.set_page_config(page_title="Cyber Threat Hunting", layout="wide")

    st.title("Cyber Threat Hunting & Attack Mapping - Designed By Randy Singh from KNet Consulting Group.")



    # Sidebar

    with st.sidebar:

        st.header("Options")

        api_key = st.text_input("OpenAI API Key (optional)", type="password")



        if st.button("Generate Sample Data"):

            st.session_state["df"] = generate_sample_data()



        uploaded = st.file_uploader("Upload CSV/JSON/Excel", type=["csv", "json", "xlsx"])

        if uploaded:

            if uploaded.name.endswith(".csv"):

                st.session_state["df"] = pd.read_csv(uploaded)

            elif uploaded.name.endswith(".json"):

                st.session_state["df"] = pd.read_json(uploaded)

            else:

                st.session_state["df"] = pd.read_excel(uploaded)



        if st.button("Clear Data"):

            st.session_state["df"] = None



    # Main panel

    df = st.session_state.get("df")

    if df is not None:

        st.subheader("Raw Events")

        st.dataframe(df.head(20))



        G = build_graph(df)

        st.subheader("Attack Graph")

        visualize_graph(G)



        st.subheader("Detections")

        detections = detect_credential_stuffing(df)

        if detections:

            for det in detections:

                st.write(f"- {det}")

                if st.button(f"Explain: {det}"):

                    st.info(explain_detection(det, api_key=api_key))

        else:

            st.success("No anomalies detected.")



        # Download options

        st.subheader("Download Data")

        st.download_button("Download as CSV", df.to_csv(index=False).encode("utf-8"), "events.csv")

        st.download_button("Download as JSON", df.to_json(orient="records").encode("utf-8"), "events.json")

    else:

        st.info("Generate or upload data to start threat hunting.")





if __name__ == "__main__":


    main()
