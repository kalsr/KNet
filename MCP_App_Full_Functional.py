

# mcp_app_full.py
# MCP — Model Context Protocol (Full Streamlit app with colored sidebar, SQLite, charts, settings)
# Save next to Kalsnetlogo.png and run: streamlit run mcp_app_full.py

import streamlit as st
import pandas as pd
import numpy as np
import json
import io
import sqlite3
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from pathlib import Path

# ----------------- Config -----------------
DATA_DIR = Path("./data")
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "mcp_store.db"
LOGO_FILE = "Kalsnetlogo.png"   # place your logo here

st.set_page_config(page_title="MCP — Model Context Protocol", layout="wide")

# ----------------- Styling (colored buttons) -----------------
st.markdown(
    """
    <style>
    /* Buttons */
    .mcp-btn {
      display:block;
      padding:10px 12px;
      margin:6px 0;
      border-radius:8px;
      color: #fff;
      text-decoration:none;
      font-weight:700;
      text-align:center;
      box-shadow: 0 2px 6px rgba(0,0,0,0.12);
      width: 100%;
      max-width: 220px;
      display:inline-block;
    }
    .mcp-blue { background: linear-gradient(180deg,#2f80ed,#2565d6); }
    .mcp-green { background: linear-gradient(180deg,#2ecc71,#22b45a); }
    .mcp-red { background: linear-gradient(180deg,#ec5f5f,#d64545); }
    .mcp-amber { background: linear-gradient(180deg,#f6c85f,#efb536); color:#111; }
    .mcp-indigo { background: linear-gradient(180deg,#6a5acd,#5b49c9); }
    .mcp-muted { background:#f3f6f9; color:#222; border:1px solid #e1e5ea; box-shadow:none; }

    /* Sidebar tweaks to keep buttons stacked nicely */
    .css-1d391kg { padding-top: 8px; } /* minor safe tweak for sidebar spacing (may vary by Streamlit version) */

    .mcp-header { font-size:28px; font-weight:800; margin-bottom: 6px; }
    .mcp-sub { color:#6c757d; margin-bottom:10px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------- SQLite helpers -----------------
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

def append_event(event_name: str, payload: dict | None = None):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO context_events (ts, event, payload) VALUES (?, ?, ?)",
                (datetime.utcnow().isoformat() + "Z", event_name, json.dumps(payload or {})))
    conn.commit()
    conn.close()

def load_events(limit: int = 200) -> pd.DataFrame:
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

# ----------------- Utilities -----------------
def generate_sample_data(n: int = 50, seed: str | None = None, spaced_seconds: int = 5) -> pd.DataFrame:
    rng = np.random.default_rng(int(seed) if (seed and str(seed).strip().isdigit()) else None)
    categories = ["Normal", "Anomaly", "Warning", "Info"]
    rows = []
    base = datetime.utcnow() - timedelta(seconds=n*spaced_seconds)
    for i in range(1, n+1):
        ts = base + timedelta(seconds=i*spaced_seconds)
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

def dataframe_to_csv_bytes(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode("utf-8")

def dataframe_to_json_bytes(df: pd.DataFrame) -> bytes:
    return df.to_json(orient="records", force_ascii=False).encode("utf-8")

# ----------------- Core use-case functions -----------------
def anomaly_detection_pipeline(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    df = df.copy()
    df["score"] = pd.to_numeric(df["score"], errors="coerce").fillna(0.0)
    df["anomaly_flag"] = df["score"].apply(lambda s: "ANOMALY" if float(s) < threshold else "OK")
    df["anomaly_reason"] = df.apply(lambda r: "low_score" if r["anomaly_flag"]=="ANOMALY" else "", axis=1)
    append_event("anomaly_detection_run", {"records": len(df), "threshold": threshold})
    return df

def policy_compliance_monitor(df: pd.DataFrame) -> pd.DataFrame:
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

def model_drift_metrics(df: pd.DataFrame, history_n: int = 100) -> dict:
    df = df.copy()
    stats = {"count": len(df)}
    if len(df) > 0 and "score" in df.columns:
        stats.update({
            "mean_score": float(df["score"].mean()),
            "std_score": float(df["score"].std(ddof=0) if len(df)>1 else 0.0),
            "min_score": float(df["score"].min()),
            "max_score": float(df["score"].max())
        })
    # compare to historical snapshots in DB
    hist = load_events(history_n)
    historical_means = []
    for _, row in hist.iterrows():
        try:
            p = json.loads(row["payload"])
            if isinstance(p, dict) and ("mean_score" in p):
                historical_means.append(p["mean_score"])
        except Exception:
            continue
    if historical_means:
        stats["historical_mean_of_means"] = float(np.mean(historical_means))
        stats["drift_delta"] = (stats.get("mean_score") or 0.0) - stats["historical_mean_of_means"]
    append_event("drift_metrics_computed", {"mean_score": stats.get("mean_score")})
    return stats

def data_labeling_assist(df: pd.DataFrame, top_n: int = 10) -> tuple[pd.DataFrame, pd.DataFrame]:
    df = df.copy()
    df["score"] = pd.to_numeric(df["score"], errors="coerce").fillna(0.0)
    df["uncertain"] = df["score"].apply(lambda s: True if 0.35 <= float(s) <= 0.6 else False)
    candidates = df[df["uncertain"]].head(top_n)
    append_event("labeling_task_created", {"candidates": len(candidates)})
    return df, candidates

def incident_triage_assistant(df: pd.DataFrame, anomaly_weight: int=20, violation_weight: int=50) -> pd.DataFrame:
    df = df.copy()
    def severity_calc(row):
        base = (1.0 - float(row.get("score",0.0))) * 100
        policy_weight = violation_weight if row.get("policy_state","")=="VIOLATION" else (anomaly_weight if row.get("anomaly_flag","")=="ANOMALY" else 0)
        return base + policy_weight
    df["severity"] = df.apply(severity_calc, axis=1)
    df = df.sort_values("severity", ascending=False).reset_index(drop=True)
    append_event("incident_triage_run", {"records": len(df)})
    return df

# ----------------- Session state default initialization -----------------
if "df" not in st.session_state:
    st.session_state["df"] = generate_sample_data(50)
    append_event("sample_data_generated", {"n":50})

if "settings" not in st.session_state:
    st.session_state["settings"] = {
        "anomaly_threshold": 0.20,
        "anomaly_weight": 20,
        "violation_weight": 50
    }

if "last_handled_action" not in st.session_state:
    st.session_state["last_handled_action"] = None

# ----------------- Sidebar (colored action buttons + native controls) -----------------
st.sidebar.markdown("<div style='text-align:center;margin-bottom:8px;'>", unsafe_allow_html=True)
if Path(LOGO_FILE).exists():
    st.sidebar.image(LOGO_FILE, width=120)
st.sidebar.markdown("</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='margin-top:4px;margin-bottom:6px;'><b>Actions</b></div>", unsafe_allow_html=True)

# Colored anchor-style links (visual)
st.sidebar.markdown(f"<a class='mcp-btn mcp-blue' href='?action=gen_default'>Generate Sample Data (50)</a>", unsafe_allow_html=True)
st.sidebar.markdown(f"<a class='mcp-btn mcp-indigo' href='?action=gen_custom'>Generate (Custom)</a>", unsafe_allow_html=True)
st.sidebar.markdown(f"<a class='mcp-btn mcp-green' href='?action=upload'>Upload File</a>", unsafe_allow_html=True)
st.sidebar.markdown(f"<a class='mcp-btn mcp-amber' href='?action=run_inference'>Run Inference (Anomaly)</a>", unsafe_allow_html=True)
st.sidebar.markdown(f"<a class='mcp-btn mcp-blue' href='?action=apply_policy'>Apply Policy</a>", unsafe_allow_html=True)
st.sidebar.markdown(f"<a class='mcp-btn mcp-indigo' href='?action=drift'>Model Drift</a>", unsafe_allow_html=True)
st.sidebar.markdown(f"<a class='mcp-btn mcp-green' href='?action=label'>Label Assist</a>", unsafe_allow_html=True)
st.sidebar.markdown(f"<a class='mcp-btn mcp-amber' href='?action=triage'>Incident Triage</a>", unsafe_allow_html=True)
st.sidebar.markdown(f"<a class='mcp-btn mcp-red' href='?action=clear'>Clear Session</a>", unsafe_allow_html=True)

st.sidebar.write("---")
st.sidebar.markdown("**Native controls** (recommended):")
# Native upload + sample generator
uploaded_file = st.sidebar.file_uploader("Upload CSV/JSON", type=["csv","json"])
native_samplesize = st.sidebar.number_input("Sample size", min_value=5, max_value=5000, value=50, step=5)
native_seed = st.sidebar.text_input("Seed (optional)")
if st.sidebar.button("Generate Sample (native)"):
    st.session_state["df"] = generate_sample_data(int(native_samplesize), native_seed or None)
    append_event("sample_data_generated", {"n": int(native_samplesize), "seed": native_seed})
    st.sidebar.success(f"Generated {native_samplesize} records.")
if st.sidebar.button("Clear Session (native)"):
    # clear session state but keep DB
    keys = list(st.session_state.keys())
    for k in keys:
        st.session_state.pop(k, None)
    # re-add defaults
    st.session_state["df"] = generate_sample_data(50)
    st.session_state["settings"] = {"anomaly_threshold":0.20, "anomaly_weight":20, "violation_weight":50}
    append_event("session_cleared", {"retain_db": True})
    st.sidebar.success("Session cleared and default sample reloaded.")

st.sidebar.write("---")
st.sidebar.markdown("**Danger**")
if st.sidebar.button("Clear DB (PERMANENT)"):
    confirm = st.sidebar.text_input("Type DELETE to confirm DB clear")
    if confirm == "DELETE":
        clear_events_db()
        st.sidebar.success("DB cleared.")
    else:
        st.sidebar.warning("Type DELETE to confirm clearing DB (irreversible).")

# ----------------- Main app layout -----------------
col1, col2 = st.columns([3,1])
with col1:
    header_cols = st.columns([1,6])
    with header_cols[0]:
        if Path(LOGO_FILE).exists():
            st.image(LOGO_FILE, width=80)
    with header_cols[1]:
        st.markdown("<div class='mcp-header'>Model Context Protocol (MCP)</div>", unsafe_allow_html=True)
        st.markdown("<div class='mcp-sub'>Interactive demo — context, policies, audits, export. By Randy Singh, KNet Consulting.</div>", unsafe_allow_html=True)

with col2:
    st.write("")  # small spacing
    events_preview = load_events(5)
    if not events_preview.empty:
        st.caption("Recent events")
        st.dataframe(events_preview[["ts","event"]].head(6))
    else:
        st.caption("No events yet")

st.markdown("---")

# Read action query param (if any)
action = st.experimental_get_query_params().get("action", [None])[0]  # safe to use to read only

# Simple guard: only process an action if it's new (prevents reprocessing if page reloaded)
if action and st.session_state.get("last_handled_action") != action:
    st.session_state["last_handled_action"] = action
    # handle a few quick actions that don't need more inputs
    if action == "gen_default":
        st.session_state["df"] = generate_sample_data(50)
        append_event("sample_data_generated", {"n":50})
        st.experimental_rerun()
    if action == "clear":
        # clear session only, keep DB
        # clear keys except settings? We'll re-init minimal state
        keys = list(st.session_state.keys())
        for k in keys:
            st.session_state.pop(k, None)
        st.session_state["df"] = generate_sample_data(50)
        st.session_state["settings"] = {"anomaly_threshold":0.20, "anomaly_weight":20, "violation_weight":50}
        append_event("session_cleared", {"via": "sidebar_action"})
        st.experimental_rerun()
    # for other actions we just fall through to show the relevant UI below (e.g., gen_custom shows the generator form)

# ----------------- Tabs -----------------
tabs = st.tabs(["Data & Upload", "Use Cases", "Visuals", "Drift / Export", "Settings", "Audit"])

# ----- Data & Upload -----
with tabs[0]:
    st.subheader("Data & Upload")
    df = st.session_state.get("df")
    c1, c2, c3 = st.columns([1,1,2])

    with c1:
        st.markdown("**Generate**")
        n = st.number_input("N records", min_value=5, max_value=5000, value=50, step=5, key="ui_n")
        seed = st.text_input("Seed (optional)", key="ui_seed")
        if st.button("Generate Sample Data (main)"):
            st.session_state["df"] = generate_sample_data(int(n), seed or None)
            append_event("sample_data_generated", {"n": int(n), "seed": seed})
            st.success(f"Generated {n} records.")

    with c2:
        st.markdown("**Upload**")
        uploaded = st.file_uploader("Upload CSV or JSON", type=["csv","json"], key="main_uploader")
        if uploaded is not None:
            try:
                uploaded.seek(0)
                if uploaded.name.lower().endswith(".csv"):
                    df_new = pd.read_csv(uploaded)
                else:
                    # try parsing JSON
                    uploaded.seek(0)
                    obj = json.load(uploaded)
                    df_new = pd.json_normalize(obj)
                # normalize columns and ensure 'score' exists
                st.session_state["df"] = df_new
                append_event("file_uploaded", {"filename": uploaded.name, "records": len(df_new)})
                st.success(f"Loaded {len(df_new)} records from {uploaded.name}.")
            except Exception as e:
                st.error(f"Upload failed: {e}")

    with c3:
        st.markdown("**Quick actions**")
        if st.button("Run Inference (Anomaly)"):
            df = st.session_state.get("df")
            if df is None:
                st.warning("No data loaded.")
            else:
                st.session_state["df"] = anomaly_detection_pipeline(df, st.session_state["settings"]["anomaly_threshold"])
                st.success("Anomaly detection applied.")
        if st.button("Apply Policy"):
            df = st.session_state.get("df")
            if df is None:
                st.warning("No data loaded.")
            else:
                st.session_state["df"] = policy_compliance_monitor(df)
                st.success("Policy applied.")
        if st.button("Run Incident Triage"):
            df = st.session_state.get("df")
            if df is None:
                st.warning("No data loaded.")
            else:
                # ensure policy & anomaly columns exist
                if "policy_state" not in df.columns:
                    df = policy_compliance_monitor(df)
                if "anomaly_flag" not in df.columns:
                    df = anomaly_detection_pipeline(df, st.session_state["settings"]["anomaly_threshold"])
                st.session_state["df"] = incident_triage_assistant(df, st.session_state["settings"]["anomaly_weight"], st.session_state["settings"]["violation_weight"])
                st.success("Incident triage complete.")

    st.markdown("---")
    df_display = st.session_state.get("df")
    if df_display is None or len(df_display)==0:
        st.info("No data loaded. Use generate or upload.")
    else:
        st.dataframe(df_display.head(500))

# ----- Use Cases -----
with tabs[1]:
    st.subheader("Use Cases & Labeling")
    df = st.session_state.get("df")
    if df is None or len(df)==0:
        st.info("No data available for use cases.")
    else:
        st.markdown("**Data Labeling Assist**")
        df, candidates = data_labeling_assist(df, top_n=25)
        st.session_state["df"] = df
        if candidates.empty:
            st.write("No uncertain candidates found (score between 0.35 and 0.6).")
        else:
            st.write("Candidates (low-confidence rows):")
            st.dataframe(candidates)
            with st.form("label_form"):
                sel = st.multiselect("Select row indices to label", list(candidates.index))
                label_val = st.selectbox("Label to apply", ["MANUAL_REVIEW", "CONFIRMED_ANOMALY", "FALSE_POSITIVE"])
                if st.form_submit_button("Apply Labels"):
                    for idx in sel:
                        if idx in st.session_state["df"].index:
                            st.session_state["df"].at[idx, "human_label"] = label_val
                    append_event("labels_applied", {"count": len(sel), "label": label_val})
                    st.success(f"Applied label '{label_val}' to {len(sel)} rows.")

# ----- Visuals -----
with tabs[2]:
    st.subheader("Visualizations: Pie charts & Trend")
    df = st.session_state.get("df")
    if df is None or len(df)==0:
        st.info("No data to visualize.")
    else:
        # Preprocess timestamp for time-series plotting
        df_plot = df.copy()
        if "timestamp" in df_plot.columns:
            try:
                df_plot["timestamp_parsed"] = pd.to_datetime(df_plot["timestamp"], utc=True, errors="coerce")
                # if all NaT, fallback to index as x
                if df_plot["timestamp_parsed"].notna().sum() < 2:
                    df_plot["timestamp_parsed"] = pd.to_datetime(df_plot.index, unit="s", errors="coerce")
            except Exception:
                df_plot["timestamp_parsed"] = pd.to_datetime(df_plot.index, errors="coerce")
        else:
            df_plot["timestamp_parsed"] = pd.to_datetime(df_plot.index, errors="coerce")

        # Pie charts
        fig1, axes = plt.subplots(1, 2, figsize=(10,4))
        # Category distribution
        if "category" in df_plot.columns:
            cat_counts = df_plot["category"].fillna("UNKNOWN").value_counts()
            axes[0].pie(cat_counts.values, labels=cat_counts.index, autopct="%1.1f%%", startangle=90)
            axes[0].set_title("Category Distribution")
        else:
            axes[0].text(0.5,0.5,"No category data", ha="center", va="center")
        # Flags distribution: prefer anomaly_flag, else policy_state
        flag_col = "anomaly_flag" if "anomaly_flag" in df_plot.columns else ("policy_state" if "policy_state" in df_plot.columns else None)
        if flag_col:
            fcounts = df_plot[flag_col].fillna("NONE").value_counts()
            axes[1].pie(fcounts.values, labels=fcounts.index, autopct="%1.1f%%", startangle=90)
            axes[1].set_title(flag_col.replace("_"," ").title())
        else:
            axes[1].text(0.5,0.5,"Run inference/policy to see flags", ha="center", va="center")
        st.pyplot(fig1)

        # Trend chart: average score over time (grouped by minute)
        if df_plot["timestamp_parsed"].notna().sum() >= 2 and "score" in df_plot.columns:
            ts_df = df_plot.set_index("timestamp_parsed").sort_index()
            # resample per minute or per 30s if short data
            delta = (ts_df.index.max() - ts_df.index.min()).total_seconds() if len(ts_df.index)>1 else 0
            if delta <= 300:
                rule = "30S"
            elif delta <= 3600:
                rule = "1T"
            else:
                rule = "5T"
            agg = ts_df["score"].resample(rule).mean().ffill()
            fig2, ax2 = plt.subplots(figsize=(10,3))
            ax2.plot(agg.index.to_pydatetime(), agg.values, marker="o", linestyle="-")
            ax2.set_title("Trend: Average Score over Time")
            ax2.set_xlabel("Time")
            ax2.set_ylabel("Average Score")
            fig2.autofmt_xdate()
            st.pyplot(fig2)
        else:
            # fallback: simple score-by-index plot
            fig3, ax3 = plt.subplots(figsize=(8,3))
            ax3.plot(df_plot.index, pd.to_numeric(df_plot["score"], errors="coerce").fillna(0.0), marker=".", linestyle="-")
            ax3.set_title("Score vs Record Index (fallback)")
            ax3.set_xlabel("Record Index")
            ax3.set_ylabel("Score")
            st.pyplot(fig3)

# ----- Drift / Export -----
with tabs[3]:
    st.subheader("Drift Metrics & Export")
    df = st.session_state.get("df")
    if st.button("Compute Drift Metrics"):
        if df is None or len(df)==0:
            st.warning("No data for drift.")
        else:
            stats = model_drift_metrics(df, history_n=200)
            st.json(stats)
    st.markdown("---")
    if df is not None and len(df)>0:
        st.download_button("⬇️ Download CSV", data=dataframe_to_csv_bytes(df), file_name="mcp_results.csv", mime="text/csv")
        st.download_button("⬇️ Download JSON", data=dataframe_to_json_bytes(df), file_name="mcp_results.json", mime="application/json")
        if st.button("Save Snapshot to DB"):
            snap = {
                "records": len(df),
                "mean_score": float(df["score"].mean()) if "score" in df.columns else None,
                "min_score": float(df["score"].min()) if "score" in df.columns else None
            }
            append_event("snapshot", snap)
            st.success("Snapshot saved to DB.")

# ----- Settings -----
with tabs[4]:
    st.subheader("Settings & Thresholds")
    settings = st.session_state["settings"]
    t = st.slider("Anomaly threshold (score < threshold → ANOMALY)", 0.0, 1.0, float(settings.get("anomaly_threshold",0.20)), 0.01)
    aw = st.slider("Anomaly weight (triage)", 0, 100, int(settings.get("anomaly_weight",20)), 1)
    vw = st.slider("Violation weight (triage)", 0, 200, int(settings.get("violation_weight",50)), 1)
    if st.button("Save Settings"):
        st.session_state["settings"]["anomaly_threshold"] = float(t)
        st.session_state["settings"]["anomaly_weight"] = int(aw)
        st.session_state["settings"]["violation_weight"] = int(vw)
        append_event("settings_updated", st.session_state["settings"])
        st.success("Settings saved.")

# ----- Audit -----
with tabs[5]:
    st.subheader("Audit Log (DB)")
    audit = load_events(500)
    if audit.empty:
        st.info("No events logged yet.")
    else:
        st.dataframe(audit)

# ----------------- Footer -----------------
st.markdown("---")
st.caption("MCP Demo Application — built for demonstration and extension. © Randy Singh / KNet Consulting")

