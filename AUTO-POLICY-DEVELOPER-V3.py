


# =========================================================
# KNet PolicyForge AI
# Developed by Randy Singh from Kalsnet (KNet) Consulting Group
# =========================================================
#
# REQUIREMENTS:
# pip install streamlit groq pandas reportlab python-docx
#
# RUN:
# streamlit run knet_policyforge_ai_enhanced.py
# =========================================================

import streamlit as st
from groq import Groq
import json
import pandas as pd
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from docx import Document
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="KNet PolicyForge AI",
    layout="wide",
    page_icon="🛡️"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1, h2, h3, h4 {
    color: #4FC3F7;
}

.stButton>button {
    background-color: #1F6FEB;
    color: white;
    border-radius: 10px;
    padding: 0.5rem 1rem;
    border: none;
    font-weight: 600;
}

.stTextInput>div>div>input,
.stTextArea textarea,
[data-baseweb="select"] {
    border-radius: 8px;
}

.policy-header {
    text-align: center;
    padding: 25px;
    background: linear-gradient(135deg, #111827, #1F2937);
    border-radius: 18px;
    margin-bottom: 20px;
    border: 1px solid #374151;
}

.policy-title {
    color: #00BFFF;
    font-size: 3.2rem;
    font-weight: 900;
    margin: 0;
    text-shadow: 0 0 8px rgba(0,191,255,0.7);
}

.policy-subtitle {
    color: #D1D5DB;
    font-size: 1.1rem;
    font-weight: 600;
    margin-top: 10px;
}

/* =========================================================
   ✅ FIXED FOOTER (BRIGHT + READABLE)
   ========================================================= */

.footer-box {
    background-color: #F8FAFC;   /* LIGHT BACKGROUND */
    padding: 25px;
    border-radius: 12px;
    margin-top: 25px;
    border: 1px solid #CBD5E1;
    color: #0F172A;             /* DARK TEXT */
}

.footer-box h4 {
    color: #0F172A;
    font-size: 1.2rem;
    margin-bottom: 10px;
}

.footer-box p {
    color: #1F2937;
    font-size: 0.95rem;
    line-height: 1.5;
}

.footer-box ul {
    color: #111827;
    padding-left: 20px;
}

.footer-box li {
    margin-bottom: 5px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="policy-header">
    <div class="policy-title">🛡️ KNet PolicyForge AI</div>
    <div class="policy-subtitle">
        Developed by Randy Singh from Kalsnet (KNet) Consulting Group
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("⚙️ Configuration")

groq_api_key = st.sidebar.text_input("Groq API Key", type="password")

st.sidebar.markdown("""
### How to Get Groq API Key
1. Visit https://console.groq.com
2. Create a free account
3. Navigate to API Keys
4. Generate a new API key
5. Paste the key here
""")

model_name = st.sidebar.selectbox(
    "Select Groq Model",
    [
        "llama-3.3-70b-versatile",
        "mixtral-8x7b-32768",
        "gemma2-9b-it"
    ]
)

policy_area = st.sidebar.selectbox(
    "Policy Area",
    [
        "Cybersecurity Policy",
        "Acceptable Use Policy",
        "Remote Work Policy",
        "AI Governance Policy",
        "Incident Response Policy",
        "Disaster Recovery Policy",
        "Business Continuity Policy",
        "Data Retention Policy",
        "Privacy Policy",
        "HR Policy",
        "Zero Trust Policy",
        "Vendor Management Policy"
    ]
)

organization_type = st.sidebar.selectbox(
    "Organization Type",
    [
        "Government",
        "Enterprise",
        "Healthcare",
        "Financial",
        "Educational",
        "Small Business",
        "Technology Company"
    ]
)

detail_level = st.sidebar.selectbox(
    "Policy Detail Level",
    ["Basic", "Standard", "Advanced", "Enterprise Grade"]
)

# =========================================================
# (Rest of your code remains EXACTLY the same)
# =========================================================

# FOOTER (UNCHANGED STRUCTURE, NOW READABLE)
st.markdown("""
<div class="footer-box">

<h4>About KNet PolicyForge AI</h4>

<p>
This enterprise-grade AI policy generation platform helps organizations
create professional governance, cybersecurity, compliance,
risk management, HR, and operational policies using advanced AI models.
</p>

<b>Features:</b>
<ul>
<li>AI-powered policy development</li>
<li>Enterprise-grade formatting</li>
<li>Multi-format exports</li>
<li>Professional GUI</li>
<li>Editable policy workspace</li>
<li>Upload & review capability</li>
</ul>

<p><b>Developed by Randy Singh from Kalsnet (KNet) Consulting Group</b></p>

</div>
""", unsafe_allow_html=True)