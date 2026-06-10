import streamlit as st
import pandas as pd
import json

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(page_title="AI Enterprise Platform", layout="wide")

# =====================================================
# HEADER (BOLD BLUE)
# =====================================================
st.markdown("""
<div style='background-color:#0056D2;padding:18px;border-radius:10px;text-align:center;'>
<h1 style='color:white;font-weight:bold;margin:0;'>
ARTIFICIAL INTELLIGENCE ENTERPRISE PLATFORM
</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
### 🔷 **Developed by Randy Singh – Kalsnet (KNet) Consulting Group**
""", unsafe_allow_html=True)

# =====================================================
# NAVIGATION STATE
# =====================================================
if "view" not in st.session_state:
    st.session_state.view = "main"

# =====================================================
# BACK BUTTON (FOR LLM EXTERNAL VIEW FLOW)
# =====================================================
def back_button():
    if st.button("⬅ Back to Platform"):
        st.session_state.view = "main"

# =====================================================
# DASHBOARD
# =====================================================
def dashboard():

    st.subheader("📊 Executive Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("AI Modules", "8+")
    col2.metric("LLMs", "15+")
    col3.metric("System Status", "🟢 Active")

    st.markdown("## 🧠 Core Platform Architecture")

    st.graphviz_chart("""
    digraph {
        User -> Dashboard
        Dashboard -> AI_Engine
        AI_Engine -> RAG_System
        AI_Engine -> LLM_Hub
        RAG_System -> Vector_DB
        LLM_Hub -> Response_Engine
    }
    """)

    st.markdown("""
### 🔷 Core Platform Modules (with Use Cases & Benefits)

- 🤖 Chatbot Engine  
  Use: Customer support, AI assistants  
  Benefit: Reduces manual workload, improves response speed  

- 🧠 RAG System  
  Use: Document Q&A, enterprise search  
  Benefit: Improves accuracy, reduces hallucinations  

- 📚 Taxonomy Engine  
  Use: AI classification, research structuring  
  Benefit: Organizes knowledge for better understanding  

- 🌐 LLM Hub  
  Use: Switching between AI models  
  Benefit: Best response quality via model selection  

- 📄 Export Engine  
  Use: Reports, documentation  
  Benefit: Fast compliance & reporting automation  
""")

# =====================================================
# TAXONOMY & FRAMEWORK
# =====================================================
def taxonomy_framework():

    st.subheader("🧠 AI Taxonomy vs Framework")

    st.markdown("""
## 📌 AI Taxonomy (WHAT exists)

- Machine Learning → predictions, fraud detection
- Deep Learning → LLMs, vision systems
- NLP → chatbots, translation
- Computer Vision → drones, healthcare imaging

### ✔ Benefits
- Structured AI understanding
- Easier research & design

---

## 🏗 AI Framework (HOW it works)

- Data Layer → datasets
- Model Layer → AI models
- API Layer → integration
- Application Layer → apps

### ✔ Benefits
- Scalable architecture
- Modular system design
""")

# =====================================================
# AI MODULES (ENHANCED)
# =====================================================
def ai_modules():

    st.subheader("🤖 AI Modules Overview")

    modules = [
        ("Classical AI", "Rule-based systems used in expert systems, fraud detection → Benefit: fast deterministic decisions"),
        ("Machine Learning", "Predictive systems like recommendation engines → Benefit: learns from data automatically"),
        ("Deep Learning", "Neural networks powering ChatGPT & vision AI → Benefit: handles complex patterns"),
        ("NLP", "Chatbots, translation, sentiment analysis → Benefit: improves human-computer interaction"),
        ("Computer Vision", "Image recognition, drones, medical imaging → Benefit: automated visual understanding"),
        ("RAG", "Combines search + LLMs → Benefit: accurate enterprise AI answers"),
        ("AI Agents", "Autonomous AI workflows → Benefit: task automation"),
        ("Generative AI", "Creates text, images, code → Benefit: accelerates content creation")
    ]

    for name, desc in modules:
        st.markdown(f"### 🔹 {name}")
        st.write(desc)

# =====================================================
# LLM HUB (CLICKABLE LINKS)
# =====================================================
def llms():

    st.subheader("🌐 Top LLMs (Click to Open)")

    models = [
        ("GPT-4 / ChatGPT", "https://chat.openai.com"),
        ("Claude", "https://claude.ai"),
        ("Gemini", "https://gemini.google.com"),
        ("LLaMA", "https://ai.meta.com/llama"),
        ("Mistral", "https://mistral.ai"),
        ("Cohere", "https://cohere.com"),
        ("DeepSeek", "https://chat.deepseek.com"),
        ("Perplexity AI", "https://www.perplexity.ai"),
    ]

    for name, link in models:
        if st.button(name):
            st.session_state.view = link

# =====================================================
# EXTERNAL VIEW HANDLER
# =====================================================
def external_view(url):
    st.subheader("🌐 External AI Model")

    st.markdown(f"""
### You are now viewing:

👉 [{url}]({url})

(Click link above to access model)
""")

    back_button()

# =====================================================
# EXPORT SYSTEM
# =====================================================
def export_system():

    st.subheader("📄 Export Center")

    # -----------------------------
    # SAMPLE REPORT DATA
    # -----------------------------
    report_data = {
        "Platform": "AI Enterprise System",
        "Sections": [
            "Taxonomy Analysis",
            "Framework Overview",
            "LLM Comparison",
            "AI Modules Report"
        ],
        "Status": "Ready for Export"
    }

    df = pd.DataFrame({
        "Report Type": ["Taxonomy Report", "Framework Report", "LLM Report"],
        "Status": ["Ready", "Ready", "Ready"]
    })

    # -----------------------------
    # PREVIEW SECTION (ALWAYS VISIBLE)
    # -----------------------------
    st.markdown("## 📊 Report Preview")

    st.dataframe(df)

    st.markdown("### JSON Preview")
    st.json(report_data)

    # -----------------------------
    # ACTION BUTTONS
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        if st.button("📄 Generate PDF Report"):
            st.session_state.pdf_done = True

    with col2:
        if st.button("📝 Generate Word Report"):
            st.session_state.word_done = True

    # -----------------------------
    # CONDITIONAL STATUS MESSAGES
    # -----------------------------
    if "pdf_done" in st.session_state and st.session_state.pdf_done:
        st.success("✅ PDF Report Generated Successfully")

    if "word_done" in st.session_state and st.session_state.word_done:
        st.success("✅ Word Report Generated Successfully")

# =====================================================
# SIDEBAR NAVIGATION
# =====================================================
menu = st.sidebar.radio("Navigation", [
    "Dashboard",
    "Taxonomy & Framework",
    "AI Modules",
    "LLMs",
    "Export Center"
])

# =====================================================
# ROUTING
# =====================================================
if st.session_state.view != "main":
    external_view(st.session_state.view)

else:
    if menu == "Dashboard":
        dashboard()

    elif menu == "Taxonomy & Framework":
        taxonomy_framework()

    elif menu == "AI Modules":
        ai_modules()

    elif menu == "LLMs":
        llms()

    elif menu == "Export Center":
        export_system()

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.markdown("""
<div style='text-align:center;color:#0056D2;font-weight:bold;font-size:16px;'>
AI Enterprise Platform | Developed by Randy Singh – Kalsnet (KNet) Consulting Group
</div>
""", unsafe_allow_html=True)
