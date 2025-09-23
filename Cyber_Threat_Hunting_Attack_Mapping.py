# Cyber_Threat_Hunting_Attack_Mapping

# Use Case:

# Graph-based reasoning to link attacker behaviors (MITRE ATT&CK, logs, alerts)

# LLM explanations to describe anomalies and suggest remediation

# THIS APPLICATION IS DESIGNED & DEVELOPED BY RANDY SINGH FROM KNet CONSULTING GROUP.



import streamlit as st

import pandas as pd

import numpy as np

import networkx as nx

from pyvis.network import Network

import streamlit.components.v1 as components

import json

import io

import os

from datetime import datetime, timedelta

import random

from pathlib import Path



# Optional OpenAI. If not installed or API key not set, app falls back to rule-based explanations.

try:

    import openai

    OPENAI_AVAILABLE = True

except Exception:

    OPENAI_AVAILABLE = False



# -------------------------

# Utilities / Session init

# -------------------------

def set_page_config():

    st.set_page_config(page_title="Cyber Threat Hunting & Attack Mapping", layout="wide", initial_sidebar_state="expanded")



def inject_css():

    st.markdown(

        """

        <style>

        /* Background & card */

        .stApp {

            background: linear-gradient(180deg, #071A2D 0%, #0f1724 100%);

            color: #edf6ff;

        }

        .big-button {

            background: linear-gradient(90deg,#0077b6,#00b4d8);

            color: white;

            font-weight: 700;

            border-radius: 8px;

            padding: 8px 12px;

            margin: 4px 0;

        }

        .secondary-button {

            background: linear-gradient(90deg,#6a11cb,#2575fc);

            color: white;

            font-weight: 600;

            border-radius: 8px;

            padding: 6px 10px;

        }

        .danger-button {

            background: linear-gradient(90deg,#ff4d6d,#ff7a6b);

            color: white;

            font-weight: 700;

            border-radius: 8px;

            padding: 6px 10px;

        }

        .card {

            background: rgba(255,255,255,0.03);

            padding: 14px;

            border-radius: 10px;

            margin-bottom: 12px;

        }

        .small-mono { font-family: monospace; font-size: 12px; color:#cfe9ff; }

        </style>

        """, unsafe_allow_html=True

    )



def init_session_state():

    if "events_df" not in st.session_state:

        st.session_state["events_df"] = None

    if "graph" not in st.session_state:

        st.session_state["graph"] = None

    if "detections" not in st.session_state:

        st.session_state["detections"] = []

    if "summary_text" not in st.session_state:

        st.session_state["summary_text"] = ""

    if "last_action" not in st.session_state:

        st.session_state["last_action"] = None



# -------------------------

# Sample data generator

# -------------------------

MITRE_EX = [

    ("T1110", "Brute Force / Credential Stuffing"),

    ("T1078", "Valid Accounts"),

    ("T1059", "Command and Scripting Interpreter"),

    ("T1566", "Phishing"),

    ("T1210", "Exploitation"),

]



