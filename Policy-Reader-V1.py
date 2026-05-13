

import streamlit as st
import os
import json
import pandas as pd
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(page_title="Policy Intelligence Q&A System", layout="wide")

# ===============================
# HEADER / BRANDING
# ===============================
st.markdown("""
    <div style="background-color:#0f172a;padding:15px;border-radius:10px">
        <h2 style="color:white;text-align:center;">
            Policy Intelligence Q&A System
        </h2>
        <h4 style="color:#cbd5e1;text-align:center;">
            Developed by Randy Singh from Kalsnet (KNet) Consulting Group
        </h4>
    </div>
""", unsafe_allow_html=True)

st.write("")

# ===============================
# SESSION STATE INIT
# ===============================
if "policy_text" not in st.session_state:
    st.session_state.policy_text = ""

if "qa_results" not in st.session_state:
    st.session_state.qa_results = []

# ===============================
# POLICY UPLOAD SECTION
# ===============================
st.subheader("📄 Upload Policy File (.txt)")

uploaded_file = st.file_uploader("Upload Policy File", type=["txt"])

if uploaded_file:
    st.session_state.policy_text = uploaded_file.read().decode("utf-8")
    st.success("Policy loaded successfully!")

# Show policy preview
if st.session_state.policy_text:
    with st.expander("📖 View Loaded Policy"):
        st.write(st.session_state.policy_text)

# ===============================
# Q&A SECTION
# ===============================
st.subheader("❓ Ask Questions on Policy")

question = st.text_input("Enter your question")

def get_policy_answer(policy, question):
    """Simple keyword-based retrieval"""
    question_words = set(question.lower().split())
    sentences = policy.split(".")
    
    matched = []
    for s in sentences:
        if any(word in s.lower() for word in question_words):
            matched.append(s.strip())

    if not matched:
        return "No relevant information found in policy."
    
    return " | ".join(matched[:5])

if st.button("Get Answer"):
    if not st.session_state.policy_text:
        st.error("Policy does not exist so please add the policy to do any question answer.")
    elif not question:
        st.error("Please enter a question")
    else:
        answer = get_policy_answer(st.session_state.policy_text, question)

        result = {
            "question": question,
            "answer": answer
        }

        st.session_state.qa_results.append(result)

        st.subheader("📌 Answer")
        st.write(answer)

        st.success("Query processed successfully")

# ===============================
# RESULTS DISPLAY
# ===============================
if st.session_state.qa_results:
    st.subheader("📊 Query History")

    df = pd.DataFrame(st.session_state.qa_results)
    st.dataframe(df, use_container_width=True)

# ===============================
# EXPORT FUNCTIONS
# ===============================
def export_json(data):
    return json.dumps(data, indent=4).encode("utf-8")

def export_csv(data):
    df = pd.DataFrame(data)
    return df.to_csv(index=False).encode("utf-8")

def export_pdf(data):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("Policy Q&A Report", styles["Title"]))
    content.append(Spacer(1, 12))

    for item in data:
        content.append(Paragraph(f"Q: {item['question']}", styles["Normal"]))
        content.append(Paragraph(f"A: {item['answer']}", styles["Normal"]))
        content.append(Spacer(1, 10))

    doc.build(content)
    buffer.seek(0)
    return buffer

# ===============================
# DOWNLOAD SECTION
# ===============================
st.subheader("⬇️ Export Results")

if st.session_state.qa_results:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.download_button(
            "Download JSON",
            data=export_json(st.session_state.qa_results),
            file_name="policy_results.json",
            mime="application/json"
        )

    with col2:
        st.download_button(
            "Download CSV",
            data=export_csv(st.session_state.qa_results),
            file_name="policy_results.csv",
            mime="text/csv"
        )

    with col3:
        st.download_button(
            "Download PDF",
            data=export_pdf(st.session_state.qa_results),
            file_name="policy_results.pdf",
            mime="application/pdf"
        )
else:
    st.info("No results available for export yet.")