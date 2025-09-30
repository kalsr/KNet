




# Agentic_Cyber_ML.py
# Author: Randy Singh / KNet Consulting Group


import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.ensemble import IsolationForest
from io import BytesIO
import json
import plotly.express as px
import networkx as nx
import plotly.graph_objects as go
import urllib.parse

# -------------------------
# App configuration
# -------------------------
st.set_page_config(page_title="Agentic Cyber ML", page_icon="", layout="wide")

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
    st.session_state.audit.insert(0, {"timestamp": now_iso(), "user": user, "role": role, "action": action, "details": details})

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
    df["bytes"] = pd.to_numeric(df.get("bytes", 0), errors="coerce").fillna(0)
    if "protocol" in df.columns:
        df["proto_enc"] = df["protocol"].astype("category").cat.codes
    else:
        df["proto_enc"] = 0
    df["src_ip"] = df.get("src_ip", "unknown")
    df["dst_ip"] = df.get("dst_ip", "unknown")
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
    raw = -model.decision_function(features)
    minv, maxv = raw.min(), raw.max()
    norm = np.zeros_like(raw) if maxv - minv <= 0 else (raw - minv)/(maxv - minv)
    df["anomaly_score"] = np.round(norm,4)
    df["action"] = "ALLOW"
    df.loc[df["anomaly_score"]>=0.7, "action"]="SUSPECT"
    df.loc[df["anomaly_score"]>=0.9, "action"]="BLOCK"
    if "quarantined" not in df.columns:
        df["quarantined"] = False
    return df

def convert_df_to_csv_bytes(df):
    return df.to_csv(index=False).encode("utf-8")

def convert_df_to_json_bytes(df):
    return df.to_json(orient="records", date_format="iso").encode("utf-8")

def convert_df_to_excel_bytes(df):
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="results")
    return buffer.getvalue()

def network_plot_from_df(df):
    if df is None or df.empty:
        return None
    top = (df.groupby(["src_ip","dst_ip"]).size().reset_index(name="count")
           .sort_values("count", ascending=False).head(80))
    G = nx.DiGraph()
    for _, row in top.iterrows():
        G.add_node(row["src_ip"])
        G.add_node(row["dst_ip"])
        G.add_edge(row["src_ip"], row["dst_ip"], weight=int(row["count"]))
    if len(G)==0:
        return None
    pos = nx.spring_layout(G, seed=42)
    edge_x, edge_y = [], []
    for u,v in G.edges():
        x0,y0 = pos[u]; x1,y1 = pos[v]
        edge_x += [x0,x1,None]; edge_y += [y0,y1,None]
    edge_trace = go.Scatter(x=edge_x, y=edge_y, mode="lines", line=dict(width=1,color="#888"), hoverinfo="none")
    node_x, node_y, colors, texts = [],[],[],[]
    for n in G.nodes():
        x,y = pos[n]; node_x.append(x); node_y.append(y)
        texts.append(n)
        quarantined = df.loc[(df["src_ip"]==n) | (df["dst_ip"]==n),"quarantined"].any()
        colors.append("red" if quarantined else "green")
    node_trace = go.Scatter(x=node_x, y=node_y, mode="markers+text", text=texts, textposition="top center",
                            marker=dict(color=colors,size=12,line=dict(width=1)))
    fig = go.Figure(data=[edge_trace,node_trace])
    fig.update_layout(title="Network Map (red = quarantined)", showlegend=False, xaxis=dict(visible=False), yaxis=dict(visible=False), height=480)
    return fig

# -------------------------
# Initialize session
# -------------------------
init_state()

# -------------------------
# Sidebar
# -------------------------
st.sidebar.title("Agentic Cyber ML - ")
st.session_state.user = st.sidebar.text_input("Username", value=st.session_state.user)
st.session_state.role = st.sidebar.selectbox("Role", ["Admin","Analyst","Viewer"], index=["Admin","Analyst","Viewer"].index(st.session_state.role))
if st.sidebar.button("Set Role"):
    audit_add(st.session_state.user, st.session_state.role, "SetRole", f"Role set to {st.session_state.role}")
    st.sidebar.success(f"Role set: {st.session_state.role}")

st.sidebar.markdown("---")
page = st.sidebar.radio("Pages", ["Threat Hunting","Audit Logs"])
st.sidebar.markdown("---")

# -------------------------
# Role permissions
# -------------------------
role = st.session_state.role
can_generate = role in ("Admin","Analyst","Viewer")
can_train = role in ("Admin","Analyst")
can_score = role in ("Admin","Analyst")
can_contain = role=="Admin"
can_reset = role=="Admin"
can_upload = role in ("Admin","Analyst","Viewer")

# -------------------------
# HTML styled button
# -------------------------
def html_button(label, key, color, width="200px"):
    href = f"?{urllib.parse.urlencode({'key':key})}"
    html = f"""
    <a href="{href}" style="
        display:inline-block;
        background:{color};
        color:#fff;
        padding:10px 20px;
        text-decoration:none;
        border-radius:8px;
        font-weight:bold;
        margin:4px;
    ">{label}</a>
    """
    st.markdown(html, unsafe_allow_html=True)

