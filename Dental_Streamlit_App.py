# THIS APPLICATION IS DEVELOPED BY RANDY SINGH FROM KNet CONSULTING GROUP.

# python
# dental_app_streamlit.py
# Streamlit port of the multi-user dental practice patient console
# - SQLite by default (patients.db)
# - Optional Postgres via env DB_BACKEND=postgres and PG_* envs
# - Generate Sample(50), Clear All, Add, Delete Selected, Bulk status update
# - Search, Status filter
# - Save JSON (download)
# - Upload JSON/CSV/TXT
# THIS APPLICATION IS DEVELOPED BY RANDY SINGH FROM knET CONSULTING GROUP

import os
import sqlite3
from datetime import datetime
import random
import pandas as pd
import streamlit as st

try:
    import psycopg2  # optional; used only if DB_BACKEND=postgres
except Exception:
    psycopg2 = None

# -------------------------- Config --------------------------

APP_TITLE = "Dental Practice - Multi-User (Streamlit)"
STATUSES = ["Waiting", "In Progress", "Completed"]
ROLES = ["Receptionist", "Dentist", "Billing", "Follow-up"]

# -------------------------- DB Layer --------------------------

class DB:
    def __init__(self):
        self.backend = os.environ.get("DB_BACKEND", "sqlite").strip().lower()
        if self.backend == "postgres":
            if psycopg2 is None:
                raise RuntimeError("psycopg2-binary not installed but DB_BACKEND=postgres set.")
            self.db_type = "postgres"
            self.conn = self._connect_postgres()
        else:
            self.db_type = "sqlite"
            self.conn = self._connect_sqlite()
        self._init_schema()

    def _connect_sqlite(self):
        conn = sqlite3.connect("patients.db", check_same_thread=False)
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA foreign_keys=ON;")
        return conn

    def _connect_postgres(self):
        host = os.environ.get("PG_HOST", "127.0.0.1")
        db = os.environ.get("PG_DATABASE", "dental_office")
        user = os.environ.get("PG_USER", "postgres")
        pw = os.environ.get("PG_PASSWORD", "postgres")
        port = int(os.environ.get("PG_PORT", "5432"))
        conn = psycopg2.connect(host=host, database=db, user=user, password=pw, port=port)
        conn.autocommit = True
        return conn

    def _init_schema(self):
        c = self.conn.cursor()
        if self.db_type == "sqlite":
            c.execute("""
                CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    status TEXT NOT NULL,
                    last_updated_by TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                );
            """)
            c.execute("CREATE INDEX IF NOT EXISTS idx_patients_status ON patients(status);")
            c.execute("CREATE INDEX IF NOT EXISTS idx_patients_name ON patients(name);")
            self.conn.commit()
        else:
            c.execute("""
                CREATE TABLE IF NOT EXISTS patients (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    status TEXT NOT NULL,
                    last_updated_by TEXT,
                    created_at TIMESTAMP NOT NULL,
                    updated_at TIMESTAMP NOT NULL
                );
            """)
            c.execute("CREATE INDEX IF NOT EXISTS idx_patients_status ON patients(status);")
            c.execute("CREATE INDEX IF NOT EXISTS idx_patients_name ON patients(name);")

    # CRUD
    def add_patient(self, name, role_default="Receptionist"):
        now = datetime.utcnow()
        if self.db_type == "sqlite":
            self.conn.execute(
                "INSERT INTO patients (name, status, last_updated_by, created_at, updated_at) VALUES (?, ?, ?, ?, ?);",
                (name, "Waiting", role_default, now.isoformat(), now.isoformat()),
            )
            self.conn.commit()
        else:
            cur = self.conn.cursor()
            cur.execute(
                "INSERT INTO patients (name, status, last_updated_by, created_at, updated_at) VALUES (%s, %s, %s, %s, %s);",
                (name, "Waiting", role_default, now, now),
            )

    def update_status(self, patient_id, new_status, role):
        now = datetime.utcnow()
        if self.db_type == "sqlite":
            self.conn.execute(
                "UPDATE patients SET status=?, last_updated_by=?, updated_at=? WHERE id=?;",
                (new_status, role, now.isoformat(), int(patient_id)),
            )
            self.conn.commit()
        else:
            cur = self.conn.cursor()
            cur.execute(
                "UPDATE patients SET status=%s, last_updated_by=%s, updated_at=%s WHERE id=%s;",
                (new_status, role, now, int(patient_id)),
            )

    def delete_patient(self, patient_id):
        if self.db_type == "sqlite":
            self.conn.execute("DELETE FROM patients WHERE id=?;", (int(patient_id),))
            self.conn.commit()
        else:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM patients WHERE id=%s;", (int(patient_id),))

    def delete_all(self):
        if self.db_type == "sqlite":
            self.conn.execute("DELETE FROM patients;")
            self.conn.commit()
        else:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM patients;")

    def fetch_patients(self, search_text="", status_filter="All"):
        clauses = []
        params = []

        if search_text:
            like = f"%{search_text}%"
            if self.db_type == "sqlite":
                clauses.append("(name LIKE ? OR CAST(id AS TEXT) LIKE ?)")
                params.extend([like, like])
            else:
                clauses.append("(name ILIKE %s OR CAST(id AS TEXT) LIKE %s)")
                params.extend([like, like])

        if status_filter and status_filter != "All":
            if self.db_type == "sqlite":
                clauses.append("status = ?")
            else:
                clauses.append("status = %s")
            params.append(status_filter)

        where = " WHERE " + " AND ".join(clauses) if clauses else ""
        order = " ORDER BY updated_at DESC, id DESC"
        q = "SELECT id, name, status, last_updated_by, created_at, updated_at FROM patients" + where + order

        if self.db_type == "sqlite":
            cur = self.conn.execute(q, tuple(params))
            rows = cur.fetchall()
        else:
            cur = self.conn.cursor()
            cur.execute(q, tuple(params))
            rows = cur.fetchall()

        # Normalize to DataFrame
        df = pd.DataFrame(rows, columns=["ID", "Name", "Status", "LastUpdatedBy", "CreatedAt", "UpdatedAt"])
        return df

