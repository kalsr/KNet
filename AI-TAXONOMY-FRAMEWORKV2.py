

import streamlit as st
import pandas as pd
import json
import hashlib
import os

from docx import Document
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Enterprise AI Platform",
    layout="wide"
)

# =====================================================
# SIMPLE AUTH SYSTEM (DEMO)
# =====================================================
USERS = {
    "admin": "admin123",
    "user": "user123"
}

def hash_pwd(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

if "auth" not in st.session_state:
    st.session_state.auth = False

def login():
    st.sidebar.subheader("🔐 Login")

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state.auth = True
            st.session_state.user = username
        else:
            st.sidebar.error("Invalid credentials")

login()

if not st.session_state.auth:
    st.warning("Please login to access the platform")
    st.stop()

# =====================================================
# HEADER
# =====================================================
st.markdown("""
<h1 style='color:#0056D2;text-align:center;'>
ENTERPRISE AI TAXONOMY & PLATFORM
</h1>
<h4 style='text-align:center;color:#333;'>
AI Chatbot | Taxonomy | Reports | Database Ready | Cloud Deployable
</h4>
""", unsafe_allow_html=True)

# =====================================================
# CHATBOT (SIMPLIFIED GPT STYLE)
# =====================================================
def chatbot():
    st.subheader("🔴 AI Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    user_input = st.chat_input("Ask AI...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # SIMPLE MOCK AI RESPONSE (replace with OpenAI API if needed)
        response = f"AI Response: You asked about '{user_input}'. This is a simulated enterprise AI reply."

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

# =====================================================
# TAXONOMY ENGINE
# =====================================================
def taxonomy():
    st.subheader("🧠 AI Taxonomy Engine")

    menu = st.selectbox("Select Domain", [
        "Learning & Intelligence",
        "Advanced Computing",
        "AI Systems"
    ])

    if menu == "Learning & Intelligence":

        st.markdown("### Machine Learning")
        st.write("Predictive systems based on data.")

        st.markdown("### Deep Learning")
        st.write("Neural networks with multiple layers.")

        st.markdown("### NLP")
        st.write("Understanding human language.")

        st.graphviz_chart("""
        digraph {
            Data -> ML -> Model -> Prediction
        }
        """)

    elif menu == "Advanced Computing":

        st.markdown("### Quantum Computing")
        st.write("Qubits and quantum physics-based computation.")

        st.markdown("### Supercomputing")
        st.write("High-performance distributed computing.")

        st.graphviz_chart("""
        digraph {
            Input -> HPC -> Parallel_Processing -> Output
        }
        """)

    elif menu == "AI Systems":

        st.markdown("### Computer Vision")
        st.write("Machines interpret images.")

        st.markdown("### AI Agents")
        st.write("Autonomous intelligent systems.")

        st.graphviz_chart("""
        digraph {
            Input -> AI_Model -> Action
        }
        """)

# =====================================================
# MERMAID DIAGRAMS
# =====================================================
def mermaid():
    st.subheader("📊 AI Architecture (Mermaid)")

    st.markdown("""
```mermaid
graph TD
AI --> ML
AI --> DL
AI --> Quantum
ML --> Supervised
DL --> NeuralNetworks
````

""")

# =====================================================

# EXPORT SYSTEM

# =====================================================

def export_system():
    st.subheader("📄 Export Reports")

    data = {
        "AI": "Enterprise Platform",
        "Modules": ["Chatbot", "Taxonomy", "Reports"]
    }

    st.json(data)

    # CSV export
    df = pd.DataFrame({
        "Module": ["Chatbot", "Taxonomy", "Reports"],
        "Status": ["Active", "Active", "Active"]
    })

    st.download_button(
        "⬇ Download CSV",
        df.to_csv(index=False),
        "report.csv",
        "text/csv"
    )

    # JSON export
    st.download_button(
        "⬇ Download JSON",
        json.dumps(data),
        "report.json",
        "application/json"
    )

    # PDF generation
    if st.button("Generate PDF"):
        file = "report.pdf"
        doc = SimpleDocTemplate(file)
        styles = getSampleStyleSheet()
        doc.build([Paragraph("Enterprise AI Report", styles["Title"])])
        st.success("PDF Generated")

    # Word generation
    if st.button("Generate Word"):
        doc = Document()
        doc.add_heading("Enterprise AI Report", 0)
        doc.add_paragraph("AI Platform Report Generated")
        doc.save("report.docx")
        st.success("Word Document Generated")


# =====================================================

# SIDEBAR NAVIGATION

# =====================================================

menu = st.sidebar.radio("Navigation", [
"Dashboard",
"Chatbot",
"AI Taxonomy",
"Mermaid Diagrams",
"Export System"
])

# =====================================================

# ROUTING

# =====================================================

if menu == "Dashboard":
st.title("📊 Dashboard")
st.write("Enterprise AI Platform Overview")

elif menu == "Chatbot":
chatbot()

elif menu == "AI Taxonomy":
taxonomy()

elif menu == "Mermaid Diagrams":
mermaid()

elif menu == "Export System":
export_system()

# =====================================================

# FOOTER

# =====================================================

st.markdown("---")
st.markdown("""

<div style='text-align:center;color:#0056D2;font-weight:bold;'>
Enterprise AI Platform | KNet Consulting Group
</div>
""", unsafe_allow_html=True)
