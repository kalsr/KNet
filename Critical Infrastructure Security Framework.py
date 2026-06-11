
# Critical Infrastructure Security Framework


import streamlit as st
from io import BytesIO
import json
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random

# ---------------------------------------------------------
# Page config
# ---------------------------------------------------------
st.set_page_config(page_title="Critical Infrastructure Security Framework", layout="wide")

# ---------------------------------------------------------
# Bold blue title bar + app description
# ---------------------------------------------------------
st.markdown(
    """
    <div style="background-color:#004aad;padding:15px;border-radius:5px;">
        <h1 style="color:white;text-align:center;margin-bottom:5px;">
            Critical Infrastructure Security Framework Analyzer
        </h1>
        <h4 style="color:white;text-align:center;margin-top:0;">
            Developed by Randy Singh, Kalsnet (KNet) Consulting Group
        </h4>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    This application helps security analysts, planners, and system administrators understand and apply a 
    **Critical Infrastructure Security Framework** across DISA, DoD, and U.S. critical infrastructure.  
    It organizes 21 framework checklist items under the NIST CSF pillars (Identify, Protect, Detect, Respond, Recover), 
    providing explanations, subcategories, references, diagrams, synthetic data, and exportable reports for real‑world use.
    """
)

st.markdown("---")

# ---------------------------------------------------------
# Pillars (for two-level navigation) with colors and diagrams
# ---------------------------------------------------------
pillars = {
    "Identify": {
        "color": "#1f77b4",
        "mermaid": """
flowchart TD
    Org[Organization] --> Assets[Assets & Resources]
    Org --> BusinessEnv[Business Environment]
    Org --> Governance[Governance & Policies]
    Org --> RiskAssess[Risk Assessment]
    Org --> RiskStrategy[Risk Management Strategy]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    Organization -> "Assets & Resources";
    Organization -> "Business Environment";
    Organization -> "Governance & Policies";
    Organization -> "Risk Assessment";
    Organization -> "Risk Management Strategy";
}
""",
    },
    "Protect": {
        "color": "#2ca02c",
        "mermaid": """
flowchart TD
    Controls[Security Controls] --> Access[Access Control]
    Controls --> Training[Awareness & Training]
    Controls --> DataSec[Data Security]
    Controls --> Processes[Protection Processes]
    Controls --> Maintenance[System Maintenance]
    Controls --> Tech[Protective Technology]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    "Security Controls" -> "Access Control";
    "Security Controls" -> "Awareness & Training";
    "Security Controls" -> "Data Security";
    "Security Controls" -> "Protection Processes";
    "Security Controls" -> "System Maintenance";
    "Security Controls" -> "Protective Technology";
}
""",
    },
    "Detect": {
        "color": "#ff7f0e",
        "mermaid": """
flowchart TD
    Infra[Critical Infrastructure] --> Monitoring[Continuous Monitoring]
    Monitoring --> Anomalies[Anomalies & Events]
    Monitoring --> Detection[Detection Processes]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    "Critical Infrastructure" -> "Continuous Monitoring";
    "Continuous Monitoring" -> "Anomalies & Events";
    "Continuous Monitoring" -> "Detection Processes";
}
""",
    },
    "Respond": {
        "color": "#d62728",
        "mermaid": """
flowchart TD
    Incident[Incident] --> Plan[Response Planning]
    Plan --> Analysis[Response Analysis]
    Analysis --> Mitigation[Mitigation Activities]
    Mitigation --> Improve[Improving Response Activities]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    Incident -> "Response Planning";
    "Response Planning" -> "Response Analysis";
    "Response Analysis" -> "Mitigation Activities";
    "Mitigation Activities" -> "Improving Response Activities";
}
""",
    },
    "Recover": {
        "color": "#9467bd",
        "mermaid": """
flowchart TD
    Disruption[Service Disruption] --> RecPlan[Recovery Planning]
    RecPlan --> RecImprove[Recovery Planning Improvements]
    RecPlan --> Restore[Restoration & Communications]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    "Service Disruption" -> "Recovery Planning";
    "Recovery Planning" -> "Recovery Planning Improvements";
    "Recovery Planning" -> "Restoration & Communications";
}
""",
    },
}

