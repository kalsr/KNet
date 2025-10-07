

# cyber_threat_detector_agentic_db_fixed_v2.py

import streamlit as st
import pandas as pd
import sqlite3
import os
import random
import json
from datetime import datetime, timedelta

# -------------------------
# Configuration
# -------------------------
DB_FILE = "cyber_threats.db"
TABLE_NAME = "analysis"
AGENTIC_TABLE = "agentic_analysis"

st.set_page_config(page_title="Cyber Threat Detector — Agentic AI + DB - Designed By Randy Singh", layout="wide")

# -------------------------
# Styling
# -------------------------
st.markdown("""
<style>
div.stButton > button, .stDownloadButton > button {
    background-color: #2b9348;
    color: white;
    border: none;
    padding: 8px 14px;
    border-radius: 8px;
    font-weight: 600;
}
div.stButton > button:hover, .stDownloadButton > button:hover { filter: brightness(0.95); }
.big-red {
    display:inline-block; padding:8px 12px; background-color:#d00000;
    color:white; border-radius:8px; font-weight:700; margin-left:8px;
}
.control-card { padding:12px; border-radius:8px; border:1px solid #eee; background-color:#fff; }
.small { font-size:13px; color:#666; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# Database Helper Functions
# -------------------------
def get_conn():
    return sqlite3.connect(DB_FILE, check_same_thread=False)

def init_database(preload_if_empty=True, preload_count=50):
    conn = get_conn()
    cur = conn.cursor()
    # main threat table
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            threat_name TEXT,
            alert_type TEXT,
            severity TEXT,
            confidence REAL,
            timestamp TEXT,
            mitigation TEXT,
            notes TEXT
        )
    """)
    # agentic analysis table
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {AGENTIC_TABLE} (
            analysis_id INTEGER PRIMARY KEY AUTOINCREMENT,
            record_id INTEGER,
            threat_name TEXT,
            alert_type TEXT,
            confidence REAL,
            conclusions TEXT,
            mitigations TEXT,
            log TEXT,
            decision TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    if preload_if_empty:
        cur.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
        count = cur.fetchone()[0]
        if count == 0:
            rows = generate_sample_dataframe(preload_count)
            rows.to_sql(TABLE_NAME, conn, if_exists="append", index=False)
    conn.close()

def insert_records(df):
    """Insert uploaded/generated records into DB. Only keep known columns."""
    conn = get_conn()
    allowed_cols = ["threat_name","alert_type","severity","confidence","timestamp","mitigation","notes"]
    df_to_insert = df.copy()
    # keep only allowed columns
    for col in df_to_insert.columns:
        if col not in allowed_cols:
            df_to_insert.drop(columns=[col], inplace=True)
    # fill missing columns with defaults
    for col in allowed_cols:
        if col not in df_to_insert.columns:
            if col == "confidence":
                df_to_insert[col] = 0.5
            else:
                df_to_insert[col] = ""
    df_to_insert = df_to_insert[allowed_cols]
    df_to_insert.to_sql(TABLE_NAME, conn, if_exists="append", index=False)
    conn.close()

def fetch_records(limit=None):
    conn = get_conn()
    q = f"SELECT * FROM {TABLE_NAME} ORDER BY id DESC"
    if limit:
        q += f" LIMIT {int(limit)}"
    df = pd.read_sql_query(q, conn)
    conn.close()
    return df

def query_by_threatname(term, limit=None):
    conn = get_conn()
    t = f"%{term.strip().lower()}%"
    q = f"""SELECT * FROM {TABLE_NAME}
            WHERE LOWER(threat_name) LIKE ? OR LOWER(alert_type) LIKE ?
            ORDER BY id DESC"""
    if limit:
        q += f" LIMIT {int(limit)}"
    df = pd.read_sql_query(q, conn, params=(t,t))
    conn.close()
    return df

def save_agentic_result(record_id, record, agent_out):
    """Save Agentic analysis into DB"""
    try:
        conn = get_conn()
        cur = conn.cursor()
        threat_name = record.get("threat_name") if isinstance(record, dict) else None
        alert_type = record.get("alert_type") if isinstance(record, dict) else None
        confidence = None
        conclusions = []
        mitigations = []
        log = []
        decision_text = ""
        if isinstance(agent_out, dict):
            result = agent_out.get("result", {})
            confidence = result.get("confidence", None)
            conclusions = result.get("conclusions", []) or []
            mitigations = result.get("mitigations", []) or []
            log = agent_out.get("log", []) or []
            dec = agent_out.get("decision", "")
            if isinstance(dec, dict):
                decision_text = dec.get("decision", "") or str(dec)
            else:
                decision_text = str(dec)
        cur.execute(f"""
            INSERT INTO {AGENTIC_TABLE} 
            (record_id, threat_name, alert_type, confidence, conclusions, mitigations, log, decision, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            int(record_id) if record_id is not None else None,
            threat_name,
            alert_type,
            float(confidence) if confidence is not None else None,
            json.dumps(conclusions, ensure_ascii=False),
            json.dumps(mitigations, ensure_ascii=False),
            json.dumps(log, ensure_ascii=False),
            decision_text,
            datetime.now().isoformat(sep=" ")
        ))
        conn.commit()
        analysis_id = cur.lastrowid
        conn.close()
        return analysis_id
    except Exception as e:
        st.error(f"Failed to save agentic result: {e}")
        try:
            conn.close()
        except:
            pass
        return None

def fetch_agentic_results(limit=None, term=None):
    conn = get_conn()
    q = f"SELECT * FROM {AGENTIC_TABLE}"
    params = ()
    if term and term.strip():
        t = f"%{term.strip().lower()}%"
        q += " WHERE LOWER(threat_name) LIKE ? OR LOWER(alert_type) LIKE ?"
        params = (t,t)
    q += " ORDER BY analysis_id DESC"
    if limit:
        q += f" LIMIT {int(limit)}"
    df = pd.read_sql_query(q, conn, params=params)
    conn.close()
    return df

def reset_database(preload_count=50):
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    init_database(preload_if_empty=True, preload_count=preload_count)

# -------------------------
# Sample Data Generation
# -------------------------
def generate_sample_dataframe(n):
    rows = []
    for i in range(n):
        tname = f"AutoThreat_{random.randint(1000,9999)}"
        atype = random.choice(["malware","phish","sql_injection","xss","ddos","brute_force","scan"])
        severity = random.choice(["Low","Medium","High","Critical"])
        conf = round(random.uniform(0.5,0.95),2)
        ts = (datetime.now() - timedelta(minutes=random.randint(0,1440*10))).isoformat(sep=" ")
        mitigation = f"Mitigation guidance for {atype}"
        notes = f"Generated sample record {i+1}"
        rows.append({
            "threat_name": tname,
            "alert_type": atype,
            "severity": severity,
            "confidence": conf,
            "timestamp": ts,
            "mitigation": mitigation,
            "notes": notes
        })
    return pd.DataFrame(rows)

# -------------------------
# Rule-based Detection
# -------------------------
def detect_threats(record):
    facts, conclusions, mitigations = [], [], []
    try:
        confidence = float(record.get("confidence", 0.5))
    except:
        confidence = 0.5
    atype = str(record.get("alert_type","Unknown")).lower()
    payload = str(record.get("notes","")).lower()
    facts.append(f"Alert type={atype}, severity={record.get('severity')}")
    if "sql" in atype or "union" in payload:
        conclusions.append("Possible SQL Injection.")
        mitigations.append("Use parameterized queries; enable WAF SQLi filter.")
        confidence = max(confidence, 0.6)
    if "xss" in atype or "<script" in payload:
        conclusions.append("Potential XSS injection detected.")
        mitigations.append("Sanitize user input; CSP headers.")
        confidence = max(confidence, 0.55)
    if "phish" in atype:
        conclusions.append("Phishing campaign pattern.")
        mitigations.append("Educate users; enable link scanning.")
        confidence = max(confidence, 0.6)
    if "malware" in atype:
        conclusions.append("Malware threat detected.")
        mitigations.append("Isolate host; run AV scan.")
        confidence = max(confidence, 0.7)
    if "ddos" in atype:
        conclusions.append("Possible DDoS flood observed.")
        mitigations.append("Enable rate limiting; blackhole source.")
        confidence = max(confidence, 0.75)
    if "scan" in atype:
        conclusions.append("Reconnaissance scanning activity.")
        mitigations.append("Block scanning IPs; alert SOC.")
        confidence = max(confidence, 0.5)
    if not conclusions:
        conclusions.append("No critical threat signature.")
        mitigations.append("Continue monitoring and deeper packet analysis.")
    return {"facts": facts, "conclusions": conclusions, "mitigations": mitigations, "confidence": round(float(confidence),2)}

# -------------------------
# Agentic AI Module
# -------------------------
class SimpleAgent:
    def __init__(self, record):
        self.record = record
        self.log = []
    def observe(self):
        self.log.append("OBSERVE: Gathered record fields.")
        return self.record
    def hypothesize(self):
        atype = str(self.record.get("alert_type","")).lower()
        hyp = "Unknown Threat"
        if "sql" in atype: hyp = "SQL Injection"
        elif "xss" in atype: hyp = "Cross-Site Scripting"
        elif "phish" in atype: hyp = "Phishing"
        elif "malware" in atype: hyp = "Malware"
        elif "ddos" in atype: hyp = "DDoS"
        elif "scan" in atype: hyp = "Reconnaissance"
        self.log.append(f"HYPOTHESIZE: Possible threat = {hyp}")
        return hyp
    def test(self):
        result = detect_threats(self.record)
        self.log.append("TEST: Ran rule-based checks.")
        return result
    def decide_and_act(self, result):
        conf = result.get("confidence",0)
        if conf >= 0.75:
            decision = "Immediate Response Required"
        elif conf >= 0.55:
            decision = "Investigate and Contain"
        else:
            decision = "Monitor Further"
        self.log.append(f"DECIDE: {decision}")
        return {"decision": decision, "actions": result["mitigations"]}
    def run(self):
        self.observe()
        hyp = self.hypothesize()
        result = self.test()
        decision = self.decide_and_act(result)
        return {"log": self.log, "hypothesis": hyp, "result": result, "decision": decision}

# -------------------------
# Initialize DB
# -------------------------
init_database(preload_if_empty=True, preload_count=50)

# -------------------------
# UI — Top Section
# -------------------------
st.title(" Cyber Threat Detector — Agentic AI + DB")

col1, col2 = st.columns([2,1])
with col1:
    st.subheader("Data Controls")
    uploaded = st.file_uploader("Upload sample data (CSV/XLSX)", type=["csv","xlsx"])
    if uploaded:
        try:
            df = pd.read_csv(uploaded) if uploaded.name.lower().endswith(".csv") else pd.read_excel(uploaded)
            st.success(f"Loaded {len(df)} records.")
            if st.button("Save uploaded data to DB"):
                insert_records(df)
                st.success("Saved to DB successfully.")
        except Exception as e:
            st.error(f"Upload failed: {e}")

with col2:
    st.subheader("Database Info")
    total = len(fetch_records())
    st.metric("Total DB Records", total)
    st.write("DB file:", f"`{DB_FILE}`")
