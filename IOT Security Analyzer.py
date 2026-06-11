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
st.set_page_config(page_title="IoT Security Analyzer", layout="wide")

# ---------------------------------------------------------
# Bold blue title bar + app description
# ---------------------------------------------------------
st.markdown(
    """
    <div style="background-color:#004aad;padding:15px;border-radius:5px;">
        <h1 style="color:white;text-align:center;margin-bottom:5px;">
            IoT Security Analyzer Application Platform
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
    This application helps security analysts, system and network administrators understand and mitigate 
    the **Top 10 IoT security vulnerabilities** identified by OWASP and related guidance.  
    For each vulnerability, it provides a short explanation, recommended security steps, best practices, 
    and visual diagrams showing how risks propagate across IoT ecosystems.  
    Synthetic data and export features make it useful for training, documentation, and real‑world security reviews.
    """
)

st.markdown("---")

# ---------------------------------------------------------
# Vulnerability definitions (description, steps, best practices, diagrams)
# ---------------------------------------------------------
vulnerabilities = {
    1: {
        "title": "INSECURE WEB INTERFACE",
        "description": (
            "Insecure web interfaces expose IoT devices to attacks via poorly protected login pages, "
            "weak input validation, and misconfigured sessions. Attackers can exploit these flaws to "
            "steal credentials, change device settings, or pivot deeper into the network."
        ),
        "recommended": [
            "Determine if default usernames and passwords can be changed during initial product setup.",
            "Verify account lockout after 3–5 failed login attempts.",
            "Check if password recovery or registration pages reveal valid account information.",
            "Review the interface for XSS, CSRF, and SQL injection vulnerabilities.",
            "Verify security checklist from DISA Risk Management Framework (RMF).",
        ],
        "best": [
            "Force change of default usernames and passwords during initial setup.",
            "Use robust password recovery mechanisms that do not disclose account existence.",
            "Harden the web interface against XSS, SQLi, and CSRF using secure coding practices.",
            "Ensure credentials are never exposed in internal or external network traffic.",
            "Enforce strong password policies and account lockout after repeated failures.",
        ],
        "mermaid": """
flowchart TD
    User[User Browser] --> UI[IoT Web Interface]
    UI --> Auth[Authentication Module]
    UI --> Config[Device Configuration]
    Attacker[Malicious Actor] --> UI
    UI --> Net[Internal Network]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Web Interface";
    "Web Interface" -> "Auth Service";
    "Web Interface" -> "Device Config";
    Attacker -> "Web Interface";
    "Web Interface" -> "Internal Network";
}
""",
    },
    2: {
        "title": "INSUFFICIENT AUTHENTICATION/AUTHORIZATION",
        "description": (
            "Weak or missing authentication and authorization controls allow unauthorized users or devices "
            "to access sensitive functions. Poor role separation and credential handling can lead to "
            "privilege escalation and full compromise of IoT systems."
        ),
        "recommended": [
            "Test password strength by attempting simple passwords such as '1234' across all interfaces.",
            "Review network traffic to ensure credentials are not transmitted in clear text.",
            "Review password controls: complexity, history, expiration, and forced reset for new users.",
            "Verify re‑authentication for sensitive features and administrative actions.",
            "Review role‑based access control and test for privilege escalation.",
            "Verify security checklist from DISA Risk Management Framework (RMF).",
        ],
        "best": [
            "Require strong, complex passwords and enforce password policies.",
            "Implement granular role‑based access control with least‑privilege principles.",
            "Protect credentials in transit and at rest using strong encryption.",
            "Implement multi‑factor authentication where possible.",
            "Secure password recovery mechanisms and session management.",
            "Ensure credentials can be revoked and rotated quickly.",
            "Require app, device, and server authentication with unique IDs.",
            "Issue unique, non‑reusable authentication tokens or session keys.",
        ],
        "mermaid": """
flowchart TD
    User[User] --> Login[Login Service]
    Login --> AuthZ[Authorization Engine]
    AuthZ --> DeviceOps[Device Operations]
    Attacker[Malicious Actor] --> Login
    Login --> WeakPolicy[Weak Password Policy]
    WeakPolicy --> Breach[Account Compromise]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Login Service";
    "Login Service" -> "AuthZ Engine";
    "AuthZ Engine" -> "Device Operations";
    Attacker -> "Login Service";
    "Login Service" -> "Weak Policy";
    "Weak Policy" -> "Account Compromise";
}
""",
    },
    3: {
        "title": "INSECURE NETWORK SERVICES",
        "description": (
            "IoT devices often expose unnecessary or poorly secured network services. Open ports, "
            "legacy protocols, and unpatched services can be exploited for denial‑of‑service, remote code "
            "execution, or lateral movement across the network."
        ),
        "recommended": [
            "Use port scanners to identify open ports and exposed services on IoT devices.",
            "Review which ports are necessary and whether any are exposed to the internet via UPnP.",
            "Test services for DoS, buffer overflow, and fuzzing vulnerabilities using automated tools.",
            "Verify security checklist from DISA Risk Management Framework (RMF).",
        ],
        "best": [
            "Expose only strictly necessary ports and services.",
            "Harden services against buffer overflow and fuzzing attacks.",
            "Implement protections against DoS attacks that affect devices or networks.",
            "Disable UPnP or similar mechanisms that expose services to the internet.",
            "Detect and block abnormal service request traffic at gateway layers.",
        ],
        "mermaid": """
flowchart TD
    Device[IoT Device] --> Ports[Open Ports]
    Ports --> LAN[Local Network]
    Ports --> Internet[Internet Exposure via UPnP]
    Attacker[Malicious Actor] --> Internet
    Attacker --> Ports
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    "IoT Device" -> "Open Ports";
    "Open Ports" -> "Local Network";
    "Open Ports" -> "Internet (UPnP)";
    Attacker -> "Internet (UPnP)";
    Attacker -> "Open Ports";
}
""",
    },
    4: {
        "title": "LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION",
        "description": (
            "When data between devices, mobile apps, and cloud services is sent without strong encryption "
            "or integrity checks, attackers can intercept, read, or modify messages. This undermines "
            "confidentiality and trust in IoT communications."
        ),
        "recommended": [
            "Review network traffic for clear‑text data between device, mobile app, and cloud.",
            "Verify use of up‑to‑date SSL/TLS and correct certificate validation.",
            "Review all encryption protocols to ensure they follow accepted standards.",
            "Verify security checklist from DISA Risk Management Framework (RMF).",
        ],
        "best": [
            "Encrypt all data in transit using strong protocols such as TLS 1.2+.",
            "Avoid proprietary or weak encryption schemes; use industry‑standard algorithms.",
            "Encrypt message payloads end‑to‑end where possible.",
            "Use secure key exchange and key management practices.",
            "Implement integrity verification (MACs, signatures) for received data.",
        ],
        "mermaid": """
flowchart TD
    Device[IoT Device] -->|Unencrypted| Cloud[Cloud Service]
    Mobile[Mobile App] -->|Unencrypted| Cloud
    Attacker[Network Sniffer] --> Cloud
    Attacker --> Device
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    "IoT Device" -> "Cloud Service" [label="Unencrypted"];
    "Mobile App" -> "Cloud Service" [label="Unencrypted"];
    Attacker -> "Cloud Service";
    Attacker -> "IoT Device";
}
""",
    },
    5: {
        "title": "PRIVACY CONCERNS",
        "description": (
            "IoT devices collect extensive personal, behavioral, and environmental data. Poor data minimization, "
            "unclear consent, and weak protection can lead to privacy violations, surveillance, and regulatory risk."
        ),
        "recommended": [
            "Identify all categories of personal and sensitive data collected by the device and services.",
            "Review data retention policies and where data is stored (device, gateway, cloud).",
            "Check whether users are informed and consent to data collection and sharing.",
            "Assess third‑party integrations and data sharing agreements.",
        ],
        "best": [
            "Apply data minimization: collect only what is necessary for functionality.",
            "Implement clear, transparent privacy notices and consent mechanisms.",
            "Encrypt and pseudonymize stored personal data where possible.",
            "Provide user controls for data access, deletion, and sharing preferences.",
            "Regularly review privacy impact and compliance with relevant regulations.",
        ],
        "mermaid": """
flowchart TD
    User[User] --> Device[IoT Device]
    Device --> DataStore[Data Storage]
    DataStore --> Cloud[Cloud Analytics]
    Cloud --> ThirdParty[Third-Party Services]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "IoT Device";
    "IoT Device" -> "Data Storage";
    "Data Storage" -> "Cloud Analytics";
    "Cloud Analytics" -> "Third-Party Services";
}
""",
    },
    6: {
        "title": "INSECURE CLOUD INTERFACE",
        "description": (
            "Cloud dashboards and APIs used to manage IoT fleets can become a single point of failure. "
            "Weak authentication, misconfigured APIs, or exposed keys can allow attackers to control many devices at once."
        ),
        "recommended": [
            "Review cloud console and API authentication mechanisms (MFA, API keys, OAuth).",
            "Check for overly permissive API keys or tokens and hard‑coded credentials.",
            "Assess access control for tenants, projects, and device groups.",
            "Review logging and monitoring for suspicious cloud activity.",
        ],
        "best": [
            "Enforce strong authentication (MFA) for cloud dashboards.",
            "Use scoped, least‑privilege API keys and rotate them regularly.",
            "Implement fine‑grained access control for device management operations.",
            "Enable comprehensive logging, alerting, and anomaly detection.",
            "Secure CI/CD pipelines that deploy cloud‑side IoT services.",
        ],
        "mermaid": """
flowchart TD
    Admin[Admin User] --> Portal[Cloud Management Portal]
    Portal --> Devices[IoT Device Fleet]
    Attacker[Malicious Actor] --> Portal
    Portal --> API[Cloud APIs]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    Admin -> "Cloud Portal";
    "Cloud Portal" -> "IoT Device Fleet";
    Attacker -> "Cloud Portal";
    "Cloud Portal" -> "Cloud APIs";
}
""",
    },
    7: {
        "title": "INSECURE MOBILE INTERFACE",
        "description": (
            "Mobile apps used to control IoT devices can leak credentials, expose APIs, or store sensitive data "
            "insecurely. Reverse‑engineering and tampering can reveal secrets or bypass security controls."
        ),
        "recommended": [
            "Review mobile app storage for hard‑coded keys, tokens, or credentials.",
            "Analyze API calls from the app to identify insecure endpoints or clear‑text traffic.",
            "Check for rooted/jailbroken device protections and app integrity checks.",
            "Assess permissions requested by the app versus actual needs.",
        ],
        "best": [
            "Avoid storing secrets in the app; use secure token services.",
            "Use certificate pinning and TLS for all API calls.",
            "Implement app integrity checks and tamper detection.",
            "Limit app permissions to the minimum required.",
            "Regularly perform mobile application security testing.",
        ],
        "mermaid": """
flowchart TD
    User[User] --> MobileApp[Mobile App]
    MobileApp --> Device[IoT Device]
    MobileApp --> Cloud[Cloud API]
    Attacker[Reverse Engineer] --> MobileApp
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Mobile App";
    "Mobile App" -> "IoT Device";
    "Mobile App" -> "Cloud API";
    Attacker -> "Mobile App";
}
""",
    },
    8: {
        "title": "INSUFFICIENT SECURITY CONFIGURABILITY",
        "description": (
            "Some IoT products ship with fixed, non‑configurable security settings. Administrators cannot adjust "
            "password policies, encryption options, or logging, leaving deployments unable to meet organizational requirements."
        ),
        "recommended": [
            "Review available security settings (password policies, encryption, logging, access control).",
            "Check whether defaults can be changed and whether advanced options exist.",
            "Assess ability to disable insecure features and protocols.",
            "Evaluate configuration management across large fleets of devices.",
        ],
        "best": [
            "Provide configurable security policies aligned with enterprise standards.",
            "Allow administrators to enable/disable protocols and features.",
            "Offer centralized configuration management and templating.",
            "Document recommended secure configurations and baselines.",
            "Support secure remote updates to configuration settings.",
        ],
        "mermaid": """
flowchart TD
    Admin[Admin] --> ConfigUI[Security Config UI]
    ConfigUI --> Device[IoT Device]
    Device --> Logs[Security Logs]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    Admin -> "Security Config UI";
    "Security Config UI" -> "IoT Device";
    "IoT Device" -> "Security Logs";
}
""",
    },
    9: {
        "title": "INSECURE SOFTWARE/FIRMWARE",
        "description": (
            "Unpatched firmware, insecure update mechanisms, and lack of code signing allow attackers to install "
            "malicious firmware or exploit known vulnerabilities, turning IoT devices into persistent footholds."
        ),
        "recommended": [
            "Inventory firmware versions and compare against known vulnerabilities.",
            "Review update mechanisms for encryption, integrity, and authenticity checks.",
            "Check whether rollback protections and secure boot are implemented.",
            "Assess how quickly security patches can be deployed across fleets.",
        ],
        "best": [
            "Use signed firmware with verified integrity and authenticity.",
            "Implement secure boot to prevent unauthorized firmware from running.",
            "Provide encrypted, authenticated update channels.",
            "Maintain a regular patching and vulnerability management process.",
            "Support remote, controlled firmware updates with rollback safety.",
        ],
        "mermaid": """
flowchart TD
    DevTeam[Development Team] --> Firmware[Signed Firmware]
    Firmware --> Device[IoT Device]
    Attacker[Malicious Firmware] --> Device
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    "Development Team" -> "Signed Firmware";
    "Signed Firmware" -> "IoT Device";
    Attacker -> "IoT Device" [label="Malicious Firmware"];
}
""",
    },
    10: {
        "title": "POOR PHYSICAL SECURITY",
        "description": (
            "IoT devices deployed in public or uncontrolled environments can be physically accessed, opened, or "
            "tampered with. Attackers may extract keys, modify hardware, or connect debug interfaces to bypass protections."
        ),
        "recommended": [
            "Identify deployment locations and assess physical access risks.",
            "Review tamper‑evident and tamper‑resistant features on devices.",
            "Check for exposed debug ports (JTAG, UART) and unsecured storage.",
            "Evaluate procedures for device loss, theft, and decommissioning.",
        ],
        "best": [
            "Use tamper‑resistant enclosures and tamper‑evident seals.",
            "Disable or secure debug interfaces in production devices.",
            "Encrypt sensitive data and keys stored on the device.",
            "Implement procedures for secure disposal and replacement.",
            "Combine physical security with monitoring and alerting.",
        ],
        "mermaid": """
flowchart TD
    Device[IoT Device] --> Field[Field Deployment]
    Attacker[Physical Attacker] --> Field
    Field --> Tamper[Tamper / Opening]
    Tamper --> Keys[Key Extraction]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    "IoT Device" -> "Field Deployment";
    Attacker -> "Field Deployment";
    "Field Deployment" -> "Tamper Event";
    "Tamper Event" -> "Key Extraction";
}
""",
    },
}

