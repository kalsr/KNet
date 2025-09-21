# THIS APPLICATION IS DESIGNED & DEVELOPED BY RANDY SINGH FROM KNet CONSULTING.

# mcp_app_full.py

# MCP — Model Context Protocol (Complete Streamlit app with 5 use cases & colored GUI)

# Save as mcp_app_full.py and run: `streamlit run mcp_app_full.py`



import streamlit as st

import pandas as pd

import numpy as np

import json, io, os

from datetime import datetime

import matplotlib.pyplot as plt

from pathlib import Path



# -------------------------

# Configuration / paths

# -------------------------

DATA_DIR = Path("./data")

DATA_DIR.mkdir(exist_ok=True)

CONTEXT_STORE_PATH = DATA_DIR / "context_store.jsonl"   # persistent context (append per event)

SAMPLE_DATA_PATH = DATA_DIR / "sample_data.csv"



# -------------------------

# Styling: colored HTML buttons

# -------------------------

st.set_page_config(page_title="MCP — Model Context Protocol", layout="wide")



st.markdown(

    """

    <style>

    /* general page tweaks */

    .mcp-header { font-size:26px; font-weight:700; margin-bottom: 6px; }

    .mcp-sub { color: #6c757d; margin-bottom: 18px; }



    /* styled HTML buttons (anchor tags) */

    .mcp-btn {

      display:inline-block;

      padding:12px 18px;

      margin:6px 0;

      border-radius:8px;

      color: white;

      text-decoration: none;

      font-weight:600;

      box-shadow: 0 2px 6px rgba(0,0,0,0.12);

    }

    .mcp-blue { background: linear-gradient(180deg,#2f80ed,#2565d6); }

    .mcp-green { background: linear-gradient(180deg,#2ecc71,#22b45a); }

    .mcp-red { background: linear-gradient(180deg,#ec5f5f,#d64545); }

    .mcp-amber { background: linear-gradient(180deg,#f6c85f,#efb536); color:#111; }

    .mcp-indigo { background: linear-gradient(180deg,#6a5acd,#5b49c9); }

    .mcp-muted { background: #f0f2f5; color:#222; box-shadow:none; border:1px solid #e1e5ea; }



    /* callouts */

    .mcp-small { font-size:12px; color:#6c757d; margin-top:8px; }



    /* force table full width in main area */

    .streamlit-expanderHeader { font-weight:600; }

    </style>

    """,

    unsafe_allow_html=True,

)



# -------------------------

# Helper utilities

# -------------------------

def now_iso():

    return datetime.utcnow().isoformat() + "Z"



def append_to_context_store(event: dict):

    """Append JSON line to context store for persistence / audit."""

    event_record = event.copy()

    event_record.setdefault("ts", now_iso())

    with open(CONTEXT_STORE_PATH, "a", encoding="utf-8") as f:

        f.write(json.dumps(event_record, ensure_ascii=False) + "\n")



def load_context_store(n=200):

    if not CONTEXT_STORE_PATH.exists():

        return []

    lines = []

    with open(CONTEXT_STORE_PATH, "r", encoding="utf-8") as f:

        for line in f:

            try:

                lines.append(json.loads(line.strip()))

            except Exception:

                continue

    return lines[-n:]



def generate_sample_data(n=50, seed=None):

    rng = np.random.default_rng(int(seed) if (seed is not None and str(seed).strip().isdigit()) else None)

    categories = ["Normal", "Anomaly", "Warning", "Info"]

    rows = []

    base_ts = datetime.utcnow()

    for i in range(1, n+1):

        r = {

            "id": i,

            "timestamp": (base_ts).isoformat() + "Z",

            "score": float(np.round(rng.uniform(0, 1), 3)),

            "category": rng.choice(categories, p=[0.6,0.1,0.2,0.1]),

            "message": rng.choice([

                "User login", "File accessed", "Process started", "Timeout error",

                "High memory usage", "Configuration change", "Health check passed", "Permission denied"

            ])

        }

        rows.append(r)

    df = pd.DataFrame(rows)

    return df



def dataframe_to_csv_bytes(df):

    return df.to_csv(index=False).encode("utf-8")



def dataframe_to_json_bytes(df):

    return df.to_json(orient="records", force_ascii=False).encode("utf-8")



# -------------------------

# MCP core functions (use case implementations)

# -------------------------

def anomaly_detection_pipeline(df: pd.DataFrame):

    """Use case 1: Anomaly detection - flag low-score or unusual messages"""

    df = df.copy()

    # simple threshold on score; lower score means anomaly here (example)

    df["anomaly_flag"] = df["score"].apply(lambda s: "ANOMALY" if float(s) < 0.2 else "OK")

    # add simple anomaly reason heuristic

    df["anomaly_reason"] = df.apply(lambda r: "low_score" if r["anomaly_flag"]=="ANOMALY" else "", axis=1)

    append_to_context_store({"event":"anomaly_detection_run", "records": len(df)})

    return df



