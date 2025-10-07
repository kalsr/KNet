

# Cyber_Threat_Detector_Full_Dashboard.py

import streamlit as st
import pandas as pd
import sqlite3
import os
import random
import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# -------------------------
# Configuration
# -------------------------
DB_FILE = "cyber_threats.db"
TABLE_NAME = "analysis"
AGENTIC_TABLE = "agentic_analysis"

st.set_page_config(page_title="Cyber Threat Detector — Full Dashboard", layout="wide")

# -------------------------
# Styling for cards & colored buttons
# -------------------------
st.markdown("""
<style>
div.stButton > button, .stDownloadButton > button {
    color: white; border: none; padding: 12px 16px; border-radius: 10px; font-weight: 600; font-size: 16px; width: 100%;
}
.generate-btn {background-color: #2b9348;} .generate-btn:hover {filter: brightness(0.95);}
.upload-btn {background-color: #3a86ff;} .upload-btn:hover {filter: brightness(0.9);}
.agentic-btn {background-color: #ffbe0b; color:black;} .agentic-btn:hover {filter: brightness(0.9);}
.reset-btn {background-color: #d00000;} .reset-btn:hover {filter: brightness(0.9);}
.card {padding:15px; margin:10px; border-radius:12px; border:1px solid #eee; background-color:#f8f9fa;}
.summary-card {padding:15px; margin:5px; border-radius:12px; border:1px solid #eee; background-color:#e0f7fa; text-align:center;}
.recommendation {padding:10px; border-radius:10px; background-color:#ffefc4; margin:5px 0;}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Database Helper Functions
# -------------------------
def get_conn(): return sqlite3.connect(DB_FILE, check_same_thread=False)

def init_database(preload_if_empty=True, preload_count=50):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            threat_name TEXT,
            alert_type TEXT,
            severity TEXT,
            confidence REAL,
            timestamp TEXT,
            mitigation TEXT,
            notes TEXT,
            notes_json TEXT
        )
    """)
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
            insert_records(rows)
    conn.close()

def insert_records(df):
    df_copy = df.copy()
    known_cols = ['threat_name','alert_type','severity','confidence','timestamp','mitigation','notes']
    df_copy['notes_json'] = ""
    for col in df_copy.columns:
        if col not in known_cols:
            df_copy['notes_json'] += df_copy[col].astype(str) + "; "
    conn = get_conn()
    df_copy.to_sql(TABLE_NAME, conn, if_exists="append", index=False)
    conn.close()

def fetch_records(limit=None):
    conn = get_conn()
    q = f"SELECT * FROM {TABLE_NAME} ORDER BY id DESC"
    if limit:
        q += f" LIMIT {int(limit)}"
    df = pd.read_sql_query(q, conn)
    conn.close()
    return df

