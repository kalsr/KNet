


# Agentic_Cyber_ML.py
# Agentic Cyber ML Demo (single-file)

# Features:
#- Multi-page: Threat Hunting | Incident Playbooks | Audit Logs
#- Role-based (Admin / Analyst / Viewer) demo
#- Generate up to 100 synthetic network logs
#- Upload logs (CSV, JSON, XLSX)
#- ML-based anomaly detection using IsolationForest (unsupervised)
#- Auto-Contain: quarantines top suspicious IPs; visualized on a network map
#- Download results (CSV / JSON / Excel)
#- Red Reset button; other action buttons green
#- Audit log records actions

# THIS APPLICATION IS DEVELOPED BY RANDY SINGH FROM KNET CONSULTING GROUP.

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
import base64

# -------------------------
# App config
# -------------------------
st.set_page_config(page_title="Agentic Cyber ML — Autonomous Threat Detection",
                   page_icon="🛡️", layout="wide")

# -------------------------
# Helpers
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
    if "playbooks" not in st.session_state:
        st.session_state.playbooks = []
    if "last_action" not in st.session_state:
        st.session_state.last_action = None

def audit_add(user, role, action, details=""):
    entry = {
        "timestamp": now_iso(),
        "user": user,
        "role": role,
        "action": action,
        "details": details
    }
    st.session_state.audit.insert(0, entry)

def generate_sample_logs(n=50):
    rng = np.random.default_rng(seed=42)
    timestamps = [datetime.utcnow() - timedelta(seconds=int(i*30)) for i in range(n)]
    src_ips = [f"10.{rng.integers(0,256)}.{rng.integers(0,256)}.{rng.integers(1,255)}" for _ in range(n)]
    dst_ips = [f"192.168.{rng.integers(0,256)}.{rng.integers(1,255)}" for _ in range(n)]
    protocol = rng.choice(["TCP","UDP","ICMP","HTTP","HTTPS","SSH","DNS"], size=n,
                          p=[0.25,0.2,0.03,0.18,0.18,0.07,0.09])
    bytes_sent = rng.integers(40, 200000, size=n)
    malicious = np.zeros(n, dtype=int)
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
        "malicious_label": malicious
    })
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
    # safe operations: create numeric features and return features matrix
    df = df.copy()
    df["bytes"] = pd.to_numeric(df.get("bytes", 0), errors="coerce").fillna(0)
    if "protocol" in df.columns:
        df["proto_enc"] = df["protocol"].astype("category").cat.codes
    else:
        df["proto_enc"] = 0
    df["pair"] = df["src_ip"].astype(str) + "->" + df["dst_ip"].astype(str)
    counts = df["pair"].value_counts().to_dict()
    df["pair_count"] = df["pair"].map(counts).fillna(1)
    features = df[["bytes","proto_enc","pair_count"]].astype(float)
    return df, features

def train_isolation_forest(features, cont=0.05):
    # scikit-learn modern params; removed deprecated behaviour param
    model = IsolationForest(n_estimators=200, contamination=cont, random_state=42)
    model.fit(features)
    return model

def score_with_iforest(df, model, features):
    df = df.copy()
    raw = -model.decision_function(features)  # higher -> more anomalous
    minv, maxv = raw.min(), raw.max()
    if maxv - minv <= 0:
        norm = np.zeros_like(raw)
    else:
        norm = (raw - minv) / (maxv - minv)
    df["anomaly_score"] = norm.round(4)
    df["action"] = "ALLOW"
    df.loc[df["anomaly_score"] >= 0.7, "action"] = "SUSPECT"
    df.loc[df["anomaly_score"] >= 0.9, "action"] = "BLOCK"
    if "quarantined" not in df.columns:
        df["quarantined"] = False
    return df

def convert_df_to_csv_bytes(df):
    return df.to_csv(index=False).encode("utf-8")

def convert_df_to_json_bytes(df):
    return df.to_json(orient="records", date_format="iso").encode("utf-8")

def convert_df_to_excel_bytes(df):
    buffer = BytesIO()
    try:
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="results")
    except Exception:
        # fallback if openpyxl not available
        df.to_excel(buffer, index=False, sheet_name="results")
    return buffer.getvalue()

def html_action_button(label, token, color_hex="#27ae60", size="14px"):
    href = "?" + urllib.parse.urlencode({"action": token})
    html = f"""
    <a href="{href}" style="
      display:inline-block;
      background:{color_hex};
      color:#fff;
      padding:8px 12px;
      text-decoration:none;
      border-radius:8px;
      font-weight:600;
      font-size:{size};
      margin:4px 4px;
    ">{label}</a>
    """
    st.markdown(html, unsafe_allow_html=True)

def download_link_bytes(data_bytes, filename, label):
    b64 = base64.b64encode(data_bytes).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}">{label}</a>'
    st.markdown(href, unsafe_allow_html=True)

def build_network_figure(df):
    # Build a simple network layout for top src/dst relationships
    if df.empty:
        return None
    # Use top N pairs
    df_pairs = df.copy()
    df_pairs["pair"] = df_pairs["src_ip"].astype(str) + "->" + df_pairs["dst_ip"].astype(str)
    top = df_pairs.groupby(["src_ip","dst_ip"]).size().reset_index(name="count").sort_values("count", ascending=False).head(40)
    G = nx.DiGraph()
    for _, row in top.iterrows():
        s = row["src_ip"]; d = row["dst_ip"]; c = int(row["count"])
        G.add_node(s); G.add_node(d)
        G.add_edge(s, d, weight=c)
    if len(G) == 0:
        return None
    pos = nx.spring_layout(G, seed=42)
    xs = []; ys = []; texts = []
    for n, p in pos.items():
        xs.append(p[0]); ys.append(p[1]); texts.append(str(n))
    edge_x = []
    edge_y = []
    edge_w = []
    for u,v,data in G.edges(data=True):
        x0,y0 = pos[u]; x1,y1 = pos[v]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]
        edge_w.append(data.get("weight",1))
    # node scatter
    node_df = pd.DataFrame({"x": xs, "y": ys, "label": texts})
    fig = px.scatter(node_df, x="x", y="y", hover_name="label", size_max=20)
    # add edges as lines
    for i in range(0, len(edge_x), 3):
        # slice edges
        seg_x = edge_x[i:i+3]; seg_y = edge_y[i:i+3]
        fig.add_shape(type="line", x0=seg_x[0], y0=seg_y[0], x1=seg_x[1], y1=seg_y[1],
                      line=dict(width=1, color="LightSeaGreen"))
    fig.update_layout(xaxis=dict(visible=False), yaxis=dict(visible=False), showlegend=False, height=450)
    return fig

# -------------------------
# Initialize state
# -------------------------
init_state()

# -------------------------
# Sidebar (role + nav)
# -------------------------
st.sidebar.title("Agentic Cyber ML")
st.sidebar.subheader("User / Role (demo)")
user_name = st.sidebar.text_input("Username", value=st.session_state.user)
role_select = st.sidebar.selectbox("Role", ["Admin", "Analyst", "Viewer"],
                                   index=["Admin","Analyst","Viewer"].index(st.session_state.role) if st.session_state.role in ["Admin","Analyst","Viewer"] else 2)
if st.sidebar.button("Set Role"):
    st.session_state.user = user_name if user_name.strip() else "guest"
    st.session_state.role = role_select
    audit_add(st.session_state.user, st.session_state.role, "SetRole", f"Role set to {role_select}")
    st.sidebar.success(f"Role set: {st.session_state.role}")

st.sidebar.markdown("---")
page = st.sidebar.radio("Pages", ["Threat Hunting", "Incident Playbooks", "Audit Logs"])
st.sidebar.markdown("---")
st.sidebar.caption("Note: demo only — local role handling (not secure).")

