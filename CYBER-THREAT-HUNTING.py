# THREAT HUNTING APPLICATION

# CYBER-THREAT-HUNTING.py
# app.py

import streamlit as st

import pandas as pd, json, io, os, datetime, random

from typing import List, Dict, Any



st.set_page_config(page_title="Agentic AI: Automated Threat Hunting", layout="wide")



# -- Styles for professional look --

st.markdown("""

    <style>

        .main {background-color: #f7f9fb;}

        .big-title {font-size:28px; font-weight:700; color:#0b4b6f;}

        .sub-title {font-size:14px; color:#2b6f8a;}

        .btn-primary {background: linear-gradient(90deg,#0066cc,#0099ff); color:white; padding:8px 14px; border-radius:8px; border:none;}

        .btn-danger {background: linear-gradient(90deg,#cc0000,#ff3300); color:white; padding:8px 14px; border-radius:8px; border:none;}

        .btn-neutral {background: linear-gradient(90deg,#6c757d,#adb5bd); color:white; padding:8px 14px; border-radius:8px; border:none;}

        .hr {height:1px; background:#e6eef6; margin:12px 0;}

        .small {font-size:12px; color:#6b7280;}

    </style>

""", unsafe_allow_html=True)



st.markdown('<div class="big-title">Agentic AI — Automated Threat Hunting (Demo)</div>', unsafe_allow_html=True)

st.markdown('<div class="sub-title">Monitors logs, runs anomaly detection, and correlates threat intel (simulated).</div>', unsafe_allow_html=True)

st.write("")



# Initialize session state

if "df" not in st.session_state:

    st.session_state.df = pd.DataFrame()

if "results" not in st.session_state:

    st.session_state.results = None



# Helper: default path for sample file if user places it in same folder

DEFAULT_SAMPLE = os.path.join(os.getcwd(), "sample_50_records.json")



col1, col2, col3 = st.columns([1,2,1])

with col1:

    if st.button("🔄 Generate 50 Sample Records", key="gen50"):

        sample_path = DEFAULT_SAMPLE

        try:

            with open(sample_path, "r") as f:

                data = json.load(f)

            st.session_state.df = pd.DataFrame(data)

            st.success("Loaded 50 sample records into the workspace.")

        except Exception as e:

            st.error(f"Could not load sample file from {sample_path}: {e}")



with col2:

    if st.button("➕ Generate New Data (10 records)", key="gen_new"):

        # Append synthetic new records

        start = int(st.session_state.df["id"].max()) + 1 if (not st.session_state.df.empty and "id" in st.session_state.df.columns) else 1

        new = []

        for i in range(start, start+10):

            now = datetime.datetime.datetime.utcnow().isoformat() + "Z"

            rec = {

                "id": int(i),

                "timestamp": now,

                "source_ip": f"{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}",

                "dest_ip": f"{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}",

                "dest_port": int(random.choice([22,80,443,8080,53,3389, random.randint(1024,65535)])),

                "bytes_sent": int(random.randint(40,2000000)),

                "bytes_received": int(random.randint(20,1500000)),

                "user_agent": random.choice([ "Mozilla/5.0", "curl/7.68.0", "python-requests/2.28.1" ]),

                "event_type": random.choice(["connection","http_request","dns_query","ssh_login","failed_login","file_access"]),

                "threat_score": int(random.randint(0,100)),

                "notes": "",

                "shodan_info": {}

            }

            new.append(rec)

        new_df = pd.DataFrame(new)

        if st.session_state.df.empty:

            st.session_state.df = new_df

        else:

            st.session_state.df = pd.concat([st.session_state.df, new_df], ignore_index=True)

        st.success("Generated 10 new records and appended.")



with col3:

    if st.button("🗑️ Clear Data", key="clear"):

        st.session_state.df = pd.DataFrame()

        st.session_state.results = None

        st.success("Cleared workspace data and results.")



st.write("---")



# Upload area

st.markdown("### Upload your logs (JSON, CSV, TXT)")

uploaded = st.file_uploader("Upload a JSON/CSV/TXT file containing event logs", type=["json","csv","txt"])

if uploaded is not None:

    try:

        content = uploaded.getvalue().decode("utf-8")

        if uploaded.name.endswith(".json"):

            data = json.loads(content)

            df = pd.DataFrame(data)

        elif uploaded.name.endswith(".csv"):

            df = pd.read_csv(io.StringIO(content))

        else:

            # try to parse line-delimited JSON or simple CSV

            try:

                lines = content.strip().splitlines()

                parsed = [json.loads(l) for l in lines if l.strip()]

                df = pd.DataFrame(parsed)

            except Exception:

                df = pd.read_csv(io.StringIO(content))

        st.session_state.df = df

        st.success(f"Uploaded and loaded {uploaded.name} ({len(st.session_state.df)} records).")

    except Exception as e:

        st.error(f"Failed to parse upload: {e}")



# Display and controls for results

st.markdown("### Workspace — Data Preview & Controls")

if st.session_state.df.empty:

    st.info("No records loaded. Use 'Generate 50 Sample Records', upload a file, or generate new data.")

