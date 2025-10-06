
import streamlit as st
import pandas as pd
import sqlite3
import json
import random
import io
import os
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Config
BUNDLED_CSV = os.path.join(os.path.dirname(__file__), "cyber_threats.csv")
DEFAULT_DB_NAME = "cyber_threats_uploaded.db"

st.set_page_config(page_title="Cyber Threat Detector v2 - Randy Singh | KNet Consulting", layout="wide")

# ----- CSS Styling for colored buttons and layout -----
st.markdown("""
<style>
.big-button { display:inline-block; padding:10px 18px; font-size:15px; border-radius:8px; text-align:center; cursor:pointer; margin:4px; color:white; font-weight:700;}
.green {background-color:#2b9348;}
.blue {background-color:#1971c2;}
.orange {background-color:#f08a24;}
.red {background-color:#d00000;}
.gray {background-color:#6c757d;}
.card {padding:12px; border-radius:8px; border:1px solid #eee; background-color:#fff; margin-bottom:12px;}
.header {font-size:18px; font-weight:800;}
.small {font-size:13px; color:#666;}
</style>
""", unsafe_allow_html=True)

# ----- Header -----
st.title("🔐 Cyber Threat Detector — v2")
st.markdown("**Developed by Randy Singh — KNet Consulting Group**")
st.markdown("A demo app: rule-based detection + simple Agentic reasoning + dataset management + visual analytics.")

# ----- Sidebar Controls -----
with st.sidebar:
    st.header("Data Controls")
    st.markdown("<div class='small'>Upload a dataset (CSV / JSON / Excel) or use bundled DB / generate samples.</div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload threat data (CSV, JSON, Excel)", type=["csv","json","xls","xlsx"])
    st.markdown("<div class='big-button green'>Upload Data File</div>", unsafe_allow_html=True)

    st.write("---")
    st.write("Or load / generate data")

    if st.button("Load Bundled DB", key="load_db_v2"):
        st.session_state['loaded_source'] = 'bundled'
    st.markdown("<div class='big-button blue'>Load Bundled DB</div>", unsafe_allow_html=True)

    gen_count = st.slider("Generate sample records", 20, 100, 25, step=5)
    if st.button("Generate Sample Records", key="gen_v2"):
        st.session_state['generated'] = gen_count
        st.session_state['loaded_source'] = 'generated'
    st.markdown("<div class='big-button orange'>Generate Sample Records</div>", unsafe_allow_html=True)

    st.write("---")
    if st.button("Reset / Clear All", key="reset_v2"):
        for k in list(st.session_state.keys()):
            st.session_state.pop(k, None)
        st.experimental_rerun()
    st.markdown("<div class='big-button red'>Reset / Clear All</div>", unsafe_allow_html=True)

    st.write("---")
    st.header("Save analysis")
    save_csv = st.checkbox("Save results as CSV", value=True)
    save_json = st.checkbox("Save results as JSON", value=False)
    save_excel = st.checkbox("Save results as Excel", value=False)
    save_db = st.checkbox("Save to SQLite DB", value=False)

    st.write("---")
    st.header("Agentic-AI")
    use_agent = st.checkbox("Enable Agentic Reasoning Module", value=True)
    st.write("Agentic module provides an explainable trace of reasoning steps.")

# ----- Helper functions -----
@st.cache_data
def load_bundled_csv():
    if os.path.exists(BUNDLED_CSV):
        return pd.read_csv(BUNDLED_CSV)
    else:
        # if bundled CSV missing, create a small placeholder
        df = pd.DataFrame([{"id":1,"timestamp":datetime.now().isoformat(sep=' '),"source_ip":"192.168.0.1",
                            "dest_ip":"10.0.0.5","src_port":12345,"dest_port":80,"protocol":"HTTP","bytes":250,"packets":2,
                            "alert_type":"Port Scan","severity":"Low","description":"Placeholder record","indicators":"[]",
                            "tactic":"TA0007","technique":"T1595","detected_by":"IDS","confidence":0.4,"payload_signature":"",
                            "file_hash":"","url":"","username":"","outcome":"blocked","remediation":"Block IP","tags":"scan"}])
        return df

def generate_samples(n):
    df = load_bundled_csv().sample(n=n, replace=True, random_state=random.randint(1,10000)).reset_index(drop=True)
    now = datetime.now()
    df['timestamp'] = [(now - pd.to_timedelta(random.randint(0,60*24*14),'m')).isoformat(sep=' ') for _ in range(len(df))]
    df['id'] = range(1, len(df)+1)
    return df

