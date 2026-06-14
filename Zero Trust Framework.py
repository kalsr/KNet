import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random
import json
import io
from datetime import datetime, timedelta

# ─── Optional export dependencies ─────────────────────────────────────────────
try:
    from fpdf import FPDF
    FPDF_AVAILABLE = True
except ImportError:
    FPDF_AVAILABLE = False

try:
    from docx import Document as DocxDocument
    from docx.shared import RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    DOCX_AVAILABLE = True
except ImportError:
    DOCX_AVAILABLE = False

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE CONFIG
# ══════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Zero-Trust Framework | KNet Consulting",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════════════════════
#  GLOBAL STYLES (Option A – Deep Blue Federal Theme)
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    """
<style>
  body {
      background-color: #f4f7fc;
      font-family: "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  }
  .zt-title {
      text-align: center; font-size: 2.6rem; font-weight: 900;
      color: #003087; letter-spacing: 1px; margin-bottom: 0;
  }
  .zt-subtitle {
      text-align: center; font-size: 1.1rem; font-weight: 700;
      color: #0047AB; margin-top: 4px; margin-bottom: 6px;
  }
  .zt-tagline {
      text-align: center; color: #555; font-size: 0.9rem; margin-bottom: 20px;
  }
  .zt-hr { border: 2px solid #0047AB; margin: 10px 0 22px 0; }

  .section-header {
      background: linear-gradient(90deg, #003087 0%, #1a6fe8 100%);
      color: white; padding: 10px 18px; border-radius: 8px;
      font-weight: 700; font-size: 1.1rem; margin: 14px 0 10px 0;
      box-shadow: 0 2px 6px rgba(0,0,0,0.18);
  }

  .req-card {
      background: #f0f6ff; border-left: 4px solid #0047AB;
      border-radius: 8px; padding: 10px 14px; margin: 6px 0;
      font-size: 0.92rem; box-shadow: 0 1px 4px rgba(0,0,0,0.08);
  }
  .rec-card {
      background: #fff8e1; border-left: 4px solid #f0a500;
      border-radius: 8px; padding: 10px 14px; margin: 6px 0;
      font-size: 0.92rem; box-shadow: 0 1px 4px rgba(0,0,0,0.08);
  }
  .sol-card {
      background: #e8f5e9; border-left: 4px solid #2e7d32;
      border-radius: 8px; padding: 10px 14px; margin: 6px 0;
      font-size: 0.92rem; box-shadow: 0 1px 4px rgba(0,0,0,0.08);
  }

  div[data-testid="metric-container"] {
      background: #f0f6ff; border: 1px solid #c2d9ff;
      border-radius: 10px; padding: 12px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  }

  section[data-testid="stSidebar"] {
      background: #001a6b;
  }
  section[data-testid="stSidebar"] * {
      color: #e8f0ff !important;
  }
  section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2 {
      color: #ffffff !important;
  }
  .sidebar-box {
      background: rgba(255,255,255,0.06);
      padding: 10px 12px;
      border-radius: 8px;
      margin-bottom: 12px;
      border: 1px solid rgba(255,255,255,0.12);
  }
  .sidebar-footer {
      font-size: 0.8rem;
      color: #cbd4ff;
      text-align: center;
      margin-top: 10px;
  }
</style>
""",
    unsafe_allow_html=True,
)

