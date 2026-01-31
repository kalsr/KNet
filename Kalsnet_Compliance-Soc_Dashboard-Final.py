

# ============================================================
# Kalsnet_Compliance-SOC_Dashboard.py
# Enterprise SOC + FedRAMP / DoD + Commercial Compliance Demo
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from fpdf import FPDF
import json

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Kalsnet SOC Compliance Dashboard",
    layout="wide"
)

# ============================================================
# HEADER – BOLD BLUE BRANDING
# ============================================================
st.markdown("""
<h1 style="text-align:center; color:#0047AB; font-weight:bold; font-size:48px;">
KALSNET SOC COMPLIANCE DASHBOARD
</h1>

<h3 style="text-align:center; color:#0047AB; font-weight:bold;">
Threat Monitoring • FedRAMP / DoD • Commercial SOC
</h3>

<p style="text-align:center; font-weight:bold; color:#0047AB;">
Designed & Developed by Randy Singh<br>
Kalsnet (KNet) Consulting Group
</p>
<hr>
""", unsafe_allow_html=True)

# ============================================================
# ATTACK + MITRE MAP
# ============================================================
attack_map = {
    "Phishing": ("T1566", "Phishing"),
    "Ransomware": ("T1486", "Data Encrypted"),
    "DoS": ("T1499", "Denial of Service"),
    "MITM": ("T1557", "Adversary-in-the-Middle"),
    "SQL Injection": ("T1190", "Exploit App"),
    "XSS": ("T1059", "Command Execution"),
    "Zero-Day": ("T1203", "Client Exploit"),
    "DNS Spoofing": ("T1565", "Data Manipulation")
}

# ============================================================
# FEDRAMP / NIST CONTROLS
# ============================================================
fedramp_controls = {
    "Access Control": ["AC-2", "AC-3", "AC-6"],
    "Audit & Accountability": ["AU-2", "AU-6", "AU-12"],
    "Incident Response": ["IR-4", "IR-6", "IR-8"],
    "Risk Assessment": ["RA-3", "RA-5"],
    "System Integrity": ["SI-2", "SI-7", "SI-10"],
    "Boundary Protection": ["SC-7", "SC-5"],
    "Identification & Auth": ["IA-2", "IA-5"]
}

# ============================================================
# SIDEBAR
# ============================================================
st.sidebar.header("⚙️ SOC Configuration")

mode = st.sidebar.radio(
    "SOC Mode",
    ["FedRAMP / DoD SOC", "Commercial SOC"]
)

sector = "Government"
if mode == "Commercial SOC":
    sector = st.sidebar.radio(
        "Industry Sector",
        ["Banking", "Healthcare", "FinTech", "Retail"]
    )

records = st.sidebar.slider("Synthetic Events", 10, 200, 60)

uploaded = st.sidebar.file_uploader(
    "Upload Log File (CSV)", type=["csv"]
)

# ✅ FIXED RESET BUTTON (NO experimental_rerun)
if st.sidebar.button("🔴 RESET DATA", use_container_width=True):
    st.rerun()

# ============================================================
# DATA GENERATION
# ============================================================
if uploaded:
    df = pd.read_csv(uploaded)
else:
    df = pd.DataFrame({
        "Time": [datetime.now().strftime("%H:%M:%S") for _ in range(records)],
        "Sector": [sector for _ in range(records)],  # ✅ NEW FIELD
        "Attack_Type": np.random.choice(list(attack_map.keys()), records),
        "Severity": np.random.choice(["Low", "Medium", "High", "Critical"], records),
        "Detected": np.random.choice(["Yes", "No"], records),
        "Source_IP": [
            f"10.{np.random.randint(1,255)}.{np.random.randint(1,255)}.{np.random.randint(1,255)}"
            for _ in range(records)
        ]
    })

# ============================================================
# THREAT SCORING
# ============================================================
def score_event(row):
    base = {"Low": 20, "Medium": 40, "High": 70, "Critical": 90}
    score = base[row["Severity"]]
    if row["Detected"] == "No":
        score += 10
    return min(score, 100)

df["Threat_Score"] = df.apply(score_event, axis=1)

# ============================================================
# EXECUTIVE METRICS
# ============================================================
st.subheader("📊 Executive SOC Overview")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Events", len(df))
c2.metric("Critical", len(df[df["Severity"] == "Critical"]))
c3.metric("Undetected", len(df[df["Detected"] == "No"]))
c4.metric("Avg Threat Score", round(df["Threat_Score"].mean(), 1))

# ============================================================
# PIE CHARTS
# ============================================================
st.subheader("📈 Threat Distribution")

p1, p2, p3 = st.columns(3)

with p1:
    fig, ax = plt.subplots()
    df["Attack_Type"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    ax.set_title("Attack Types")
    st.pyplot(fig)

with p2:
    fig, ax = plt.subplots()
    df["Severity"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    ax.set_title("Severity Levels")
    st.pyplot(fig)

with p3:
    fig, ax = plt.subplots()
    df["Detected"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    ax.set_title("Detection Coverage")
    st.pyplot(fig)

# ============================================================
# FEDRAMP / DOD EXPLANATION
# ============================================================
if mode == "FedRAMP / DoD SOC":
    st.subheader("🛡️ FedRAMP / DoD Compliance Mapping")

    st.markdown("""
**This SOC dashboard aligns with FedRAMP Moderate / High requirements by:**

• Continuous monitoring & audit logging  
• NIST 800-53 control traceability  
• Incident detection & response workflows  
• Evidence export for ATO & POA&M  
• Zero Trust & boundary protection enforcement
""")

    for k, v in fedramp_controls.items():
        st.write(f"**{k}:** {', '.join(v)}")

# ============================================================
# COMMERCIAL SOC INFO
# ============================================================
if mode == "Commercial SOC":
    st.subheader(f"🏦 Commercial SOC – {sector}")

    st.markdown(f"""
**Sector-Specific SOC Coverage for {sector}:**

• Regulatory alignment (PCI-DSS, HIPAA, GLBA, SOX)  
• Threat prioritization & severity scoring  
• Executive & audit-ready reporting  
• Exportable compliance evidence
""")

# ============================================================
# DATA TABLE
# ============================================================
st.subheader("📄 SOC Event Log")
st.dataframe(df, use_container_width=True)

# ============================================================
# EXPORTS
# ============================================================
st.subheader("⬇️ Export Results")

c1, c2, c3 = st.columns(3)

with c1:
    st.download_button(
        "Download CSV",
        df.to_csv(index=False),
        "soc_results.csv",
        "text/csv"
    )

with c2:
    st.download_button(
        "Download JSON",
        json.dumps(df.to_dict(orient="records"), indent=2),
        "soc_results.json",
        "application/json"
    )

with c3:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, "Kalsnet SOC Compliance Report", ln=True)

    for _, row in df.head(30).iterrows():
        pdf.multi_cell(0, 6, str(row.to_dict()))

    st.download_button(
        "Download PDF",
        pdf.output(dest="S").encode("latin-1"),
        "soc_results.pdf",
        "application/pdf"
    )