# ---------------------------------------------------------
# Sidebar: Synthetic data controls
# ---------------------------------------------------------
if "record_count" not in st.session_state:
    st.session_state.record_count = 0

st.sidebar.header("Synthetic Data Controls")

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

def generate_synthetic_data(n):
    data = []
    vuln_keys = list(vulnerabilities.keys())
    for i in range(n):
        v_id = random.choice(vuln_keys)
        data.append(
            {
                "record_id": i + 1,
                "vulnerability_id": v_id,
                "vulnerability_name": vulnerabilities[v_id]["title"],
                "severity": random.choice(["Low", "Medium", "High", "Critical"]),
            }
        )
    return data

synthetic_data = generate_synthetic_data(record_count)

# ---------------------------------------------------------
# Main layout
# ---------------------------------------------------------
col_left, col_right = st.columns([1, 1])

with col_left:
    st.subheader("Select IoT Vulnerability")

    vuln_number = st.selectbox(
        "Choose vulnerability number",
        options=list(vulnerabilities.keys()),
        format_func=lambda x: f"{x}. {vulnerabilities[x]['title']}",
    )

    vuln = vulnerabilities[vuln_number]

    st.markdown(f"### {vuln_number}. {vuln['title']}")
    st.markdown(f"**What this vulnerability is:** {vuln['description']}")

    st.markdown("#### Recommended Security Steps")
    for step in vuln["recommended"]:
        st.markdown(f"- {step}")

    st.markdown("#### Best Practices")
    for bp in vuln["best"]:
        st.markdown(f"- {bp}")

    st.markdown("#### Diagrams & Flow Charts")

    tab_mermaid, tab_graphviz = st.tabs(["Mermaid diagram", "Graphviz diagram"])

    with tab_mermaid:
        st.markdown("##### Logical flow (Mermaid)")
        st.markdown(
            f"```mermaid\n{vuln['mermaid']}\n```",
            unsafe_allow_html=True,
        )

    with tab_graphviz:
        st.markdown("##### Data/attack flow (Graphviz)")
        st.graphviz_chart(vuln["graphviz"])

