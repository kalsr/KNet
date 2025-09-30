

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
import plotly.graph_objects as go
import networkx as nx
import urllib.parse
import base64

# -------------------------
# App configuration
# -------------------------
st.set_page_config(
    page_title="Agentic Cyber ML — Autonomous Threat Detection",
    page_icon="🛡️",
    layout="wide",
)

# -------------------------
# Helpers & core functions
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
    protocol = rng.choice(
        ["TCP","UDP","ICMP","HTTP","HTTPS","SSH","DNS"],
        size=n,
        p=[0.25,0.2,0.03,0.18,0.18,0.07,0.09]
    )
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
    norm = np.zeros_like(raw) if maxv - minv <= 0 else (raw - minv) / (maxv - minv)
    df["anomaly_score"] = np.round(norm, 4)
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
    try:
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="results")
    except Exception:
        df.to_excel(buffer, index=False, sheet_name="results")
    return buffer.getvalue()

def html_action_anchor(label, token, color_hex="#27ae60", size="14px"):
    href = "?" + urllib.parse.urlencode({"action": token})
    html = f'''
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
    '''
    st.markdown(html, unsafe_allow_html=True)

def download_link_bytes(data_bytes, filename, label):
    b64 = base64.b64encode(data_bytes).decode()
    href = f'data:application/octet-stream;base64,{b64}'
    st.markdown(f'<a href="{href}" download="{filename}">{label}</a>', unsafe_allow_html=True)

def network_plot_from_df(df):
    # Use only a subset to keep graph readable
    if df is None or df.empty:
        return None
    # Build graph from top pairs by count
    df_pairs = df.copy()
    df_pairs["pair"] = df_pairs["src_ip"].astype(str) + "->" + df_pairs["dst_ip"].astype(str)
    top = (df_pairs.groupby(["src_ip","dst_ip"]).size().reset_index(name="count")
           .sort_values("count", ascending=False).head(80))
    G = nx.DiGraph()
    for _, row in top.iterrows():
        s = row["src_ip"]; d = row["dst_ip"]; c = int(row["count"])
        G.add_node(s); G.add_node(d)
        G.add_edge(s, d, weight=c)
    if len(G)==0:
        return None
    pos = nx.spring_layout(G, seed=42)
    edge_x, edge_y = [], []
    for u,v in G.edges():
        x0,y0 = pos[u]; x1,y1 = pos[v]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]
    edge_trace = go.Scatter(x=edge_x, y=edge_y, mode='lines', line=dict(width=1, color="#888"), hoverinfo='none')
    node_x, node_y, texts, colors = [], [], [], []
    for n in G.nodes():
        x,y = pos[n]
        node_x.append(x); node_y.append(y); texts.append(n)
        quarantined = df.loc[df["src_ip"]==n, "quarantined"].any() or df.loc[df["dst_ip"]==n, "quarantined"].any()
        colors.append("red" if quarantined else "green")
    node_trace = go.Scatter(
        x=node_x, y=node_y, mode='markers+text', text=texts, textposition='top center',
        marker=dict(color=colors, size=12, line=dict(width=1))
    )
    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(title="Network Map (red = quarantined)", showlegend=False, xaxis=dict(visible=False), yaxis=dict(visible=False), height=480)
    return fig

# -------------------------
# Init state
# -------------------------
init_state()

# -------------------------
# Sidebar: role + nav
# -------------------------
st.sidebar.title("Agentic Cyber ML")
st.sidebar.subheader("User / Role (demo)")
user_name = st.sidebar.text_input("Username", value=st.session_state.user)
role_choice = st.sidebar.selectbox("Role", ["Admin", "Analyst", "Viewer"], index=["Admin","Analyst","Viewer"].index(st.session_state.role) if st.session_state.role in ["Admin","Analyst","Viewer"] else 2)
if st.sidebar.button("Set Role"):
    st.session_state.user = user_name if user_name.strip() else "guest"
    st.session_state.role = role_choice
    audit_add(st.session_state.user, st.session_state.role, "SetRole", f"Role set to {role_choice}")
    st.sidebar.success(f"Role set: {st.session_state.role}")

