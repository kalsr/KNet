
# Supply-Chain-Risk-Management-Framework


# scrm_streamlit_app.py

import streamlit as st
import json
import io
from datetime import datetime
import pandas as pd

try:
    from docx import Document
except ImportError:
    Document = None

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
except ImportError:
    canvas = None

# ------------------------------------------------------------------------------------
# Core SCRM knowledge base (categories 1–7, with details, examples, and Mermaid flows)
# ------------------------------------------------------------------------------------

SCRM_CATEGORIES = {
    1: {
        "name": "SCRM Stakeholders Tiers",
        "description": (
            "This category models organizational stakeholders across three tiers: "
            "executive leadership, mission/business management, and systems management. "
            "It aligns with NIST-style multi-tier risk management for ICT supply chains."
        ),
        "subcategories": {
            "Tier 1 – Organization Stakeholders": {
                "text": (
                    "Executive Leadership (CEO, CIO, COO, CFO, CISO, CTO, etc.) "
                    "provide risk executive functions. Tier 1 activities help to ensure "
                    "that ICT SCRM mitigation strategies are cost‑effective, efficient, "
                    "and consistent with the strategic goals and objectives of the "
                    "organization.\n\n"
                    "Typical Tier‑1 responsibilities:\n"
                    "- Define corporate strategy, policy, goals, and objectives.\n"
                    "- Establish ICT SCRM policies based on external and organizational "
                    "requirements (laws, regulations, standards).\n"
                    "- Set risk tolerance for ICT supply chain risks.\n"
                    "- Charter an ICT SCRM team and ensure integration with enterprise "
                    "risk management.\n"
                ),
                "examples": [
                    "Board of directors approves an enterprise SCRM policy that mandates "
                    "supplier security assessments for all critical ICT components.",
                    "CISO defines acceptable risk thresholds for using offshore software "
                    "development vendors.",
                ],
                "mermaid": """
flowchart TD
    A[Executive Leadership] --> B[Define SCRM Policy]
    B --> C[Set Risk Tolerance]
    C --> D[Charter ICT SCRM Team]
    D --> E[Integrate with Enterprise Risk Management]
"""
            },
            "Tier 1 – Organization Activities": {
                "text": (
                    "Tier‑1 activities operationalize strategy into concrete policies and "
                    "enterprise‑wide practices.\n\n"
                    "Key activities:\n"
                    "- Establish ICT SCRM policies and funding models.\n"
                    "- Map mission/business requirements (cost, schedule, performance, "
                    "security, privacy, quality, safety) to SCRM needs.\n"
                    "- Ensure SCRM requirements are embedded in corporate processes "
                    "(procurement, architecture, operations).\n"
                ),
                "examples": [
                    "Enterprise procurement policy requires security clauses in all ICT "
                    "contracts, including SBOM and incident‑notification SLAs.",
                    "Corporate architecture board mandates that all new systems include "
                    "supplier risk assessments during design reviews.",
                ],
                "mermaid": """
flowchart TD
    P[Corporate Strategy] --> Q[Define SCRM Policy]
    Q --> R[Map Mission Requirements]
    R --> S[Embed in Procurement & Architecture]
    S --> T[Continuous Policy Review]
"""
            },
            "Tier 2 – Mission Stakeholders": {
                "text": (
                    "Business Management (program management, R&D, engineering, "
                    "acquisitions, cost accounting, quality, safety, security) own "
                    "mission/business processes.\n\n"
                    "They translate enterprise SCRM policy into program‑level "
                    "requirements and manage trust relationships with system integrators, "
                    "suppliers, and service providers."
                ),
                "examples": [
                    "Program manager for a critical logistics system defines supplier "
                    "onboarding criteria including security certifications and audit rights.",
                    "Engineering lead requires secure development practices and code "
                    "escrow for third‑party software components.",
                ],
                "mermaid": """
flowchart TD
    A1[Mission Owner] --> B1[Define Program Requirements]
    B1 --> C1[Include SCRM Controls]
    C1 --> D1[Select Trusted Suppliers]
    D1 --> E1[Monitor Supplier Performance]
"""
            },
            "Tier 2 – Mission Activities": {
                "text": (
                    "Tier‑2 activities focus on mission/business processes:\n"
                    "- Define risk response strategies for critical processes.\n"
                    "- Establish ICT SCRM processes to support missions.\n"
                    "- Determine SCRM requirements for mission systems.\n"
                    "- Integrate SCRM into enterprise architecture and program governance."
                ),
                "examples": [
                    "Mission owner defines contingency plans for supplier disruption, "
                    "including alternate vendors and stockpiling critical components.",
                    "Business process team adds supplier risk checkpoints to change "
                    "management workflows.",
                ],
                "mermaid": """
flowchart TD
    M[Mission Process] --> N[Identify Critical Dependencies]
    N --> O[Define SCRM Requirements]
    O --> P[Integrate into Architecture]
    P --> Q[Implement Controls in Systems]
"""
            },
            "Tier 3 – Information Systems Stakeholders": {
                "text": (
                    "Systems Management (architects, developers, system owners, QA/QC, "
                    "testers, contracting personnel, maintenance and disposal teams) "
                    "implement SCRM at the system level.\n\n"
                    "They decide how to acquire, integrate, operate, and retire ICT "
                    "components in line with SCRM policies."
                ),
                "examples": [
                    "System architect chooses only hardware from vetted suppliers with "
                    "secure manufacturing and tamper‑evident packaging.",
                    "QA team adds supply‑chain‑focused test cases (e.g., firmware integrity "
                    "checks) to regression suites.",
                ],
                "mermaid": """
flowchart TD
    S1[System Architect] --> T1[Select Components]
    T1 --> U1[Apply SCRM Requirements]
    U1 --> V1[Implement & Test]
    V1 --> W1[Operate & Monitor]
    W1 --> X1[Retire Securely]
"""
            },
            "Tier 3 – Information Systems Activities": {
                "text": (
                    "Tier‑3 activities integrate SCRM into the SDLC:\n"
                    "- Apply, monitor, and manage SCRM controls in system development and sustainment.\n"
                    "- Apply SCRM controls to the SDLC environment (build pipelines, repositories, CI/CD).\n"
                    "- Address acquisition, requirements, design, development, delivery, installation, "
                    "integration, maintenance, and disposal with supply‑chain awareness."
                ),
                "examples": [
                    "DevOps team enforces signed artifacts and provenance tracking in CI/CD pipelines.",
                    "Operations team maintains an asset inventory with supplier metadata and lifecycle status.",
                ],
                "mermaid": """
flowchart TD
    SDLC[Secure SDLC] --> Req[Secure Requirements]
    Req --> Design[Secure Design]
    Design --> Dev[Secure Development]
    Dev --> Deploy[Secure Deployment]
    Deploy --> Ops[Secure Operations]
    Ops --> Retire[Secure Disposal]
"""
            },
        },
    },
    2: {
        "name": "Supply Chain Threat Agents",
        "description": (
            "Threat agents are entities that can intentionally or unintentionally "
            "compromise the supply chain—such as nation‑states, criminal groups, "
            "insiders, or negligent partners."
        ),
        "subcategories": {
            "External Adversaries": {
                "text": (
                    "Nation‑states, organized crime, hacktivists, and competitors may "
                    "target ICT supply chains to insert malicious components, steal IP, "
                    "or disrupt operations."
                ),
                "examples": [
                    "A nation‑state compromises a firmware supplier to implant backdoors "
                    "in networking equipment.",
                    "A criminal group tampers with shipping labels to divert high‑value "
                    "hardware to black markets.",
                ],
                "mermaid": """
flowchart TD
    A[External Adversary] --> B[Compromise Supplier]
    B --> C[Insert Malicious Component]
    C --> D[Deploy to Organization]
    D --> E[Exploit in Production]
"""
            },
            "Insiders and Partners": {
                "text": (
                    "Employees, contractors, and partner staff can abuse access or make "
                    "errors that introduce supply‑chain risk."
                ),
                "examples": [
                    "A disgruntled engineer leaks design files for a critical chip to a competitor.",
                    "A partner misconfigures access controls on a shared repository, exposing source code.",
                ],
                "mermaid": """
flowchart TD
    I[Insider/Partner] --> J[Abuse Access]
    J --> K[Leak IP / Tamper Components]
    K --> L[Impact Organization]
"""
            },
        },
    },
    3: {
        "name": "Supply Chain Threat Considerations",
        "description": (
            "Threat considerations focus on how, where, and when threats can manifest "
            "across the supply chain lifecycle."
        ),
        "subcategories": {
            "Lifecycle Stages": {
                "text": (
                    "Threats can appear during design, manufacturing, integration, "
                    "distribution, operation, and disposal.\n\n"
                    "Each stage has unique exposure: design tampering, counterfeit parts, "
                    "compromised logistics, or insecure recycling."
                ),
                "examples": [
                    "Design stage: malicious modification of PCB layouts to add hidden debug ports.",
                    "Manufacturing stage: counterfeit chips mixed into legitimate batches.",
                ],
                "mermaid": """
flowchart TD
    D[Design] --> M[Manufacturing]
    M --> I[Integration]
    I --> L[Logistics]
    L --> O[Operation]
    O --> R[Retirement]
"""
            },
            "Attack Vectors": {
                "text": (
                    "Common vectors include compromised tooling, insecure repositories, "
                    "unverified components, weak contracts, and opaque supplier chains."
                ),
                "examples": [
                    "Build tools infected with malware that injects malicious code into binaries.",
                    "Third‑party libraries pulled from untrusted repositories without integrity checks.",
                ],
                "mermaid": """
flowchart TD
    AV[Attack Vector] --> Tool[Compromised Tooling]
    AV --> Repo[Insecure Repositories]
    AV --> Comp[Unverified Components]
    AV --> Contract[Weak Contract Terms]
"""
            },
        },
    },
    4: {
        "name": "Supply Chain Vulnerability Considerations",
        "description": (
            "Vulnerabilities are weaknesses in processes, technology, or people that "
            "allow threats to succeed."
        ),
        "subcategories": {
            "Process Vulnerabilities": {
                "text": (
                    "Lack of supplier vetting, missing SBOMs, weak change control, and "
                    "poor incident response create exploitable gaps."
                ),
                "examples": [
                    "No formal supplier risk assessment before onboarding new hardware vendors.",
                    "Change requests that bypass security review for urgent hotfixes.",
                ],
                "mermaid": """
flowchart TD
    PV[Process Weakness] --> SV[Supplier Vetting Gap]
    PV --> CC[Weak Change Control]
    PV --> IR[Poor Incident Response]
"""
            },
            "Technical Vulnerabilities": {
                "text": (
                    "Unsigned firmware, insecure update channels, lack of integrity "
                    "checks, and missing telemetry increase risk."
                ),
                "examples": [
                    "Devices accept unsigned firmware updates over HTTP.",
                    "No runtime attestation or integrity monitoring for critical components.",
                ],
                "mermaid": """
flowchart TD
    TV[Technical Weakness] --> FW[Unsigned Firmware]
    TV --> UC[Insecure Update Channel]
    TV --> IM[Missing Integrity Monitoring]
"""
            },
        },
    },
    5: {
        "name": "Supply Chain Constraints",
        "description": (
            "Constraints are practical limits—budget, schedule, regulatory, "
            "geopolitical, and technical—that shape SCRM decisions."
        ),
        "subcategories": {
            "Business Constraints": {
                "text": (
                    "Cost, time‑to‑market, and contractual obligations may restrict "
                    "supplier choices or depth of assessments."
                ),
                "examples": [
                    "Project deadline forces use of existing supplier without full security audit.",
                    "Budget limitations prevent deploying hardware attestation on all endpoints.",
                ],
                "mermaid": """
flowchart TD
    BC[Business Constraints] --> SC[Supplier Choice]
    BC --> DA[Depth of Assessment]
    BC --> CT[Control Trade-offs]
"""
            },
            "Regulatory and Geopolitical Constraints": {
                "text": (
                    "Export controls, data residency laws, and sanctions influence where "
                    "and how components can be sourced and operated."
                ),
                "examples": [
                    "Sanctions prohibit purchasing chips from certain regions, requiring redesign.",
                    "Data residency laws mandate local hosting, limiting cloud provider options.",
                ],
                "mermaid": """
flowchart TD
    RG[Regulation] --> EC[Export Controls]
    RG --> DR[Data Residency]
    RG --> SAN[Sanctions]
"""
            },
        },
    },
    6: {
        "name": "Supply Chain Vulnerabilities Mapped to Organizations",
        "description": (
            "This category maps specific vulnerabilities to organizational tiers, "
            "functions, and systems to prioritize remediation."
        ),
        "subcategories": {
            "Tier Mapping": {
                "text": (
                    "Vulnerabilities are mapped to Tier‑1 (policy/strategy), Tier‑2 "
                    "(mission/process), and Tier‑3 (systems/implementation) to clarify "
                    "ownership and remediation paths."
                ),
                "examples": [
                    "Tier‑1: absence of enterprise SCRM policy.\n"
                    "Tier‑2: mission program lacks supplier risk register.\n"
                    "Tier‑3: system accepts unsigned third‑party plugins.",
                ],
                "mermaid": """
flowchart TD
    V[Vulnerability] --> T1[Tier 1 - Policy]
    V --> T2[Tier 2 - Mission]
    V --> T3[Tier 3 - Systems]
"""
            },
            "Organizational Heatmap": {
                "text": (
                    "Heatmaps visualize concentration of vulnerabilities across "
                    "departments, systems, and suppliers."
                ),
                "examples": [
                    "Heatmap shows high risk in legacy logistics systems relying on "
                    "single‑source suppliers.",
                    "Supplier heatmap highlights two vendors with repeated security incidents.",
                ],
                "mermaid": """
flowchart TD
    HM[Heatmap] --> Dept[Departments]
    HM --> Sys[Systems]
    HM --> Sup[Suppliers]
"""
            },
        },
    },
    7: {
        "name": "SCRM Plan Controls at Tiers 1, 2, & 3",
        "description": (
            "Controls are specific measures applied at each tier to reduce supply‑chain risk."
        ),
        "subcategories": {
            "Tier 1 Controls": {
                "text": (
                    "Enterprise‑level controls:\n"
                    "- Formal SCRM policy and governance.\n"
                    "- Central SCRM office or team.\n"
                    "- Standardized supplier risk framework and scoring.\n"
                    "- Board‑level reporting on supply‑chain risk."
                ),
                "examples": [
                    "Quarterly board report includes supply‑chain risk metrics and remediation status.",
                    "Enterprise SCRM office maintains a unified supplier risk register.",
                ],
                "mermaid": """
flowchart TD
    C1[Tier 1 Controls] --> P1[SCRM Policy]
    C1 --> G1[Governance Board]
    C1 --> F1[Risk Framework]
"""
            },
            "Tier 2 Controls": {
                "text": (
                    "Mission/process‑level controls:\n"
                    "- Supplier onboarding and offboarding procedures.\n"
                    "- Contractual security clauses and SLAs.\n"
                    "- Mission‑specific risk registers and playbooks."
                ),
                "examples": [
                    "Program contracts require SBOM, vulnerability disclosure, and incident response SLAs.",
                    "Mission risk register includes supplier disruption scenarios and mitigations.",
                ],
                "mermaid": """
flowchart TD
    C2[Tier 2 Controls] --> Onb[Onboarding Process]
    C2 --> SLA[Security SLAs]
    C2 --> RR[Risk Register]
"""
            },
            "Tier 3 Controls": {
                "text": (
                    "System‑level controls:\n"
                    "- Secure SDLC with supply‑chain checks.\n"
                    "- Integrity verification (signatures, attestation).\n"
                    "- Runtime monitoring and logging with supplier context.\n"
                    "- Secure decommissioning and data sanitization."
                ),
                "examples": [
                    "Build pipeline verifies signatures of all third‑party libraries.",
                    "Decommissioning procedure includes secure wiping and supplier notification.",
                ],
                "mermaid": """
flowchart TD
    C3[Tier 3 Controls] --> SDLC3[Secure SDLC]
    C3 --> INT3[Integrity Verification]
    C3 --> MON3[Monitoring]
    C3 --> DEC3[Secure Decommissioning]
"""
            },
        },
    },
}

