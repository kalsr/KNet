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
            Developed by Randy Singh, Computer Scientist (October 2020)
        </h4>
        <h5 style="color:white;text-align:center;margin-top:0;">
            Email Isolation is one of the technologies listed in FY21 vision (Mr. Steven Wallace All Hands, Oct 22, 2020)
        </h5>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    This Streamlit application is a modern, cloud‑safe version of the original Java **EmailIsolationMenu** framework.  
    It presents the 17 main categories of the Email Isolation Framework, with detailed content for **Email Elements**  
    and structured content for all other categories.
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
Mail User Agents (MUAs):
A MUA is a software component (or web interface) that allows an end user to compose and send messages to one or more recipients.
A MUA transmits new messages to a server for further processing (either final delivery or transfer to another server).
The MUA is also the component used by end users to access a mailbox where in-bound emails have been delivered.
MUAs are available for a variety of systems including mobile hosts.
The proper secure configuration for an MUA depends on the MUA in question and the system it is running on.
MUAs may utilize several protocols to connect to and communicate with email servers.
There may also be other features as well such as a cryptographic interface for producing encrypted and/or digitally signed email.

Mail Transfer Agents (MTAs):
Email is transmitted, in a store and forward fashion, across networks via Mail Transfer Agents (MTAs).
MTAs communicate using the Simple Mail Transfer Protocol (SMTP) and act as both client and server, depending on the situation.
For example, an MTA can act as a server when accepting an email message from an end user's MUA, then act as a client in connecting to
and transferring the message to the recipient domain's MTA for final delivery.

Mail Submission Agents (MSA):
An MTA that accepts mail from MUAs and begins the transmission process by sending it to an MTA for further processing.
Often the MSA and first-hop MTA is the same process, just fulfilling both roles.

Mail Delivery Agent (MDA):
An MTA that receives mail from an organization's inbound MTA and ultimately places the message in a specific mailbox.
Mail servers may also perform various security functions to prevent malicious email from being delivered or include authentication
credentials such as digital signatures.

Special Use Components:
In addition to MUAs and MTAs, an organization may use one or more special purpose components for a particular task, such as malware
filtering, email archiving, or content filtering.

Special Considerations for Cloud and Hosted Service Customers:
Organizations that outsource their email service (whole or in part) may not have direct access to MTAs or special use components.
In Email as a Service (EaaS), the service provider is responsible for the email infrastructure; in Infrastructure as a Service (IaaS),
customers may configure their own email servers.
"""

EMAIL_RELATED_COMPONENTS_TEXT = """
In addition to MUAs and MTAs, there are other network components used to support the email service for an organization.

Domain Name System (DNS):
DNS is a global, distributed database and lookup protocol used to map domain names to IP addresses.
MUAs use DNS to find MSAs; MTAs use DNS to find the next-hop server via MX records.
Reverse DNS is used to map IP addresses to domain names and is sometimes used as a crude authentication check.

DNS and Email Security:
DNS publishes policy artifacts and public keys for SPF, DKIM, and related technologies used to validate that messages originate
from authorized mail servers.
Reputation services also use DNS-based data to assess authenticity and combat spam and malicious email.

Enterprise Perimeter Security Components:
Firewalls, IDS, and malware scanners may affect email transactions even if they do not directly handle email.
Misconfiguration can block legitimate SMTP connections and prevent valid email delivery.

Public Key Infrastructure (PKIX):
Organizations that use S/MIME, OpenPGP, or TLS rely on certificate infrastructure.
X.509 certificates authenticate TLS endpoints and certify public keys used for digital signatures and encryption.
"""

EMAIL_PROTOCOLS_TEXT = """
There are two types of protocols used in the transmission of email:
1) Protocols used to transfer messages between MTAs and end users (MUAs).
2) Protocols used to transfer messages between mail servers.

Simple Mail Transfer Protocol (SMTP):
SMTP is a text-based client-server protocol used to transfer email messages from one server to another or from an MUA to an MSA/MTA.
Clients send ASCII commands; servers respond with ASCII status codes.

Mail Access Protocols (POP3, IMAP, MAPI/RPC):
MUAs typically use POP3 or IMAP to retrieve mail from a mailbox.
POP3 usually downloads all mail and may delete it from the server; IMAP keeps mail on the server and supports multiple clients accessing
the same mailbox.
Both POP3 and IMAP can be secured via TLS (ports 995 and 993 respectively, or STARTTLS on 110/143).
Microsoft Exchange clients may use MAPI/RPC; some cloud providers use web portals as MUAs.

Internet Email Addresses:
SMTP uses an envelope MAIL FROM address; email headers contain a FROM address.
Both consist of local-part@domain-part.
"""

EMAIL_FORMATS_TEXT = """
Email messages may be formatted as plain text or as compound documents containing multiple components and attachments.

Multi-Purpose Internet Mail Extensions (MIME):
MIME allows email to contain non-ASCII character sets and non-text components.
Messages are broken into parts, each with a content type (e.g., text/plain, image/jpeg, text/html).
MIME messages can be nested and include attachments.

