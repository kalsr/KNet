


# mcp_cyber_siem.py
# THIS CODE IS DESIGNED BY RANDY SINGH FROM KNet CONSULTING GROUP.

import streamlit as st

import pandas as pd

import numpy as np

from datetime import datetime, timedelta

from io import StringIO

from dateutil import parser as dtparser

from sklearn.ensemble import IsolationForest

import json

import uuid

import time



# --- Page config ---

st.set_page_config(page_title="MCP Cyber SIEM Monitor", layout="wide")



# --- Minimal CSS for colored buttons + badges ---

st.markdown(

    """

    <style>

    .action-btn {

      display:inline-block;

      padding:8px 14px;

      margin:6px 4px;

      border-radius:10px;

      color:white;

      font-weight:700;

      cursor:pointer;

      text-align:center;

      box-shadow: 0 2px 6px rgba(0,0,0,0.08);

    }

    .btn-blue { background:#0ea5e9; }   /* primary */

    .btn-green { background:#16a34a; }  /* success */

    .btn-red { background:#ef4444; }    /* danger */

    .btn-yellow { background:#f59e0b; } /* warn */

    .badge { padding:5px 8px; border-radius:8px; color:#fff; font-weight:700; }

    .badge-high { background:#ef4444; }

    .badge-med { background:#f59e0b; color:#111; }

    .badge-low { background:#10b981; }

    .monospace { font-family: monospace; background:#f8fafc; padding:6px; border-radius:6px; }

    </style>

    """,

    unsafe_allow_html=True,

)



# ------------------------

# MCP Simulation (Tool Registry + Auditable Calls)

# ------------------------

class MCPToolCallLog:

    def __init__(self):

        self.records = []



    def add(self, tool_name, input_payload, output_payload):

        rec = {

            "id": str(uuid.uuid4()),

            "timestamp": datetime.utcnow().isoformat(),

            "tool": tool_name,

            "input": input_payload,

            "output": output_payload

        }

        self.records.append(rec)



    def as_df(self):

        if not self.records:

            return pd.DataFrame(columns=["id","timestamp","tool","input","output"])

        return pd.DataFrame(self.records)



# Global call log in session

if 'mcp_call_log' not in st.session_state:

    st.session_state['mcp_call_log'] = MCPToolCallLog()



# Decorator to register MCP tools (simulated)

MCP_TOOL_REGISTRY = {}



def mcp_tool(name):

    def decorator(fn):

        MCP_TOOL_REGISTRY[name] = fn

        return fn

    return decorator



def call_mcp_tool(name, input_payload, simulate_delay=0.05):

    """

    Simulate an MCP tool invocation:

      - validate tool exists

      - run tool with structured input (dictionary)

      - log invocation to st.session_state['mcp_call_log'] for auditability

    """

    if name not in MCP_TOOL_REGISTRY:

        raise RuntimeError(f"MCP tool not found: {name}")

    # Convert input_payload to structured form (simulate validation)

    if not isinstance(input_payload, dict):

        raise ValueError("MCP input must be a dict (structured payload).")

    # Simulate call delay

    time.sleep(simulate_delay)

    # Execute tool

    try:

        output = MCP_TOOL_REGISTRY[name](input_payload)

    except Exception as e:

        output = {"error": str(e)}

    # Log the call

    st.session_state['mcp_call_log'].add(name, input_payload, output)

    return output



# Example MCP tools (these are purposely simple and deterministic)

@mcp_tool("check_ip_reputation")

def tool_check_ip_reputation(payload):

    """

    Example tool: check a list of IPs against a known 'malicious' set.

    Input payload: {"ips": ["1.2.3.4", ...]}

    Output: {"results": {"1.2.3.4": {"reputation":"clean"|"malicious","score":0-100}}}

    """

    ips = payload.get("ips", [])

    # simulated malicious IP set (RFC 5737 test IPs plus others)

    MALICIOUS = {"203.0.113.5", "198.51.100.7", "192.0.2.77"}

    results = {}

    for ip in ips:

        if ip in MALICIOUS:

            results[ip] = {"reputation": "malicious", "score": 95}

        else:

            # score lightly based on last octet to be deterministic

            try:

                last = int(ip.split('.')[-1])

                score = (last % 20)

            except:

                score = 5

            results[ip] = {"reputation": "clean", "score": score}

    return {"results": results}



@mcp_tool("lookup_cve_sim")

