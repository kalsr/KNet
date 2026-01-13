


# ============================================================
# API Simulation & Security Analytics Platform
#
# Developed by Randy Singh
# Kalsnet (KNet) Consulting Group
#
# Features:
# - Log-file driven API simulation
# - GUI with upload & slider
# - Charts & analytics
# - Anomaly & fraud detection
# - Export to CSV & PDF
# ============================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
import tempfile

# ------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------
st.set_page_config(
    page_title="API Simulation Platform",
    layout="wide"
)

# ------------------------------------------------------------
# Title
# ------------------------------------------------------------
st.title("🔐 API Simulation, Analytics & Security Platform")
st.subheader(
    "Developed by **Randy Singh** – Kalsnet (KNet) Consulting Group"
)

st.markdown(
    """
This enterprise-grade platform simulates real-world API behavior using
log files and performs **security analytics, anomaly detection,
and compliance-oriented reporting**.
"""
)

st.divider()

# ------------------------------------------------------------
# Sidebar Controls
# ------------------------------------------------------------
st.sidebar.header("⚙️ Controls")

uploaded_file = st.sidebar.file_uploader(
    "Upload API Log File (.txt)",
    type=["txt"]
)

record_limit = st.sidebar.slider(
    "Records to Display",
    min_value=10,
    max_value=100,
    value=20,
    step=10
)

# ------------------------------------------------------------
# Load Log Data
# ------------------------------------------------------------
def load_log_data(file):
    records = []

    for line in file:
        line = line.decode("utf-8").strip()
        if "|" not in line:
            continue

        request, response = line.split("|", 1)
        status = response.strip().split()[0]

        records.append({
            "Request": request.strip(),
            "Response": response.strip(),
            "Status": status
        })

    return pd.DataFrame(records)

# ------------------------------------------------------------
# Anomaly Detection Logic
# ------------------------------------------------------------
def detect_anomalies(df):
    anomalies = []

    # Excessive 404s
    if (df["Status"] == "404").sum() > 10:
        anomalies.append("High number of 404 errors – possible API probing")

    # Brute-force style login attempts
    login_attempts = df["Request"].str.contains("/login", case=False)
    if login_attempts.sum() > 5:
        anomalies.append("Multiple login attempts – possible brute-force attack")

    # Error rate spike
    error_rate = len(df[df["Status"].isin(["401", "403", "404", "500"])]) / len(df)
    if error_rate > 0.3:
        anomalies.append("High error rate detected – abnormal API behavior")

    return anomalies

# ------------------------------------------------------------
# PDF Export
# ------------------------------------------------------------
def export_pdf(summary_text):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    c = canvas.Canvas(tmp.name, pagesize=LETTER)

    text = c.beginText(40, 750)
    text.setFont("Helvetica", 10)

    for line in summary_text.split("\n"):
        text.textLine(line)

    c.drawText(text)
    c.showPage()
    c.save()

    return tmp.name

# ------------------------------------------------------------
# Main App Logic
# ------------------------------------------------------------
if uploaded_file:
    df = load_log_data(uploaded_file)

    if df.empty:
        st.error("No valid API records found.")
    else:
        st.success(f"Loaded {len(df)} API records")

        df_view = df.head(record_limit)

        # ----------------------------------------------------
        # Display Logs
        # ----------------------------------------------------
        st.subheader("📄 API Log Records")
        st.dataframe(df_view, use_container_width=True)

        # ----------------------------------------------------
        # Analytics
        # ----------------------------------------------------
        st.subheader("📊 API Analytics")

        status_counts = df["Status"].value_counts()

        col1, col2 = st.columns(2)

        with col1:
            fig1, ax1 = plt.subplots()
            status_counts.plot(kind="bar", ax=ax1)
            ax1.set_xlabel("Status Code")
            ax1.set_ylabel("Count")
            st.pyplot(fig1)

        with col2:
            fig2, ax2 = plt.subplots()
            ax2.pie(
                status_counts,
                labels=status_counts.index,
                autopct="%1.1f%%",
                startangle=90
            )
            ax2.axis("equal")
            st.pyplot(fig2)

        # ----------------------------------------------------
        # Anomaly Detection
        # ----------------------------------------------------
        st.subheader("🚨 Anomaly & Fraud Detection")

        anomalies = detect_anomalies(df)

        if anomalies:
            for a in anomalies:
                st.warning(a)
        else:
            st.success("No abnormal API behavior detected.")

        # ----------------------------------------------------
        # Security Explanation
        # ----------------------------------------------------
        st.subheader("🔍 API Security Risk Assessment")

        st.markdown(
            """
APIs are frequent attack targets due to:
- Weak authentication
- Excessive error disclosure
- Lack of rate limiting
- Poor monitoring

Common vulnerabilities include:
**Broken Authentication, API Enumeration, Injection, and DoS attacks**
(OWASP API Top 10).
"""
        )

        # ----------------------------------------------------
        # Recommendations
        # ----------------------------------------------------
        st.subheader("🛡️ Security Recommendations")

        st.markdown(
            """
✔ Enforce OAuth2 / JWT authentication  
✔ Apply rate limiting & throttling  
✔ Monitor logs continuously  
✔ Use API Gateways & WAFs  
✔ Validate all input parameters  
✔ Mask sensitive error messages  
✔ Encrypt traffic using TLS  
✔ Conduct regular security audits  
"""
        )

        # ----------------------------------------------------
        # Export Section
        # ----------------------------------------------------
        st.subheader("📤 Export Analytics")

        # CSV Export
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download Log Data (CSV)",
            csv,
            "api_logs.csv",
            "text/csv"
        )

        # PDF Export
        summary = f"""
API SIMULATION SECURITY REPORT
----------------------------------
Total Records: {len(df)}
404 Errors: {(df['Status']=='404').sum()}
401 Errors: {(df['Status']=='401').sum()}
403 Errors: {(df['Status']=='403').sum()}

Detected Anomalies:
{chr(10).join(anomalies) if anomalies else 'None detected'}

Recommendations:
- Implement authentication
- Apply rate limiting
- Monitor logs
"""

        pdf_path = export_pdf(summary)

        with open(pdf_path, "rb") as f:
            st.download_button(
                "Download Security Report (PDF)",
                f,
                "api_security_report.pdf",
                "application/pdf"
            )

else:
    st.info(
        "Upload a log file to start.\n\n"
        "Format:\n"
        "`GET /api/data | 200 OK - Response`"
    )

# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------
st.divider()
st.caption("© Kalsnet (KNet) Consulting Group – API Security Platform")
