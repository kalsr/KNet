# mcp_cyber_monitor.py
# THIS MCP USE CASE HAS BEEN DESIGNED BY RANDY SINGH FROM KNet CONSULTING GROUP

import streamlit as st

import pandas as pd

import numpy as np

from datetime import datetime, timedelta

from io import StringIO

from dateutil import parser as dtparser

from sklearn.ensemble import IsolationForest



st.set_page_config(page_title="MCP Cyber Monitor", layout="wide")



# -------------------------

# Utility & parser functions

# -------------------------

def parse_generic_line(line):

    """

    Tries to parse a text line into fields:

    Expecting at least: timestamp src_ip dest_ip dest_port protocol status user message

    Accepts CSV-like or space-separated formats. If fails, returns None.

    """

    line = line.strip()

    if not line:

        return None

    # Try CSV

    if ',' in line and '"' not in line:

        parts = [p.strip() for p in line.split(',')]

        # If simple structured

        if len(parts) >= 6:

            try:

                ts = dtparser.parse(parts[0])

            except Exception:

                return None

            rec = {

                "timestamp": ts,

                "src_ip": parts[1],

                "dest_ip": parts[2],

                "dest_port": int(parts[3]) if parts[3].isdigit() else None,

                "protocol": parts[4],

                "status": parts[5],

                "user": parts[6] if len(parts) >= 7 else "",

                "raw": line

            }

            return rec

    # Try splitted by spaces (like syslog)

    parts = line.split()

    # heuristics: timestamp at start

    try:

        ts = dtparser.parse(" ".join(parts[:2]))

        remainder = parts[2:]

    except Exception:

        # fallback: try first token only

        try:

            ts = dtparser.parse(parts[0])

            remainder = parts[1:]

        except Exception:

            return None

    # remainder heuristic: look for src_ip (token containing .)

    src_ip = None

    dest_ip = None

    dest_port = None

    protocol = None

    status = None

    user = ""

    for tok in remainder:

        if "." in tok and src_ip is None:

            src_ip = tok.strip(',')

        elif "." in tok and dest_ip is None:

            dest_ip = tok.strip(',')

    # find port token if any numeric token

    for tok in remainder:

        if tok.isdigit() and dest_port is None:

            dest_port = int(tok)

    # status: look for keywords

    lowers = [t.lower() for t in remainder]

    if "failed" in lowers or "failed_login" in lowers or "invalid" in lowers:

        status = "FAILED_LOGIN"

    elif "accepted" in lowers or "success" in lowers:

        status = "SUCCESS_LOGIN"

    else:

        status = "INFO"

    rec = {

        "timestamp": ts,

        "src_ip": src_ip or "unknown",

        "dest_ip": dest_ip or "unknown",

        "dest_port": dest_port,

        "protocol": protocol or "tcp",

        "status": status,

        "user": user,

        "raw": line

    }

    return rec





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

    # normalize timestamp

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # fill nulls

    df['dest_port'] = df['dest_port'].fillna(-1).astype(int)

    return df





# -------------------------

# Sample log generator

# -------------------------

def generate_sample_logs(n_events=1000, start_time=None):

    """

    Generates a sample DataFrame with columns:

    timestamp, src_ip, dest_ip, dest_port, protocol, status, user, raw

    """

    import random, ipaddress

    if start_time is None:

        start_time = datetime.utcnow() - timedelta(hours=1)

    times = [start_time + timedelta(seconds=int(i)) for i in np.random.randint(0, 3600, size=n_events)]

    # make some normal clients and some suspicious ones

    normal_ips = [f"10.0.{i//255}.{i%255}" for i in range(1,50)]

    attacker_ips = ["203.0.113.5", "198.51.100.7", "192.0.2.77"]  # example attacker IPs

    dest_ip = "172.16.0.10"

    rows = []

    for t in times:

        if np.random.rand() < 0.95:

            src = np.random.choice(normal_ips)

            port = np.random.choice([80, 443, 22, 3389])

            status = "SUCCESS_LOGIN" if np.random.rand() > 0.98 else "INFO"

        else:

            # suspicious: failed login or port scan type

            src = np.random.choice(attacker_ips)

            if np.random.rand() < 0.6:

                status = "FAILED_LOGIN"

                port = np.random.choice([22, 23, 3389])

            else:

                # port scan: many distinct ports

                status = "INFO"

                port = np.random.randint(1, 2000)

        user = "alice" if np.random.rand() < 0.3 else ""

        raw = f"{t.isoformat()} {src} {dest_ip} {port} tcp {status} {user}"

        rows.append({

            "timestamp": t, "src_ip": src, "dest_ip": dest_ip, "dest_port": port,

            "protocol": "tcp", "status": status, "user": user, "raw": raw

        })

    df = pd.DataFrame(rows)

    df = df.sort_values("timestamp").reset_index(drop=True)

    return df





