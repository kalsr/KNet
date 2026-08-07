# Hospital Patient Portal — Backend API
# Developed by Randy Singh | Kalsnet (KNet) Consulting


import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Configuration — toggle to a real hospital system by setting env vars
# ---------------------------------------------------------------------------
HOSPITAL_API_BASE_URL = os.getenv("HOSPITAL_API_BASE_URL", "")  # e.g. real FHIR server
HOSPITAL_API_KEY = os.getenv("HOSPITAL_API_KEY", "")
DB_PATH = os.path.join(os.path.dirname(__file__), "hospital_demo.db")


def use_live_upstream() -> bool:
    """Returns True if this deployment is configured to talk to a real
    hospital system rather than the local demo database."""
    return bool(HOSPITAL_API_BASE_URL)


# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------
app = FastAPI(
    title="Hospital Patient Portal API",
    description="Demo backend by Randy Singh — Kalsnet (KNet) Consulting",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten this to your Streamlit domain in production
    allow_methods=["*"],
    allow_headers=["*"],
)


@contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    with get_db() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY,
                first_name TEXT, last_name TEXT, dob TEXT,
                gender TEXT, phone TEXT, email TEXT,
                primary_doctor TEXT, insurance TEXT
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER, doctor TEXT, department TEXT,
                appointment_date TEXT, appointment_time TEXT,
                reason TEXT, status TEXT DEFAULT 'Scheduled',
                created_at TEXT
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS lab_results (
                id INTEGER PRIMARY KEY,
                patient_id INTEGER, test_name TEXT, result TEXT,
                unit TEXT, reference_range TEXT, status TEXT,
                collected_date TEXT, ordering_doctor TEXT
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS prescriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER, medication TEXT, dosage TEXT,
                frequency TEXT, doctor TEXT, notes TEXT,
                prescribed_date TEXT, status TEXT DEFAULT 'Active'
            )
        """)

        # Seed demo data only once
        c.execute("SELECT COUNT(*) FROM patients")
        if c.fetchone()[0] == 0:
            c.executemany(
                "INSERT INTO patients VALUES (?,?,?,?,?,?,?,?,?)",
                [
                    (101, "Emily", "Carter", "1985-03-14", "Female",
                     "555-201-4432", "emily.carter@mail.com", "Dr. Nathan Wu", "BlueShield PPO"),
                    (102, "Marcus", "Alvarez", "1972-11-02", "Male",
                     "555-330-9981", "marcus.alvarez@mail.com", "Dr. Sarah Kim", "Aetna HMO"),
                    (103, "Priya", "Desai", "1990-07-22", "Female",
                     "555-118-2245", "priya.desai@mail.com", "Dr. Nathan Wu", "United Healthcare"),
                    (104, "Liam", "O'Connor", "1963-01-30", "Male",
                     "555-772-6610", "liam.oconnor@mail.com", "Dr. James Reyes", "Medicare"),
                    (105, "Sofia", "Nguyen", "2001-09-09", "Female",
                     "555-499-3327", "sofia.nguyen@mail.com", "Dr. Sarah Kim", "Cigna PPO"),
                ],
            )
            c.executemany(
                "INSERT INTO lab_results VALUES (?,?,?,?,?,?,?,?,?)",
                [
                    (1, 101, "Hemoglobin A1c", "5.6", "%", "4.0 - 5.6", "Normal", "2026-07-10", "Dr. Nathan Wu"),
                    (2, 101, "Total Cholesterol", "212", "mg/dL", "<200", "High", "2026-07-10", "Dr. Nathan Wu"),
                    (3, 102, "Blood Glucose (Fasting)", "138", "mg/dL", "70 - 99", "High", "2026-07-15", "Dr. Sarah Kim"),
                    (4, 103, "White Blood Cell Count", "6.8", "10^3/uL", "4.5 - 11.0", "Normal", "2026-07-18", "Dr. Nathan Wu"),
                    (5, 104, "Creatinine", "1.4", "mg/dL", "0.6 - 1.3", "High", "2026-07-20", "Dr. James Reyes"),
                    (6, 105, "Vitamin D, 25-Hydroxy", "22", "ng/mL", "30 - 100", "Low", "2026-07-22", "Dr. Sarah Kim"),
                ],
            )

        conn.commit()


init_db()


# ---------------------------------------------------------------------------
# Schemas
# ---------------------------------------------------------------------------
class Patient(BaseModel):
    id: int
    first_name: str
    last_name: str
    dob: str
    gender: str
    phone: str
    email: str
    primary_doctor: str
    insurance: str


class AppointmentIn(BaseModel):
    patient_id: int = Field(..., description="ID of the patient booking the appointment")
    doctor: str
    department: str
    appointment_date: str = Field(..., description="YYYY-MM-DD")
    appointment_time: str = Field(..., description="HH:MM, 24hr")
    reason: str


class AppointmentOut(AppointmentIn):
    id: int
    status: str
    created_at: str


class LabResult(BaseModel):
    id: int
    patient_id: int
    test_name: str
    result: str
    unit: str
    reference_range: str
    status: str
    collected_date: str
    ordering_doctor: str


class PrescriptionIn(BaseModel):
    patient_id: int
    medication: str
    dosage: str
    frequency: str
    doctor: str
    notes: Optional[str] = ""


class PrescriptionOut(PrescriptionIn):
    id: int
    prescribed_date: str
    status: str


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.get("/", tags=["Health"])
def root():
    return {
        "service": "Hospital Patient Portal API",
        "developer": "Randy Singh — Kalsnet (KNet) Consulting",
        "live_upstream_configured": use_live_upstream(),
    }


@app.get("/patients", response_model=List[Patient], tags=["Patients"])
def get_patients(search: Optional[str] = Query(None, description="Filter by last name")):
    """Retrieve all patients, optionally filtered by last name."""
    with get_db() as conn:
        c = conn.cursor()
        if search:
            c.execute("SELECT * FROM patients WHERE last_name LIKE ?", (f"%{search}%",))
        else:
            c.execute("SELECT * FROM patients")
        rows = c.fetchall()
    return [dict(r) for r in rows]


@app.post("/appointments", response_model=AppointmentOut, tags=["Appointments"])
def create_appointment(appt: AppointmentIn):
    """Book a new appointment for a patient."""
    with get_db() as conn:
        c = conn.cursor()
        c.execute("SELECT id FROM patients WHERE id = ?", (appt.patient_id,))
        if not c.fetchone():
            raise HTTPException(status_code=404, detail="Patient not found")

        created_at = datetime.now().isoformat(timespec="seconds")
        c.execute(
            """INSERT INTO appointments
               (patient_id, doctor, department, appointment_date, appointment_time, reason, status, created_at)
               VALUES (?,?,?,?,?,?, 'Scheduled', ?)""",
            (appt.patient_id, appt.doctor, appt.department, appt.appointment_date,
             appt.appointment_time, appt.reason, created_at),
        )
        new_id = c.lastrowid

    return AppointmentOut(**appt.dict(), id=new_id, status="Scheduled", created_at=created_at)


@app.get("/labresults", response_model=List[LabResult], tags=["Lab Results"])
def get_lab_results(patient_id: Optional[int] = Query(None, description="Filter by patient ID")):
    """Retrieve lab results, optionally filtered by patient."""
    with get_db() as conn:
        c = conn.cursor()
        if patient_id:
            c.execute("SELECT * FROM lab_results WHERE patient_id = ?", (patient_id,))
        else:
            c.execute("SELECT * FROM lab_results")
        rows = c.fetchall()
    return [dict(r) for r in rows]


@app.post("/prescriptions", response_model=PrescriptionOut, tags=["Prescriptions"])
def create_prescription(rx: PrescriptionIn):
    """Issue a new prescription for a patient."""
    with get_db() as conn:
        c = conn.cursor()
        c.execute("SELECT id FROM patients WHERE id = ?", (rx.patient_id,))
        if not c.fetchone():
            raise HTTPException(status_code=404, detail="Patient not found")

        prescribed_date = datetime.now().strftime("%Y-%m-%d")
        c.execute(
            """INSERT INTO prescriptions
               (patient_id, medication, dosage, frequency, doctor, notes, prescribed_date, status)
               VALUES (?,?,?,?,?,?,?, 'Active')""",
            (rx.patient_id, rx.medication, rx.dosage, rx.frequency, rx.doctor, rx.notes, prescribed_date),
        )
        new_id = c.lastrowid

    return PrescriptionOut(**rx.dict(), id=new_id, prescribed_date=prescribed_date, status="Active")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