# -------------------------
# Threat Hunting Page
# -------------------------
if page=="Threat Hunting":
    st.title("Agentic Cyber Threat Hunting - Randy Singh From KNet Consulting Group")

    # Sample log slider
    sample_n = st.sidebar.slider("Number of sample logs", 10, 100, 50, 5)
    contamination = st.sidebar.slider("Contamination fraction", 0.01, 0.2, 0.05, 0.01)

    # Buttons row
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        if can_generate and st.button("Generate Sample Logs", key="gen"):
            st.session_state.df = generate_sample_logs(sample_n)
            audit_add(st.session_state.user, st.session_state.role,"Generate",f"{sample_n} logs")
            st.success(f"Generated {sample_n} logs")
    with col2:
        if can_train and st.button("Train Model", key="train"):
            if st.session_state.df.empty:
                st.error("No data to train.")
            else:
                df_f, feats = create_features(st.session_state.df)
                model = train_isolation_forest(feats, contamination)
                st.session_state.model = model
                st.session_state.df = df_f
                st.session_state.model_stats = {"contamination": contamination, "n_samples": len(feats)}
                audit_add(st.session_state.user, st.session_state.role,"Train",f"Trained on {len(feats)} rows")
                st.success("Model trained")
    with col3:
        if can_score and st.button("Score Logs", key="score"):
            if st.session_state.model is None:
                st.error("No trained model.")
            elif st.session_state.df.empty:
                st.error("No logs to score.")
            else:
                df_f, feats = create_features(st.session_state.df)
                scored = score_with_iforest(df_f, st.session_state.model, feats)
                st.session_state.df = scored
                audit_add(st.session_state.user, st.session_state.role,"Score",f"Scored {len(feats)} rows")
                st.success("Logs scored")
    with col4:
        if can_contain and st.button("Auto-Contain (Admin)", key="contain"):
            if st.session_state.df.empty or "anomaly_score" not in st.session_state.df.columns:
                st.error("Score logs first.")
            else:
                dfc = st.session_state.df.copy()
                top = dfc.sort_values("anomaly_score", ascending=False).head(10)
                ips = top["src_ip"].value_counts().index.tolist()[:5]
                dfc.loc[dfc["src_ip"].isin(ips),"quarantined"] = True
                st.session_state.df = dfc
                audit_add(st.session_state.user, st.session_state.role,"AutoContain",f"Quarantined {len(ips)} IPs")
                st.success(f"Quarantined {len(ips)} source IPs")
    with col5:
        if can_reset and st.button("Reset Data", key="reset"):
            st.session_state.df = pd.DataFrame()
            st.session_state.model = None
            st.session_state.model_stats = {}
            audit_add(st.session_state.user, st.session_state.role,"Reset","Session reset")
            st.success("Session reset")

    # File upload
    uploaded = st.file_uploader("Upload logs (CSV/JSON/XLSX)", type=["csv","json","xls","xlsx"])
    if uploaded and can_upload:
        df_u = read_uploaded_file(uploaded)
        if df_u is not None:
            for c in ["timestamp","src_ip","dst_ip","protocol","bytes"]:
                if c not in df_u.columns:
                    df_u[c] = "" if c!="bytes" else 0
            if "quarantined" not in df_u.columns:
                df_u["quarantined"] = False
            st.session_state.df = df_u
            audit_add(st.session_state.user, st.session_state.role,"Upload",f"{uploaded.name} ({len(df_u)} rows)")
            st.success(f"Uploaded {uploaded.name} ({len(df_u)} rows)")

    # Display data and charts
    if not st.session_state.df.empty:
        st.subheader("Logs snapshot")
        st.dataframe(st.session_state.df.head(200), use_container_width=True)
        if "anomaly_score" in st.session_state.df.columns:
            st.subheader("Anomaly Score Histogram")
            fig = px.histogram(st.session_state.df, x="anomaly_score", nbins=30)
            st.plotly_chart(fig, use_container_width=True)
            st.subheader("Network Graph (red=quarantined)")
            net_fig = network_plot_from_df(st.session_state.df)
            if net_fig: st.plotly_chart(net_fig, use_container_width=True)
        # Downloads
        st.subheader("Download / Export")
        c1,c2,c3 = st.columns(3)
        with c1: st.download_button("CSV", convert_df_to_csv_bytes(st.session_state.df), "results.csv")
        with c2: st.download_button("JSON", convert_df_to_json_bytes(st.session_state.df), "results.json")
        with c3: st.download_button("Excel", convert_df_to_excel_bytes(st.session_state.df), "results.xlsx")

# -------------------------
# Audit Logs Page
# -------------------------
if page=="Audit Logs":
    st.title(" Audit Logs")
    if st.session_state.audit:
        df_a = pd.DataFrame(st.session_state.audit)
        st.dataframe(df_a, use_container_width=True)
        st.download_button("Download Audit CSV", convert_df_to_csv_bytes(df_a), "audit_logs.csv")
    else:
        st.info("No audit logs yet.")

st.caption("Agentic Cyber ML — Demo. Local role handling only. Not for production.")