# -------------------------
# Parse action param from url (anchor-based html_action_button uses ?action=)
# -------------------------
query_params = st.query_params
action_param = None
if isinstance(query_params, dict):
    action_param = query_params.get("action", [None])[0] if "action" in query_params else None

# -------------------------
# Top UI area: action anchors (generate/upload/train/score/contain/reset)
# -------------------------
col_top_left, col_top_right = st.columns([3,1])
with col_top_left:
    st.markdown("### Agentic Cyber ML — Autonomous Threat Detection Demo")
    st.markdown("Generate sample logs, upload data, run unsupervised anomaly detection, auto-contain suspicious IPs, and download results.")
with col_top_right:
    # Red Reset anchor
    href = "?" + urllib.parse.urlencode({"action": "reset"})
    reset_html = f"""
    <a href="{href}" style="
      display:inline-block;
      background:#e74c3c;
      color:#fff;
      padding:8px 10px;
      text-decoration:none;
      border-radius:8px;
      font-weight:700;
      font-size:13px;
    ">Reset</a>
    """
    st.markdown(reset_html, unsafe_allow_html=True)

# Provide common anchors
st.markdown("---")
action_row = st.container()
with action_row:
    html_action_button("Generate Sample Logs", "generate", color_hex="#27ae60")
    html_action_button("Upload Logs", "upload", color_hex="#27ae60")
    html_action_button("Train/Score (Run ML)", "run_ml", color_hex="#27ae60")
    html_action_button("Auto-Contain Top Suspicious", "auto_contain", color_hex="#27ae60")
    html_action_button("Download CSV", "download_csv", color_hex="#2980b9")
    html_action_button("Download JSON", "download_json", color_hex="#2980b9")
    html_action_button("Download XLSX", "download_xlsx", color_hex="#2980b9")

# -------------------------
# Action handling for anchors (simple)
# -------------------------
def handle_action_token(token):
    st.session_state.last_action = token
    if token == "generate":
        df_new = generate_sample_logs(80)
        st.session_state.df = df_new
        audit_add(st.session_state.user, st.session_state.role, "Generate", "Generated 80 sample logs")
        st.success("Sample logs generated (80).")
    elif token == "upload":
        # open file uploader in a modal-like area below (we'll just signal)
        audit_add(st.session_state.user, st.session_state.role, "UploadRequested", "User requested upload via anchor")
        st.info("Use the upload widget below to pick a file (CSV / JSON / XLSX).")
    elif token == "run_ml":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No logs available — generate or upload logs first.")
            return
        df, features = create_features(st.session_state.df)
        model = train_isolation_forest(features, cont=0.05)
        scored = score_with_iforest(df, model, features)
        st.session_state.df = scored
        st.session_state.model = model
        st.session_state.model_stats = {"contamination":0.05, "n_samples": len(features)}
        audit_add(st.session_state.user, st.session_state.role, "RunML", f"Trained IsolationForest on {len(features)} records")
        st.success("ML run completed — anomaly scores added.")
    elif token == "auto_contain":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No logs available to contain.")
            return
        df = st.session_state.df.copy()
        # quarantine top anomalous src_ips
        top_block = df.sort_values("anomaly_score", ascending=False).head(10)
        ips_to_quarantine = top_block["src_ip"].value_counts().index.tolist()
        df.loc[df["src_ip"].isin(ips_to_quarantine), "quarantined"] = True
        st.session_state.df = df
        audit_add(st.session_state.user, st.session_state.role, "AutoContain", f"Quarantined {len(ips_to_quarantine)} src_ip(s)")
        st.success(f"Quarantined top {len(ips_to_quarantine)} source IPs.")
    elif token == "download_csv":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No data to download.")
            return
        csvb = convert_df_to_csv_bytes(st.session_state.df)
        download_link_bytes(csvb, "agentic_results.csv", "Click here to download CSV")
        audit_add(st.session_state.user, st.session_state.role, "Download", "Downloaded CSV")
    elif token == "download_json":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No data to download.")
            return
        jsb = convert_df_to_json_bytes(st.session_state.df)
        download_link_bytes(jsb, "agentic_results.json", "Click here to download JSON")
        audit_add(st.session_state.user, st.session_state.role, "Download", "Downloaded JSON")
    elif token == "download_xlsx":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No data to download.")
            return
        xb = convert_df_to_excel_bytes(st.session_state.df)
        download_link_bytes(xb, "agentic_results.xlsx", "Click here to download XLSX")
        audit_add(st.session_state.user, st.session_state.role, "Download", "Downloaded XLSX")
    elif token == "reset":
        st.session_state.df = pd.DataFrame()
        st.session_state.model = None
        st.session_state.model_stats = {}
        audit_add(st.session_state.user, st.session_state.role, "Reset", "Application reset by user")
        st.experimental_set_query_params()  # clear url params
        st.success("Application reset.")
    else:
        # unknown token
        st.info(f"Action: {token}")

if action_param:
    # handle token (note: this executes on page load when action param present)
    try:
        handle_action_token(action_param)
    except Exception as e:
        st.error(f"Action error: {e}")

