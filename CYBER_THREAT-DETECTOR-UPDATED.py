# TODAY-4

# THIS CYBER-THREAT-DETECTOR IS DESIGNED BY RANDY SINGH FROM KNet CONSULTING GROUP.
# python
# Cyber-Threat-Detection.py

import streamlit as st
import pandas as pd, json, io, os, random
from datetime import datetime
import matplotlib.pyplot as plt

# ---------------------------
# Streamlit Page Config
# ---------------------------
st.set_page_config(
    page_title="Agentic AI: Automated Threat Hunting Designed By Randy Singh from KNet consulting Group.",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# Styles
# ---------------------------
st.markdown("""
    <style>
        .main {background-color: #f4f9fc;}
        .big-title {font-size:30px; font-weight:700; color:#003366; padding:10px;}
        .sub-title {font-size:15px; color:#225577; padding-left:10px;}
        .stButton>button {
            border-radius: 12px;
            font-weight:600;
            padding:10px 20px;
            border:none;
        }
        .stButton>button:hover {opacity:0.9;}
        div.stDownloadButton > button {
            background: linear-gradient(90deg,#28a745,#5cd65c);
            color:white; border-radius:8px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">Agentic AI — Automated Threat Hunting - Designed By Randy Singh KNet Consulting Group.', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Monitors logs, runs anomaly detection, and correlates threat intel (simulated).</div>', unsafe_allow_html=True)
st.write("")

# ---------------------------
# Session State Init
# ---------------------------
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()
if "results" not in st.session_state:
    st.session_state.results = None

# ---------------------------
# Helper: Generate synthetic logs
# ---------------------------
def generate_records(n=10, start_id=1):
    records = []
    for i in range(start_id, start_id+n):
        now = datetime.utcnow().isoformat() + "Z"
        rec = {
            "id": int(i),
            "timestamp": now,
            "source_ip": f"{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}",
            "dest_ip": f"{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}",
            "dest_port": int(random.choice([22,80,443,8080,53,3389, random.randint(1024,65535)])),
            "bytes_sent": int(random.randint(40,2000000)),
            "bytes_received": int(random.randint(20,1500000)),
            "user_agent": random.choice(["Mozilla/5.0", "curl/7.68.0", "python-requests/2.28.1"]),
            "event_type": random.choice(["connection","http_request","dns_query","ssh_login","failed_login","file_access"]),
            "threat_score": int(random.randint(0,100)),
            "notes": "",
            "shodan_info": {}
        }
        records.append(rec)
    return pd.DataFrame(records)

# ---------------------------
# Controls
# ---------------------------
col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.button("🔄 Generate 50 Sample Records", key="gen50"):
        new_df = generate_records(50, start_id=1)
        st.session_state.df = new_df
        st.success("Generated 50 sample records into the workspace.")

with col2:
    if st.button("➕ Generate New Data (10 records)", key="gen_new"):
        start = int(st.session_state.df["id"].max()) + 1 if (not st.session_state.df.empty and "id" in st.session_state.df.columns) else 1
        new_df = generate_records(10, start_id=start)
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

# ---------------------------
# Upload area
# ---------------------------
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

# ---------------------------
# Workspace preview
# ---------------------------
st.markdown("### Workspace — Data Preview & Controls")
if st.session_state.df.empty:
    st.info("No records loaded. Use 'Generate 50 Sample Records', upload a file, or generate new data.")
else:
    st.write(f"Showing {len(st.session_state.df)} records.")
    st.dataframe(st.session_state.df.head(200))

# ---------------------------
# Threat Hunting Function
# ---------------------------
def run_threat_hunt(df: pd.DataFrame, threshold: int, flag_ports: bool) -> pd.DataFrame:
    df = df.copy()
    df["anomaly"] = False
    df["anomaly_reasons"] = ""

    # Rule 1: threat_score above threshold
    if "threat_score" in df.columns:
        high = df["threat_score"].fillna(0).astype(float) >= float(threshold)
        df.loc[high, "anomaly"] = True
        df.loc[high, "anomaly_reasons"] += "High threat_score; "

    # Rule 2: suspicious ports
    if flag_ports and "dest_port" in df.columns:
        df["dest_port"] = pd.to_numeric(df["dest_port"], errors="coerce").fillna(0).astype(int)
        suspicious = df["dest_port"].isin([22,3389]) | (df["dest_port"] > 49152)
        df.loc[suspicious, "anomaly"] = True
        df.loc[suspicious, "anomaly_reasons"] += "Suspicious dest_port; "

    # Rule 3: large bytes transfer
    if "bytes_sent" in df.columns and "bytes_received" in df.columns:
        big = (pd.to_numeric(df["bytes_sent"], errors="coerce").fillna(0) +
               pd.to_numeric(df["bytes_received"], errors="coerce").fillna(0)) > 1000000
        df.loc[big, "anomaly"] = True
        df.loc[big, "anomaly_reasons"] += "Large bytes transfer; "

    # Rule 4: high dest_ip diversity
    if "source_ip" in df.columns and "dest_ip" in df.columns:
        counts = df.groupby("source_ip")["dest_ip"].nunique()
        risky_sources = counts[counts >= 10].index.tolist()
        df.loc[df["source_ip"].isin(risky_sources), "anomaly"] = True
        df.loc[df["source_ip"].isin(risky_sources), "anomaly_reasons"] += "High dest_ip diversity; "

    return df

# ---------------------------
# Threat Hunt UI
# ---------------------------
st.markdown("### Run Agentic Threat Hunt (Simulated)")
threat_col, action_col = st.columns(2)
threshold = threat_col.slider("Threat score threshold", min_value=0, max_value=100, value=60)
detect_port_scan = threat_col.checkbox("Flag unusual ports", value=True)
run_btn = action_col.button("🕵️ Run Threat Hunt", key="run_hunt")

if run_btn:
    if st.session_state.df.empty:
        st.warning("No data to analyze.")
    else:
        result_df = run_threat_hunt(st.session_state.df, threshold, detect_port_scan)
        st.session_state.results = result_df
        n_anom = int(result_df["anomaly"].sum())
        st.success(f"Threat hunt completed. Found {n_anom} anomalous records.")
        if n_anom > 0:
            st.dataframe(result_df[result_df["anomaly"]].head(500))
        else:
            st.info("No anomalies found with current rules/threshold.")

# ---------------------------
# Charts Dashboard
# ---------------------------
if st.session_state.results is not None and not st.session_state.results.empty:
    st.markdown("### 📊 Threat Dashboard")

    df = st.session_state.results

    chart1, chart2, chart3 = st.columns(3)

    # Pie: anomalies vs normal
    with chart1:
        labels = ["Anomalies", "Normal"]
        values = [df["anomaly"].sum(), (~df["anomaly"]).sum()]
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
        ax.set_title("Anomaly Ratio")
        st.pyplot(fig)

    # Pie: anomalies by reason
    with chart2:
        reasons = df.loc[df["anomaly"], "anomaly_reasons"].str.split(";").explode().str.strip()
        reasons = reasons[reasons != ""]
        reason_counts = reasons.value_counts().head(5)
        fig, ax = plt.subplots()
        ax.pie(reason_counts, labels=reason_counts.index, autopct="%1.1f%%", startangle=90)
        ax.set_title("Top Anomaly Reasons")
        st.pyplot(fig)

    # Line chart: threat scores over time
    with chart3:
        if "timestamp" in df.columns and "threat_score" in df.columns:
            df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
            df_sorted = df.sort_values("timestamp")
            fig, ax = plt.subplots()
            ax.plot(df_sorted["timestamp"], df_sorted["threat_score"], marker="o", linestyle="-")
            ax.set_title("Threat Scores Over Time")
            ax.set_ylabel("Threat Score")
            ax.set_xlabel("Time")
            plt.xticks(rotation=45)
            st.pyplot(fig)

    # Bar chart: event type distribution
    st.markdown("### Event Type Distribution")
    if "event_type" in df.columns:
        fig, ax = plt.subplots()
        df["event_type"].value_counts().plot(kind="bar", ax=ax)
        ax.set_title("Events by Type")
        ax.set_ylabel("Count")
        st.pyplot(fig)

# ---------------------------
# Save / Export
# ---------------------------
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
        st.download_button("⬇️ Download Results (JSON)",
                           data=st.session_state.results.to_json(orient="records", indent=2),
                           file_name="threat_hunt_results.json",
                           mime="application/json")
    else:
        st.info("Run the agent to enable download.")

st.write("---")
st.markdown("#### Notes & Next Steps")
st.markdown("""
# This demo Designed By Randy Singh from KNet consulting Group Simulates an Agentic Threat Hunting Workflow: loading logs, running rule-based anomaly detection, correlating events, and exporting results.

# For real deployments: integrate with SIEM (Elastic/ELK), threat intel feeds (MISP, AlienVault OTX), and orchestration (run firewall rules, create SOC tickets).
# """)



