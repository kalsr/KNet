

# =========================================================
# AI Governance & Public Policy Intelligence Platform Builder
# Streamlit Cloud Safe Version
# Developed by Randy Singh from Kalsnet (KNet) Consulting Group
# =========================================================

import streamlit as st
from pathlib import Path
from zipfile import ZipFile
from textwrap import dedent
from docx import Document
from docx.shared import Pt
import json

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Governance Platform Builder",
    layout="wide",
    page_icon="🏛️"
)

# =========================================================
# HEADER
# =========================================================

st.title("🏛️ AI Governance & Public Policy Intelligence Platform Builder")
st.subheader("Developed by Randy Singh from Kalsnet (KNet) Consulting Group")

st.markdown("""
This utility automatically generates a complete enterprise-grade project package
including:

- README.md
- requirements.txt
- Streamlit app.py
- SQL database schema
- Enterprise Architecture Guide (DOCX)
- GUI Mockup
- SaaS Roadmap
- Metadata JSON
- ZIP Package
""")

# =========================================================
# GENERATE PACKAGE BUTTON
# =========================================================

if st.button("🚀 Generate Complete Platform Package", use_container_width=True):

    try:
        # =========================================================
        # CREATE BASE DIRECTORY (STREAMLIT CLOUD SAFE)
        # =========================================================

        base = Path("ai_policy_platform_output")
        base.mkdir(parents=True, exist_ok=True)

        # =========================================================
        # README
        # =========================================================

        readme = dedent("""
        # AI Governance & Public Policy Intelligence Platform

        ## Developed by Randy Singh from Kalsnet (KNet) Consulting Group

        This enterprise Streamlit platform demonstrates how AI can support:
        - Public policy generation
        - Government affairs intelligence
        - Compliance analysis
        - NIST/FedRAMP mapping
        - RAG document search
        - Multi-agent AI workflows
        - Secure document exports
        """)

        (base / "README.md").write_text(readme, encoding="utf-8")

        # =========================================================
        # REQUIREMENTS
        # =========================================================

        requirements = """
streamlit
groq
pandas
python-docx
reportlab
langchain
chromadb
sentence-transformers
pypdf
bcrypt
sqlalchemy
streamlit-authenticator
"""

        (base / "requirements.txt").write_text(
            requirements.strip() + "\n",
            encoding="utf-8"
        )

        # =========================================================
        # APP.PY
        # =========================================================

        app_code = dedent("""
        import streamlit as st

        st.set_page_config(page_title="AI Governance Platform", layout="wide")

        st.title("AI Governance & Public Policy Intelligence Platform")
        st.subheader("Developed by Randy Singh from Kalsnet (KNet) Consulting Group")

        st.success("Application package generated successfully.")
        """)

        (base / "app.py").write_text(app_code, encoding="utf-8")

        # =========================================================
        # DATABASE SCHEMA
        # =========================================================

        schema = dedent("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password_hash TEXT,
            role TEXT,
            created_at TIMESTAMP
        );

        CREATE TABLE policies (
            id INTEGER PRIMARY KEY,
            policy_name TEXT,
            policy_type TEXT,
            generated_text TEXT,
            created_by INTEGER,
            created_at TIMESTAMP
        );

        CREATE TABLE audit_logs (
            id INTEGER PRIMARY KEY,
            username TEXT,
            action TEXT,
            timestamp TIMESTAMP
        );
        """)

        (base / "database_schema.sql").write_text(schema, encoding="utf-8")

        # =========================================================
        # ENTERPRISE ARCHITECTURE GUIDE (DOCX)
        # =========================================================

        doc = Document()

        title = doc.add_heading(
            "AI Governance & Public Policy Intelligence Platform",
            level=1
        )
        title.runs[0].font.size = Pt(22)

        subtitle = doc.add_heading(
            "Developed by Randy Singh from Kalsnet (KNet) Consulting Group",
            level=2
        )
        subtitle.runs[0].font.size = Pt(16)

        sections = {
            "1. Full Enterprise Architecture":
                "Frontend: Streamlit, Backend: Python APIs, AI Layer: Groq LLM, Database: PostgreSQL, Vector DB: ChromaDB.",
            "2. RAG Implementation":
                "ChromaDB vector database with LangChain retrieval.",
            "3. Security":
                "RBAC, MFA, encryption and audit logging.",
            "4. Multi-Agent AI":
                "Agents for policy, compliance and risk analysis.",
            "5. NIST/FedRAMP Design":
                "Supports NIST SP 800-53 and FedRAMP."
        }

        for heading, paragraph in sections.items():
            doc.add_heading(heading, level=2)
            doc.add_paragraph(paragraph)

        doc.save(str(base / "Enterprise_Architecture_Guide.docx"))

        # =========================================================
        # OTHER FILES
        # =========================================================

        (base / "project_structure.txt").write_text(
            "app.py\nrequirements.txt\nREADME.md\n",
            encoding="utf-8"
        )

        (base / "gui_mockup.txt").write_text(
            "Sidebar: API Key, Policy Selection, Export Options",
            encoding="utf-8"
        )

        (base / "saas_roadmap.txt").write_text(
            "Phase 1: MVP\nPhase 2: Enterprise\nPhase 3: Government Cloud",
            encoding="utf-8"
        )

        metadata = {
            "project": "AI Governance & Public Policy Intelligence Platform",
            "developer": "Randy Singh from Kalsnet (KNet) Consulting Group",
            "version": "1.0"
        }

        (base / "metadata.json").write_text(
            json.dumps(metadata, indent=4),
            encoding="utf-8"
        )

        # =========================================================
        # CREATE ZIP
        # =========================================================

        zip_path = Path("AI_Governance_Public_Policy_Platform.zip")

        with ZipFile(zip_path, "w") as z:
            for file in base.rglob("*"):
                if file.is_file():
                    z.write(file, file.relative_to(base.parent))

        # =========================================================
        # STREAMLIT OUTPUT
        # =========================================================

        st.success("✅ All files generated successfully!")

        st.info(f"📁 Output Directory: {base.resolve()}")
        st.info(f"📦 ZIP Package: {zip_path.resolve()}")

        # Download button
        with open(zip_path, "rb") as f:
            st.download_button(
                label="⬇️ Download Complete ZIP Package",
                data=f,
                file_name="AI_Governance_Public_Policy_Platform.zip",
                mime="application/zip",
                use_container_width=True
            )

        # Show generated files
        st.subheader("📂 Generated Files")
        for file in sorted(base.rglob("*")):
            if file.is_file():
                st.write(f"• {file.name}")

    except Exception as e:
        st.error(f"Error: {e}")