# -------------------------- Helpers --------------------------

def random_name():
    first = ["Alex","Blake","Casey","Drew","Evan","Finn","Gabe","Hayden","Ira","Jules","Kai","Lee","Maya","Nico","Owen","Parker","Quinn","Riley","Sage","Toni","Uma","Vince","Wren","Xan","Yael","Zoe"]
    last = ["Smith","Johnson","Lee","Brown","Garcia","Miller","Davis","Martinez","Wilson","Anderson","Taylor","Thomas","Moore","Jackson","White","Harris","Clark","Lewis","Young","Walker"]
    return f"{random.choice(first)} {random.choice(last)} {random.randint(1, 999)}"

def generate_sample_50(db: DB, role: str):
    # New randomized 50 every time
    for _ in range(50):
        db.add_patient(random_name(), role_default=role)

def add_uploaded_data(db: DB, file, how: str):
    """
    Load data from uploaded JSON/CSV/TXT and insert patients.
    JSON: list[ {name, status?} ] or {patients:[...]}; CSV: columns with 'name' or first column; TXT: names per line
    how: 'append' or 'replace'
    """
    if how == "replace":
        db.delete_all()

    name_rows = []

    if file.name.lower().endswith(".json"):
        import json
        obj = json.loads(file.read().decode("utf-8"))
        if isinstance(obj, dict) and "patients" in obj:
            records = obj["patients"]
        elif isinstance(obj, list):
            records = obj
        else:
            records = []
        for r in records:
            if isinstance(r, dict):
                nm = r.get("name") or r.get("Name")
            else:
                nm = str(r)
            if nm:
                name_rows.append((nm, r.get("status") if isinstance(r, dict) else None))
    elif file.name.lower().endswith(".csv"):
        df = pd.read_csv(file)
        name_col = None
        for cand in ["name", "Name", "patient", "Patient"]:
            if cand in df.columns:
                name_col = cand
                break
        if name_col is None:
            # fallback: first column
            name_col = df.columns[0]
        for _, row in df.iterrows():
            nm = str(row[name_col]).strip()
            st = row.get("status") if "status" in df.columns else row.get("Status")
            if nm:
                name_rows.append((nm, st if pd.notna(st) else None))
    else:
        # TXT
        for line in file.read().decode("utf-8").splitlines():
            nm = line.strip()
            if nm:
                name_rows.append((nm, None))

    for nm, stv in name_rows:
        # if status provided, use it; else default Waiting
        # We'll add with default role from sidebar
        db.add_patient(nm, role_default=st.session_state.get("current_role", ROLES[0]))
        if stv and stv in STATUSES:
            # update immediately
            # need the last inserted ID — easiest: fetch newest where name matches
            df = db.fetch_patients(search_text=nm, status_filter="All")
            if not df.empty:
                pid = int(df.iloc[0]["ID"])
                db.update_status(pid, stv, st.session_state.get("current_role", ROLES[0]))

def save_json_download(df: pd.DataFrame):
    data = {"patients": df.to_dict(orient="records")}
    import json
    payload = json.dumps(data, indent=2)
    st.download_button(
        "💾 Save JSON",
        data=payload,
        file_name=f"patients_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json",
        mime="application/json",
        use_container_width=True,
    )

