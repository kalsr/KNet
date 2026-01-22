


# ============================================================
# F5 BIG-IP API POSTURE MANAGEMENT – ENTERPRISE DASHBOARD
# Designed by Randy Singh
# Kalsnet (KNet) Consulting Group
# ============================================================

import streamlit as st
import pandas as pd
import random
import time
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------
st.set_page_config(
    page_title="F5 BIG-IP API Posture Management",
    layout="wide"
)

# ------------------------------------------------------------
# RESET TOKEN (STREAMLIT-SAFE RESET)
# ------------------------------------------------------------
if "reset_token" not in st.session_state:
    st.session_state.reset_token = 0

def reset_all():
    plt.close("all")
    st.session_state.reset_token += 1
    st.rerun()

# ------------------------------------------------------------
# HEADER BANNER
# ------------------------------------------------------------
st.markdown(
    """
    <div style="background-color:#003366;padding:16px;border-radius:6px;margin-bottom:10px">
        <h2 style="color:white;text-align:center;margin:0;">
            API Posture Management Program
        </h2>
        <p style="color:white;text-align:center;margin:0;">
            Designed by Randy Singh – Kalsnet (KNet) Consulting Group
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------------------
# SYNTHETIC F5 BIG-IP DATA GENERATOR
# ------------------------------------------------------------
def generate_f5_bigip_records(num_records):
    apis = [
        "/api/v1/users", "/api/v1/products", "/api/v1/orders",
        "/api/v2/customers", "/api/v2/inventory", "/login", "/logout"
    ]
    status_codes = [200, 201, 204, 400, 401, 403, 404, 429, 500]

    records = []
    for _ in range(num_records):
        records.append({
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
            "src_ip": f"203.0.{random.randint(1,255)}.{random.randint(1,255)}",
            "dst_ip": f"192.168.{random.randint(0,1)}.{random.randint(1,255)}",
            "api": random.choice(apis),
            "status_code": random.choice(status_codes),
            "latency_ms": round(random.uniform(50, 2500), 1)
        })

    return pd.DataFrame(records)

# ------------------------------------------------------------
# POSTURE ANALYSIS
# ------------------------------------------------------------
def analyze_posture(df):
    posture = df.groupby("api").agg(
        hits=("api", "count"),
        failures=("status_code", lambda x: (x >= 400).sum()),
        avg_latency_ms=("latency_ms", "mean")
    ).reset_index()

    posture["Zero_Trust_Violation"] = posture["failures"] > 5
    return posture

# ------------------------------------------------------------
# THREAT SEVERITY + COMPLIANCE
# ------------------------------------------------------------
def threat_analysis(posture):
    findings = []

    for _, row in posture.iterrows():
        score = row["failures"] * 10 + row["avg_latency_ms"] / 50

        if score > 90:
            severity = "CRITICAL"
        elif score > 60:
            severity = "HIGH"
        elif score > 30:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        findings.append({
            "API": row["api"],
            "Severity": severity,
            "NIST": "SI-4, IA-7",
            "STIG": "SRG-APP-000516",
            "Zero Trust": "Continuous Verification"
        })

    return pd.DataFrame(findings)

# ------------------------------------------------------------
# PDF EXPORT (DoD BRIEFING)
# ------------------------------------------------------------
def export_pdf(threats_df):
    filename = "F5_API_Posture_DoD_Report.pdf"
    doc = SimpleDocTemplate(filename, pagesize=LETTER)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("F5 BIG-IP API Posture Assessment", styles["Title"]))
    elements.append(Spacer(1, 12))

    table_data = [list(threats_df.columns)] + threats_df.values.tolist()
    table = Table(table_data)
    elements.append(table)

    doc.build(elements)
    return filename

# ------------------------------------------------------------
# SIDEBAR CONTROLS
# ------------------------------------------------------------
st.sidebar.header("Simulation Controls")

record_count = st.sidebar.slider(
    "Synthetic API Records",
    0, 100, 50,
    key=f"slider_{st.session_state.reset_token}"
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Real F5 BIG-IP CSV",
    type=["csv"],
    key=f"upload_{st.session_state.reset_token}"
)

# ------------------------------------------------------------
# DATA SOURCE
# ------------------------------------------------------------
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Real F5 BIG-IP data loaded")
else:
    df = generate_f5_bigip_records(record_count)

# ------------------------------------------------------------
# DISPLAY SYNTHETIC / REAL DATA
# ------------------------------------------------------------
st.subheader("F5 BIG-IP API Traffic Records")
st.dataframe(df, use_container_width=True)

# ------------------------------------------------------------
# ANALYSIS
# ------------------------------------------------------------
posture = analyze_posture(df)
threats = threat_analysis(posture)

# ------------------------------------------------------------
# METRICS
# ------------------------------------------------------------
m1, m2, m3 = st.columns(3)
m1.metric("Total API Calls", len(df))
m2.metric("Unique APIs", df["api"].nunique())
m3.metric("Threat Findings", len(threats))

# ------------------------------------------------------------
# CHARTS
# ------------------------------------------------------------
st.subheader("HTTP Status Code Distribution")
fig1, ax1 = plt.subplots()
df["status_code"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax1)
ax1.set_ylabel("")
st.pyplot(fig1)

st.subheader("API Usage (Hits per Endpoint)")
fig2, ax2 = plt.subplots()
posture.set_index("api")["hits"].plot.bar(ax=ax2)
ax2.set_ylabel("Hits")
st.pyplot(fig2)

# ------------------------------------------------------------
# POSTURE & THREATS
# ------------------------------------------------------------
st.subheader("API Posture Summary")
st.dataframe(posture, use_container_width=True)

st.subheader("Threat Severity & Compliance Mapping")
st.dataframe(threats, use_container_width=True)

# ------------------------------------------------------------
# PDF EXPORT
# ------------------------------------------------------------
if st.button("📄 Export DoD PDF Report"):
    pdf = export_pdf(threats)
    with open(pdf, "rb") as f:
        st.download_button("Download Report", f, file_name=pdf)

# ------------------------------------------------------------
# RESET BUTTON
# ------------------------------------------------------------
st.markdown(
    """
    <style>
    div.stButton > button {
        background-color:#cc0000;
        color:white;
        font-size:18px;
        height:48px;
        width:100%;
        border-radius:6px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("RESET ALL DATA"):
    reset_all()