def tool_lookup_cve_sim(payload):

    """

    Simulated CVE lookup: input a list of packages and return mock CVE counts.

    payload: {"packages": [{"package":"pkg","version":"1.2.3"}, ...]}

    """

    pkgs = payload.get("packages", [])

    results = {}

    for p in pkgs:

        name = p.get("package", "unknown")

        # simulated vulnerability heuristic:

        if "legacy" in name or "openssl" in name:

            results[name] = {"cve_count": np.random.randint(1,5)}

        else:

            results[name] = {"cve_count": np.random.randint(0,2)}

    return {"results": results}



# ------------------------

# Log generation & parser

# ------------------------

def generate_sample_logs(n=50, start_time=None):

    if start_time is None:

        start_time = datetime.utcnow()

    rng = np.random.default_rng(seed=int(start_time.timestamp()))

    normal_ips = [f"10.0.{i//255}.{i%255}" for i in range(1,40)]

    attacker_ips = ["203.0.113.5", "198.51.100.7", "192.0.2.77"]

    dest_ip = "172.16.0.10"

    rows = []

    for _ in range(n):

        ts = start_time - timedelta(minutes=int(rng.integers(0,120)))

        if rng.random() < 0.9:

            src = rng.choice(normal_ips)

            port = int(rng.choice([80,443,22,3389]))

            status = "SUCCESS_LOGIN" if rng.random() > 0.98 else "INFO"

        else:

            src = rng.choice(attacker_ips)

            if rng.random() < 0.6:

                status = "FAILED_LOGIN"

                port = int(rng.choice([22,23,3389]))

            else:

                status = "INFO"

                port = int(rng.integers(1,2000))

        user = "alice" if rng.random() < 0.3 else ""

        raw = f"{ts.isoformat()} {src} {dest_ip} {port} tcp {status} {user}"

        rows.append({"timestamp": ts.isoformat(), "src_ip": src, "dest_ip": dest_ip,

                     "dest_port": port, "protocol":"tcp", "status":status, "user":user, "raw": raw})

    df = pd.DataFrame(rows).sort_values("timestamp").reset_index(drop=True)

    return df



def parse_generic_line(line):

    line = line.strip()

    if not line:

        return None

    # CSV-style detection

    if ',' in line and '"' not in line:

        parts = [p.strip() for p in line.split(',')]

        if len(parts) >= 6:

            try:

                ts = dtparser.parse(parts[0])

            except:

                return None

            return {

                "timestamp": ts,

                "src_ip": parts[1],

                "dest_ip": parts[2],

                "dest_port": int(parts[3]) if parts[3].isdigit() else -1,

                "protocol": parts[4],

                "status": parts[5],

                "user": parts[6] if len(parts) > 6 else "",

                "raw": line

            }

    # space-separated fallback (simple)

    parts = line.split()

    try:

        ts = dtparser.parse(parts[0])

        remainder = parts[1:]

    except Exception:

        # try first two tokens

        try:

            ts = dtparser.parse(" ".join(parts[:2]))

            remainder = parts[2:]

        except Exception:

            return None

    src=None; dest=None; dport=None; status="INFO"; user=""

    for tok in remainder:

        if "." in tok and src is None:

            src = tok

        elif tok.isdigit() and dport is None:

            dport = int(tok)

        elif tok.upper() in ("FAILED_LOGIN","SUCCESS_LOGIN","INFO","ERROR"):

            status = tok.upper()

    return {"timestamp": ts, "src_ip": src or "unknown", "dest_ip": dest or "unknown",

            "dest_port": int(dport) if dport is not None else -1, "protocol":"tcp",

            "status": status, "user":user, "raw": line}



def parse_logs_text(text):

    lines = text.splitlines()

    records = []

    for ln in lines:

        p = parse_generic_line(ln)

        if p:

            records.append(p)

    if not records:

        return pd.DataFrame()

    df = pd.DataFrame(records)

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    df['dest_port'] = df['dest_port'].fillna(-1).astype(int)

    return df



# ------------------------

# Detection functions

# ------------------------

def flag_blacklist(df, blacklist):

    df = df.copy()

    df['blacklisted'] = df['src_ip'].isin(blacklist)

    return df