# -------------------------
# Page: Threat Hunting
# -------------------------
if page == "Threat Hunting":
    st.header("🕵️ Threat Hunting (IsolationForest ML)")
    left, right = st.columns([2,1])
    with left:
        st.subheader("Data Controls")
        # Upload widget
        uploaded = st.file_uploader("Upload logs (CSV / JSON / XLSX)", type=["csv","json","xls","xlsx"])
        if uploaded is not None:
            df_u = read_uploaded_file(uploaded)
            if df_u is not None:
                # basic normalization: require timestamp, src_ip, dst_ip, protocol, bytes
                st.session_state.df = df_u
                # ensure columns exist
                for c in ["timestamp","src_ip","dst_ip","protocol","bytes","quarantined"]:
                    if c not in st.session_state.df.columns:
                        if c == "quarantined":
                            st.session_state.df[c] = False
                        else:
                            st.session_state.df[c] = ""
                audit_add(st.session_state.user, st.session_state.role, "Upload", f"Uploaded file: {uploaded.name}")
                st.success(f"Uploaded: {uploaded.name} ({len(st.session_state.df)} records).")
        st.markdown("**Quick actions**")
        if st.button("Generate 50 sample logs"):
            df_new = generate_sample_logs(50)
            st.session_state.df = df_new
            audit_add(st.session_state.user, st.session_state.role, "Generate", "Generated 50 sample logs")
            st.success("Generated 50 sample logs.")
        # ML controls
        st.markdown("**Machine Learning**")
        cont = st.slider("Contamination (expected fraction of anomalies)", min_value=0.01, max_value=0.2, value=0.05, step=0.01)
        if st.button("Train & Score (IsolationForest)"):
            if st.session_state.df is None or st.session_state.df.empty:
                st.warning("No data to train on. Generate or upload logs first.")
            else:
                df, feats = create_features(st.session_state.df)
                model = train_isolation_forest(feats, cont=cont)
                scored = score_with_iforest(df, model, feats)
                st.session_state.df = scored
                st.session_state.model = model
                st.session_state.model_stats = {"contamination": cont, "n_samples": len(feats)}
                audit_add(st.session_state.user, st.session_state.role, "TrainScore", f"Trained model on {len(feats)} rows")
                st.success("Model trained and anomaly scores computed.")
        st.markdown("**Containment**")
        if st.button("Auto-Contain Top 5 Suspicious (by src_ip)"):
            if st.session_state.df is None or st.session_state.df.empty:
                st.warning("No data to contain.")
            else:
                df = st.session_state.df.copy()
                top_block = df.sort_values("anomaly_score", ascending=False).head(10)
                ips_to_quarantine = top_block["src_ip"].value_counts().index.tolist()[:5]
                df.loc[df["src_ip"].isin(ips_to_quarantine), "quarantined"] = True
                st.session_state.df = df
                audit_add(st.session_state.user, st.session_state.role, "AutoContain", f"Quarantined {len(ips_to_quarantine)} IPs")
                st.success(f"Quarantined {len(ips_to_quarantine)} src_ip(s).")
        st.markdown("---")
        st.markdown("**Download current results**")
        if st.session_state.df is not None and not st.session_state.df.empty:
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.download_button("Download CSV", data=convert_df_to_csv_bytes(st.session_state.df),
                                   file_name="agentic_results.csv", mime="text/csv")
            with col_b:
                st.download_button("Download JSON", data=convert_df_to_json_bytes(st.session_state.df),
                                   file_name="agentic_results.json", mime="application/json")
            with col_c:
                try:
                    st.download_button("Download XLSX", data=convert_df_to_excel_bytes(st.session_state.df),
                                       file_name="agentic_results.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                except Exception:
                    st.download_button("Download XLSX", data=convert_df_to_excel_bytes(st.session_state.df),
                                       file_name="agentic_results.xlsx", mime="application/vnd.ms-excel")
        else:
            st.info("No results to download yet.")
    with right:
        st.subheader("Current Data Snapshot")
        if st.session_state.df is None or st.session_state.df.empty:
            st.info("No logs loaded. Generate or upload logs to begin.")
        else:
            st.write(f"Records: {len(st.session_state.df)}")
            preview = st.session_state.df.head(200)
            st.dataframe(preview)
        st.markdown("**Model Stats**")
        st.json(st.session_state.model_stats if st.session_state.model_stats else {"status":"no model"})

    st.markdown("---")
    st.subheader("Visualizations")
    viz_col1, viz_col2 = st.columns([1,1])
    with viz_col1:
        st.markdown("**Top anomalous records**")
        if st.session_state.df is not None and not st.session_state.df.empty and "anomaly_score" in st.session_state.df.columns:
            topn = st.session_state.df.sort_values("anomaly_score", ascending=False).head(25)
            fig = px.bar(topn, x="src_ip", y="anomaly_score", hover_data=["dst_ip","protocol","bytes"], title="Top anomalies by src_ip")
            fig.update_layout(xaxis_tickangle=-45, height=400)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No anomaly scores yet. Run ML.")
    with viz_col2:
        st.markdown("**Network Map (top pairs)**")
        fig_net = build_network_figure(st.session_state.df if st.session_state.df is not None else pd.DataFrame())
        if fig_net is not None:
            st.plotly_chart(fig_net, use_container_width=True)
        else:
            st.info("Network graph empty — generate/upload logs.")

# -------------------------
# Page: Incident Playbooks
# -------------------------
elif page == "Incident Playbooks":
    st.header("📘 Incident Playbooks")
    st.write("Create, view, and update incident playbooks. These are demo templates for response actions.")
    # list existing playbooks
    if st.session_state.playbooks:
        for i, pb in enumerate(st.session_state.playbooks):
            with st.expander(f"Playbook #{i+1}: {pb.get('title','Untitled')} - Status: {pb.get('status','open')}"):
                st.write("**Description**")
                st.write(pb.get("description",""))
                st.write("**Steps**")
                for step in pb.get("steps", []):
                    st.write(f"- {step}")
                cols = st.columns(3)
                if cols[0].button(f"Mark Mitigated #{i}", key=f"mit_{i}"):
                    st.session_state.playbooks[i]["status"] = "mitigated"
                    audit_add(st.session_state.user, st.session_state.role, "PlaybookMitigated", f"Playbook #{i+1} mitigated")
                    st.success("Marked mitigated.")
                if cols[1].button(f"Clone #{i}", key=f"clone_{i}"):
                    st.session_state.playbooks.append(dict(st.session_state.playbooks[i]))
                    audit_add(st.session_state.user, st.session_state.role, "PlaybookClone", f"Cloned playbook #{i+1}")
                    st.success("Cloned.")
                if cols[2].button(f"Delete #{i}", key=f"del_{i}"):
                    st.session_state.playbooks.pop(i)
                    audit_add(st.session_state.user, st.session_state.role, "PlaybookDelete", f"Deleted playbook #{i+1}")
                    st.success("Deleted.")
    else:
        st.info("No playbooks yet. Create one below.")

    st.markdown("### Create new playbook")
    new_title = st.text_input("Playbook title", key="pb_title")
    new_desc = st.text_area("Description", key="pb_desc")
    new_steps_text = st.text_area("Steps (one per line)", key="pb_steps")
    if st.button("Add Playbook"):
        steps = [s.strip() for s in new_steps_text.splitlines() if s.strip()]
        pb = {"title": new_title or f"Playbook {len(st.session_state.playbooks)+1}",
              "description": new_desc,
              "steps": steps,
              "status": "open",
              "created_at": now_iso()}
        st.session_state.playbooks.append(pb)
        audit_add(st.session_state.user, st.session_state.role, "PlaybookAdd", f"Added playbook '{pb['title']}'")
        st.success("Playbook added.")

# -------------------------
# Page: Audit Logs
# -------------------------
elif page == "Audit Logs":
    st.header("📜 Audit Logs")
    st.write("Action history for demo interactions (local only).")
    if not st.session_state.audit:
        st.info("No audit entries yet.")
    else:
        df_a = pd.DataFrame(st.session_state.audit)
        st.dataframe(df_a)
        st.download_button("Download Audit CSV", data=convert_df_to_csv_bytes(df_a), file_name="audit_logs.csv")

# -------------------------
# Footer / housekeeping
# -------------------------
st.markdown("---")
st.caption("Agentic Cyber ML — Demo. Not for production use. Local role handling only. Actions recorded in an in-memory audit log.")
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
import base64

# -------------------------
# App config
# -------------------------
st.set_page_config(page_title="Agentic Cyber ML — Autonomous Threat Detection",
                   page_icon="🛡️", layout="wide")

# -------------------------
# Helpers
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
    if "playbooks" not in st.session_state:
        st.session_state.playbooks = []
    if "last_action" not in st.session_state:
        st.session_state.last_action = None

def audit_add(user, role, action, details=""):
    entry = {
        "timestamp": now_iso(),
        "user": user,
        "role": role,
        "action": action,
        "details": details
    }
    st.session_state.audit.insert(0, entry)

def generate_sample_logs(n=50):
    rng = np.random.default_rng(seed=42)
    timestamps = [datetime.utcnow() - timedelta(seconds=int(i*30)) for i in range(n)]
    src_ips = [f"10.{rng.integers(0,256)}.{rng.integers(0,256)}.{rng.integers(1,255)}" for _ in range(n)]
    dst_ips = [f"192.168.{rng.integers(0,256)}.{rng.integers(1,255)}" for _ in range(n)]
    protocol = rng.choice(["TCP","UDP","ICMP","HTTP","HTTPS","SSH","DNS"], size=n,
                          p=[0.25,0.2,0.03,0.18,0.18,0.07,0.09])
    bytes_sent = rng.integers(40, 200000, size=n)
    malicious = np.zeros(n, dtype=int)
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
        "malicious_label": malicious
    })
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
    # safe operations: create numeric features and return features matrix
    df = df.copy()
    df["bytes"] = pd.to_numeric(df.get("bytes", 0), errors="coerce").fillna(0)
    if "protocol" in df.columns:
        df["proto_enc"] = df["protocol"].astype("category").cat.codes
    else:
        df["proto_enc"] = 0
    df["pair"] = df["src_ip"].astype(str) + "->" + df["dst_ip"].astype(str)
    counts = df["pair"].value_counts().to_dict()
    df["pair_count"] = df["pair"].map(counts).fillna(1)
    features = df[["bytes","proto_enc","pair_count"]].astype(float)
    return df, features

