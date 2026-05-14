


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
# CUSTOM CSS (FIXED FOOTER + READABILITY)
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

/* HEADER */
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

/* ✅ FIXED FOOTER (NOW BRIGHT) */
.footer-box {
    background-color: #ffffff !important;
    color: #111111 !important;
    padding: 22px;
    border-radius: 12px;
    margin-top: 20px;
    border: 1px solid #d0d0d0;
}

/* make all footer text readable */
.footer-box h4,
.footer-box p,
.footer-box li,
.footer-box ul,
.footer-box b {
    color: #111111 !important;
}

/* ✅ FIX FILE UPLOAD VISIBILITY */
.stFileUploader {
    background-color: #ffffff !important;
    padding: 10px;
    border-radius: 10px;
    border: 1px solid #ccc;
}

/* Uploaded text area readability */
.stTextArea textarea {
    background-color: #ffffff !important;
    color: #111111 !important;
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

# (❗ REST OF YOUR CODE REMAINS EXACTLY THE SAME)