st.sidebar.markdown("---")
page = st.sidebar.radio("Pages", ["Threat Hunting", "Incident Playbooks", "Audit Logs"])
st.sidebar.markdown("---")
st.sidebar.caption("Demo only — local role handling. Not for production.")

# permission helpers
role = st.session_state.role
can_train = role in ("Admin","Analyst")
can_score = role in ("Admin","Analyst")
can_contain = role == "Admin"
can_reset = role == "Admin"
can_download = True
can_upload = role in ("Admin","Analyst","Viewer")

# -------------------------
# Top header + anchor buttons
# -------------------------
col_h1, col_h2 = st.columns([3,1])
with col_h1:
    st.title("Agentic Cyber ML — Autonomous Threat Detection (Demo)")
    st.markdown("Generate or upload logs → train → score → auto-contain (Admin) → visualize & download.")
with col_h2:
    # red reset anchor
    html_action_anchor = lambda label, token, color: st.markdown(
        f'<a href="?action={token}" style="display:inline-block;background:{color};color:#fff;padding:8px 10px;text-decoration:none;border-radius:8px;font-weight:700;font-size:13px;">{label}</a>', unsafe_allow_html=True
    )
    html_action_anchor("Reset", "reset", "#c0392b")

st.markdown("---")

# anchor actions row
row = st.container()
with row:
    html_action_anchor("Generate Sample Logs", "generate", "#27ae60")
    html_action_anchor("Train Model", "train", "#27ae60")
    html_action_anchor("Score Logs", "score", "#27ae60")
    html_action_anchor("Auto-Contain (Admin)", "auto_contain", "#27ae60")
    html_action_anchor("Download CSV", "download_csv", "#2980b9")
    html_action_anchor("Download JSON", "download_json", "#2980b9")
    html_action_anchor("Download XLSX", "download_xlsx", "#2980b9")

st.markdown("---")

# -------------------------
# Parse action from URL (anchor)
# -------------------------
query_params = st.query_params
action_param = None
if isinstance(query_params, dict):
    action_param = query_params.get("action", [None])[0] if "action" in query_params else None