# ------------------------------------------------------------------------------------
# Helper functions for export
# ------------------------------------------------------------------------------------

def build_text_export(category_id, subcat_key):
    cat = SCRM_CATEGORIES[category_id]
    sub = cat["subcategories"][subcat_key]
    lines = []
    lines.append(f"SCRM Category {category_id}: {cat['name']}")
    lines.append(f"Subcategory: {subcat_key}")
    lines.append("")
    lines.append("Description:")
    lines.append(cat["description"])
    lines.append("")
    lines.append("Details:")
    lines.append(sub["text"])
    lines.append("")
    lines.append("Real-world examples:")
    for ex in sub["examples"]:
        lines.append(f"- {ex}")
    lines.append("")
    lines.append("Mermaid conceptual flow:")
    lines.append(sub["mermaid"])
    return "\n".join(lines)


def build_docx_export(category_id, subcat_key):
    if Document is None:
        return None
    cat = SCRM_CATEGORIES[category_id]
    sub = cat["subcategories"][subcat_key]
    doc = Document()
    doc.add_heading(f"SCRM Category {category_id}: {cat['name']}", level=1)
    doc.add_heading(f"Subcategory: {subcat_key}", level=2)
    doc.add_paragraph("Description:")
    doc.add_paragraph(cat["description"])
    doc.add_paragraph("Details:")
    doc.add_paragraph(sub["text"])
    doc.add_paragraph("Real-world examples:")
    for ex in sub["examples"]:
        doc.add_paragraph(f"- {ex}")
    doc.add_paragraph("Mermaid conceptual flow:")
    doc.add_paragraph(sub["mermaid"])
    buf = io.BytesIO()
    doc.save(buf)
    buf.seek(0)
    return buf


