# Auto-creates cyber_threats.db (with a table analysis) when it first runs
# Preloads 50 mock records if the DB is empty on first launch
# Buttons for:
# Upload sample data (CSV, XLSX) and save into DB
# Generate sample data (20–100 records) and insert into DB
# Display database records (with a slider to select how many to display)
# Query DB by threat name (text search)
# Reset / Recreate DB (red button) — deletes DB and reinitializes with 50 records

# All major UI buttons visually green (via injected CSS). Reset also shows a red visual element to indicate danger.
# Download query/display results as CSV or JSON
# All functions implemented and called where appropriate

# THIS APPLICATION IS DEVELOPED BY RANDY SINGH FROM KNet CONSULTING GROUP




import streamlit as st

import pandas as pd

import sqlite3

import os

import random

import string

import io

from datetime import datetime, timedelta



# -------------------------

# Configuration

# -------------------------

DB_FILE = "cyber_threats.db"

TABLE_NAME = "analysis"

BUNDLED_CSV = "cyber_threats.csv"  # optional bundled CSV (if present will be used for generate samples)



st.set_page_config(page_title="Cyber Threat Detector — Full App", layout="wide")



# -------------------------

# Styling: make buttons green and reset visually red

# -------------------------

st.markdown(

    """

    <style>

    /* Make streamlit buttons green by default */

    div.stButton > button, .stDownloadButton > button {

        background-color: #2b9348;

        color: white;

        border: none;

        padding: 8px 14px;

        border-radius: 8px;

        font-weight: 600;

    }

    /* Slight hover style */

    div.stButton > button:hover, .stDownloadButton > button:hover {

        filter: brightness(0.95);

    }

    /* Make danger / reset visual element red (we will render a red-looking div next to reset) */

    .big-red {

        display:inline-block;

        padding:8px 12px;

        background-color: #d00000;

        color: #fff;

        border-radius:8px;

        font-weight:700;

        margin-left:8px;

    }

    /* Tighter spacing for controls */

    .control-card { padding: 12px; border-radius:8px; border:1px solid #eee; background-color:#fff; }

    </style>

    """,

    unsafe_allow_html=True,

)



# -------------------------

# Database helper functions

# -------------------------

def get_conn():

    return sqlite3.connect(DB_FILE, check_same_thread=False)



