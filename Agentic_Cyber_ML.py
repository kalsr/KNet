

# Agentic_Cyber_ML.py

# Agentic Cyber ML — Single-file Streamlit demo
# Full features:
# Generate 10..100 sample logs or upload CSV/JSON/XLSX
# Train (IsolationForest), Score, Auto-Contain (Admin)
# Network visualization, downloads, audit log, playbooks
# Author: Randy Singh / KNet Consulting Group 


import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.ensemble import IsolationForest
from io import BytesIO
import json
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx

# -------------------------
# Page config
# -------------------------
st.set_page_config(page_title="Agentic Cyber ML", page_icon="🛡️", layout="wide")

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
    if "playbooks" not in st.session_state:
        st.session_state.playbooks = []

def audit_add(user, role, action, details=""):
    entry = {"timestamp": now_iso(), "user": user, "role": role, "action": action, "details": details}
    st.session_state.audit.insert(0, entry)

def generate_sample_logs(n=50):
    rng = np.random.default_rng(seed=42)
    timestamps = [datetime.utcnow() - timedelta(seconds=int(i*30)) for i in range(n)]
    src_ips = [f"10.{rng.integers(0,256)}.{rng.integers(0,256)}.{rng.integers(1,255)}" for _ in range(n)]
    dst_ips = [f"192.168.{rng.integers(0,256)}.{rng.integers(1,255)}" for _ in range(n)]
    protocol = rng.choice(["TCP","UDP","ICMP","HTTP","HTTPS","SSH","DNS"], size=n,
                          p=[0.25,0.2,0.03,0.18,0.18,0.07,0.09])
    bytes_sent = rng.integers(40, 200_000, size=n)
    malicious = np.zeros(n, dtype=int)
    spikes = rng.choice(n, size=max(1, n//15), replace=False)
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
    df = df.copy()
    # safe column checks
    if "bytes" not in df.columns:
        df["bytes"] = 0
    df["bytes"] = pd.to_numeric(df["bytes"], errors="coerce").fillna(0)
    if "protocol" in df.columns:
        df["proto_enc"] = df["protocol"].astype("category").cat.codes
    else:
        df["proto_enc"] = 0
    if "src_ip" not in df.columns:
        df["src_ip"] = "unknown"
    if "dst_ip" not in df.columns:
        df["dst_ip"] = "unknown"
    df["pair"] = df["src_ip"].astype(str) + "->" + df["dst_ip"].astype(str)
    counts = df["pair"].value_counts().to_dict()
    df["pair_count"] = df["pair"].map(counts).fillna(1)
    features = df[["bytes","proto_enc","pair_count"]].astype(float)
    return df, features

def train_isolation_forest(features, cont=0.05):
    model = IsolationForest(n_estimators=200, contamination=cont, random_state=42)
    model.fit(features)
    return model

def score_with_iforest(df, model, features):
    df = df.copy()
    raw = -model.decision_function(features)  # higher => more anomalous
    minv, maxv = raw.min(), raw.max()
    if maxv - minv <= 0:
        norm = np.zeros_like(raw)
    else:
        norm = (raw - minv) / (maxv - minv)
    df["anomaly_score"] = np.round(norm, 4)
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
        df.to_excel(buffer, index=False, sheet_name="results")
    return buffer.getvalue()

def network_plot_from_df(df):
    if df is None or df.empty:
        return None
    df_pairs = df.copy()
    df_pairs["pair"] = df_pairs["src_ip"].astype(str) + "->" + df_pairs["dst_ip"].astype(str)
    top = (df_pairs.groupby(["src_ip","dst_ip"]).size().reset_index(name="count")
           .sort_values("count", ascending=False).head(80))
    G = nx.DiGraph()
    for _, row in top.iterrows():
        s = row["src_ip"]; d = row["dst_ip"]; c = int(row["count"])
        G.add_node(s); G.add_node(d); G.add_edge(s, d, weight=c)
    if len(G) == 0:
        return None
    pos = nx.spring_layout(G, seed=42)
    edge_x, edge_y = [], []
    for u, v in G.edges():
        x0, y0 = pos[u]; x1, y1 = pos[v]
        edge_x += [x0, x1, None]; edge_y += [y0, y1, None]
    edge_trace = go.Scatter(x=edge_x, y=edge_y, mode='lines', line=dict(width=1, color="#888"), hoverinfo='none')
    node_x, node_y, texts, colors = [], [], [], []
    for n in G.nodes():
        x,y = pos[n]; node_x.append(x); node_y.append(y); texts.append(n)
        quarantined = df.loc[(df["src_ip"]==n) | (df["dst_ip"]==n), "quarantined"].any()
        colors.append("red" if quarantined else "green")
    node_trace = go.Scatter(x=node_x, y=node_y, mode='markers+text', text=texts, textposition='top center',
                            marker=dict(color=colors, size=12, line=dict(width=1)))
    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(title="Network Map (red = quarantined)", showlegend=False, xaxis=dict(visible=False), yaxis=dict(visible=False), height=480)
    return fig

# -------------------------
# Initialize session
# -------------------------
init_state()

# -------------------------
# Small CSS: style primary buttons green, reset red
# -------------------------
st.markdown(
    """
    <style>
    /* Make primary buttons green */
    div.stButton > button { background: #27ae60; color: white; border-radius:8px; padding:8px 12px; font-weight:600; }
    /* Give reset button a red look when it contains 'Reset' text (best-effort) */
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# Sidebar: user / role / navigation
# -------------------------
st.sidebar.title("Agentic Cyber ML")
st.sidebar.subheader("User / Role (demo)")
user_name = st.sidebar.text_input("Username", value=st.session_state.user)
role_choice = st.sidebar.selectbox("Role", ["Admin","Analyst","Viewer"],
                                   index=["Admin","Analyst","Viewer"].index(st.session_state.role) if st.session_state.role in ["Admin","Analyst","Viewer"] else 2)
if st.sidebar.button("Set Role"):
    st.session_state.user = user_name if user_name.strip() else "guest"
    st.session_state.role = role_choice
    audit_add(st.session_state.user, st.session_state.role, "SetRole", f"Role set to {role_choice}")
    st.sidebar.success(f"Role set: {st.session_state.role}")

st.sidebar.markdown("---")
page = st.sidebar.radio("Pages", ["Threat Hunting","Incident Playbooks","Audit Logs"])
st.sidebar.markdown("---")
st.sidebar.caption("Demo only — local role handling (not secure).")

# role permissions
role = st.session_state.role
can_generate = role in ("Admin","Analyst","Viewer")
can_train = role in ("Admin","Analyst")
can_score = role in ("Admin","Analyst")
can_contain = role == "Admin"
can_reset = role == "Admin"
can_upload = role in ("Admin","Analyst","Viewer")

# -------------------------
# Header + action buttons (functional st.button)
# -------------------------
st.title("Agentic Cyber ML — Autonomous Threat Detection (Demo)")
st.markdown("Generate or upload logs → train → score → auto-contain (Admin) → visualize & download.")

# top controls: slider + buttons
col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
sample_n = st.sidebar.slider("Sample logs to generate", min_value=10, max_value=100, value=50, step=5)

with col1:
    gen_clicked = st.button("Generate Sample Logs")
with col2:
    train_clicked = st.button("Train Model")
with col3:
    score_clicked = st.button("Score Logs")
with col4:
    contain_clicked = st.button("Auto-Contain (Admin)")
with col5:
    reset_clicked = st.button("Reset")

st.markdown("---")

# -------------------------
# Page: Threat Hunting
# -------------------------
if page == "Threat Hunting":
    left, right = st.columns([2,1])
    with left:
        st.subheader("Data controls (Generate / Upload / Train / Score / Contain)")

        # Upload widget
        uploaded = st.file_uploader("Upload logs (CSV / JSON / XLSX)", type=["csv","json","xls","xlsx"])
        if uploaded is not None:
            if not can_upload:
                st.warning("Your role cannot upload files.")
                audit_add(st.session_state.user, st.session_state.role, "UploadDenied", "role not allowed")
            else:
                df_u = read_uploaded_file(uploaded)
                if df_u is not None:
                    # normalize minimal fields
                    if "timestamp" not in df_u.columns:
                        df_u["timestamp"] = now_iso()
                    for c in ["src_ip","dst_ip","protocol","bytes"]:
                        if c not in df_u.columns:
                            df_u[c] = "" if c!="bytes" else 0
                    if "quarantined" not in df_u.columns:
                        df_u["quarantined"] = False
                    st.session_state.df = df_u
                    audit_add(st.session_state.user, st.session_state.role, "Upload", f"{uploaded.name} ({len(df_u)} rows)")
                    st.success(f"Uploaded {uploaded.name} ({len(df_u)} rows).")

        # Generate
        if gen_clicked:
            if not can_generate:
                st.warning("Role not permitted to generate logs.")
                audit_add(st.session_state.user, st.session_state.role, "GenerateDenied", "")
            else:
                st.session_state.df = generate_sample_logs(sample_n)
                audit_add(st.session_state.user, st.session_state.role, "Generate", f"{sample_n} sample logs")
                st.success(f"Generated {sample_n} sample logs.")

        # Train
        st.markdown("### Machine Learning")
        contamination = st.slider("Contamination (expected anomaly fraction)", min_value=0.01, max_value=0.2, value=0.05, step=0.01)
        if train_clicked:
            if not can_train:
                st.warning("Your role cannot train models.")
                audit_add(st.session_state.user, st.session_state.role, "TrainDenied", "")
            else:
                if st.session_state.df is None or st.session_state.df.empty:
                    st.error("No data available. Generate or upload logs first.")
                else:
                    df_f, feats = create_features(st.session_state.df)
                    model = train_isolation_forest(feats, cont=contamination)
                    st.session_state.model = model
                    st.session_state.df = df_f
                    st.session_state.model_stats = {"contamination": contamination, "n_samples": len(feats)}
                    audit_add(st.session_state.user, st.session_state.role, "Train", f"Trained on {len(feats)} rows")
                    st.success("Model trained.")

        # Score
        if score_clicked:
            if not can_score:
                st.warning("Your role cannot score logs.")
                audit_add(st.session_state.user, st.session_state.role, "ScoreDenied", "")
            else:
                if st.session_state.model is None:
                    st.error("No trained model present. Train first.")
                elif st.session_state.df is None or st.session_state.df.empty:
                    st.error("No logs available to score.")
                else:
                    df_f, feats = create_features(st.session_state.df)
                    scored = score_with_iforest(df_f, st.session_state.model, feats)
                    st.session_state.df = scored
                    audit_add(st.session_state.user, st.session_state.role, "Score", f"Scored {len(feats)} rows")
                    st.success("Logs scored (anomaly_score added).")

        # Auto-contain
        if contain_clicked:
            if not can_contain:
                st.warning("Only Admin may auto-contain.")
                audit_add(st.session_state.user, st.session_state.role, "ContainDenied", "")
            else:
                if st.session_state.df is None or st.session_state.df.empty or "anomaly_score" not in st.session_state.df.columns:
                    st.error("No scored logs available to contain. Run Train & Score first.")
                else:
                    dfc = st.session_state.df.copy()
                    top = dfc.sort_values("anomaly_score", ascending=False).head(10)
                    ips = top["src_ip"].value_counts().index.tolist()[:5]
                    dfc.loc[dfc["src_ip"].isin(ips), "quarantined"] = True
                    st.session_state.df = dfc
                    audit_add(st.session_state.user, st.session_state.role, "AutoContain", f"Quarantined {len(ips)} src_ip(s)")
                    st.success(f"Quarantined {len(ips)} source IP(s).")

        # Reset
        if reset_clicked:
            if not can_reset:
                st.warning("Only Admin may reset the session.")
                audit_add(st.session_state.user, st.session_state.role, "ResetDenied", "")
            else:
                st.session_state.df = pd.DataFrame()
                st.session_state.model = None
                st.session_state.model_stats = {}
                audit_add(st.session_state.user, st.session_state.role, "Reset", "Session reset")
                st.success("Session reset.")

        # Downloads (in-page)
        st.markdown("---")
        st.markdown("### Download / Export")
        if st.session_state.df is not None and not st.session_state.df.empty:
            cdl1, cdl2, cdl3 = st.columns(3)
            with cdl1:
                st.download_button("Download CSV", data=convert_df_to_csv_bytes(st.session_state.df), file_name="agentic_results.csv", mime="text/csv")
            with cdl2:
                st.download_button("Download JSON", data=convert_df_to_json_bytes(st.session_state.df), file_name="agentic_results.json", mime="application/json")
            with cdl3:
                st.download_button("Download XLSX", data=convert_df_to_excel_bytes(st.session_state.df), file_name="agentic_results.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        else:
            st.info("No data to download yet.")

    with right:
        st.subheader("Session & Model")
        st.write(f"User: **{st.session_state.user}** — Role: **{st.session_state.role}**")
        st.markdown("**Model stats**")
        st.json(st.session_state.model_stats if st.session_state.model_stats else {"status":"no model"})
        st.markdown("---")
        st.subheader("Recent audit entries")
        if st.session_state.audit:
            df_a = pd.DataFrame(st.session_state.audit).head(50)
            st.table(df_a[["timestamp","user","role","action","details"]])
            st.download_button("Download Audit CSV", data=convert_df_to_csv_bytes(df_a), file_name="audit_recent.csv", mime="text/csv")
        else:
            st.info("No audit entries yet.")

    st.markdown("---")
    st.subheader("Data snapshot & visualizations")
    if st.session_state.df is None or st.session_state.df.empty:
        st.info("No logs loaded. Generate or upload logs to begin.")
    else:
        st.write(f"Records: {len(st.session_state.df)}")
        st.dataframe(st.session_state.df.head(200), use_container_width=True)
        if "anomaly_score" in st.session_state.df.columns:
            hist = px.histogram(st.session_state.df, x="anomaly_score", nbins=30, title="Anomaly Score Distribution")
            st.plotly_chart(hist, use_container_width=True)
            net_fig = network_plot_from_df(st.session_state.df)
            if net_fig is not None:
                st.plotly_chart(net_fig, use_container_width=True)
        else:
            st.info("No anomaly scores yet. Run Train & Score.")

# -------------------------
# Incident Playbooks page (simple)
# -------------------------
if page == "Incident Playbooks":
    st.header("📘 Incident Playbooks (Demo)")
    for i, pb in enumerate(st.session_state.playbooks):
        with st.expander(f"Playbook #{i+1}: {pb.get('title','Untitled')} (status: {pb.get('status','open')})"):
            st.write(pb.get("description",""))
            st.write("Steps:")
            for s in pb.get("steps", []):
                st.write(f"- {s}")
            btns = st.columns(3)
            if btns[0].button(f"Mark Mitigated #{i}", key=f"mit_{i}"):
                st.session_state.playbooks[i]["status"] = "mitigated"
                audit_add(st.session_state.user, st.session_state.role, "PlaybookMitigated", f"Mitigated #{i+1}")
                st.experimental_rerun()
            if btns[1].button(f"Clone #{i}", key=f"clone_{i}"):
                st.session_state.playbooks.append(dict(st.session_state.playbooks[i]))
                audit_add(st.session_state.user, st.session_state.role, "PlaybookClone", f"Cloned #{i+1}")
                st.experimental_rerun()
            if btns[2].button(f"Delete #{i}", key=f"del_{i}"):
                if st.session_state.role != "Admin":
                    st.warning("Only Admin can delete playbooks.")
                    audit_add(st.session_state.user, st.session_state.role, "PlaybookDeleteDenied", f"Tried to delete #{i+1}")
                else:
                    st.session_state.playbooks.pop(i)
                    audit_add(st.session_state.user, st.session_state.role, "PlaybookDelete", f"Deleted #{i+1}")
                st.experimental_rerun()

    st.markdown("### Create new playbook")
    new_title = st.text_input("Title", key="pb_title")
    new_desc = st.text_area("Description", key="pb_desc")
    new_steps = st.text_area("Steps (one per line)", key="pb_steps")
    if st.button("Add Playbook"):
        steps = [s.strip() for s in new_steps.splitlines() if s.strip()]
        pb = {"title": new_title or f"Playbook {len(st.session_state.playbooks)+1}",
              "description": new_desc, "steps": steps, "status": "open", "created_at": now_iso()}
        st.session_state.playbooks.append(pb)
        audit_add(st.session_state.user, st.session_state.role, "PlaybookAdd", f"Added '{pb['title']}'")
        st.success("Playbook added.")
        st.experimental_rerun()

# -------------------------
# Audit Logs page
# -------------------------
if page == "Audit Logs":
    st.header("📜 Audit Logs")
    if st.session_state.audit:
        df_a = pd.DataFrame(st.session_state.audit)
        st.dataframe(df_a, use_container_width=True)
        st.download_button("Download Audit CSV", data=convert_df_to_csv_bytes(df_a), file_name="audit_logs.csv", mime="text/csv")
    else:
        st.info("No audit entries yet.")

st.markdown("---")
st.caption("Agentic Cyber ML — Demo. Not for production use. Local role handling only.")