def build_pdf_export(category_id, subcat_key):
    if canvas is None:
        return None
    cat = SCRM_CATEGORIES[category_id]
    sub = cat["subcategories"][subcat_key]
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter)
    width, height = letter
    y = height - 50
    def draw_line(text, y_pos):
        c.drawString(40, y_pos, text)
        return y_pos - 15

    y = draw_line(f"SCRM Category {category_id}: {cat['name']}", y)
    y = draw_line(f"Subcategory: {subcat_key}", y)
    y = draw_line("", y)
    y = draw_line("Description:", y)
    for line in cat["description"].split("\n"):
        y = draw_line(line[:100], y)
    y = draw_line("", y)
    y = draw_line("Details:", y)
    for line in sub["text"].split("\n"):
        if y < 80:
            c.showPage()
            y = height - 50
        y = draw_line(line[:100], y)
    y = draw_line("", y)
    y = draw_line("Real-world examples:", y)
    for ex in sub["examples"]:
        if y < 80:
            c.showPage()
            y = height - 50
        y = draw_line(f"- {ex[:100]}", y)
    c.showPage()
    c.save()
    buf.seek(0)
    return buf


def build_json_export(category_id, subcat_key):
    cat = SCRM_CATEGORIES[category_id]
    sub = cat["subcategories"][subcat_key]
    payload = {
        "category_id": category_id,
        "category_name": cat["name"],
        "subcategory": subcat_key,
        "description": cat["description"],
        "details": sub["text"],
        "examples": sub["examples"],
        "mermaid": sub["mermaid"],
        "exported_at": datetime.utcnow().isoformat() + "Z",
    }
    return json.dumps(payload, indent=2)


