# ==========================================================
# KALSNET (KNet) – ENTERPRISE AGENTIC AI + CYBER RANGE SYSTEM
# ==========================================================

import streamlit as st
from groq import Groq
import pandas as pd
import json
import matplotlib.pyplot as plt
import io
import random
import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------
st.set_page_config(page_title="KNet Cyber AI Platform", layout="wide")

# ----------------------------------------------------------
# HEADER (ALWAYS SHOW FIRST)
# ----------------------------------------------------------
st.markdown("<h1 style='color:blue; text-align:center;'>Kalsnet (KNet) – Agentic AI Platform</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:blue; text-align:center;'>Autonomous AI + Analytics + Reporting Engine</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='color:blue; text-align:center;'>Developed by Randy Singh</h4>", unsafe_allow_html=True)

# ----------------------------------------------------------
# SIDEBAR AUTH (FIXED SAFE GATE)
# ----------------------------------------------------------
st.sidebar.title("🔐 Access Control (Optional)")

password = st.sidebar.text_input("Enter Password:", type="password")

access_granted = (password == "knet123")

if password and not access_granted:
    st.sidebar.error("❌ Incorrect Password")

if access_granted:
    st.sidebar.success("✅ Access Granted")
else:
    st.sidebar.info("ℹ️ Enter password to enable execution features")

# ----------------------------------------------------------
# GROQ API (ALWAYS AVAILABLE UI)
# ----------------------------------------------------------
st.sidebar.markdown("---")
api_key = st.sidebar.text_input("GROQ API Key", type="password")

if api_key:
    client = Groq(api_key=api_key)
else:
    client = None

# ----------------------------------------------------------
# USE CASES
# ----------------------------------------------------------
st.subheader("🎯 Select Use Case")

mode = st.selectbox("Choose Mode", [
    "Cyber Range Simulation",
    "Financial Fraud Simulation",
    "Supply Chain Risk",
    "Healthcare Analytics",
    "Custom Analytics"
])

task = st.text_area("Enter Task")
run = st.button("🚀 Run System")

# ----------------------------------------------------------
# RISK ENGINE
# ----------------------------------------------------------
def risk(score):
    if score < 25:
        return "Low Risk"
    elif score < 50:
        return "Medium Risk"
    elif score < 75:
        return "High Risk"
    else:
        return "Critical"

# ----------------------------------------------------------
# CYBER GENERATOR
# ----------------------------------------------------------
def cyber_event():
    return {
        "Timestamp": datetime.datetime.now(),
        "Source IP": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
        "Attack Type": random.choice(["Brute Force", "Malware", "Phishing", "Exfiltration"]),
        "Severity Score": random.randint(1,100)
    }

# ----------------------------------------------------------
# AI FUNCTION
# ----------------------------------------------------------
def run_ai(task):
    if not client:
        return "API key missing"

    try:
        res = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role":"user","content":task}],
            max_tokens=600
        )
        return res.choices[0].message.content
    except:
        return None

# ----------------------------------------------------------
# EXECUTION (ONLY BLOCKED HERE, NOT UI)
# ----------------------------------------------------------
if run:

    if not access_granted:
        st.error("🔒 Enter correct password to run system")
        st.stop()

    result = run_ai(task)

    if not result:
        st.error("AI execution failed")
        st.stop()

    st.success("AI Response")
    st.write(result)

    st.subheader(f"📊 Analytics Dashboard - {mode}")

    records = []

    # ---------------- CYBER RANGE ----------------
    if mode == "Cyber Range Simulation":
        for _ in range(40):
            records.append(cyber_event())

    # ---------------- FINANCE ----------------
    elif mode == "Financial Fraud Simulation":
        for _ in range(40):
            records.append({
                "Account": random.randint(1000,9999),
                "Amount": random.randint(100,10000),
                "Risk Score": random.randint(1,100)
            })

    # ---------------- SUPPLY ----------------
    elif mode == "Supply Chain Risk":
        for _ in range(40):
            records.append({
                "Supplier": f"Vendor-{random.randint(1,50)}",
                "Delay": random.randint(0,30),
                "Risk Score": random.randint(1,100)
            })

    # ---------------- HEALTH ----------------
    elif mode == "Healthcare Analytics":
        for _ in range(40):
            records.append({
                "Patient": random.randint(1000,9999),
                "Risk Score": random.randint(1,100)
            })

    # ---------------- CUSTOM ----------------
    else:
        for _ in range(40):
            records.append({
                "Metric": random.randint(1,100)
            })

    df = pd.DataFrame(records)

    # pick score column safely
    score_col = [c for c in df.columns if "Score" in c][0] if any("Score" in c for c in df.columns) else df.columns[-1]
    df["Risk Level"] = df[score_col].apply(risk)

    st.dataframe(df, use_container_width=True)

    # ---------------- CONSISTENT SUMMARY ----------------
    summary = df["Risk Level"].value_counts().reindex(
        ["Low Risk","Medium Risk","High Risk","Critical"], fill_value=0
    )

    summary_df = pd.DataFrame({
        "Risk Level": summary.index,
        "Count": summary.values
    })

    st.subheader("📈 Risk Summary")
    st.dataframe(summary_df)

    # ---------------- CHARTS ----------------
    fig1, ax1 = plt.subplots()
    ax1.bar(summary_df["Risk Level"], summary_df["Count"])
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    ax2.pie(summary_df["Count"], labels=summary_df["Risk Level"], autopct="%1.1f%%")
    st.pyplot(fig2)

    # ---------------- EXPORTS ----------------
    st.download_button("CSV", df.to_csv(index=False), "data.csv")
    st.download_button("JSON", json.dumps(df.to_dict(), indent=2), "data.json")

    def pdf_export(text):
        buf = io.BytesIO()
        doc = SimpleDocTemplate(buf)
        style = getSampleStyleSheet()

        doc.build([
            Paragraph("KNet Report", style["Title"]),
            Spacer(1, 12),
            Paragraph(text.replace("\n","<br/>"), style["BodyText"])
        ])

        buf.seek(0)
        return buf

    st.download_button("PDF", pdf_export(result), "report.pdf")

# ----------------------------------------------------------
# FOOTER
# ----------------------------------------------------------
st.markdown("---")
st.markdown("""
### 📌 System Behavior
- UI always loads
- Password only blocks execution (not interface)
- Analytics is mode-based
- Risk summary always matches dataset exactly
""")