def save_agentic_result(record_id, record, agent_out):
    conn = get_conn()
    conn.execute(f"""
        INSERT INTO {AGENTIC_TABLE} 
        (record_id, threat_name, alert_type, confidence, conclusions, mitigations, log, decision, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        record_id,
        record.get("threat_name"),
        record.get("alert_type"),
        agent_out["result"]["confidence"],
        json.dumps(agent_out["result"]["conclusions"]),
        json.dumps(agent_out["result"]["mitigations"]),
        json.dumps(agent_out["log"]),
        agent_out["decision"]["decision"],
        datetime.now().isoformat(sep=" ")
    ))
    conn.commit()
    conn.close()

def fetch_agentic_results(limit=None, term=None):
    conn = get_conn()
    q = f"SELECT * FROM {AGENTIC_TABLE}"
    params = ()
    if term:
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
            "notes": notes,
            "notes_json": ""
        })
    return pd.DataFrame(rows)

# -------------------------
# Rule-based Detection
# -------------------------
def detect_threats(record):
    facts, conclusions, mitigations = [], [], []
    confidence = record.get("confidence", 0.5)
    atype = record.get("alert_type","Unknown").lower()
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
# Summary Panel at top
# -------------------------
df_all = fetch_records()
if len(df_all)>0:
    severity_counts = df_all['severity'].value_counts().to_dict()
    col_low = severity_counts.get('Low',0)
    col_med = severity_counts.get('Medium',0)
    col_high = severity_counts.get('High',0)
    col_crit = severity_counts.get('Critical',0)
    st.markdown("### 🔹 Threat Summary")
    cols = st.columns(4)
    cols[0].markdown(f"<div class='summary-card'><h4>Low</h4><p>{col_low}</p></div>", unsafe_allow_html=True)
    cols[1].markdown(f"<div class='summary-card'><h4>Medium</h4><p>{col_med}</p></div>", unsafe_allow_html=True)
    cols[2].markdown(f"<div class='summary-card'><h4>High</h4><p>{col_high}</p></div>", unsafe_allow_html=True)
    cols[3].markdown(f"<div class='summary-card'><h4>Critical</h4><p>{col_crit}</p></div>", unsafe_allow_html=True)

# -------------------------
# Dashboard: Upload / Generate / View / Agentic
# -------------------------
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='card'><h4>Upload & Save Data</h4></div>", unsafe_allow_html=True)
    uploaded = st.file_uploader("Upload CSV/XLSX", type=["csv","xlsx"])
    if uploaded:
        try:
            df = pd.read_csv(uploaded) if uploaded.name.endswith(".csv") else pd.read_excel(uploaded)
            st.success(f"Loaded {len(df)} records.")
            if st.button("Save Uploaded Data", key="save_upload"):
                insert_records(df)
                st.success("Saved to DB successfully!")
        except Exception as e:
            st.error(f"Upload failed: {e}")

with col2:
    st.markdown("<div class='card'><h4>Generate Sample Records</h4></div>", unsafe_allow_html=True)
    n = st.slider("Number of records", 20, 100, 30, step=5)
    if st.button("Generate & Insert", key="gen_insert"):
        df = generate_sample_dataframe(n)
        insert_records(df)
        st.success(f"Inserted {len(df)} sample records.")

# --- DB Info & Viewer ---
st.markdown("---")
st.subheader("Database Viewer & Agentic Detection")
display_limit = st.slider("Show records", 5, 200, 20, key="display_limit")
if st.button("Display Records", key="disp_records"):
    df_show = fetch_records(limit=display_limit)
    st.dataframe(df_show)
    if len(df_show)>0:
        # Pie charts
        fig1, ax1 = plt.subplots()
        df_show['alert_type'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax1, startangle=90)
        ax1.set_ylabel("")
        st.pyplot(fig1)
        fig2, ax2 = plt.subplots()
        df_show['severity'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax2, startangle=90,
                                                   colors=['#ff9999','#ffc000','#8fd9b6','#d395d0'])
        ax2.set_ylabel("")
        st.pyplot(fig2)
        # Agentic AI
        idx = st.number_input("Select record ID for Agentic Detection",
                              min_value=int(df_show["id"].min()),
                              max_value=int(df_show["id"].max()),
                              value=int(df_show["id"].min()),
                              key="select_record")
        rec = df_show[df_show["id"]==idx].iloc[0].to_dict()
        if st.button("Run Agentic AI & Save", key="run_agentic"):
            agent = SimpleAgent(rec)
            out = agent.run()
            save_agentic_result(rec["id"], rec, out)
            st.success(f"Agentic Detection done! Confidence={out['result']['confidence']}")
            st.markdown("**Decision:**")
            st.info(out["decision"]["decision"])
            st.markdown("**Conclusions & Mitigations:**")
            for c in out["result"]["conclusions"]: st.markdown(f"<div class='recommendation'>- {c}</div>", unsafe_allow_html=True)
            for m in out["result"]["mitigations"]: st.markdown(f"<div class='recommendation'>- {m}</div>", unsafe_allow_html=True)

# --- Query Agentic Analysis ---
st.markdown("---")
st.subheader("Query Agentic Analysis")
term = st.text_input("Search by threat_name / alert_type", key="query_term")
limit = st.number_input("Max rows to show", min_value=1, max_value=500, value=50, key="query_limit")
if st.button("Query Agentic Results", key="query_agentic"):
    df_a = fetch_agentic_results(limit=limit, term=term if term.strip() else None)
    st.dataframe(df_a)
    if len(df_a) > 0:
        st.download_button("Download CSV", data=df_a.to_csv(index=False).encode(), file_name="agentic_analysis.csv")
        st.download_button("Download JSON", data=df_a.to_json(orient="records", indent=2), file_name="agentic_analysis.json")

# --- Reset Database ---
st.markdown("---")
st.markdown("<div class='card'><h4>⚠ Reset Database</h4></div>", unsafe_allow_html=True)
if st.button("Reset / Recreate DB", key="reset_db"):
    reset_database(50)
    st.success("Database reset. Preloaded 50 sample records.")