def generate_synthetic_scrm_data(num_rows: int = 20):
    records = []
    tiers = ["Tier 1", "Tier 2", "Tier 3"]
    risk_levels = ["Low", "Medium", "High", "Critical"]
    for i in range(num_rows):
        records.append({
            "id": i + 1,
            "tier": tiers[i % len(tiers)],
            "asset": f"System-{(i % 5) + 1}",
            "supplier": f"Supplier-{(i % 7) + 1}",
            "risk_level": risk_levels[i % len(risk_levels)],
            "vulnerability": "Unsigned firmware" if i % 3 == 0 else "Weak supplier vetting",
            "threat_agent": "External adversary" if i % 2 == 0 else "Insider/partner",
        })
    return pd.DataFrame(records)

# ------------------------------------------------------------------------------------
# Streamlit UI
# ------------------------------------------------------------------------------------

st.set_page_config(
    page_title="SCRM Framework Dashboard",
    layout="wide",
)

st.title("Supply Chain Risk Management (SCRM) Framework Dashboard")

st.markdown(
    "> Executive Leadership (CEO, CIO, COO, CFO, CISO, CTO, etc.) provide risk "
    "executive functions and help ensure that ICT SCRM mitigation strategies are "
    "cost‑effective, efficient, and consistent with strategic goals."
)

