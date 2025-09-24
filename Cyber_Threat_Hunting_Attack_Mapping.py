

# app_fixed_queryparams.py
# Cyber Threat Hunting & Attack Mapping (final)
# Preserves original functions; fixes query param API usage.
# Designed by Randy Singh — KNet Consulting Group

import streamlit as st
import pandas as pd
import numpy as np
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components
import random, os, io, json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Optional OpenAI (modern client detection)
try:
    import openai
    try:
        from openai import OpenAI as OpenAIClientClass  # newer client (if installed)
    except Exception:
        OpenAIClientClass = None
    OPENAI_AVAILABLE = True
except Exception:
    openai = None
    OpenAIClientClass = None
    OPENAI_AVAILABLE = False

# ----------------------------
# ORIGINAL CORE FUNCTIONS (kept unchanged where requested)
# ----------------------------
def generate_sample_data(n=200):
    users = [f"user{i}" for i in range(1, 11)]
    hosts = [f"host{i}.corp.local" for i in range(1, 6)]
    ips = [f"10.0.{i}.{j}" for i in range(1, 3) for j in range(1, 100)]
    actions = ["login", "file_access", "cmd_exec"]
    results = ["success", "failure"]

    events = []
    ts = datetime.utcnow() - timedelta(days=1)
    for _ in range(n):
        ts += timedelta(seconds=random.randint(30, 300))
        events.append({
            "timestamp": ts.isoformat(),
            "src_ip": random.choice(ips),
            "dest_host": random.choice(hosts),
            "user": random.choice(users),
            "action": random.choice(actions),
            "result": random.choice(results),
        })
    return pd.DataFrame(events)


def build_graph(df):
    G = nx.DiGraph()
    for _, row in df.iterrows():
        ip = f"IP:{row['src_ip']}"
        user = f"User:{row['user']}"
        host = f"Host:{row['dest_host']}"
        G.add_node(ip, label=row['src_ip'], ntype="ip")
        G.add_node(user, label=row['user'], ntype="user")
        G.add_node(host, label=row['dest_host'], ntype="host")
        G.add_edge(ip, user, action=row['action'], result=row['result'])
        G.add_edge(user, host, action=row['action'], result=row['result'])
    return G


def detect_credential_stuffing(df):
    detections = []
    failed = df[(df["action"] == "login") & (df["result"] == "failure")]
    for ip, group in failed.groupby("src_ip"):
        if group["user"].nunique() > 5:
            detections.append(f"Credential Stuffing from {ip}")
    return detections


# ----------------------------
# Modern / robust LLM explanation
# ----------------------------
def explain_detection(text, api_key=None, model="gpt-4o-mini"):
    if not OPENAI_AVAILABLE:
        return f"[No LLM installed] Rule-based explanation: {text}. Mitigation: block IP, enable MFA, monitor logs."

    key = api_key or os.getenv("OPENAI_API_KEY")
    if not key:
        return f"[No API key] Rule-based explanation: {text}. Mitigation: block IP, enable MFA, monitor logs."

    try:
        # Try modern OpenAI client first (if installed)
        if OpenAIClientClass is not None:
            client = OpenAIClientClass(api_key=key)
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a SOC assistant."},
                    {"role": "user", "content": f"Explain this detection: {text}"}
                ],
                max_tokens=220,
            )
            try:
                return resp.choices[0].message.content
            except Exception:
                return str(resp)
        else:
            # Fallback to legacy method if available
            resp = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a SOC assistant."},
                    {"role": "user", "content": f"Explain this detection: {text}"}
                ],
                max_tokens=220,
                api_key=key
            )
            return resp["choices"][0]["message"]["content"]
    except Exception as e:
        return f"LLM call failed: {e}. Fallback rule-based: {text}. Suggested: block IP, enable MFA, monitor logs."


# ----------------------------
# Visualization helper (unchanged behavior)
# ----------------------------
def visualize_graph(G, filename="graph.html", height=550):
    net = Network(height=f"{height}px", width="100%", bgcolor="#0f172a", font_color="white", directed=True)
    for node, data in G.nodes(data=True):
        color = "#60a5fa" if data["ntype"] == "ip" else "#34d399" if data["ntype"] == "user" else "#fbbf24"
        net.add_node(node, label=data["label"], color=color)
    for u, v, d in G.edges(data=True):
        net.add_edge(u, v, label=d.get("action", ""))
    net.save_graph(filename)
    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()
    components.html(html, height=height, scrolling=True)