# -------------------------

# Detection functions

# -------------------------

def flag_blacklist(df, blacklist):

    df = df.copy()

    df['blacklisted'] = df['src_ip'].isin(blacklist)

    return df



def failed_login_spikes(df, window_minutes=5, failed_threshold=5):

    """

    Flag src_ip if number of FAILED_LOGIN events within window_minutes >= failed_threshold.

    Returns DataFrame with aggregated counts and a flag per src_ip.

    """

    df = df.copy()

    df = df.sort_values('timestamp')

    df_failed = df[df['status'] == 'FAILED_LOGIN']

    if df_failed.empty:

        return pd.DataFrame(columns=['src_ip','failed_count','failed_flag'])

    df_failed['minute'] = df_failed['timestamp'].dt.floor(f'{window_minutes}T')

    agg = df_failed.groupby('src_ip').size().rename('failed_count').reset_index()

    agg['failed_flag'] = agg['failed_count'] >= failed_threshold

    return agg



def detect_port_scan(df, distinct_port_threshold=10, window_minutes=10):

    """

    Detects sources that contacted >= distinct_port_threshold distinct dest_ports within the time window.

    Returns aggregated table per src_ip with distinct port counts and flag.

    """

    df = df.copy()

    df['time_window'] = df['timestamp'].dt.floor(f'{window_minutes}T')

    agg = df.groupby(['src_ip','time_window'])['dest_port'].nunique().reset_index(name='distinct_ports')

    agg2 = agg.groupby('src_ip')['distinct_ports'].max().reset_index()

    agg2['portscan_flag'] = agg2['distinct_ports'] >= distinct_port_threshold

    return agg2



def detect_high_rate(df, z_thresh=3.0):

    """

    Detects IPs with requests/minute much higher than average using z-score.

    """

    df = df.copy()

    df['minute'] = df['timestamp'].dt.floor('T')

    per_min = df.groupby(['src_ip','minute']).size().reset_index(name='count')

    ip_stats = per_min.groupby('src_ip')['count'].agg(['mean','std','max']).reset_index()

    ip_stats['z'] = (ip_stats['max'] - ip_stats['mean']) / (ip_stats['std'].replace(0, np.nan))

    ip_stats['rate_flag'] = ip_stats['z'] >= z_thresh

    ip_stats = ip_stats.fillna(0)

    return ip_stats



def run_isolation_forest_on_hosts(df, n_estimators=100, contamination=0.01):

    """

    Build feature vector per host and run IsolationForest to score anomalies.

    Features: total_requests, failed_count, unique_dest_ports

    """

    df = df.copy()

    total = df.groupby('src_ip').size().rename('total_requests')

    failed = df[df['status']=='FAILED_LOGIN'].groupby('src_ip').size().rename('failed_count')

    uniq_ports = df.groupby('src_ip')['dest_port'].nunique().rename('unique_ports')

    features = pd.concat([total, failed, uniq_ports], axis=1).fillna(0)

    # small numeric scaling

    features['total_requests'] = features['total_requests'].astype(float)

    model = IsolationForest(n_estimators=n_estimators, contamination=contamination, random_state=42)

    if len(features) < 2:

        features['isoforest_score'] = 0

        features['isoforest_flag'] = False

        return features.reset_index()

    model.fit(features)

    scores = model.decision_function(features)

    preds = model.predict(features)  # -1 anomaly, 1 normal

    features['isoforest_score'] = scores

    features['isoforest_flag'] = preds == -1

    return features.reset_index()





