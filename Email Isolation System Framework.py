import streamlit as st
from io import BytesIO
import json
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from datetime import datetime
import random

# ---------------------------------------------------------
# Page config
# ---------------------------------------------------------
st.set_page_config(page_title="Email Isolation Framework Application", layout="wide")

# ---------------------------------------------------------
# Cloud-safe workspace
# ---------------------------------------------------------
WORKSPACE = "workspace"
FILES_DIR = os.path.join(WORKSPACE, "files")
UPLOADS_DIR = os.path.join(WORKSPACE, "uploads")

os.makedirs(FILES_DIR, exist_ok=True)
os.makedirs(UPLOADS_DIR, exist_ok=True)

# ---------------------------------------------------------
# Title bar + explanation
# ---------------------------------------------------------
st.markdown(
    """
    <div style="background-color:#004aad;padding:15px;border-radius:5px;">
        <h1 style="color:white;text-align:center;margin-bottom:5px;">
            EMAIL-ISOLATION FRAMEWORK APPLICATION
        </h1>
        <h4 style="color:white;text-align:center;margin-top:0;">
            Developed by Randy Singh, Computer Scientist From Kalsnet(KNet) Consulting Group.
        </h4>
        <h5 style="color:white;text-align:center;margin-top:0;">
            This Streamlit application is a modern, cloud‑safe version of the original Java EmailIsolationMenu framework.
        </h5>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    This Streamlit application is a modern, cloud‑safe version of the original Java **EmailIsolationMenu** framework.  
    It presents the 17 main categories of the Email Isolation Framework, with detailed content, real‑world examples,  
    and diagrams for each category.
    """
)

st.markdown("---")

# ---------------------------------------------------------
# Main menu definitions (1–17)
# ---------------------------------------------------------
MAIN_MENU = {
    1: "EMAIL ISOLATION ELEMENTS",
    2: "EMAIL STANDARDS",
    3: "EMAIL SECURITY THREATS",
    4: "EMAIL ISOLATION USE-CASES",
    5: "EMAIL-MALWARE INCIDENTS PREVENTION",
    6: "EMAIL-MALWARE INCIDENTS RESPONSE",
    7: "SIGNING & ENCRYPTING EMAIL MESSAGES",
    8: "PLANNING & MANAGING EMAIL SERVERS",
    9: "SECURING THE EMAIL SERVERS OPERATING SYSTEMS",
    10: "SECURING EMAIL SERVER CONTENTS",
    11: "IMPLEMENTING SECURE NETWORK INFRASTRUCTURE",
    12: "SECURING EMAIL CLIENTS",
    13: "ADMINISTERING THE EMAIL SERVERS",
    14: "AUTHENTICATING A SENDING DOMAIN & EMAIL MESSAGES",
    15: "PROTECTING EMAIL CONFIDENTIALITY",
    16: "REDUCING UNSOLICITED BULK EMAIL",
    17: "END USER EMAIL SECURITY RECOMMENDATIONS",
}

# ---------------------------------------------------------
# Email Elements subcategories
# ---------------------------------------------------------
EMAIL_ELEMENTS_SUBMENU = {
    1: "EMAIL COMPONENTS",
    2: "RELATED COMPONENTS",
    3: "EMAIL PROTOCOLS",
    4: "EMAIL FORMATS",
    5: "SECURE WEB-MAIL SOLUTIONS",
}

EMAIL_COMPONENTS_TEXT = """
Email components form the building blocks of any email system.

Mail User Agents (MUAs):
A MUA is a software component (or web interface) that allows an end user to compose and send messages to one or more recipients.
Real-world example: Outlook, Thunderbird, Apple Mail, Gmail web UI.

Mail Transfer Agents (MTAs):
Email is transmitted, in a store and forward fashion, across networks via MTAs.
Real-world example: Postfix, Exim, Microsoft Exchange transport service.

Mail Submission Agents (MSA) and Mail Delivery Agents (MDA):
MSA accepts mail from MUAs; MDA delivers mail into mailboxes.
Real-world example: Dovecot acting as MDA for IMAP mailboxes.

Special Use Components:
Malware filters, archiving systems, and DLP gateways sit alongside MTAs.
Real-world example: Secure email gateways like Proofpoint or Microsoft Defender for Office 365.

Cloud and Hosted Service Customers:
In Email as a Service (EaaS), the provider runs MTAs and MDAs; customers configure MUAs and policies.
Real-world example: Microsoft 365, Google Workspace.
"""

