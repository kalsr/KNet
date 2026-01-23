

# ============================================================
# API RUNTIME & POSTURE MANAGEMENT PLATFORM
# F5 BIG-IP Schema | NIST | STIG | MITRE ATT&CK | Zero Trust
# Designed by Randy Singh
# Kalsnet (KNet) Consulting Group
# ============================================================

import streamlit as st
import pandas as pd
import random
import time
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from io import BytesIO

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(page_title="API Runtime & Posture Management", layout="wide")

# ------------------------------
# HEADER
# ------------------------------
st.markdown("""
<div style="background-color:#003366;padding:15px;border-radius:5px">
    <h2 style="color:white;text-align:center;">
    API Runtime & Posture Management Platform<br>
    <span style="font-size:16px;">Designed by Randy Singh | Kalsnet (KNet) Consulting Group</span>
    </h2>
</div>
""", unsafe_allow_html=True)

# ------------------------------
# SESSION STATE INIT
# ------------------------------
if "data" not in st.session_state:
    st.session_state.data = None
if "analysis" not in st.session_state:
    st.session_state.analysis = None
if "view_mode" not in st.session_state:
    st.session_state.view_mode = "Executive"

# ------------------------------
# RESET FUNCTION
# ------------------------------
def reset_all():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# ------------------------------
# SYNTHETIC DATA GENERATOR (F5 BIG-IP STYLE)
# ------------------------------
def generate_f5_runtime_data(num_records):
    apis = [
        "/api/v1/users","/api/v1/orders","/api/v1/products",
        "/login","/logout","/api/v2/inventory"
    ]
    records = []
    for _ in range(num_records):
        response_time = random.uniform(100,300)
        if random.random() < 0.15:
            response_time = random.uniform(500,1200)
        records.append({
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "src_ip": f"203.0.{random.randint(1,255)}.{random.randint(1,255)}",
            "dst_ip": f"192.168.{random.randint(0,1)}.{random.randint(1,255)}",
            "api": random.choice(apis),
            "status_code": random.choice([200,201,204,400,401,403,404,500]),
            "response_time_ms": round(response_time,2),
        })
    return pd.DataFrame(records)

# ------------------------------
# ANALYSIS ENGINE
# ------------------------------
def analyze_api_behavior(df):
    threshold = 400
    analysis = (
        df.groupby("api")
        .agg(
            total_requests=("response_time_ms","count"),
            avg_response_time=("response_time_ms","mean"),
            anomalies=("response_time_ms", lambda x: (x>=threshold).sum()),
            errors=("status_code", lambda x: (x>=400).sum()),
        ).reset_index()
    )
    analysis["anomaly_percent"] = (analysis["anomalies"]/analysis["total_requests"])*100
    analysis["severity"] = analysis["anomaly_percent"].apply(
        lambda x: "Critical" if x>25 else "High" if x>15 else "Medium" if x>5 else "Low"
    )
    # Zero Trust trust-score: 0-100 based on anomaly %
    analysis["zero_trust_score"] = 100 - analysis["anomaly_percent"]
    # NIST / STIG mapping
    analysis["NIST_Control"] = "SI-4 / RA-5 / AC-7"
    analysis["STIG_ID"] = "SRG-APP-000516"
    # MITRE ATT&CK example mapping
    analysis["MITRE_Technique"] = "T1071 / T1486 / T1210"
    return analysis

# ------------------------------
# PDF EXPORT FUNCTION
# ------------------------------
def export_pdf(df):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=LETTER)
    styles = getSampleStyleSheet()
    elements = [Paragraph("<b>API Runtime & Posture Report (DoD ATO)</b>", styles["Title"])]
    elements.append(Spacer(1,12))
    # Table for executive summary
    table_data = [df.columns.tolist()] + df.values.tolist()
    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.grey),
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("ALIGN",(1,1),(-1,-1),"CENTER")
    ]))
    elements.append(table)
    doc.build(elements)
    buffer.seek(0)
    return buffer

# ------------------------------
# SIDEBAR CONTROLS
# ------------------------------
st.sidebar.header("Controls")
record_count = st.sidebar.slider("Synthetic Record Count",0,100,50)
uploaded_file = st.sidebar.file_uploader("Upload Real F5 BIG-IP CSV Data", type=["csv"])
st.sidebar.markdown("### View Mode")
view_mode = st.sidebar.radio("Select view:", ["Executive","SOC","Engineer"], index=0)
st.session_state.view_mode = view_mode
if st.sidebar.button("🔴 RESET ALL DATA"):
    reset_all()

# ------------------------------
# DATA LOAD
# ------------------------------
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state.data = df
elif st.session_state.data is None:
    st.session_state.data = generate_f5_runtime_data(record_count)

df = st.session_state.data
analysis = analyze_api_behavior(df)
st.session_state.analysis = analysis

# ------------------------------
# DASHBOARD DISPLAY
# ------------------------------
st.subheader("API Runtime & Discovery Summary")
if view_mode=="Executive":
    st.dataframe(analysis[["api","total_requests","avg_response_time","anomalies","severity","zero_trust_score"]])
elif view_mode=="SOC":
    st.dataframe(analysis[["api","status_code","errors","anomalies","severity","MITRE_Technique"]])
else:
    st.dataframe(analysis)

# ------------------------------
# HEATMAP
# ------------------------------
st.subheader("API Risk Heatmap")
heatmap_df = analysis.set_index("api")[["anomalies","errors"]]
fig, ax = plt.subplots(figsize=(10,4))
sns.heatmap(heatmap_df, annot=True,cmap="Reds",ax=ax)
st.pyplot(fig)

# ------------------------------
# PIE CHARTS
# ------------------------------
st.subheader("Overall API Response Distribution")
anomaly_counts = df["response_time_ms"].apply(lambda x: "Anomaly" if x>=400 else "Normal").value_counts()
fig2, ax2 = plt.subplots()
ax2.pie(anomaly_counts.values, labels=anomaly_counts.index, autopct="%1.1f%%", startangle=90)
ax2.axis("equal")
st.pyplot(fig2)

st.subheader("HTTP Status Code Distribution")
status_counts = df["status_code"].value_counts()
fig3, ax3 = plt.subplots()
ax3.pie(status_counts.values, labels=status_counts.index, autopct="%1.1f%%", startangle=90)
ax3.axis("equal")
st.pyplot(fig3)

# ------------------------------
# THREAT ALERTS
# ------------------------------
st.subheader("Detected Threats / Findings")
for _, row in analysis.iterrows():
    if row["severity"] in ["High","Critical"]:
        st.error(f"{row['api']} | Severity: {row['severity']} | Zero Trust Score: {row['zero_trust_score']} | MITRE: {row['MITRE_Technique']}")

# ------------------------------
# PDF EXPORT
# ------------------------------
if st.button("📄 Export DoD PDF Report"):
    pdf_buffer = export_pdf(analysis)
    st.download_button("Download PDF",pdf_buffer,file_name="API_Runtime_Posture_Report.pdf",mime="application/pdf")