def detect_threats(df_row):
    facts, conclusions, mitigations = [], [], []
    try:
        confidence = float(df_row.get('confidence', 0.5) or 0.5)
    except:
        confidence = 0.5
    atype = str(df_row.get('alert_type','Unknown')).lower()
    payload = str(df_row.get('payload_signature','')).lower()
    bytes_count = int(df_row.get('bytes',0) or 0)
    tags = str(df_row.get('tags',''))

    facts.append(f"Observed alert_type={atype}, bytes={bytes_count}, payload='{payload}'")

    if "sql" in atype or "union select" in payload:
        conclusions.append("SQL Injection attempt detected against a database-driven endpoint.")
        mitigations.append("Use parameterized queries, input validation, and WAF rules for SQLi patterns.")
        confidence = max(confidence, 0.6)
    if "xss" in atype or "<script" in payload:
        conclusions.append("Cross-Site Scripting (XSS) attempt detected—script content in request parameters.")
        mitigations.append("Sanitize and encode output; implement Content Security Policy (CSP).")
        confidence = max(confidence,0.55)
    if "brute" in atype or "failed_logins" in str(df_row.get('indicators','')):
        conclusions.append("Brute-force login activity detected (many failed attempts).")
        mitigations.append("Rate-limit logins, enable account lockout policies, enforce MFA.")
        confidence = max(confidence,0.5)
    if "phish" in atype or str(df_row.get('url','')).startswith("http://"):
        conclusions.append("Phishing link detected—malicious URL present in email or message.")
        mitigations.append("Block the URL at gateway, remove phishing emails, and enforce DMARC/DKIM/SPF.")
        confidence = max(confidence,0.6)
    if "malware" in atype or df_row.get('file_hash','') != "":
        conclusions.append("Malware suspected (suspicious payload or known file hash).")
        mitigations.append("Isolate host, run AV/EDR scan and remediation, update signatures and block hashes.")
        confidence = max(confidence,0.7)
    if "port scan" in atype or "many_ports" in str(df_row.get('indicators','')):
        conclusions.append("Port scan detected—reconnaissance activity.")
        mitigations.append("Block noisy source IPs, tighten firewall rules, increase sensor coverage.")
        confidence = max(confidence,0.4)
    if bytes_count>500000 and ("ddos" in atype or "many_connections" in str(df_row.get('indicators','')) or "ddos" in tags):
        conclusions.append("Traffic profile indicates likely DDoS (very high bytes/connections).")
        mitigations.append("Engage DDoS mitigation, rate-limit, scale resources or blackhole attack if needed.")
        confidence = max(confidence,0.75)
    if "exfil" in atype or "/download" in payload or "exfil" in tags:
        conclusions.append("Potential data exfiltration activity (suspicious large uploads/downloads).")
        mitigations.append("Block destination, inspect traffic, revoke or rotate compromised credentials.")
        confidence = max(confidence,0.65)

    if len(conclusions) == 0:
        conclusions.append("No high-fidelity rule matched. Recommend deeper inspection (sandbox, PCAP capture).")
        mitigations.append("Collect PCAPs, perform endpoint triage, increase logging and retention.")
        confidence = min(confidence,0.5)

    return {"facts":facts,"conclusions":conclusions,"mitigations":mitigations,"confidence":round(float(confidence),2)}

# Simple Agentic reasoning module
class SimpleAgent:
    def __init__(self, record):
        self.record = record
        self.log = []

    def observe(self):
        self.log.append("OBSERVE: Collected raw fields from record for analysis.")
        return self.record

    def hypothesize(self):
        atype = str(self.record.get('alert_type','')).lower()
        hypothesis = "Unknown"
        if "sql" in atype: hypothesis = "SQL Injection"
        elif "xss" in atype: hypothesis = "Cross-Site Scripting"
        elif "brute" in atype: hypothesis = "Brute Force Login"
        elif "phish" in atype: hypothesis = "Phishing"
        elif "malware" in atype or self.record.get('file_hash','') != "": hypothesis = "Malware"
        elif "scan" in atype: hypothesis = "Reconnaissance/Port Scan"
        elif "ddos" in atype: hypothesis = "DDoS"
        self.log.append(f"HYPOTHESIZE: Proposed hypothesis = {hypothesis}")
        return hypothesis

    def test(self):
        result = detect_threats(self.record)
        self.log.append("TEST: Ran rule-based tests against the record.")
        self.log.append(f"TEST RESULT: conclusions={len(result['conclusions'])}, confidence={result['confidence']}")
        return result

    def decide_and_act(self, result):
        decision = "Investigate further"
        actions = []
        conf = result.get('confidence',0)
        if conf >= 0.75:
            decision = "Immediate Remediation Recommended"
            actions = result['mitigations']
        elif 0.5 <= conf < 0.75:
            decision = "Triage and Contain"
            actions = result['mitigations'][:2]
        else:
            decision = "Monitor and Collect More Evidence"
            actions = ["Enable deeper logging","Capture PCAP","Endpoint triage"]
        self.log.append(f"DECIDE: {decision}; ACTIONS: {actions}")
        return {"decision":decision,"actions":actions}

    def run(self):
        self.observe()
        hyp = self.hypothesize()
        result = self.test()
        decision = self.decide_and_act(result)
        return {"log": self.log, "hypothesis": hyp, "result": result, "decision": decision}