def gen_sample_events(n=200, start_time=None):

    if start_time is None:

        start_time = datetime.utcnow() - timedelta(days=7)



    users = [f"user{i}" for i in range(1, 31)]

    hosts = [f"host{i}.corp.local" for i in range(1, 25)]

    ip_pool = [f"10.0.{i}.{j}" for i in range(1, 10) for j in range(1, 50)]

    actions = ["login", "file_access", "cmd_exec", "svc_start"]

    results = ["success", "failure"]

    events = []



    # inject credential-stuffing pattern

    stuffed_ip = random.choice(ip_pool)

    stuffed_users = random.sample(users, k=8)

    ts = start_time

    for u in stuffed_users:

        events.append({

            "timestamp": ts.isoformat(),

            "src_ip": stuffed_ip,

            "dest_host": random.choice(hosts),

            "user": u,

            "action": "login",

            "result": "failure",

            "alert": "",

            "mitre_id": "T1110",

            "mitre_desc": "Brute Force / Credential Stuffing"

        })

        ts += timedelta(seconds=random.randint(10, 90))

    # final success

    events.append({

        "timestamp": (ts + timedelta(seconds=20)).isoformat(),

        "src_ip": stuffed_ip,

        "dest_host": random.choice(hosts),

        "user": random.choice(stuffed_users),

        "action": "login",

        "result": "success",

        "alert": "suspicious_success_after_many_failures",

        "mitre_id": "T1110",

        "mitre_desc": "Brute Force / Credential Stuffing"

    })



    # churn the rest of events

    ts = start_time

    for i in range(n - len(events)):

        ts += timedelta(seconds=random.randint(30, 600))

        src = random.choice(ip_pool)

        user = random.choice(users)

        host = random.choice(hosts)

        action = random.choices(actions, weights=[0.6,0.2,0.15,0.05])[0]

        result = random.choices(results, weights=[0.82,0.18])[0]

        mitre_id = ""

        mitre_desc = ""

        if action == "cmd_exec" and random.random() < 0.03:

            mitre_id, mitre_desc = ("T1059", "Command and Scripting Interpreter")

        if action == "login" and result == "failure" and random.random() < 0.05:

            mitre_id, mitre_desc = random.choice(MITRE_EX)

        events.append({

            "timestamp": ts.isoformat(),

            "src_ip": src,

            "dest_host": host,

            "user": user,

            "action": action,

            "result": result,

            "alert": "",

            "mitre_id": mitre_id,

            "mitre_desc": mitre_desc

        })



    df = pd.DataFrame(events)

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df.sort_values("timestamp", inplace=True)

    df.reset_index(drop=True, inplace=True)

    return df



# -------------------------

# Graph builder & detectors

# -------------------------

def build_graph_from_events(df: pd.DataFrame):

    G = nx.DiGraph()

    for _, row in df.iterrows():

        ts = row["timestamp"]

        src = f"IP:{row['src_ip']}"

        user = f"User:{row['user']}"

        host = f"Host:{row['dest_host']}"

        G.add_node(src, label=row['src_ip'], ntype="ip")

        G.add_node(user, label=row['user'], ntype="user")

        G.add_node(host, label=row['dest_host'], ntype="host")

        G.add_edge(src, user, edge_type="attempt", timestamp=ts.isoformat(), action=row.get("action",""), result=row.get("result",""))

        G.add_edge(user, host, edge_type="access", timestamp=ts.isoformat(), action=row.get("action",""), result=row.get("result",""))

        if pd.notna(row.get("mitre_id")) and row.get("mitre_id") != "":

            mitre = f"MITRE:{row['mitre_id']}"

            G.add_node(mitre, label=row['mitre_id'], ntype="mitre", desc=row.get("mitre_desc",""))

            G.add_edge(user, mitre, edge_type="mapped", timestamp=ts.isoformat())

    return G



def detect_credential_stuffing(df: pd.DataFrame, fail_threshold=5, window_minutes=60):

    detections = []

    logins = df[(df["action"] == "login")].copy()

    logins["ts"] = pd.to_datetime(logins["timestamp"])

    for ip, group in logins.groupby("src_ip"):

        group = group.sort_values("ts")

        for i in range(len(group)):

            window_start = group.iloc[i]["ts"]

            window_end = window_start + pd.Timedelta(minutes=window_minutes)

            window = group[(group["ts"] >= window_start) & (group["ts"] <= window_end)]

            failed_users = window[window["result"] == "failure"]["user"].nunique()

            if failed_users >= fail_threshold:

                detections.append({

                    "type": "credential_stuffing",

                    "src_ip": ip,

                    "start": window_start.isoformat(),

                    "end": window["ts"].max().isoformat(),

                    "failed_user_count": failed_users,

                    "evidence": window

                })

                break

    return detections



def detect_brute_force(df: pd.DataFrame, attempts_threshold=10):

    detections = []

    logins = df[(df["action"] == "login")].copy()

    logins["ts"] = pd.to_datetime(logins["timestamp"])

    for user, group in logins.groupby("user"):

        failed_attempts = group[group["result"] == "failure"]

        if len(failed_attempts) >= attempts_threshold:

            detections.append({

                "type": "brute_force_target",

                "user": user,

                "failed_attempts": len(failed_attempts),

                "distinct_ips": failed_attempts["src_ip"].nunique(),

                "evidence": failed_attempts

            })

    return detections



