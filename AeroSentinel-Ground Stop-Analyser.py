


# AeroSentinel — Ground Stop Cyber-Attack Detection Console
# Developed by Randy Singh from Kalsnet (KNet) Consulting Group

# Purpose

# When a nationwide ground stop is declared, investigators must quickly answer:
#"Is this a cyber attack, or a technical / operational failure?"

# This console ingests aviation-system telemetry and security event logs,
# runs statistical + machine-learning anomaly detection, scores cyber-attack
# indicators (mapped to MITRE ATT&CK), and produces an evidence-backed verdict
# exportable to PDF, Word, TXT and CSV.

import io
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from sklearn.ensemble import IsolationForest

APP_NAME = "AeroSentinel"
APP_TAGLINE = "Ground Stop Cyber-Attack Detection Console"
DEVELOPER = "Developed by Randy Singh from Kalsnet (KNet) Consulting Group"

SYSTEMS = ["NOTAM", "ERAM", "TFMS", "SWIM", "ATCSCC-Comms"]
METRICS = ["inbound_mbps", "conn_count", "auth_fail", "auth_ok",
           "cpu_pct", "error_rate", "latency_ms", "integrity_fail"]
TELEMETRY_COLS = ["timestamp", "system"] + METRICS
EVENT_COLS = ["timestamp", "system", "event_type", "src_ip", "country",
              "user", "severity", "detail"]
TRUSTED_COUNTRIES = {"US"}

# ---------------------------------------------------------------------------
# Page setup & styling
# ---------------------------------------------------------------------------
st.set_page_config(page_title=f"{APP_NAME} | KNet", page_icon="🛡️", layout="wide")