# ----- Load / Source Data -----
df = None
source = None

if uploaded_file is not None:
    try:
        if uploaded_file.type == "text/csv" or uploaded_file.name.lower().endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.type in ["application/vnd.ms-excel","application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"] or uploaded_file.name.lower().endswith((".xls",".xlsx")):
            df = pd.read_excel(uploaded_file)
        else:
            # try json
            df = pd.read_json(uploaded_file)
        source = "uploaded"
    except Exception as e:
        st.error(f"Failed to read uploaded file: {e}")
        st.stop()

elif st.session_state.get('loaded_source','') == 'bundled':
    df = load_bundled_csv(); source = "bundled"
elif st.session_state.get('loaded_source','') == 'generated':
    df = generate_samples(st.session_state.get('generated',25)); source = "generated"
else:
    # default to bundled if available
    df = load_bundled_csv(); source = "bundled"

# Ensure index column exists
if 'id' not in df.columns:
    df.insert(0, 'id', range(1, len(df)+1))

st.write(f"Loaded **{len(df)}** records (source: {source})")
st.dataframe(df.head(50))

# ----- CSV-to-DB Upload Integration -----
st.markdown("### 📥 Upload CSV to populate SQLite DB")
if uploaded_file is not None:
    db_name = st.text_input("Enter SQLite DB filename to create:", value=DEFAULT_DB_NAME)
    if st.button("Create SQLite DB from uploaded file"):
        conn = sqlite3.connect(db_name)
        df.to_sql("threats", conn, index=False, if_exists="replace")
        conn.close()
        st.success(f"✅ SQLite DB '{db_name}' created from uploaded CSV!")
        with open(db_name, "rb") as f:
            db_bytes = f.read()
        st.download_button("Download SQLite DB", data=db_bytes, file_name=db_name, mime="application/x-sqlite3")

# ----- Select a record to analyze -----
st.markdown("### 🔍 Select a record to analyze")
idx = st.number_input("Record index (1-based)", min_value=1, max_value=len(df), value=1, step=1)
record = df.iloc[int(idx)-1].to_dict()
st.json(record)