def init_database(preload_if_empty: bool = True, preload_count: int = 50):

    """Create DB file and table. If empty and preload_if_empty True insert preload_count mock records."""

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

            notes TEXT

        )

    """)

    conn.commit()



    if preload_if_empty:

        cur.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")

        count = cur.fetchone()[0]

        if count == 0:

            # Insert preload_count mock records

            for i in range(preload_count):

                tname = f"Threat_{i+1}_{random.choice(string.ascii_uppercase)}"

                atype = random.choice(["malware","phish","sql_injection","xss","ddos","brute_force","scan"])

                severity = random.choice(["Low","Medium","High","Critical"])

                confidence = round(random.uniform(0.5,0.99), 2)

                ts = (datetime.now() - timedelta(days=random.randint(0,30), minutes=random.randint(0,1440))).isoformat(sep=' ')

                mitigation = f"Suggested mitigation {i+1}"

                notes = f"Auto-generated sample record #{i+1}"

                cur.execute(f"""

                    INSERT INTO {TABLE_NAME} (threat_name, alert_type, severity, confidence, timestamp, mitigation, notes)

                    VALUES (?, ?, ?, ?, ?, ?, ?)

                """, (tname, atype, severity, confidence, ts, mitigation, notes))

            conn.commit()

    conn.close()



def insert_records(df: pd.DataFrame):

    """Insert a DataFrame into the DB (df columns should match or be subset)."""

    conn = get_conn()

    # Normalize columns to DB schema

    expected = ["threat_name","alert_type","severity","confidence","timestamp","mitigation","notes"]

    for c in expected:

        if c not in df.columns:

            df[c] = None

    # Keep only expected columns

    to_store = df[expected].copy()

    to_store.to_sql(TABLE_NAME, conn, if_exists="append", index=False)

    conn.close()



def fetch_records(limit: int = None, order_desc: bool = True) -> pd.DataFrame:

    conn = get_conn()

    q = f"SELECT * FROM {TABLE_NAME}"

    if order_desc:

        q += " ORDER BY id DESC"

    if limit:

        q += f" LIMIT {int(limit)}"

    df = pd.read_sql_query(q, conn)

    conn.close()

    return df



def query_by_threatname(term: str, limit: int = None) -> pd.DataFrame:

    conn = get_conn()

    # Simple case-insensitive wildcard search across threat_name and alert_type

    t = f"%{term.strip().lower()}%"

    q = f"SELECT * FROM {TABLE_NAME} WHERE LOWER(threat_name) LIKE ? OR LOWER(alert_type) LIKE ? ORDER BY id DESC"

    if limit:

        q += f" LIMIT {int(limit)}"

    df = pd.read_sql_query(q, conn, params=(t,t))

    conn.close()

    return df



def reset_database(preload_count: int = 50):

    """Delete DB and reinitialize (with preload_count records)."""

    if os.path.exists(DB_FILE):

        try:

            os.remove(DB_FILE)

        except Exception as e:

            raise RuntimeError(f"Failed to delete DB file: {e}")

    init_database(preload_if_empty=True, preload_count=preload_count)



# -------------------------

# Sample data generation

# -------------------------

def generate_sample_dataframe(n: int) -> pd.DataFrame:

    rows = []

    for i in range(n):

        tname = f"AutoThreat_{random.randint(1000,9999)}_{random.choice(string.ascii_uppercase)}"

        atype = random.choice(["malware","phish","sql_injection","xss","ddos","brute_force","scan"])

        severity = random.choice(["Low","Medium","High","Critical"])

        confidence = round(random.uniform(0.5,0.99), 2)

        ts = (datetime.now() - timedelta(days=random.randint(0,30), minutes=random.randint(0,1440))).isoformat(sep=' ')

        mitigation = f"Auto mitigation for {tname}"

        notes = f"Generated sample {i+1}"

        rows.append({

            "threat_name": tname,

            "alert_type": atype,

            "severity": severity,

            "confidence": confidence,

            "timestamp": ts,

            "mitigation": mitigation,

            "notes": notes

        })

    return pd.DataFrame(rows)



# -------------------------

# Initialize DB on app start (preload 50 if empty)

# -------------------------

init_database(preload_if_empty=True, preload_count=50)



# -------------------------

# UI Layout

# -------------------------

st.title("🔐 Cyber Threat Detector — Full App")

st.markdown("Professional demo: upload/generate data, query and view SQLite DB, and reset the database.")



# Two-column top controls

with st.container():

    col1, col2 = st.columns([2,1])



    with col1:

        st.subheader("Data Controls")

        st.markdown("<div class='control-card'>", unsafe_allow_html=True)



        # Upload sample data file and save to DB

        uploaded = st.file_uploader("Upload sample data (CSV / XLSX)", type=["csv","xlsx","xls"], help="CSV columns expected: threat_name,alert_type,severity,confidence,timestamp,mitigation,notes")

        if uploaded is not None:

            try:

                if uploaded.type == "text/csv" or uploaded.name.lower().endswith(".csv"):

                    df_uploaded = pd.read_csv(uploaded)

                else:

                    df_uploaded = pd.read_excel(uploaded)

                st.success(f"Read {len(df_uploaded)} rows from uploaded file.")

                st.write(df_uploaded.head(5))

                if st.button("Save uploaded file to DB"):

                    insert_records(df_uploaded)

                    st.success("Uploaded data saved to database.")

            except Exception as e:

                st.error(f"Failed to parse uploaded file: {e}")



        st.markdown("---")



        # Generate sample data (20-100) and insert

        gen_count = st.slider("Generate sample records", min_value=20, max_value=100, value=50, step=5)

        if st.button("Generate sample records and insert into DB"):

            df_gen = generate_sample_dataframe(gen_count)

            insert_records(df_gen)

            st.success(f"Generated and inserted {len(df_gen)} records into the database.")

            st.dataframe(df_gen.head(8))



        st.markdown("</div>", unsafe_allow_html=True)



    with col2:

        st.subheader("Quick Export / Info")

        st.markdown("<div class='control-card'>", unsafe_allow_html=True)

        # Quick stats about DB

        try:

            df_all = fetch_records(limit=1_000_000)

            total_count = len(df_all)

        except Exception:

            total_count = 0

        st.metric("Records in DB", total_count)

        st.write("Database file:", f"`{DB_FILE}`")

        # Link-ish hint for DB browser

        st.write("To open DB locally, use *DB Browser for SQLite* (https://sqlitebrowser.org).")

        st.markdown("</div>", unsafe_allow_html=True)



# Horizontal rule

st.markdown("---")



# Middle section: Display and Query controls

st.subheader("Database Viewer & Query")



st.markdown("Use the buttons below to display or query DB records. Use the slider to limit how many rows are shown. Download results as CSV/JSON.")



display_col, query_col, reset_col = st.columns([2,2,1])



with display_col:

    display_limit = st.slider("Records to display (when viewing)", min_value=5, max_value=500, value=25, step=5)

    if st.button("Display DB records (show latest)"):

        try:

            df_show = fetch_records(limit=display_limit)

            st.success(f"Loaded {len(df_show)} records.")

            st.dataframe(df_show, use_container_width=True)

            csv = df_show.to_csv(index=False).encode('utf-8')

            st.download_button("Download shown records (CSV)", data=csv, file_name="db_shown_records.csv")

            st.download_button("Download shown records (JSON)", data=df_show.to_json(orient="records", indent=2), file_name="db_shown_records.json")

        except Exception as e:

            st.error(f"Failed to read DB: {e}")



with query_col:

    st.write("Search by threat name or alert type (case-insensitive substring):")

    q_term = st.text_input("Enter search term", value="")

    q_limit = st.number_input("Max results to return", min_value=1, max_value=1000, value=100, step=1)

    if st.button("Query DB by threat / alert"):

        if not q_term.strip():

            st.warning("Enter a search term first.")

        else:

            try:

                df_q = query_by_threatname(q_term, limit=q_limit)

                st.success(f"Found {len(df_q)} matching records.")

                st.dataframe(df_q, use_container_width=True)

                st.download_button("Download query results (CSV)", data=df_q.to_csv(index=False).encode('utf-8'), file_name="db_query_results.csv")

                st.download_button("Download query results (JSON)", data=df_q.to_json(orient="records", indent=2), file_name="db_query_results.json")

            except Exception as e:

                st.error(f"Query failed: {e}")



with reset_col:

    # Show a red visual label and a red-appearing reset button cue; actual st.button remains green (global CSS)

    st.markdown("<span class='big-red'>DANGER: Reset DB</span>", unsafe_allow_html=True)

    if st.button("Reset / Recreate DB (danger)"):

        try:

            reset_database(preload_count=50)

            st.success("Database deleted and recreated. Preloaded 50 sample records.")

        except Exception as e:

            st.error(f"Reset failed: {e}")



# -------------------------

# Footer: manual DB actions & info

# -------------------------

st.markdown("---")

st.write("Advanced: You can manually inspect the database file `cyber_threats.db` in the app folder. Use DB Browser for SQLite to open and export tables.")

st.caption("Buttons are styled green except the red danger marker next to Reset. This is a local demo app — for production change DB path & add proper authentication.")