else:

    st.write(f"Showing {len(st.session_state.df)} records.")

    st.dataframe(st.session_state.df.head(200))



# Agentic Threat Hunting (simulated)

st.markdown("### Run Agentic Threat Hunt (Simulated)")

threat_col, action_col = st.columns(2)

threshold = threat_col.slider("Threat score threshold", min_value=0, max_value=100, value=60)

detect_port_scan = threat_col.checkbox("Flag unusual ports (e.g., many unique destination ports per source)", value=True)

run_btn = action_col.button("🕵️ Run Threat Hunt", key="run_hunt", help="Agent will analyze data, flag anomalies, and annotate records.")



def run_threat_hunt(df: pd.DataFrame, threshold: int, flag_ports: bool) -> pd.DataFrame:

    df = df.copy()

    # Basic anomaly rules

    df["anomaly"] = False

    df["anomaly_reasons"] = ""

    # rule 1: threat_score above threshold

    if "threat_score" in df.columns:

        high = df["threat_score"].fillna(0).astype(float) >= float(threshold)

        df.loc[high, "anomaly"] = True

        df.loc[high, "anomaly_reasons"] = df.loc[high, "anomaly_reasons"].astype(str) + "High threat_score; "

    # rule 2: suspicious ports

    if flag_ports and "dest_port" in df.columns:

        # cast safely

        try:

            df["dest_port"] = df["dest_port"].fillna(0).astype(int)

        except Exception:

            df["dest_port"] = df["dest_port"].apply(lambda x: int(float(x)) if x not in (None, "") else 0)

        suspicious = df["dest_port"].isin([22,3389]) | (df["dest_port"] > 49152)

        df.loc[suspicious, "anomaly"] = True

        df.loc[suspicious, "anomaly_reasons"] = df.loc[suspicious, "anomaly_reasons"].astype(str) + "Suspicious dest_port; "

    # rule 3: large bytes transfer

    if "bytes_sent" in df.columns and "bytes_received" in df.columns:

        big = (pd.to_numeric(df["bytes_sent"].fillna(0), errors="coerce").fillna(0) + pd.to_numeric(df["bytes_received"].fillna(0), errors="coerce").fillna(0)) > 1000000

        df.loc[big, "anomaly"] = True

        df.loc[big, "anomaly_reasons"] = df.loc[big, "anomaly_reasons"].astype(str) + "Large bytes transfer; "

    # basic correlation: flag sources that connected to many unique dest_ips

    if "source_ip" in df.columns and "dest_ip" in df.columns:

        counts = df.groupby("source_ip")["dest_ip"].nunique()

        # threshold = 10 unique dest IPs

        risky_sources = counts[counts >= 10].index.tolist()

        df.loc[df["source_ip"].isin(risky_sources), "anomaly"] = True

        df.loc[df["source_ip"].isin(risky_sources), "anomaly_reasons"] = df.loc[df["source_ip"].isin(risky_sources), "anomaly_reasons"].astype(str) + "High dest_ip diversity; "

    # final: convert bools to explicit types

    df["anomaly"] = df["anomaly"].astype(bool)

    return df



if run_btn:

    if st.session_state.df.empty:

        st.warning("No data to analyze.")

    else:

        result_df = run_threat_hunt(st.session_state.df, threshold, detect_port_scan)

        st.session_state.results = result_df

        n_anom = int(result_df["anomaly"].sum()) if "anomaly" in result_df.columns else 0

        st.success(f"Threat hunt completed. Found {n_anom} anomalous records.")

        if n_anom > 0:

            st.dataframe(result_df[result_df["anomaly"]].head(500))

        else:

            st.info("No anomalies found with current rules/threshold.")



# Save/export results

st.markdown("### Save / Export")

save_col, download_col = st.columns(2)

with save_col:

    out_name = st.text_input("Output file name (json)", value="threat_hunt_results.json")

    if st.button("💾 Save results to file", key="save"):

        if st.session_state.results is None:

            st.warning("No results to save. Run the agent first.")

        else:

            try:

                path = os.path.join(os.getcwd(), out_name)

                st.session_state.results.to_json(path, orient="records", indent=2)

                st.success(f"Saved results to {path}")

            except Exception as e:

                st.error(f"Failed to save: {e}")



with download_col:

    if st.session_state.results is not None:

        st.download_button("⬇️ Download Results (JSON)", data=st.session_state.results.to_json(orient="records", indent=2), file_name="threat_hunt_results.json", mime="application/json")

    else:

        st.info("Run the agent to enable download.")



st.write("---")

st.markdown("#### Notes & Next Steps")

st.markdown("""

- This demo simulates an agentic threat hunting workflow: loading logs, running rule-based anomaly detection, correlating events, and exporting results.\n

- For real deployments: integrate with SIEM (Elastic/ELK), threat intel feeds (MISP, AlienVault OTX), and orchestration (run firewall rules, create SOC tickets). Use secure API keys and audit all actions.\n

- Optional: enable Shodan/OpenAI integrations by providing API keys and extending the `run_threat_hunt` function to call external services. When enabling external actions (like modifying firewall rules), always include manual approval gates in production.

""")