st.sidebar.header("Navigation")

category_ids = sorted(SCRM_CATEGORIES.keys())
category_labels = [f"{cid}. {SCRM_CATEGORIES[cid]['name']}" for cid in category_ids]
selected_label = st.sidebar.selectbox("Select SCRM Category", category_labels)
selected_category_id = int(selected_label.split(".")[0])
selected_category = SCRM_CATEGORIES[selected_category_id]

subcat_keys = list(selected_category["subcategories"].keys())
selected_subcat_key = st.sidebar.selectbox("Select Subcategory", subcat_keys)

st.sidebar.markdown("---")
st.sidebar.subheader("Exports & Synthetic Data")

# Main layout
col_main, col_side = st.columns([3, 2])

with col_main:
    st.header(f"{selected_category_id}. {selected_category['name']}")
    st.subheader(selected_subcat_key)

    st.markdown("**Category description:**")
    st.write(selected_category["description"])

    st.markdown("**Detailed framework text:**")
    st.write(selected_category["subcategories"][selected_subcat_key]["text"])

    st.markdown("**Real-world examples:**")
    for ex in selected_category["subcategories"][selected_subcat_key]["examples"]:
        st.markdown(f"- {ex}")

    st.markdown("**Conceptual flow (Mermaid diagram):**")
    st.markdown(
        f"```mermaid\n{selected_category['subcategories'][selected_subcat_key]['mermaid']}\n```"
    )

