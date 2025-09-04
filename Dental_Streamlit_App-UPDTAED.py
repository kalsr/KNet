

### `dental_app_streamlit.py` (complete, fixed)
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
# THIS APPLICATION IS DEVELOPED BY RANDY SINGH FROM KNet CONSULTING GROUP

import os
import sqlite3
from datetime import datetime
import random
import pandas as pd
import streamlit as st

# optional Postgres
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

    fname = file.name.lower()
    content_bytes = file.read()  # bytes
    # ensure we can parse multiple times - decode to text
    try:
        text = content_bytes.decode("utf-8")
    except Exception:
        text = content_bytes.decode("latin-1")

    if fname.endswith(".json"):
        import json as _json
        obj = _json.loads(text)
        if isinstance(obj, dict) and "patients" in obj:
            records = obj["patients"]
        elif isinstance(obj, list):
            records = obj
        else:
            records = []
        for r in records:
            if isinstance(r, dict):
                nm = r.get("name") or r.get("Name")
                status_val = r.get("status") or r.get("Status")
            else:
                nm = str(r)
                status_val = None
            if nm:
                name_rows.append((nm, status_val))
    elif fname.endswith(".csv"):
        # read via pandas from the decoded text buffer
        from io import StringIO
        df_buf = pd.read_csv(StringIO(text))
        name_col = None
        for cand in ["name", "Name", "patient", "Patient"]:
            if cand in df_buf.columns:
                name_col = cand
                break
        if name_col is None:
            # fallback: first column
            name_col = df_buf.columns[0]
        status_col = None
        for cand in ["status", "Status"]:
            if cand in df_buf.columns:
                status_col = cand
                break
        for _, row in df_buf.iterrows():
            nm = str(row[name_col]).strip()
            status_val = row[status_col] if status_col is not None else None
            if pd.notna(status_val):
                status_val = str(status_val).strip()
            else:
                status_val = None
            if nm:
                name_rows.append((nm, status_val))
    else:
        # TXT - one name per line
        for line in text.splitlines():
            nm = line.strip()
            if nm:
                name_rows.append((nm, None))

    # insert rows
    for nm, status_val in name_rows:
        db.add_patient(nm, role_default=st.session_state.get("current_role", ROLES[0]))
        if status_val and status_val in STATUSES:
            # attempt to find newest inserted matching name (best-effort)
            df = db.fetch_patients(search_text=nm, status_filter="All")
            if not df.empty:
                pid = int(df.iloc[0]["ID"])
                db.update_status(pid, status_val, st.session_state.get("current_role", ROLES[0]))

def save_json_download(df: pd.DataFrame):
    data = {"patients": df.to_dict(orient="records")}
    import json as _json
    payload = _json.dumps(data, indent=2)
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