EMAIL_RELATED_COMPONENTS_TEXT = """
Related components support email but are not themselves email servers.

Domain Name System (DNS):
DNS maps domain names to IP addresses and MX records to mail servers.
Real-world example: A domain 'example.com' with MX records pointing to 'mail.example.com'.

DNS and Email Security:
SPF, DKIM, and DMARC records are published in DNS.
Real-world example: A DMARC policy 'v=DMARC1; p=reject;' for a high-security domain.

Enterprise Perimeter Security Components:
Firewalls, IDS/IPS, and web proxies influence email flows.
Real-world example: A firewall only allowing SMTP over TLS from specific IP ranges.

Public Key Infrastructure (PKIX):
Certificates for TLS and S/MIME are issued and managed via PKI.
Real-world example: An internal CA issuing certificates for mail.example.com used in TLS.
"""

EMAIL_PROTOCOLS_TEXT = """
Protocols define how email is transported and accessed.

Simple Mail Transfer Protocol (SMTP):
SMTP moves messages between servers and from MUAs to MTAs.
Real-world example: An MTA listening on port 587 for authenticated submission and 25 for server-to-server relay.

Mail Access Protocols (POP3, IMAP, MAPI/RPC):
POP3 downloads mail; IMAP synchronizes mail across devices; MAPI/RPC is used by Outlook with Exchange.
Real-world example: A user reading mail on a phone via IMAP and on a laptop via Outlook (MAPI).

Internet Email Addresses:
SMTP uses an envelope MAIL FROM; headers use a FROM field.
Real-world example: MAIL FROM: bounce@example.com, header From: "Support" <support@example.com>.
"""

EMAIL_FORMATS_TEXT = """
Email formats describe how messages are structured.

MIME:
MIME allows multipart messages with text, HTML, and attachments.
Real-world example: An email with both plain text and HTML versions plus a PDF attachment.

S/MIME:
S/MIME adds signatures and encryption using X.509 certificates.
Real-world example: A signed email from finance@example.com where the recipient can verify authenticity.

OpenPGP:
OpenPGP provides encryption and signatures using PGP-compatible keys.
Real-world example: A developer mailing patches to a security mailing list using PGP-encrypted email.
"""

SECURE_WEBMAIL_TEXT = """
Secure web-mail solutions provide browser-based access to email while enforcing strong controls.

Key Features:
- Strong authentication (MFA, conditional access)
- TLS encryption for all sessions
- Content filtering and script isolation
- Remote rendering of risky content

Real-world example:
A bank provides web-mail to employees via a hardened portal that opens attachments in a remote sandbox.
Users see the content, but malicious macros never run on their local devices.
"""

# ---------------------------------------------------------
# Synthetic data (for export/report)
# ---------------------------------------------------------
def generate_synthetic_data(n):
    categories = list(MAIN_MENU.values())
    data = []
    for i in range(n):
        cat = random.choice(categories)
        score = random.randint(1, 5)
        data.append(
            {
                "record_id": i + 1,
                "category": cat,
                "risk_level": random.choice(["Low", "Medium", "High", "Critical"]),
                "maturity_score": score,
                "status": random.choice(["Planned", "In Progress", "Implemented", "Under Review"]),
            }
        )
    return data

if "record_count" not in st.session_state:
    st.session_state.record_count = 50

st.sidebar.header("Framework Controls & Synthetic Data")

selected_main_id = st.sidebar.selectbox(
    "Select Email Isolation Framework Category (1–17)",
    options=list(MAIN_MENU.keys()),
    format_func=lambda k: f"{k}. {MAIN_MENU[k]}",
)

record_count = st.sidebar.slider(
    "Number of synthetic framework records",
    min_value=0,
    max_value=500,
    value=st.session_state.record_count,
    step=10,
)
st.session_state.record_count = record_count

synthetic_data = generate_synthetic_data(record_count)

# ---------------------------------------------------------
# Workspace browser (simple view)
# ---------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.subheader("Workspace Directory Browser")

files_in_files = sorted(os.listdir(FILES_DIR))
files_in_uploads = sorted(os.listdir(UPLOADS_DIR))

st.sidebar.write(f"Files in workspace/files ({len(files_in_files)}):")
for f in files_in_files[:10]:
    st.sidebar.write(f"- {f}")

st.sidebar.write(f"Files in workspace/uploads ({len(files_in_uploads)}):")
for f in files_in_uploads[:10]:
    st.sidebar.write(f"- {f}")

st.sidebar.markdown("---")
st.sidebar.subheader("Upload Reference Document (optional)")

uploaded_file_sidebar = st.sidebar.file_uploader("Upload a file (stored in workspace/uploads)")
if uploaded_file_sidebar:
    upload_path = os.path.join(UPLOADS_DIR, uploaded_file_sidebar.name)
    with open(upload_path, "wb") as f:
        f.write(uploaded_file_sidebar.read())
    st.sidebar.success(f"Uploaded to {upload_path}")