# -------------------------- UI --------------------------

st.set_page_config(page_title=APP_TITLE, layout="wide")
st.title(APP_TITLE)

# Instantiate DB (1x) and keep it
if "db" not in st.session_state:
    st.session_state.db = DB()
db: DB = st.session_state.db

# Sidebar: info & controls
with st.sidebar:
    st.subheader("Settings")
    st.caption(f"Backend: **{db.db_type.upper()}**")
    st.session_state.current_role = st.selectbox("Active Role", ROLES, index=0)
    st.markdown("---")
    st.markdown("### Import Data")
    up_how = st.radio("On upload:", ["append", "replace"], horizontal=True)
    file = st.file_uploader("Upload JSON / CSV / TXT", type=["json","csv","txt"])
    if file and st.button("Import", type="primary", use_container_width=True):
        try:
            add_uploaded_data(db, file, up_how)
            st.success("Data imported")
        except Exception as e:
            st.error(f"Import failed: {e}")

# Toolbar
colA, colB, colC, colD, colE, colF = st.columns([1,1,1,1,1,2])

with colA:
    if st.button("➕ Add Patient", use_container_width=True):
        st.session_state.show_add = True
with colB:
    if st.button("🧪 Generate Sample (50)", type="primary", use_container_width=True):
        generate_sample_50(db, role=st.session_state.current_role)
        st.success("50 randomized patients added")
with colC:
    if st.button("🗑️ Clear All Records", use_container_width=True):
        db.delete_all()
        st.success("All records removed")
with colD:
    if st.button("🔄 Refresh", use_container_width=True):
        st.rerun()
with colE:
    pass
with colF:
    # Search + Status filter
    search = st.text_input("Search (name or ID)", value="", placeholder="Type to search...")
    status_filter = st.selectbox("Status Filter", ["All"] + STATUSES, index=0)

# Add patient modal-ish row
if st.session_state.get("show_add"):
    with st.form("add_form", border=True):
        nm = st.text_input("Patient Name", "")
        c1, c2 = st.columns([1,1])
        with c1:
            add_now = st.form_submit_button("Add", type="primary", use_container_width=True)
        with c2:
            cancel = st.form_submit_button("Cancel", use_container_width=True)
        if add_now:
            if nm.strip():
                db.add_patient(nm.strip(), role_default=st.session_state.current_role)
                st.success(f"Added: {nm.strip()}")
                st.session_state.show_add = False
            else:
                st.warning("Please enter a name")
        if cancel:
            st.session_state.show_add = False

# Fetch + display
df = db.fetch_patients(search_text=search, status_filter=status_filter)

# Selection column for actions
if not df.empty:
    df_display = df.copy()
    df_display.insert(0, "Select", False)
    edited = st.data_editor(
        df_display,
        use_container_width=True,
        height=520,
        key="editor",
        column_config={
            "Select": st.column_config.CheckboxColumn(required=False),
            "Status": st.column_config.SelectboxColumn(options=STATUSES),
        },
        disabled=["ID","CreatedAt","UpdatedAt","LastUpdatedBy"],  # allow editing Status visually; actions below apply
    )
else:
    st.info("No patients yet. Use **Add Patient** or **Generate Sample (50)**.")
    edited = df

# Action buttons for selected rows
if not df.empty:
    sel_mask = edited["Select"] == True
    selected_rows = edited[sel_mask]

    st.markdown("#### Actions on Selected")
    ac1, ac2, ac3, ac4 = st.columns(4)
    with ac1:
        if st.button("Set Waiting", use_container_width=True):
            for pid in selected_rows["ID"].tolist():
                db.update_status(pid, "Waiting", st.session_state.current_role)
            st.success(f"Updated {len(selected_rows)} -> Waiting")
            st.rerun()
    with ac2:
        if st.button("Set In Progress", use_container_width=True):
            for pid in selected_rows["ID"].tolist():
                db.update_status(pid, "In Progress", st.session_state.current_role)
            st.success(f"Updated {len(selected_rows)} -> In Progress")
            st.rerun()
    with ac3:
        if st.button("Set Completed", use_container_width=True):
            for pid in selected_rows["ID"].tolist():
                db.update_status(pid, "Completed", st.session_state.current_role)
            st.success(f"Updated {len(selected_rows)} -> Completed")
            st.rerun()
    with ac4:
        if st.button("Delete Selected", use_container_width=True):
            for pid in selected_rows["ID"].tolist():
                db.delete_patient(pid)
            st.success(f"Deleted {len(selected_rows)} record(s)")
            st.rerun()

# Save JSON
st.markdown("---")
save_json_download(df)

# Footer info
st.caption(f"Backend: **{db.db_type.upper()}** | Records: **{len(df)}**")