# -------------------------

# Streamlit UI

# -------------------------

st.title("MCP Cyber Threat Monitor — Prototype")

st.markdown("""

Prototype app demonstrating log ingestion, parsing, simple heuristics and an optional ML anomaly detector.

Use this to prototype use-cases for security monitoring and to feed structured events into an MCP workflow.

""")



# Sidebar controls

st.sidebar.header("Options & Thresholds")

n_sample = st.sidebar.number_input("Sample events to generate", value=1000, min_value=10, max_value=200000, step=10)

failed_thresh = st.sidebar.number_input("Failed login threshold (per host)", value=5, min_value=1)

failed_window = st.sidebar.number_input("Window (minutes) for failed-login aggregation", value=5, min_value=1)

portscan_threshold = st.sidebar.number_input("Distinct port threshold (port-scan)", value=10, min_value=1)

portscan_window = st.sidebar.number_input("Port-scan window (minutes)", value=10, min_value=1)

z_thresh = st.sidebar.slider("Z-score threshold for high rate detection", min_value=1.0, max_value=10.0, value=3.0)

use_isof = st.sidebar.checkbox("Run IsolationForest anomaly detection (may be slower)", value=True)

isof_contam = st.sidebar.slider("IsolationForest contamination", min_value=0.001, max_value=0.1, value=0.01)



# Blacklist input

st.sidebar.markdown("### Blacklist (comma-separated IPs)")

blacklist_text = st.sidebar.text_area("blacklist", value="203.0.113.5,198.51.100.7", height=80)

blacklist = [ip.strip() for ip in blacklist_text.split(',') if ip.strip()]



col1, col2 = st.columns([1,2])



with col1:

    st.subheader("Input: Generate or Upload logs")

    if st.button("Generate sample logs"):

        df_logs = generate_sample_logs(n_events=n_sample)

        st.success(f"Generated {len(df_logs)} sample events.")

    else:

        df_logs = None



    uploaded = st.file_uploader("Upload log file (text) — one event per line (CSV or space-separated).", type=['log','txt','csv'])

    if uploaded is not None:

        try:

            raw_text = StringIO(uploaded.getvalue().decode('utf-8')).read()

        except Exception:

            raw_text = StringIO(uploaded.getvalue().decode('latin-1')).read()

        parsed = parse_logs_text(raw_text)

        if parsed.empty:

            st.warning("No parseable lines found in uploaded file.")

        else:

            df_logs = parsed

            st.success(f"Parsed {len(df_logs)} events from upload.")



    if df_logs is None:

        st.info("No log dataset yet. Click 'Generate sample logs' or upload a file.")

    else:

        st.write("Preview of logs:")

        st.dataframe(df_logs.head(25))



