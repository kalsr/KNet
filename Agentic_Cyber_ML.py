


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

# -------------------------
# App configuration
# -------------------------
st.set_page_config(
    page_title="Agentic Cyber ML — Autonomous Threat Detection",
    page_icon="🛡️",
    layout="wide"
)

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
    protocol = rng.choice(["TCP","UDP","ICMP","HTTP","HTTPS","SSH","DNS"],
                          size=n, p=[0.25,0.2,0.03,0.18,0.18,0.07,0.09])
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
    """Create numeric features for the IsolationForest."""
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
    model = IsolationForest(n_estimators=200, contamination=cont, random_state=42)
    model.fit(features)
    return model

def score_with_iforest(df, model, features):
    df = df.copy()
    raw = -model.decision_function(features)

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
# HTML button helper
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
# Sidebar
# -------------------------
st.sidebar.title("Agentic Cyber ML")
st.sidebar.subheader("User / Role (demo)")

user_name = st.sidebar.text_input("Username", value=st.session_state.user)
role = st.sidebar.selectbox(
    "Role",
    ["Admin", "Analyst", "Viewer"],
    index={"Admin":0,"Analyst":1,"Viewer":2}[st.session_state.role]
    if st.session_state.role in ["Admin","Analyst","Viewer"] else 2
)

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
query_params = st.query_params
action_param = query_params.get("action", [None])[0] if "action" in query_params else None

# -------------------------
# Page: Threat Hunting
# -------------------------
if page == "Threat Hunting":
    st.title("🕵️ Threat Hunting (IsolationForest ML)")
    st.markdown("Use the controls on the left to generate/upload logs, run ML detection, visualize, auto-contain, and download results.")