st.markdown(
    """
    <style>
    .block-container {padding-top: 1.2rem;}
    .hero {
        background: linear-gradient(120deg, #0b1f3a 0%, #12355b 55%, #1d4e89 100%);
        border-radius: 14px; padding: 22px 28px; color: #fff; margin-bottom: 14px;
        border-left: 6px solid #f2a541;
    }
    .hero h1 {margin: 0; font-size: 2.1rem; letter-spacing: .5px; color:#fff;}
    .hero .tag {font-size: 1.05rem; opacity: .9; margin-top: 2px;}
    .hero .dev {font-size: .92rem; margin-top: 10px; color: #f2c879; font-style: italic;}
    .verdict {border-radius: 12px; padding: 16px 20px; color: #fff; font-weight: 600;}
    .v-high {background: #b42318;} .v-mod {background: #c4661f;} .v-low {background: #1e7b4f;}
    .ind {border:1px solid rgba(128,128,128,.25); border-radius:10px; padding:10px 14px; margin-bottom:8px;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="hero">
      <h1>🛡️ {APP_NAME}</h1>
      <div class="tag">{APP_TAGLINE} — is the ground stop a cyber attack or a system failure?</div>
      <div class="dev">{DEVELOPER}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# User guide — fields, formulas, glossary, real-world use (shown at the top)
# ---------------------------------------------------------------------------
GUIDE_FIELDS = """
#### System telemetry file (one row per system per minute)
| Field | Meaning | Unit / values | Why it matters |
|---|---|---|---|
| `timestamp` | Minute the measurement was taken | date-time | Lines up all systems on one clock |
| `system` | Aviation system measured | NOTAM, ERAM, TFMS, SWIM, ATCSCC-Comms | Shows which system failed first |
| `inbound_mbps` | Incoming network traffic | megabits per second | A sudden flood suggests a DDoS attack |
| `conn_count` | Open network connections | count | Floods and scans open many connections |
| `auth_fail` | Failed logins in that minute | count | Bursts suggest password guessing |
| `auth_ok` | Successful logins in that minute | count | Unusual success after failures = possible break-in |
| `cpu_pct` | Processor load | 0–100 % | Overload from attack traffic or a runaway fault |
| `error_rate` | Requests that returned errors | % | Rises in both attacks and ordinary failures |
| `latency_ms` | Response time | milliseconds | Slowdown is the first symptom users notice |
| `integrity_fail` | Failed data-integrity checks (hash / checksum mismatches) | count | Data changed or corrupted — tampering or a bad update |

#### Security event log (one row per security event)
| Field | Meaning | Values / examples |
|---|---|---|
| `timestamp` | When the event happened | date-time |
| `system` | System the event came from | NOTAM, SWIM, … |
| `event_type` | What happened | `login_failure`, `login_success`, `firewall_block`, `priv_escalation`, `new_admin_account`, `config_change`, `file_deleted`, `malware_alert` |
| `src_ip` | Network address the action came from | e.g. 10.20.3.8 (internal), 185.220.101.44 (external) |
| `country` | Country of the source address (geolocation) | two-letter code, e.g. US, RU |
| `user` | Account involved | e.g. admin_notam |
| `severity` | Importance set by the logging tool | low, medium, high, critical |
| `detail` | Free-text description; include the change ticket (e.g. `CHG-48812`) for approved work | text |

#### Sidebar settings
| Setting | What it controls | Default |
|---|---|---|
| Robust z-score threshold | How far from normal a value must be to count as abnormal | 4.0 |
| Sustained minutes to fire | How many consecutive abnormal minutes are needed before an indicator fires | 5 |
| ML contamination | Share of data points the machine-learning model is told to flag as anomalies | 0.05 (5 %) |
| Systems | Which systems are included in the analysis | all |

#### Dashboard outputs
| Output | Meaning |
|---|---|
| Cyber-attack likelihood (0–100) | Evidence score — see *Formulas* |
| Verdict | HIGH (≥ 60), MODERATE (30–59), LOW (< 30) |
| Indicators fired | How many of the 8 attack indicators were triggered |
| ML anomalies | Data points the Isolation Forest flagged as unusual |
| Security / critical events | Rows in the event log, and those marked critical |
| Non-cyber signals | Evidence pointing to an ordinary failure; each one lowers the score |
"""

GUIDE_FORMULAS = [
    ('md', '#### 1. Baseline (what "normal" looks like)\nThe first **40 %** of the time window, for each system separately, is treated as normal operation.\n\n#### 2. Robust z-score (how unusual a value is)'),
    ('latex', 'z = \\frac{x - \\text{median}_{\\text{baseline}}}{1.4826 \\times \\text{MAD}_{\\text{baseline}}}\n\\qquad \\text{MAD} = \\text{median}\\big(|x_i - \\text{median}|\\big)'),
    ('md', '- *x* is the current value; the median and **MAD** (median absolute deviation) come from the baseline.\n- 1.4826 scales MAD so it is comparable to a standard deviation for normally distributed data.\n- Median/MAD are used instead of mean/std-dev because one big spike cannot distort them.\n- Example: baseline median 120 Mbps, MAD 7 → 1.4826 × 7 ≈ 10.4. A reading of 1,200 Mbps gives z ≈ (1200 − 120) / 10.4 ≈ **104** — far above the 4.0 threshold.\n\n#### 3. Sustained run'),
    ('latex', '\\text{run} = \\text{longest streak of consecutive minutes where } z > \\text{threshold}'),
    ('md', 'An indicator based on telemetry fires only if the run is ≥ *Sustained minutes* (≥ 3 minutes for the login-failure indicator). This filters out one-off blips.\n\n#### 4. Isolation Forest (machine learning)\nAn unsupervised model that builds 200 random trees per system over all 8 metrics together. Unusual points get separated from the rest in fewer splits.'),
    ('latex', 's(x) = 2^{-\\,E[h(x)]\\,/\\,c(n)}'),
    ('md', '- *h(x)*: number of splits needed to isolate the point; *E[h(x)]* is its average over all trees.\n- *c(n)*: average path length expected for *n* points (normalising constant).\n- *s* near 1 = very anomalous; well below 0.5 = normal. The app shows this as **ML score**.\n- **Contamination** sets the cut-off: the top *contamination* share of scores is flagged as anomalies.\n\n#### 5. Attack indicators and weights\n| # | Indicator | Fires when | MITRE ATT&CK | Weight |\n|---|---|---|---|---|\n| 1 | Volumetric traffic surge | `inbound_mbps` z > threshold for ≥ sustained minutes on any system | T1498 Network DoS | 15 |\n| 2 | Login-failure burst | `auth_fail` z > threshold for ≥ 3 consecutive minutes | T1110 Brute Force | 15 |\n| 3 | Success after failures | Same IP has ≥ 10 `login_failure` **and** ≥ 1 `login_success` | T1078 Valid Accounts | 15 |\n| 4 | Untrusted geography | Any login attempt from a country other than US | TA0001 Initial Access | 10 |\n| 5 | Privilege escalation / rogue admin | Any `priv_escalation` or `new_admin_account` event | T1068 / T1136 | 15 |\n| 6 | Tampering outside change control | `integrity_fail` > 0 **and** a `file_deleted`/`config_change` with no `CHG-` ticket or "approved" in `detail` | T1565 / T1485 | 15 |\n| 7 | Malware / EDR alert | Any `malware_alert` event | T1485 / TA0002 | 10 |\n| 8 | Coordinated anomalies | ≥ 3 systems ML-anomalous in the same minute, for ≥ sustained minutes | Campaign indicator | 5 |\n| | **Maximum** | | | **100** |\n\n#### 6. Non-cyber (benign) signals\nEach one found lowers the score by 10:\n- Approved maintenance events (`detail` contains `CHG-`, "approved" or "maintenance").\n- Error-rate failure confined to a **single** system with **no** traffic surge.\n- **No** login-failure burst, **no** success-after-failure and **no** foreign logins.\n\n#### 7. Final score and verdict'),
    ('latex', '\\text{Score} = \\max\\Big(0,\\; \\min\\big(100,\\ \\textstyle\\sum \\text{weights of fired indicators}\\big) - 10 \\times \\text{benign signals}\\Big)'),
    ('md', "| Score | Verdict |\n|---|---|\n| 60–100 | **HIGH** — likely cyber attack |\n| 30–59 | **MODERATE** — possible cyber involvement, investigate |\n| 0–29 | **LOW** — likely technical / operational failure |\n\n*The weights are expert-judgement starting values, not statistically calibrated. Tune them on your organisation's past incidents.*"),
]

GUIDE_GLOSSARY = """
| Term | Explanation |
|---|---|
| **Ground stop** | FAA order holding departures on the ground, for one airport, an airline or the whole country |
| **FAA** | Federal Aviation Administration — US civil aviation regulator and air-traffic operator |
| **ATCSCC** | Air Traffic Control System Command Center — the FAA centre that issues ground stops |
| **NOTAM** | Notice to Air Missions — system sending pilots safety notices (closed runways, hazards). Its failure caused the Jan 2023 nationwide ground stop |
| **ERAM** | En Route Automation Modernization — computers controlling high-altitude traffic |
| **TFMS** | Traffic Flow Management System — plans and balances traffic across the country |
| **SWIM** | System Wide Information Management — the FAA's data-sharing network between systems and airlines |
| **ADS-B** | Aircraft position broadcasts; can be spoofed or jammed |
| **Cyber attack** | Deliberate attempt to disrupt, damage or gain unauthorised access to systems or data |
| **DDoS** | Distributed Denial of Service — flooding a system with traffic from many machines until it fails |
| **Brute force / password spray** | Guessing passwords repeatedly; spraying tries a few common passwords across many accounts |
| **Credential compromise** | Attacker logs in with a real, stolen or guessed account |
| **Privilege escalation** | Gaining higher (admin/root) rights than the account should have |
| **Rogue admin account** | New administrator account created by an attacker for persistence |
| **Data tampering / destruction** | Altering or deleting data; a **wiper** is malware built to erase data |
| **Integrity check** | Comparing a file's hash or checksum with a known-good value to detect changes |
| **Change control / change window** | Formal approval (ticket such as CHG-48812) and agreed time for maintenance |
| **EDR** | Endpoint Detection & Response — security software on servers and PCs that raises malware alerts |
| **Firewall block** | Network traffic the firewall refused |
| **IP address / geolocation** | Network address of a device; geolocation estimates its country (can be hidden by VPNs) |
| **SYN flood** | Common DDoS technique that opens many half-finished connections |
| **MITRE ATT&CK** | Public catalogue of attacker techniques; codes like **T1498** identify a technique, **TA0001** a tactic (goal) |
| **IOC** | Indicator of Compromise — evidence (IP, file hash, account) suggesting a breach |
| **Anomaly** | A value or pattern that differs strongly from normal |
| **Baseline** | The normal period used for comparison |
| **Median / MAD** | Middle value / typical distance from the middle — outlier-resistant statistics |
| **z-score** | How many "typical deviations" a value is from normal |
| **Isolation Forest** | Machine-learning method that finds anomalies by how easily points are isolated by random splits |
| **Contamination** | Expected share of anomalies told to the ML model |
| **False positive / negative** | Alarm raised with no attack / attack missed with no alarm |
| **SOC** | Security Operations Center — the team monitoring and responding to security events |
| **SIEM** | Security Information & Event Management — central log platform (e.g. Splunk, Microsoft Sentinel, Elastic) |
| **CISA** | Cybersecurity and Infrastructure Security Agency — US federal cyber-defence agency |
| **Chain of custody** | Documented handling of evidence so it remains usable for investigation or prosecution |
| **Attribution** | Identifying who carried out an attack — requires far more than this tool provides |
"""

GUIDE_REAL_WORLD = """
#### What this application can do in a real incident
- **Fast triage:** load exported telemetry and security logs and, in minutes, see whether the evidence leans toward *attack* or *failure*, and why.
- **Correlation:** put network, login, integrity and malware evidence from several systems on one timeline, so investigators can see what happened first.
- **Structured investigation:** the Playbook tab walks analysts through the standard probes, and the reports record the evidence, checklist status and notes.
- **Communication:** PDF/Word reports with MITRE ATT&CK mapping give leadership, FAA and CISA a common, evidence-based summary.
- **Repeatable analysis:** re-upload fresh exports as the incident unfolds to see whether the score is rising or falling.

#### What it does NOT do (as built)
- **Not real-time.** It analyses files you upload (batch). It does not connect to live feeds or stream data by itself.
- **Does not stop or block attacks.** It is a decision-support tool, not a firewall, EDR or intrusion-prevention system.
- **Does not prove or attribute an attack.** A HIGH score means "evidence pattern consistent with an attack". Confirmation and attribution need forensic investigation by the SOC, FAA and law enforcement.
- **No access to FAA data.** Real NOTAM/ERAM/TFMS telemetry and security logs are not public; the app only works with data your organisation is authorised to hold.
- **Simple rules can be evaded.** A careful attacker using valid credentials from a US address, during a change window, may trigger few indicators. Insider actions look similar to maintenance.
- **Needs tuning.** Thresholds and weights are starting values. Calibrate them on your own normal data and past incidents to control false positives and negatives.
- **Demo data is synthetic.** Results on the demo scenarios show how the tool works, not how it performs on real attacks.

#### Making it real-time (next steps for a production deployment)
1. **Connect to live sources:** pull data every 1–5 minutes from your SIEM (Splunk, Sentinel, Elastic), NetFlow collectors, EDR and system-health monitoring, via their APIs or a message bus such as Kafka, instead of CSV upload.
2. **Auto-refresh:** re-run detection on a timer (e.g. Streamlit `st.fragment(run_every=60)`) over a rolling window.
3. **Alerting:** push HIGH verdicts to the SOC through email, Teams/Slack or PagerDuty.
4. **Threat intelligence:** check source IPs and file hashes against CISA advisories and threat-intel feeds.
5. **Security & governance:** run inside the protected network with sign-in, role-based access and audit logging, and validate against past incidents before relying on it.
"""

with st.expander("📘 Guide — fields, formulas & glossary  |  🌍 Real-world use & limits", expanded=False):
    g1, g2, g3, g4 = st.tabs(["🗂️ Fields", "🧮 Formulas", "📖 Glossary", "🌍 Real-world use & limits"])
    with g1:
        st.markdown(GUIDE_FIELDS)
    with g2:
        for kind, content in GUIDE_FORMULAS:
            if kind == "latex":
                st.latex(content)
            else:
                st.markdown(content)
    with g3:
        st.markdown(GUIDE_GLOSSARY)
    with g4:
        st.markdown(GUIDE_REAL_WORLD)

# ---------------------------------------------------------------------------
# Synthetic data generation
# ---------------------------------------------------------------------------
SCENARIOS = {
    "Cyber attack (DDoS + credential compromise + data tampering)": "cyber",
    "Non-cyber failure (corrupted database after maintenance)": "failure",
    "Normal operations (baseline)": "normal",
}


@st.cache_data(show_spinner=False)
def make_synthetic(scenario: str, hours: int = 6, seed: int = 7):
    rng = np.random.default_rng(seed)
    start = datetime(2026, 11, 13, 0, 0)
    ts = pd.date_range(start, periods=hours * 60, freq="min")
    n = len(ts)
    incident = int(n * 0.55)  # incident begins ~55% into the window
    rows = []
    base = {
        "NOTAM": (120, 900), "ERAM": (300, 1500), "TFMS": (200, 1100),
        "SWIM": (450, 2200), "ATCSCC-Comms": (80, 400),
    }
    for sys_name in SYSTEMS:
        mb, cc = base[sys_name]
        diurnal = 1 + 0.15 * np.sin(np.linspace(0, np.pi, n))
        d = pd.DataFrame({
            "timestamp": ts,
            "system": sys_name,
            "inbound_mbps": rng.normal(mb, mb * 0.06, n) * diurnal,
            "conn_count": rng.normal(cc, cc * 0.05, n) * diurnal,
            "auth_fail": rng.poisson(2, n).astype(float),
            "auth_ok": rng.poisson(25, n).astype(float),
            "cpu_pct": np.clip(rng.normal(38, 5, n), 0, 100),
            "error_rate": np.clip(rng.normal(0.4, 0.15, n), 0, None),
            "latency_ms": np.clip(rng.normal(45, 6, n), 1, None),
            "integrity_fail": np.zeros(n),
        })
        sl = slice(incident, n)
        k = n - incident
        if scenario == "cyber":
            if sys_name in ("NOTAM", "SWIM", "ERAM"):
                d.loc[d.index[sl], "inbound_mbps"] *= rng.uniform(6, 12, k)
                d.loc[d.index[sl], "conn_count"] *= rng.uniform(5, 9, k)
                d.loc[d.index[sl], "cpu_pct"] = np.clip(rng.normal(93, 4, k), 0, 100)
                d.loc[d.index[sl], "latency_ms"] = rng.normal(900, 150, k)
                d.loc[d.index[sl], "error_rate"] = rng.normal(18, 4, k)
            pre = slice(incident - 40, incident)
            d.loc[d.index[pre], "auth_fail"] = rng.poisson(60, 40).astype(float)
            if sys_name == "NOTAM":
                d.loc[d.index[incident + 15:n], "integrity_fail"] = rng.poisson(9, k - 15).astype(float)
        elif scenario == "failure":
            if sys_name == "NOTAM":
                d.loc[d.index[sl], "error_rate"] = rng.normal(35, 6, k)
                d.loc[d.index[sl], "latency_ms"] = rng.normal(2500, 300, k)
                d.loc[d.index[sl], "inbound_mbps"] *= 0.35
                d.loc[d.index[sl], "conn_count"] *= 0.4
                d.loc[d.index[sl], "integrity_fail"] = rng.poisson(12, k).astype(float)
        rows.append(d)
    tel = pd.concat(rows, ignore_index=True)
    tel[METRICS] = tel[METRICS].clip(lower=0).round(2)

    # --- security event log ---
    ev = []
    def add(t, s, et, ip, c, u, sev, det):
        ev.append([t, s, et, ip, c, u, sev, det])

    for _ in range(140):  # routine noise
        t = ts[rng.integers(0, n)]
        s = rng.choice(SYSTEMS)
        add(t, s, rng.choice(["login_success", "login_failure", "firewall_block"], p=[.7, .2, .1]),
            f"10.20.{rng.integers(1, 40)}.{rng.integers(2, 250)}", "US",
            rng.choice(["ops_jlee", "ops_mkhan", "svc_backup", "noc_rpatel"]), "low", "routine")

    t0 = ts[incident]
    if scenario == "cyber":
        bad_ips = ["185.220.101.44", "45.155.205.233", "103.75.190.12"]
        for i in range(220):
            add(t0 - timedelta(minutes=int(rng.integers(5, 40))), "NOTAM", "login_failure",
                rng.choice(bad_ips), rng.choice(["RU", "NL", "CN"]), "admin_notam", "medium",
                "password spray")
        add(t0 - timedelta(minutes=4), "NOTAM", "login_success", bad_ips[0], "RU",
            "admin_notam", "high", "success after repeated failures")
        add(t0 - timedelta(minutes=3), "NOTAM", "priv_escalation", bad_ips[0], "RU",
            "admin_notam", "critical", "sudo to root")
        add(t0 - timedelta(minutes=2), "NOTAM", "new_admin_account", bad_ips[0], "RU",
            "sys_maint2", "critical", "account created outside change window")
        add(t0 + timedelta(minutes=10), "NOTAM", "config_change", bad_ips[0], "RU",
            "sys_maint2", "critical", "db replication target modified")
        add(t0 + timedelta(minutes=14), "NOTAM", "file_deleted", bad_ips[0], "RU",
            "sys_maint2", "critical", "notam_master.db deleted")
        add(t0 + timedelta(minutes=20), "SWIM", "malware_alert", "10.20.5.17", "US",
            "svc_swim", "critical", "EDR: wiper-like behaviour")
        for i in range(60):
            add(t0 + timedelta(minutes=int(rng.integers(0, 120))), rng.choice(["NOTAM", "SWIM", "ERAM"]),
                "firewall_block", f"{rng.integers(1, 223)}.{rng.integers(0, 255)}.{rng.integers(0, 255)}.{rng.integers(1, 254)}",
                rng.choice(["RU", "CN", "BR", "VN", "NL"]), "-", "high", "SYN flood")
    elif scenario == "failure":
        add(t0 - timedelta(minutes=20), "NOTAM", "config_change", "10.20.3.8", "US",
            "contractor_dbadmin", "medium", "scheduled maintenance: DB sync (CHG-48812)")
        add(t0 - timedelta(minutes=5), "NOTAM", "file_deleted", "10.20.3.8", "US",
            "contractor_dbadmin", "medium", "files removed during sync (approved change window)")
    evdf = pd.DataFrame(ev, columns=EVENT_COLS).sort_values("timestamp").reset_index(drop=True)
    return tel, evdf


# ---------------------------------------------------------------------------
# Detection engine
# ---------------------------------------------------------------------------
def robust_z(s: pd.Series, baseline_frac: float = 0.4) -> pd.Series:
    b = s.iloc[: max(10, int(len(s) * baseline_frac))]
    med = b.median()
    mad = (b - med).abs().median() * 1.4826
    if mad == 0 or np.isnan(mad):
        mad = b.std() if b.std() > 0 else 1.0
    return (s - med) / mad


def compute_zscores(tel: pd.DataFrame) -> pd.DataFrame:
    out = []
    for s, g in tel.sort_values("timestamp").groupby("system"):
        g = g.copy()
        for m in METRICS:
            g[f"z_{m}"] = robust_z(g[m])
        out.append(g)
    return pd.concat(out, ignore_index=True)


def run_isolation_forest(tel: pd.DataFrame, contamination: float) -> pd.DataFrame:
    tel = tel.copy()
    tel["ml_score"] = 0.0
    tel["ml_anomaly"] = False
    for s, g in tel.groupby("system"):
        X = g[METRICS].fillna(0).values
        if len(X) < 20:
            continue
        model = IsolationForest(n_estimators=200, contamination=contamination, random_state=42)
        model.fit(X)
        tel.loc[g.index, "ml_score"] = -model.score_samples(X)
        tel.loc[g.index, "ml_anomaly"] = model.predict(X) == -1
    return tel


def longest_run(mask: pd.Series) -> int:
    best = cur = 0
    for v in mask:
        cur = cur + 1 if v else 0
        best = max(best, cur)
    return best


def assess(tel_z: pd.DataFrame, ev: pd.DataFrame, z_thr: float, sustain: int):
    """Return (score, verdict, indicators list, non-cyber signals list)."""
    ind = []

    def add(name, technique, weight, fired, evidence):
        ind.append({"indicator": name, "mitre": technique, "weight": weight,
                    "fired": bool(fired), "evidence": evidence})

    # 1. Volumetric surge (DDoS)
    surge = {s: longest_run(g["z_inbound_mbps"] > z_thr) for s, g in tel_z.groupby("system")}
    hit = {s: r for s, r in surge.items() if r >= sustain}
    add("Volumetric traffic surge (possible DDoS)", "T1498 Network DoS", 15, hit,
        f"Sustained inbound spikes on {', '.join(hit)} (max {max(surge.values())} min)" if hit else "No sustained traffic surge")

    # 2. Auth failure burst
    af = {s: longest_run(g["z_auth_fail"] > z_thr) for s, g in tel_z.groupby("system")}
    hit_af = {s: r for s, r in af.items() if r >= 3}
    add("Authentication-failure burst (brute force / spray)", "T1110 Brute Force", 15, hit_af,
        f"Bursts on {', '.join(hit_af)}" if hit_af else "Auth failures within baseline")

    e = ev.copy()
    e["timestamp"] = pd.to_datetime(e["timestamp"])
    # 3. Success after failures from same IP
    fails = e[e.event_type == "login_failure"].groupby("src_ip").size()
    succ_ips = set(e[e.event_type == "login_success"].src_ip)
    sus = [ip for ip in succ_ips if fails.get(ip, 0) >= 10]
    add("Login success after repeated failures (credential compromise)", "T1078 Valid Accounts", 15, sus,
        f"IPs: {', '.join(sus)}" if sus else "None observed")

    # 4. Untrusted geography
    foreign = e[(~e.country.isin(TRUSTED_COUNTRIES)) & e.event_type.isin(["login_success", "login_failure"])]
    add("Access attempts from untrusted geographies", "TA0001 Initial Access", 10, len(foreign) > 0,
        f"{len(foreign)} attempts from {', '.join(sorted(foreign.country.unique()))}" if len(foreign) else "None")

    # 5. Privilege escalation / rogue accounts
    pe = e[e.event_type.isin(["priv_escalation", "new_admin_account"])]
    add("Privilege escalation / rogue admin account", "T1068 / T1136", 15, len(pe) > 0,
        f"{len(pe)} events; users: {', '.join(pe.user.unique())}" if len(pe) else "None")

    # 6. Data integrity failures
    integ = tel_z.groupby("system")["integrity_fail"].sum()
    integ_hit = integ[integ > 0]
    destr = e[e.event_type.isin(["file_deleted", "config_change"])]
    unapproved = destr[~destr.detail.str.contains("CHG-|approved", case=False, na=False)]
    add("Data tampering / destruction outside change control", "T1565 / T1485", 15,
        len(integ_hit) > 0 and len(unapproved) > 0,
        f"Integrity failures on {', '.join(integ_hit.index)}; {len(unapproved)} unapproved destructive changes"
        if len(integ_hit) else "No integrity failures")

    # 7. Malware alerts
    mal = e[e.event_type == "malware_alert"]
    add("Malware / EDR alerts", "T1485 Wiper / TA0002", 10, len(mal) > 0,
        f"{len(mal)} alert(s): {'; '.join(mal.detail)}" if len(mal) else "None")

    # 8. Coordinated multi-system anomaly
    multi = tel_z[tel_z.ml_anomaly].groupby("timestamp").system.nunique()
    coord = int((multi >= 3).sum())
    add("Coordinated anomalies across ≥3 systems", "Campaign indicator", 5, coord >= sustain,
        f"{coord} minutes with ≥3 systems anomalous simultaneously")

    score = min(100, sum(i["weight"] for i in ind if i["fired"]))

    # Non-cyber (benign root cause) signals
    benign = []
    approved = e[e.detail.str.contains("CHG-|approved|maintenance", case=False, na=False)]
    if len(approved):
        benign.append(f"{len(approved)} change-managed maintenance events precede the incident (e.g. '{approved.detail.iloc[0]}')")
    err_sys = [s for s, g in tel_z.groupby("system") if longest_run(g["z_error_rate"] > z_thr) >= sustain]
    if len(err_sys) == 1 and not hit:
        benign.append(f"Error/latency failure isolated to a single system ({err_sys[0]}) with no traffic surge")
    if not hit_af and not sus and len(foreign) == 0:
        benign.append("No authentication anomalies or foreign access — consistent with internal fault")

    score = max(0, score - 10 * len(benign))
    if score >= 60:
        verdict = "HIGH — Likely cyber attack"
    elif score >= 30:
        verdict = "MODERATE — Possible cyber involvement, investigate"
    else:
        verdict = "LOW — Likely technical / operational failure"
    return score, verdict, ind, benign


# ---------------------------------------------------------------------------
# Report builders
# ---------------------------------------------------------------------------
def report_text(meta, score, verdict, ind, benign, anomalies, notes, checklist):
    L = [f"{APP_NAME} — {APP_TAGLINE}", DEVELOPER, "=" * 72,
         f"Generated: {datetime.now():%Y-%m-%d %H:%M:%S}",
         f"Data source: {meta['source']}", f"Window: {meta['start']} to {meta['end']}",
         f"Systems analysed: {meta['systems']}", "",
         f"CYBER-ATTACK LIKELIHOOD SCORE: {score}/100", f"VERDICT: {verdict}", "",
         "INDICATORS", "-" * 72]
    for i in ind:
        L.append(f"[{'FIRED' if i['fired'] else ' ok  '}] {i['indicator']} ({i['mitre']}, w={i['weight']})")
        L.append(f"        {i['evidence']}")
    L += ["", "NON-CYBER / BENIGN SIGNALS", "-" * 72]
    L += [f" - {b}" for b in benign] or [" - none"]
    L += ["", f"ANOMALOUS DATA POINTS: {len(anomalies)} (top 15 by ML score)", "-" * 72]
    for _, r in anomalies.head(15).iterrows():
        L.append(f" {r.timestamp}  {r.system:<13} ml={r.ml_score:.3f}  mbps={r.inbound_mbps:.0f}  "
                 f"authfail={r.auth_fail:.0f}  err={r.error_rate:.1f}  integ={r.integrity_fail:.0f}")
    L += ["", "INVESTIGATION CHECKLIST", "-" * 72]
    L += [f" [{'x' if v else ' '}] {k}" for k, v in checklist.items()]
    L += ["", "ANALYST NOTES", "-" * 72, notes or "(none)"]
    return "\n".join(L)


def report_csv(score, verdict, ind, anomalies):
    df_ind = pd.DataFrame(ind)
    df_ind.insert(0, "section", "indicator")
    df_an = anomalies[["timestamp", "system", "ml_score"] + METRICS].copy()
    df_an.insert(0, "section", "anomaly")
    head = pd.DataFrame([{"section": "summary", "indicator": "cyber_score", "evidence": score},
                         {"section": "summary", "indicator": "verdict", "evidence": verdict}])
    return pd.concat([head, df_ind, df_an], ignore_index=True).to_csv(index=False).encode()


def report_docx(meta, score, verdict, ind, benign, anomalies, notes, checklist):
    from docx import Document
    from docx.shared import Pt, RGBColor
    doc = Document()
    doc.add_heading(f"{APP_NAME} — {APP_TAGLINE}", 0)
    p = doc.add_paragraph(DEVELOPER)
    p.runs[0].italic = True
    doc.add_paragraph(f"Generated {datetime.now():%Y-%m-%d %H:%M} | Source: {meta['source']} | "
                      f"Window: {meta['start']} → {meta['end']}")
    doc.add_heading("Verdict", 1)
    r = doc.add_paragraph().add_run(f"{verdict}  (score {score}/100)")
    r.bold = True
    r.font.size = Pt(14)
    r.font.color.rgb = RGBColor(0xB4, 0x23, 0x18) if score >= 60 else (
        RGBColor(0xC4, 0x66, 0x1F) if score >= 30 else RGBColor(0x1E, 0x7B, 0x4F))
    doc.add_heading("Cyber-attack indicators", 1)
    t = doc.add_table(rows=1, cols=4)
    t.style = "Light Grid Accent 1"
    for c, h in zip(t.rows[0].cells, ["Status", "Indicator", "MITRE ATT&CK", "Evidence"]):
        c.text = h
    for i in ind:
        cells = t.add_row().cells
        cells[0].text = "FIRED" if i["fired"] else "clear"
        cells[1].text = i["indicator"]
        cells[2].text = i["mitre"]
        cells[3].text = str(i["evidence"])
    doc.add_heading("Non-cyber signals", 1)
    for b in benign or ["None identified"]:
        doc.add_paragraph(b, style="List Bullet")
    doc.add_heading("Top anomalies", 1)
    t2 = doc.add_table(rows=1, cols=6)
    t2.style = "Light Grid Accent 1"
    for c, h in zip(t2.rows[0].cells, ["Time", "System", "ML score", "Mbps", "Auth fail", "Integrity"]):
        c.text = h
    for _, rr in anomalies.head(20).iterrows():
        cells = t2.add_row().cells
        for c, v in zip(cells, [str(rr.timestamp), rr.system, f"{rr.ml_score:.3f}",
                                f"{rr.inbound_mbps:.0f}", f"{rr.auth_fail:.0f}", f"{rr.integrity_fail:.0f}"]):
            c.text = v
    doc.add_heading("Investigation checklist", 1)
    for k, v in checklist.items():
        doc.add_paragraph(f"{'☑' if v else '☐'} {k}")
    doc.add_heading("Analyst notes", 1)
    doc.add_paragraph(notes or "(none)")
    buf = io.BytesIO()
    doc.save(buf)
    return buf.getvalue()


def report_pdf(meta, score, verdict, ind, benign, anomalies, notes, checklist):
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=letter, leftMargin=40, rightMargin=40, topMargin=40)
    ss = getSampleStyleSheet()
    small = ParagraphStyle("s", parent=ss["BodyText"], fontSize=8, leading=10)
    vcol = "#b42318" if score >= 60 else ("#c4661f" if score >= 30 else "#1e7b4f")
    story = [
        Paragraph(f"<b>{APP_NAME}</b> — {APP_TAGLINE}", ss["Title"]),
        Paragraph(f"<i>{DEVELOPER}</i>", ss["Normal"]),
        Paragraph(f"Generated {datetime.now():%Y-%m-%d %H:%M} | Source: {meta['source']} | "
                  f"Window: {meta['start']} → {meta['end']}", small),
        Spacer(1, 10),
        Paragraph(f"<font color='{vcol}' size=14><b>{verdict}</b></font> &nbsp; (score {score}/100)", ss["Heading2"]),
        Paragraph("Cyber-attack indicators", ss["Heading2"]),
    ]
    data = [["Status", "Indicator", "MITRE", "Evidence"]]
    for i in ind:
        data.append(["FIRED" if i["fired"] else "clear", Paragraph(i["indicator"], small),
                     Paragraph(i["mitre"], small), Paragraph(str(i["evidence"]), small)])
    tbl = Table(data, colWidths=[42, 160, 80, 250])
    style = [("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#12355b")),
             ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
             ("GRID", (0, 0), (-1, -1), 0.4, colors.grey), ("FONTSIZE", (0, 0), (-1, -1), 8),
             ("VALIGN", (0, 0), (-1, -1), "TOP")]
    for r_i, i in enumerate(ind, start=1):
        if i["fired"]:
            style.append(("TEXTCOLOR", (0, r_i), (0, r_i), colors.HexColor("#b42318")))
    tbl.setStyle(TableStyle(style))
    story += [tbl, Spacer(1, 8), Paragraph("Non-cyber signals", ss["Heading2"])]
    story += [Paragraph(f"• {b}", small) for b in (benign or ["None identified"])]
    story += [Paragraph("Top anomalies", ss["Heading2"])]
    ad = [["Time", "System", "ML", "Mbps", "AuthFail", "Err%", "Integ"]]
    for _, r in anomalies.head(20).iterrows():
        ad.append([str(r.timestamp)[:16], r.system, f"{r.ml_score:.3f}", f"{r.inbound_mbps:.0f}",
                   f"{r.auth_fail:.0f}", f"{r.error_rate:.1f}", f"{r.integrity_fail:.0f}"])
    at = Table(ad)
    at.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#12355b")),
                            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                            ("GRID", (0, 0), (-1, -1), 0.4, colors.grey), ("FONTSIZE", (0, 0), (-1, -1), 7.5)]))
    story += [at, Paragraph("Investigation checklist", ss["Heading2"])]
    story += [Paragraph(f"{'[x]' if v else '[ ]'} {k}", small) for k, v in checklist.items()]
    story += [Paragraph("Analyst notes", ss["Heading2"]), Paragraph((notes or "(none)").replace("\n", "<br/>"), small)]
    doc.build(story)
    return buf.getvalue()


# ---------------------------------------------------------------------------
# Sidebar — data source & settings
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("⚙️ Data source")
    mode = st.radio("Choose input", ["Synthetic demo data", "Upload real data"], index=0)
    if mode == "Synthetic demo data":
        scen_label = st.selectbox("Demo scenario", list(SCENARIOS))
        hours = st.slider("Time window (hours)", 2, 24, 6)
        tel, ev = make_synthetic(SCENARIOS[scen_label], hours)
        source = f"Synthetic — {scen_label}"
    else:
        st.caption("Telemetry CSV columns: " + ", ".join(TELEMETRY_COLS))
        tf = st.file_uploader("System telemetry (CSV)", type=["csv"])
        st.caption("Security events CSV columns: " + ", ".join(EVENT_COLS))
        ef = st.file_uploader("Security event log (CSV)", type=["csv"])
        t_tmp, e_tmp = make_synthetic("normal", 1)
        c1, c2 = st.columns(2)
        c1.download_button("Telemetry template", t_tmp.head(20).to_csv(index=False), "telemetry_template.csv")
        c2.download_button("Events template", e_tmp.head(20).to_csv(index=False), "events_template.csv")
        if tf is None:
            st.info("Upload telemetry to begin (or switch to synthetic demo).")
            st.stop()
        tel = pd.read_csv(tf)
        missing = [c for c in TELEMETRY_COLS if c not in tel.columns]
        if missing:
            st.error(f"Telemetry missing columns: {missing}")
            st.stop()
        tel["timestamp"] = pd.to_datetime(tel["timestamp"])
        if ef is not None:
            ev = pd.read_csv(ef)
            for c in EVENT_COLS:
                if c not in ev.columns:
                    ev[c] = ""
        else:
            ev = pd.DataFrame(columns=EVENT_COLS)
        ev["timestamp"] = pd.to_datetime(ev["timestamp"], errors="coerce")
        ev = ev.fillna("")
        source = f"Uploaded — {tf.name}" + (f" + {ef.name}" if ef else "")

    st.header("🎚️ Detection tuning")
    z_thr = st.slider("Robust z-score threshold", 2.0, 10.0, 4.0, 0.5)
    sustain = st.slider("Sustained minutes to fire", 1, 30, 5)
    contamination = st.slider("ML contamination (expected anomaly share)", 0.01, 0.30, 0.05, 0.01)
    sel_systems = st.multiselect("Systems", sorted(tel.system.unique()), default=sorted(tel.system.unique()))

tel = tel[tel.system.isin(sel_systems)]
if tel.empty:
    st.warning("No systems selected.")
    st.stop()

with st.spinner("Running detection engine…"):
    tel_z = run_isolation_forest(compute_zscores(tel), contamination)
    score, verdict, indicators, benign = assess(tel_z, ev, z_thr, sustain)
anomalies = tel_z[tel_z.ml_anomaly].sort_values("ml_score", ascending=False)
meta = {"source": source, "start": str(tel.timestamp.min()), "end": str(tel.timestamp.max()),
        "systems": ", ".join(sel_systems)}

# ---------------------------------------------------------------------------
# Tabs
# ---------------------------------------------------------------------------
tabs = st.tabs(["📊 Overview", "🌐 Network", "🔐 Authentication", "🧬 Integrity",
                "🤖 ML Anomalies", "🕒 Event Timeline", "🧭 Investigation Playbook", "📄 Reports"])

with tabs[0]:
    vcls = "v-high" if score >= 60 else ("v-mod" if score >= 30 else "v-low")
    left, right = st.columns([1, 2])
    with left:
        fig = go.Figure(go.Indicator(
            mode="gauge+number", value=score, title={"text": "Cyber-attack likelihood"},
            gauge={"axis": {"range": [0, 100]}, "bar": {"color": "#12355b"},
                   "steps": [{"range": [0, 30], "color": "#cfe8da"}, {"range": [30, 60], "color": "#f6dcc2"},
                             {"range": [60, 100], "color": "#f3c3bf"}]}))
        fig.update_layout(height=260, margin=dict(t=50, b=10, l=40, r=40))
        st.plotly_chart(fig, width="stretch")
        st.markdown(f'<div class="verdict {vcls}">{verdict}</div>', unsafe_allow_html=True)
    with right:
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Indicators fired", f"{sum(i['fired'] for i in indicators)}/{len(indicators)}")
        k2.metric("ML anomalies", len(anomalies))
        k3.metric("Security events", len(ev))
        k4.metric("Critical events", int((ev.severity == "critical").sum()) if len(ev) else 0)
        st.subheader("Indicators")
        for i in indicators:
            icon = "🔴" if i["fired"] else "🟢"
            st.markdown(f'<div class="ind">{icon} <b>{i["indicator"]}</b> '
                        f'<code>{i["mitre"]}</code><br><small>{i["evidence"]}</small></div>',
                        unsafe_allow_html=True)
        if benign:
            st.subheader("Non-cyber signals")
            for b in benign:
                st.success(b)

with tabs[1]:
    m = st.selectbox("Metric", ["inbound_mbps", "conn_count", "cpu_pct", "latency_ms", "error_rate"])
    st.plotly_chart(px.line(tel_z, x="timestamp", y=m, color="system", title=f"{m} by system"),
                    width="stretch")
    heat = tel_z.pivot_table(index="system", columns=tel_z.timestamp.dt.floor("15min"),
                             values=f"z_{m}", aggfunc="max")
    st.plotly_chart(px.imshow(heat, aspect="auto", color_continuous_scale="RdYlBu_r",
                              title=f"Peak robust z-score ({m}) per 15 min"), width="stretch")

with tabs[2]:
    st.plotly_chart(px.area(tel_z, x="timestamp", y="auth_fail", color="system",
                            title="Authentication failures per minute"), width="stretch")
    if len(ev):
        logins = ev[ev.event_type.isin(["login_failure", "login_success"])]
        c1, c2 = st.columns(2)
        c1.plotly_chart(px.bar(logins.groupby("country").size().reset_index(name="count"),
                               x="country", y="count", title="Login attempts by country"), width="stretch")
        top = logins.groupby(["src_ip", "event_type"]).size().unstack(fill_value=0)
        top["total"] = top.sum(axis=1)
        c2.dataframe(top.sort_values("total", ascending=False).head(10), width="stretch")

with tabs[3]:
    st.plotly_chart(px.bar(tel_z.groupby("system")["integrity_fail"].sum().reset_index(),
                           x="system", y="integrity_fail", title="Data-integrity check failures"),
                    width="stretch")
    if len(ev):
        st.dataframe(ev[ev.event_type.isin(["config_change", "file_deleted", "new_admin_account",
                                            "priv_escalation", "malware_alert"])], width="stretch")

with tabs[4]:
    st.plotly_chart(px.scatter(tel_z, x="timestamp", y="ml_score", color="ml_anomaly", facet_row="system",
                               height=140 * len(sel_systems) + 80, title="Isolation Forest anomaly score",
                               color_discrete_map={True: "#b42318", False: "#9bb3cf"}),
                    width="stretch")
    st.dataframe(anomalies.head(100)[["timestamp", "system", "ml_score"] + METRICS], width="stretch")

with tabs[5]:
    if len(ev):
        sev_order = {"low": 0, "medium": 1, "high": 2, "critical": 3}
        evp = ev.copy()
        evp["sev_n"] = evp.severity.map(sev_order).fillna(0)
        st.plotly_chart(px.scatter(evp, x="timestamp", y="event_type", color="severity", symbol="system",
                                   hover_data=["src_ip", "country", "user", "detail"],
                                   color_discrete_map={"low": "#9bb3cf", "medium": "#f2a541",
                                                       "high": "#e4572e", "critical": "#8b0000"},
                                   title="Security event timeline"), width="stretch")
        st.dataframe(evp[evp.sev_n >= 2].drop(columns="sev_n"), width="stretch")
    else:
        st.info("No security events loaded.")

CHECKLIST = [
    "Confirm scope: which systems failed first (NOTAM, ERAM, TFMS, SWIM, comms)?",
    "Correlate outage start with change tickets / maintenance windows",
    "Review auth logs for spray, brute force, success-after-failure, impossible travel",
    "Check for new/elevated privileged accounts and off-hours admin sessions",
    "Verify database & file integrity against known-good hashes/backups",
    "Pull EDR/AV alerts and hunt for wiper / ransomware artefacts",
    "Inspect NetFlow/firewall for volumetric floods and C2 beacons",
    "Check ADS-B / GPS feeds for spoofing or jamming anomalies",
    "Preserve evidence: memory images, logs, disk snapshots (chain of custody)",
    "Notify FAA SOC, CISA, TSA and FBI per incident-reporting requirements",
]
with tabs[6]:
    st.markdown("Work through these probes to separate **cyber attack** from **technical failure**. "
                "Ticked items are included in the exported report.")
    checklist = {c: st.checkbox(c, key=f"chk_{n}") for n, c in enumerate(CHECKLIST)}
    notes = st.text_area("Analyst notes", height=140, placeholder="Findings, hypotheses, hand-offs…")

with tabs[7]:
    st.subheader("Export investigation report")
    st.caption("Reports include verdict, indicators with MITRE mapping, anomalies, checklist status and notes.")
    stamp = datetime.now().strftime("%Y%m%d_%H%M")
    args = (meta, score, verdict, indicators, benign, anomalies, notes, checklist)
    c1, c2, c3, c4 = st.columns(4)
    c1.download_button("📕 PDF", report_pdf(*args), f"aerosentinel_{stamp}.pdf", "application/pdf",
                       width="stretch")
    c2.download_button("📘 Word", report_docx(*args), f"aerosentinel_{stamp}.docx",
                       "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                       width="stretch")
    c3.download_button("📄 Text", report_text(*args), f"aerosentinel_{stamp}.txt", "text/plain",
                       width="stretch")
    c4.download_button("📊 CSV", report_csv(score, verdict, indicators, anomalies),
                       f"aerosentinel_{stamp}.csv", "text/csv", width="stretch")
    with st.expander("Preview text report"):
        st.code(report_text(*args), language="text")

st.markdown("---")
st.caption(f"{APP_NAME} • {DEVELOPER} • For investigative decision support only — "
           "confirm findings with your SOC, FAA and CISA before attribution.")