def failed_login_spikes(df, window_minutes=5, failed_threshold=5):

    df_failed = df[df['status']=='FAILED_LOGIN'].copy()

    if df_failed.empty:

        return pd.DataFrame(columns=['src_ip','failed_count','failed_flag'])

    df_failed['window'] = df_failed['timestamp'].dt.floor(f'{window_minutes}T')

    agg = df_failed.groupby('src_ip').size().rename('failed_count').reset_index()

    agg['failed_flag'] = agg['failed_count'] >= failed_threshold

    return agg



def detect_port_scan(df, distinct_port_threshold=10, window_minutes=10):

    df = df.copy()

    df['win'] = df['timestamp'].dt.floor(f'{window_minutes}T')

    agg = df.groupby(['src_ip','win'])['dest_port'].nunique().reset_index(name='distinct_ports')

    agg2 = agg.groupby('src_ip')['distinct_ports'].max().reset_index()

    agg2['portscan_flag'] = agg2['distinct_ports'] >= distinct_port_threshold

    return agg2



def detect_high_rate(df, z_thresh=3.0):

    df = df.copy()

    df['minute'] = df['timestamp'].dt.floor('T')

    per_min = df.groupby(['src_ip','minute']).size().reset_index(name='count')

    ip_stats = per_min.groupby('src_ip')['count'].agg(['mean','std','max']).reset_index()

    ip_stats['z'] = (ip_stats['max'] - ip_stats['mean']) / (ip_stats['std'].replace(0,np.nan))

    ip_stats['rate_flag'] = ip_stats['z'] >= z_thresh

    ip_stats = ip_stats.fillna(0)

    return ip_stats



def run_isolation_forest_on_hosts(df, n_estimators=100, contamination=0.02):

    total = df.groupby('src_ip').size().rename('total_requests')

    failed = df[df['status']=='FAILED_LOGIN'].groupby('src_ip').size().rename('failed_count')

    uniq_ports = df.groupby('src_ip')['dest_port'].nunique().rename('unique_ports')

    features = pd.concat([total, failed, uniq_ports], axis=1).fillna(0)

    features['total_requests'] = features['total_requests'].astype(float)

    if len(features) < 2:

        features = features.reset_index()

        features['isof_score'] = 0

        features['isof_flag'] = False

        return features

    model = IsolationForest(n_estimators=n_estimators, contamination=contamination, random_state=42)

    model.fit(features)

    scores = model.decision_function(features)

    preds = model.predict(features)

    features['isof_score'] = scores

    features['isof_flag'] = preds == -1

    return features.reset_index()



# ------------------------

# Streamlit UI layout

# ------------------------

st.title("MCP Cyber SIEM Monitor — Prototype")

st.markdown("A demo SIEM-like app demonstrating structured MCP tool calls, rule-based detection, and basic anomaly detection. Not production-grade.")



# Sidebar controls

st.sidebar.header("Settings")

n_sample = st.sidebar.number_input("Sample events to generate", value=50, min_value=10, max_value=200000, step=10)

failed_thresh = st.sidebar.number_input("Failed login threshold (per host)", value=5, min_value=1)

failed_window = st.sidebar.number_input("Window (minutes) for failed-login aggregation", value=5, min_value=1)

portscan_threshold = st.sidebar.number_input("Distinct port threshold (port-scan)", value=12, min_value=1)

portscan_window = st.sidebar.number_input("Port-scan window (minutes)", value=10, min_value=1)

z_thresh = st.sidebar.slider("Z-score threshold for high-rate detection", min_value=1.0, max_value=8.0, value=3.0)

use_isof = st.sidebar.checkbox("Run IsolationForest anomaly detector (per-host)", value=True)

isof_contam = st.sidebar.slider("IsolationForest contamination", min_value=0.001, max_value=0.1, value=0.02)



st.sidebar.markdown("### Blacklist (comma-separated IPs)")

blacklist_text = st.sidebar.text_area("blacklist", value="203.0.113.5,198.51.100.7", height=80)

blacklist = [ip.strip() for ip in blacklist_text.split(',') if ip.strip()]



# Main two-column layout

left_col, right_col = st.columns([1.4,1])



