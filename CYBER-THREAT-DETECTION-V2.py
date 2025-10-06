# CYBER-THREAT-DETECTION-V1_full.py
import streamlit as st
import pandas as pd
import sqlite3
import json
import random
import io
import os
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import hashlib

# ----------------- Config -----------------
BUNDLED_CSV = os.path.join(os.path.dirname(__file__), "cyber_threats.csv")
DEFAULT_DB_NAME = "cyber_threats_uploaded.db"

st.set_page_config(page_title="Cyber Threat Detector v2 - Randy Singh | KNet Consulting", layout="wide")

# ----------------- Styling -----------------
# We style the native Streamlit buttons so they look like colored cards.
st.markdown("""
<style>
/* Make sidebar buttons look like colored cards */
.stButton>button {
  border-radius:10px;
  padding:12px 18px;
  font-size:15px;
  font-weight:700;
  color: #fff;
  margin:6px 0;
  width:100%;
  box-shadow: 0 2px 6px rgba(0,0,0,0.12);
  border: none;
}

/* Use data attributes (order-sensitive) to map colors reliably */
div[data-testid="stSidebar"] .stButton button:nth-of-type(1) { background:#2b9348; } /* Upload */
div[data-testid="stSidebar"] .stButton button:nth-of-type(2) { background:#1971c2; } /* Load Bundled */
div[data-testid="stSidebar"] .stButton button:nth-of-type(3) { background:#f08a24; } /* Generate */
div[data-testid="stSidebar"] .stButton button:nth-of-type(4) { background:#d00000; } /* Reset */

/* Main area card styles (for optional visual cards if displayed) */
.card {
  padding:14px;
  border-radius:10px;
  background: linear-gradient(90deg, #ffffff, #f7f9fc);
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  margin-bottom:10px;
}
.header { font-weight:800; font-size:18px; margin-bottom:6px; }
.small { font-size:13px; color:#555; }
</style>
""", unsafe_allow_html=True)

# ----------------- Header -----------------
st.title("🔐 Cyber Threat Detector — v2")
st.markdown("**Developed by Randy Singh — KNet Consulting Group**")
st.markdown("A demo app: rule-based detection + simple Agentic reasoning + dataset management + visual analytics.")