# Run detection on selected record
if st.button("Run Detection on Selected Record"):
    res = detect_threats(record)
    st.success(f"Detection completed — confidence {res['confidence']}")
    st.markdown("**Facts**")
    for f in res['facts']:
        st.write("- " + f)
    st.markdown("**Conclusions**")
    for c in res['conclusions']:
        st.write("- " + c)
    st.markdown("**Recommended Mitigations**")
    for m in res['mitigations']:
        st.write("- " + m)

    # Agentic tracing
    if use_agent:
        agent = SimpleAgent(record)
        agent_out = agent.run()
        st.markdown("#### Agentic Reasoning Trace")
        for line in agent_out['log']:
            st.write("- " + line)
        st.markdown(f"**Agent hypothesis:** {agent_out['hypothesis']}")
        st.markdown("**Agent decision & actions**")
        st.write(agent_out['decision'])

    # Offer to save analysis
    if save_csv or save_json or save_excel or save_db:
        out_df = pd.DataFrame([record])
        out_df['analysis_facts'] = json.dumps(res['facts'])
        out_df['analysis_conclusions'] = json.dumps(res['conclusions'])
        out_df['analysis_mitigations'] = json.dumps(res['mitigations'])
        out_df['analysis_confidence'] = res['confidence']

        if save_csv:
            csv_name = "analysis_result.csv"
            out_df.to_csv(csv_name, index=False)
            st.download_button("Download analysis as CSV", data=open(csv_name,"rb"), file_name=csv_name, mime="text/csv")
        if save_json:
            json_name = "analysis_result.json"
            out_df.to_json(json_name, orient="records", indent=2)
            st.download_button("Download analysis as JSON", data=open(json_name,"rb"), file_name=json_name, mime="application/json")
        if save_excel:
            excel_name = "analysis_result.xlsx"
            out_df.to_excel(excel_name, index=False)
            st.download_button("Download analysis as Excel", data=open(excel_name,"rb"), file_name=excel_name, mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        if save_db:
            db_path = "analysis_results.db"
            conn = sqlite3.connect(db_path)
            out_df.to_sql("analysis", conn, index=False, if_exists="append")
            conn.close()
            with open(db_path,"rb") as f:
                st.download_button("Download analysis DB", data=f.read(), file_name=db_path, mime="application/x-sqlite3")

# ----- Visual Analytics: Pie, Bar, Trend -----
st.markdown("---")
st.markdown("### 📈 Visual Analytics")

# Prepare analytics fields safely
df_analytics = df.copy()
# Ensure timestamp is datetime for trend
if 'timestamp' in df_analytics.columns:
    try:
        df_analytics['ts'] = pd.to_datetime(df_analytics['timestamp'], errors='coerce')
        df_analytics['date'] = df_analytics['ts'].dt.date
    except:
        df_analytics['date'] = pd.NaT
else:
    df_analytics['date'] = pd.NaT

# Pie chart: distribution of alert_type (top 10)
type_counts = df_analytics['alert_type'].fillna("Unknown").value_counts().nlargest(10)
fig1, ax1 = plt.subplots()
ax1.pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.subheader("Threat Type Distribution (Top 10)")
st.pyplot(fig1)

# Bar chart: severity counts
if 'severity' in df_analytics.columns:
    sev_counts = df_analytics['severity'].fillna("Unknown").value_counts()
    fig2, ax2 = plt.subplots()
    ax2.bar(sev_counts.index.astype(str), sev_counts.values)
    ax2.set_xlabel("Severity")
    ax2.set_ylabel("Count")
    ax2.set_title("Threats by Severity")
    st.subheader("Threats by Severity")
    st.pyplot(fig2)

# Trend chart: counts by date (if dates available)
if 'date' in df_analytics.columns and df_analytics['date'].notna().any():
    trend = df_analytics.groupby('date').size().reset_index(name='count')
    fig3, ax3 = plt.subplots()
    ax3.plot(trend['date'].astype(str), trend['count'], marker='o')
    ax3.set_xlabel("Date")
    ax3.set_ylabel("Number of Alerts")
    ax3.set_title("Alerts Over Time")
    plt.xticks(rotation=45)
    st.subheader("Alerts Over Time")
    st.pyplot(fig3)
else:
    st.info("No usable timestamps to build trend chart (ensure 'timestamp' column exists).")

# ----- Bulk detection -----
st.markdown("---")
st.markdown("### 📊 Bulk detection: Run rules across entire dataset")
if st.button("Run Bulk Detection (all records)"):
    results = []
    for _, row in df.iterrows():
        r = detect_threats(row)
        results.append({
            "id": int(row.get('id',0)),
            "alert_type": row.get('alert_type',''),
            "confidence": r['confidence'],
            "conclusions": "; ".join(r['conclusions']),
            "mitigations": "; ".join(r['mitigations'])
        })
    rdf = pd.DataFrame(results).sort_values(by='confidence', ascending=False)
    st.dataframe(rdf.head(200))
    st.success("Bulk detection complete. You may download results below.")

    # Offer downloads
    csv_bytes = rdf.to_csv(index=False).encode()
    st.download_button("Download bulk detection CSV", data=csv_bytes, file_name="bulk_detection_results.csv", mime="text/csv")
    st.download_button("Download bulk detection JSON", data=rdf.to_json(orient="records", indent=2).encode(), file_name="bulk_detection_results.json", mime="application/json")
    # Save to SQLite if requested via sidebar
    if save_db:
        conn = sqlite3.connect("bulk_detection.db")
        rdf.to_sql("bulk_analysis", conn, index=False, if_exists="replace")
        conn.close()
        with open("bulk_detection.db","rb") as f:
            st.download_button("Download bulk_detection.db", data=f.read(), file_name="bulk_detection.db", mime="application/x-sqlite3")

st.markdown("---")
st.caption("Demo app: rule-based detection and simple agentic reasoning. For production, integrate with EDR/IDS feeds and threat intel.")