# ---------------------------------------------------------
# Framework items (21 checklist entries)
# ---------------------------------------------------------
framework_items = {
    1: {
        "pillar": "Identify",
        "title": "IDENTIFY ASSET MANAGEMENT ITEMS",
        "description": (
            "Asset management ensures that all data, personnel, devices, systems, and facilities that support "
            "the mission are identified, inventoried, and prioritized according to business value and risk."
        ),
        "subcategories": [
            "Physical devices and systems are inventoried.",
            "Software platforms and applications are inventoried.",
            "Organizational communication and data flows are mapped.",
            "External information systems are catalogued.",
            "Resources are prioritized by classification, criticality, and business value.",
            "Cybersecurity roles and responsibilities are established for workforce and third parties.",
        ],
        "references": [
            "CCS CSC 1, CCS CSC 2",
            "COBIT 5 BAI09.01, BAI09.02",
            "ISO/IEC 27001:2013 A.8.1.1, A.8.1.2",
            "NIST SP 800-53 Rev. 4 CM-8",
        ],
    },
    2: {
        "pillar": "Identify",
        "title": "IDENTIFY BUSINESS ENVIRONMENT",
        "description": (
            "Business environment focuses on understanding mission, objectives, stakeholders, and the "
            "organization’s role in the supply chain and critical infrastructure to inform cybersecurity decisions."
        ),
        "subcategories": [
            "Role in the supply chain is identified and communicated.",
            "Place in critical infrastructure and sector is identified.",
            "Mission priorities and objectives are established and communicated.",
            "Dependencies and critical functions for critical services are established.",
            "Resilience requirements for critical services are defined.",
        ],
        "references": [
            "COBIT 5 APO02.06, APO03.01",
            "ISO/IEC 27001:2013 A.11.1.4, A.17.1.1",
            "NIST SP 800-53 Rev. 4 PM-8, CP-2",
        ],
    },
    3: {
        "pillar": "Identify",
        "title": "IDENTIFY GOVERNANCE POLICIES & PROCEDURES",
        "description": (
            "Governance ensures policies, procedures, and processes for regulatory, legal, risk, and operational "
            "requirements are understood and used to manage cybersecurity risk."
        ),
        "subcategories": [
            "Information security policy is established.",
            "Security roles and responsibilities are aligned internally and externally.",
            "Legal and regulatory requirements, including privacy, are understood and managed.",
            "Governance and risk management processes address cybersecurity risks.",
        ],
        "references": [
            "ISA 62443-2-1:2009 4.3.2.6",
            "ISO/IEC 27001:2013 A.5.1.1, A.18.1",
            "NIST SP 800-53 Rev. 4 PM-1, PM-9, PM-11",
        ],
    },
    4: {
        "pillar": "Identify",
        "title": "IDENTIFY RISK ASSESSMENT",
        "description": (
            "Risk assessment identifies threats, vulnerabilities, likelihood, and impact to critical infrastructure "
            "assets, informing prioritization and treatment of cybersecurity risks."
        ),
        "subcategories": [
            "Risk assessment methodology is defined and approved.",
            "Threats and vulnerabilities to critical assets are identified.",
            "Likelihood and impact of adverse events are analyzed.",
            "Risk register is maintained and updated regularly.",
        ],
        "references": [
            "NIST SP 800-30, NIST SP 800-39",
            "ISO/IEC 27005:2018",
            "COBIT 5 APO12 (Risk Management)",
        ],
    },
    5: {
        "pillar": "Identify",
        "title": "IDENTIFY RISK MANAGEMENT STRATEGY",
        "description": (
            "Risk management strategy defines how the organization will respond to risk (accept, avoid, transfer, "
            "mitigate) and align cybersecurity investments with business priorities."
        ),
        "subcategories": [
            "Risk appetite and tolerance are defined.",
            "Risk response options are documented and applied.",
            "Cybersecurity investment priorities are aligned with risk.",
            "Risk management strategy is communicated to stakeholders.",
        ],
        "references": [
            "NIST SP 800-39",
            "ISO/IEC 27001:2013 A.6.1.1",
            "COBIT 5 APO12, APO13",
        ],
    },
    6: {
        "pillar": "Protect",
        "title": "PROTECTION BY ACCESS CONTROL",
        "description": (
            "Access control ensures only authorized users, processes, and devices can access critical infrastructure "
            "systems and data, enforcing least privilege and separation of duties."
        ),
        "subcategories": [
            "Identity and access management policies are defined.",
            "Role-based access control is implemented.",
            "Privileged access is monitored and controlled.",
            "Remote access is secured and logged.",
        ],
        "references": [
            "NIST SP 800-53 Rev. 4 AC family",
            "ISO/IEC 27001:2013 A.9",
            "ISA 62443-3-3 SR 1 (Access Control)",
        ],
    },
    7: {
        "pillar": "Protect",
        "title": "PROTECTION BY AWARENESS AND TRAINING",
        "description": (
            "Awareness and training ensure personnel understand cybersecurity responsibilities, threats, and "
            "procedures, reducing human error and social engineering risks."
        ),
        "subcategories": [
            "Security awareness program is established.",
            "Role-based training is provided for critical roles.",
            "Training covers incident reporting and escalation.",
            "Training effectiveness is measured and improved.",
        ],
        "references": [
            "NIST SP 800-53 Rev. 4 AT family",
            "ISO/IEC 27001:2013 A.7.2.2",
        ],
    },
    8: {
        "pillar": "Protect",
        "title": "PROTECTION BY DATA SECURITY",
        "description": (
            "Data security protects the confidentiality, integrity, and availability of information through "
            "classification, encryption, backup, and secure handling practices."
        ),
        "subcategories": [
            "Data classification scheme is defined and applied.",
            "Encryption is used for sensitive data at rest and in transit.",
            "Backup and recovery mechanisms are implemented.",
            "Data handling and disposal procedures are enforced.",
        ],
        "references": [
            "NIST SP 800-53 Rev. 4 SC, MP families",
            "ISO/IEC 27001:2013 A.8, A.10",
        ],
    },
    9: {
        "pillar": "Protect",
        "title": "PROTECTION BY INFORMATION PROTECTION PROCESSES & PROCEDURES",
        "description": (
            "Information protection processes and procedures ensure security controls are consistently applied, "
            "maintained, and improved across critical infrastructure systems."
        ),
        "subcategories": [
            "Documented security procedures exist for key operations.",
            "Change management includes security impact analysis.",
            "Configuration management is enforced.",
            "Periodic reviews and audits of processes are performed.",
        ],
        "references": [
            "NIST SP 800-53 Rev. 4 CM, CP families",
            "ISO/IEC 27001:2013 A.12",
        ],
    },
    10: {
        "pillar": "Protect",
        "title": "PROTECTION BY MAINTENANCE OF INDUSTRIAL CONTROL & INFORMATION SYSTEMS",
        "description": (
            "Maintenance ensures industrial control systems and information systems are updated, patched, and "
            "serviced securely without introducing new vulnerabilities."
        ),
        "subcategories": [
            "Maintenance activities are authorized and logged.",
            "Patching and updates follow secure procedures.",
            "Vendor access for maintenance is controlled.",
            "Maintenance tools and media are secured.",
        ],
        "references": [
            "NIST SP 800-53 Rev. 4 MA family",
            "ISA 62443-2-1 maintenance requirements",
        ],
    },
    11: {
        "pillar": "Protect",
        "title": "PROTECTION BY USING PROTECTIVE TECHNOLOGY",
        "description": (
            "Protective technology includes firewalls, IDS/IPS, endpoint protection, and other technical controls "
            "that enforce security policies and detect/prevent attacks."
        ),
        "subcategories": [
            "Network segmentation and firewalls are deployed.",
            "Intrusion detection/prevention systems are in place.",
            "Endpoint protection is installed on critical systems.",
            "Security technologies are tuned and maintained.",
        ],
        "references": [
            "NIST SP 800-53 Rev. 4 SC, SI families",
            "ISA 62443-3-3 SR 3, SR 5",
        ],
    },
    12: {
        "pillar": "Detect",
        "title": "DETECT ANOMALIES & EVENTS",
        "description": (
            "Detection of anomalies and events identifies deviations from normal operations that may indicate "
            "security incidents or emerging threats."
        ),
        "subcategories": [
            "Baseline of normal operations is defined.",
            "Anomaly detection rules and thresholds are configured.",
            "Events are correlated across systems.",
            "Alerts are generated for suspicious activity.",
        ],
        "references": [
            "NIST SP 800-53 Rev. 4 SI-4",
            "ISO/IEC 27001:2013 A.12.4",
        ],
    },
    13: {
        "pillar": "Detect",
        "title": "DETECTION BY CONTINUOUS SECURITY MONITORING",
        "description": (
            "Continuous monitoring provides ongoing visibility into security posture, enabling timely detection "
            "of attacks and misconfigurations."
        ),
        "subcategories": [
            "Security information and event management (SIEM) is implemented.",
            "Logs from critical systems are collected and analyzed.",
            "Monitoring covers network, endpoints, and ICS.",
            "Monitoring results feed into risk management.",
        ],
        "references": [
            "NIST SP 800-137 (Information Security Continuous Monitoring)",
            "NIST SP 800-53 Rev. 4 CA-7",
        ],
    },
    14: {
        "pillar": "Detect",
        "title": "DETECTION PROCESSES",
        "description": (
            "Detection processes define how potential incidents are triaged, validated, and escalated, ensuring "
            "consistent and effective response."
        ),
        "subcategories": [
            "Documented procedures exist for handling alerts.",
            "Roles and responsibilities for detection are defined.",
            "Detection processes are tested and refined.",
            "Integration with incident response is established.",
        ],
        "references": [
            "NIST SP 800-61 (Computer Security Incident Handling Guide)",
            "ISO/IEC 27035 (Incident Management)",
        ],
    },
    15: {
        "pillar": "Respond",
        "title": "RESPONSE PLANNING",
        "description": (
            "Response planning ensures the organization has documented, tested plans to address cybersecurity "
            "incidents affecting critical infrastructure."
        ),
        "subcategories": [
            "Incident response plan is documented and approved.",
            "Plans cover communication, containment, and recovery.",
            "Plans are aligned with business continuity requirements.",
            "Plans are reviewed and updated regularly.",
        ],
        "references": [
            "NIST SP 800-61",
            "ISO/IEC 27001:2013 A.16",
        ],
    },
    16: {
        "pillar": "Respond",
        "title": "RESPONSE ANALYSIS",
        "description": (
            "Response analysis evaluates incidents, their root causes, and effectiveness of response actions to "
            "improve future resilience."
        ),
        "subcategories": [
            "Post-incident reviews are conducted.",
            "Root cause analysis is performed.",
            "Lessons learned are documented.",
            "Improvements are fed back into controls and plans.",
        ],
        "references": [
            "NIST SP 800-61 (Post-incident activity)",
            "COBIT 5 MEA (Monitor, Evaluate, Assess)",
        ],
    },
    17: {
        "pillar": "Respond",
        "title": "RESPOND BY MITIGATION ACTIVITIES",
        "description": (
            "Mitigation activities focus on containing, eradicating, and reducing the impact of incidents on "
            "critical infrastructure operations."
        ),
        "subcategories": [
            "Containment strategies are defined and executed.",
            "Eradication of malicious artifacts is performed.",
            "Temporary workarounds are implemented where needed.",
            "Risk of recurrence is reduced through corrective actions.",
        ],
        "references": [
            "NIST SP 800-61 (Containment, Eradication, Recovery)",
        ],
    },
    18: {
        "pillar": "Respond",
        "title": "IMPROVING RESPONSE ACTIVITIES",
        "description": (
            "Improving response activities ensures continuous enhancement of incident handling capabilities, "
            "tools, and coordination."
        ),
        "subcategories": [
            "Response metrics are defined and tracked.",
            "Training and exercises are conducted.",
            "Coordination with external partners is improved.",
            "Response tools and playbooks are updated.",
        ],
        "references": [
            "NIST SP 800-84 (Exercises)",
            "ISO/IEC 27001:2013 A.7.2.2, A.16",
        ],
    },
    19: {
        "pillar": "Recover",
        "title": "RECOVERY PLANNING",
        "description": (
            "Recovery planning defines how critical services will be restored after an incident, ensuring "
            "continuity of operations."
        ),
        "subcategories": [
            "Recovery plans for critical services are documented.",
            "Dependencies and priorities are identified.",
            "Recovery objectives (RTO/RPO) are defined.",
            "Recovery plans are tested regularly.",
        ],
        "references": [
            "NIST SP 800-34 (Contingency Planning)",
            "ISO/IEC 27001:2013 A.17",
        ],
    },
    20: {
        "pillar": "Recover",
        "title": "RECOVERY PLANNING IMPROVEMENTS",
        "description": (
            "Recovery planning improvements ensure lessons learned from disruptions are used to strengthen "
            "future recovery capabilities."
        ),
        "subcategories": [
            "Post-recovery reviews are conducted.",
            "Gaps in recovery plans are identified.",
            "Improvements are implemented and documented.",
            "Recovery strategies are aligned with evolving risks.",
        ],
        "references": [
            "COBIT 5 DSS04 (Continuity)",
            "ISO/IEC 27001:2013 A.17.1.2",
        ],
    },
    21: {
        "pillar": "Recover",
        "title": "RESTORATION ACTIVITIES COMMUNICATIONS",
        "description": (
            "Restoration communications coordinate internal and external messaging during and after recovery, "
            "maintaining trust with stakeholders and regulators."
        ),
        "subcategories": [
            "Communication plans for restoration are defined.",
            "Stakeholders are informed of status and impact.",
            "Regulatory and legal reporting requirements are met.",
            "Public and media communications are managed.",
        ],
        "references": [
            "NIST SP 800-61 (Communication)",
            "ISO/IEC 27001:2013 A.16.1.2",
        ],
    },
}