# Put the whole app on a single page; styled separators and clear buttons
st.markdown(
    """
    <style>
    .big-btn { font-size:15px; padding:10px 12px; border-radius:8px; }
    .primary { background:#0d6efd; color:white; }
    .success { background:#198754; color:white; }
    .warn { background:#ffc107; color:#1a1a1a; }
    .danger { background:#dc3545; color:white; }
    .muted { color:#6c757d; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar: info & controls (import)
with st.sidebar:
    st.subheader("Settings & Import")
    st.caption(f"Backend: **{db.db_type.upper()}**")
    # keep current role in session_state
    if "current_role" not in st.session_state:
        st.session_state.current_role = ROLES[0]
    st.session_state.current_role = st.selectbox("Active Role", ROLES, index=ROLES.index(st.session_state.current_role))
    st.markdown("---")
    st.markdown("### Import Data")
    up_how = st.radio("On upload:", ["append", "replace"])
    uploaded_file = st.file_uploader("Upload JSON / CSV / TXT", type=["json", "csv", "txt"])
    if uploaded_file:
        if st.button("Import Upload", use_container_width=True):
            try:
                add_uploaded_data(db, uploaded_file, up_how)
                st.success("Data imported successfully.")
            except Exception as e:
                st.error(f"Import failed: {e}")

# Top toolbar (full-width)
colA, colB, colC, colD, colE, colF = st.columns([1.4,1.4,1.4,1.4,1.6,3.0])

with colA:
    if st.button("➕ Add Patient", key="btn_add", use_container_width=True):
        st.session_state.show_add = True
with colB:
    if st.button("🧪 Generate Sample (50)", key="btn_sample", use_container_width=True):
        generate_sample_50(db, role=st.session_state.current_role)
        st.success("50 randomized patients added")
with colC:
    if st.button("🗑️ Clear All Records", key="btn_clear", use_container_width=True):
        db.delete_all()
        st.success("All records removed")
with colD:
    if st.button("🔄 Refresh", key="btn_refresh", use_container_width=True):
        # simple refresh
        st.experimental_rerun()
with colE:
    # Save/Export quick buttons
    if st.button("⬇️ Export CSV (All)", key="btn_export", use_container_width=True):
        df_all = db.fetch_patients(search_text="", status_filter="All")
        csv_bytes = df_all.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", data=csv_bytes, file_name=f"patients_all_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv", mime="text/csv")
with colF:
    # Search + Status filter
    search = st.text_input("Search (name or ID)", value="", placeholder="Type to search...", key="search_input")
    status_filter = st.selectbox("Status Filter", ["All"] + STATUSES, index=0)

st.markdown("---")

# Add patient form (modal-like)
if st.session_state.get("show_add"):
    with st.form("add_form"):
        nm = st.text_input("Patient Name", "")
        submitted = st.form_submit_button("Add Patient")
        cancelled = st.form_submit_button("Cancel")
        if submitted:
            if nm.strip():
                db.add_patient(nm.strip(), role_default=st.session_state.current_role)
                st.success(f"Added: {nm.strip()}")
                st.session_state.show_add = False
                # refresh view
                st.experimental_rerun()
            else:
                st.warning("Please enter a name")
        if cancelled:
            st.session_state.show_add = False

# Fetch records and display table (with checkbox selection via st.data_editor)
df = db.fetch_patients(search_text=search, status_filter=status_filter)

if df.empty:
    st.info("No patients yet. Use **Add Patient** or **Generate Sample (50)** or import a file.")
else:
    # insert selection column
    df_display = df.copy()
    df_display.insert(0, "Select", False)

    # show editable table allowing checkboxes and quick Status editing (visual only)
    edited = st.data_editor(
        df_display,
        use_container_width=True,
        height=480,
        key="editor",
        column_config={
            "Select": st.column_config.CheckboxColumn(required=False),
            "Status": st.column_config.SelectboxColumn(options=STATUSES),
        },
        disabled=["ID", "CreatedAt", "UpdatedAt", "LastUpdatedBy"],
    )

    # Actions for selected rows
    sel_mask = edited["Select"] == True
    selected_rows = edited[sel_mask]
    n_selected = len(selected_rows)

    st.markdown(f"**Selected:** {n_selected} record(s)")
    ac1, ac2, ac3, ac4 = st.columns([1,1,1,1])
    with ac1:
        if st.button("Set Waiting", key="act_wait"):
            pids = selected_rows["ID"].tolist()
            for pid in pids:
                db.update_status(pid, "Waiting", st.session_state.current_role)
            st.success(f"Updated {len(pids)} -> Waiting")
            st.experimental_rerun()
    with ac2:
        if st.button("Set In Progress", key="act_prog"):
            pids = selected_rows["ID"].tolist()
            for pid in pids:
                db.update_status(pid, "In Progress", st.session_state.current_role)
            st.success(f"Updated {len(pids)} -> In Progress")
            st.experimental_rerun()
    with ac3:
        if st.button("Set Completed", key="act_comp"):
            pids = selected_rows["ID"].tolist()
            for pid in pids:
                db.update_status(pid, "Completed", st.session_state.current_role)
            st.success(f"Updated {len(pids)} -> Completed")
            st.experimental_rerun()
    with ac4:
        if st.button("Delete Selected", key="act_del"):
            pids = selected_rows["ID"].tolist()
            for pid in pids:
                db.delete_patient(pid)
            st.success(f"Deleted {len(pids)} record(s)")
            st.experimental_rerun()

# Divider and download/save
st.markdown("---")
save_json_download(df)

# Footer info and quick stats
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Backend", db.db_type.upper())
with col2:
    st.metric("Records", len(df))
with col3:
    # show sample status distribution
    if not df.empty:
        dist = df["Status"].value_counts().to_dict()
        st.metric("Waiting / InProgress /Completed", f"{dist.get('Waiting',0)} / {dist.get('In Progress',0)} / {dist.get('Completed',0)}")
    else:
        st.metric("Waiting / InProgress /Completed", "0 / 0 / 0")

st.caption("Tip: Import files (JSON/CSV/TXT) from the sidebar. JSON should be a list or {patients:[...]} with 'name' and optional 'status'.")
