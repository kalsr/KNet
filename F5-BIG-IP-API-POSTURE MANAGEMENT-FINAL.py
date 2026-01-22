


# ============================================================
# F5 BIG-IP API POSTURE MANAGEMENT – ENTERPRISE STREAMLIT
# Designed by Randy Singh
# Kalsnet (KNet) Consulting Group
# ============================================================

import streamlit as st
import pandas as pd
import random
import time
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="F5 BIG-IP API Posture Management", layout="wide")

# -------------------------------
# SESSION RESET COUNTER (KEY FIX)
# -------------------------------
if "reset_counter" not in st.session_state:
    st.session_state.reset_counter = 0

# -------------------------------
# TOP BLUE BANNER
# -------------------------------
st.markdown(
    """
    <div style="background-color:#003366;padding:15px;border-radius:5px">
        <h2 style="color:white;text-align:center;">
            API Posture Management Program<br>
            Designed by Randy Singh – Kalsnet (KNet) Consulting Group
        </h2>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# RESET FUNCTION (STREAMLIT SAFE)
# -------------------------------
def reset_all():
    plt.close("all")
    st.session_state.reset_counter += 1
    st.rerun()

# -------------------------------
# SYNTHETIC F5 DATA GENERATOR
# -------------------------------
def generate_f5_bigip_records(num_records):
    apis = [
        '/api/v1/users', '/api/v1/products', '/api/v1/orders',
        '/api/v2/customers', '/api/v2/inventory', '/login', '/logout'
    ]
    status_codes = [200, 201, 204, 400, 401, 403, 404, 429, 500]

    data = []
    for _ in range(num_records):
        data.append({
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()),
            "src_ip": f"203.0.{random.randint(1,255)}.{random.randint(1,255)}",
            "api": random.choice(apis),
            "status_code": random.choice(status_codes),
            "latency": round(random.uniform(0.1, 2.5), 3)
        })

    return pd.DataFrame(data)

# -------------------------------
# POSTURE + ZERO TRUST ANALYSIS
# -------------------------------
def analyze_posture(df):
    posture = df.groupby("api").agg(
        hits=("api", "count"),
        failures=("status_code", lambda x: (x >= 400).sum()),
        avg_latency=("latency", "mean")
    ).reset_index()

    posture["zero_trust_violation"] = posture["failures"] > 5
    return posture

# -------------------------------
# THREAT SCORING + COMPLIANCE
# -------------------------------
def threat_scoring(posture):
    threats = []

    for _, row in posture.iterrows():
        score = row["failures"] * 10 + int(row["avg_latency"] * 10)

        if score > 80:
            severity = "CRITICAL"
        elif score > 50:
            severity = "HIGH"
        elif score > 30:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        threats.append({
            "API": row["api"],
            "Severity": severity,
            "NIST": "SI-4 / IA-7",
            "STIG": "SRG-APP-000516",
            "Zero Trust": "Continuous Verification"
        })

    return pd.DataFrame(threats)

# -------------------------------
# PDF EXPORT (DOD BRIEFING)
# -------------------------------
def generate_pdf(threats_df):
    file_name = "F5_API_Posture_DoD_Report.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=LETTER)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("F5 BIG-IP API Posture Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    for _, row in threats_df.iterrows():
        elements.append(
            Paragraph(
                f"<b>{row['API']}</b> | Severity: {row['Severity']}<br/>"
                f"NIST: {row['NIST']} | STIG: {row['STIG']} | Zero Trust: {row['Zero Trust']}",
                styles["Normal"]
            )
        )
        elements.append(Spacer(1, 8))

    doc.build(elements)
    return file_name

# -------------------------------
# SIDEBAR CONTROLS
# -------------------------------
st.sidebar.header("Controls")

record_count = st.sidebar.slider(
    "Generate Synthetic F5 Records",
    0, 100, 50,
    key=f"slider_{st.session_state.reset_counter}"
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Real F5 BIG-IP CSV Data",
    type=["csv"],
    key=f"uploader_{st.session_state.reset_counter}"
)

# -------------------------------
# DATA SELECTION
# -------------------------------
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = generate_f5_bigip_records(record_count)

# -------------------------------
# ANALYSIS
# -------------------------------
posture = analyze_posture(df)
threats_df = threat_scoring(posture)

# -------------------------------
# DASHBOARD
# -------------------------------
st.subheader("API Posture Summary")
st.dataframe(posture)

st.subheader("Threat Severity & Compliance Mapping")
st.dataframe(threats_df)

# -------------------------------
# CHART
# -------------------------------
st.subheader("Threat Severity Distribution")
fig, ax = plt.subplots()
threats_df["Severity"].value_counts().plot.bar(ax=ax)
st.pyplot(fig)

# -------------------------------
# PDF EXPORT
# -------------------------------
if st.button("📄 Export DoD PDF Report"):
    pdf = generate_pdf(threats_df)
    with open(pdf, "rb") as f:
        st.download_button("Download Report", f, file_name=pdf)

# -------------------------------
# RESET BUTTON
# -------------------------------
st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: red;
        color: white;
        font-size: 18px;
        height: 50px;
        width: 100%;
        border-radius: 6px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("RESET ALL DATA"):
    reset_all()