def policy_compliance_monitor(df: pd.DataFrame):

    """Use case 2: Check messages vs simple compliance policies"""

    df = df.copy()

    # Example policy: messages containing 'permission', 'denied' => violation

    def check_policy(msg):

        msg_l = str(msg).lower()

        if "permission" in msg_l or "denied" in msg_l or "config" in msg_l:

            return "VIOLATION"

        if "timeout" in msg_l or "error" in msg_l:

            return "WARNING"

        return "OK"

    df["policy_state"] = df["message"].apply(check_policy)

    append_to_context_store({"event":"policy_monitor_run", "records": len(df)})

    return df



def model_drift_metrics(df: pd.DataFrame, history_n=100):

    """Use case 3: Model drift - compute simple drift stat vs historical scores stored in context."""

    # Compute current distribution stats

    df = df.copy()

    stats = {"count": len(df)}

    if len(df)>0:

        stats.update({

            "mean_score": float(df["score"].mean()),

            "std_score": float(df["score"].std(ddof=0) if len(df)>1 else 0.0),

            "min_score": float(df["score"].min()),

            "max_score": float(df["score"].max())

        })

    # For demo, compare to stored context mean (if available)

    ctx = load_context_store(n=history_n)

    historical_scores = []

    for e in ctx:

        # context store events might record previous mean scores

        if "mean_score" in e:

            historical_scores.append(e["mean_score"])

    if historical_scores:

        stats["historical_mean_of_mean_scores"] = float(np.mean(historical_scores))

        stats["drift_delta"] = stats.get("mean_score", 0.0) - stats["historical_mean_of_mean_scores"]

    else:

        stats["historical_mean_of_mean_scores"] = None

        stats["drift_delta"] = None

    append_to_context_store({"event":"drift_metrics_computed", "mean_score": stats.get("mean_score")})

    return stats



def data_labeling_assist(df: pd.DataFrame, top_n=10):

    """Use case 4: Present low-confidence items for labeling (simulate by 'Review' inference)"""

    df = df.copy()

    # define low-confidence region -> label candidates

    df["uncertain"] = df["score"].apply(lambda s: True if 0.35 <= float(s) <= 0.6 else False)

    candidates = df[df["uncertain"]].head(top_n)

    append_to_context_store({"event":"labeling_task_created", "candidates": len(candidates)})

    return df, candidates



def incident_triage_assistant(df: pd.DataFrame):

    """Use case 5: Prioritize incidents by severity combining score & policy flags"""

    df = df.copy()

    # severity score = (1 - score) * base + policy_weight

    def severity_calc(row):

        base = (1.0 - float(row["score"])) * 100

        policy_weight = 50 if (row.get("policy_state","")=="VIOLATION") else (20 if row.get("anomaly_flag","")=="ANOMALY" else 0)

        return base + policy_weight

    df["severity"] = df.apply(severity_calc, axis=1)

    df = df.sort_values("severity", ascending=False).reset_index(drop=True)

    append_to_context_store({"event":"incident_triage_run", "top_severity": float(df["severity"].iloc[0]) if len(df)>0 else None})

    return df



# -------------------------

# Page layout / sidebar

# -------------------------

st.markdown('<div class="mcp-header">Model Context Protocol (MCP) — Interactive Demo</div>', unsafe_allow_html=True)

st.markdown('<div class="mcp-sub">A demonstration framework: context store, handlers, policies, audit, and exports.</div>', unsafe_allow_html=True)



# Use HTML "buttons" (links) to create stable colored action triggers via query params

# We'll also provide fallback Streamlit buttons for convenience.



# Build action links

base_qs = st.experimental_get_query_params()

def make_action_link(action, label, css_class):

    # create a query param anchor that will reload page with ?action=... 

    return f'<a href="?action={action}" class="mcp-btn {css_class}">{label}</a>'



# Left control column and right main column

left, right = st.columns([1, 3])