with col_right:
    st.subheader("Synthetic Data Preview")
    if synthetic_data:
        st.dataframe(synthetic_data, use_container_width=True)
    else:
        st.info("No synthetic data generated. Use the slider in the sidebar to create records.")

# ---------------------------------------------------------
# Export functions
# ---------------------------------------------------------
def build_text_report(vuln_number, vuln, synthetic_data):
    lines = []
    lines.append("IoT Security Analyzer Report")
    lines.append("Developed by Randy Singh, Kalsnet (KNet) Consulting Group")
    lines.append("")
    lines.append(f"Selected Vulnerability: {vuln_number}. {vuln['title']}")
    lines.append("")
    lines.append("Description:")
    lines.append(vuln["description"])
    lines.append("")
    lines.append("Recommended Security Steps:")
    for step in vuln["recommended"]:
        lines.append(f"- {step}")
    lines.append("")
    lines.append("Best Practices:")
    for bp in vuln["best"]:
        lines.append(f"- {bp}")
    lines.append("")
    lines.append(f"Synthetic Data Records: {len(synthetic_data)}")
    for row in synthetic_data[:50]:  # limit for readability
        lines.append(
            f"Record {row['record_id']}: {row['vulnerability_name']} "
            f"(Severity: {row['severity']})"
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

def export_json(vuln_number, vuln, synthetic_data):
    payload = {
        "application": "IoT Security Analyzer",
        "developer": "Randy Singh, Kalsnet (KNet) Consulting Group",
        "vulnerability_number": vuln_number,
        "vulnerability_title": vuln["title"],
        "description": vuln["description"],
        "recommended_steps": vuln["recommended"],
        "best_practices": vuln["best"],
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
st.subheader("Export Report")

report_text = build_text_report(vuln_number, vuln, synthetic_data)

pdf_buffer = export_pdf(report_text)
word_buffer = export_word(report_text)
json_buffer = export_json(vuln_number, vuln, synthetic_data)

col1, col2, col3 = st.columns(3)

with col1:
    st.download_button(
        label="📄 Export as PDF",
        data=pdf_buffer,
        file_name="iot_security_analyzer_report.pdf",
        mime="application/pdf",
    )

with col2:
    st.download_button(
        label="📝 Export as Word",
        data=word_buffer,
        file_name="iot_security_analyzer_report.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )

with col3:
    st.download_button(
        label="🧾 Export as JSON",
        data=json_buffer,
        file_name="iot_security_analyzer_report.json",
        mime="application/json",
    )