def train_isolation_forest(features, cont=0.05):
    # scikit-learn modern params; removed deprecated behaviour param
    model = IsolationForest(n_estimators=200, contamination=cont, random_state=42)
    model.fit(features)
    return model

def score_with_iforest(df, model, features):
    df = df.copy()
    raw = -model.decision_function(features)  # higher -> more anomalous
    minv, maxv = raw.min(), raw.max()
    if maxv - minv <= 0:
        norm = np.zeros_like(raw)
    else:
        norm = (raw - minv) / (maxv - minv)
    df["anomaly_score"] = norm.round(4)
    df["action"] = "ALLOW"
    df.loc[df["anomaly_score"] >= 0.7, "action"] = "SUSPECT"
    df.loc[df["anomaly_score"] >= 0.9, "action"] = "BLOCK"
    if "quarantined" not in df.columns:
        df["quarantined"] = False
    return df

def convert_df_to_csv_bytes(df):
    return df.to_csv(index=False).encode("utf-8")

def convert_df_to_json_bytes(df):
    return df.to_json(orient="records", date_format="iso").encode("utf-8")

def convert_df_to_excel_bytes(df):
    buffer = BytesIO()
    try:
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="results")
    except Exception:
        # fallback if openpyxl not available
        df.to_excel(buffer, index=False, sheet_name="results")
    return buffer.getvalue()

def html_action_button(label, token, color_hex="#27ae60", size="14px"):
    href = "?" + urllib.parse.urlencode({"action": token})
    html = f"""
    <a href="{href}" style="
      display:inline-block;
      background:{color_hex};
      color:#fff;
      padding:8px 12px;
      text-decoration:none;
      border-radius:8px;
      font-weight:600;
      font-size:{size};
      margin:4px 4px;
    ">{label}</a>
    """
    st.markdown(html, unsafe_allow_html=True)

def download_link_bytes(data_bytes, filename, label):
    b64 = base64.b64encode(data_bytes).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}">{label}</a>'
    st.markdown(href, unsafe_allow_html=True)

def build_network_figure(df):
    # Build a simple network layout for top src/dst relationships
    if df.empty:
        return None
    # Use top N pairs
    df_pairs = df.copy()
    df_pairs["pair"] = df_pairs["src_ip"].astype(str) + "->" + df_pairs["dst_ip"].astype(str)
    top = df_pairs.groupby(["src_ip","dst_ip"]).size().reset_index(name="count").sort_values("count", ascending=False).head(40)
    G = nx.DiGraph()
    for _, row in top.iterrows():
        s = row["src_ip"]; d = row["dst_ip"]; c = int(row["count"])
        G.add_node(s); G.add_node(d)
        G.add_edge(s, d, weight=c)
    if len(G) == 0:
        return None
    pos = nx.spring_layout(G, seed=42)
    xs = []; ys = []; texts = []
    for n, p in pos.items():
        xs.append(p[0]); ys.append(p[1]); texts.append(str(n))
    edge_x = []
    edge_y = []
    edge_w = []
    for u,v,data in G.edges(data=True):
        x0,y0 = pos[u]; x1,y1 = pos[v]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]
        edge_w.append(data.get("weight",1))
    # node scatter
    node_df = pd.DataFrame({"x": xs, "y": ys, "label": texts})
    fig = px.scatter(node_df, x="x", y="y", hover_name="label", size_max=20)
    # add edges as lines
    for i in range(0, len(edge_x), 3):
        # slice edges
        seg_x = edge_x[i:i+3]; seg_y = edge_y[i:i+3]
        fig.add_shape(type="line", x0=seg_x[0], y0=seg_y[0], x1=seg_x[1], y1=seg_y[1],
                      line=dict(width=1, color="LightSeaGreen"))
    fig.update_layout(xaxis=dict(visible=False), yaxis=dict(visible=False), showlegend=False, height=450)
    return fig

# -------------------------
# Initialize state
# -------------------------
init_state()

# -------------------------
# Sidebar (role + nav)
# -------------------------
st.sidebar.title("Agentic Cyber ML")
st.sidebar.subheader("User / Role (demo)")
user_name = st.sidebar.text_input("Username", value=st.session_state.user)
role_select = st.sidebar.selectbox("Role", ["Admin", "Analyst", "Viewer"],
                                   index=["Admin","Analyst","Viewer"].index(st.session_state.role) if st.session_state.role in ["Admin","Analyst","Viewer"] else 2)
if st.sidebar.button("Set Role"):
    st.session_state.user = user_name if user_name.strip() else "guest"
    st.session_state.role = role_select
    audit_add(st.session_state.user, st.session_state.role, "SetRole", f"Role set to {role_select}")
    st.sidebar.success(f"Role set: {st.session_state.role}")

st.sidebar.markdown("---")
page = st.sidebar.radio("Pages", ["Threat Hunting", "Incident Playbooks", "Audit Logs"])
st.sidebar.markdown("---")
st.sidebar.caption("Note: demo only — local role handling (not secure).")

# -------------------------
# Parse action param from url (anchor-based html_action_button uses ?action=)
# -------------------------
query_params = st.query_params
action_param = None
if isinstance(query_params, dict):
    action_param = query_params.get("action", [None])[0] if "action" in query_params else None

# -------------------------
# Top UI area: action anchors (generate/upload/train/score/contain/reset)
# -------------------------
col_top_left, col_top_right = st.columns([3,1])
with col_top_left:
    st.markdown("### Agentic Cyber ML — Autonomous Threat Detection Demo")
    st.markdown("Generate sample logs, upload data, run unsupervised anomaly detection, auto-contain suspicious IPs, and download results.")
with col_top_right:
    # Red Reset anchor
    href = "?" + urllib.parse.urlencode({"action": "reset"})
    reset_html = f"""
    <a href="{href}" style="
      display:inline-block;
      background:#e74c3c;
      color:#fff;
      padding:8px 10px;
      text-decoration:none;
      border-radius:8px;
      font-weight:700;
      font-size:13px;
    ">Reset</a>
    """
    st.markdown(reset_html, unsafe_allow_html=True)

# Provide common anchors
st.markdown("---")
action_row = st.container()
with action_row:
    html_action_button("Generate Sample Logs", "generate", color_hex="#27ae60")
    html_action_button("Upload Logs", "upload", color_hex="#27ae60")
    html_action_button("Train/Score (Run ML)", "run_ml", color_hex="#27ae60")
    html_action_button("Auto-Contain Top Suspicious", "auto_contain", color_hex="#27ae60")
    html_action_button("Download CSV", "download_csv", color_hex="#2980b9")
    html_action_button("Download JSON", "download_json", color_hex="#2980b9")
    html_action_button("Download XLSX", "download_xlsx", color_hex="#2980b9")