# ---------------------------------------------------------
# Sidebar: Pillar selection + synthetic data controls
# ---------------------------------------------------------
if "record_count" not in st.session_state:
    st.session_state.record_count = 0

st.sidebar.header("Navigation & Synthetic Data")

pillar = st.sidebar.selectbox(
    "Select NIST CSF Pillar",
    options=list(pillars.keys()),
)

record_count = st.sidebar.slider(
    "Number of synthetic records",
    min_value=0,
    max_value=500,
    value=st.session_state.record_count,
    step=10,
)

reset = st.sidebar.button("Reset Data")

if reset:
    st.session_state.record_count = 0
    record_count = 0

st.session_state.record_count = record_count

st.sidebar.markdown(f"**Current synthetic records:** {st.session_state.record_count}")

# Filter items by pillar
items_for_pillar = [i for i, v in framework_items.items() if v["pillar"] == pillar]

item_number = st.sidebar.selectbox(
    "Select framework checklist item",
    options=items_for_pillar,
    format_func=lambda x: f"{x}. {framework_items[x]['title']}",
)

# ---------------------------------------------------------
# Synthetic data generation
# ---------------------------------------------------------
def generate_synthetic_data(n):
    data = []
    for i in range(n):
        item_id = random.choice(list(framework_items.keys()))
        item = framework_items[item_id]
        data.append(
            {
                "record_id": i + 1,
                "pillar": item["pillar"],
                "item_id": item_id,
                "item_title": item["title"],
                "status": random.choice(["Planned", "In Progress", "Implemented", "Needs Review"]),
            }
        )
    return data