# ══════════════════════════════════════════════════════════════════════════════
#  HEADER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    '<p class="zt-title">ZERO-TRUST FRAMEWORK APPLICATION</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="zt-subtitle">Developed by Randy Singh | KalSnet (KNet) Consulting Group</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="zt-tagline">Based on DISA/BDE5 ZTA Working Group Requirements &amp; Use Cases &nbsp;|&nbsp; Originally authored April 2019</p>',
    unsafe_allow_html=True,
)
st.markdown('<hr class="zt-hr">', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  DATA DEFINITIONS
# ══════════════════════════════════════════════════════════════════════════════
FUNCTIONAL_REQUIREMENTS = {
    "Identity & Authentication": {
        "requirement": "Need to associate identity to user and device.",
        "example": "Active Directory + certificate-based device identity via PKI/CAC cards.",
        "solution": "Deploy a centralised Identity Provider (IdP) such as Microsoft Entra ID or Okta integrated with LDAP/SAML.",
        "recommendation": "Enforce MFA for every user login. Bind device certificates to hardware TPM chips to prevent credential theft.",
    },
    "Health & Compliance": {
        "requirement": "Need to determine patch level and security posture of device prior to network authorization.",
        "example": "NAC solution checks OS STIG compliance, AV status, and missing agents before granting network access.",
        "solution": "Integrate a Network Access Control (NAC) platform such as Cisco ISE or Forescout with your IdP.",
        "recommendation": "Define a minimum compliance baseline (patch age <= 30 days, STIG score >= 80%). Non-compliant devices land in an auto-remediation VLAN.",
    },
    "Authorization": {
        "requirement": "Need to authorize user/device, based on identity and hygiene, at micro-perimeter or Just-In-Time (JIT) for administrators.",
        "example": "PAM tool grants time-limited SSH/RDP session to admin only after ITSM ticket is validated.",
        "solution": "Deploy a Privileged Access Management (PAM) solution (CyberArk, BeyondTrust) with JIT provisioning tied to ServiceNow tickets.",
        "recommendation": "Apply least-privilege RBAC. Rotate JIT credentials every session. Log every privileged action to SIEM.",
    },
    "Accounting": {
        "requirement": "Need to identify and document resources consumed by users and administrators for compliance and incident response.",
        "example": "Splunk SIEM ingests auth logs, network flow data, and privileged session recordings.",
        "solution": "Centralise logging via a SIEM (Splunk, Microsoft Sentinel). Feed NetFlow data and endpoint telemetry.",
        "recommendation": "Retain logs for at least 12 months online, 36 months archived. Automate anomaly alerting with UEBA rules.",
    },
    "Segmentation": {
        "requirement": "Need to limit communication (directional port/protocol) between all network flows including application tiers.",
        "example": "Micro-segmentation policy allows only TCP 443 from Web tier to App tier; all other flows are denied.",
        "solution": "Implement software-defined micro-segmentation (VMware NSX, Illumio, or Guardicore). Define allow-lists per workload.",
        "recommendation": "Start with ring-fence of crown-jewel systems. Expand micro-segmentation iteratively. Validate with automated penetration tests.",
    },
    "Orchestration": {
        "requirement": "Need capability to dynamically provision identity, hygiene, authorization, and segmentation policies.",
        "example": "Ansible playbook triggered by new VM spin-up auto-pushes firewall rules and registers device in IdP.",
        "solution": "Use a Security Orchestration platform (SOAR) or Infrastructure-as-Code (Terraform + Ansible) with REST API integration to all ZTA pillars.",
        "recommendation": "Treat policies as code. Store in Git. Enforce CI/CD pipeline validation before deployment. Run automated compliance checks post-deploy.",
    },
}

USE_CASES = {
    "Use Case 1 - End-User Authentication & Authorization": [
        "User leverages Multi-Factor Authentication (MFA) to establish identity via a centralised Identity Provider.",
        "Device establishes identity via certificate-based authentication (PKI/CAC).",
        "Health & Compliance tool confirms security posture, patch status, and required tool presence.",
        "Real-time contextual access control is determined by validated identity + device health score.",
        "Network authorisation granted based on contextual access control policy.",
        "All authentication & authorisation activities are logged to SIEM (Splunk/Sentinel).",
    ],
    "Use Case 2 - Application & Data Segmentation": [
        "Software-Defined Networking (SDN) enables MicroCore & Perimeter (MCAP) for switching/routing + firewall.",
        "Each application tier (Web, App, DB) enforces granular port/protocol firewall policy.",
        "Application processes are learned and whitelisted for legitimate port/protocol usage.",
        "Data is tagged and specifically associated with owning systems/applications.",
        "All authorisation activities are logged to SIEM.",
        "All authentication & authorisation occur against the centralised Identity Provider.",
    ],
    "Use Case 3 - Admin Authentication & Authorization": [
        "Administrator authenticates via MFA against a centralised Identity Provider.",
        "Just-In-Time (JIT) gateway grants time-limited access to specific systems upon valid ITSM ticket.",
        "Systems managed via JIT Gateway or API-driven orchestration tool over isolated management segment.",
        "All authorisation activities logged to SIEM.",
        "Centralised Identity Provider leveraged for all identities and authorisations.",
    ],
    "Use Case 4 - Security Policy Orchestration": [
        "SDE Global Orchestrator enables service delivery and cyber operations across the agency.",
        "Service-level orchestrators deploy specific systems and associated granular security policies via API.",
        "Policy Enforcement Engines accept policy via REST API and enforce on infrastructure.",
        "All orchestration activities logged to SIEM.",
        "Orchestrated policies include deployment of identity and roles on centralised Identity Provider.",
    ],
}

ARCHITECTURAL_REQUIREMENTS = {
    "Identity Requirements": [
        "1. The system shall NOT assume trust of the device or user.",
        "1.1 The system shall have the capability to identify the user.",
        "1.2 The system shall have the capability to identify the device.",
        "1.2.1 The system shall be able to identify client and server endpoints.",
        "1.2.2 The system shall be able to identify network devices.",
        "2. The system shall integrate with an enterprise identity provider.",
        "2.1 The system shall integrate with industry-standard providers: AD, RADIUS, LDAP, OAuth, OpenID Connect, SAML.",
        "3. The system shall support enterprise authentication methods.",
        "3.1 The system shall support certificate-based authentication.",
        "3.2 The system shall support Public Key Infrastructure (PKI).",
        "3.3 The system shall support or integrate with Multi-Factor Authentication (MFA).",
        "4. The system shall have the ability to continuously challenge identity.",
        "4.1 The system shall support multiple attributes (e.g., geolocation) to challenge identity.",
        "5. The system shall connect to a centralised identity source.",
        "6. The system shall redirect or drop unidentified users or machines.",
    ],
    "Health & Compliance Requirements": [
        "1. The system shall determine endpoint health & compliance.",
        "1.1 The system shall determine OS STIG compliance posture.",
        "1.2 The system shall determine patch level of the device.",
        "1.3 The system shall determine if required tools/agents are missing.",
        "1.4 The system shall detect unauthorised software on the device.",
        "1.5 The system shall determine FQDN, IP, MAC address, and OS of the device.",
        "2. The system shall place non-compliant machines in remediation.",
        "3. The system shall support health & compliance checks across multiple device types.",
    ],
    "Authorization Requirements": [
        "1. The system shall control authorisation of users and machines.",
        "1.1 The system shall assign role-based access controls (RBAC) to groups and users.",
        "2. The system shall support time-limited authorisation for administrators.",
        "2.1 The system shall provide a portal to request privileged access (JIT).",
        "3. The system shall associate identity to authorisation policy via ZTA tool integration.",
        "3.1 The system shall align network security policy to authorisation of users and machines.",
        "4. The system shall support dynamic/real-time access decisions.",
        "5. The system shall support querying to determine authorisation level of user or device.",
    ],
    "Accounting & Auditing Requirements": [
        "1. The system shall provide accounting of all elements within the ZTA.",
        "1.1 The system shall account for user and device identity events.",
        "1.2 The system shall account for each authorisation grant or change.",
        "1.3 The system shall account for each segmentation policy change.",
        "2. The system shall account for all network flows within the ZTA.",
        "2.1 The system shall provide packet capture capability.",
        "2.2 The system shall log and account for all production data flow transactions.",
        "2.3 The system shall support offloading to enterprise SIEM tools.",
        "3. The system shall provide log data via REST API to a log aggregator.",
    ],
    "Segmentation Requirements": [
        "1. The system shall provide network micro-segmentation of application systems.",
        "1.1 The system shall apply role-based rule sets to groups and individual systems.",
        "1.2 The system shall segment north-south network flows.",
        "1.3 The system shall segment east-west network flows.",
        "1.4 The system shall segment end-to-end / transport network flows.",
        "2. The system shall segment both stateless and stateful application flows.",
        "3. The system shall segment host-level processes for security policies.",
    ],
    "Orchestration Requirements": [
        "1. The system shall support automation through REST APIs.",
        "1.1 The system shall accept REST API calls to configure identity, security, and accounting policies.",
        "2. The system shall support dynamic policy enforcement and changes.",
    ],
    "Cloud, Data Tagging & Discovery Requirements": [
        "1. The system shall provide the same protections across cloud-hosted environments.",
        "1.1 The system shall support CSP IaaS offerings.",
        "1.2 The system shall support CSP PaaS offerings.",
        "1.3 The system shall support CSP SaaS offerings.",
        "1.4 The system shall protect/proxy CSP administrative access.",
        "2. The system shall support tagging of data.",
        "3. The system shall support asset discovery.",
        "3.1 The system shall discover assets on the network.",
        "3.2 The system shall discover flows between assets on the network.",
    ],
    "Optional Requirements": [
        "1. The system shall replace existing security architecture constructs.",
        "1.1 The system shall replace existing perimeter security capabilities.",
        "2. The system shall integrate with existing security architecture constructs.",
        "2.1 The system shall integrate with Web Application Firewalls (WAF).",
        "2.2 The system shall integrate with application-aware firewalls (NGFW).",
        "2.3 The system shall integrate with database firewalls.",
        "2.4 The system shall integrate with Intrusion Prevention Systems (IPS).",
    ],
}

EVALUATION_CRITERIA = {
    "Effectiveness": {
        "definition": "Ability to accomplish mission objectives and achievement of desired results -- aligned to ZTA requirements.",
        "metrics": [
            "% of ZTA pillars fully implemented",
            "Mean Time to Detect (MTTD)",
            "Mean Time to Respond (MTTR)",
            "% reduction in lateral movement incidents",
        ],
        "target": ">= 90% pillar coverage; MTTD < 60 min; MTTR < 4 hrs",
        "recommendation": "Conduct quarterly ZTA maturity assessments against CISA ZT Maturity Model. Map every control to NIST SP 800-207.",
    },
    "Suitability": {
        "definition": "Ability of the solution to be supported in the intended operational environment, aligned to common operational requirements (automation, architecture, security).",
        "metrics": [
            "Vendor SLA uptime (%)",
            "Integration API coverage (%)",
            "STIG compliance score (%)",
            "Number of supported identity protocols",
        ],
        "target": "99.9% uptime; 100% REST API coverage; STIG score >= 85%",
        "recommendation": "Evaluate solutions against DoD APL. Require vendor FIPS 140-2/3 certification. Include operational sustainment costs in TCO model.",
    },
    "Performance": {
        "definition": "Measure of system performance expressed in quantifiable form -- focused on deployment footprint and scalability.",
        "metrics": [
            "Authentication latency (ms)",
            "Policy enforcement throughput (Gbps)",
            "Simultaneous sessions supported",
            "Auto-scale response time (sec)",
        ],
        "target": "Auth latency < 200ms; throughput >= 10 Gbps; >= 100K concurrent sessions",
        "recommendation": "Load-test at 150% of projected peak. Define auto-scaling triggers. Monitor with real-time dashboards (Grafana/Prometheus).",
    },
}

# ══════════════════════════════════════════════════════════════════════════════
#  SYNTHETIC DATA
# ══════════════════════════════════════════════════════════════════════════════
@st.cache_data
def generate_synthetic_data(n: int) -> pd.DataFrame:
    random.seed(42)
    pillars = [
        "Identity & Auth",
        "Health & Compliance",
        "Authorization",
        "Accounting",
        "Segmentation",
        "Orchestration",
    ]
    device_types = [
        "Workstation",
        "Server",
        "Mobile",
        "IoT Sensor",
        "Network Device",
        "Cloud VM",
    ]
    departments = [
        "CYBERCOM",
        "DISA/BDE5",
        "TRANSCOM",
        "DIA",
        "NSA",
        "SOCOM",
        "CENTCOM",
        "EUCOM",
    ]
    statuses = ["Compliant", "Non-Compliant", "Remediation", "Pending Review"]
    status_weights = [0.60, 0.20, 0.12, 0.08]
    os_list = [
        "Windows 11 STIG",
        "RHEL 9 STIG",
        "macOS Ventura",
        "Ubuntu 22.04 LTS",
        "Windows Server 2022",
    ]
    base_date = datetime(2024, 1, 1)
    records = []
    for i in range(1, n + 1):
        status = random.choices(statuses, weights=status_weights)[0]
        score = random.randint(60, 100) if status == "Compliant" else random.randint(20, 59)
        records.append(
            {
                "Record_ID": f"ZT-{i:04d}",
                "Timestamp": base_date
                + timedelta(days=random.randint(0, 364), hours=random.randint(0, 23)),
                "Pillar": random.choice(pillars),
                "Device_Type": random.choice(device_types),
                "Department": random.choice(departments),
                "OS": random.choice(os_list),
                "Compliance_Status": status,
                "STIG_Score": score,
                "Auth_Latency_ms": random.randint(45, 380),
                "Patch_Age_Days": random.randint(0, 90),
                "MFA_Enabled": random.choice([True, True, True, False]),
                "Segmentation_Policy_Applied": random.choice([True, True, False]),
                "Incident_Flagged": status == "Non-Compliant" and random.random() < 0.4,
            }
        )
    return pd.DataFrame(records)

# ══════════════════════════════════════════════════════════════════════════════
#  EXPORT HELPERS
# ══════════════════════════════════════════════════════════════════════════════
def build_text_report(selected_category: str, content: dict) -> str:
    lines = [
        "=" * 80,
        "  ZERO-TRUST FRAMEWORK APPLICATION",
        "  Developed by Randy Singh | KalSnet (KNet) Consulting Group",
        f"  Category: {selected_category}",
        f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "=" * 80,
        "",
    ]
    for key, val in content.items():
        lines.append(f"[{key}]")
        if isinstance(val, list):
            for item in val:
                lines.append(f"  * {item}")
        elif isinstance(val, dict):
            for k2, v2 in val.items():
                if isinstance(v2, list):
                    lines.append(f"  {k2}:")
                    for item in v2:
                        lines.append(f"    - {item}")
                else:
                    lines.append(f"  {k2}: {v2}")
        else:
            lines.append(f"  {val}")
        lines.append("")
    return "\n".join(lines)


def build_json_report(selected_category: str, content: dict) -> str:
    payload = {
        "framework": "Zero-Trust Framework Application",
        "author": "Randy Singh | KalSnet (KNet) Consulting Group",
        "category": selected_category,
        "generated": datetime.now().isoformat(),
        "data": content,
    }
    return json.dumps(payload, indent=2, default=str)


def _pdf_safe(text: str) -> str:
    replacements = [
        ("\u2013", "-"),
        ("\u2014", "--"),
        ("\u2018", "'"),
        ("\u2019", "'"),
        ("\u201c", '"'),
        ("\u201d", '"'),
        ("\u2026", "..."),
        ("\u2022", "*"),
        ("\u00a0", " "),
        ("\u2265", ">="),
        ("\u2264", "<="),
        ("\u00ae", "(R)"),
        ("\u2122", "(TM)"),
        ("\u00e9", "e"),
        ("\u00e8", "e"),
        ("\u00e0", "a"),
        ("\u00fc", "u"),
        ("\u00f6", "o"),
        ("\u00e4", "a"),
        ("\u00b0", " deg"),
        ("\u00b7", "-"),
        ("\u2212", "-"),
    ]
    for char, replacement in replacements:
        text = text.replace(char, replacement)
    return text.encode("latin-1", errors="ignore").decode("latin-1")


def build_pdf_bytes(selected_category: str, content: dict) -> bytes:
    if not FPDF_AVAILABLE:
        return b""
    try:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        pdf.set_font("Helvetica", "B", 16)
        pdf.set_text_color(0, 71, 171)
        pdf.cell(
            0,
            10,
            _pdf_safe("ZERO-TRUST FRAMEWORK APPLICATION"),
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
        )

        pdf.set_font("Helvetica", "B", 11)
        pdf.cell(
            0,
            7,
            _pdf_safe("Developed by Randy Singh | KalSnet (KNet) Consulting Group"),
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
        )

        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(80, 80, 80)
        ts = _pdf_safe(
            f"Category: {selected_category}   |   Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        )
        pdf.cell(0, 6, ts, new_x="LMARGIN", new_y="NEXT", align="C")

        pdf.set_draw_color(0, 71, 171)
        pdf.set_line_width(0.8)
        y = pdf.get_y() + 2
        pdf.line(10, y, 200, y)
        pdf.ln(6)

        for key, val in content.items():
            pdf.set_font("Helvetica", "B", 11)
            pdf.set_text_color(0, 71, 171)
            pdf.cell(0, 8, _pdf_safe(str(key)), new_x="LMARGIN", new_y="NEXT")

            pdf.set_font("Helvetica", "", 9)
            pdf.set_text_color(30, 30, 30)

            if isinstance(val, list):
                for item in val:
                    pdf.multi_cell(0, 6, _pdf_safe(f"  * {item}"))
            elif isinstance(val, dict):
                for k2, v2 in val.items():
                    pdf.set_font("Helvetica", "B", 9)
                    pdf.cell(
                        0,
                        6,
                        _pdf_safe(f"  {k2}:"),
                        new_x="LMARGIN",
                        new_y="NEXT",
                    )
                    pdf.set_font("Helvetica", "", 9)
                    if isinstance(v2, list):
                        for item in v2:
                            pdf.multi_cell(0, 5, _pdf_safe(f"    - {item}"))
                    else:
                        pdf.multi_cell(0, 6, _pdf_safe(f"    {v2}"))
            else:
                pdf.multi_cell(0, 6, _pdf_safe(f"  {val}"))

            pdf.ln(2)

        raw = pdf.output()
        if isinstance(raw, (bytes, bytearray)):
            return bytes(raw)
        return raw.encode("latin-1")

    except Exception as exc:
        try:
            fallback = FPDF()
            fallback.add_page()
            fallback.set_font("Helvetica", "", 11)
            fallback.multi_cell(0, 8, _pdf_safe(f"PDF error: {exc}"))
            raw = fallback.output()
            if isinstance(raw, (bytes, bytearray)):
                return bytes(raw)
            return raw.encode("latin-1")
        except Exception:
            return b""


def build_docx_bytes(selected_category: str, content: dict) -> bytes:
    if not DOCX_AVAILABLE:
        return b""
    try:
        doc = DocxDocument()

        t = doc.add_heading("ZERO-TRUST FRAMEWORK APPLICATION", 0)
        t.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in t.runs:
            run.font.color.rgb = RGBColor(0, 71, 171)

        sub = doc.add_paragraph(
            "Developed by Randy Singh | KalSnet (KNet) Consulting Group"
        )
        sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if sub.runs:
            sub.runs[0].bold = True
            sub.runs[0].font.color.rgb = RGBColor(0, 71, 171)

        ts_para = doc.add_paragraph(
            f"Category: {selected_category}   |   {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        )
        ts_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.add_paragraph()

        for key, val in content.items():
            h = doc.add_heading(str(key), level=2)
            for run in h.runs:
                run.font.color.rgb = RGBColor(0, 71, 171)

            if isinstance(val, list):
                for item in val:
                    doc.add_paragraph(str(item), style="List Bullet")
            elif isinstance(val, dict):
                for k2, v2 in val.items():
                    p = doc.add_paragraph()
                    run_label = p.add_run(f"{k2}: ")
                    run_label.bold = True
                    if isinstance(v2, list):
                        p.add_run(", ".join(str(x) for x in v2))
                    else:
                        p.add_run(str(v2))
            else:
                doc.add_paragraph(str(val))
            doc.add_paragraph()

        buf = io.BytesIO()
        doc.save(buf)
        return buf.getvalue()

    except Exception as exc:
        try:
            doc = DocxDocument()
            doc.add_paragraph(f"Word export error: {exc}")
            buf = io.BytesIO()
            doc.save(buf)
            return buf.getvalue()
        except Exception:
            return b""

# ══════════════════════════════════════════════════════════════════════════════
#  SIDEBAR — NAVIGATION & ABOUT (RADIO BUTTONS)
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("## ZTA Navigator")
    st.markdown("---")

    category = st.radio(
        "Select Framework Category",
        [
            "Overview & Architecture Diagram",
            "1. Functional Requirements",
            "2. Proposed Use Cases",
            "3. Architectural Requirements",
            "4. Evaluation Criteria",
            "Synthetic Data & Analytics",
        ],
        index=0,
        key="category_radio",
    )

    st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
    st.markdown("**About**")
    st.markdown("Randy Singh  \nComputer Scientist  \nDISA / BDE5  \nKalSnet (KNet) Consulting")
    st.markdown("`(301) 225-9535`")
    st.markdown("</div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  MAIN CONTENT RENDERING
# ══════════════════════════════════════════════════════════════════════════════
export_payload: dict = {}

# ─── Overview & Architecture Diagram ──────────────────────────────────────────
if category == "Overview & Architecture Diagram":
    st.markdown(
        '<div class="section-header">Zero-Trust Overview & Reference Architecture</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1.4, 1])

    with col1:
        st.markdown(
            """
**Zero-Trust Tenets**

- **Never trust, always verify** — every user, device, and workload is continuously validated.
- **Assume breach** — design for containment, micro-segmentation, and rapid detection.
- **Least privilege** — authorisation is granular, time-bound, and context-aware.
- **Data-centric security** — protection follows the data across on-prem and cloud.

**DISA / BDE5 Context**

This framework aligns with DISA/BDE5 ZTA Working Group guidance and DoD reference architectures,
providing a practical mapping from mission requirements to deployable technical controls.
"""
        )

    with col2:
        st.markdown(
            """
**Logical Architecture Layers**

- **Identity & Authentication** — IdP, MFA, PKI, credential providers  
- **Health & Compliance** — NAC, EDR, STIG posture, patching  
- **Authorization & Accounting** — PAM, RBAC, SIEM, UEBA  
- **Segmentation & Orchestration** — SDN, micro-segmentation, SOAR, IaC  
"""
        )

    st.markdown(
        '<div class="section-header">High-Level Architecture Diagram (Conceptual)</div>',
        unsafe_allow_html=True,
    )

    arch_fig = go.Figure()

    arch_fig.add_trace(
        go.Scatter(
            x=[1, 2, 3, 4],
            y=[4, 4, 4, 4],
            mode="markers+text",
            text=[
                "Identity Provider (Entra/Okta)",
                "MFA / PKI",
                "NAC / EDR",
                "PAM / JIT",
            ],
            textposition="bottom center",
            marker=dict(size=18, color="#0047AB"),
        )
    )

    arch_fig.add_trace(
        go.Scatter(
            x=[1, 2, 3],
            y=[2, 2, 2],
            mode="markers+text",
            text=["SDN / Micro-Segmentation", "Policy Engine", "SIEM / UEBA"],
            textposition="bottom center",
            marker=dict(size=18, color="#f0a500"),
        )
    )

    arch_fig.update_layout(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        showlegend=False,
        height=360,
        margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor="#f4f7fc",
        paper_bgcolor="#f4f7fc",
    )

    st.plotly_chart(arch_fig, use_container_width=True)

    export_payload = {
        "Overview": [
            "Zero-Trust Overview & Reference Architecture",
            "Identity, Health & Compliance, Authorization, Accounting, Segmentation, and Orchestration pillars.",
        ]
    }

# ─── Functional Requirements ──────────────────────────────────────────────────
elif category == "1. Functional Requirements":
    st.markdown(
        '<div class="section-header">Zero-Trust Functional Requirements (Pillars)</div>',
        unsafe_allow_html=True,
    )

    for pillar, details in FUNCTIONAL_REQUIREMENTS.items():
        st.markdown(f"### {pillar}")

        st.markdown(
            f'<div class="req-card"><b>Requirement:</b> {details["requirement"]}</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="sol-card"><b>Solution Pattern:</b> {details["solution"]}</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="rec-card"><b>Recommendation:</b> {details["recommendation"]}</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="req-card"><b>Example:</b> {details["example"]}</div>',
            unsafe_allow_html=True,
        )

    export_payload = FUNCTIONAL_REQUIREMENTS

# ─── Proposed Use Cases ───────────────────────────────────────────────────────
elif category == "2. Proposed Use Cases":
    st.markdown(
        '<div class="section-header">Proposed Zero-Trust Use Cases</div>',
        unsafe_allow_html=True,
    )

    for uc_name, steps in USE_CASES.items():
        st.markdown(f"### {uc_name}")
        for step in steps:
            st.markdown(f"- {step}")
        st.markdown("")

    export_payload = USE_CASES

# ─── Architectural Requirements ───────────────────────────────────────────────
elif category == "3. Architectural Requirements":
    st.markdown(
        '<div class="section-header">Architectural Requirements by Pillar</div>',
        unsafe_allow_html=True,
    )

    for req_group, items in ARCHITECTURAL_REQUIREMENTS.items():
        st.markdown(f"### {req_group}")
        for item in items:
            st.markdown(f"- {item}")
        st.markdown("")

    export_payload = ARCHITECTURAL_REQUIREMENTS

# ─── Evaluation Criteria ──────────────────────────────────────────────────────
elif category == "4. Evaluation Criteria":
    st.markdown(
        '<div class="section-header">Evaluation Criteria for Zero-Trust Solutions</div>',
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    keys = list(EVALUATION_CRITERIA.keys())

    for i, key in enumerate(keys):
        with cols[i]:
            crit = EVALUATION_CRITERIA[key]
            st.markdown(f"### {key}")
            st.markdown(f"**Definition**: {crit['definition']}")
            st.markdown("**Metrics:**")
            for m in crit["metrics"]:
                st.markdown(f"- {m}")
            st.markdown(f"**Target:** {crit['target']}")
            st.markdown(f"**Recommendation:** {crit['recommendation']}")

    export_payload = EVALUATION_CRITERIA

# ─── Synthetic Data & Analytics ───────────────────────────────────────────────
elif category == "Synthetic Data & Analytics":
    st.markdown(
        '<div class="section-header">Synthetic ZTA Telemetry & Analytics</div>',
        unsafe_allow_html=True,
    )

    n_records = st.slider("Number of synthetic records", 200, 2000, 800, step=200)
    df = generate_synthetic_data(n_records)

    top_row = st.columns(4)
    with top_row[0]:
        compliant_pct = (df["Compliance_Status"] == "Compliant").mean() * 100
        st.metric("Compliant Endpoints", f"{compliant_pct:.1f} %")
    with top_row[1]:
        avg_stig = df["STIG_Score"].mean()
        st.metric("Average STIG Score", f"{avg_stig:.1f}")
    with top_row[2]:
        mfa_pct = df["MFA_Enabled"].mean() * 100
        st.metric("MFA Coverage", f"{mfa_pct:.1f} %")
    with top_row[3]:
        incidents = df["Incident_Flagged"].sum()
        st.metric("Incidents Flagged", str(incidents))

    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        status_counts = df["Compliance_Status"].value_counts().reset_index()
        status_counts.columns = ["Compliance_Status", "Count"]
        fig_status = px.bar(
            status_counts,
            x="Compliance_Status",
            y="Count",
            color="Compliance_Status",
            title="Compliance Status Distribution",
            color_discrete_sequence=px.colors.qualitative.Set2,
        )
        fig_status.update_layout(
            plot_bgcolor="#f4f7fc",
            paper_bgcolor="#f4f7fc",
            margin=dict(l=10, r=10, t=40, b=10),
        )
        st.plotly_chart(fig_status, use_container_width=True)

    with col_chart2:
        pillar_scores = df.groupby("Pillar")["STIG_Score"].mean().reset_index()
        fig_pillar = px.line(
            pillar_scores,
            x="Pillar",
            y="STIG_Score",
            markers=True,
            title="Average STIG Score by ZTA Pillar",
            color_discrete_sequence=["#0047AB"],
        )
        fig_pillar.update_layout(
            plot_bgcolor="#f4f7fc",
            paper_bgcolor="#f4f7fc",
            margin=dict(l=10, r=10, t=40, b=10),
        )
        st.plotly_chart(fig_pillar, use_container_width=True)

    st.markdown("### Raw Synthetic Dataset Preview")
    st.dataframe(df.head(20), use_container_width=True)

    export_payload = {
        "summary": {
            "records": n_records,
            "compliant_pct": compliant_pct,
            "avg_stig_score": avg_stig,
            "mfa_coverage_pct": mfa_pct,
            "incidents_flagged": int(incidents),
        },
        "sample": df.head(50).to_dict(orient="records"),
    }

# ══════════════════════════════════════════════════════════════════════════════
#  SIDEBAR — EXPORT THIS VIEW (ONLY)
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
    st.markdown("**Export This View**")

    # Text
    text_report = build_text_report(category, export_payload)
    st.download_button(
        "Download Text (.txt)",
        data=text_report,
        file_name=f"zero_trust_{category.replace(' ', '_').lower()}.txt",
        mime="text/plain",
        key="dl_txt",
    )

    # JSON
    json_report = build_json_report(category, export_payload)
    st.download_button(
        "Download JSON (.json)",
        data=json_report,
        file_name=f"zero_trust_{category.replace(' ', '_').lower()}.json",
        mime="application/json",
        key="dl_json",
    )

    # PDF
    pdf_bytes = build_pdf_bytes(category, export_payload)
    if pdf_bytes:
        st.download_button(
            "Download PDF (.pdf)",
            data=pdf_bytes,
            file_name=f"zero_trust_{category.replace(' ', '_').lower()}.pdf",
            mime="application/pdf",
            key="dl_pdf",
        )
    else:
        st.caption("PDF export not available — install `fpdf2` in the environment.")

    # Word
    docx_bytes = build_docx_bytes(category, export_payload)
    if docx_bytes:
        st.download_button(
            "Download Word (.docx)",
            data=docx_bytes,
            file_name=f"zero_trust_{category.replace(' ', '_').lower()}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            key="dl_docx",
        )
    else:
        st.caption("Word export not available — install `python-docx` in the environment.")

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown(
        '<div class="sidebar-footer">Zero-Trust Framework | DISA / BDE5 | KalSnet (KNet) Consulting</div>',
        unsafe_allow_html=True,
    )

# ══════════════════════════════════════════════════════════════════════════════
#  FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    """
<div style="text-align:center;color:#888;font-size:0.8rem;margin-top:20px;">
Zero-Trust Framework Application | Developed by Randy Singh | KalSnet (KNet) Consulting Group |
DISA / BDE5 Technology Innovation Team | {year}
</div>
""".format(year=datetime.now().year),
    unsafe_allow_html=True,
)