with col2:

    st.subheader("Processing & Detection")

    if df_logs is not None:

        # ensure timestamp dtype

        df_logs['timestamp'] = pd.to_datetime(df_logs['timestamp'])

        # 1) Blacklist

        df1 = flag_blacklist(df_logs, blacklist)

        # 2) Failed login spikes

        failed_agg = failed_login_spikes(df_logs, window_minutes=int(failed_window), failed_threshold=int(failed_thresh))

        # 3) Port scan detection

        portscan_agg = detect_port_scan(df_logs, distinct_port_threshold=int(portscan_threshold), window_minutes=int(portscan_window))

        # 4) High rate detection

        highrate = detect_high_rate(df_logs, z_thresh=float(z_thresh))

        # 5) Isolation Forest

        if use_isof:

            isof = run_isolation_forest_on_hosts(df_logs, contamination=float(isof_contam))

        else:

            isof = None



        st.markdown("### Summary")

        total_events = len(df_logs)

        unique_src = df_logs['src_ip'].nunique()

        st.metric("Total events", total_events)

        st.metric("Unique source IPs", unique_src)



        # Compose flags table per src_ip

        src_table = pd.DataFrame({"src_ip": df_logs['src_ip'].unique()})

        src_table = src_table.merge(failed_agg[['src_ip','failed_count','failed_flag']], on='src_ip', how='left')

        src_table = src_table.merge(portscan_agg[['src_ip','distinct_ports','portscan_flag']], on='src_ip', how='left')

        src_table = src_table.merge(highrate[['src_ip','mean','std','max','z','rate_flag']], on='src_ip', how='left')

        if isof is not None:

            src_table = src_table.merge(isof[['src_ip','total_requests','failed_count','unique_ports','isoforest_score','isoforest_flag']], on='src_ip', how='left')

        src_table['blacklisted'] = src_table['src_ip'].isin(blacklist)

        src_table = src_table.fillna(0)



        # calculate overall flagged hosts

        src_table['any_flag'] = src_table[['blacklisted','failed_flag','portscan_flag','rate_flag','isoforest_flag']].any(axis=1)

        flagged_hosts = src_table[src_table['any_flag'] == True]



        st.markdown("### Flagged Hosts")

        st.write(f"Hosts flagged: {len(flagged_hosts)}")

        st.dataframe(flagged_hosts.sort_values(by=['any_flag'], ascending=False).reset_index(drop=True).head(50))



        # show time series of events

        st.markdown("### Time series: events per minute")

        ts = df_logs.set_index('timestamp').resample('1T').size()

        st.line_chart(ts)



        # top offending IPs

        st.markdown("### Top source IPs (by event count)")

        top_src = df_logs['src_ip'].value_counts().reset_index()

        top_src.columns = ['src_ip','count']

        st.bar_chart(top_src.set_index('src_ip').head(20))



        # show raw flagged events (a subset)

        st.markdown("### Flagged raw events (examples)")

        # flagged raw events are events whose src_ip is flagged or blacklisted

        flagged_raw = df_logs[df_logs['src_ip'].isin(flagged_hosts['src_ip'])]

        st.dataframe(flagged_raw.sort_values('timestamp', ascending=False).head(200))



        # Downloads: allow saving flagged hosts and flagged raw events

        st.markdown("### Save results")

        # prepare CSV & JSON bytes

        csv_flagged_hosts = flagged_hosts.to_csv(index=False).encode('utf-8')

        json_flagged_hosts = flagged_hosts.to_json(orient='records', date_format='iso').encode('utf-8')

        csv_flagged_raw = flagged_raw.to_csv(index=False).encode('utf-8')

        json_flagged_raw = flagged_raw.to_json(orient='records', date_format='iso').encode('utf-8')



        st.download_button("Download flagged hosts (CSV)", csv_flagged_hosts, file_name="flagged_hosts.csv", mime="text/csv")

        st.download_button("Download flagged hosts (JSON)", json_flagged_hosts, file_name="flagged_hosts.json", mime="application/json")

        st.download_button("Download flagged raw events (CSV)", csv_flagged_raw, file_name="flagged_raw_events.csv", mime="text/csv")

        st.download_button("Download flagged raw events (JSON)", json_flagged_raw, file_name="flagged_raw_events.json", mime="application/json")



        st.markdown("---")

        st.subheader("Notes & next steps")

        st.markdown("""

        - This is a **prototype**. Replace/extend the parser to match your real log format (Syslog, Windows event logs, Cloudwatch, etc.).  

        - Tune thresholds and blacklists to reduce false positives.  

        - To run continuously on live logs, add a file-watcher (e.g. `watchdog`) or stream logs to this app's backend.  

        - For production: centralize logs (Filebeat/Logstash), store in a database, and use proper enrichment (geoip, ASN, user directories).

        - To integrate with MCP: convert the `flagged_raw` / `flagged_hosts` rows into the model context payload expected by your MCP implementation and call your models/pipelines.

        """)



    else:

        st.info("No logs to process; generate or upload above.")



st.markdown("---")

st.caption("Prototype created for MCP use-case prototyping. Not intended as production SIEM. Treat real logs with care.")
