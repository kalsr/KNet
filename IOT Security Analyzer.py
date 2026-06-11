#IOT Security Analyzer

import streamlit as st
from io import BytesIO
import json
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random

# -----------------------------
# App Title and Header
# -----------------------------
st.set_page_config(page_title="IoT Security Analyzer", layout="wide")

st.markdown(
    """
    # IoT Security Analyzer Application Platform  
    #### Developed by Randy Singh, Kalsnet (KNet) Consulting Group
    """
)

st.markdown("---")

# -----------------------------
# Vulnerability Data
# -----------------------------
vulnerabilities = {
    1: {
        "title": "INSECURE WEB INTERFACE",
        "recommended": [
            "Determining if the default username and password can be changed during initial product setup.",
            "Determining if a specific user account is locked out after 3–5 failed login attempts.",
            "Determining if valid accounts can be identified using password recovery mechanisms or new user pages.",
            "Reviewing the interface for issues such as cross-site scripting, cross-site request forgery and SQL injection.",
            "VERIFY SECURITY CHECKLIST FROM DISA RISK MANAGEMENT FRAMEWORK (RMF).",
        ],
        "best": [
            "Default passwords and ideally default usernames to be changed during initial setup.",
            "Ensuring password recovery mechanisms are robust and do not supply an attacker with information indicating a valid account.",
            "Ensuring web interface is not susceptible to XSS, SQLi or CSRF.",
            "Ensuring credentials are not exposed in internal or external network traffic.",
            "Ensuring weak passwords are not allowed.",
            "Ensuring account lockout after 3–5 failed login attempts.",
        ],
    },
    2: {
        "title": "INSUFFICIENT AUTHENTICATION/AUTHORIZATION",
        "recommended": [
            "Attempting to use simple passwords such as 1234 to determine if the password policy is sufficient.",
            "Reviewing network traffic to determine if credentials are being transmitted in clear text.",
            "Reviewing requirements around password controls such as complexity, history, expiration and forced reset.",
            "Reviewing whether re-authentication is required for sensitive features.",
            "Reviewing interfaces to determine whether separation of roles is enforced.",
            "Reviewing access controls and testing for privilege escalation.",
            "VERIFY SECURITY CHECKLIST FROM DISA RISK MANAGEMENT FRAMEWORK (RMF).",
        ],
        "best": [
            "Ensuring that strong passwords are required.",
            "Ensuring granular access control is in place when necessary.",
            "Ensuring credentials are properly protected.",
            "Implementing two-factor authentication where possible.",
            "Ensuring that password recovery mechanisms are secure.",
            "Ensuring re-authentication is required for sensitive features.",
            "Ensuring options are available for configuring password controls.",
            "Ensuring credentials can be revoked.",
            "App, device and server authentication are required.",
            "Managing authenticated user ID, device ID and app ID mapping in the authentication server.",
            "Ensuring authentication token/session key issued to client is always different.",
            "Ensuring user ID, app ID and device ID are universally unique.",
        ],
    },
    3: {
        "title": "INSECURE NETWORK SERVICES",
        "recommended": [
            "Determining if insecure network services exist by reviewing your device for open ports using a port scanner.",
            "Reviewing network ports to ensure they are necessary and if any are exposed to the internet via UPnP.",
            "Testing open ports using automated tools for DoS, UDP service vulnerabilities and buffer overflow/fuzzing attacks.",
            "VERIFY SECURITY CHECKLIST FROM DISA RISK MANAGEMENT FRAMEWORK (RMF).",
        ],
        "best": [
            "Ensuring only necessary ports are exposed and available.",
            "Ensuring services are not vulnerable to buffer overflow and fuzzing attacks.",
            "Ensuring services are not vulnerable to DoS attacks affecting the device or other devices/users.",
            "Ensuring network ports or services are not exposed to the internet via UPnP.",
            "Detecting and blocking abnormal service request traffic at the service gateway layer.",
        ],
    },
    4: {
        "title": "LACK OF TRANSPORT ENCRYPTION/INTEGRITY VERIFICATION",
        "recommended": [
            "Reviewing network traffic of the device, mobile application and cloud connections for clear-text information.",
            "Reviewing the use of SSL/TLS to ensure it is up to date and properly implemented.",
            "Reviewing encryption protocols to ensure they are recommended and accepted.",
            "VERIFY SECURITY CHECKLIST FROM DISA RISK MANAGEMENT FRAMEWORK (RMF).",
        ],
        "best": [
            "Ensuring data is encrypted using protocols such as SSL and TLS while transiting networks.",
            "Using other industry standard encryption techniques if SSL/TLS are not available.",
            "Using only accepted encryption standards and avoiding proprietary encryption protocols.",
            "Ensuring message payload encryption.",
            "Ensuring secure encryption key handshaking.",
            "Ensuring received data integrity verification.",
        ],
    },
    5: {"title": "PRIVACY CONCERNS", "recommended": [], "best": []},
    6: {"title": "INSECURE CLOUD INTERFACE", "recommended": [], "best": []},
    7: {"title": "INSECURE MOBILE INTERFACE", "recommended": [], "best": []},
    8: {"title": "INSUFFICIENT SECURITY CONFIGURABILITY", "recommended": [], "best": []},
    9: {"title": "INSECURE SOFTWARE/FIRMWARE", "recommended": [], "best": []},
    10: {"title": "POOR PHYSICAL SECURITY", "recommended": [], "best": []},
}

# -----------------------------
# Sidebar: Synthetic Data Controls
# -----------------------------
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

st.sidebar.markdown(
    f"**Current synthetic records:** {st.session_state.record_count}"
)

# Generate synthetic data
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

# -----------------------------
# Main Layout
# -----------------------------
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

    st.markdown("#### Recommended Security Steps")
    if vuln["recommended"]:
        for step in vuln["recommended"]:
            st.markdown(f"- {step}")
    else:
        st.info("Recommended steps not yet defined for this vulnerability.")

    st.markdown("#### Best Practices")
    if vuln["best"]:
        for bp in vuln["best"]:
            st.markdown(f"- {bp}")
    else:
        st.info("Best practices not yet defined for this vulnerability.")

with col_right:
    st.subheader("Synthetic Data Preview")
    if synthetic_data:
        st.dataframe(synthetic_data, use_container_width=True)
    else:
        st.info("No synthetic data generated. Use the slider in the sidebar to create records.")

# -----------------------------
# Export Functions
# -----------------------------
def build_text_report(vuln_number, vuln, synthetic_data):
    lines = []
    lines.append(f"IoT Security Analyzer Report")
    lines.append(f"Developed by Randy Singh, Kalsnet (KNet) Consulting Group")
    lines.append("")
    lines.append(f"Selected Vulnerability: {vuln_number}. {vuln['title']}")
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
        c.drawString(50, y, line[:100])  # simple wrapping
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
        "recommended_steps": vuln["recommended"],
        "best_practices": vuln["best"],
        "synthetic_data": synthetic_data,
    }
    buffer = BytesIO()
    buffer.write(json.dumps(payload, indent=2).encode("utf-8"))
    buffer.seek(0)
    return buffer


# -----------------------------
# Export Buttons
# -----------------------------
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