# ---------------------------------------------------------
# Layout
# ---------------------------------------------------------
col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown(
        f"""
        <div style="background-color:#008080;padding:10px;border-radius:5px;margin-bottom:10px;">
            <h3 style="color:white;margin:0;">Category {selected_main_id}: {MAIN_MENU[selected_main_id]}</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Category 1: Email Isolation Elements (with sub-menu)
    if selected_main_id == 1:
        st.markdown("### EMAIL ISOLATION ELEMENTS – Subcategories")
        sub_id = st.selectbox(
            "Select Email Elements subcategory (1–5)",
            options=list(EMAIL_ELEMENTS_SUBMENU.keys()),
            format_func=lambda k: f"{k}. {EMAIL_ELEMENTS_SUBMENU[k]}",
        )

        if sub_id == 1:
            st.markdown("#### EMAIL COMPONENTS")
            st.text_area("Details", EMAIL_COMPONENTS_TEXT, height=400)
        elif sub_id == 2:
            st.markdown("#### RELATED COMPONENTS")
            st.text_area("Details", EMAIL_RELATED_COMPONENTS_TEXT, height=400)
        elif sub_id == 3:
            st.markdown("#### EMAIL PROTOCOLS")
            st.text_area("Details", EMAIL_PROTOCOLS_TEXT, height=400)
        elif sub_id == 4:
            st.markdown("#### EMAIL FORMATS")
            st.text_area("Details", EMAIL_FORMATS_TEXT, height=400)
        elif sub_id == 5:
            st.markdown("#### SECURE WEB-MAIL SOLUTIONS")
            st.text_area("Details", SECURE_WEBMAIL_TEXT, height=350)

    elif selected_main_id == 2:
        st.markdown("### EMAIL STANDARDS")
        st.text_area(
            "Details",
            """
Email standards define the protocols, formats, and security mechanisms that underpin interoperable messaging.

Core Standards:
- SMTP for transport
- MIME for message structure
- POP/IMAP for mailbox access

Security Standards:
- SPF: declares authorized sending IPs
- DKIM: signs messages with domain keys
- DMARC: enforces alignment and policies
- S/MIME and OpenPGP: provide encryption and signatures

Real-world example:
A SaaS provider configures SPF, DKIM, and DMARC for its domain to ensure that customers can trust invoices and notifications.
            """,
            height=400,
        )

    elif selected_main_id == 3:
        st.markdown("### EMAIL SECURITY THREATS")
        st.text_area(
            "Details",
            """
Email security threats include:

- Phishing and spear-phishing
- Business Email Compromise (BEC)
- Malware and ransomware delivery
- Credential harvesting
- Data exfiltration via attachments or links

Real-world example:
An attacker sends a fake invoice to finance@company.com with a malicious macro-enabled spreadsheet.
Without isolation, opening the file on a finance workstation could trigger ransomware.
With isolation, the spreadsheet opens in a remote sandbox, and the macro never runs on the endpoint.
            """,
            height=400,
        )

    elif selected_main_id == 4:
        st.markdown("### EMAIL ISOLATION USE-CASES")
        st.text_area(
            "Details",
            """
Key use-cases for email isolation:

1. Isolating active content in HTML emails
2. Opening attachments in disposable or sandboxed environments
3. Rendering potentially malicious emails in remote browsers
4. Protecting high-value users (executives, admins)
5. Supporting incident response and forensic analysis

Real-world example:
A CISO mandates that all emails to the executive team are rendered via a remote browser solution.
Executives see full content, but any malicious scripts run in a controlled environment.
            """,
            height=400,
        )

    elif selected_main_id == 5:
        st.markdown("### EMAIL-MALWARE INCIDENTS PREVENTION")
        st.text_area(
            "Details",
            """
Prevention strategies:

- Signature-based and behavioral malware scanning
- Sandbox detonation of attachments
- URL rewriting and time-of-click analysis
- Blocking risky file types (e.g., .exe, .js, macro-enabled Office files)
- Enforcing strong authentication and encryption

Real-world example:
A healthcare organization blocks all macro-enabled Office attachments at the gateway and uses isolation for PDFs and images.
Suspicious content is opened in a sandbox, protecting clinical workstations.
            """,
            height=400,
        )

    elif selected_main_id == 6:
        st.markdown("### EMAIL-MALWARE INCIDENTS RESPONSE")
        st.text_area(
            "Details",
            """
Incident response steps:

- Identify affected users and mailboxes
- Quarantine malicious messages
- Revoke compromised credentials
- Analyze payloads in a forensic sandbox
- Communicate with stakeholders and regulators

Real-world example:
After detecting a phishing campaign, the SOC uses isolation logs to see which users opened the email and what actions were taken.
They quickly reset passwords and block the malicious domain.
            """,
            height=400,
        )

    elif selected_main_id == 7:
        st.markdown("### SIGNING & ENCRYPTING EMAIL MESSAGES")
        st.text_area(
            "Details",
            """
Digital signatures and encryption:

- S/MIME and OpenPGP provide authentication, integrity, and confidentiality
- Certificates and keys must be managed securely
- Policies define when signing and encryption are required

Real-world example:
A legal department requires all external communications to be signed and sensitive contracts to be encrypted.
Isolation respects signatures while still inspecting metadata and enforcing policy at trusted gateways.
            """,
            height=400,
        )

    elif selected_main_id == 8:
        st.markdown("### PLANNING & MANAGING EMAIL SERVERS")
        st.text_area(
            "Details",
            """
Planning and management:

- Capacity planning and high availability
- Backup and disaster recovery
- Patch management and configuration hardening
- Logging, monitoring, and alerting

Real-world example:
An enterprise deploys redundant MTAs in two data centers, with isolation gateways in front.
If one data center fails, email and isolation continue from the other site.
            """,
            height=400,
        )

    elif selected_main_id == 9:
        st.markdown("### SECURING THE EMAIL SERVERS OPERATING SYSTEMS")
        st.text_area(
            "Details",
            """
OS security for email servers:

- Harden baselines (CIS benchmarks)
- Disable unnecessary services
- Enforce least privilege
- Apply timely patches
- Monitor for anomalous activity

Real-world example:
A Linux-based MTA runs on a hardened OS image with SELinux enforced, SSH restricted, and configuration managed via Ansible.
Isolation components rely on this hardened platform.
            """,
            height=400,
        )

    elif selected_main_id == 10:
        st.markdown("### SECURING EMAIL SERVER CONTENTS")
        st.text_area(
            "Details",
            """
Securing contents:

- Access control and role-based permissions
- Encryption at rest for mailboxes and archives
- Retention and deletion policies
- Legal hold mechanisms
- Protection against unauthorized export

Real-world example:
A financial institution encrypts all mailbox databases and uses DLP to prevent sensitive data (e.g., account numbers) from leaving via email.
Isolation integrates with DLP to inspect content safely.
            """,
            height=400,
        )

    elif selected_main_id == 11:
        st.markdown("### IMPLEMENTING SECURE NETWORK INFRASTRUCTURE")
        st.text_area(
            "Details",
            """
Network security for email:

- Segmented networks and DMZs
- Firewalls and secure DNS
- TLS for all server-to-server and client-to-server connections
- IDS/IPS and SIEM integration

Real-world example:
MTAs and isolation gateways sit in a DMZ, with strict firewall rules controlling inbound and outbound SMTP.
TLS is enforced with modern ciphers, and logs feed into a central SIEM.
            """,
            height=400,
        )

    elif selected_main_id == 12:
        st.markdown("### SECURING EMAIL CLIENTS")
        st.text_area(
            "Details",
            """
Client security:

- Hardened configurations (disable macros, active content)
- Secure protocols (IMAP/POP over TLS)
- Endpoint protection (EDR/AV)
- Regular updates and patching

Real-world example:
A company configures Outlook via group policy to disable automatic macro execution and to warn users about external content.
Isolation further reduces risk by rendering risky content remotely.
            """,
            height=400,
        )

    elif selected_main_id == 13:
        st.markdown("### ADMINISTERING THE EMAIL SERVERS")
        st.text_area(
            "Details",
            """
Administration:

- Account provisioning and deprovisioning
- Role-based access control
- Monitoring and logging
- Change management and approvals
- Auditing administrative actions

Real-world example:
Admin access to MTAs and isolation gateways is controlled via just-in-time privileged access, with all actions logged and reviewed.
            """,
            height=400,
        )

    elif selected_main_id == 14:
        st.markdown("### AUTHENTICATING A SENDING DOMAIN & EMAIL MESSAGES")
        st.text_area(
            "Details",
            """
Authentication mechanisms:

- SPF: validates sending IPs
- DKIM: signs messages with domain keys
- DMARC: enforces alignment and policies
- Reputation services and TLS certificate validation

Real-world example:
A retailer uses DMARC with 'p=quarantine' and monitors reports.
Isolation uses SPF/DKIM/DMARC results to decide whether to render content in a high-risk sandbox or block it outright.
            """,
            height=400,
        )

    elif selected_main_id == 15:
        st.markdown("### PROTECTING EMAIL CONFIDENTIALITY")
        st.text_area(
            "Details",
            """
Confidentiality controls:

- Encryption in transit (TLS)
- Encryption at rest (disk/database encryption)
- End-to-end encryption (S/MIME, OpenPGP)
- Policies for sensitive data handling

Real-world example:
A healthcare provider encrypts all email containing patient data and uses isolation to safely inspect metadata and routing information
without exposing the content to untrusted systems.
            """,
            height=400,
        )

    elif selected_main_id == 16:
        st.markdown("### REDUCING UNSOLICITED BULK EMAIL")
        st.text_area(
            "Details",
            """
Spam reduction:

- Content filtering and Bayesian analysis
- Reputation-based blocking and blacklists
- Rate limiting and feedback loops
- DMARC enforcement

Real-world example:
An ISP uses machine learning-based spam filters plus DMARC enforcement.
Isolation ensures that any spam that slips through is rendered safely and cannot easily compromise endpoints.
            """,
            height=400,
        )

    elif selected_main_id == 17:
        st.markdown("### END USER EMAIL SECURITY RECOMMENDATIONS")
        st.text_area(
            "Details",
            """
End-user best practices:

- Recognize phishing and suspicious requests
- Avoid clicking unknown links or opening unexpected attachments
- Use strong, unique passwords and MFA
- Report suspicious messages promptly

Real-world example:
A company runs quarterly phishing simulations and provides just-in-time training.
Isolation reduces the impact of mistakes, but user vigilance remains critical.
            """,
            height=400,
        )

    # Conceptual flow diagram (Mermaid)
    st.markdown("#### Conceptual Flow (Mermaid)")
    mermaid = f"""
flowchart TD
    User[End User / Admin] --> Menu[Select Category {selected_main_id}]
    Menu --> Engine[Email Isolation Framework Engine]
    Engine --> Policy[Policies / Controls for {MAIN_MENU[selected_main_id]}]
    Policy --> Report[Exported Report / Synthetic Data]
    """
    st.markdown(f"```mermaid\n{mermaid}\n```")

    # Additional diagram (Graphviz)
    st.markdown("#### Structural Diagram (Graphviz)")
    graphviz_src = f"""
digraph G {{
    rankdir=LR;
    node [shape=box, style=filled, color="#e0f2ff"];

    User -> Menu;
    Menu -> Engine;
    Engine -> Policy;
    Policy -> Report;

    Engine [label="Engine\\n({MAIN_MENU[selected_main_id]})"];
}}
"""
    st.graphviz_chart(graphviz_src)

with col_right:
    st.subheader("Synthetic Email Isolation Framework Data")
    st.dataframe(synthetic_data, use_container_width=True)

# ---------------------------------------------------------
# Export functions
# ---------------------------------------------------------
def build_text_report(category_id, synthetic_data):
    lines = [
        "Email Isolation Framework Report",
        "Developed by Randy Singh, Computer Scientist (October 2020)",
        "",
        f"Selected Category: {category_id}. {MAIN_MENU[category_id]}",
        "",
        "Synthetic Data Records:",
        f"Total: {len(synthetic_data)}",
        "",
    ]
    for row in synthetic_data[:50]:
        lines.append(
            f"{row['record_id']}: {row['category']} | Risk: {row['risk_level']} | "
            f"Maturity: {row['maturity_score']} | Status: {row['status']}"
        )
    return "\n".join(lines)

def export_pdf(text):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    y = 750
    for line in text.split("\n"):
        c.drawString(40, y, line[:100])
        y -= 15
        if y < 40:
            c.showPage()
            y = 750
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

def export_json(category_id, synthetic_data):
    payload = {
        "category_id": category_id,
        "category_name": MAIN_MENU[category_id],
        "synthetic_data": synthetic_data,
        "generated_at": datetime.utcnow().isoformat() + "Z",
    }
    buffer = BytesIO()
    buffer.write(json.dumps(payload, indent=2).encode())
    buffer.seek(0)
    return buffer

# ---------------------------------------------------------
# Export buttons
# ---------------------------------------------------------
st.markdown("---")
st.subheader("Export Email Isolation Framework Report")

report_text = build_text_report(selected_main_id, synthetic_data)

c1, c2, c3 = st.columns(3)
with c1:
    st.download_button("📄 PDF", export_pdf(report_text), "email_isolation_report.pdf")
with c2:
    st.download_button("📝 Word", export_word(report_text), "email_isolation_report.docx")
with c3:
    st.download_button("🧾 JSON", export_json(selected_main_id, synthetic_data), "email_isolation_report.json")