def detect_lateral_movement(df: pd.DataFrame):

    detections = []

    df2 = df.copy()

    df2["ts"] = pd.to_datetime(df2["timestamp"])

    for user, group in df2.groupby("user"):

        user_succ = group[(group["action"] == "login") & (group["result"] == "success")].sort_values("ts")

        if user_succ.empty:

            continue

        for _, row in user_succ.iterrows():

            t0 = row["ts"]

            window = group[(group["ts"] >= t0) & (group["ts"] <= t0 + pd.Timedelta(hours=2))]

            hosts_accessed = window["dest_host"].nunique()

            if hosts_accessed >= 3:

                detections.append({

                    "type": "possible_lateral_movement",

                    "user": user,

                    "start": t0.isoformat(),

                    "hosts_count": hosts_accessed,

                    "evidence": window

                })

                break

    return detections



# -------------------------

# LLM explanation helpers

# -------------------------

def rule_based_explanation(summary: str):

    summary_low = summary.lower()

    if "credential_stuffing" in summary_low or "credential stuffing" in summary_low or "brute force" in summary_low:

        return (

            "Explanation: Multiple failed login attempts from a single IP targeting many usernames indicates credential-stuffing.\n"

            "MITRE mapping: T1110 - Brute Force / Credential Stuffing.\n"

            "Remediation:\n"

            "1) Block or throttle the offending IP; add to firewall/IDS deny list.\n"

            "2) Enforce MFA and strong password policies.\n"

            "3) Reset affected credentials and monitor for lateral movement."

        )

    if "brute_force_target" in summary_low:

        return (

            "Explanation: One account is seeing many failed logins from multiple IPs - possible brute-force targeting.\n"

            "MITRE mapping: T1110 / T1078.\n"

            "Remediation:\n"

            "1) Temporarily lock the account; force password reset.\n"

            "2) Enable MFA and throttle auth attempts.\n"

            "3) Investigate and block malicious sources."

        )

    if "lateral" in summary_low:

        return (

            "Explanation: Same user performed actions across multiple hosts shortly after login - possible lateral movement.\n"

            "MITRE mapping: T1021 / T1075 dependent on context.\n"

            "Remediation:\n"

            "1) Isolate affected hosts and collect for forensics.\n"

            "2) Rotate credentials and review privileged accounts.\n"

            "3) Increase monitoring and containment."

        )

    return "Explanation: Unusual activity detected. Review evidence and apply incident response."



def llm_explain_detection(detection_summary: str, openai_api_key: str = None, model="gpt-4o-mini"):

    key = openai_api_key or os.environ.get("OPENAI_API_KEY")

    if OPENAI_AVAILABLE and key:

        try:

            openai.api_key = key

            prompt = (

                "You are a SOC assistant. Explain the detection in plain English, map to MITRE ATT&CK techniques if applicable, "

                "and suggest 3 specific remediation steps.\n\nDetection Summary:\n" + detection_summary

            )

            resp = openai.ChatCompletion.create(

                model=model,

                messages=[{"role":"system","content":"You are a cybersecurity analyst."},

                          {"role":"user","content":prompt}],

                temperature=0.2,

                max_tokens=400

            )

            text = resp["choices"][0]["message"]["content"].strip()

            return text

        except Exception as e:

            return f"(LLM call failed: {e})\n\nFallback:\n{rule_based_explanation(detection_summary)}"

    else:

        return rule_based_explanation(detection_summary)



# -------------------------

# Visualize using pyvis

# -------------------------

