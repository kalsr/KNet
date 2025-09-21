# mcp_app_full_fixed.py
# MCP — Model Context Protocol (Fixed: no deprecated APIs, top-bar colored buttons, charts, SQLite)
# Place Kalsnetlogo.png next to this file and run: streamlit run mcp_app_full_fixed.py

import streamlit as st
import pandas as pd
import numpy as np
import json
import io
import sqlite3
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from pathlib import Path

# ---------------- Configuration ----------------
DATA_DIR = Path("./data")
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "mcp_store.db"
LOGO_FILE = "Kalsnetlogo.png"  # Put your logo in same folder

st.set_page_config(page_title="MCP — Model Context Protocol", layout="wide", initial_sidebar_state="collapsed")

# ---------------- CSS / Styling ----------------
st.markdown(
    """
    <style>
    /* Top-bar action buttons */
    .mcp-topbar { display:flex; gap:8px; align-items:center; padding:12px 8px; border-radius:8px;
                  background: linear-gradient(90deg, #ffffff, #f6f8fb); box-shadow: 0 2px 6px rgba(20,20,40,0.06);
                  margin-bottom: 12px; }
    .mcp-action {
      display:inline-block;
      padding:10px 14px;
      border-radius:10px;
      color:#fff;
      font-weight:700;
      text-decoration:none;
      font-size:14px;
      box-shadow: 0 3px 8px rgba(0,0,0,0.12);
    }
    .mcp-blue { background: linear-gradient(180deg,#2f80ed,#2565d6); }
    .mcp-green { background: linear-gradient(180deg,#2ecc71,#22b45a); }
    .mcp-red { background: linear-gradient(180deg,#ec5f5f,#d64545); }
    .mcp-amber { background: linear-gradient(180deg,#f6c85f,#efb536); color:#111; }
    .mcp-indigo { background: linear-gradient(180deg,#6a5acd,#5b49c9); }
    .mcp-muted { background:#f3f6f9; color:#222; border:1px solid #e1e5ea; box-shadow:none; }
    .mcp-header { font-size:22px; font-weight:800; margin:0; }
    .mcp-sub { color:#6c757d; margin-top:2px; margin-bottom:0; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- SQLite helpers ----------------
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

def append_event(event_name, payload=None):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO context_events (ts, event, payload) VALUES (?, ?, ?)",
                (datetime.utcnow().isoformat()+"Z", event_name, json.dumps(payload or {})))
    conn.commit()
    conn.close()

def load_events(limit=200):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM context_events ORDER BY id DESC LIMIT ?", conn, params=(limit,))
    conn.close()
    return df

def clear_events_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM context_events")
    conn.commit()
    conn.close()

init_db()

# ---------------- Utilities ----------------
def generate_sample_data(n=50, seed=None, spaced_seconds=5):
    rng = np.random.default_rng(int(seed) if (seed is not None and str(seed).strip().isdigit()) else None)
    categories = ["Normal", "Anomaly", "Warning", "Info"]
    rows = []
    base = datetime.utcnow() - timedelta(seconds=n * spaced_seconds)
    for i in range(1, n+1):
        ts = base + timedelta(seconds=i * spaced_seconds)
        rows.append({
            "id": i,
            "timestamp": ts.isoformat() + "Z",
            "score": float(np.round(rng.uniform(0, 1), 3)),
            "category": rng.choice(categories, p=[0.6,0.1,0.2,0.1]),
            "message": rng.choice([
                "User login", "File accessed", "Process started", "Timeout error",
                "High memory usage", "Configuration change", "Health check passed", "Permission denied"
            ])
        })
    return pd.DataFrame(rows)

def dataframe_to_csv_bytes(df):
    return df.to_csv(index=False).encode("utf-8")

def dataframe_to_json_bytes(df):
    return df.to_json(orient="records", force_ascii=False).encode("utf-8")

# ---------------- Use-case functions ----------------
def anomaly_detection_pipeline(df, threshold=0.2):
    df = df.copy()
    df["score"] = pd.to_numeric(df.get("score", 0), errors="coerce").fillna(0.0)
    df["anomaly_flag"] = df["score"].apply(lambda s: "ANOMALY" if float(s) < threshold else "OK")
    df["anomaly_reason"] = df.apply(lambda r: "low_score" if r["anomaly_flag"] == "ANOMALY" else "", axis=1)
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

def model_drift_metrics(df, history_n=100):
    stats = {"count": len(df)}
    if len(df) > 0 and "score" in df.columns:
        stats.update({
            "mean_score": float(df["score"].mean()),
            "std_score": float(df["score"].std(ddof=0) if len(df)>1 else 0.0),
            "min_score": float(df["score"].min()),
            "max_score": float(df["score"].max())
        })
    hist = load_events(history_n)
    historical_means = []
    for _, row in hist.iterrows():
        try:
            p = json.loads(row["payload"])
            if isinstance(p, dict) and "mean_score" in p:
                historical_means.append(p["mean_score"])
        except Exception:
            continue
    if historical_means:
        stats["historical_mean_of_means"] = float(np.mean(historical_means))
        stats["drift_delta"] = stats.get("mean_score", 0.0) - stats["historical_mean_of_means"]
    append_event("drift_metrics_computed", {"mean_score": stats.get("mean_score")})
    return stats

def data_labeling_assist(df, top_n=10):
    df = df.copy()
    df["score"] = pd.to_numeric(df.get("score", 0), errors="coerce").fillna(0.0)
    df["uncertain"] = df["score"].apply(lambda s: True if 0.35 <= float(s) <= 0.6 else False)
    candidates = df[df["uncertain"]].head(top_n)
    append_event("labeling_task_created", {"candidates": len(candidates)})
    return df, candidates

def incident_triage_assistant(df, anomaly_weight=20, violation_weight=50):
    df = df.copy()
    def severity_calc(row):
        base = (1.0 - float(row.get("score", 0.0))) * 100
        policy_weight = violation_weight if row.get("policy_state", "") == "VIOLATION" else (anomaly_weight if row.get("anomaly_flag", "") == "ANOMALY" else 0)
        return base + policy_weight
    df["severity"] = df.apply(severity_calc, axis=1)
    df = df.sort_values("severity", ascending=False).reset_index(drop=True)
    append_event("incident_triage_run", {"records": len(df)})
    return df

# ---------------- Session defaults ----------------
if "df" not in st.session_state:
    st.session_state["df"] = generate_sample_data(50)
    append_event("sample_data_generated", {"n": 50})

if "settings" not in st.session_state:
    st.session_state["settings"] = {"anomaly_threshold": 0.20, "anomaly_weight": 20, "violation_weight": 50}

if "last_handled_action" not in st.session_state:
    st.session_state["last_handled_action"] = None

# ---------------- Header + top-bar action buttons ----------------
top_container = st.container()
with top_container:
    left, mid, right = st.columns([1, 6, 1])
    with left:
        if Path(LOGO_FILE).exists():
            st.image(LOGO_FILE, width=72)
    with mid:
        st.markdown("<p class='mcp-header'>Model Context Protocol (MCP)</p>", unsafe_allow_html=True)
        st.markdown("<p class='mcp-sub'>Interactive demo — context store, policies, audits, exports. By Randy Singh / KNet Consulting.</p>", unsafe_allow_html=True)
        # Top action buttons (anchor links that set query params)
        st.markdown(
            """
            <div class='mcp-topbar'>
              <a class='mcp-action mcp-blue' href='?action=gen_default'>Generate Sample (50)</a>
              <a class='mcp-action mcp-indigo' href='?action=gen_custom'>Generate Custom</a>
              <a class='mcp-action mcp-green' href='?action=upload'>Upload File</a>
              <a class='mcp-action mcp-amber' href='?action=run_inference'>Run Inference</a>
              <a class='mcp-action mcp-blue' href='?action=apply_policy'>Apply Policy</a>
              <a class='mcp-action mcp-indigo' href='?action=drift'>Model Drift</a>
              <a class='mcp-action mcp-green' href='?action=label'>Label Assist</a>
              <a class='mcp-action mcp-amber' href='?action=triage'>Triage</a>
              <a class='mcp-action mcp-red' href='?action=clear'>Clear</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---------------- Action handling via query params (uses st.query_params) ----------------
q = st.query_params
action = q.get("action", [None])[0] if isinstance(q.get("action"), list) else q.get("action")

# Only process an action once (prevents double-run on rerender)
if action and st.session_state.get("last_handled_action") != action:
    st.session_state["last_handled_action"] = action

    # simple direct actions
    if action == "gen_default":
        st.session_state["df"] = generate_sample_data(50)
        append_event("sample_data_generated", {"n": 50})
        # clear query params and reload
        st.set_query_params()
        st.rerun()

    if action == "clear":
        # clear runtime session (but keep DB)
        keys = list(st.session_state.keys())
        for k in keys:
            st.session_state.pop(k, None)
        st.session_state["df"] = generate_sample_data(50)
        st.session_state["settings"] = {"anomaly_threshold": 0.20, "anomaly_weight": 20, "violation_weight": 50}
        append_event("session_cleared", {"via": "topbar"})
        st.set_query_params()
        st.rerun()

    # for actions that require UI input, we keep action in query so UI can show forms (handled below)
    # e.g. gen_custom, upload, label, triage, run_inference, apply_policy, drift handled in UI below

# ---------------- Main tabs ----------------
tabs = st.tabs(["Data", "Use Cases", "Visuals", "Drift & Export", "Settings", "Audit"])

# ---------- Data Tab ----------
with tabs[0]:
    st.subheader("Data — generate / upload / preview")
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("**Generate sample data**")
        n = st.number_input("Records", min_value=5, max_value=5000, value=50, step=5, key="gen_n")
        seed = st.text_input("Seed (optional)", key="gen_seed")
        if st.button("Generate (main)"):
            st.session_state["df"] = generate_sample_data(int(n), seed or None)
            append_event("sample_data_generated", {"n": int(n), "seed": seed})
            st.success(f"Generated {n} records.")

        st.markdown("---")
        st.markdown("**File upload** (CSV or JSON)")
        uploaded = st.file_uploader("Upload file", type=["csv", "json"], key="main_u")
        if uploaded is not None:
            try:
                uploaded.seek(0)
                if uploaded.name.lower().endswith(".csv"):
                    df_new = pd.read_csv(uploaded)
                else:
                    uploaded.seek(0)
                    obj = json.load(uploaded)
                    df_new = pd.json_normalize(obj)
                st.session_state["df"] = df_new
                append_event("file_uploaded", {"name": uploaded.name, "records": len(df_new)})
                st.success(f"Loaded {len(df_new)} records from {uploaded.name}.")
                # clear query params in case action=upload
                st.set_query_params()
            except Exception as e:
                st.error(f"Failed to parse upload: {e}")

        st.markdown("---")
        st.markdown("**Quick actions**")
        if st.button("Run Inference (main)"):
            df = st.session_state.get("df")
            if df is None or len(df) == 0:
                st.warning("No data present.")
            else:
                st.session_state["df"] = anomaly_detection_pipeline(df, st.session_state["settings"]["anomaly_threshold"])
                st.success("Anomaly detection applied.")
        if st.button("Apply Policy (main)"):
            df = st.session_state.get("df")
            if df is None or len(df) == 0:
                st.warning("No data present.")
            else:
                st.session_state["df"] = policy_compliance_monitor(df)
                st.success("Policy applied.")

    with col2:
        st.markdown("**Session controls**")
        if st.button("Clear session (keep DB)"):
            keys = list(st.session_state.keys())
            for k in keys:
                st.session_state.pop(k, None)
            st.session_state["df"] = generate_sample_data(50)
            st.session_state["settings"] = {"anomaly_threshold": 0.20, "anomaly_weight": 20, "violation_weight": 50}
            append_event("session_cleared", {"via": "button"})
            st.success("Session cleared & default sample loaded.")

        st.markdown("---")
        st.markdown("**DB actions**")
        if st.button("Clear DB (PERMANENT)"):
            # require explicit confirmation text input
            confirm = st.text_input("Type DELETE to confirm DB clear", key="confirm_db_clear")
            if confirm == "DELETE":
                clear_events_db()
                st.success("DB cleared.")
            else:
                st.warning("Type DELETE into the box above to confirm permanent DB clear.")

    # Data preview
    st.markdown("### Data preview")
    df = st.session_state.get("df")
    if df is None or len(df) == 0:
        st.info("No data loaded. Generate or upload to begin.")
    else:
        st.dataframe(df.head(500))

# ---------- Use Cases Tab ----------
with tabs[1]:
    st.subheader("Use Cases: labeling, triage, and manual operations")
    df = st.session_state.get("df")
    if df is None or len(df) == 0:
        st.info("No data available for use cases.")
    else:
        left, right = st.columns([2, 1])
        with left:
            st.markdown("**Labeling Assist**")
            df, candidates = data_labeling_assist(df, top_n=25)
            st.session_state["df"] = df
            if candidates.empty:
                st.write("No uncertain candidates (score between 0.35 and 0.6).")
            else:
                st.write("Candidates for labeling:")
                st.dataframe(candidates)
                with st.form("label_form_main"):
                    sel = st.multiselect("Choose indices to label", list(candidates.index))
                    label_val = st.selectbox("Label value", ["MANUAL_REVIEW", "CONFIRMED_ANOMALY", "FALSE_POSITIVE"])
                    if st.form_submit_button("Apply labels"):
                        for idx in sel:
                            if idx in st.session_state["df"].index:
                                st.session_state["df"].at[idx, "human_label"] = label_val
                        append_event("labels_applied", {"count": len(sel), "label": label_val})
                        st.success(f"Applied label '{label_val}' to {len(sel)} rows.")

            st.markdown("---")
            st.markdown("**Incident triage (priority ordering)**")
            if st.button("Run Incident Triage"):
                df = st.session_state.get("df")
                if df is None:
                    st.warning("No data.")
                else:
                    if "policy_state" not in df.columns:
                        df = policy_compliance_monitor(df)
                    if "anomaly_flag" not in df.columns:
                        df = anomaly_detection_pipeline(df, st.session_state["settings"]["anomaly_threshold"])
                    st.session_state["df"] = incident_triage_assistant(df, st.session_state["settings"]["anomaly_weight"], st.session_state["settings"]["violation_weight"])
                    st.success("Triage completed.")
                    st.dataframe(st.session_state["df"].head(20))

        with right:
            st.markdown("Quick inference")
            if st.button("Run Anomaly Detection (quick)"):
                df = st.session_state.get("df")
                if df is None:
                    st.warning("No data.")
                else:
                    st.session_state["df"] = anomaly_detection_pipeline(df, st.session_state["settings"]["anomaly_threshold"])
                    st.success("Anomaly detection done.")

            if st.button("Apply Policy (quick)"):
                df = st.session_state.get("df")
                if df is None:
                    st.warning("No data.")
                else:
                    st.session_state["df"] = policy_compliance_monitor(df)
                    st.success("Policy applied.")

# ---------- Visuals Tab ----------
with tabs[2]:
    st.subheader("Visualizations: pie charts and trend")
    df = st.session_state.get("df")
    if df is None or len(df) == 0:
        st.info("No data to visualize.")
    else:
        # Prepare timestamp
        df_plot = df.copy()
        if "timestamp" in df_plot.columns:
            df_plot["ts_parsed"] = pd.to_datetime(df_plot["timestamp"], utc=True, errors="coerce")
            # if parsing failed for most rows, fallback to index
            if df_plot["ts_parsed"].notna().sum() < 2:
                df_plot["ts_parsed"] = pd.to_datetime(df_plot.index, unit="s", errors="coerce")
        else:
            df_plot["ts_parsed"] = pd.to_datetime(df_plot.index, errors="coerce")

        # Pie charts: category and flags
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        if "category" in df_plot.columns:
            cat_counts = df_plot["category"].fillna("UNKNOWN").value_counts()
            axes[0].pie(cat_counts.values, labels=cat_counts.index, autopct="%1.1f%%", startangle=90)
            axes[0].set_title("Category Distribution")
        else:
            axes[0].text(0.5, 0.5, "No category column", ha="center", va="center")

        flag_col = "anomaly_flag" if "anomaly_flag" in df_plot.columns else ("policy_state" if "policy_state" in df_plot.columns else None)
        if flag_col:
            fcounts = df_plot[flag_col].fillna("NONE").value_counts()
            axes[1].pie(fcounts.values, labels=fcounts.index, autopct="%1.1f%%", startangle=90)
            axes[1].set_title(flag_col.replace("_", " ").title())
        else:
            axes[1].text(0.5, 0.5, "Run inference / policy to view flags", ha="center", va="center")

        st.pyplot(fig)

        # Trend chart: average score over time
        if df_plot["ts_parsed"].notna().sum() >= 2 and "score" in df_plot.columns:
            ts_df = df_plot.set_index("ts_parsed").sort_index()
            # choose resample rule based on span
            span = (ts_df.index.max() - ts_df.index.min()).total_seconds()
            rule = "30S" if span <= 300 else ("1T" if span <= 3600 else "5T")
            agg = ts_df["score"].resample(rule).mean().ffill()
            fig2, ax2 = plt.subplots(figsize=(12, 3))
            ax2.plot(agg.index.to_pydatetime(), agg.values, marker="o", linestyle="-")
            ax2.set_title("Trend — Average Score over Time")
            ax2.set_xlabel("Time")
            ax2.set_ylabel("Avg Score")
            fig2.autofmt_xdate()
            st.pyplot(fig2)
        else:
            # fallback: score vs index
            fig3, ax3 = plt.subplots(figsize=(10,3))
            ax3.plot(df_plot.index, pd.to_numeric(df_plot.get("score", 0), errors="coerce").fillna(0.0), marker=".", linestyle="-")
            ax3.set_title("Score vs Record Index")
            ax3.set_xlabel("Index")
            ax3.set_ylabel("Score")
            st.pyplot(fig3)

# ---------- Drift & Export Tab ----------
with tabs[3]:
    st.subheader("Drift metrics & exports")
    df = st.session_state.get("df")
    if st.button("Compute Drift Metrics"):
        if df is None or len(df) == 0:
            st.warning("No data.")
        else:
            stats = model_drift_metrics(df, history_n=200)
            st.json(stats)
    st.markdown("---")
    if df is not None and len(df) > 0:
        st.download_button("Download CSV", data=dataframe_to_csv_bytes(df), file_name="mcp_results.csv", mime="text/csv")
        st.download_button("Download JSON", data=dataframe_to_json_bytes(df), file_name="mcp_results.json", mime="application/json")
        if st.button("Save Snapshot to DB"):
            snap = {
                "records": len(df),
                "mean_score": float(df["score"].mean()) if "score" in df.columns else None,
                "min_score": float(df["score"].min()) if "score" in df.columns else None
            }
            append_event("snapshot", snap)
            st.success("Snapshot saved.")

# ---------- Settings Tab ----------
with tabs[4]:
    st.subheader("Settings — thresholds & weights")
    s = st.session_state["settings"]
    new_threshold = st.slider("Anomaly threshold (score < threshold = ANOMALY)", 0.0, 1.0, float(s.get("anomaly_threshold", 0.2)), 0.01)
    new_aw = st.slider("Anomaly weight (triage)", 0, 100, int(s.get("anomaly_weight", 20)), 1)
    new_vw = st.slider("Violation weight (triage)", 0, 200, int(s.get("violation_weight", 50)), 1)
    if st.button("Save Settings"):
        st.session_state["settings"]["anomaly_threshold"] = float(new_threshold)
        st.session_state["settings"]["anomaly_weight"] = int(new_aw)
        st.session_state["settings"]["violation_weight"] = int(new_vw)
        append_event("settings_updated", st.session_state["settings"])
        st.success("Settings saved.")

# ---------- Audit Tab ----------
with tabs[5]:
    st.subheader("Audit log (SQLite)")
    audit_df = load_events(500)
    if audit_df.empty:
        st.info("No events recorded yet.")
    else:
        st.dataframe(audit_df)

# ---------- Footer ----------
st.markdown("---")
st.caption("MCP — Model Context Protocol. Built by Randy Singh / KNet Consulting. Database stored at ./data/mcp_store.db")