# ----------------------------
# Timestamp normalizer
# ----------------------------
def _ensure_timestamp(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "timestamp" not in df.columns:
        base = pd.Timestamp.utcnow() - pd.Timedelta(days=1)
        df["timestamp"] = [ (base + pd.Timedelta(seconds=i*60)).isoformat() for i in range(len(df)) ]
    def _extract(x):
        if isinstance(x, list):
            return x[0] if x else None
        if isinstance(x, dict):
            for k in ("timestamp","time","ts","date"):
                if k in x:
                    return x[k]
            return None
        return x
    df["timestamp"] = df["timestamp"].apply(_extract)
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    if df["timestamp"].isna().all():
        base = pd.Timestamp.utcnow() - pd.Timedelta(days=1)
        df["timestamp"] = [ base + pd.Timedelta(seconds=i*60) for i in range(len(df)) ]
    elif df["timestamp"].isna().any():
        existing_max = df["timestamp"].max()
        if pd.isna(existing_max):
            existing_max = pd.Timestamp.utcnow()
        missing_idx = df.index[df["timestamp"].isna()].tolist()
        for j, idx in enumerate(missing_idx):
            df.at[idx, "timestamp"] = existing_max + pd.Timedelta(seconds=(j+1)*60)
    return df


# ----------------------------
# Additional detectors & helpers
# ----------------------------
def detect_bruteforce_user(df, threshold_failures=8, window_minutes=30):
    df = _ensure_timestamp(df)
    detections = []
    failed = df[(df["action"] == "login") & (df["result"] == "failure")]
    for user, group in failed.groupby("user"):
        group = group.sort_values("timestamp")
        times = group["timestamp"].tolist()
        for i in range(len(times)):
            start = times[i]
            end = start + pd.Timedelta(minutes=window_minutes)
            subset = group[(group["timestamp"] >= start) & (group["timestamp"] <= end)]
            if len(subset) >= threshold_failures:
                ips = subset["src_ip"].nunique()
                detections.append(f"Brute-force against user {user}: {len(subset)} failures from {ips} IP(s) in {window_minutes}m")
                break
    return detections

def detect_port_scan_like(df, threshold_hosts=4, window_minutes=10):
    df = _ensure_timestamp(df)
    detections = []
    for ip, group in df.sort_values("timestamp").groupby("src_ip"):
        for i in range(len(group)):
            start = group["timestamp"].iloc[i]
            end = start + pd.Timedelta(minutes=window_minutes)
            subset = group[(group["timestamp"] >= start) & (group["timestamp"] <= end)]
            if subset["dest_host"].nunique() >= threshold_hosts:
                detections.append(f"Port-scan-like / host sweep from {ip} (hit {subset['dest_host'].nunique()} hosts in {window_minutes}m)")
                break
    return detections

def detect_data_exfiltration_like(df, threshold_files=6, window_hours=4):
    df = _ensure_timestamp(df)
    detections = []
    facc = df[(df["action"] == "file_access") & (df["result"] == "success")].sort_values("timestamp")
    for key, group in facc.groupby(["src_ip", "user"]):
        times = group["timestamp"].tolist()
        for i in range(len(times)):
            start = times[i]
            end = start + pd.Timedelta(hours=window_hours)
            subset = group[(group["timestamp"] >= start) & (group["timestamp"] <= end)]
            if len(subset) >= threshold_files and subset["dest_host"].nunique() >= 2:
                detections.append(f"Data-exfiltration-like activity by user {key[1]} from {key[0]}: {len(subset)} file accesses across {subset['dest_host'].nunique()} hosts in {window_hours}h")
                break
    return detections

def aggregate_detections(df, params):
    dets = []
    for d in detect_credential_stuffing(df):
        dets.append({"type": "credential_stuffing", "text": d, "severity": "high"})
    for d in detect_port_scan_like(df, threshold_hosts=params.get("port_scan_hosts",4), window_minutes=params.get("port_scan_window",10)):
        dets.append({"type": "port_scan", "text": d, "severity": "medium"})
    for d in detect_bruteforce_user(df, threshold_failures=params.get("brute_force_failures",8), window_minutes=params.get("brute_force_window",30)):
        dets.append({"type": "brute_force_user", "text": d, "severity": "high"})
    for d in detect_data_exfiltration_like(df, threshold_files=params.get("data_exfil_files",6), window_hours=params.get("data_exfil_window",4)):
        dets.append({"type": "data_exfiltration", "text": d, "severity": "critical"})
    return dets

def visualize_graph_highlight(G, detections, filename="graph_highlight.html"):
    highlight_nodes = set()
    for d in detections:
        txt = d["text"]
        for token in txt.replace(",", " ").split():
            if token.count('.') == 3 and token.startswith("10."):
                highlight_nodes.add(f"IP:{token}")
            if token.startswith("user"):
                highlight_nodes.add(f"User:{token}")
            if token.startswith("host"):
                if "." not in token:
                    highlight_nodes.add(f"Host:{token}.corp.local")
                else:
                    highlight_nodes.add(f"Host:{token}")
            if token.startswith("IP:") or token.startswith("User:") or token.startswith("Host:"):
                highlight_nodes.add(token)

    net = Network(height="650px", width="100%", bgcolor="#0f172a", font_color="white", directed=True)
    for node, data in G.nodes(data=True):
        base_color = "#60a5fa" if data["ntype"] == "ip" else "#34d399" if data["ntype"] == "user" else "#fbbf24"
        if node in highlight_nodes:
            net.add_node(node, label=data["label"], color="#ef4444", size=30)
        else:
            net.add_node(node, label=data["label"], color=base_color)
    for u, v, d in G.edges(data=True):
        label = d.get("action", "")
        net.add_edge(u, v, label=label)
    net.save_graph(filename)
    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()
    components.html(html, height=700, scrolling=True)


# Targeted anomaly generator
def generate_targeted_anomaly(df, anomaly_type="credential_stuffing", n=50):
    base_df = df if (df is not None and isinstance(df, pd.DataFrame) and not df.empty) else generate_sample_data(50)
    users = base_df["user"].unique().tolist() if "user" in base_df.columns else [f"user{i}" for i in range(1, 11)]
    hosts = base_df["dest_host"].unique().tolist() if "dest_host" in base_df.columns else [f"host{i}.corp.local" for i in range(1, 6)]
    base_ts = datetime.utcnow() - timedelta(hours=1)
    ips_pool = [f"10.0.250.{i}" for i in range(1, 255)]

    new_events = []
    if anomaly_type == "credential_stuffing":
        bad_ip = random.choice(ips_pool)
        for i in range(n):
            new_events.append({
                "timestamp": (base_ts + timedelta(seconds=i*5)).isoformat(),
                "src_ip": bad_ip,
                "dest_host": random.choice(hosts),
                "user": f"user{(i % 12) + 1}",
                "action": "login",
                "result": "failure"
            })
    elif anomaly_type == "brute_force_user":
        target_user = random.choice(users)
        for i in range(n):
            new_events.append({
                "timestamp": (base_ts + timedelta(seconds=i*7)).isoformat(),
                "src_ip": random.choice(ips_pool),
                "dest_host": random.choice(hosts),
                "user": target_user,
                "action": "login",
                "result": "failure"
            })
    elif anomaly_type == "port_scan":
        bad_ip = random.choice(ips_pool)
        for i in range(n):
            new_events.append({
                "timestamp": (base_ts + timedelta(seconds=i*3)).isoformat(),
                "src_ip": bad_ip,
                "dest_host": hosts[i % len(hosts)],
                "user": random.choice(users),
                "action": "file_access",
                "result": "failure" if i % 5 else "success"
            })
    elif anomaly_type == "data_exfiltration":
        bad_ip = random.choice(ips_pool)
        bad_user = random.choice(users)
        for i in range(n):
            new_events.append({
                "timestamp": (base_ts + timedelta(seconds=i*45)).isoformat(),
                "src_ip": bad_ip,
                "dest_host": hosts[i % len(hosts)],
                "user": bad_user,
                "action": "file_access",
                "result": "success"
            })
    else:
        for i in range(n):
            new_events.append({
                "timestamp": (base_ts + timedelta(seconds=i*10)).isoformat(),
                "src_ip": random.choice(ips_pool),
                "dest_host": random.choice(hosts),
                "user": random.choice(users),
                "action": random.choice(["login", "file_access", "cmd_exec"]),
                "result": random.choice(["success", "failure"])
            })
    return pd.concat([base_df, pd.DataFrame(new_events)], ignore_index=True)


# MITRE mapping + playbooks
MITRE_MAP = {
    "credential_stuffing": [("TA0006 - Credential Access", "T1110.004 - Credential Stuffing"), ("TA0006", "T1110 - Brute Force")],
    "brute_force_user": [("TA0006", "T1110 - Brute Force"), ("TA0006", "T1110.001 - Password Guessing")],
    "port_scan": [("TA0043 - Reconnaissance", "T1595 - Active Scanning")],
    "data_exfiltration": [("TA0010 - Exfiltration", "T1020 - Automated Exfiltration"), ("TA0010", "T1041 - Exfiltration Over C2")],
}
PLAYBOOKS = {
    "credential_stuffing": [
        "Block offending IP(s) at perimeter and application layer.",
        "Enable MFA and force password resets as needed.",
        "Add rate-limiting and CAPTCHA for authentication endpoints."
    ],
    "brute_force_user": [
        "Lock the targeted account(s) and collect logs for forensics.",
        "Force credential rotation and enable MFA.",
        "Monitor for lateral movement from same source IPs."
    ],
    "port_scan": [
        "Block the scanning IPs and review firewall rules.",
        "Harden hosts and close unused ports/services.",
        "Check IDS/packet capture for more indicators."
    ],
    "data_exfiltration": [
        "Isolate endpoint(s) and collect forensic artifacts.",
        "Review outbound logs and cloud uploads.",
        "Engage incident response and legal/compliance."
    ]
}

# ----------------------------
# Streamlit UI - final
# ----------------------------
def main():
    st.set_page_config(page_title="Cyber Threat Hunting - Final", layout="wide", initial_sidebar_state="expanded")

    # Query-param backed theme persistence (NO experimental_* calls)
    qp = st.query_params  # read query params
    if "theme" not in st.session_state:
        theme_from_q = qp.get("theme")
        if theme_from_q:
            st.session_state["theme"] = theme_from_q[0] if isinstance(theme_from_q, list) else theme_from_q
        else:
            st.session_state["theme"] = "Dark"

    theme = st.sidebar.radio("Theme", ["Dark", "Light"], index=0 if st.session_state["theme"] == "Dark" else 1)
    # persist theme back to query params
    st.session_state["theme"] = theme
    st.query_params = {"theme": theme}

    # apply basic CSS theme
    if theme == "Dark":
        st.markdown("""<style>.stApp{background:linear-gradient(180deg,#021026,#071026);color:#e6eef8}</style>""", unsafe_allow_html=True)
    else:
        st.markdown("""<style>.stApp{background:linear-gradient(180deg,#ffffff,#eef2ff);color:#0b1220}</style>""", unsafe_allow_html=True)

    st.title(" Cyber Threat Hunting & Attack Mapping (Final)")
    st.caption("Designed & Developed by Randy Singh — KNet Consulting Group")

    if "df" not in st.session_state:
        st.session_state["df"] = None

    with st.sidebar:
        st.header("Controls & Data")
        api_key = st.text_input("OpenAI API Key (optional)", type="password")
        n_samples = st.slider("Sample records (max 200)", min_value=10, max_value=200, value=100, step=10)
        if st.button("Generate Sample Data"):
            st.session_state["df"] = generate_sample_data(n=n_samples)
            st.success(f"Generated {n_samples} synthetic events.")

        st.markdown("---")
        st.markdown("**Upload CSV / JSON / Excel**")
        uploaded = st.file_uploader("Upload file", type=["csv", "json", "xlsx"])
        if uploaded is not None:
            try:
                if uploaded.name.endswith(".csv"):
                    df_up = pd.read_csv(uploaded)
                elif uploaded.name.endswith(".json"):
                    try:
                        df_up = pd.read_json(uploaded)
                    except Exception:
                        uploaded.seek(0)
                        df_up = pd.read_json(uploaded, lines=True)
                else:
                    df_up = pd.read_excel(uploaded)
                st.session_state["df"] = df_up
                st.success(f"Loaded {uploaded.name} ({len(df_up)} rows).")
            except Exception as e:
                st.error(f"Upload failed: {e}")

        st.markdown("---")
        if st.button("Load Sample EDR Dataset"):
            edf = generate_sample_data(150)
            edf["process_name"] = np.random.choice(["explorer.exe","powershell.exe","svchost.exe","ransomware.exe","cmd.exe"], size=len(edf))
            edf["cmdline"] = ["-exec" if a=="cmd_exec" else "" for a in edf["action"]]
            edf["file_size"] = np.random.randint(100, 50000, size=len(edf))
            st.session_state["df"] = edf
            st.success("Loaded synthetic EDR dataset (150 rows).")

        st.markdown("---")
        st.subheader("Insert Targeted Anomaly (demo)")
        anomaly_choice = st.selectbox("Anomaly type", ["credential_stuffing", "brute_force_user", "port_scan", "data_exfiltration", "mixed"])
        anomaly_count = st.slider("Anomaly size (events)", 10, 500, 80, 10)
        if st.button("Insert Targeted Anomaly"):
            st.session_state["df"] = generate_targeted_anomaly(st.session_state.get("df"), anomaly_type=anomaly_choice, n=anomaly_count)
            st.success(f"Inserted {anomaly_count} events of '{anomaly_choice}'.")

        st.markdown("---")
        st.subheader("Detection thresholds (tunable)")
        port_scan_hosts = st.slider("Port-scan: unique hosts", 2, 10, 4)
        port_scan_window = st.slider("Port-scan window (mins)", 1, 60, 10)
        brute_force_failures = st.slider("Brute-force: failures", 3, 30, 8)
        brute_force_window = st.slider("Brute-force window (mins)", 5, 120, 30)
        suspicious_cmds = st.slider("Cmd_exec threshold", 1, 20, 5)
        data_exfil_files = st.slider("Data-exfil: file accesses", 2, 50, 6)
        data_exfil_window = st.slider("Data-exfil window (hours)", 1, 24, 4)

        st.markdown("---")
        if st.button("Clear Data"):
            st.session_state["df"] = None
            st.info("Data cleared.")

    # main panel
    df = st.session_state.get("df")
    if df is None:
        st.info("No data yet. Use the sidebar to generate, upload, or load demo data.")
        return

    # normalize timestamps & required columns
    try:
        df = _ensure_timestamp(df)
    except Exception as e:
        st.warning(f"Timestamp normalization fallback: {e}")
        df["timestamp"] = pd.Timestamp.utcnow()

    for col in ["src_ip","dest_host","user","action","result"]:
        if col not in df.columns:
            if col == "src_ip":
                df[col] = np.random.choice([f"10.0.1.{i}" for i in range(1,50)], size=len(df))
            elif col == "dest_host":
                df[col] = np.random.choice([f"host{i}.corp.local" for i in range(1,6)], size=len(df))
            elif col == "user":
                df[col] = np.random.choice([f"user{i}" for i in range(1,11)], size=len(df))
            elif col == "action":
                df[col] = np.random.choice(["login","file_access","cmd_exec"], size=len(df))
            else:
                df[col] = np.random.choice(["success","failure"], size=len(df))

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Overview metrics
    st.subheader("Overview")
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Events", f"{len(df)}")
    c2.metric("Unique IPs", f"{df['src_ip'].nunique()}")
    c3.metric("Unique Users", f"{df['user'].nunique()}")
    c4.metric("Unique Hosts", f"{df['dest_host'].nunique()}")

    # Raw preview
    st.subheader("Raw Events (preview)")
    st.dataframe(df.head(100))

    # Charts & PNG downloads
    st.subheader("Charts & Visuals")
    c1,c2,c3 = st.columns(3)
    action_counts = df["action"].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(action_counts.values, labels=[f"{a} ({c})" for a,c in zip(action_counts.index, action_counts.values)], startangle=90, wedgeprops=dict(edgecolor='w'))
    ax1.axis("equal")
    with c1:
        st.markdown("**Actions**")
        st.pyplot(fig1)
        png1 = io.BytesIO(); fig1.savefig(png1, format="png", bbox_inches="tight"); png1.seek(0)
        st.download_button("Download Actions PNG", png1.getvalue(), "actions.png", mime="image/png")

    result_counts = df["result"].value_counts()
    fig2, ax2 = plt.subplots()
    ax2.pie(result_counts.values, labels=[f"{a} ({c})" for a,c in zip(result_counts.index, result_counts.values)], startangle=90, wedgeprops=dict(edgecolor='w'))
    ax2.axis("equal")
    with c2:
        st.markdown("**Results**")
        st.pyplot(fig2)
        png2 = io.BytesIO(); fig2.savefig(png2, format="png", bbox_inches="tight"); png2.seek(0)
        st.download_button("Download Results PNG", png2.getvalue(), "results.png", mime="image/png")

    top_users = df["user"].value_counts().head(6)
    fig3, ax3 = plt.subplots()
    ax3.barh(top_users.index[::-1], top_users.values[::-1])
    ax3.set_title("Top Users")
    with c3:
        st.markdown("**Top Users**")
        st.pyplot(fig3)
        png3 = io.BytesIO(); fig3.savefig(png3, format="png", bbox_inches="tight"); png3.seek(0)
        st.download_button("Download Top Users PNG", png3.getvalue(), "top_users.png", mime="image/png")

    # Attack graph
    st.subheader("Attack Graph")
    G = build_graph(df)
    visualize_graph(G)

    # Detections & playbooks
    st.subheader("Detections & Playbooks")
    params = {
        "port_scan_hosts": port_scan_hosts,
        "port_scan_window": port_scan_window,
        "brute_force_failures": brute_force_failures,
        "brute_force_window": brute_force_window,
        "suspicious_cmds": suspicious_cmds,
        "data_exfil_files": data_exfil_files,
        "data_exfil_window": data_exfil_window
    }
    detections = aggregate_detections(df, params)
    if not detections:
        st.success("No anomalies detected.")
    else:
        det_col, graph_col = st.columns([1,1.3])
        with det_col:
            for i, det in enumerate(detections):
                sev = det.get("severity","info")
                header = f"[{sev.upper()}] {det['text']}"
                with st.expander(header, expanded=False):
                    st.markdown(f"**Type:** `{det.get('type')}`")
                    mitre = MITRE_MAP.get(det.get("type"), [])
                    if mitre:
                        st.markdown("**MITRE ATT&CK Mapping:**")
                        for t, tech in mitre:
                            st.markdown(f"- {t} | {tech}")
                    if st.button(f"Explain ({i})", key=f"exp_{i}"):
                        st.info(explain_detection(det["text"], api_key=api_key))
                    st.markdown("**Recommended Playbook**")
                    for step in PLAYBOOKS.get(det.get("type"), ["Triage and investigate."]):
                        st.write(f"- {step}")
                    pb = f"Playbook for: {det['text']}\nSeverity: {sev}\n\n" + "\n".join([f"- {s}" for s in PLAYBOOKS.get(det.get("type"), ["Triage and investigate."])])
                    st.download_button(f"Download Playbook ({i})", pb.encode("utf-8"), file_name=f"playbook_{i}.txt", mime="text/plain")
        with graph_col:
            st.markdown("Attack Graph (highlight suspicious nodes)")
            visualize_graph_highlight(G, detections)

    # Exports: CSV, JSON, XLSX
    st.subheader("Export Data")
    try:
        csv_bytes = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", csv_bytes, "events.csv", mime="text/csv")
    except Exception as e:
        st.error(f"CSV export failed: {e}")

    try:
        json_bytes = df.to_json(orient="records", date_format="iso").encode("utf-8")
        st.download_button("Download JSON", json_bytes, "events.json", mime="application/json")
    except Exception as e:
        st.error(f"JSON export failed: {e}")

    try:
        to_xlsx = io.BytesIO()
        try:
            with pd.ExcelWriter(to_xlsx, engine="openpyxl") as writer:
                df.to_excel(writer, index=False, sheet_name="events")
        except Exception:
            with pd.ExcelWriter(to_xlsx) as writer:
                df.to_excel(writer, index=False, sheet_name="events")
        to_xlsx.seek(0)
        excel_bytes = to_xlsx.getvalue()
        st.download_button("Download XLSX", excel_bytes, "events.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    except Exception as e:
        st.warning(f"XLSX export not available: {e}. Install openpyxl or xlsxwriter for Excel downloads.")

    st.markdown("---")
    st.caption("KNet Consulting Group — Cyber Threat Hunting Demo • Built by Randy Singh")

if __name__ == "__main__":
    main()
