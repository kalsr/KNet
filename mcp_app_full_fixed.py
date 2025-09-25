# mcp_app_full_fixed.py

import streamlit as st
import pandas as pd
import numpy as np
import sqlite3, json, datetime, io
import matplotlib.pyplot as plt

# ---------------- Initialize session state ----------------
if "df" not in st.session_state:
    st.session_state["df"] = None
if "settings" not in st.session_state:
    st.session_state["settings"] = {"anomaly_threshold": 0.20, "anomaly_weight": 20, "violation_weight": 50}
if "last_handled_action" not in st.session_state:
    st.session_state["last_handled_action"] = None

# ---------------- SQLite Logging (Audit Trail) ----------------
DB_FILE = "mcp_audit.db"
conn = sqlite3.connect(DB_FILE, check_same_thread=False)
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS context_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        event_type TEXT,
        details TEXT
    )
""")
conn.commit()

def append_event(event_type, details: dict):
    ts = datetime.datetime.utcnow().isoformat()
    cur.execute(
        "INSERT INTO context_events (timestamp, event_type, details) VALUES (?, ?, ?)",
        (ts, event_type, json.dumps(details)),
    )
    conn.commit()

# ---------------- Data Simulation ----------------
def generate_sample_data(n=50):
    np.random.seed(42)
    return pd.DataFrame({
        "id": range(n),
        "feature1": np.random.randn(n),
        "feature2": np.random.rand(n) * 10,
        "timestamp": pd.date_range("2025-01-01", periods=n, freq="h")
    })

# ---------------- Analysis Modules ----------------
def anomaly_detection_pipeline(df, settings):
    df["anomaly"] = np.abs(df["feature1"]) > settings["anomaly_threshold"] * df["feature1"].std()
    append_event("anomaly_detection", {"anomalies": int(df["anomaly"].sum())})
    return df

def policy_compliance_monitor(df, settings):
    df["violation"] = df["feature2"] > 8
    append_event("policy_check", {"violations": int(df["violation"].sum())})
    return df

def drift_detection_module(df):
    drift_score = df["feature1"].mean() - 0
    append_event("drift_check", {"drift_score": float(drift_score)})
    return drift_score

def incident_triage_assistant(df, settings):
    df["risk_score"] = df["anomaly"]*settings["anomaly_weight"] + df["violation"]*settings["violation_weight"]
    append_event("triage", {"max_risk": int(df["risk_score"].max())})
    return df

# ---------------- Sidebar Navigation ----------------
st.sidebar.title("Navigation")
nav_choice = st.sidebar.radio("Select Section:", [
    "Data Generation", "Inference & Analysis", "Policy Compliance",
    "Drift Detection", "Triage & Labeling", "Audit Log", "Export Context"
])

# ---------------- Action handling via query params ----------------
q = st.query_params
action = q.get("action", [None])[0] if isinstance(q.get("action"), list) else q.get("action")

if action and st.session_state.get("last_handled_action") != action:
    st.session_state["last_handled_action"] = action

    if action == "gen_default":
        st.session_state["df"] = generate_sample_data(50)
        append_event("sample_data_generated", {"n": 50})
        st.query_params.clear()   # ✅ FIX
        st.rerun()

    if action == "clear":
        keys = list(st.session_state.keys())
        for k in keys:
            st.session_state.pop(k, None)
        st.session_state["df"] = generate_sample_data(50)
        st.session_state["settings"] = {"anomaly_threshold": 0.20, "anomaly_weight": 20, "violation_weight": 50}
        append_event("session_cleared", {"via": "topbar"})
        st.query_params.clear()   # ✅ FIX
        st.rerun()

# ---------------- Top Action Bar ----------------
st.markdown("""
    <div style="display:flex; justify-content: space-between; background:#f0f2f6; padding:10px; border-radius:5px;">
        <a href="?action=gen_default"><button>Generate Sample Data</button></a>
        <a href="?action=clear"><button>Clear Session</button></a>
    </div>
""", unsafe_allow_html=True)

# ---------------- Section Implementations ----------------
if nav_choice == "Data Generation":
    st.header("Data Generation")
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        st.session_state["df"] = pd.read_csv(uploaded)
        append_event("file_upload", {"rows": len(st.session_state["df"])})
        st.query_params.clear()   # ✅ FIX

    st.dataframe(st.session_state["df"] if st.session_state["df"] is not None else pd.DataFrame())

elif nav_choice == "Inference & Analysis":
    st.header("Anomaly Detection")
    if st.session_state["df"] is not None:
        st.session_state["df"] = anomaly_detection_pipeline(st.session_state["df"], st.session_state["settings"])
        st.dataframe(st.session_state["df"])
    else:
        st.warning("No data available.")

elif nav_choice == "Policy Compliance":
    st.header("Policy Compliance Monitoring")
    if st.session_state["df"] is not None:
        st.session_state["df"] = policy_compliance_monitor(st.session_state["df"], st.session_state["settings"])
        st.dataframe(st.session_state["df"])
    else:
        st.warning("No data available.")

elif nav_choice == "Drift Detection":
    st.header("Drift Detection")
    if st.session_state["df"] is not None:
        drift_score = drift_detection_module(st.session_state["df"])
        st.metric("Drift Score", f"{drift_score:.2f}")
    else:
        st.warning("No data available.")

elif nav_choice == "Triage & Labeling":
    st.header("Incident Triage & Labeling")
    if st.session_state["df"] is not None:
        st.session_state["df"] = incident_triage_assistant(st.session_state["df"], st.session_state["settings"])
        st.dataframe(st.session_state["df"])
    else:
        st.warning("No data available.")

elif nav_choice == "Audit Log":
    st.header("Audit Log (Context Events)")
    rows = cur.execute("SELECT * FROM context_events ORDER BY id DESC LIMIT 50").fetchall()
    df_logs = pd.DataFrame(rows, columns=["id", "timestamp", "event_type", "details"])
    st.dataframe(df_logs)

elif nav_choice == "Export Context":
    st.header("Export Context")
    if st.session_state["df"] is not None:
        csv_buf = io.StringIO()
        st.session_state["df"].to_csv(csv_buf, index=False)
        st.download_button("Download CSV", data=csv_buf.getvalue(), file_name="context.csv")
        json_buf = io.StringIO()
        st.session_state["df"].to_json(json_buf, orient="records")
        st.download_button("Download JSON", data=json_buf.getvalue(), file_name="context.json")
    else:
        st.warning("No data available.")