synthetic_data = generate_synthetic_data(record_count)

# ---------------------------------------------------------
# Main layout
# ---------------------------------------------------------
col_left, col_right = st.columns([1, 1])

selected_item = framework_items[item_number]
pillar_info = pillars[pillar]

with col_left:
    # Colored pillar header
    st.markdown(
        f"""
        <div style="background-color:{pillar_info['color']};padding:10px;border-radius:5px;margin-bottom:10px;">
            <h3 style="color:white;margin:0;">Pillar: {pillar}</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(f"### {item_number}. {selected_item['title']}")
    st.markdown(f"**What this framework item is:** {selected_item['description']}")

    st.markdown("#### Subcategories")
    for sub in selected_item["subcategories"]:
        st.markdown(f"- {sub}")

    st.markdown("#### Important Reference Documents")
    for ref in selected_item["references"]:
        st.markdown(f"- {ref}")

    st.markdown("#### Pillar Diagrams & Flow Charts")

    tab_mermaid, tab_graphviz = st.tabs(["Mermaid diagram", "Graphviz diagram"])

    with tab_mermaid:
        st.markdown("##### Logical flow (Mermaid)")
        st.markdown(
            f"```mermaid\n{pillar_info['mermaid']}\n```",
            unsafe_allow_html=True,
        )

    with tab_graphviz:
        st.markdown("##### Data/Process flow (Graphviz)")
        st.graphviz_chart(pillar_info["graphviz"])

with col_right:
    st.subheader("Synthetic Data Preview (Framework Implementation Status)")
    if synthetic_data:
        st.dataframe(synthetic_data, use_container_width=True)
    else:
        st.info("No synthetic data generated. Use the slider in the sidebar to create records.")

# ---------------------------------------------------------
# Export functions
# ---------------------------------------------------------
def build_text_report(item_number, item, pillar, synthetic_data):
    lines = []
    lines.append("Critical Infrastructure Security Framework Report")
    lines.append("Developed by Randy Singh, Kalsnet (KNet) Consulting Group")
    lines.append("")
    lines.append(f"Pillar: {pillar}")
    lines.append(f"Selected Checklist Item: {item_number}. {item['title']}")
    lines.append("")
    lines.append("Description:")
    lines.append(item["description"])
    lines.append("")
    lines.append("Subcategories:")
    for sub in item["subcategories"]:
        lines.append(f"- {sub}")
    lines.append("")
    lines.append("Reference Documents:")
    for ref in item["references"]:
        lines.append(f"- {ref}")
    lines.append("")
    lines.append(f"Synthetic Data Records: {len(synthetic_data)}")
    for row in synthetic_data[:50]:  # limit for readability
        lines.append(
            f"Record {row['record_id']}: {row['pillar']} - {row['item_title']} "
            f"(Status: {row['status']})"
        )
    return "\n".join(lines)

def export_pdf(text):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    y = height - 50
    for line in text.split("\n"):
        c.drawString(50, y, line[:100])
        y -= 15
        if y < 50:
            c.showPage()
            y = height - 50
    c.save()
    buffer.seek(0)
    return buffer

def export_word(text):
    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

def export_json(item_number, item, pillar, synthetic_data):
    payload = {
        "application": "Critical Infrastructure Security Framework Analyzer",
        "developer": "Randy Singh, Kalsnet (KNet) Consulting Group",
        "pillar": pillar,
        "item_number": item_number,
        "item_title": item["title"],
        "description": item["description"],
        "subcategories": item["subcategories"],
        "references": item["references"],
        "synthetic_data": synthetic_data,
    }
    buffer = BytesIO()
    buffer.write(json.dumps(payload, indent=2).encode("utf-8"))
    buffer.seek(0)
    return buffer

# ---------------------------------------------------------
# Export buttons
# ---------------------------------------------------------
st.markdown("---")
st.subheader("Export Framework Report")

report_text = build_text_report(item_number, selected_item, pillar, synthetic_data)

pdf_buffer = export_pdf(report_text)
word_buffer = export_word(report_text)
json_buffer = export_json(item_number, selected_item, pillar, synthetic_data)

col1, col2, col3 = st.columns(3)

with col1:
    st.download_button(
        label="📄 Export as PDF",
        data=pdf_buffer,
        file_name="critical_infrastructure_framework_report.pdf",
        mime="application/pdf",
    )

with col2:
    st.download_button(
        label="📝 Export as Word",
        data=word_buffer,
        file_name="critical_infrastructure_framework_report.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )

with col3:
    st.download_button(
        label="🧾 Export as JSON",
        data=json_buffer,
        file_name="critical_infrastructure_framework_report.json",
        mime="application/json",
    )