# ----------------- Sidebar Controls -----------------
with st.sidebar:
    st.header("Data Controls")
    st.markdown("<div class='small'>Upload a dataset (CSV / JSON / Excel) or use bundled DB / generate synthetic samples.</div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload threat data (CSV, JSON, Excel)", type=["csv","json","xls","xlsx"])

    # 1) Upload button (functional)
    if st.button("Upload Data File"):
        if uploaded_file is None:
            st.warning("Please choose a file to upload first.")
        else:
            try:
                fname = uploaded_file.name.lower()
                uploaded_file.seek(0)
                if fname.endswith(".csv") or uploaded_file.type == "text/csv":
                    df_uploaded = pd.read_csv(uploaded_file)
                elif fname.endswith((".xls", ".xlsx")) or uploaded_file.type in ["application/vnd.ms-excel","application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
                    df_uploaded = pd.read_excel(uploaded_file)
                else:
                    uploaded_file.seek(0)
                    df_uploaded = pd.read_json(uploaded_file)
                if 'id' not in df_uploaded.columns:
                    df_uploaded.insert(0, 'id', range(1, len(df_uploaded)+1))
                st.session_state['df'] = df_uploaded
                st.session_state['source'] = 'uploaded'
                st.session_state['uploaded_filename'] = uploaded_file.name
                st.success(f"Uploaded '{uploaded_file.name}' loaded into session.")
            except Exception as e:
                st.error(f"Failed to read uploaded file: {e}")

    st.write("---")

    # 2) Load bundled dataset
    if st.button("Load Bundled DB"):
        if os.path.exists(BUNDLED_CSV):
            try:
                df_bundled = pd.read_csv(BUNDLED_CSV)
            except Exception as e:
                st.error(f"Failed to read bundled CSV: {e}")
                df_bundled = pd.DataFrame()
        else:
            # Fallback placeholder row
            df_bundled = pd.DataFrame([{
                "id": 1,
                "timestamp": datetime.now().isoformat(sep=' '),
                "source_ip":"192.168.0.1",
                "dest_ip":"10.0.0.5","src_port":12345,"dest_port":80,"protocol":"HTTP",
                "bytes":250,"packets":2,"alert_type":"Port Scan","severity":"Low",
                "description":"Placeholder record","indicators":"[]","tactic":"TA0007",
                "technique":"T1595","detected_by":"IDS","confidence":0.4,"payload_signature":"",
                "file_hash":"","url":"","username":"","outcome":"blocked","remediation":"Block IP","tags":"scan"
            }])
        if 'id' not in df_bundled.columns:
            df_bundled.insert(0, 'id', range(1, len(df_bundled)+1))
        st.session_state['df'] = df_bundled
        st.session_state['source'] = 'bundled'
        st.success("Bundled dataset loaded into session.")

    st.write("---")

    # 3) Generate synthetic samples
    gen_count = st.slider("Generate sample records", 20, 200, 50, step=5)
    if st.button("Generate Sample Records"):
        # create synthetic dataset
        def generate_synthetic(n):
            alert_types = [
                "Port Scan", "SQL Injection", "XSS Attempt", "Brute Force",
                "Phishing URL", "Malware Download", "DDoS", "Data Exfiltration",
                "Suspicious Login", "Ransomware Activity"
            ]
            severities = ["Low","Medium","High","Critical"]
            protocols = ["HTTP","HTTPS","TCP","UDP","SSH","DNS"]
            now = datetime.now()
            rows = []
            for i in range(n):
                # random IPs
                src_ip = f"{random.randint(10,250)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
                dest_ip = f"10.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
                alert = random.choice(alert_types)
                severity = random.choices(severities, weights=[40,35,20,5])[0]
                protocol = random.choice(protocols)
                # bytes skewed based on type
                if "DDoS" in alert:
                    bytes_count = random.randint(100000, 5000000)
                elif "Exfil" in alert or "Exfiltration" in alert or "Ransomware" in alert:
                    bytes_count = random.randint(10000, 200000)
                else:
                    bytes_count = random.randint(50, 20000)
                # payload signature or URL
                payload_sig = ""
                url = ""
                if "SQL" in alert:
                    payload_sig = "UNION SELECT" if random.random() < 0.6 else "SELECT * FROM users"
                if "XSS" in alert:
                    payload_sig = "<script>alert(1)</script>"
                if "Phishing" in alert:
                    url = f"http://malicious-{random.randint(1000,9999)}.example.com/login"
                file_hash = ""
                if "Malware" in alert or random.random() < 0.05:
                    # generate pseudo hash
                    file_hash = hashlib.sha1(f"{random.random()}{i}".encode()).hexdigest()
                ts = (now - timedelta(minutes=random.randint(0, 60*24*30))).isoformat(sep=' ')
                row = {
                    "id": i+1,
                    "timestamp": ts,
                    "source_ip": src_ip,
                    "dest_ip": dest_ip,
                    "src_port": random.randint(1024,65000),
                    "dest_port": random.choice([80,443,22,21,53,3389,445]),
                    "protocol": protocol,
                    "bytes": bytes_count,
                    "packets": random.randint(1,1500),
                    "alert_type": alert,
                    "severity": severity,
                    "description": f"Auto-generated record: {alert}",
                    "indicators": "[]",
                    "tactic": random.choice(["TA0007","TA0006","TA0001","TA0040"]),
                    "technique": random.choice(["T1595","T1190","T1059","T1110"]),
                    "detected_by":"SimSensor",
                    "confidence": round(random.uniform(0.3,0.95),2),
                    "payload_signature": payload_sig,
                    "file_hash": file_hash,
                    "url": url,
                    "username": f"user{random.randint(1,999)}",
                    "outcome": random.choice(["blocked","allowed","quarantined"]),
                    "remediation": "",
                    "tags": ",".join(random.sample(["scan","ddos","exfil","malware","phish","credential","suspicious"], k=2))
                }
                rows.append(row)
            return pd.DataFrame(rows)
        df_gen = generate_synthetic(gen_count)
        st.session_state['df'] = df_gen
        st.session_state['source'] = 'generated'
        st.session_state['generated_n'] = gen_count
        st.success(f"Synthetic dataset of {gen_count} records generated and loaded into session.")

    st.write("---")

    # 4) Reset / Clear All
    if st.button("Reset / Clear All"):
        # Clear session state robustly
        try:
            for k in list(st.session_state.keys()):
                del st.session_state[k]
        except Exception:
            st.session_state.clear()
        # Rerun to reflect cleared state
        st.experimental_rerun()

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

# ----------------- Helper functions -----------------
@st.cache_data
def load_bundled_csv():
    if os.path.exists(BUNDLED_CSV):
        return pd.read_csv(BUNDLED_CSV)
    else:
        return pd.DataFrame([{
            "id":1,
            "timestamp":datetime.now().isoformat(sep=' '),
            "source_ip":"192.168.0.1","dest_ip":"10.0.0.5","src_port":12345,"dest_port":80,"protocol":"HTTP",
            "bytes":250,"packets":2,"alert_type":"Port Scan","severity":"Low","description":"Placeholder record",
            "indicators":"[]","tactic":"TA0007","technique":"T1595","detected_by":"IDS","confidence":0.4,"payload_signature":"",
            "file_hash":"","url":"","username":"","outcome":"blocked","remediation":"Block IP","tags":"scan"
        }])

def detect_threats(df_row):
    facts, conclusions, mitigations = [], [], []
    try:
        confidence = float(df_row.get('confidence', 0.5) or 0.5)
    except:
        confidence = 0.5
    atype = str(df_row.get('alert_type','Unknown')).lower()
    payload = str(df_row.get('payload_signature','')).lower()
    try:
        bytes_count = int(df_row.get('bytes',0) or 0)
    except:
        bytes_count = 0
    tags = str(df_row.get('tags',''))

    facts.append(f"Observed alert_type={atype}, bytes={bytes_count}, payload='{payload}'")

    if "sql" in atype or "union select" in payload:
        conclusions.append("SQL Injection attempt detected.")
        mitigations.append("Use parameterized queries and WAF rules.")
        confidence = max(confidence, 0.6)
    if "xss" in atype or "<script" in payload:
        conclusions.append("Cross-Site Scripting (XSS) attempt detected.")
        mitigations.append("Sanitize output; implement CSP.")
        confidence = max(confidence,0.55)
    if "brute" in atype or "failed_logins" in str(df_row.get('indicators','')):
        conclusions.append("Brute-force login activity detected.")
        mitigations.append("Rate-limit and enable MFA.")
        confidence = max(confidence,0.5)
    if "phish" in atype or str(df_row.get('url','')).startswith("http://"):
        conclusions.append("Phishing link detected.")
        mitigations.append("Block URL and remove emails.")
        confidence = max(confidence,0.6)
    if "malware" in atype or df_row.get('file_hash','') != "":
        conclusions.append("Malware suspected.")
        mitigations.append("Isolate host and run AV/EDR scans.")
        confidence = max(confidence,0.7)
    if "port scan" in atype or "scan" in tags:
        conclusions.append("Port scan / reconnaissance detected.")
        mitigations.append("Block noisy source IPs and tighten firewall.")
        confidence = max(confidence,0.4)
    if bytes_count>500000 and ("ddos" in atype or "ddos" in tags):
        conclusions.append("Traffic indicates likely DDoS.")
        mitigations.append("Engage DDoS mitigation services.")
        confidence = max(confidence,0.75)
    if "exfil" in atype or "/download" in payload or "exfil" in tags:
        conclusions.append("Potential data exfiltration activity.")
        mitigations.append("Block destination and inspect traffic.")
        confidence = max(confidence,0.65)

    if len(conclusions) == 0:
        conclusions.append("No high-fidelity rule matched. Recommend deeper inspection.")
        mitigations.append("Collect PCAP and increase logging.")
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

# ----------------- Load / Source Data (session-persistent) -----------------
if 'df' in st.session_state:
    df = st.session_state['df']
    source = st.session_state.get('source', 'session')
else:
    # default to bundled
    df = load_bundled_csv()
    source = 'bundled'
    st.session_state['df'] = df
    st.session_state['source'] = 'bundled'

# Ensure id column exists and is a simple integer index
if 'id' not in df.columns:
    df.insert(0, 'id', range(1, len(df)+1))
else:
    try:
        df['id'] = df['id'].astype(int)
    except:
        df['id'] = range(1, len(df)+1)

st.write(f"Loaded **{len(df)}** records (source: {source})")
st.dataframe(df.head(50))

# ----------------- CSV-to-DB Upload Integration -----------------
st.markdown("### 📥 Upload CSV to populate SQLite DB")
if st.session_state.get('source') == 'uploaded':
    db_name = st.text_input("Enter SQLite DB filename to create:", value=DEFAULT_DB_NAME)
    if st.button("Create SQLite DB from uploaded file"):
        try:
            conn = sqlite3.connect(db_name)
            st.session_state['df'].to_sql("threats", conn, index=False, if_exists="replace")
            conn.close()
            st.success(f"✅ SQLite DB '{db_name}' created from uploaded CSV!")
            st.session_state['last_created_db'] = os.path.abspath(db_name)
            with open(db_name, "rb") as f:
                db_bytes = f.read()
            st.download_button("Download SQLite DB", data=db_bytes, file_name=db_name, mime="application/x-sqlite3")
        except Exception as e:
            st.error(f"Failed to create SQLite DB: {e}")

# ----------------- Select a record to analyze -----------------
st.markdown("### 🔍 Select a record to analyze")
idx = st.number_input("Record index (1-based)", min_value=1, max_value=max(1, len(df)), value=1, step=1)
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
            st.session_state['last_created_csv'] = os.path.abspath(csv_name)
        if save_json:
            json_name = "analysis_result.json"
            out_df.to_json(json_name, orient="records", indent=2)
            st.download_button("Download analysis as JSON", data=open(json_name,"rb"), file_name=json_name, mime="application/json")
            st.session_state['last_created_json'] = os.path.abspath(json_name)
        if save_excel:
            excel_name = "analysis_result.xlsx"
            out_df.to_excel(excel_name, index=False)
            st.download_button("Download analysis as Excel", data=open(excel_name,"rb"), file_name=excel_name, mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            st.session_state['last_created_excel'] = os.path.abspath(excel_name)
        if save_db:
            db_path = "analysis_results.db"
            conn = sqlite3.connect(db_path)
            out_df.to_sql("analysis", conn, index=False, if_exists="append")
            conn.close()
            with open(db_path,"rb") as f:
                st.download_button("Download analysis DB", data=f.read(), file_name=db_path, mime="application/x-sqlite3")
            st.session_state['last_created_db'] = os.path.abspath(db_path)

# ----------------- Visual Analytics -----------------
st.markdown("---")
st.markdown("### 📈 Visual Analytics")

df_analytics = df.copy()
if 'timestamp' in df_analytics.columns:
    try:
        df_analytics['ts'] = pd.to_datetime(df_analytics['timestamp'], errors='coerce')
        df_analytics['date'] = df_analytics['ts'].dt.date
    except:
        df_analytics['date'] = pd.NaT
else:
    df_analytics['date'] = pd.NaT

# Pie chart
type_counts = df_analytics['alert_type'].fillna("Unknown").value_counts().nlargest(10)
fig1, ax1 = plt.subplots()
ax1.pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
st.subheader("Threat Type Distribution (Top 10)")
st.pyplot(fig1)

# Bar chart: severity
if 'severity' in df_analytics.columns:
    sev_counts = df_analytics['severity'].fillna("Unknown").value_counts()
    fig2, ax2 = plt.subplots()
    ax2.bar(sev_counts.index.astype(str), sev_counts.values)
    ax2.set_xlabel("Severity")
    ax2.set_ylabel("Count")
    ax2.set_title("Threats by Severity")
    st.subheader("Threats by Severity")
    st.pyplot(fig2)

# Trend
if df_analytics['date'].notna().any():
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

# ----------------- Bulk detection -----------------
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
    csv_bytes = rdf.to_csv(index=False).encode()
    st.download_button("Download bulk detection CSV", data=csv_bytes, file_name="bulk_detection_results.csv", mime="text/csv")
    st.download_button("Download bulk detection JSON", data=rdf.to_json(orient="records", indent=2).encode(), file_name="bulk_detection_results.json", mime="application/json")
    if save_db:
        conn = sqlite3.connect("bulk_detection.db")
        rdf.to_sql("bulk_analysis", conn, index=False, if_exists="replace")
        conn.close()
        with open("bulk_detection.db","rb") as f:
            st.download_button("Download bulk_detection.db", data=f.read(), file_name="bulk_detection.db", mime="application/x-sqlite3")
        st.session_state['last_created_db'] = os.path.abspath("bulk_detection.db")

# ----------------- Data Source Panel -----------------
st.markdown("---")
st.markdown("### 📂 Data Source Panel — where DB/files were created")
def show_path(label, varname):
    val = st.session_state.get(varname, None)
    if val:
        abs_path = os.path.abspath(val)
        exists = os.path.exists(abs_path)
        st.write(f"**{label}:** {abs_path} — {'Exists' if exists else 'Not found'}")
    else:
        st.write(f"**{label}:** Not created yet")

show_path("Last created SQLite DB", "last_created_db")
show_path("Last created CSV", "last_created_csv")
show_path("Last created JSON", "last_created_json")
show_path("Last created Excel", "last_created_excel")
show_path("Uploaded filename (in session)", "uploaded_filename")

st.caption("Files created by the app are in the app working directory (where you launched streamlit). Download or move them to persistent storage as needed.")

st.markdown("---")
st.caption("Demo app: rule-based detection and simple agentic reasoning. For production, integrate with EDR/IDS feeds and threat intel.")