# -------------------------
# Page: Threat Hunting
# -------------------------
if page == "Threat Hunting":
    st.header("🕵️ Threat Hunting")
    col_left, col_right = st.columns([2,1])

    with col_left:
        st.subheader("Data Controls")

        # sample size slider in sidebar for anchors + in-page generate
        sample_n = st.sidebar.slider("Sample logs (when generating)", min_value=10, max_value=100, value=50, step=5)
        if st.button("Generate sample logs (in-page)"):
            df_new = generate_sample_logs(sample_n)
            st.session_state.df = df_new
            audit_add(st.session_state.user, st.session_state.role, "Generate", f"{sample_n} sample logs generated (in-page)")
            st.success(f"Generated {sample_n} sample logs.")

        uploaded = st.file_uploader("Upload logs (CSV / JSON / XLSX)", type=["csv","json","xls","xlsx"])
        if uploaded is not None:
            if not can_upload:
                st.warning("Your role cannot upload files.")
                audit_add(st.session_state.user, st.session_state.role, "UploadDenied", "Role denied upload")
            else:
                df_u = read_uploaded_file(uploaded)
                if df_u is not None:
                    # ensure basic columns exist (best effort)
                    for c in ["timestamp","src_ip","dst_ip","protocol","bytes"]:
                        if c not in df_u.columns:
                            df_u[c] = "" if c!="bytes" else 0
                    if "quarantined" not in df_u.columns:
                        df_u["quarantined"] = False
                    st.session_state.df = df_u
                    audit_add(st.session_state.user, st.session_state.role, "Upload", f"Uploaded {uploaded.name}")
                    st.success(f"Uploaded {uploaded.name} ({len(df_u)} rows).")

        st.markdown("### Machine Learning")
        cont = st.slider("Contamination (expected anomaly fraction)", min_value=0.01, max_value=0.2, value=0.05, step=0.01)
        if st.button("Train & Score (in-page)"):
            if not can_train:
                st.warning("Your role cannot train models.")
                audit_add(st.session_state.user, st.session_state.role, "TrainDenied", "Role denied training")
            else:
                if st.session_state.df is None or st.session_state.df.empty:
                    st.warning("No data available. Generate or upload logs first.")
                else:
                    df_f, feats = create_features(st.session_state.df)
                    model = train_isolation_forest(feats, cont=cont)
                    scored = score_with_iforest(df_f, model, feats)
                    st.session_state.model = model
                    st.session_state.df = scored
                    st.session_state.model_stats = {"contamination": cont, "n_samples": len(feats)}
                    audit_add(st.session_state.user, st.session_state.role, "TrainScore", f"Trained+scored on {len(feats)} rows")
                    st.success("Model trained and logs scored.")

        st.markdown("### Containment")
        if st.button("Auto-Contain Top 5 suspicious (in-page)"):
            if not can_contain:
                st.warning("Only Admin can auto-contain. Action denied.")
                audit_add(st.session_state.user, st.session_state.role, "ContainDenied", "Role denied auto-contain")
            else:
                if st.session_state.df is None or st.session_state.df.empty or "anomaly_score" not in st.session_state.df.columns:
                    st.warning("No scored data to contain. Run Train & Score first.")
                else:
                    dfc = st.session_state.df.copy()
                    top = dfc.sort_values("anomaly_score", ascending=False).head(10)
                    ips = top["src_ip"].value_counts().index.tolist()[:5]
                    dfc.loc[dfc["src_ip"].isin(ips), "quarantined"] = True
                    st.session_state.df = dfc
                    audit_add(st.session_state.user, st.session_state.role, "AutoContain", f"Quarantined {len(ips)} src_ip(s)")
                    st.success(f"Quarantined {len(ips)} source IP(s).")

        st.markdown("---")
        st.markdown("### Download / Export")
        if st.session_state.df is not None and not st.session_state.df.empty:
            col_dl1, col_dl2, col_dl3 = st.columns(3)
            with col_dl1:
                st.download_button("Download CSV", data=convert_df_to_csv(st.session_state.df),
                                   file_name="agentic_results.csv", mime="text/csv")
            with col_dl2:
                st.download_button("Download JSON", data=convert_df_to_json(st.session_state.df),
                                   file_name="agentic_results.json", mime="application/json")
            with col_dl3:
                st.download_button("Download XLSX", data=convert_df_to_excel(st.session_state.df),
                                   file_name="agentic_results.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        else:
            st.info("No data to download yet (generate or upload first).")

    with col_right:
        st.subheader("Session / Model Info")
        st.write(f"User: **{st.session_state.user}** — Role: **{st.session_state.role}**")
        st.markdown("**Model stats**")
        st.json(st.session_state.model_stats if st.session_state.model_stats else {"status": "no model"})
        st.markdown("---")
        st.subheader("Audit (recent)")
        if st.session_state.audit:
            df_a = pd.DataFrame(st.session_state.audit).head(50)
            st.table(df_a[["timestamp","user","role","action","details"]])
            st.download_button("Download Audit CSV", data=convert_df_to_csv(df_a),
                               file_name="audit_recent.csv", mime="text/csv")
        else:
            st.info("No audit entries yet.")

    st.markdown("---")
    st.subheader("Data Snapshot & Visualizations")
    if st.session_state.df is None or st.session_state.df.empty:
        st.info("No logs loaded. Use Generate or Upload to begin.")
    else:
        st.write(f"Records: {len(st.session_state.df)}")
        st.dataframe(st.session_state.df.head(200), use_container_width=True)

        if "anomaly_score" in st.session_state.df.columns:
            fig = px.histogram(st.session_state.df, x="anomaly_score", nbins=30, title="Anomaly Score Distribution")
            st.plotly_chart(fig, use_container_width=True)
            net_fig = network_plot_from_df(st.session_state.df)
            if net_fig is not None:
                st.plotly_chart(net_fig, use_container_width=True)
        else:
            st.info("No anomaly scores present. Run Train & Score.")

# -------------------------
# Anchor action handling (executed regardless of page; enforce role checks)
# -------------------------
if action_param:
    # map anchor actions to operations, but respect role permissions
    token = action_param
    # For anchors that affect data, perform them and show messages
    if token == "generate":
        # generate using sidebar sample_n if present
        sample_n = int(st.session_state.get("sample_n", 50)) if "sample_n" in st.session_state else 50
        # read slider value if present (sidebar)
        try:
            # reading slider directly not possible here if not in session; fallback to 50
            sample_n = int(st.sidebar._state.session_state.get("slider", sample_n)) if False else st.sidebar.slider("Number of sample logs", 10, 100, 50)
        except Exception:
            sample_n = st.sidebar.slider("Number of sample logs", 10, 100, 50)
        st.session_state.df = generate_sample_logs(sample_n)
        audit_add(st.session_state.user, st.session_state.role, "Generate", f"{sample_n} logs generated (anchor)")
        st.experimental_rerun()

    if token == "train":
        if not can_train:
            st.warning("Your role is not permitted to train models. (Anchor train blocked.)")
            audit_add(st.session_state.user, st.session_state.role, "TrainDenied", "Role denied anchor-train")
        else:
            if st.session_state.df is None or st.session_state.df.empty:
                st.warning("No data available to train.")
            else:
                df_f, feats = create_features(st.session_state.df)
                model = train_isolation_forest(feats, cont=0.05)
                st.session_state.model = model
                st.session_state.df = df_f
                st.session_state.model_stats = {"contamination":0.05, "n_samples": len(feats)}
                audit_add(st.session_state.user, st.session_state.role, "Train", f"Trained on {len(feats)} rows (anchor)")
                st.success("Model trained (anchor).")
                st.experimental_rerun()

    if token == "score":
        if not can_score:
            st.warning("Your role is not permitted to score models. (Anchor score blocked.)")
            audit_add(st.session_state.user, st.session_state.role, "ScoreDenied", "Role denied anchor-score")
        else:
            if st.session_state.model is None:
                st.warning("No trained model present. Train first.")
            else:
                df_f, feats = create_features(st.session_state.df)
                df_scored = score_with_iforest(df_f, st.session_state.model, feats)
                st.session_state.df = df_scored
                audit_add(st.session_state.user, st.session_state.role, "Score", f"Scored {len(feats)} rows (anchor)")
                st.success("Logs scored (anchor).")
                st.experimental_rerun()

    if token == "auto_contain":
        if not can_contain:
            st.warning("Only Admin can auto-contain. (Anchor blocked.)")
            audit_add(st.session_state.user, st.session_state.role, "ContainDenied", "Role denied anchor-contain")
        else:
            if st.session_state.df is None or st.session_state.df.empty or "anomaly_score" not in st.session_state.df.columns:
                st.warning("No scored data to contain. Run Train & Score first.")
            else:
                dfc = st.session_state.df.copy()
                top = dfc.sort_values("anomaly_score", ascending=False).head(10)
                ips = top["src_ip"].value_counts().index.tolist()[:5]
                dfc.loc[dfc["src_ip"].isin(ips), "quarantined"] = True
                st.session_state.df = dfc
                audit_add(st.session_state.user, st.session_state.role, "AutoContain", f"Quarantined {len(ips)} src_ips (anchor)")
                st.success("Auto-contain executed (anchor).")
                st.experimental_rerun()

    if token == "download_csv":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No data to download.")
            audit_add(st.session_state.user, st.session_state.role, "DownloadDenied", "No data")
        else:
            csvb = convert_df_to_csv(st.session_state.df)
            download_link_bytes(csvb, "agentic_results.csv", "Download CSV (anchor)")
            audit_add(st.session_state.user, st.session_state.role, "Download", "CSV downloaded (anchor)")

    if token == "download_json":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No data to download.")
            audit_add(st.session_state.user, st.session_state.role, "DownloadDenied", "No data")
        else:
            jb = convert_df_to_json(st.session_state.df)
            download_link_bytes(jb, "agentic_results.json", "Download JSON (anchor)")
            audit_add(st.session_state.user, st.session_state.role, "Download", "JSON downloaded (anchor)")

    if token == "download_xlsx":
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("No data to download.")
            audit_add(st.session_state.user, st.session_state.role, "DownloadDenied", "No data")
        else:
            xb = convert_df_to_excel(st.session_state.df)
            download_link_bytes(xb, "agentic_results.xlsx", "Download XLSX (anchor)")
            audit_add(st.session_state.user, st.session_state.role, "Download", "XLSX downloaded (anchor)")

    if token == "reset":
        if not can_reset:
            st.warning("Only Admin can reset the session. (Anchor reset blocked.)")
            audit_add(st.session_state.user, st.session_state.role, "ResetDenied", "Role denied anchor-reset")
        else:
            st.session_state.df = pd.DataFrame()
            st.session_state.model = None
            st.session_state.model_stats = {}
            audit_add(st.session_state.user, st.session_state.role, "Reset", "Session reset (anchor)")
            # clear URL params if possible
            try:
                st.experimental_set_query_params()
            except Exception:
                pass
            st.success("Session reset (anchor).")
            st.experimental_rerun()

# -------------------------
# Incident Playbooks page (simple CRUD demo)
# -------------------------
if page == "Incident Playbooks":
    st.header("📘 Incident Playbooks (Demo)")
    if "playbooks" not in st.session_state:
        st.session_state.playbooks = []
    for i, pb in enumerate(st.session_state.playbooks):
        with st.expander(f"Playbook #{i+1}: {pb.get('title','Untitled')} (status: {pb.get('status','open')})"):
            st.write(pb.get("description",""))
            st.write("Steps:")
            for s in pb.get("steps", []):
                st.write(f"- {s}")
            cols = st.columns(3)
            if cols[0].button(f"Mark Mitigated #{i}", key=f"mit_{i}"):
                st.session_state.playbooks[i]["status"] = "mitigated"
                audit_add(st.session_state.user, st.session_state.role, "PlaybookMitigated", f"Mitigated #{i+1}")
                st.experimental_rerun()
            if cols[1].button(f"Clone #{i}", key=f"clone_{i}"):
                st.session_state.playbooks.append(dict(st.session_state.playbooks[i]))
                audit_add(st.session_state.user, st.session_state.role, "PlaybookClone", f"Cloned #{i+1}")
                st.experimental_rerun()
            if cols[2].button(f"Delete #{i}", key=f"del_{i}"):
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
    new_steps_txt = st.text_area("Steps (one per line)", key="pb_steps")
    if st.button("Add Playbook"):
        steps = [s.strip() for s in new_steps_txt.splitlines() if s.strip()]
        pb = {"title": new_title or f"Playbook {len(st.session_state.playbooks)+1}",
              "description": new_desc,
              "steps": steps,
              "status": "open",
              "created_at": now_iso()}
        st.session_state.playbooks.append(pb)
        audit_add(st.session_state.user, st.session_state.role, "PlaybookAdd", f"Added '{pb['title']}'")
        st.success("Playbook created.")
        st.experimental_rerun()

# -------------------------
# Audit Logs page
# -------------------------
if page == "Audit Logs":
    st.header("📜 Audit Logs")
    if st.session_state.audit:
        df_a = pd.DataFrame(st.session_state.audit)
        st.dataframe(df_a, use_container_width=True)
        st.download_button("Download Audit CSV", data=convert_df_to_csv(df_a), file_name="audit_logs.csv", mime="text/csv")
    else:
        st.info("No audit entries yet.")

# -------------------------
# Footer
# -------------------------
st.markdown("---")
st.caption("Agentic Cyber ML — Demo. Not for production use. Role handling is local and for demonstration only.")
