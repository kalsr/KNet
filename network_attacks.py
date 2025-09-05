
## Complete Code: `network_attacks.py`
# THIS PROGRAM IS DEVELOPED BY RANDY SINGH FROM KNet CONSULTING GROUP.

# python
# NETWORK ATTACKS WITH SUMMARY OF ATTACKS
# Streamlit App - Designed by Randy Singh (KNet Consulting Group)

import random
import time
import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.set_page_config(page_title="Network Attacks Simulator", layout="wide")
st.title("Network Attacks - Threat Analyser")
st.caption("Designed by Randy Singh – KNet Consulting Group")

# -------------------------------
# Attack Data
# -------------------------------
attack_types = [
    {"name": "SQL Injection", "reason": "User input is not properly sanitized",
     "explanation": "Injects malicious SQL code to access/modify data"},
    {"name": "Cross-Site Scripting (XSS)", "reason": "User input is not properly sanitized",
     "explanation": "Injects malicious JavaScript to steal data/take control of session"},
    {"name": "Cross-Site Request Forgery (CSRF)", "reason": "Lack of token-based authentication",
     "explanation": "Tricks user into performing unintended actions"},
    {"name": "Path Traversal", "reason": "Improper file path validation",
     "explanation": "Accesses sensitive files by manipulating paths"},
    {"name": "Command Injection", "reason": "User input is not properly sanitized",
     "explanation": "Injects malicious system commands"},
    {"name": "Remote File Inclusion (RFI)", "reason": "Improper file inclusion validation",
     "explanation": "Includes malicious remote files"},
    {"name": "Local File Inclusion (LFI)", "reason": "Improper file inclusion validation",
     "explanation": "Includes malicious local files"},
]

http_methods = ["GET", "POST", "PUT", "DELETE"]
parameter_types = ["URL", "Cookie", "Header", "Body"]

# -------------------------------
# Generate Logs
# -------------------------------
def generate_logs(normal_count=50, attack_count=10):
    logs = []
    # Normal logs
    for _ in range(normal_count):
        logs.append({
            "timestamp": int(time.time()),
            "method": random.choice(http_methods),
            "param": random.choice(parameter_types),
            "event": "Normal Request"
        })
    # Attack logs
    attack_summary = {}
    for _ in range(attack_count):
        attack = random.choice(attack_types)
        log_entry = {
            "timestamp": int(time.time()),
            "method": random.choice(http_methods),
            "param": random.choice(parameter_types),
            "event": f"{attack['name']} Attack"
        }
        logs.append(log_entry)

        attack_summary.setdefault(attack["name"], {
            "count": 0, "reason": attack["reason"], "explanation": attack["explanation"]
        })
        attack_summary[attack["name"]]["count"] += 1

    return logs, attack_summary

# -------------------------------
# Convert to TXT
# -------------------------------
def dataframe_to_txt(df):
    lines = []
    for _, row in df.iterrows():
        lines.append(" | ".join([f"{col}: {row[col]}" for col in df.columns]))
    return "\n".join(lines)

# -------------------------------
# File Loader (CSV, JSON, TXT)
# -------------------------------
def load_uploaded_file(uploaded_file):
    if uploaded_file is None:
        return None, None
    try:
        df = None
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".json"):
            df = pd.read_json(uploaded_file)
        elif uploaded_file.name.endswith(".txt"):
            lines = uploaded_file.read().decode("utf-8").splitlines()
            records = []
            for line in lines:
                parts = line.split("-")
                if len(parts) == 4:
                    records.append({
                        "timestamp": parts[0].strip(),
                        "method": parts[1].strip(),
                        "param": parts[2].strip(),
                        "event": parts[3].strip()
                    })
            df = pd.DataFrame(records)

        if df is None or df.empty:
            return None, None

        # Build attack summary from uploaded logs
        summary = {}
        for _, row in df.iterrows():
            event = str(row.get("event", ""))
            for atk in attack_types:
                if atk["name"] in event:
                    summary.setdefault(atk["name"], {
                        "count": 0,
                        "reason": atk["reason"],
                        "explanation": atk["explanation"]
                    })
                    summary[atk["name"]]["count"] += 1

        summary_df = pd.DataFrame([
            {"Attack": k, "Occurrences": v["count"], "Reason": v["reason"], "Explanation": v["explanation"]}
            for k, v in summary.items()
        ])

        return df, summary_df

    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None, None