with left:

    st.markdown(make_action_link("gen_default", "Generate Sample Data (50)", "mcp-blue"), unsafe_allow_html=True)

    st.markdown(make_action_link("gen_custom", "Generate with Options", "mcp-indigo"), unsafe_allow_html=True)

    st.markdown(make_action_link("clear", "Clear / Reset", "mcp-red"), unsafe_allow_html=True)

    st.markdown(make_action_link("upload", "Upload File", "mcp-green"), unsafe_allow_html=True)

    st.markdown(make_action_link("run_inference", "Run Inference (Anomaly)", "mcp-amber"), unsafe_allow_html=True)

    st.markdown(make_action_link("apply_policy", "Apply Policy (Compliance)", "mcp-blue"), unsafe_allow_html=True)

    st.markdown(make_action_link("drift", "Model Drift Dashboard", "mcp-indigo"), unsafe_allow_html=True)

    st.markdown(make_action_link("label", "Data Labeling Assist", "mcp-green"), unsafe_allow_html=True)

    st.markdown(make_action_link("triage", "Incident Triage Assistant", "mcp-amber"), unsafe_allow_html=True)



    st.markdown("<div class='mcp-small'>You can also use the native controls below to upload and download.</div>", unsafe_allow_html=True)

    st.write("---")

    # native upload + quick generate controls

    uploaded = st.file_uploader("Upload data (CSV/JSON/TXT)", type=["csv","json","txt"])

    st.markdown("**Sample generator options**")

    sample_n = st.number_input("Sample size", min_value=5, max_value=5000, value=50, step=5)

    sample_seed = st.text_input("Random seed (optional)")



    if st.button("Generate Sample Data (native)"):

        df = generate_sample_data(int(sample_n), sample_seed or None)

        st.session_state["df"] = df

        st.success(f"Generated {len(df)} records (native).")

        append_to_context_store({"event":"sample_data_generated", "n": len(df), "seed": sample_seed or None})



    if st.button("Clear / Reset (native)"):

        st.session_state.pop("df", None)

        st.session_state.pop("audit", None)

        st.success("Session cleared.")