# -------------------------
# Action handling for anchors (simple)
# -------------------------
def handle_action_token(token):
    st.session_state.last_action = token
    if token == "generate":
        df_new = generate_sample_logs(80)
        st.session_state.df = df_new
        audit_add(st.session_state.user, st.session_state.role, "Generate", "Generated 80 sample logs")
        st.success("Sample logs generated (80).")
    elif token == "upload":
        # open file uploader in a modal-like area below (we'll just signal)
        audit_add(st.session_state.user, st.session_state.role, "UploadRequested", "User requested upload via anchor")
        st.info("Use the upload widget below to pick a file (CSV / JSON / XLSX).")
    elif token == "run_ml":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No logs available — generate or upload logs first.")
            return
        df, features = create_features(st.session_state.df)
        model = train_isolation_forest(features, cont=0.05)
        scored = score_with_iforest(df, model, features)
        st.session_state.df = scored
        st.session_state.model = model
        st.session_state.model_stats = {"contamination":0.05, "n_samples": len(features)}
        audit_add(st.session_state.user, st.session_state.role, "RunML", f"Trained IsolationForest on {len(features)} records")
        st.success("ML run completed — anomaly scores added.")
    elif token == "auto_contain":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No logs available to contain.")
            return
        df = st.session_state.df.copy()
        # quarantine top anomalous src_ips
        top_block = df.sort_values("anomaly_score", ascending=False).head(10)
        ips_to_quarantine = top_block["src_ip"].value_counts().index.tolist()
        df.loc[df["src_ip"].isin(ips_to_quarantine), "quarantined"] = True
        st.session_state.df = df
        audit_add(st.session_state.user, st.session_state.role, "AutoContain", f"Quarantined {len(ips_to_quarantine)} src_ip(s)")
        st.success(f"Quarantined top {len(ips_to_quarantine)} source IPs.")
    elif token == "download_csv":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No data to download.")
            return
        csvb = convert_df_to_csv_bytes(st.session_state.df)
        download_link_bytes(csvb, "agentic_results.csv", "Click here to download CSV")
        audit_add(st.session_state.user, st.session_state.role, "Download", "Downloaded CSV")
    elif token == "download_json":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No data to download.")
            return
        jsb = convert_df_to_json_bytes(st.session_state.df)
        download_link_bytes(jsb, "agentic_results.json", "Click here to download JSON")
        audit_add(st.session_state.user, st.session_state.role, "Download", "Downloaded JSON")
    elif token == "download_xlsx":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No data to download.")
            return
        xb = convert_df_to_excel_bytes(st.session_state.df)
        download_link_bytes(xb, "agentic_results.xlsx", "Click here to download XLSX")
        audit_add(st.session_state.user, st.session_state.role, "Download", "Downloaded XLSX")
    elif token == "reset":
        st.session_state.df = pd.DataFrame()
        st.session_state.model = None
        st.session_state.model_stats = {}
        audit_add(st.session_state.user, st.session_state.role, "Reset", "Application reset by user")
        st.experimental_set_query_params()  # clear url params
        st.success("Application reset.")
    else:
        # unknown token
        st.info(f"Action: {token}")

if action_param:
    # handle token (note: this executes on page load when action param present)
    try:
        handle_action_token(action_param)
    except Exception as e:
        st.error(f"Action error: {e}")