# -------------------------------
# Session State Init
# -------------------------------
if "df" not in st.session_state:
    st.session_state.df = None
if "summary_df" not in st.session_state:
    st.session_state.summary_df = None

# -------------------------------
# Sidebar Controls
# -------------------------------
st.sidebar.header("⚙️ Controls")
normal_count = st.sidebar.slider("Normal Requests", 20, 100, 50, 5)
attack_count = st.sidebar.slider("Attack Events", 5, 30, 10, 1)

uploaded_file = st.sidebar.file_uploader("Upload Real Log File (CSV, JSON, TXT)", type=["csv", "json", "txt"])

if st.sidebar.button("Run Analyser"):
    logs, attack_summary = generate_logs(normal_count, attack_count)
    st.session_state.df = pd.DataFrame(logs)
    st.session_state.summary_df = pd.DataFrame([
        {"Attack": k, "Occurrences": v["count"], "Reason": v["reason"], "Explanation": v["explanation"]}
        for k, v in attack_summary.items()
    ])

if uploaded_file:
    df, summary_df = load_uploaded_file(uploaded_log_file)
    if df is not None:
        st.session_state.df = df
        st.session_state.summary_df = summary_df

# Clear simulation
if st.sidebar.button("Clear Analyser"):
    st.session_state.df = None
    st.session_state.summary_df = None

# Refresh page
if st.sidebar.button("Refresh Analyser"):
    st.session_state.clear()
    st.experimental_rerun()

# -------------------------------
# Main UI
# -------------------------------
if st.session_state.df is not None:
    st.subheader("Logs")
    st.dataframe(st.session_state.df, use_container_width=True, height=400)

    if st.session_state.summary_df is not None and not st.session_state.summary_df.empty:
        st.subheader("Attack Summary")
        st.dataframe(st.session_state.summary_df, use_container_width=True)

        # Charts
        st.subheader("📈 Visual Analysis")
        col1, col2 = st.columns(2)

        with col1:
            bar_fig = px.bar(st.session_state.summary_df, x="Attack", y="Occurrences",
                             color="Attack", title="Attack Counts", text="Occurrences")
            bar_fig.update_traces(textposition="outside")
            st.plotly_chart(bar_fig, use_container_width=True)

        with col2:
            pie_fig = px.pie(st.session_state.summary_df, names="Attack", values="Occurrences",
                             title="Attack Distribution (%)")
            st.plotly_chart(pie_fig, use_container_width=True)

        # Key Insights
        st.subheader("Key Insights")
        top_attack = st.session_state.summary_df.sort_values("Occurrences", ascending=False).iloc[0]
        st.success(f" Most Frequent Attack: {top_attack['Attack']} "
                   f"({top_attack['Occurrences']} times)\n\n"
                   f"Reason: {top_attack.get('Reason','-')}\n\n"
                   f"Explanation: {top_attack.get('Explanation','-')}")

        # Downloads
        st.subheader("Downloads")
        df = st.session_state.df
        summary_df = st.session_state.summary_df

        st.download_button("Download Logs (CSV)", df.to_csv(index=False), "network_logs.csv", "text/csv")
        st.download_button("Download Logs (JSON)", df.to_json(orient="records", indent=2), "network_logs.json", "application/json")
        st.download_button("Download Logs (TXT)", dataframe_to_txt(df), "network_logs.txt", "text/plain")

        st.download_button("Download Attack Summary (CSV)", summary_df.to_csv(index=False), "attack_summary.csv", "text/csv")
        st.download_button("Download Attack Summary (JSON)", summary_df.to_json(orient="records", indent=2), "attack_summary.json", "application/json")
        st.download_button("Download Attack Summary (TXT)", dataframe_to_txt(summary_df), "attack_summary.txt", "text/plain")
else:
    st.info("👈 PLEASE USE THE SIDE BAR TO RUN SIMULATION OR UPLOAD LOG FILE.")