Security in MIME Messages (S/MIME):
S/MIME provides authentication, integrity, non-repudiation (via digital signatures), and confidentiality (via encryption).
It uses public key cryptography and X.509 certificates.
Messages can be signed, encrypted, or both.

Pretty Good Privacy (PGP/OpenPGP):
OpenPGP is an open standard for signing and encrypting email, derived from PGP.
It defines formats for keys, signatures, and messages and is widely implemented (e.g., GnuPG).
"""

SECURE_WEBMAIL_TEXT = """
Secure web-mail solutions provide browser-based access to email while enforcing strong authentication, TLS encryption,
content filtering, and isolation of active content (scripts, macros, embedded objects). They are often deployed as part of
zero-trust architectures, ensuring that email is rendered in a controlled environment and limiting direct exposure of endpoints
to malicious payloads.
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
            st.text_area("Details", SECURE_WEBMAIL_TEXT, height=300)

    # Categories 2–17: concrete content
    elif selected_main_id == 2:
        st.markdown("### EMAIL STANDARDS")
        st.text_area(
            "Details",
            "Email standards define the protocols, formats, and security mechanisms that underpin interoperable messaging. "
            "Core standards include SMTP for transport, MIME for message structure, and POP/IMAP for mailbox access. "
            "Security-related standards include SPF, DKIM, DMARC, S/MIME, and OpenPGP, which collectively address "
            "authentication, integrity, confidentiality, and anti-spoofing. A robust email isolation framework aligns "
            "with these standards to ensure compatibility while enforcing stronger controls.",
            height=350,
        )

    elif selected_main_id == 3:
        st.markdown("### EMAIL SECURITY THREATS")
        st.text_area(
            "Details",
            "Email security threats include phishing, spear-phishing, business email compromise (BEC), malware delivery, "
            "ransomware, credential harvesting, and data exfiltration via attachments or links. Attackers exploit human "
            "trust, weak authentication, and unpatched clients or servers. An isolation framework mitigates these threats "
            "by separating untrusted content from endpoints, scanning attachments and URLs, enforcing policy-based "
            "controls, and integrating threat intelligence.",
            height=350,
        )

    elif selected_main_id == 4:
        st.markdown("### EMAIL ISOLATION USE-CASES")
        st.text_area(
            "Details",
            "Key use-cases for email isolation include: (1) isolating active content in HTML emails; (2) opening attachments "
            "in disposable or sandboxed environments; (3) rendering potentially malicious emails in remote browsers; "
            "(4) protecting high-value users such as executives and system administrators; and (5) supporting incident "
            "response by safely analyzing suspicious messages. These use-cases align with zero-trust principles and "
            "reduce the attack surface of the enterprise.",
            height=350,
        )

    elif selected_main_id == 5:
        st.markdown("### EMAIL-MALWARE INCIDENTS PREVENTION")
        st.text_area(
            "Details",
            "Prevention focuses on blocking malware before it reaches end users. Controls include signature-based and "
            "behavioral malware scanning, sandbox detonation of attachments, URL rewriting and time-of-click analysis, "
            "policy-based blocking of risky file types, and enforcement of strong authentication and encryption. "
            "Email isolation adds another layer by ensuring that even if malicious content is delivered, it is executed "
            "in a controlled environment rather than on the endpoint.",
            height=350,
        )

    elif selected_main_id == 6:
        st.markdown("### EMAIL-MALWARE INCIDENTS RESPONSE")
        st.text_area(
            "Details",
            "Incident response for email-based malware includes rapid identification of affected users, quarantine of "
            "malicious messages, revocation of compromised credentials, forensic analysis of payloads, and coordinated "
            "communication with stakeholders. Isolation platforms can capture detailed telemetry about how a message was "
            "rendered and interacted with, supporting root-cause analysis and improving future detection and prevention.",
            height=350,
        )

    elif selected_main_id == 7:
        st.markdown("### SIGNING & ENCRYPTING EMAIL MESSAGES")
        st.text_area(
            "Details",
            "Digital signatures (S/MIME, OpenPGP) provide authentication, integrity, and non-repudiation for email, while "
            "encryption protects confidentiality. Proper key management, certificate validation, and policy enforcement "
            "are critical. An isolation framework must respect cryptographic protections while still inspecting metadata "
            "and enforcing organizational policies, for example by scanning encrypted content at trusted gateways or "
            "requiring secure key escrow for regulated environments.",
            height=350,
        )

    elif selected_main_id == 8:
        st.markdown("### PLANNING & MANAGING EMAIL SERVERS")
        st.text_area(
            "Details",
            "Planning and managing email servers involves capacity planning, high availability design, backup and recovery, "
            "patch management, and configuration hardening. Administrators must define clear roles for MTAs, MDAs, and "
            "gateways, integrate logging and monitoring, and align with organizational security policies. Email isolation "
            "components are typically deployed alongside or in front of these servers, requiring careful architectural "
            "integration and change management.",
            height=350,
        )

    elif selected_main_id == 9:
        st.markdown("### SECURING THE EMAIL SERVERS OPERATING SYSTEMS")
        st.text_area(
            "Details",
            "Securing the operating systems that host email servers includes hardening baselines, disabling unnecessary "
            "services, enforcing least privilege, applying timely patches, and monitoring for anomalous activity. "
            "Configuration management and compliance scanning help ensure that OS-level vulnerabilities do not undermine "
            "the security of the email infrastructure. Isolation solutions rely on these hardened platforms to provide "
            "trustworthy execution environments.",
            height=350,
        )

    elif selected_main_id == 10:
        st.markdown("### SECURING EMAIL SERVER CONTENTS")
        st.text_area(
            "Details",
            "Email server contents—mailboxes, archives, logs—often contain sensitive information. Controls include access "
            "control, encryption at rest, retention and deletion policies, legal hold mechanisms, and protection against "
            "unauthorized export. Isolation frameworks may integrate with content scanning and data loss prevention (DLP) "
            "to ensure that sensitive data is not leaked via email.",
            height=350,
        )

    elif selected_main_id == 11:
        st.markdown("### IMPLEMENTING SECURE NETWORK INFRASTRUCTURE")
        st.text_area(
            "Details",
            "Secure network infrastructure for email includes segmented networks, firewalls, secure DNS, TLS for all "
            "server-to-server and client-to-server connections, and intrusion detection/prevention systems. Email "
            "isolation components often sit at network boundaries, requiring secure routing, certificate management, and "
            "integration with SIEM and SOC workflows.",
            height=350,
        )

    elif selected_main_id == 12:
        st.markdown("### SECURING EMAIL CLIENTS")
        st.text_area(
            "Details",
            "Securing email clients (MUAs) involves hardening configurations, disabling risky features (macros, active "
            "content), enforcing secure protocols (IMAP/POP over TLS), and integrating endpoint protection. Isolation "
            "reduces reliance on client-side defenses by rendering untrusted content remotely, but client hygiene remains "
            "essential for credentials, local data, and user behavior.",
            height=350,
        )

    elif selected_main_id == 13:
        st.markdown("### ADMINISTERING THE EMAIL SERVERS")
        st.text_area(
            "Details",
            "Administration covers account provisioning, role-based access control, monitoring, logging, change management, "
            "and policy enforcement. Secure administration requires strong authentication, just-in-time access, and "
            "auditing of administrative actions. Isolation frameworks may expose administrative consoles and APIs that "
            "must be protected with the same rigor as core email servers.",
            height=350,
        )

    elif selected_main_id == 14:
        st.markdown("### AUTHENTICATING A SENDING DOMAIN & EMAIL MESSAGES")
        st.text_area(
            "Details",
            "Authenticating sending domains and messages relies on SPF, DKIM, and DMARC, plus reputation services and "
            "TLS with certificate validation. These mechanisms help distinguish legitimate email from spoofed or "
            "fraudulent messages. Isolation platforms can use authentication results to decide how aggressively to "
            "isolate or block content, and to feed signals into broader threat intelligence systems.",
            height=350,
        )

    elif selected_main_id == 15:
        st.markdown("### PROTECTING EMAIL CONFIDENTIALITY")
        st.text_area(
            "Details",
            "Confidentiality is protected through encryption in transit (TLS) and at rest, plus end-to-end encryption "
            "mechanisms like S/MIME and OpenPGP. Policy controls determine when encryption is required, how keys are "
            "managed, and how exceptions are handled. Isolation must coexist with confidentiality, ensuring that sensitive "
            "messages are handled securely while still enabling necessary inspection and control at trusted points.",
            height=350,
        )

    elif selected_main_id == 16:
        st.markdown("### REDUCING UNSOLICITED BULK EMAIL")
        st.text_area(
            "Details",
            "Reducing unsolicited bulk email (spam) involves content filtering, reputation-based blocking, rate limiting, "
            "feedback loops, and enforcement of DMARC policies. Advanced systems use machine learning to classify messages "
            "and adapt to evolving spam campaigns. Isolation adds resilience by ensuring that even spam that bypasses "
            "filters is rendered safely and cannot easily compromise endpoints.",
            height=350,
        )

    elif selected_main_id == 17:
        st.markdown("### END USER EMAIL SECURITY RECOMMENDATIONS")
        st.text_area(
            "Details",
            "End users should be trained to recognize phishing, avoid clicking unknown links, verify unexpected requests, "
            "use strong and unique passwords, enable multi-factor authentication, and report suspicious messages. "
            "Security awareness programs, simulated phishing campaigns, and clear reporting channels are essential. "
            "Email isolation supports users by reducing the impact of mistakes, but human vigilance remains a critical "
            "layer of defense.",
            height=350,
        )

    # Conceptual flow diagram
    st.markdown("#### Conceptual Flow (Mermaid)")
    mermaid = f"""
flowchart TD
    User[End User / Admin] --> Menu[Select Category {selected_main_id}]
    Menu --> Engine[Email Isolation Framework Engine]
    Engine --> Policy[Policies / Controls for {MAIN_MENU[selected_main_id]}]
    Policy --> Report[Exported Report / Synthetic Data]
    """
    st.markdown(f"```mermaid\n{mermaid}\n```")

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