def visualize_pyvis(graph: nx.Graph, height="600px", width="100%"):

    net = Network(height=height, width=width, bgcolor="#071A2D", font_color="white", directed=True)

    for n, data in graph.nodes(data=True):

        label = data.get("label", str(n))

        ntype = data.get("ntype", "other")

        title = ""

        if ntype == "ip":

            color = "#FF7A59"

            shape = "dot"

            title = f"IP: {label}"

        elif ntype == "user":

            color = "#59D2FF"

            shape = "diamond"

            title = f"User: {label}"

        elif ntype == "host":

            color = "#B19CFF"

            shape = "square"

            title = f"Host: {label}"

        elif ntype == "mitre":

            color = "#FFD86B"

            shape = "triangle"

            title = f"MITRE: {label} - {data.get('desc','')}"

        else:

            color = "#9AA7B0"

            shape = "dot"

        net.add_node(n, label=label, title=title, color=color, shape=shape)



    for u, v, d in graph.edges(data=True):

        label = d.get("edge_type", "")

        title = f"{label}\\n{d.get('action','')}\\n{d.get('result','')}\\n{d.get('timestamp','')}"

        net.add_edge(u, v, label=label, title=title)



    net.toggle_physics(True)

    return net



def render_pyvis_to_streamlit(net: Network):

    # Save to temp file and render

    tmp = Path("pyvis_temp.html")

    net.save_graph(str(tmp))

    html = tmp.read_text()

    components.html(html, height=650, scrolling=True)



# -------------------------

# IO helpers

# -------------------------

def load_uploaded_file(uploaded_file):

    name = uploaded_file.name.lower()

    if name.endswith(".csv"):

        df = pd.read_csv(uploaded_file)

    elif name.endswith(".json"):

        df = pd.read_json(uploaded_file)

    elif name.endswith(".xlsx") or name.endswith(".xls"):

        df = pd.read_excel(uploaded_file)

    else:

        raise ValueError("Unsupported file type. Upload CSV, JSON, or XLSX.")

    return df



def df_to_csv_bytes(df: pd.DataFrame):

    return df.to_csv(index=False).encode("utf-8")



def df_to_json_bytes(df: pd.DataFrame):

    return df.to_json(orient="records", date_format="iso").encode("utf-8")



# -------------------------

# Streamlit UI / Main

# -------------------------