with left_col:

    st.subheader("Input: Generate or Upload logs")

    col_g1, col_g2, col_g3 = st.columns([1,1,1])

    with col_g1:

        if st.button("Generate sample logs (50)", key="gen", help="Generate sample logs"):

            st.session_state['df_logs'] = generate_sample_logs(n_sample)

            st.success("Sample logs generated.")

    with col_g2:

        if st.button("Refresh sample", key="refresh"):

            st.session_state['df_logs'] = generate_sample_logs(n_sample)

            st.success("Sample logs refreshed.")

    with col_g3:

        uploaded = st.file_uploader("Upload logs (txt/csv)", type=['txt','log','csv'])

        if uploaded is not None:

            try:

                content = uploaded.getvalue().decode('utf-8')

            except:

                content = uploaded.getvalue().decode('latin-1')

            # If CSV, try read directly

            if uploaded.name.lower().endswith('.csv'):

                try:

                    df_parsed = pd.read_csv(StringIO(content))

                    # Try to ensure required columns exist; if not, treat as raw lines

                    if set(['timestamp','src_ip']).issubset(set(df_parsed.columns)):

                        st.session_state['df_logs'] = df_parsed.copy()

                        st.success(f"CSV parsed: {len(df_parsed)} rows.")

                    else:

                        # fallback to parse each line

                        df_parsed = parse_logs_text(content)

                        st.session_state['df_logs'] = df_parsed

                        st.success(f"Parsed {len(df_parsed)} log lines from file.")

                except Exception as e:

                    df_parsed = parse_logs_text(content)

                    st.session_state['df_logs'] = df_parsed

                    st.success(f"Parsed {len(df_parsed)} log lines from file.")

            else:

                df_parsed = parse_logs_text(content)

                st.session_state['df_logs'] = df_parsed

                st.success(f"Parsed {len(df_parsed)} log lines from file.")



    if 'df_logs' not in st.session_state:

        st.session_state['df_logs'] = generate_sample_logs(n_sample)



    df_logs = st.session_state['df_logs'].copy()

    st.markdown("**Log preview (most recent 100 rows)**")

    st.dataframe(df_logs.sort_values('timestamp', ascending=False).head(100))



with right_col:

    st.subheader("MCP Actions & Detections")

    # MCP demonstration controls

    st.markdown("**MCP Tool Demo**")

    st.markdown("Use the MCP tool registry to enrich or check data in a structured way. Calls are logged for auditability.")

    # 1) Check IP reputations for top N source IPs

    top_n = st.number_input("Top source IPs to check (MCP tool)", min_value=1, max_value=50, value=5)

    if st.button("Run MCP: Check IP Reputation", key="mcp_ip"):

        ips = df_logs['src_ip'].value_counts().head(top_n).index.tolist()

        payload = {"ips": ips}

        out = call_mcp_tool("check_ip_reputation", payload)

        st.success("MCP tool `check_ip_reputation` invoked. See MCP call log below.")

        st.json(out)



    # 2) MCP: CVE lookup sim for top packages (if any package field present in logs)

    if st.button("Run MCP: CVE Lookup (simulated)"):

        # prepare sample payload: top unique "user" strings treated as package names (demo)

        packages = [{"package": u or "unknown", "version": "1.0.0"} for u in df_logs['user'].unique()[:10]]

        payload = {"packages": packages}

        out = call_mcp_tool("lookup_cve_sim", payload)

        st.success("MCP tool `lookup_cve_sim` invoked.")

        st.json(out)



    st.markdown("---")

    # Run detection button

    if st.button("Run all detections & aggregate results", key="run_all", help="Run rule-based detections and optional ML anomaly detection"):

        st.session_state['run_now'] = True



    # Show MCP call log

    st.markdown("**MCP Call Log (auditable)**")

    cl_df = st.session_state['mcp_call_log'].as_df()

    if not cl_df.empty:

        # Show last 10 calls

        st.dataframe(cl_df.sort_values('timestamp', ascending=False).head(10))

        # Expand to view details

        if st.checkbox("Show full MCP call log"):

            st.json(cl_df.to_dict(orient='records'))

    else:

        st.info("No MCP tool calls yet. Use the MCP buttons above.")



# Run detections if requested or default

