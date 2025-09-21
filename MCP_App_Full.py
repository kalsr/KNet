

# mcp_app_full.py
# THIS APPLICATION IS DESIGNED & DEVELOPED BY RANDY SINGH FROM KNet CONSULTING.
# MCP — Model Context Protocol (Streamlit app with DB, trend charts, settings, and logo)
# Run: streamlit run mcp_app_full.py

import streamlit as st
import pandas as pd
import numpy as np
import json
import io
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
from pathlib import Path

# ---------- Configuration ----------
DATA_DIR = Path("./data")
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "mcp_store.db"
LOGO_PATH = "Kalsnetlogo.png"  # <- Put your logo image in the same directory

st.set_page_config(page_title="MCP — Model Context Protocol", layout="wide")

# ---------- DB Setup ----------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS context_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ts TEXT,
        event TEXT,
        payload TEXT
    )
    """)
    conn.commit()
    conn.close()

def append_event(event, payload=None):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO context_events (ts, event, payload) VALUES (?, ?, ?)",
                (datetime.utcnow().isoformat()+"Z", event, json.dumps(payload or {})))
    conn.commit()
    conn.close()

def load_events(limit=200):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM context_events ORDER BY id DESC LIMIT ?", conn, params=(limit,))
    conn.close()
    return df

init_db()

# ---------- Styling ----------
st.markdown(
    """
    <style>
    .mcp-header { font-size:28px; font-weight:800; margin-bottom: 4px; }
    .mcp-sub { color: #6c757d; margin-bottom: 14px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Helpers ----------
def generate_sample_data(n=50, seed=None):
    rng = np.random.default_rng(int(seed) if (seed and str(seed).isdigit()) else None)
    categories = ["Normal", "Anomaly", "Warning", "Info"]
    rows = []
    ts = datetime.utcnow()
    for i in range(1, n+1):
        r = {
            "id": i,
            "timestamp": ts.isoformat()+"Z",
            "score": float(np.round(rng.uniform(0, 1), 3)),
            "category": rng.choice(categories, p=[0.6,0.1,0.2,0.1]),
            "message": rng.choice([
                "User login", "File accessed", "Process started", "Timeout error",
                "High memory usage", "Configuration change", "Health check passed", "Permission denied"
            ])
        }
        rows.append(r)
    return pd.DataFrame(rows)

def dataframe_to_csv_bytes(df):
    return df.to_csv(index=False).encode("utf-8")

def dataframe_to_json_bytes(df):
    return df.to_json(orient="records", force_ascii=False).encode("utf-8")

# ---------- MCP Handlers ----------
def anomaly_detection_pipeline(df, threshold=0.2):
    df = df.copy()
    df["anomaly_flag"] = df["score"].apply(lambda s: "ANOMALY" if float(s) < threshold else "OK")
    append_event("anomaly_detection_run", {"records": len(df), "threshold": threshold})
    return df

def policy_compliance_monitor(df):
    df = df.copy()
    def check_policy(msg):
        msg_l = str(msg).lower()
        if "permission" in msg_l or "denied" in msg_l or "config" in msg_l:
            return "VIOLATION"
        if "timeout" in msg_l or "error" in msg_l:
            return "WARNING"
        return "OK"
    df["policy_state"] = df["message"].apply(check_policy)
    append_event("policy_monitor_run", {"records": len(df)})
    return df

def model_drift_metrics(df, history=100):
    df = df.copy()
    stats = {
        "count": len(df),
        "mean_score": float(df["score"].mean()) if len(df) else None
    }
    hist = load_events(history)
    past_means = []
    for _, row in hist.iterrows():
        try:
            payload = json.loads(row["payload"])
            if "mean_score" in payload:
                past_means.append(payload["mean_score"])
        except Exception:
            continue
    if past_means:
        stats["historical_mean"] = float(np.mean(past_means))
        stats["drift_delta"] = stats["mean_score"] - stats["historical_mean"]
    append_event("drift_metrics", stats)
    return stats

def incident_triage_assistant(df, anomaly_weight=20, violation_weight=50):
    df = df.copy()
    def severity_calc(row):
        base = (1.0 - float(row["score"])) * 100
        policy_weight = violation_weight if row.get("policy_state","")=="VIOLATION" else (anomaly_weight if row.get("anomaly_flag","")=="ANOMALY" else 0)
        return base + policy_weight
    df["severity"] = df.apply(severity_calc, axis=1)
    df = df.sort_values("severity", ascending=False).reset_index(drop=True)
    append_event("incident_triage", {"records": len(df)})
    return df

# ---------- Session State ----------
if "df" not in st.session_state:
    st.session_state["df"] = generate_sample_data(50)
    append_event("sample_data_generated", {"n": 50})

if "settings" not in st.session_state:
    st.session_state["settings"] = {"anomaly_threshold": 0.2, "anomaly_weight": 20, "violation_weight": 50}

# ---------- Header with Logo ----------
col_logo, col_title = st.columns([1,4])
with col_logo:
    if Path(LOGO_PATH).exists():
        st.image(LOGO_PATH, width=80)
with col_title:
    st.markdown('<div class="mcp-header">Model Context Protocol (MCP) — Interactive Demo</div>', unsafe_allow_html=True)
    st.markdown('<div class="mcp-sub">Designed & Developed by Randy Singh @ KNet Consulting</div>', unsafe_allow_html=True)

# ---------- Tabs ----------
tabs = st.tabs(["Data", "Use Cases", "Visuals", "Drift & Export", "Settings", "Audit"])

# --- Data Tab ---
with tabs[0]:
    st.subheader("Data Management")
    n = st.number_input("Sample size", 5, 5000, 50, 5)
    seed = st.text_input("Random seed")
    if st.button("Generate Sample Data"):
        st.session_state["df"] = generate_sample_data(n, seed)
        append_event("sample_data_generated", {"n": n, "seed": seed})
        st.success(f"Generated {n} records.")

    uploaded = st.file_uploader("Upload Data (CSV/JSON)")
    if uploaded:
        try:
            if uploaded.name.endswith(".csv"):
                df = pd.read_csv(uploaded)
            else:
                df = pd.read_json(uploaded)
            st.session_state["df"] = df
            append_event("file_uploaded", {"filename": uploaded.name, "records": len(df)})
            st.success(f"Loaded {len(df)} records.")
        except Exception as e:
            st.error(f"Failed: {e}")

    st.dataframe(st.session_state["df"].head(200))

# --- Use Cases ---
with tabs[1]:
    df = st.session_state["df"]
    st.subheader("Run Use Cases")

    if st.button("Run Anomaly Detection"):
        st.session_state["df"] = anomaly_detection_pipeline(df, st.session_state["settings"]["anomaly_threshold"])
        st.success("Anomaly detection complete.")

    if st.button("Apply Policy Compliance Monitor"):
        st.session_state["df"] = policy_compliance_monitor(df)
        st.success("Policy compliance check complete.")

    if st.button("Run Incident Triage"):
        df = st.session_state["df"]
        if "policy_state" not in df.columns:
            df = policy_compliance_monitor(df)
        if "anomaly_flag" not in df.columns:
            df = anomaly_detection_pipeline(df, st.session_state["settings"]["anomaly_threshold"])
        st.session_state["df"] = incident_triage_assistant(df,
                                                           st.session_state["settings"]["anomaly_weight"],
                                                           st.session_state["settings"]["violation_weight"])
        st.dataframe(st.session_state["df"].head(20))

# --- Visuals ---
with tabs[2]:
    st.subheader("Visualizations")
    df = st.session_state["df"]
    if len(df) > 0:
        fig, ax = plt.subplots(figsize=(6,4))
        df["score"].plot(ax=ax, marker="o", linestyle="-", alpha=0.7)
        ax.set_title("Real-time Trend: Score over Records")
        ax.set_xlabel("Record Index")
        ax.set_ylabel("Score")
        st.pyplot(fig)
    else:
        st.info("No data to visualize.")

# --- Drift & Export ---
with tabs[3]:
    st.subheader("Drift Metrics")
    if st.button("Compute Drift Metrics"):
        stats = model_drift_metrics(st.session_state["df"])
        st.json(stats)

    st.markdown("---")
    st.subheader("Export Data")
    df = st.session_state["df"]
    if len(df) > 0:
        st.download_button("Download CSV", dataframe_to_csv_bytes(df), "mcp_results.csv")
        st.download_button("Download JSON", dataframe_to_json_bytes(df), "mcp_results.json")

    if st.button("Save Snapshot"):
        stats = {
            "records": len(df),
            "mean_score": float(df["score"].mean()) if "score" in df.columns else None
        }
        append_event("snapshot", stats)
        st.success("Snapshot saved to DB.")

# --- Settings ---
with tabs[4]:
    st.subheader("Adjust Settings")
    st.session_state["settings"]["anomaly_threshold"] = st.slider("Anomaly Threshold", 0.0, 1.0, st.session_state["settings"]["anomaly_threshold"], 0.01)
    st.session_state["settings"]["anomaly_weight"] = st.slider("Anomaly Weight", 0, 100, st.session_state["settings"]["anomaly_weight"], 5)
    st.session_state["settings"]["violation_weight"] = st.slider("Violation Weight", 0, 100, st.session_state["settings"]["violation_weight"], 5)
    st.success("Settings updated.")

# --- Audit ---
with tabs[5]:
    st.subheader("Audit Log")
    audit_df = load_events(200)
    if len(audit_df) == 0:
        st.info("No events logged yet.")
    else:
        st.dataframe(audit_df)

st.markdown("---")
st.caption("MCP Demo Application Designed & Developed by Randy Singh — extended with SQLite persistence, real-time charts, and configurable thresholds.")