def main():

    set_page_config()

    inject_css()

    init_session_state()



    st.markdown("<h1 style='color: #bde0fe'>Cyber Threat Hunting & Attack Mapping</h1>", unsafe_allow_html=True)

    st.markdown("<div class='card'><b>Reasoning:</b> Graph-based linking of IPs, users, hosts and MITRE techniques. <b>LLM:</b> Explain anomalies and suggest remediation (OpenAI optional).</div>", unsafe_allow_html=True)



    # Sidebar

    with st.sidebar:

        st.header("Settings & LLM")

        openai_key = st.text_input("OpenAI API Key (optional)", value=os.environ.get("OPENAI_API_KEY",""), type="password", help="Enter your OpenAI API key for LLM explanations (optional).")

        model_choice = st.selectbox("Preferred model (if available)", options=["gpt-4o-mini", "gpt-4o", "gpt-4o-mini-instruct"], index=0)

        st.markdown("---")

        st.markdown("## Detection thresholds")

        cs_fail = st.number_input("Credential-stuffing distinct failed users threshold", min_value=2, max_value=50, value=5)

        cs_window = st.number_input("Credential-stuffing window (minutes)", min_value=1, max_value=1440, value=60)

        brute_thresh = st.number_input("Brute-force attempts per user threshold", min_value=3, max_value=500, value=10)

        st.markdown("---")

        st.markdown("## Quick actions")

        if st.button("Clear all loaded data", key="sidebar_clear"):

            st.session_state["events_df"] = None

            st.session_state["graph"] = None

            st.session_state["detections"] = []

            st.session_state["summary_text"] = ""

            st.session_state["last_action"] = "cleared"

            st.success("Cleared session data.")



    # Main columns

    col1, col2 = st.columns([1.1, 2])



    with col1:

        st.markdown("### Data")

        if st.button("Generate sample data (200 events)", key="gen_sample_btn"):

            df = gen_sample_events(n=200)

            st.session_state["events_df"] = df

            st.session_state["last_action"] = "generated"

            st.success("Sample data generated (200 events).")



        uploaded = st.file_uploader("Upload CSV / JSON / XLSX", type=["csv","json","xlsx","xls"], key="uploader")

        if uploaded is not None:

            try:

                df = load_uploaded_file(uploaded)

                if "timestamp" not in df.columns:

                    df.rename(columns={df.columns[0]:"timestamp"}, inplace=True)

                # ensure minimal columns exist

                for c in ["src_ip","dest_host","user","action","result"]:

                    if c not in df.columns:

                        df[c] = np.nan

                # convert timestamp

                try:

                    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

                except Exception:

                    pass

                st.session_state["events_df"] = df

                st.session_state["last_action"] = f"uploaded:{uploaded.name}"

                st.success(f"Uploaded {uploaded.name} ({len(df)} rows).")

            except Exception as e:

                st.error(f"Failed to load file: {e}")



        st.markdown("### Controls")

        if st.session_state["events_df"] is not None:

            if st.button("Build Graph & Run Detections", key="process_btn"):

                df = st.session_state["events_df"].copy()

                if "timestamp" in df.columns:

                    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

                df["action"] = df.get("action", "login")

                df["result"] = df.get("result", "failure")

                G = build_graph_from_events(df)

                st.session_state["graph"] = G

                det_cs = detect_credential_stuffing(df, fail_threshold=int(cs_fail), window_minutes=int(cs_window))

                det_bf = detect_brute_force(df, attempts_threshold=int(brute_thresh))

                det_lat = detect_lateral_movement(df)

                detections = det_cs + det_bf + det_lat

                st.session_state["detections"] = detections

                st.session_state["last_action"] = "processed"

                st.success(f"Processed: graph nodes={len(G.nodes())}, edges={len(G.edges())}. Detections={len(detections)}.")



        if st.session_state["events_df"] is not None:

            df = st.session_state["events_df"]

            st.markdown("### Download processed data")

            st.download_button("Download events as CSV", df_to_csv_bytes(df), file_name="events.csv", mime="text/csv")

            st.download_button("Download events as JSON", df_to_json_bytes(df), file_name="events.json", mime="application/json")



            if st.session_state.get("detections"):

                dets = st.session_state["detections"]

                rows = []

                for d in dets:

                    row = {k:v for k,v in d.items() if k!="evidence"}

                    row["evidence_rows"] = len(d.get("evidence", pd.DataFrame()))

                    rows.append(row)

                df_dets = pd.DataFrame(rows)

                st.download_button("Download detections CSV", df_to_csv_bytes(df_dets), file_name="detections.csv", mime="text/csv")

                st.download_button("Download detections JSON", df_to_json_bytes(df_dets), file_name="detections.json", mime="application/json")



    with col2:

        st.markdown("### Visualizations & Results")

        if st.session_state["events_df"] is None:

            st.info("No data loaded. Generate sample data or upload logs to begin.")

        else:

            df = st.session_state["events_df"].copy()

            st.markdown("#### Events sample (first 20 rows)")

            st.dataframe(df.head(20), height=220)



            st.markdown("#### Summary metrics")

            cols = st.columns(3)

            cols[0].metric("Total Events", f"{len(df)}")

            cols[1].metric("Unique IPs", f"{df['src_ip'].nunique() if 'src_ip' in df.columns else 'N/A'}")

            cols[2].metric("Unique Users", f"{df['user'].nunique() if 'user' in df.columns else 'N/A'}")



            # show detections if any

            if st.session_state.get("detections"):

                st.markdown("#### Detections")

                for idx, det in enumerate(st.session_state["detections"], start=1):

                    d_type = det.get("type", "unknown")

                    with st.expander(f"{idx}. {d_type}"):

                        # show high level

                        meta = {k:v for k,v in det.items() if k not in ("evidence",)}

                        st.json(meta)

                        # show sample evidence

                        ev = det.get("evidence")

                        if isinstance(ev, pd.DataFrame) and not ev.empty:

                            st.markdown("**Evidence sample (first 10 rows)**")

                            st.dataframe(ev.head(10))

                        # LLM / explanation

                        if st.button(f"Explain detection {idx} with LLM", key=f"explain_{idx}"):

                            summary_text = json.dumps(meta, default=str, indent=2)

                            explanation = llm_explain_detection(summary_text, openai_api_key=openai_key, model=model_choice)

                            st.session_state["summary_text"] = explanation

                            st.markdown("**LLM Explanation / Remediation**")

                            st.markdown(f"```\n{explanation}\n```")