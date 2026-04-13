# ==========================================================
# KALSNET (KNet) – AGENTIC AI + CYBER RANGE PLATFORM
# GROQ KEY ONLY VERSION (FIXED)
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
st.set_page_config(page_title="KNet AI Platform", layout="wide")

# ----------------------------------------------------------
# HEADER
# ----------------------------------------------------------
st.markdown("<h1 style='color:blue; text-align:center;'>Kalsnet (KNet) – Agentic AI Platform</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:blue; text-align:center;'>Autonomous AI + Analytics + Reporting Engine</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='color:blue; text-align:center;'>Developed by Randy Singh</h4>", unsafe_allow_html=True)

# ----------------------------------------------------------
# GROQ API KEY (ONLY REQUIREMENT)
# ----------------------------------------------------------
st.sidebar.title("🔑 GROQ API KEY")

api_key = st.sidebar.text_input("Enter your GROQ API Key:", type="password")

if not api_key:
    st.warning("⚠️ Please enter GROQ API key to continue")
    st.stop()

client = Groq(api_key=api_key)

st.sidebar.success("✅ API Key Loaded")

# ----------------------------------------------------------
# USE CASES
# ----------------------------------------------------------
st.subheader("🎯 Select Agentic AI Use Case")

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
# AI FUNCTION
# ----------------------------------------------------------
def run_ai(task):
    try:
        res = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": task}],
            max_tokens=600
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

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
# CYBER EVENT GENERATOR
# ----------------------------------------------------------
def cyber_event():
    return {
        "Timestamp": datetime.datetime.now(),
        "Source IP": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
        "Destination IP": f"10.0.{random.randint(1,255)}.{random.randint(1,255)}",
        "Attack Type": random.choice(["Brute Force", "Malware", "Phishing", "Exfiltration"]),
        "Severity Score": random.randint(1,100)
    }

# ----------------------------------------------------------
# EXECUTION
# ----------------------------------------------------------
if run:

    result = run_ai(task)

    st.success("✅ AI Response")
    st.write(result)

    st.subheader(f"📊 Analytics Dashboard - {mode}")

    records = []

    # ---------------- CYBER ----------------
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

    # safe score detection
    score_col = [c for c in df.columns if "Score" in c or "Amount" in c or "Metric" in c]
    score_col = score_col[0] if score_col else df.columns[-1]

    df["Risk Level"] = df[score_col].apply(risk)

    st.dataframe(df, use_container_width=True)

    # ------------------------------------------------------
    # CONSISTENT RISK SUMMARY
    # ------------------------------------------------------
    summary = df["Risk Level"].value_counts().reindex(
        ["Low Risk","Medium Risk","High Risk","Critical"], fill_value=0
    )

    summary_df = pd.DataFrame({
        "Risk Level": summary.index,
        "Count": summary.values
    })

    st.subheader("📈 Risk Distribution Summary")
    st.dataframe(summary_df)

    # ------------------------------------------------------
    # BAR CHART
    # ------------------------------------------------------
    fig1, ax1 = plt.subplots()
    ax1.bar(summary_df["Risk Level"], summary_df["Count"])
    st.pyplot(fig1)

    # ------------------------------------------------------
    # PIE CHART
    # ------------------------------------------------------
    fig2, ax2 = plt.subplots()
    ax2.pie(summary_df["Count"], labels=summary_df["Risk Level"], autopct="%1.1f%%")
    st.pyplot(fig2)

    # ------------------------------------------------------
    # EXPORT CSV
    # ------------------------------------------------------
    st.download_button("⬇️ CSV", df.to_csv(index=False), "data.csv")

    # ------------------------------------------------------
    # EXPORT JSON
    # ------------------------------------------------------
    st.download_button("⬇️ JSON", json.dumps(df.to_dict(), indent=2), "data.json")

    # ------------------------------------------------------
    # EXPORT PDF
    # ------------------------------------------------------
    def export_pdf(text):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer)
        style = getSampleStyleSheet()

        doc.build([
            Paragraph("KNet AI Report", style["Title"]),
            Spacer(1, 12),
            Paragraph(text.replace("\n","<br/>"), style["BodyText"])
        ])

        buffer.seek(0)
        return buffer

    st.download_button("⬇️ PDF", export_pdf(result), "report.pdf")

# ----------------------------------------------------------
# FOOTER
# ----------------------------------------------------------
st.markdown("---")
st.markdown("### 📌 System Info: Only GROQ API Key required. No password gating.")