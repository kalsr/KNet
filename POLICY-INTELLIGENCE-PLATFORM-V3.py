

# =========================================================
# AI Governance & Public Policy Intelligence Platform
# Enterprise Dashboard UI (Upgraded)
# Developed by Randy Singh from Kalsnet (KNet) Consulting Group
# =========================================================

import streamlit as st
import json
from groq import Groq

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Governance Platform",
    layout="wide",
    page_icon="🏛️"
)

# =========================================================
# PROFESSIONAL UI STYLING
# =========================================================

st.markdown("""
<style>

/* BACKGROUND */
.main {
    background-color: #0E1117;
}

/* TOP HEADER BAR */
.header {
    background: linear-gradient(90deg, #0B3D91, #1E90FF);
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 20px;
}

/* MAIN TITLE */
.title {
    font-size: 34px;
    font-weight: 900;
    color: white;
}

/* SUBTITLE (BLUE BOLD BRAND LINE) */
.subtitle {
    font-size: 16px;
    font-weight: 900;
    color: #00BFFF;
    margin-top: 5px;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* CARDS */
.card {
    background-color: #1A1F2E;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #2A2F3A;
}

/* BUTTONS */
.stButton>button {
    background-color: #1E90FF;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    padding: 0.5rem 1rem;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER (LIKE YOUR IMAGE STYLE)
# =========================================================

st.markdown("""
<div class="header">
    <div class="title">AI GOVERNANCE & PUBLIC POLICY INTELLIGENCE PLATFORM</div>
    <div class="subtitle">
        <b>Developed by Randy Singh from Kalsnet (KNet) Consulting Group</b>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR NAVIGATION (LIKE DASHBOARD)
# =========================================================

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "Policy Generator",
        "Compliance Auditor",
        "Reports",
        "Settings"
    ]
)

# =========================================================
# GROQ CONFIG
# =========================================================

st.sidebar.header("⚙️ AI Configuration")

api_key = st.sidebar.text_input("Groq API Key", type="password")

st.sidebar.markdown("""
### 🔑 Get Groq Key
1. https://console.groq.com  
2. Sign up free  
3. Go to API Keys  
4. Create Key  
5. Paste here  
""")

model = st.sidebar.selectbox(
    "Model",
    ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
)

# =========================================================
# DROPDOWN OPTIONS (FIXED)
# =========================================================

industry_options = [
    "Government",
    "Defense",
    "Healthcare",
    "Finance",
    "Education",
    "Energy",
    "Technology",
    "Transportation"
]

policy_objectives = [
    "Cybersecurity Protection",
    "Data Privacy Compliance",
    "AI Governance & Ethics",
    "Risk Management",
    "Regulatory Compliance",
    "Incident Response",
    "Zero Trust Implementation"
]

# =========================================================
# DASHBOARD METRICS (LIKE IMAGE CARDS)
# =========================================================

if menu == "Dashboard":

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Policies Generated", "128", "↑ 12%")
    col2.metric("Compliance Score", "92%", "↑ 5%")
    col3.metric("Risk Alerts", "37", "↓ 3%")
    col4.metric("Active Reports", "18", "↑ 2")

    st.markdown("---")

    st.info("Use Policy Generator to create enterprise-grade AI policies")

# =========================================================
# POLICY GENERATOR (MAIN UI LIKE IMAGE)
# =========================================================

if menu == "Policy Generator":

    st.subheader("📄 Policy Generation Engine")

    col1, col2 = st.columns(2)

    with col1:
        org = st.text_input("Organization Name")
        industry = st.selectbox("Industry", industry_options)

    with col2:
        policy_type = st.selectbox("Policy Objective", policy_objectives)
        risk = st.selectbox("Risk Level", ["Low", "Medium", "High", "Critical"])

    requirement = st.text_area("Additional Requirements")

    if st.button("🚀 Generate Policy", use_container_width=True):

        if not api_key:
            st.error("Enter Groq API Key")
        else:
            client = Groq(api_key=api_key)

            prompt = f"""
Create enterprise policy:

Org: {org}
Industry: {industry}
Objective: {policy_type}
Risk: {risk}

Requirements:
{requirement}
"""

            res = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a senior policy architect."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=4000
            )

            st.session_state["result"] = res.choices[0].message.content

    # OUTPUT BOX (CARD STYLE)
    if "result" in st.session_state:

        st.markdown("### 📘 Generated Policy")

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write(st.session_state["result"])
        st.markdown("</div>", unsafe_allow_html=True)

        if st.button("🔄 Reset"):
            st.session_state.clear()
            st.rerun()

# =========================================================
# PLACEHOLDER PAGES
# =========================================================

if menu == "Compliance Auditor":
    st.subheader("🛡️ Compliance Auditor Module")
    st.info("Coming soon: NIST, ISO 27001, FedRAMP mapping engine")

if menu == "Reports":
    st.subheader("📊 Reports & Analytics")
    st.info("Coming soon: dashboards, charts, exports")

if menu == "Settings":
    st.subheader("⚙️ Settings Panel")
    st.info("System configuration and admin controls")