with right:

    # Load df from session if present

    df = st.session_state.get("df", None)



    # If upload via native control

    if uploaded is not None:

        try:

            content = uploaded.read()

            uploaded.seek(0)

            # try JSON

            try:

                obj = json.loads(content.decode("utf-8"))

                df = pd.json_normalize(obj)

            except Exception:

                # CSV fallback

                uploaded.seek(0)

                df = pd.read_csv(io.BytesIO(content))

            st.session_state["df"] = df

            st.success(f"Loaded {len(df)} records from upload.")

            append_to_context_store({"event":"file_uploaded", "filename": uploaded.name, "records": len(df)})

        except Exception as e:

            st.error(f"Failed to parse uploaded file: {e}")



    # Check query param action triggers (links)

    q = st.experimental_get_query_params()

    action = q.get("action", [None])[0]



    # Helper to show dataset

    def show_data_table(df_local):

        st.subheader("Data Preview")

        st.dataframe(df_local.head(500))



    # Process actions triggered by the HTML links:

    if action == "gen_default":

        df = generate_sample_data(50)

        st.session_state["df"] = df

        st.experimental_set_query_params()  # clear query param

        st.experimental_rerun()



    if action == "gen_custom":

        # show simple modal-like controls inline

        st.info("Generate custom sample data")

        n_gen = st.number_input("Number of records", min_value=5, max_value=2000, value=50, key="gc_n")

        seed_gen = st.text_input("Seed (optional)", key="gc_seed")

        if st.button("Generate now (custom)"):

            df = generate_sample_data(int(n_gen), seed_gen or None)

            st.session_state["df"] = df

            append_to_context_store({"event":"sample_data_generated", "n": int(n_gen), "seed": seed_gen or None})

            st.success(f"Generated {len(df)} records.")

            st.experimental_set_query_params()

            st.experimental_rerun()



    if action == "clear":

        st.session_state.pop("df", None)

        st.session_state.pop("audit", None)

        append_to_context_store({"event":"session_cleared"})

        st.experimental_set_query_params()

        st.experimental_rerun()



    if action == "upload":

        st.info("Use the Upload control on the left to select a CSV/JSON/TXT file. After upload the file will be parsed into the app.")

        st.experimental_set_query_params()



    # If no df: show instructions

    df = st.session_state.get("df", None)

    if df is None:

        st.warning("No data loaded. Use 'Generate Sample Data' or 'Upload' to begin.")

    else:

        show_data_table(df)



    # Action buttons (native) for use cases

    st.markdown("---")

    st.subheader("Run Use Cases / Actions")



    # Run Inference (Anomaly Detection pipeline)

    if (action == "run_inference") or st.button("Run Inference (Anomaly Detection)"):

        df = st.session_state.get("df")

        if df is None:

            st.warning("No data present.")

        else:

            # run anomaly detection pipeline

            df = anomaly_detection_pipeline(df)

            st.session_state["df"] = df

            st.success("Anomaly detection completed.")

            st.experimental_set_query_params()



    # Policy compliance

    if (action == "apply_policy") or st.button("Apply Policy: Compliance Monitor"):

        df = st.session_state.get("df")

        if df is None:

            st.warning("No data present.")

        else:

            df = policy_compliance_monitor(df)

            st.session_state["df"] = df

            st.success("Policy compliance check complete.")

            st.experimental_set_query_params()



    # Model drift dashboard

    if (action == "drift") or st.button("Model Drift: Compute Metrics"):

        df = st.session_state.get("df")

        if df is None:

            st.warning("No data present.")

        else:

            stats = model_drift_metrics(df)

            st.success("Drift metrics computed.")

            st.json(stats)

            st.experimental_set_query_params()



    # Data labeling assist

    if (action == "label") or st.button("Data Labeling Assist"):

        df = st.session_state.get("df")

        if df is None:

            st.warning("No data present.")

        else:

            df, candidates = data_labeling_assist(df, top_n=25)

            st.session_state["df"] = df

            st.subheader("Labeling Candidates (low-confidence / uncertain)")

            if candidates.empty:

                st.write("No candidates found.")

            else:

                # show candidates and allow quick labeling

                labeled = []

                with st.form("label_form"):

                    sel_index = st.multiselect("Select rows to label (by index in displayed table)", list(candidates.index))

                    label_value = st.selectbox("Label value to apply", ["MANUAL_REVIEW", "CONFIRMED_ANOMALY", "FALSE_POSITIVE"])

                    submit = st.form_submit_button("Apply label")

                    if submit:

                        for idx in sel_index:

                            st.session_state["df"].at[idx, "human_label"] = label_value

                        append_to_context_store({"event":"labels_applied", "count": len(sel_index), "label": label_value})

                        st.success(f"Applied label '{label_value}' to {len(sel_index)} rows.")

                st.dataframe(candidates)



            st.experimental_set_query_params()



    # Incident triage

    if (action == "triage") or st.button("Incident Triage Assistant"):

        df = st.session_state.get("df")

        if df is None:

            st.warning("No data present.")

        else:

            # ensure policy and anomaly columns exist

            if "policy_state" not in df.columns:

                df = policy_compliance_monitor(df)

            if "anomaly_flag" not in df.columns:

                df = anomaly_detection_pipeline(df)

            df = incident_triage_assistant(df)

            st.session_state["df"] = df

            st.subheader("Top incidents (by severity)")

            st.dataframe(df.head(20))

            st.experimental_set_query_params()



    # Visualizations (pie charts)

    st.markdown("---")

    st.subheader("Visualizations")

    if df is not None and len(df)>0:

        try:

            fig, axes = plt.subplots(1, 2, figsize=(10,4))

            # Category distribution

            cat_counts = df["category"].value_counts()

            axes[0].pie(cat_counts.values, labels=cat_counts.index, autopct="%1.1f%%", startangle=90)

            axes[0].set_title("Category Distribution")

            # Inference / flags distribution

            flag_col = "anomaly_flag" if "anomaly_flag" in df.columns else ("policy_state" if "policy_state" in df.columns else None)

            if flag_col:

                fcounts = df[flag_col].value_counts()

                axes[1].pie(fcounts.values, labels=fcounts.index, autopct="%1.1f%%", startangle=90)

                axes[1].set_title(flag_col.replace("_"," ").title())

            else:

                axes[1].text(0.5, 0.5, "Run inference / policy to see flags", ha="center", va="center")

            st.pyplot(fig)

        except Exception as e:

            st.error(f"Chart generation failed: {e}")

    else:

        st.info("No data to visualize.")



    # Export / download

    st.markdown("---")

    st.subheader("Export / Save")

    if df is not None:

        st.download_button("⬇️ Download CSV", data=dataframe_to_csv_bytes(df), file_name="mcp_results.csv", mime="text/csv")

        st.download_button("⬇️ Download JSON", data=dataframe_to_json_bytes(df), file_name="mcp_results.json", mime="application/json")



    # Save to persistent context store (append snapshot)

    if st.button("Save Snapshot to Context Store"):

        df = st.session_state.get("df")

        if df is None:

            st.warning("No data to save.")

        else:

            # write a summary event with mean score and count

            event = {

                "event": "snapshot",

                "records": len(df),

                "mean_score": float(df["score"].mean()) if "score" in df.columns else None,

                "min_score": float(df["score"].min()) if "score" in df.columns else None,

            }

            append_to_context_store(event)

            st.success("Snapshot appended to context store.")



    # Audit log quick view

    st.markdown("---")

    st.subheader("Audit Log (recent context events)")

    audit = load_context_store(200)

    if len(audit) == 0:

        st.write("No audit events yet.")

    else:

        # show latest 30 events

        st.dataframe(pd.DataFrame(audit[-30:][::-1]))



# Footer / notes

st.markdown("---")

st.caption("MCP Demo Application was designed by Randy Singh — Application uses the colored action buttons to step through each use case. Extend handlers and policies for real deployments.")