with col_side:
    st.subheader("Export current view")

    text_content = build_text_export(selected_category_id, selected_subcat_key)
    st.download_button(
        label="Download as TXT",
        data=text_content,
        file_name=f"scrm_category_{selected_category_id}_{selected_subcat_key}.txt",
        mime="text/plain",
    )

    json_content = build_json_export(selected_category_id, selected_subcat_key)
    st.download_button(
        label="Download as JSON",
        data=json_content,
        file_name=f"scrm_category_{selected_category_id}_{selected_subcat_key}.json",
        mime="application/json",
    )

    docx_buf = build_docx_export(selected_category_id, selected_subcat_key)
    if docx_buf is not None:
        st.download_button(
            label="Download as Word (DOCX)",
            data=docx_buf,
            file_name=f"scrm_category_{selected_category_id}_{selected_subcat_key}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
    else:
        st.info("Install `python-docx` to enable Word export.")

    pdf_buf = build_pdf_export(selected_category_id, selected_subcat_key)
    if pdf_buf is not None:
        st.download_button(
            label="Download as PDF",
            data=pdf_buf,
            file_name=f"scrm_category_{selected_category_id}_{selected_subcat_key}.pdf",
            mime="application/pdf",
        )
    else:
        st.info("Install `reportlab` to enable PDF export.")

    st.markdown("---")
    st.subheader("Synthetic SCRM Data Generator")

    num_rows = st.slider("Number of synthetic records", min_value=5, max_value=100, value=20)
    if st.button("Generate synthetic SCRM dataset"):
        df = generate_synthetic_scrm_data(num_rows)
        st.dataframe(df, use_container_width=True)

        csv_buf = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download synthetic data (CSV)",
            data=csv_buf,
            file_name="synthetic_scrm_data.csv",
            mime="text/csv",
        )

        json_buf = df.to_json(orient="records", indent=2).encode("utf-8")
        st.download_button(
            label="Download synthetic data (JSON)",
            data=json_buf,
            file_name="synthetic_scrm_data.json",
            mime="application/json",
        )

st.markdown("---")
st.caption("SCRM Framework Streamlit App – based on multi-tier supply chain risk management concepts.")
