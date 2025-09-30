

#Agentic_Cybe_ML.py


"""

# Agentic Cyber ML Demo (single-file)



# Features:

# Multi-page: Threat Hunting | Incident Playbooks | Audit Logs

# Role-based (Admin / Analyst / Viewer) demo

# Generate up to 100 synthetic network logs

# Upload logs (CSV, JSON, XLSX)

# ML-based anomaly detection using IsolationForest (unsupervised)

# Auto-Contain: quarantines top suspicious IPs; visualized on a network map

# Download results (CSV / JSON / Excel)

# Red Reset button; other action buttons green (guaranteed via HTML anchors)

# Audit log records actions

# THIS APPLICATION IS DEVELOPED BY RANDY SINGH FORM KNET CONSULTING GROUP.



import streamlit as st

import pandas as pd

import numpy as np

from datetime import datetime, timedelta

from sklearn.ensemble import IsolationForest

from io import BytesIO

import json

import plotly.express as px

import networkx as nx

import urllib.parse



# -------------------------

# App configuration

# -------------------------

st.set_page_config(page_title="Agentic Cyber ML — Autonomous Threat Detection",

                   page_icon="🛡️", layout="wide")



# -------------------------

# Helper functions

# -------------------------

def now_iso():

    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")



def init_state():

    if "df" not in st.session_state:

        st.session_state.df = pd.DataFrame()

    if "audit" not in st.session_state:

        st.session_state.audit = []

    if "user" not in st.session_state:

        st.session_state.user = "guest"

    if "role" not in st.session_state:

        st.session_state.role = "Viewer"

    if "model" not in st.session_state:

        st.session_state.model = None

    if "model_stats" not in st.session_state:

        st.session_state.model_stats = {}



def audit_add(user, role, action, details=""):

    st.session_state.audit.insert(0, {

        "timestamp": now_iso(),

        "user": user,

        "role": role,

        "action": action,

        "details": details

    })



def generate_sample_logs(n=50):

    rng = np.random.default_rng(seed=42)

    timestamps = [datetime.utcnow() - timedelta(seconds=int(i*30)) for i in range(n)]

    src_ips = [f"10.{rng.integers(0,256)}.{rng.integers(0,256)}.{rng.integers(1,255)}" for _ in range(n)]

    dst_ips = [f"192.168.{rng.integers(0,256)}.{rng.integers(1,255)}" for _ in range(n)]

    protocol = rng.choice(["TCP","UDP","ICMP","HTTP","HTTPS","SSH","DNS"], size=n, p=[0.25,0.2,0.03,0.18,0.18,0.07,0.09])

    bytes_sent = rng.integers(40, 200000, size=n)

    # Inject some labeled malicious examples as a demo (sparse)

    malicious = np.zeros(n, dtype=int)

    # make a few spikes malicious

    spikes = rng.choice(n, size=max(1,n//15), replace=False)

    for s in spikes:

        bytes_sent[s] = int(bytes_sent[s] * rng.integers(5,50))

        malicious[s] = 1

    df = pd.DataFrame({

        "timestamp": timestamps,

        "src_ip": src_ips,

        "dst_ip": dst_ips,

        "protocol": protocol,

        "bytes": bytes_sent,

        # keep label field optional for real uploads; used only for evaluation if present

        "malicious_label": malicious

    })

    # ensure quarantined flag exists

    df["quarantined"] = False

    return df



def read_uploaded_file(uploaded_file):

    name = uploaded_file.name.lower()

    try:

        if name.endswith(".csv"):

            return pd.read_csv(uploaded_file)

        elif name.endswith(".json"):

            data = json.load(uploaded_file)

            return pd.json_normalize(data)

        elif name.endswith((".xls", ".xlsx")):

            return pd.read_excel(uploaded_file)

        else:

            st.error("Unsupported file type. Use CSV, JSON, or Excel.")

            return None

    except Exception as e:

        st.error(f"Error reading file: {e}")

        return None



def create_features(df):

    """

   # Create numeric features for the IsolationForest.

  # - bytes (numeric)

   # - protocol encoded

   # - optionally: count of dst per src in window (simple feature)

    """

    df = df.copy()

    # bytes

    df["bytes"] = pd.to_numeric(df.get("bytes", 0), errors="coerce").fillna(0)

    # protocol encoding

    if "protocol" in df.columns:

        df["proto_enc"] = df["protocol"].astype("category").cat.codes

    else:

        df["proto_enc"] = 0

    # src->dst pair traffic count (local aggregation)

    df["pair"] = df["src_ip"].astype(str) + "->" + df["dst_ip"].astype(str)

    counts = df["pair"].value_counts().to_dict()

    df["pair_count"] = df["pair"].map(counts).fillna(1)

    # keep only features

    features = df[["bytes","proto_enc","pair_count"]].astype(float)

    return df, features



def train_isolation_forest(features, cont=0.05):

    model = IsolationForest(n_estimators=200, contamination=cont, random_state=42, behaviour="new")

    model.fit(features)

    # decision_function higher -> more normal; negative -> anomaly

    return model



def score_with_iforest(df, model, features):

    df = df.copy()

    # decision_function: higher => more normal; we invert and min-max to 0-1 anomaly score

    raw = -model.decision_function(features)  # higher => more anomalous

    # map to 0-1

    minv, maxv = raw.min(), raw.max()

    if maxv - minv <= 0:

        norm = np.zeros_like(raw)

    else:

        norm = (raw - minv) / (maxv - minv)

    df["anomaly_score"] = norm.round(4)

    # set action thresholds

    df["action"] = "ALLOW"

    df.loc[df["anomaly_score"] >= 0.7, "action"] = "SUSPECT"

    df.loc[df["anomaly_score"] >= 0.9, "action"] = "BLOCK"

    # ensure quarantined column exists and persists existing quarantines

    if "quarantined" not in df.columns:

        df["quarantined"] = False

    return df



def convert_df_to_csv(df):

    return df.to_csv(index=False).encode("utf-8")



def convert_df_to_json(df):

    return df.to_json(orient="records", date_format="iso").encode("utf-8")



def convert_df_to_excel(df):

    buffer = BytesIO()

    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:

        df.to_excel(writer, index=False, sheet_name="results")

    return buffer.getvalue()



# -------------------------

# HTML button helper (guaranteed colors)

# Buttons implemented as anchor links that set ?action=... in URL

# -------------------------

def html_action_button(label, token, color_hex="#27ae60", size="14px"):

    href = "?" + urllib.parse.urlencode({"action": token})

    html = f"""

    <a href="{href}" style="

      display:inline-block;

      background:{color_hex};

      color:#fff;

      padding:10px 14px;

      text-decoration:none;

      border-radius:8px;

      font-weight:600;

      font-size:{size};

      margin:4px 2px;

    ">{label}</a>

    """

    st.markdown(html, unsafe_allow_html=True)



# -------------------------

# Initialize session state

# -------------------------

init_state()



# -------------------------

# Sidebar: Role & Navigation

# -------------------------

st.sidebar.title("Agentic Cyber ML")

st.sidebar.subheader("User / Role (demo)")

user_name = st.sidebar.text_input("Username", value=st.session_state.user)

role = st.sidebar.selectbox("Role", ["Admin", "Analyst", "Viewer"], index={"Admin":0,"Analyst":1,"Viewer":2}[st.session_state.role] if st.session_state.role in ["Admin","Analyst","Viewer"] else 2)

if st.sidebar.button("Set Role"):

    st.session_state.user = user_name if user_name.strip() else "guest"

    st.session_state.role = role

    audit_add(st.session_state.user, st.session_state.role, "SetRole", f"Role set to {role}")

    st.sidebar.success(f"Role set: {st.session_state.role}")



st.sidebar.markdown("---")

page = st.sidebar.radio("Pages", ["Threat Hunting", "Incident Playbooks", "Audit Logs"])

st.sidebar.markdown("---")

st.sidebar.caption("Note: This demo uses local role handling only (not secure).")



# -------------------------

# Read action param from URL

# -------------------------

query_params = st.experimental_get_query_params()

action_param = query_params.get("action", [None])[0]



# -------------------------

# Page: Threat Hunting

# -------------------------

if page == "Threat Hunting":

    st.title("🕵️ Threat Hunting (IsolationForest ML)")

    st.markdown("Use the controls on the left to generate/upload logs, run ML detection, visualize, auto-contain, and download results.")



    left, right = st.columns([1,2], gap="large")



    with left:

        st.header("Controls")

        # Generate sample data

        num = st.slider("Records to generate", min_value=10, max_value=100, value=50, step=10)

        if st.button("Generate Sample Logs"):

            df_gen = generate_sample_logs(num)

            st.session_state.df = df_gen

            # train model and score immediately

            df_feat, feats = create_features(st.session_state.df)

            # choose contamination rate adaptive (if labels exist, use ratio)

            cont = max(0.02, min(0.2, st.session_state.df.get("malicious_label", pd.Series(0)).mean() + 0.05))

            model = train_isolation_forest(feats, cont=cont)

            scored = score_with_iforest(df_feat, model, feats)

            st.session_state.df = scored

            st.session_state.model = model

            st.session_state.model_stats = {"contamination": cont}

            audit_add(st.session_state.user, st.session_state.role, "GenerateSample", f"{num} records; cont={cont:.3f}")

            st.success(f"Generated and scored {len(scored)} records (contamination={cont:.3f}).")



        st.markdown("---")

        # Upload

        uploaded = st.file_uploader("Upload logs (CSV / JSON / XLSX)", type=["csv","json","xls","xlsx"])

        if uploaded is not None:

            df_up = read_uploaded_file(uploaded)

            if df_up is not None:

                # Normalize columns: ensure src_ip,dst_ip,protocol,bytes exist

                required_cols = ["src_ip","dst_ip","protocol","bytes"]

                # try to infer if common keys different

                found = df_up.columns.str.lower()

                # rename guessable columns

                rename_map = {}

                for col in df_up.columns:

                    c = col.lower()

                    if "src" in c and "ip" in c:

                        rename_map[col] = "src_ip"

                    if "dst" in c and ("ip" in c or "dest" in c):

                        rename_map[col] = "dst_ip"

                    if "proto" in c:

                        rename_map[col] = "protocol"

                    if "byte" in c:

                        rename_map[col] = "bytes"

                    if "malicious" in c:

                        rename_map[col] = "malicious_label"

                df_up = df_up.rename(columns=rename_map)

                for rc in required_cols:

                    if rc not in df_up.columns:

                        df_up[rc] = "" if rc.endswith("_ip") else 0

                # fill timestamp if missing

                if "timestamp" not in df_up.columns:

                    df_up["timestamp"] = pd.Timestamp.utcnow()

                # ensure quarantined flag exists

                if "quarantined" not in df_up.columns:

                    df_up["quarantined"] = False

                st.session_state.df = df_up

                audit_add(st.session_state.user, st.session_state.role, "Upload", uploaded.name)

                st.success(f"Uploaded {uploaded.name} ({len(df_up)} rows).")

                # train & score

                df_feat, feats = create_features(st.session_state.df)

                cont = max(0.02, min(0.2, df_feat.get("malicious_label", pd.Series(0)).mean() + 0.05))

                model = train_isolation_forest(feats, cont=cont)

                scored = score_with_iforest(df_feat, model, feats)

                st.session_state.df = scored

                st.session_state.model = model

                st.session_state.model_stats = {"contamination": cont}

                audit_add(st.session_state.user, st.session_state.role, "TrainAndScoreUpload", f"cont={cont:.3f}")



        st.markdown("---")

        if st.button("Retrain & Rescore (current data)"):

            if st.session_state.df.empty:

                st.warning("No data available.")

            else:

                df_feat, feats = create_features(st.session_state.df)

                cont = max(0.02, min(0.2, df_feat.get("malicious_label", pd.Series(0)).mean() + 0.05))

                model = train_isolation_forest(feats, cont=cont)

                scored = score_with_iforest(df_feat, model, feats)

                # preserve quarantined state where previously quarantined

                if "quarantined" in st.session_state.df.columns:

                    prev_q = st.session_state.df.loc[st.session_state.df["quarantined"], "src_ip"].unique().tolist()

                    scored.loc[scored["src_ip"].isin(prev_q), "quarantined"] = True

                st.session_state.df = scored

                st.session_state.model = model

                st.session_state.model_stats = {"contamination": cont}

                audit_add(st.session_state.user, st.session_state.role, "RetrainRescore", f"cont={cont:.3f}")

                st.success("Retrained model and rescored data.")



        st.markdown("---")

        st.subheader("Actions")

        st.markdown("Auto-Contain will mark top suspicious source IPs as quarantined and log the action. (Role: Admin/Analyst)")

        html_action_button("🟢 Auto-Contain Top 5 IPs", "autocontain", color_hex="#27ae60")

        html_action_button("🟥 Reset / Clear All", "reset_all", color_hex="#e74c3c")



    with right:

        st.header("Visuals & Results")

        if st.session_state.df.empty:

            st.info("No data yet — generate sample logs or upload data.")

        else:

            df = st.session_state.df.copy()

            # KPIs

            c1, c2, c3, c4 = st.columns(4)

            c1.metric("Total Records", len(df))

            c2.metric("High Risk (>=0.8)", int((df["anomaly_score"]>=0.8).sum()))

            c3.metric("SUSPECT", int((df["action"]=="SUSPECT").sum()))

            c4.metric("QUARANTINED", int(df["quarantined"].sum()))



            st.markdown("### Anomaly Score Distribution")

            fig = px.histogram(df, x="anomaly_score", nbins=25, title="Anomaly Score Distribution")

            st.plotly_chart(fig, use_container_width=True, height=300)



            st.markdown("### Network Map (top 60 edges)")

            # create a graph from top edges (by bytes)

            try:

                top = df.sort_values("bytes", ascending=False).head(60)

                G = nx.from_pandas_edgelist(top, source="src_ip", target="dst_ip", create_using=nx.Graph())

                # nodes positions

                pos = nx.spring_layout(G, seed=42)

                node_x = []

                node_y = []

                node_text = []

                node_color = []

                for node in G.nodes():

                    x, y = pos[node]

                    node_x.append(x)

                    node_y.append(y)

                    node_text.append(node)

                    # quarantined if any record with src_ip == node is quarantined

                    is_q = False

                    if node in df["src_ip"].values:

                        is_q = df.loc[(df["src_ip"]==node) & (df["quarantined"]), "quarantined"].any()

                    node_color.append("red" if is_q else "green")

                edge_x = []

                edge_y = []

                for e in G.edges():

                    x0, y0 = pos[e[0]]

                    x1, y1 = pos[e[1]]

                    edge_x += [x0, x1, None]

                    edge_y += [y0, y1, None]

                edge_trace = px.line(x=edge_x, y=edge_y).data[0]

                # node scatter

                node_trace = px.scatter(x=node_x, y=node_y, color=node_color, labels={"color":"status"})

                node_trace.update_traces(marker=dict(size=12, line=dict(width=1, color="#111")))

                # show simple network by plotting both traces

                st.plotly_chart(node_trace, use_container_width=True, height=420)

            except Exception as e:

                st.warning(f"Network visualization error: {e}")



            st.markdown("### Top Source IPs by Avg Anomaly Score")

            try:

                top_src = df.groupby("src_ip").agg(avg_score=("anomaly_score","mean"), count=("anomaly_score","size"), quarantined=("quarantined","sum")).reset_index()

                top_src = top_src.sort_values(["avg_score","count"], ascending=[False, False]).head(15)

                fig2 = px.bar(top_src, x="src_ip", y="avg_score", color="quarantined", title="Top Source IPs by Avg Anomaly Score")

                st.plotly_chart(fig2, use_container_width=True, height=300)

            except Exception:

                st.warning("Error building top-src chart.")



            st.markdown("#### Sample Records (first 200 rows)")

            st.dataframe(df.head(200), use_container_width=True)



            st.markdown("#### Downloads")

            csv_bytes = convert_df_to_csv(df)

            json_bytes = convert_df_to_json(df)

            excel_bytes = convert_df_to_excel(df)

            dlc1, dlc2, dlc3 = st.columns(3)

            dlc1.download_button("Download CSV", csv_bytes, "detection_results.csv", "text/csv")

            dlc2.download_button("Download JSON", json_bytes, "detection_results.json", "application/json")

            dlc3.download_button("Download Excel", excel_bytes, "results.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")



# -------------------------

# Page: Incident Playbooks

# -------------------------

elif page == "Incident Playbooks":

    st.title("📘 Incident Playbooks")

    st.markdown("Predefined playbooks. Executing a playbook simulates actions (quarantine, block) and logs the activity.")

    playbooks = {

        "Contain Suspicious IPs": [

            "Identify top suspicious IPs",

            "Quarantine IPs",

            "Log & notify"

        ],

        "Investigate Large Outbound Transfer": [

            "Identify large bytes transfers",

            "Snapshot endpoints",

            "Open ticket"

        ]

    }

    pb = st.selectbox("Select Playbook", list(playbooks.keys()))

    st.write("Steps:")

    for i, step in enumerate(playbooks[pb], start=1):

        st.write(f"{i}. {step}")



    if st.button("Execute Playbook (simulate)"):

        if st.session_state.role not in ("Admin", "Analyst"):

            st.warning("Permission denied. Only Admin or Analyst may execute playbooks.")

        else:

            # Example: Contain Suspicious IPs -> quarantine top 5 avg anomaly src_ips

            if st.session_state.df.empty:

                st.warning("No data to act on.")

            else:

                df = st.session_state.df

                top_src = df.groupby("src_ip").agg(avg_score=("anomaly_score","mean")).reset_index().sort_values("avg_score", ascending=False)

                top5 = top_src.head(5)["src_ip"].tolist()

                st.session_state.df.loc[st.session_state.df["src_ip"].isin(top5), "quarantined"] = True

                audit_add(st.session_state.user, st.session_state.role, "PlaybookExecute", f"{pb}; quarantined: {','.join(top5)}")

                st.success(f"Executed playbook '{pb}'. Quarantined: {', '.join(top5)}")



    # Downloads for playbook results (current df view)

    st.markdown("---")

    st.subheader("Download Latest Results")

    if st.session_state.df.empty:

        st.info("No processed results to download.")

    else:

        df = st.session_state.df

        st.download_button("Download CSV", convert_df_to_csv(df), "latest_results.csv", "text/csv")

        st.download_button("Download JSON", convert_df_to_json(df), "latest_results.json", "application/json")

        st.download_button("Download Excel", convert_df_to_excel(df), "latest_results.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")



# -------------------------

# Page: Audit Logs

# -------------------------

else:  # Audit Logs

    st.title("🧾 Audit Logs")

    st.markdown("All session actions are recorded here.")

    df_a = pd.DataFrame(st.session_state.audit)

    if df_a.empty:

        st.info("No audit entries yet.")

    else:

        st.dataframe(df_a, use_container_width=True)

        st.markdown("### Download Audit Log")

        st.download_button("Download Audit CSV", convert_df_to_csv(df_a), "audit_log.csv", "text/csv")

        st.download_button("Download Audit JSON", convert_df_to_json(df_a), "audit_log.json", "application/json")

        st.download_button("Download Audit Excel", convert_df_to_excel(df_a), "audit_log.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")



# -------------------------

# URL Action Param Handling (Auto-Contain, Reset)

# Buttons above create ?action=token anchors

# -------------------------

if action_param:

    act = action_param

    # Reset all

    if act == "reset_all":

        st.session_state.df = pd.DataFrame()

        st.session_state.model = None

        st.session_state.model_stats = {}

        st.session_state.audit = []

        audit_add("system", "system", "ResetAll", "User triggered full reset")

        # clear param and reload

        st.experimental_set_query_params()

        st.experimental_rerun()



    # Auto-Contain top 5

    if act == "autocontain":

        # permission check

        if st.session_state.role not in ("Admin","Analyst"):

            st.warning("Permission denied: role must be Admin or Analyst to Auto-Contain.")

            audit_add(st.session_state.user, st.session_state.role, "AutoContainDenied", "Insufficient role")

            st.experimental_set_query_params()

        else:

            if st.session_state.df.empty:

                st.warning("No data to contain.")

                audit_add(st.session_state.user, st.session_state.role, "AutoContainFailed", "No data")

                st.experimental_set_query_params()

            else:

                df = st.session_state.df

                # group by src_ip avg anomaly_score, select top 5 not already quarantined

                top_src = df.groupby("src_ip").agg(avg_score=("anomaly_score","mean")).reset_index().sort_values("avg_score", ascending=False)

                # exclude already quarantined

                already = df.loc[df["quarantined"], "src_ip"].unique().tolist()

                top_src = top_src[~top_src["src_ip"].isin(already)]

                top5 = top_src.head(5)["src_ip"].tolist()

                if not top5:

                    st.info("No new IPs to quarantine.")

                    audit_add(st.session_state.user, st.session_state.role, "AutoContainNoOp", "No new IPs")

                    st.experimental_set_query_params()

                else:

                    st.session_state.df.loc[st.session_state.df["src_ip"].isin(top5), "quarantined"] = True

                    audit_add(st.session_state.user, st.session_state.role, "AutoContain", f"Quarantined: {','.join(top5)}")

                    st.success(f"Auto-Contained top {len(top5)} IPs: {', '.join(top5)}")

                    # clear param and reload to update UI

                    st.experimental_set_query_params()

                    st.experimental_rerun()



# -------------------------

# Footer / explanation

# -------------------------

st.markdown("---")

st.caption("Demo: IsolationForest used for anomaly detection (unsupervised). Replace model and data connectors for production-grade integration.")