# -------------------------
# Page: Threat Hunting
# -------------------------
if page == "Threat Hunting":
    st.header("🕵️ Threat Hunting (IsolationForest ML)")
    left, right = st.columns([2,1])
    with left:
        st.subheader("Data Controls")
        # Upload widget
        uploaded = st.file_uploader("Upload logs (CSV / JSON / XLSX)", type=["csv","json","xls","xlsx"])
        if uploaded is not None:
            df_u = read_uploaded_file(uploaded)
            if df_u is not None:
                # basic normalization: require timestamp, src_ip, dst_ip, protocol, bytes
                st.session_state.df = df_u
                # ensure columns exist
                for c in ["timestamp","src_ip","dst_ip","protocol","bytes","quarantined"]:
                    if c not in st.session_state.df.columns:
                        if c == "quarantined":
                            st.session_state.df[c] = False
                        else:
                            st.session_state.df[c] = ""
                audit_add(st.session_state.user, st.session_state.role, "Upload", f"Uploaded file: {uploaded.name}")
                st.success(f"Uploaded: {uploaded.name} ({len(st.session_state.df)} records).")
        st.markdown("**Quick actions**")
        if st.button("Generate 50 sample logs"):
            df_new = generate_sample_logs(50)
            st.session_state.df = df_new
            audit_add(st.session_state.user, st.session_state.role, "Generate", "Generated 50 sample logs")
            st.success("Generated 50 sample logs.")
        # ML controls
        st.markdown("**Machine Learning**")
        cont = st.slider("Contamination (expected fraction of anomalies)", min_value=0.01, max_value=0.2, value=0.05, step=0.01)
        if st.button("Train & Score (IsolationForest)"):
            if st.session_state.df is None or st.session_state.df.empty:
                st.warning("No data to train on. Generate or upload logs first.")
            else:
                df, feats = create_features(st.session_state.df)
                model = train_isolation_forest(feats, cont=cont)
                scored = score_with_iforest(df, model, feats)
                st.session_state.df = scored
                st.session_state.model = model
                st.session_state.model_stats = {"contamination": cont, "n_samples": len(feats)}
                audit_add(st.session_state.user, st.session_state.role, "TrainScore", f"Trained model on {len(feats)} rows")
                st.success("Model trained and anomaly scores computed.")
        st.markdown("**Containment**")
        if st.button("Auto-Contain Top 5 Suspicious (by src_ip)"):
            if st.session_state.df is None or st.session_state.df.empty:
                st.warning("No data to contain.")
            else:
                df = st.session_state.df.copy()
                top_block = df.sort_values("anomaly_score", ascending=False).head(10)
                ips_to_quarantine = top_block["src_ip"].value_counts().index.tolist()[:5]
                df.loc[df["src_ip"].isin(ips_to_quarantine), "quarantined"] = True
                st.session_state.df = df
                audit_add(st.session_state.user, st.session_state.role, "AutoContain", f"Quarantined {len(ips_to_quarantine)} IPs")
                st.success(f"Quarantined {len(ips_to_quarantine)} src_ip(s).")
        st.markdown("---")
        st.markdown("**Download current results**")
        if st.session_state.df is not None and not st.session_state.df.empty:
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.download_button("Download CSV", data=convert_df_to_csv_bytes(st.session_state.df),
                                   file_name="agentic_results.csv", mime="text/csv")
            with col_b:
                st.download_button("Download JSON", data=convert_df_to_json_bytes(st.session_state.df),
                                   file_name="agentic_results.json", mime="application/json")
            with col_c:
                try:
                    st.download_button("Download XLSX", data=convert_df_to_excel_bytes(st.session_state.df),
                                       file_name="agentic_results.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                except Exception:
                    st.download_button("Download XLSX", data=convert_df_to_excel_bytes(st.session_state.df),
                                       file_name="agentic_results.xlsx", mime="application/vnd.ms-excel")
        else:
            st.info("No results to download yet.")
    with right:
        st.subheader("Current Data Snapshot")
        if st.session_state.df is None or st.session_state.df.empty:
            st.info("No logs loaded. Generate or upload logs to begin.")
        else:
            st.write(f"Records: {len(st.session_state.df)}")
            preview = st.session_state.df.head(200)
            st.dataframe(preview)
        st.markdown("**Model Stats**")
        st.json(st.session_state.model_stats if st.session_state.model_stats else {"status":"no model"})

    st.markdown("---")
    st.subheader("Visualizations")
    viz_col1, viz_col2 = st.columns([1,1])
    with viz_col1:
        st.markdown("**Top anomalous records**")
        if st.session_state.df is not None and not st.session_state.df.empty and "anomaly_score" in st.session_state.df.columns:
            topn = st.session_state.df.sort_values("anomaly_score", ascending=False).head(25)
            fig = px.bar(topn, x="src_ip", y="anomaly_score", hover_data=["dst_ip","protocol","bytes"], title="Top anomalies by src_ip")
            fig.update_layout(xaxis_tickangle=-45, height=400)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No anomaly scores yet. Run ML.")
    with viz_col2:
        st.markdown("**Network Map (top pairs)**")
        fig_net = build_network_figure(st.session_state.df if st.session_state.df is not None else pd.DataFrame())
        if fig_net is not None:
            st.plotly_chart(fig_net, use_container_width=True)
        else:
            st.info("Network graph empty — generate/upload logs.")

# -------------------------
# Page: Incident Playbooks
# -------------------------
elif page == "Incident Playbooks":
    st.header("📘 Incident Playbooks")
    st.write("Create, view, and update incident playbooks. These are demo templates for response actions.")
    # list existing playbooks
    if st.session_state.playbooks:
        for i, pb in enumerate(st.session_state.playbooks):
            with st.expander(f"Playbook #{i+1}: {pb.get('title','Untitled')} - Status: {pb.get('status','open')}"):
                st.write("**Description**")
                st.write(pb.get("description",""))
                st.write("**Steps**")
                for step in pb.get("steps", []):
                    st.write(f"- {step}")
                cols = st.columns(3)
                if cols[0].button(f"Mark Mitigated #{i}", key=f"mit_{i}"):
                    st.session_state.playbooks[i]["status"] = "mitigated"
                    audit_add(st.session_state.user, st.session_state.role, "PlaybookMitigated", f"Playbook #{i+1} mitigated")
                    st.success("Marked mitigated.")
                if cols[1].button(f"Clone #{i}", key=f"clone_{i}"):
                    st.session_state.playbooks.append(dict(st.session_state.playbooks[i]))
                    audit_add(st.session_state.user, st.session_state.role, "PlaybookClone", f"Cloned playbook #{i+1}")
                    st.success("Cloned.")
                if cols[2].button(f"Delete #{i}", key=f"del_{i}"):
                    st.session_state.playbooks.pop(i)
                    audit_add(st.session_state.user, st.session_state.role, "PlaybookDelete", f"Deleted playbook #{i+1}")
                    st.success("Deleted.")
    else:
        st.info("No playbooks yet. Create one below.")

    st.markdown("### Create new playbook")
    new_title = st.text_input("Playbook title", key="pb_title")
    new_desc = st.text_area("Description", key="pb_desc")
    new_steps_text = st.text_area("Steps (one per line)", key="pb_steps")
    if st.button("Add Playbook"):
        steps = [s.strip() for s in new_steps_text.splitlines() if s.strip()]
        pb = {"title": new_title or f"Playbook {len(st.session_state.playbooks)+1}",
              "description": new_desc,
              "steps": steps,
              "status": "open",
              "created_at": now_iso()}
        st.session_state.playbooks.append(pb)
        audit_add(st.session_state.user, st.session_state.role, "PlaybookAdd", f"Added playbook '{pb['title']}'")
        st.success("Playbook added.")

# -------------------------
# Page: Audit Logs
# -------------------------
elif page == "Audit Logs":
    st.header("📜 Audit Logs")
    st.write("Action history for demo interactions (local only).")
    if not st.session_state.audit:
        st.info("No audit entries yet.")
    else:
        df_a = pd.DataFrame(st.session_state.audit)
        st.dataframe(df_a)
        st.download_button("Download Audit CSV", data=convert_df_to_csv_bytes(df_a), file_name="audit_logs.csv")

# -------------------------
# Footer / housekeeping
# -------------------------
st.markdown("---")
st.caption("Agentic Cyber ML — Demo. Not for production use. Local role handling only. Actions recorded in an in-memory audit log.")
"""
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
import base64

# -------------------------
# App config
# -------------------------
st.set_page_config(page_title="Agentic Cyber ML — Autonomous Threat Detection",
                   page_icon="🛡️", layout="wide")

# -------------------------
# Helpers
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
    if "playbooks" not in st.session_state:
        st.session_state.playbooks = []
    if "last_action" not in st.session_state:
        st.session_state.last_action = None

def audit_add(user, role, action, details=""):
    entry = {
        "timestamp": now_iso(),
        "user": user,
        "role": role,
        "action": action,
        "details": details
    }
    st.session_state.audit.insert(0, entry)

def generate_sample_logs(n=50):
    rng = np.random.default_rng(seed=42)
    timestamps = [datetime.utcnow() - timedelta(seconds=int(i*30)) for i in range(n)]
    src_ips = [f"10.{rng.integers(0,256)}.{rng.integers(0,256)}.{rng.integers(1,255)}" for _ in range(n)]
    dst_ips = [f"192.168.{rng.integers(0,256)}.{rng.integers(1,255)}" for _ in range(n)]
    protocol = rng.choice(["TCP","UDP","ICMP","HTTP","HTTPS","SSH","DNS"], size=n,
                          p=[0.25,0.2,0.03,0.18,0.18,0.07,0.09])
    bytes_sent = rng.integers(40, 200000, size=n)
    malicious = np.zeros(n, dtype=int)
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
        "malicious_label": malicious
    })
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
    # safe operations: create numeric features and return features matrix
    df = df.copy()
    df["bytes"] = pd.to_numeric(df.get("bytes", 0), errors="coerce").fillna(0)
    if "protocol" in df.columns:
        df["proto_enc"] = df["protocol"].astype("category").cat.codes
    else:
        df["proto_enc"] = 0
    df["pair"] = df["src_ip"].astype(str) + "->" + df["dst_ip"].astype(str)
    counts = df["pair"].value_counts().to_dict()
    df["pair_count"] = df["pair"].map(counts).fillna(1)
    features = df[["bytes","proto_enc","pair_count"]].astype(float)
    return df, features

def train_isolation_forest(features, cont=0.05):
    # scikit-learn modern params; removed deprecated behaviour param
    model = IsolationForest(n_estimators=200, contamination=cont, random_state=42)
    model.fit(features)
    return model

def score_with_iforest(df, model, features):
    df = df.copy()
    raw = -model.decision_function(features)  # higher -> more anomalous
    minv, maxv = raw.min(), raw.max()
    if maxv - minv <= 0:
        norm = np.zeros_like(raw)
    else:
        norm = (raw - minv) / (maxv - minv)
    df["anomaly_score"] = norm.round(4)
    df["action"] = "ALLOW"
    df.loc[df["anomaly_score"] >= 0.7, "action"] = "SUSPECT"
    df.loc[df["anomaly_score"] >= 0.9, "action"] = "BLOCK"
    if "quarantined" not in df.columns:
        df["quarantined"] = False
    return df

def convert_df_to_csv_bytes(df):
    return df.to_csv(index=False).encode("utf-8")

def convert_df_to_json_bytes(df):
    return df.to_json(orient="records", date_format="iso").encode("utf-8")

def convert_df_to_excel_bytes(df):
    buffer = BytesIO()
    try:
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="results")
    except Exception:
        # fallback if openpyxl not available
        df.to_excel(buffer, index=False, sheet_name="results")
    return buffer.getvalue()

def html_action_button(label, token, color_hex="#27ae60", size="14px"):
    href = "?" + urllib.parse.urlencode({"action": token})
    html = f"""
    <a href="{href}" style="
      display:inline-block;
      background:{color_hex};
      color:#fff;
      padding:8px 12px;
      text-decoration:none;
      border-radius:8px;
      font-weight:600;
      font-size:{size};
      margin:4px 4px;
    ">{label}</a>
    """
    st.markdown(html, unsafe_allow_html=True)

def download_link_bytes(data_bytes, filename, label):
    b64 = base64.b64encode(data_bytes).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}">{label}</a>'
    st.markdown(href, unsafe_allow_html=True)

def build_network_figure(df):
    # Build a simple network layout for top src/dst relationships
    if df.empty:
        return None
    # Use top N pairs
    df_pairs = df.copy()
    df_pairs["pair"] = df_pairs["src_ip"].astype(str) + "->" + df_pairs["dst_ip"].astype(str)
    top = df_pairs.groupby(["src_ip","dst_ip"]).size().reset_index(name="count").sort_values("count", ascending=False).head(40)
    G = nx.DiGraph()
    for _, row in top.iterrows():
        s = row["src_ip"]; d = row["dst_ip"]; c = int(row["count"])
        G.add_node(s); G.add_node(d)
        G.add_edge(s, d, weight=c)
    if len(G) == 0:
        return None
    pos = nx.spring_layout(G, seed=42)
    xs = []; ys = []; texts = []
    for n, p in pos.items():
        xs.append(p[0]); ys.append(p[1]); texts.append(str(n))
    edge_x = []
    edge_y = []
    edge_w = []
    for u,v,data in G.edges(data=True):
        x0,y0 = pos[u]; x1,y1 = pos[v]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]
        edge_w.append(data.get("weight",1))
    # node scatter
    node_df = pd.DataFrame({"x": xs, "y": ys, "label": texts})
    fig = px.scatter(node_df, x="x", y="y", hover_name="label", size_max=20)
    # add edges as lines
    for i in range(0, len(edge_x), 3):
        # slice edges
        seg_x = edge_x[i:i+3]; seg_y = edge_y[i:i+3]
        fig.add_shape(type="line", x0=seg_x[0], y0=seg_y[0], x1=seg_x[1], y1=seg_y[1],
                      line=dict(width=1, color="LightSeaGreen"))
    fig.update_layout(xaxis=dict(visible=False), yaxis=dict(visible=False), showlegend=False, height=450)
    return fig

# -------------------------
# Initialize state
# -------------------------
init_state()

# -------------------------
# Sidebar (role + nav)
# -------------------------
st.sidebar.title("Agentic Cyber ML")
st.sidebar.subheader("User / Role (demo)")
user_name = st.sidebar.text_input("Username", value=st.session_state.user)
role_select = st.sidebar.selectbox("Role", ["Admin", "Analyst", "Viewer"],
                                   index=["Admin","Analyst","Viewer"].index(st.session_state.role) if st.session_state.role in ["Admin","Analyst","Viewer"] else 2)
if st.sidebar.button("Set Role"):
    st.session_state.user = user_name if user_name.strip() else "guest"
    st.session_state.role = role_select
    audit_add(st.session_state.user, st.session_state.role, "SetRole", f"Role set to {role_select}")
    st.sidebar.success(f"Role set: {st.session_state.role}")

st.sidebar.markdown("---")
page = st.sidebar.radio("Pages", ["Threat Hunting", "Incident Playbooks", "Audit Logs"])
st.sidebar.markdown("---")
st.sidebar.caption("Note: demo only — local role handling (not secure).")

# -------------------------
# Parse action param from url (anchor-based html_action_button uses ?action=)
# -------------------------
query_params = st.query_params
action_param = None
if isinstance(query_params, dict):
    action_param = query_params.get("action", [None])[0] if "action" in query_params else None

# -------------------------
# Top UI area: action anchors (generate/upload/train/score/contain/reset)
# -------------------------
col_top_left, col_top_right = st.columns([3,1])
with col_top_left:
    st.markdown("### Agentic Cyber ML — Autonomous Threat Detection Demo")
    st.markdown("Generate sample logs, upload data, run unsupervised anomaly detection, auto-contain suspicious IPs, and download results.")
with col_top_right:
    # Red Reset anchor
    href = "?" + urllib.parse.urlencode({"action": "reset"})
    reset_html = f"""
    <a href="{href}" style="
      display:inline-block;
      background:#e74c3c;
      color:#fff;
      padding:8px 10px;
      text-decoration:none;
      border-radius:8px;
      font-weight:700;
      font-size:13px;
    ">Reset</a>
    """
    st.markdown(reset_html, unsafe_allow_html=True)

# Provide common anchors
st.markdown("---")
action_row = st.container()
with action_row:
    html_action_button("Generate Sample Logs", "generate", color_hex="#27ae60")
    html_action_button("Upload Logs", "upload", color_hex="#27ae60")
    html_action_button("Train/Score (Run ML)", "run_ml", color_hex="#27ae60")
    html_action_button("Auto-Contain Top Suspicious", "auto_contain", color_hex="#27ae60")
    html_action_button("Download CSV", "download_csv", color_hex="#2980b9")
    html_action_button("Download JSON", "download_json", color_hex="#2980b9")
    html_action_button("Download XLSX", "download_xlsx", color_hex="#2980b9")

# -------------------------
# Action handling for anchors (simple)
# -------------------------
def handle_action_token(token):
    st.session_state.last_action = token
    if token == "generate":
        df_new = generate_sample_logs(80)
        st.session_state.df = df_new
        audit_add(st.session_state.user, st.session_state.role, "Generate", "Generated 80 sample logs")
        st.success("Sample logs generated (80).")
    elif token == "upload":
        # open file uploader in a modal-like area below (we'll just signal)
        audit_add(st.session_state.user, st.session_state.role, "UploadRequested", "User requested upload via anchor")
        st.info("Use the upload widget below to pick a file (CSV / JSON / XLSX).")
    elif token == "run_ml":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No logs available — generate or upload logs first.")
            return
        df, features = create_features(st.session_state.df)
        model = train_isolation_forest(features, cont=0.05)
        scored = score_with_iforest(df, model, features)
        st.session_state.df = scored
        st.session_state.model = model
        st.session_state.model_stats = {"contamination":0.05, "n_samples": len(features)}
        audit_add(st.session_state.user, st.session_state.role, "RunML", f"Trained IsolationForest on {len(features)} records")
        st.success("ML run completed — anomaly scores added.")
    elif token == "auto_contain":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No logs available to contain.")
            return
        df = st.session_state.df.copy()
        # quarantine top anomalous src_ips
        top_block = df.sort_values("anomaly_score", ascending=False).head(10)
        ips_to_quarantine = top_block["src_ip"].value_counts().index.tolist()
        df.loc[df["src_ip"].isin(ips_to_quarantine), "quarantined"] = True
        st.session_state.df = df
        audit_add(st.session_state.user, st.session_state.role, "AutoContain", f"Quarantined {len(ips_to_quarantine)} src_ip(s)")
        st.success(f"Quarantined top {len(ips_to_quarantine)} source IPs.")
    elif token == "download_csv":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No data to download.")
            return
        csvb = convert_df_to_csv_bytes(st.session_state.df)
        download_link_bytes(csvb, "agentic_results.csv", "Click here to download CSV")
        audit_add(st.session_state.user, st.session_state.role, "Download", "Downloaded CSV")
    elif token == "download_json":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No data to download.")
            return
        jsb = convert_df_to_json_bytes(st.session_state.df)
        download_link_bytes(jsb, "agentic_results.json", "Click here to download JSON")
        audit_add(st.session_state.user, st.session_state.role, "Download", "Downloaded JSON")
    elif token == "download_xlsx":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No data to download.")
            return
        xb = convert_df_to_excel_bytes(st.session_state.df)
        download_link_bytes(xb, "agentic_results.xlsx", "Click here to download XLSX")
        audit_add(st.session_state.user, st.session_state.role, "Download", "Downloaded XLSX")
    elif token == "reset":
        st.session_state.df = pd.DataFrame()
        st.session_state.model = None
        st.session_state.model_stats = {}
        audit_add(st.session_state.user, st.session_state.role, "Reset", "Application reset by user")
        st.experimental_set_query_params()  # clear url params
        st.success("Application reset.")
    else:
        # unknown token
        st.info(f"Action: {token}")

if action_param:
    # handle token (note: this executes on page load when action param present)
    try:
        handle_action_token(action_param)
    except Exception as e:
        st.error(f"Action error: {e}")

# -------------------------
# Page: Threat Hunting
# -------------------------
if page == "Threat Hunting":
    st.header("🕵️ Threat Hunting (IsolationForest ML)")
    left, right = st.columns([2,1])
    with left:
        st.subheader("Data Controls")
        # Upload widget
        uploaded = st.file_uploader("Upload logs (CSV / JSON / XLSX)", type=["csv","json","xls","xlsx"])
        if uploaded is not None:
            df_u = read_uploaded_file(uploaded)
            if df_u is not None:
                # basic normalization: require timestamp, src_ip, dst_ip, protocol, bytes
                st.session_state.df = df_u
                # ensure columns exist
                for c in ["timestamp","src_ip","dst_ip","protocol","bytes","quarantined"]:
                    if c not in st.session_state.df.columns:
                        if c == "quarantined":
                            st.session_state.df[c] = False
                        else:
                            st.session_state.df[c] = ""
                audit_add(st.session_state.user, st.session_state.role, "Upload", f"Uploaded file: {uploaded.name}")
                st.success(f"Uploaded: {uploaded.name} ({len(st.session_state.df)} records).")
        st.markdown("**Quick actions**")
        if st.button("Generate 50 sample logs"):
            df_new = generate_sample_logs(50)
            st.session_state.df = df_new
            audit_add(st.session_state.user, st.session_state.role, "Generate", "Generated 50 sample logs")
            st.success("Generated 50 sample logs.")
        # ML controls
        st.markdown("**Machine Learning**")
        cont = st.slider("Contamination (expected fraction of anomalies)", min_value=0.01, max_value=0.2, value=0.05, step=0.01)
        if st.button("Train & Score (IsolationForest)"):
            if st.session_state.df is None or st.session_state.df.empty:
                st.warning("No data to train on. Generate or upload logs first.")
            else:
                df, feats = create_features(st.session_state.df)
                model = train_isolation_forest(feats, cont=cont)
                scored = score_with_iforest(df, model, feats)
                st.session_state.df = scored
                st.session_state.model = model
                st.session_state.model_stats = {"contamination": cont, "n_samples": len(feats)}
                audit_add(st.session_state.user, st.session_state.role, "TrainScore", f"Trained model on {len(feats)} rows")
                st.success("Model trained and anomaly scores computed.")
        st.markdown("**Containment**")
        if st.button("Auto-Contain Top 5 Suspicious (by src_ip)"):
            if st.session_state.df is None or st.session_state.df.empty:
                st.warning("No data to contain.")
            else:
                df = st.session_state.df.copy()
                top_block = df.sort_values("anomaly_score", ascending=False).head(10)
                ips_to_quarantine = top_block["src_ip"].value_counts().index.tolist()[:5]
                df.loc[df["src_ip"].isin(ips_to_quarantine), "quarantined"] = True
                st.session_state.df = df
                audit_add(st.session_state.user, st.session_state.role, "AutoContain", f"Quarantined {len(ips_to_quarantine)} IPs")
                st.success(f"Quarantined {len(ips_to_quarantine)} src_ip(s).")
        st.markdown("---")
        st.markdown("**Download current results**")
        if st.session_state.df is not None and not st.session_state.df.empty:
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.download_button("Download CSV", data=convert_df_to_csv_bytes(st.session_state.df),
                                   file_name="agentic_results.csv", mime="text/csv")
            with col_b:
                st.download_button("Download JSON", data=convert_df_to_json_bytes(st.session_state.df),
                                   file_name="agentic_results.json", mime="application/json")
            with col_c:
                try:
                    st.download_button("Download XLSX", data=convert_df_to_excel_bytes(st.session_state.df),
                                       file_name="agentic_results.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                except Exception:
                    st.download_button("Download XLSX", data=convert_df_to_excel_bytes(st.session_state.df),
                                       file_name="agentic_results.xlsx", mime="application/vnd.ms-excel")
        else:
            st.info("No results to download yet.")
    with right:
        st.subheader("Current Data Snapshot")
        if st.session_state.df is None or st.session_state.df.empty:
            st.info("No logs loaded. Generate or upload logs to begin.")
        else:
            st.write(f"Records: {len(st.session_state.df)}")
            preview = st.session_state.df.head(200)
            st.dataframe(preview)
        st.markdown("**Model Stats**")
        st.json(st.session_state.model_stats if st.session_state.model_stats else {"status":"no model"})

    st.markdown("---")
    st.subheader("Visualizations")
    viz_col1, viz_col2 = st.columns([1,1])
    with viz_col1:
        st.markdown("**Top anomalous records**")
        if st.session_state.df is not None and not st.session_state.df.empty and "anomaly_score" in st.session_state.df.columns:
            topn = st.session_state.df.sort_values("anomaly_score", ascending=False).head(25)
            fig = px.bar(topn, x="src_ip", y="anomaly_score", hover_data=["dst_ip","protocol","bytes"], title="Top anomalies by src_ip")
            fig.update_layout(xaxis_tickangle=-45, height=400)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No anomaly scores yet. Run ML.")
    with viz_col2:
        st.markdown("**Network Map (top pairs)**")
        fig_net = build_network_figure(st.session_state.df if st.session_state.df is not None else pd.DataFrame())
        if fig_net is not None:
            st.plotly_chart(fig_net, use_container_width=True)
        else:
            st.info("Network graph empty — generate/upload logs.")

# -------------------------
# Page: Incident Playbooks
# -------------------------
elif page == "Incident Playbooks":
    st.header("📘 Incident Playbooks")
    st.write("Create, view, and update incident playbooks. These are demo templates for response actions.")
    # list existing playbooks
    if st.session_state.playbooks:
        for i, pb in enumerate(st.session_state.playbooks):
            with st.expander(f"Playbook #{i+1}: {pb.get('title','Untitled')} - Status: {pb.get('status','open')}"):
                st.write("**Description**")
                st.write(pb.get("description",""))
                st.write("**Steps**")
                for step in pb.get("steps", []):
                    st.write(f"- {step}")
                cols = st.columns(3)
                if cols[0].button(f"Mark Mitigated #{i}", key=f"mit_{i}"):
                    st.session_state.playbooks[i]["status"] = "mitigated"
                    audit_add(st.session_state.user, st.session_state.role, "PlaybookMitigated", f"Playbook #{i+1} mitigated")
                    st.success("Marked mitigated.")
                if cols[1].button(f"Clone #{i}", key=f"clone_{i}"):
                    st.session_state.playbooks.append(dict(st.session_state.playbooks[i]))
                    audit_add(st.session_state.user, st.session_state.role, "PlaybookClone", f"Cloned playbook #{i+1}")
                    st.success("Cloned.")
                if cols[2].button(f"Delete #{i}", key=f"del_{i}"):
                    st.session_state.playbooks.pop(i)
                    audit_add(st.session_state.user, st.session_state.role, "PlaybookDelete", f"Deleted playbook #{i+1}")
                    st.success("Deleted.")
    else:
        st.info("No playbooks yet. Create one below.")

    st.markdown("### Create new playbook")
    new_title = st.text_input("Playbook title", key="pb_title")
    new_desc = st.text_area("Description", key="pb_desc")
    new_steps_text = st.text_area("Steps (one per line)", key="pb_steps")
    if st.button("Add Playbook"):
        steps = [s.strip() for s in new_steps_text.splitlines() if s.strip()]
        pb = {"title": new_title or f"Playbook {len(st.session_state.playbooks)+1}",
              "description": new_desc,
              "steps": steps,
              "status": "open",
              "created_at": now_iso()}
        st.session_state.playbooks.append(pb)
        audit_add(st.session_state.user, st.session_state.role, "PlaybookAdd", f"Added playbook '{pb['title']}'")
        st.success("Playbook added.")

# -------------------------
# Page: Audit Logs
# -------------------------
elif page == "Audit Logs":
    st.header("📜 Audit Logs")
    st.write("Action history for demo interactions (local only).")
    if not st.session_state.audit:
        st.info("No audit entries yet.")
    else:
        df_a = pd.DataFrame(st.session_state.audit)
        st.dataframe(df_a)
        st.download_button("Download Audit CSV", data=convert_df_to_csv_bytes(df_a), file_name="audit_logs.csv")

# -------------------------
# Footer / housekeeping
# -------------------------
st.markdown("---")
st.caption("Agentic Cyber ML — Demo. Not for production use. Local role handling only. Actions recorded in an in-memory audit log.")
