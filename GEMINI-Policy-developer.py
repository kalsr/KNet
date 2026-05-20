# GEMINI Policy-developer

import json
import os
import pandas as pd
import streamlit as st
from docx import Document
from groq import Groq
import PyPDF2

# ==========================================
# 1. PAGE CONFIGURATION & THEME
# ==========================================
st.set_page_config(
    page_title="Auntie - Policy Developer",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for Professional UI Branding
st.markdown(
    """
    <style>
    .main-title {
        font-size: 40px;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 5px;
    }
    .subtitle {
        font-size: 18px;
        color: #4B5563;
        margin-bottom: 25px;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #F3F4F6;
        color: #374151;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        border-top: 1px solid #E5E7EB;
        z-index: 100;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# ==========================================
# 2. HELPER FUNCTIONS FOR FILE PARSING
# ==========================================
def extract_text_from_pdf(file):
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"


def extract_text_from_docx(file):
    try:
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"Error reading Word document: {str(e)}"


def extract_text_from_csv(file):
    try:
        df = pd.read_csv(file)
        return df.to_string(index=False)
    except Exception as e:
        return f"Error reading CSV: {str(e)}"


def extract_text_from_json(file):
    try:
        data = json.load(file)
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error reading JSON: {str(e)}"


# ==========================================
# 3. SIDEBAR - API CONFIGURATION & INSTRUCTIONS
# ==========================================
with st.sidebar:
    st.image(
        "https://img.icons8.com/fluency/96/policy.png", width=80
    )  # Elegant placeholder icon
    st.title("Configuration")

    # API Key Input
    groq_api_key = st.text_input(
        "Enter Groq API Key:",
        type="password",
        placeholder="gsk_...",
        help="Your key is processed securely locally and never stored online.",
    )

    st.markdown("---")

    # Instructions on getting a free key
    st.markdown("###  How to get a Free Groq Key")
    st.markdown(
        """
    1. **Visit Groq Cloud:** Go to [console.groq.com](https://console.groq.com/).
    2. **Sign Up/Log In:** Create a free account using your email or Google login (No credit card required).
    3. **Go to API Keys:** Click on the **'API Keys'** tab in the left-hand navigation menu.
    4. **Generate Key:** Click the **'Create API Key'** button.
    5. **Name & Copy:** Give it a name (e.g., *Auntie-App*), copy the key immediately, and paste it here!
    
    *Note: Groq offers a generous free tier with fast hardware inference capped by rate limits.*
    """
    )


# ==========================================
# 4. MAIN INTERFACE & BRANDING
# ==========================================
st.markdown('<div class="main-title">Auntie</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">AI-Powered Corporate & Compliance Policy Developer</div>',
    unsafe_allow_html=True,
)

# Application Metadata / Corporate Attribution Card
st.info(
    "**Developed by:** Randy Singh Kalsnet | **KNet Consulting Group**\n\n"
    "*Auntie* leverages state-of-the-art open large language models hosted on Groq's LPU inference engine to build tailored compliance structures, HR procedures, and security frameworks seamlessly."
)

st.markdown("---")


# ==========================================
# 5. CORE USER INPUT & FILE UPLOAD
# ==========================================
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. Policy Details")
    policy_name = st.text_input(
        "Policy Title/Objective:",
        placeholder="e.g., Remote Work Information Security Policy",
    )
    policy_scope = st.text_area(
        "Key Constraints, Target Audience or Scope:",
        placeholder="e.g., Applies to all European remote employees managing financial databases.",
    )
    model_choice = st.selectbox(
        "Select LLM Brain:",
        ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"],
        help="70B is better for comprehensive drafting; 8B is significantly faster.",
    )

with col2:
    st.subheader("2. Upload Contextual Data (Optional)")
    uploaded_file = st.file_uploader(
        "Upload reference documents, old frameworks, or raw data metrics:",
        type=["pdf", "docx", "csv", "json"],
    )

    extracted_context = ""
    if uploaded_file is not None:
        file_ext = uploaded_file.name.split(".")[-1].lower()

        if file_ext == "pdf":
            extracted_context = extract_text_from_pdf(uploaded_file)
        elif file_ext == "docx":
            extracted_context = extract_text_from_docx(uploaded_file)
        elif file_ext == "csv":
            extracted_context = extract_text_from_csv(uploaded_file)
        elif file_ext == "json":
            extracted_context = extract_text_from_json(uploaded_file)

        if "Error" in extracted_context:
            st.error(extracted_context)
        else:
            st.success(
                f"Successfully extracted data from {uploaded_file.name}!"
            )


# ==========================================
# 6. PROCESSING & GENERATION
# ==========================================
st.markdown("---")
if st.button(" Draft Corporate Policy Document", type="primary"):
    if not groq_api_key:
        st.warning(" Please provide a valid Groq API key in the sidebar.")
    elif not policy_name:
        st.warning(" Please specify a Policy Title before generating.")
    else:
        with st.spinner("Analyzing parameters and drafting policy document..."):
            try:
                # Initialize Groq client securely using the input key
                client = Groq(api_key=groq_api_key)

                # Assemble prompt
                system_prompt = (
                    "You are 'Auntie', an elite legal, corporate compliance, and HR advisor "
                    "developed by Randy Singh Kalsnet at KNet Consulting Group. Our goal is to draft highly professional, "
                    "Structured, Rigorous, and Legally Sound Organizational Policies."
                )

                user_prompt = f"Please draft a comprehensive corporate policy document for: '{policy_name}'.\n\n"
                if policy_scope:
                    user_prompt += f"**Scope and Constraints:**\n{policy_scope}\n\n"
                if extracted_context:
                    user_prompt += f"**Use the following supplementary data and context to guide the rules:**\n{extracted_context}\n\n"

                user_prompt += (
                    "Structure the output professionally with headers: 1. Purpose, 2. Scope, "
                    "3. Policy Elements, 4. Compliance and Enforcement, 5. Revision Control & Sign-off."
                )

                # Execute call
                completion = client.chat.completions.create(
                    model=model_choice,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    temperature=0.3,
                )

                # Display Results
                st.subheader("📋 Generated Draft Policy")
                generated_policy = completion.choices[0].message.content
                st.markdown(generated_policy)

                # Downloader Utility for user convenience
                st.download_button(
                    label=" Download Draft as Text File",
                    data=generated_policy,
                    file_name=f"{policy_name.replace(' ', '_')}_draft.txt",
                    mime="text/plain",
                )

            except Exception as e:
                st.error(
                    f"An error occurred while communicating with Groq: {str(e)}"
                )


# ==========================================
# 7. PERMANENT STICKY FOOTER
# ==========================================
st.markdown(
    '<div class="footer">Auntie App © 2026 | Developed by Randy Singh Kalsnet | KNet Consulting Group</div>',
    unsafe_allow_html=True,
)