if st.session_state.get('run_now', False) or st.button("Run detections now (quick)", key="run_now_quick"):

    df = df_logs.copy()

    # Ensure timestamp dtype

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Blacklist

    df = flag_blacklist(df, blacklist)

    # Aggregations

    failed_agg = failed_login_spikes(df, window_minutes=int(failed_window), failed_threshold=int(failed_thresh))

    portscan_agg = detect_port_scan(df, distinct_port_threshold=int(portscan_threshold), window_minutes=int(portscan_window))

    highrate = detect_high_rate(df, z_thresh=float(z_thresh))

    if use_isof:

        isof = run_isolation_forest_on_hosts(df, contamination=float(isof_contam))

    else:

        isof = None



    # Compose source summary

    src_table = pd.DataFrame({"src_ip": df['src_ip'].unique()})

    src_table = src_table.merge(failed_agg[['src_ip','failed_count','failed_flag']], on='src_ip', how='left')

    src_table = src_table.merge(portscan_agg[['src_ip','distinct_ports','portscan_flag']], on='src_ip', how='left')

    src_table = src_table.merge(highrate[['src_ip','mean','std','max','z','rate_flag']], on='src_ip', how='left')

    if isof is not None:

        src_table = src_table.merge(isof[['src_ip','total_requests','failed_count','unique_ports','isof_score','isof_flag']], on='src_ip', how='left')

    src_table['blacklisted'] = src_table['src_ip'].isin(blacklist)

    src_table = src_table.fillna(0)

    src_table['any_flag'] = src_table[['blacklisted','failed_flag','portscan_flag','rate_flag','isof_flag']].any(axis=1)



    st.session_state['detection_df'] = df

    st.session_state['src_table'] = src_table

    st.session_state['flagged_raw'] = df[df['src_ip'].isin(src_table[src_table['any_flag']].src_ip)]

    st.session_state['run_now'] = False

    st.success("Detections complete. Scroll down to view results.")



# If detection results exist, show summary, charts, tables, downloads

if 'src_table' in st.session_state:

    det_df = st.session_state['detection_df']

    src_table = st.session_state['src_table']

    flagged_raw = st.session_state['flagged_raw']



    st.markdown("---")

    st.subheader("Detection Summary")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric("Total events", len(det_df))

    with c2:

        st.metric("Unique source IPs", det_df['src_ip'].nunique())

    with c3:

        st.metric("Flagged hosts", int(src_table['any_flag'].sum()))



    # Top sources chart

    st.markdown("**Top source IPs by event count**")

    top_src = det_df['src_ip'].value_counts().head(20).reset_index()

    top_src.columns = ['src_ip','count']

    st.bar_chart(top_src.set_index('src_ip'))



    # Time series

    st.markdown("**Events per minute (time series)**")

    ts = det_df.set_index('timestamp').resample('1T').size()

    st.line_chart(ts)



    # Show flagged hosts table

    st.markdown("**Flagged hosts (aggregated)**")

    display_hosts = src_table.sort_values('any_flag', ascending=False).reset_index(drop=True)

    st.dataframe(display_hosts.head(200))



    # Show example flagged raw events

    st.markdown("**Flagged raw events (examples)**")

    st.dataframe(flagged_raw.sort_values('timestamp', ascending=False).head(200))



    # Enable MCP enrichment of flagged hosts: call check_ip_reputation automatically

    if st.button("MCP Enrich flagged IPs (auto)"):

        ips_to_check = display_hosts[display_hosts['any_flag']==True]['src_ip'].tolist()

        if ips_to_check:

            out = call_mcp_tool("check_ip_reputation", {"ips": ips_to_check})

            st.success("Enrichment complete. See MCP call log for details.")

            st.json(out)

        else:

            st.info("No flagged IPs to enrich.")



    # Downloads

    st.markdown("**Download results**")

    csv_hosts = display_hosts.to_csv(index=False).encode('utf-8')

    csv_raw = det_df.to_csv(index=False).encode('utf-8')

    json_hosts = display_hosts.to_json(orient='records', date_format='iso').encode('utf-8')

    json_raw = det_df.to_json(orient='records', date_format='iso').encode('utf-8')



    st.download_button("Download flagged hosts (CSV)", csv_hosts, file_name="flagged_hosts.csv", mime="text/csv")

    st.download_button("Download all events (CSV)", csv_raw, file_name="events_all.csv", mime="text/csv")

    st.download_button("Download flagged hosts (JSON)", json_hosts, file_name="flagged_hosts.json", mime="application/json")

    st.download_button("Download all events (JSON)", json_raw, file_name="events_all.json", mime="application/json")



    # Show MCP call log (expanded)

    st.markdown("---")

    st.subheader("MCP Call Log (full)")

    st.dataframe(st.session_state['mcp_call_log'].as_df().sort_values('timestamp', ascending=False))



    st.markdown("**MCP Audit (JSON)**")

    st.json(st.session_state['mcp_call_log'].as_df().to_dict(orient='records'))



else:

    st.info("No detection results yet. Click 'Run all detections & aggregate results' or 'Run detections now (quick)'.")





