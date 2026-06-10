import streamlit as st
import pandas as pd
import json
from docx import Document
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(page_title="AI Enterprise Platform", layout="wide")

# =====================================================
# SIMPLE LOGIN
# =====================================================
USERS = {
    "admin": "admin123",
    "user": "user123"
}

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
    st.stop()

# =====================================================
# HEADER
# =====================================================
st.title("🚀 AI Enterprise Knowledge Platform")
st.markdown("Taxonomy | Framework | LLMs | RAG | Export System")

# =====================================================
# DASHBOARD
# =====================================================
def dashboard():
    st.subheader("📊 Executive Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("AI Modules", "5+")
    col2.metric("LLMs Supported", "5")
    col3.metric("System Status", "Active")

    st.markdown("### 🧠 System Architecture")
    st.graphviz_chart("""
    digraph {
        User -> Chatbot
        Chatbot -> RAG_System
        RAG_System -> VectorDB
        Chatbot -> LLMs
    }
    """)

# =====================================================
# TAXONOMY VS FRAMEWORK EXPLAINER
# =====================================================
def theory_section():
    st.subheader("🧠 AI Taxonomy vs Framework")

    st.markdown("""
### 📌 What is AI Taxonomy?
AI Taxonomy is the **classification system of AI technologies**.

It organizes AI into categories like:
- Machine Learning
- Deep Learning
- NLP
- Computer Vision

👉 It answers: **WHAT exists in AI?**

---

### 🏗 What is AI Framework?
AI Framework is the **architecture that connects AI components together**.

It defines:
- How data flows
- How models interact
- How systems are built

👉 It answers: **HOW AI systems work together?**

---

### ⚡ Key Difference

| Taxonomy | Framework |
|----------|----------|
| Classification | Architecture |
| WHAT exists | HOW it works |
| Organizes knowledge | Builds systems |
""")

# =====================================================
# AI FEATURES (CLASSIC AI + RAG + GEN AI)
# =====================================================
def ai_features():
    st.subheader("🤖 AI Capability Layer")

    st.markdown("""
### 🧠 Classical AI
- Rule-based systems
- Decision trees
- Predictive models

### ✨ Generative AI
- ChatGPT, Claude, Gemini
- Content generation

### 📚 RAG (Retrieval Augmented Generation)
- Combines LLM + knowledge base
- Retrieves documents before answering
- Improves accuracy & reduces hallucinations
""")

    st.graphviz_chart("""
    digraph {
        Query -> Retriever
        Retriever -> VectorDB
        VectorDB -> LLM
        LLM -> Response
    }
    """)

# =====================================================
# LLM DIRECTORY
# =====================================================
def llm_directory():
    st.subheader("🌐 Large Language Models (LLMs)")

    data = [
        ["GPT-4 / GPT-5", "OpenAI", "General intelligence, coding, reasoning", "https://openai.com"],
        ["Claude", "Anthropic", "Safe reasoning + long context", "https://anthropic.com"],
        ["Gemini", "Google", "Multimodal + search integration", "https://deepmind.google"],
        ["LLaMA", "Meta", "Open-source LLM ecosystem", "https://ai.meta.com"],
        ["Mistral", "Mistral AI", "Fast enterprise models", "https://mistral.ai"]
    ]

    df = pd.DataFrame(data, columns=["Model", "Company", "Use Case", "Link"])
    st.dataframe(df)

# =====================================================
# EXPORT SYSTEM
# =====================================================
def export_system():

    st.subheader("📄 Export Reports")

    data = {
        "Platform": "AI Enterprise System",
        "Modules": ["Dashboard", "LLMs", "RAG", "Taxonomy"]
    }

    st.json(data)

    df = pd.DataFrame({
        "Module": ["Dashboard", "LLMs", "RAG", "Taxonomy"],
        "Status": ["Active", "Active", "Active", "Active"]
    })

    st.download_button("⬇ Download CSV", df.to_csv(index=False), "report.csv")

    st.download_button("⬇ Download JSON", json.dumps(data), "report.json")

    if st.button("Generate PDF"):
        doc = SimpleDocTemplate("report.pdf")
        styles = getSampleStyleSheet()
        doc.build([Paragraph("AI Enterprise Report", styles["Title"])])
        st.success("PDF Generated")

    if st.button("Generate Word"):
        doc = Document()
        doc.add_heading("AI Enterprise Report", 0)
        doc.add_paragraph("Generated AI System Report")
        doc.save("report.docx")
        st.success("Word Generated")

# =====================================================
# SIDEBAR NAVIGATION
# =====================================================
menu = st.sidebar.radio("Navigation", [
    "Dashboard",
    "Taxonomy vs Framework",
    "AI Features",
    "LLMs",
    "Export System"
])

# =====================================================
# ROUTING
# =====================================================
if menu == "Dashboard":
    dashboard()

elif menu == "Taxonomy vs Framework":
    theory_section()

elif menu == "AI Features":
    ai_features()

elif menu == "LLMs":
    llm_directory()

elif menu == "Export System":
    export_system()

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.caption("AI Enterprise Platform | KNet Consulting Group")
