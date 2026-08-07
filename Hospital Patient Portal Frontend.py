# Hospital Patient Portal — Streamlit Frontend
# Developed by Randy Singh | Kalsnet (KNet) Consulting

# Run alongside the FastAPI backend (backend/main.py):
    # uvicorn backend.main:app --reload
    # streamlit run frontend/app.py


import requests
import streamlit as st
import pandas as pd

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Hospital Patient Portal | Kalsnet Consulting",
    page_icon="🏥",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Styling — clinical blue / teal palette
# ---------------------------------------------------------------------------
PRIMARY_BLUE = "#0B3D91"
ACCENT_TEAL = "#0FA3A3"
BG_SOFT = "#F4F8FB"

st.markdown(f"""
<style>
    .stApp {{ background-color: {BG_SOFT}; }}
    .knet-title {{
        color: {PRIMARY_BLUE};
        font-weight: 800;
        font-size: 2.4rem;
        margin-bottom: 0;
    }}
    .knet-subtitle {{
        color: {ACCENT_TEAL};
        font-weight: 600;
        font-size: 1rem;
        margin-top: 0;
    }}
    .stTabs [data-baseweb="tab"] {{
        font-weight: 600;
        color: {PRIMARY_BLUE};
    }}
    div[data-testid="stMetricValue"] {{ color: {PRIMARY_BLUE}; }}
    .stButton>button {{
        background-color: {PRIMARY_BLUE};
        color: white;
        border-radius: 6px;
        font-weight: 600;
        border: none;
    }}
    .stButton>button:hover {{
        background-color: {ACCENT_TEAL};
        color: white;
    }}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Sidebar — connection settings (demo vs. real hospital system)
# ---------------------------------------------------------------------------
st.sidebar.header("⚙️ Connection Settings")
mode = st.sidebar.radio(
    "Data source",
    ["Demo API (local FastAPI)", "Live Hospital Patient Portal"],
    help="Switch to 'Live' to point this GUI at a real hospital EHR/FHIR endpoint.",
)

if mode == "Demo API (local FastAPI)":
    api_base = st.sidebar.text_input("API Base URL", value="http://localhost:8000")
    api_key = None
else:
    api_base = st.sidebar.text_input("Hospital API / FHIR Base URL", value="https://fhir.yourhospital.org/api/v1")
    api_key = st.sidebar.text_input("API Key / Bearer Token", type="password")
    st.sidebar.info(
        "In live mode, requests are sent with an `Authorization: Bearer` header "
        "to your hospital's SMART-on-FHIR gateway. No patient data is stored by this app."
    )

st.sidebar.markdown("---")
st.sidebar.caption("Kalsnet (KNet) Consulting © 2026")


def headers():
    return {"Authorization": f"Bearer {api_key}"} if api_key else {}


# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.markdown('<p class="knet-title">🏥 Hospital Patient Portal</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="knet-subtitle">Developed by Randy Singh · Kalsnet (KNet) Consulting</p>',
    unsafe_allow_html=True,
)
st.divider()

tab1, tab2, tab3, tab4 = st.tabs(
    ["👤 Patients", "📅 Book Appointment", "🧪 Lab Results", "💊 Prescriptions"]
)

# ---------------------------------------------------------------------------
# TAB 1 — GET /patients
# ---------------------------------------------------------------------------
with tab1:
    st.subheader("Patient Directory")
    col_a, col_b = st.columns([3, 1])
    with col_a:
        search = st.text_input("Search by last name", placeholder="e.g. Carter")
    with col_b:
        st.write("")
        st.write("")
        fetch_patients = st.button("🔍 Fetch Patients (GET)")

    if fetch_patients or "patients_df" not in st.session_state:
        try:
            params = {"search": search} if search else {}
            r = requests.get(f"{api_base}/patients", params=params, headers=headers(), timeout=8)
            r.raise_for_status()
            df = pd.DataFrame(r.json())
            st.session_state["patients_df"] = df
        except Exception as e:
            st.error(f"Could not reach API at {api_base}. ({e})")
            df = pd.DataFrame()
    else:
        df = st.session_state["patients_df"]

    if not df.empty:
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Patients", len(df))
        c2.metric("Unique Physicians", df["primary_doctor"].nunique() if "primary_doctor" in df else 0)
        c3.metric("Insurance Plans", df["insurance"].nunique() if "insurance" in df else 0)
        st.dataframe(df, use_container_width=True, hide_index=True)

# ---------------------------------------------------------------------------
# TAB 2 — POST /appointments
# ---------------------------------------------------------------------------
with tab2:
    st.subheader("Book a New Appointment")
    with st.form("appt_form"):
        c1, c2 = st.columns(2)
        patient_id = c1.number_input("Patient ID", min_value=1, step=1, value=101)
        doctor = c2.text_input("Doctor", value="Dr. Nathan Wu")
        c3, c4 = st.columns(2)
        department = c3.selectbox("Department", ["Cardiology", "Endocrinology", "General Medicine", "Nephrology", "Dermatology"])
        appt_date = c4.date_input("Appointment Date")
        c5, c6 = st.columns(2)
        appt_time = c5.time_input("Appointment Time")
        reason = c6.text_input("Reason for Visit", value="Routine follow-up")

        submitted = st.form_submit_button("📅 Book Appointment (POST)")

    if submitted:
        payload = {
            "patient_id": int(patient_id),
            "doctor": doctor,
            "department": department,
            "appointment_date": str(appt_date),
            "appointment_time": appt_time.strftime("%H:%M"),
            "reason": reason,
        }
        try:
            r = requests.post(f"{api_base}/appointments", json=payload, headers=headers(), timeout=8)
            r.raise_for_status()
            st.success("✅ Appointment booked successfully!")
            st.json(r.json())
        except Exception as e:
            st.error(f"Booking failed: {e}")

# ---------------------------------------------------------------------------
# TAB 3 — GET /labresults
# ---------------------------------------------------------------------------
with tab3:
    st.subheader("Lab Results")
    filter_id = st.number_input("Filter by Patient ID (0 = show all)", min_value=0, step=1, value=0)
    if st.button("🔍 Fetch Lab Results (GET)"):
        try:
            params = {"patient_id": filter_id} if filter_id else {}
            r = requests.get(f"{api_base}/labresults", params=params, headers=headers(), timeout=8)
            r.raise_for_status()
            df = pd.DataFrame(r.json())
            if not df.empty:
                def highlight(row):
                    color = "#ffe1e1" if row["status"] == "High" else ("#fff6d6" if row["status"] == "Low" else "#e4f8ec")
                    return [f"background-color: {color}"] * len(row)
                st.dataframe(df.style.apply(highlight, axis=1), use_container_width=True, hide_index=True)
            else:
                st.info("No lab results found.")
        except Exception as e:
            st.error(f"Could not reach API at {api_base}. ({e})")

# ---------------------------------------------------------------------------
# TAB 4 — POST /prescriptions
# ---------------------------------------------------------------------------
with tab4:
    st.subheader("Issue a New Prescription")
    with st.form("rx_form"):
        c1, c2 = st.columns(2)
        rx_patient_id = c1.number_input("Patient ID ", min_value=1, step=1, value=102)
        rx_doctor = c2.text_input("Prescribing Doctor", value="Dr. Sarah Kim")
        c3, c4, c5 = st.columns(3)
        medication = c3.text_input("Medication", value="Metformin")
        dosage = c4.text_input("Dosage", value="500mg")
        frequency = c5.selectbox("Frequency", ["Once daily", "Twice daily", "Three times daily", "As needed"])
        notes = st.text_area("Notes", value="Take with food.")

        rx_submitted = st.form_submit_button("💊 Issue Prescription (POST)")

    if rx_submitted:
        payload = {
            "patient_id": int(rx_patient_id),
            "medication": medication,
            "dosage": dosage,
            "frequency": frequency,
            "doctor": rx_doctor,
            "notes": notes,
        }
        try:
            r = requests.post(f"{api_base}/prescriptions", json=payload, headers=headers(), timeout=8)
            r.raise_for_status()
            st.success("✅ Prescription issued successfully!")
            st.json(r.json())
        except Exception as e:
            st.error(f"Prescription submission failed: {e}")

st.divider()
st.caption("Hospital Patient Portal — Demo Use Case · Built with FastAPI + Streamlit · Randy Singh, Kalsnet (KNet) Consulting")
