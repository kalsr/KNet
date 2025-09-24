

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
import json, random, os
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import io

# Optional OpenAI
try:
    import openai
    OPENAI_AVAILABLE = True
except Exception:
    OPENAI_AVAILABLE = False


# ----------------------------
# Original: Synthetic log generator
# ----------------------------
def generate_sample_data(n=200):
    users = [f"user{i}" for i in range(1, 11)]
    hosts = [f"host{i}.corp.local" for i in range(1, 6)]
    ips = [f"10.0.{i}.{j}" for i in range(1, 3) for j in range(1, 100)]
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
# Original detection
# ----------------------------
def detect_credential_stuffing(df):
    detections = []
    failed = df[(df["action"] == "login") & (df["result"] == "failure")]
    for ip, group in failed.groupby("src_ip"):
        if group["user"].nunique() > 5:
            detections.append(f"Credential Stuffing from {ip}")
    return detections


# ----------------------------
# Explanations
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
# Original visualization
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
# Helpers: new detections, MITRE mappings, scenarios
# ----------------------------
def _ensure_timestamp(df):
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    return df


def detect_bruteforce_user(df, threshold_failures=6, window_minutes=15):
    df = _ensure_timestamp(df)
    detections = []
    failed = df[(df["action"] == "login") & (df["result"] == "failure")]
    for user, group in failed.groupby("user"):
        group = group.sort_values("timestamp")
        for i in range(len(group)):
            start = group.iloc[i]["timestamp"]
            end = start + pd.Timedelta(minutes=window_minutes)
            subset = group[(group["timestamp"] >= start) & (group["timestamp"] <= end)]
            if len(subset) >= threshold_failures:
                detections.append(f"Brute Force Attack on {user} ({len(subset)} failures in {window_minutes}m)")
                break
    return detections


def detect_data_exfil(df, threshold=8):
    df = _ensure_timestamp(df)
    detections = []
    files = df[df["action"] == "file_access"]
    for user, group in files.groupby("user"):
        if len(group) > threshold:
            detections.append(f"Data Exfiltration suspected for {user} ({len(group)} file accesses)")
    return detections


MITRE_MAP = {
    "credential_stuffing": ("TA0006 - Credential Access", "T1110 - Brute Force"),
    "brute_force": ("TA0006 - Credential Access", "T1110 - Brute Force"),
    "data_exfil": ("TA0010 - Exfiltration", "T1020 - Automated Exfiltration"),
}


def targeted_anomaly(df, kind="credential"):
    """Insert anomalies deliberately for demo."""
    ts = pd.Timestamp.utcnow()
    extra = []
    if kind == "credential":
        for i in range(12):
            extra.append({
                "timestamp": (ts + timedelta(seconds=i*10)).isoformat(),
                "src_ip": "10.0.99.99",
                "dest_host": "host1.corp.local",
                "user": f"user{i%6}",
                "action": "login",
                "result": "failure"
            })
    elif kind == "exfil":
        for i in range(12):
            extra.append({
                "timestamp": (ts + timedelta(seconds=i*20)).isoformat(),
                "src_ip": "10.0.42.42",
                "dest_host": f"host{i%3+1}.corp.local",
                "user": "userX",
                "action": "file_access",
                "result": "success"
            })
    return pd.concat([df, pd.DataFrame(extra)], ignore_index=True)


# ----------------------------
# Streamlit app
# ----------------------------
def main():
    st.set_page_config(page_title="Cyber Threat Hunting - Designed by Randy Singh From KNet Consulting Group", layout="wide")

    # theme toggle
    theme = st.sidebar.radio("Theme", ["Dark", "Light"])
    if theme == "Dark":
        st.markdown("""<style>body{background-color:#0f172a; color:white;}</style>""", unsafe_allow_html=True)

    st.title("Cyber Threat Hunting & Attack Mapping")
    st.caption("Designed by Randy Singh – KNet Consulting Group")

    if "df" not in st.session_state:
        st.session_state["df"] = None

    # Sidebar controls
    st.sidebar.subheader("Data Options")
    n_samples = st.sidebar.slider("Generate Records", 50, 200, 100, 10)
    if st.sidebar.button("Generate Sample Data", help="Creates synthetic dataset"):
        st.session_state["df"] = generate_sample_data(n=n_samples)

    if st.sidebar.button("Insert Credential Stuffing Anomaly"):
        if st.session_state["df"] is not None:
            st.session_state["df"] = targeted_anomaly(st.session_state["df"], "credential")

    if st.sidebar.button("Insert Data Exfiltration Anomaly"):
        if st.session_state["df"] is not None:
            st.session_state["df"] = targeted_anomaly(st.session_state["df"], "exfil")

    # Demo scenario
    if st.sidebar.button("Load Demo Scenario: Ransomware Exfil"):
        df = generate_sample_data(120)
        df = targeted_anomaly(df, "exfil")
        st.session_state["df"] = df

    # Main
    df = st.session_state["df"]
    if df is None:
        st.info("Generate or load data to begin analysis.")
        return

    df = _ensure_timestamp(df)
    st.dataframe(df.head(30))

    # Charts
    st.subheader("Event Distributions")
    col1, col2 = st.columns(2)

    with col1:
        counts = df["action"].value_counts()
        fig, ax = plt.subplots()
        ax.pie(counts, labels=counts.index, autopct="%1.1f%%")
        ax.set_title("Actions")
        st.pyplot(fig)
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        st.download_button("Download Actions Chart", buf.getvalue(), "actions.png")

    with col2:
        results = df["result"].value_counts()
        fig2, ax2 = plt.subplots()
        ax2.bar(results.index, results.values, color="tomato")
        ax2.set_title("Results")
        st.pyplot(fig2)
        buf2 = io.BytesIO()
        fig2.savefig(buf2, format="png")
        st.download_button("Download Results Chart", buf2.getvalue(), "results.png")

    # Graph
    st.subheader("Attack Graph")
    G = build_graph(df)
    visualize_graph(G)

    # Detections
    st.subheader("Detections")
    detections = []
    for d in detect_credential_stuffing(df):
        detections.append(("credential_stuffing", d))
    for d in detect_bruteforce_user(df):
        detections.append(("brute_force", d))
    for d in detect_data_exfil(df):
        detections.append(("data_exfil", d))

    if not detections:
        st.success("No anomalies detected ")
    else:
        for i, (dtype, dtext) in enumerate(detections):
            tactic, technique = MITRE_MAP.get(dtype, ("Unknown", "Unknown"))
            with st.expander(f"[{dtype.upper()}] {dtext}"):
                st.markdown(f"**MITRE ATT&CK Mapping:** {tactic} | {technique}")
                if st.button(f"Explain {i}", key=f"expl{i}"):
                    st.info(explain_detection(dtext))
                st.markdown("**Mitigation Playbook:**")
                if dtype == "credential_stuffing":
                    st.write("- Block IPs, enable MFA, monitor identity systems.")
                elif dtype == "brute_force":
                    st.write("- Lock accounts, enforce strong password policy, enable rate limiting.")
                elif dtype == "data_exfil":
                    st.write("- Isolate host, monitor outbound traffic, preserve forensic evidence.")


if __name__ == "__main__":
    main()
