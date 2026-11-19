
# ClassiNet Outage Simulator
# NSANet-like Classified Enterprise Network Outage Simulation (SYNTHETIC DATA ONLY)
# Developed by Randy Singh from Kalsnet Consulting Group

# IMPORTANT: This application is a training / analysis simulator. It uses entirely
# fictional, randomly generated data that only *resembles* the general shape of a
# large, segmented, high-security enterprise network. It does not reproduce, model,
# connect to, or access any real classified system, NSA infrastructure, or
# government network. All site names, devices, and figures are invented.


import io
import datetime as dt

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from docx import Document  # noqa: E402
from docx.shared import Pt, RGBColor, Inches  # noqa: E402
from reportlab.lib import colors  # noqa: E402
from reportlab.lib.pagesizes import letter  # noqa: E402
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle  # noqa: E402
from reportlab.lib.units import inch  # noqa: E402
from reportlab.platypus import (  # noqa: E402
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, PageBreak,
)

# ---------------------------------------------------------------------------
# 1. CONSTANTS - fictional network model
# ---------------------------------------------------------------------------
APP_NAME = "ClassiNet Outage Simulator"
APP_TAGLINE = "NSANet-like Classified Enterprise Network Outage Simulation - Synthetic Data Only"
DEVELOPER = "Developed by Randy Singh from Kalsnet Consulting Group"
BLUE = "#0B4FD8"

# site -> (tier, criticality weight 0-1, users served, (x, y) diagram position)
SITES = {
    "CORE-HQ":     ("Core",               1.00, 4000, (0.0, 0.0)),
    "DC-EAST":     ("Data Center",        0.95, 2500, (2.0, 1.2)),
    "DC-WEST":     ("Data Center",        0.95, 2500, (-2.0, 1.2)),
    "GW-CRYPTO-1": ("Encryption Gateway", 0.90, 1800, (1.4, -1.4)),
    "GW-CRYPTO-2": ("Encryption Gateway", 0.90, 1800, (-1.4, -1.4)),
    "ENCLAVE-A":   ("Secure Enclave",     0.85,  900, (2.4, -2.6)),
    "ENCLAVE-B":   ("Secure Enclave",     0.85,  900, (-2.4, -2.6)),
    "REMOTE-1":    ("Remote Site",        0.50,  300, (3.6, 2.4)),
    "REMOTE-2":    ("Remote Site",        0.50,  300, (0.0, 2.8)),
    "REMOTE-3":    ("Remote Site",        0.50,  250, (-3.6, 2.4)),
}
LINKS = [
    ("CORE-HQ", "DC-EAST"), ("CORE-HQ", "DC-WEST"), ("DC-EAST", "DC-WEST"),
    ("CORE-HQ", "GW-CRYPTO-1"), ("CORE-HQ", "GW-CRYPTO-2"),
    ("GW-CRYPTO-1", "ENCLAVE-A"), ("GW-CRYPTO-2", "ENCLAVE-B"),
    ("DC-EAST", "REMOTE-1"), ("DC-EAST", "REMOTE-2"), ("DC-WEST", "REMOTE-2"),
    ("DC-WEST", "REMOTE-3"),
]
# Optional redundant paths used by the "what-if" simulator
BACKUP_LINKS = [("REMOTE-1", "DC-WEST"), ("REMOTE-3", "DC-EAST"),
                ("ENCLAVE-A", "GW-CRYPTO-2"), ("ENCLAVE-B", "GW-CRYPTO-1")]
DEFAULT_UPLOAD_CRITICALITY = 0.70
DEFAULT_UPLOAD_USERS = 500

# ---------------------------------------------------------------------------
# 2. OUTAGE CASE LIBRARY - problem + how the app addresses it
# ---------------------------------------------------------------------------
OUTAGE_CASES = {
    "WAN Fiber Cut": dict(
        component="WAN transport circuit", weight=0.16, ttd_mean=4,
        duration=(30, 360), loss=(95, 100), latency=(900, 2000), user_frac=(0.6, 1.0),
        tiers=["Remote Site", "Data Center", "Core"],
        causes=["Construction / backhoe damage", "Carrier equipment failure", "Cable theft or rodent damage"],
        problem="A physical long-haul circuit is severed. Every packet on that path is lost, and any site "
                "that has only one path (single-homed) becomes completely isolated from the core.",
        symptom="Interface down, loss of light, 100% packet loss",
        detection="Packet loss jumps to ~100% instantly; link state = DOWN",
        analysis="Topology check finds which sites lost all paths to CORE-HQ; user-minutes lost are counted",
        mitigation="Fail over to a diverse path, open a carrier ticket, add a second circuit for single-homed sites",
        key_metric="Outage Duration and Users Affected - detection is fast, recovery depends on the carrier.",
        playbook=["Confirm loss-of-light on both ends", "Shift traffic to diverse / backup path",
                  "Open priority carrier ticket with circuit ID", "Notify affected site leads",
                  "Post-incident: fund physically diverse second circuit"],
    ),
    "Routing Instability (BGP/OSPF Flap)": dict(
        component="Core routing protocol", weight=0.13, ttd_mean=12,
        duration=(10, 120), loss=(10, 60), latency=(150, 600), user_frac=(0.3, 0.8),
        tiers=["Core", "Data Center", "Encryption Gateway"],
        causes=["Flapping interface", "Route leak / bad route policy", "Router CPU or memory exhaustion"],
        problem="Routes repeatedly appear and disappear. Traffic takes changing or looping paths, causing "
                "partial loss and very high latency rather than a clean outage - it is easy to miss.",
        symptom="Intermittent loss, latency spikes, route table churn",
        detection="Loss between 10-60% with latency > 150 ms; neighbor up/down events",
        analysis="Severity score weights partial loss; MTTD highlights slow detection of 'grey' failures",
        mitigation="Dampen the flapping peer, roll back route policy, pin traffic to a stable path",
        key_metric="Time to Detect (TTD) - partial failures are often noticed late.",
        playbook=["Identify flapping neighbor from routing logs", "Apply route dampening / shut unstable peer",
                  "Roll back last routing-policy change", "Verify convergence and latency baseline",
                  "Post-incident: add alerting on neighbor state changes"],
    ),
    "DNS / Directory Service Failure": dict(
        component="Name resolution & directory", weight=0.11, ttd_mean=15,
        duration=(15, 180), loss=(0, 2), latency=(40, 120), user_frac=(0.5, 1.0),
        tiers=["Core", "Data Center"],
        causes=["DNS server crash", "Zone file error", "Directory replication failure"],
        problem="The network itself is up, but users cannot find services by name or log in. Pings work; "
                "applications do not. Monitoring that only checks links shows 'green' while users are down.",
        symptom="Name lookups time out; logins fail; links look healthy",
        detection="Low packet loss but many users affected - a 'service outage on a healthy network'",
        analysis="Users-affected and user-minutes metrics capture impact that packet loss alone misses",
        mitigation="Fail over to secondary resolvers, restore last good zone, force directory re-sync",
        key_metric="User-Minutes Lost - packet loss stays near 0%, so impact must be measured by users.",
        playbook=["Test resolution against primary and secondary resolvers", "Point clients to healthy resolver",
                  "Restore last known-good zone / directory snapshot", "Validate logins at each site",
                  "Post-incident: add synthetic name-lookup probes"],
    ),
    "Encryption Gateway / Key Expiry": dict(
        component="Inline encryption gateway (simulated)", weight=0.12, ttd_mean=20,
        duration=(30, 480), loss=(90, 100), latency=(800, 2000), user_frac=(0.8, 1.0),
        tiers=["Encryption Gateway", "Secure Enclave"],
        causes=["Cryptographic key / credential expired", "Gateway hardware fault", "Tunnel policy mismatch after update"],
        problem="Segmented secure enclaves reach the core only through encryption gateways. If a gateway fails "
                "or its keys expire, encrypted tunnels drop and the whole enclave behind it is cut off.",
        symptom="Encrypted tunnels down; enclave unreachable while the gateway may still power on",
        detection="Near-100% loss for every site behind the gateway",
        analysis="Topology view shows the enclave isolated; the What-If simulator shows the value of a second gateway path",
        mitigation="Switch to the standby gateway, re-key under approved procedures, track key expiry dates proactively",
        key_metric="Time to Restore (TTR) - re-keying under strict procedures takes time.",
        playbook=["Confirm tunnel state on both gateways", "Move enclave traffic to standby gateway",
                  "Re-key using approved (simulated) procedure", "Verify enclave reachability end-to-end",
                  "Post-incident: build a key-expiry calendar with 30/7/1-day alerts"],
    ),
    "PKI Certificate Expiry / Auth Failure": dict(
        component="PKI / authentication services", weight=0.10, ttd_mean=30,
        duration=(20, 240), loss=(0, 5), latency=(30, 80), user_frac=(0.4, 0.9),
        tiers=["Core", "Data Center", "Secure Enclave"],
        causes=["Server certificate expired", "Revocation list not reachable", "Clock drift breaks validation"],
        problem="A certificate expires or cannot be validated, so secure web, VPN and smart-card logins are "
                "rejected. Like DNS failures, the network looks healthy while users are locked out.",
        symptom="TLS / login errors; help-desk calls spike",
        detection="Low packet loss, high users affected, long time-to-detect",
        analysis="Long TTD drives a high error-budget burn; the formula guide shows how TTD inflates downtime",
        mitigation="Install renewed certificate, restore revocation-list access, fix time sync",
        key_metric="Time to Detect (TTD) - these are usually found by users, not monitoring.",
        playbook=["Check certificate validity dates on affected services", "Install renewed certificate",
                  "Confirm revocation list / time sources reachable", "Re-test logins from each tier",
                  "Post-incident: automated certificate-expiry monitoring"],
    ),
    "Power / HVAC Facility Failure": dict(
        component="Facility power & cooling", weight=0.08, ttd_mean=3,
        duration=(60, 600), loss=(100, 100), latency=(1500, 2000), user_frac=(0.9, 1.0),
        tiers=["Data Center", "Core", "Remote Site"],
        causes=["Utility power loss with generator failure", "UPS battery failure", "Cooling failure forcing shutdown"],
        problem="A facility loses power or cooling and every device in it goes dark. All sites that depend "
                "on that facility as their only path are isolated too.",
        symptom="Every device at the site unreachable simultaneously",
        detection="Instant 100% loss across all devices at one site",
        analysis="Largest duration and cost; topology shows cascading isolation of dependent sites",
        mitigation="Fail services to the alternate data center, restore power, staged equipment restart",
        key_metric="Estimated Cost and Availability - long and site-wide.",
        playbook=["Confirm facility status with site operations", "Activate continuity plan at alternate data center",
                  "Staged power-on once stable", "Verify each service tier",
                  "Post-incident: generator & UPS load testing schedule"],
    ),
    "Misconfiguration / Change Error": dict(
        component="Network device configuration", weight=0.18, ttd_mean=10,
        duration=(10, 150), loss=(20, 100), latency=(60, 400), user_frac=(0.2, 0.9),
        tiers=["Core", "Data Center", "Encryption Gateway", "Secure Enclave", "Remote Site"],
        causes=["Bad access-control / firewall rule", "Wrong VLAN or interface change", "Untested automation push"],
        problem="A planned change goes wrong - the most common cause of outages in real enterprises. "
                "Impact ranges from a single blocked application to a whole site offline.",
        symptom="Problems start right after a change window",
        detection="Outage start time correlates with a change ticket",
        analysis="Pareto chart ranks root causes so the biggest repeat offenders are fixed first",
        mitigation="Immediate rollback, then peer-reviewed, tested re-implementation",
        key_metric="Incident Count (frequency) - small but frequent; Pareto analysis targets it.",
        playbook=["Check change calendar for recent changes", "Roll back to last known-good configuration",
                  "Confirm service restored", "Root-cause review with change owner",
                  "Post-incident: pre-change validation & peer review"],
    ),
    "Traffic Congestion / DDoS-like Surge": dict(
        component="Bandwidth / capacity", weight=0.12, ttd_mean=8,
        duration=(15, 200), loss=(5, 40), latency=(200, 900), user_frac=(0.3, 0.9),
        tiers=["Core", "Data Center", "Remote Site"],
        causes=["Flood of unwanted traffic", "Large unscheduled data transfer", "Undersized link"],
        problem="Links fill up. Nothing is 'down', but queues overflow, latency rises sharply and some packets "
                "are dropped, making applications slow or unusable.",
        symptom="Utilization near 100%, high latency, moderate loss",
        detection="Latency > 200 ms with 5-40% loss and high utilization",
        analysis="Telemetry tab shows the latency spike against baseline; severity weights loss + duration",
        mitigation="Rate-limit / filter offending traffic, apply QoS priority for mission traffic, add capacity",
        key_metric="Latency and Packet Loss - service degraded rather than down.",
        playbook=["Identify top talkers / traffic sources", "Apply rate-limit or upstream filtering",
                  "Enforce QoS priority for mission-critical flows", "Monitor until utilization < 70%",
                  "Post-incident: capacity planning review"],
    ),
}

SEVERITY_BINS = [-0.1, 30, 50, 70, 100.1]
SEVERITY_LABELS = ["Low", "Medium", "High", "Critical"]
SEV_COLORS = {"Low": "#2E9E5B", "Medium": "#E3B505", "High": "#F07B1D", "Critical": "#D62828"}

# ---------------------------------------------------------------------------
# 3. FIELD / FORMULA DICTIONARY (used by UI and every export)
# ---------------------------------------------------------------------------
FIELD_DOCS = [
    ("Time to Detect (TTD)", "TTD = detect_time - start_time   (minutes)",
     "How long the problem existed before anyone/anything noticed it. Smaller is better."),
    ("Time to Restore (TTR)", "TTR = restore_time - detect_time   (minutes)",
     "How long it took to fix the problem after it was noticed."),
    ("Outage Duration", "Duration = restore_time - start_time = TTD + TTR   (minutes)",
     "Total time users were impacted, from the first failure to full recovery."),
    ("MTTD (Mean Time to Detect)", "MTTD = Sum of TTD / number of incidents",
     "The average detection time. A high MTTD means monitoring is missing problems."),
    ("MTTR (Mean Time to Restore)", "MTTR = Sum of Duration / number of incidents",
     "The average length of an outage from start to recovery."),
    ("Site Downtime", "Downtime = total minutes covered by the site's incidents (overlaps counted once)",
     "If two incidents overlap at the same site, the shared minutes are only counted one time."),
    ("Availability %", "Availability = (Period minutes - Downtime) / Period minutes x 100",
     "Share of time the site was working. 99.9% approx. 43 minutes of downtime in 30 days."),
    ("MTBF (Mean Time Between Failures)", "MTBF = (Period hours - Downtime hours) / number of incidents",
     "Average working time between failures. Larger is better."),
    ("Allowed Downtime (SLA budget)", "Allowed = (1 - SLA target) x Period minutes",
     "The maximum downtime allowed by the service-level target, e.g. 99.9% over 30 days = 43.2 min."),
    ("Error Budget Consumed %", "Budget used = Downtime / Allowed Downtime x 100",
     "Over 100% means the SLA target was broken (SLA breach)."),
    ("User-Minutes Lost", "User-Minutes = Users Affected x Duration",
     "Combines how many people and for how long - 100 users for 60 min = 6,000 user-minutes."),
    ("User-Weighted Network Availability", "= (1 - Sum of User-Minutes Lost / (Total users x Period minutes)) x 100",
     "Availability from the user's point of view: big outages at busy sites count more."),
    ("Criticality Weight (C)", "Fixed per site tier: Core 1.00, Data Center 0.95, Encryption GW 0.90, Enclave 0.85, Remote 0.50",
     "How mission-important a site is. Uploaded sites without a value default to 0.70."),
    ("Estimated Cost", "Cost = Duration x Cost-per-minute x Criticality weight",
     "A simple financial / mission-impact estimate. Cost-per-minute is set in the sidebar."),
    ("Severity Score (0-100)",
     "Score = 100 x (0.35*U + 0.30*D + 0.20*P + 0.15*C), where U = min(Users / 1000, 1), "
     "D = min(Duration / 240, 1), P = Packet loss % / 100, C = Criticality",
     "One number that blends people affected (35%), length (30%), packet loss (20%) and site importance (15%)."),
    ("Severity Level", "Low < 30 <= Medium < 50 <= High < 70 <= Critical",
     "Plain-language label derived from the Severity Score."),
    ("Isolated Site (topology)", "Site has no remaining network path to CORE-HQ after the failure",
     "Calculated with a graph search over the network diagram; used in the What-If simulator."),
]
FORMULA_LOOKUP = {name: (f, e) for name, f, e in FIELD_DOCS}

REQUIRED_COLS = ["incident_id", "site", "outage_type", "start_time", "detect_time", "restore_time", "users_affected"]
OPTIONAL_COLS = {"component": "Unspecified", "packet_loss_pct": 0.0, "latency_ms": 0.0,
                 "root_cause": "Unspecified", "criticality": np.nan}


# ---------------------------------------------------------------------------
# 4. DATA GENERATION
# ---------------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def generate_synthetic(seed: int, days: int, n_incidents: int, start_date: dt.date) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    start = pd.Timestamp(start_date)
    types = list(OUTAGE_CASES)
    w = np.array([OUTAGE_CASES[t]["weight"] for t in types])
    w = w / w.sum()
    rows = []
    for i in range(n_incidents):
        t = rng.choice(types, p=w)
        c = OUTAGE_CASES[t]
        eligible = [s for s, v in SITES.items() if v[0] in c["tiers"]]
        site = rng.choice(eligible)
        st_time = start + pd.Timedelta(minutes=int(rng.integers(0, days * 1440 - 600)))
        ttd = max(1.0, rng.gamma(2.0, c["ttd_mean"] / 2))
        ttr = rng.uniform(*c["duration"])
        detect = st_time + pd.Timedelta(minutes=round(ttd, 1))
        restore = detect + pd.Timedelta(minutes=round(ttr, 1))
        rows.append(dict(
            incident_id=f"SIM-{i + 1:04d}", site=site, outage_type=t, component=c["component"],
            start_time=st_time, detect_time=detect, restore_time=restore,
            users_affected=int(SITES[site][2] * rng.uniform(*c["user_frac"])),
            packet_loss_pct=round(float(rng.uniform(*c["loss"])), 1),
            latency_ms=round(float(rng.uniform(*c["latency"])), 0),
            root_cause=str(rng.choice(c["causes"])),
            criticality=SITES[site][1],
        ))
    df = pd.DataFrame(rows).sort_values("start_time").reset_index(drop=True)
    return df


@st.cache_data(show_spinner=False)
def generate_telemetry(incidents: pd.DataFrame, sites: tuple, start: pd.Timestamp, days: int, seed: int):
    """Hourly latency / loss / utilization per site, with incidents injected."""
    rng = np.random.default_rng(seed + 99)
    idx = pd.date_range(start, periods=days * 24, freq="h")
    hours = idx.hour.values
    frames = []
    for s in sites:
        base_lat = rng.uniform(18, 45)
        diurnal = 1 + 0.25 * np.sin((hours - 8) / 24 * 2 * np.pi)
        lat = base_lat * diurnal + rng.normal(0, 2, len(idx))
        loss = np.clip(rng.normal(0.1, 0.05, len(idx)), 0, None)
        util = np.clip(40 * diurnal + rng.normal(0, 5, len(idx)), 5, 99)
        sub = incidents[incidents["site"] == s]
        for _, r in sub.iterrows():
            m = (idx >= r["start_time"].floor("h")) & (idx <= r["restore_time"].ceil("h"))
            lat[m] = np.maximum(lat[m], r["latency_ms"] if r["latency_ms"] > 0 else lat[m])
            loss[m] = np.maximum(loss[m], r["packet_loss_pct"])
            if "Congestion" in str(r["outage_type"]):
                util[m] = rng.uniform(92, 99, m.sum())
        frames.append(pd.DataFrame({"timestamp": idx, "site": s, "latency_ms": lat.round(1),
                                    "packet_loss_pct": loss.round(2), "utilization_pct": util.round(1)}))
    return pd.concat(frames, ignore_index=True)


def upload_template() -> pd.DataFrame:
    base = pd.Timestamp("2026-03-01 08:00")
    return pd.DataFrame([
        dict(incident_id="INC-1001", site="CORE-HQ", outage_type="Misconfiguration / Change Error",
             start_time=base, detect_time=base + pd.Timedelta(minutes=6),
             restore_time=base + pd.Timedelta(minutes=48), users_affected=1200, component="Core switch",
             packet_loss_pct=65, latency_ms=240, root_cause="Bad ACL rule", criticality=1.0),
        dict(incident_id="INC-1002", site="BRANCH-17", outage_type="WAN Fiber Cut",
             start_time=base + pd.Timedelta(days=3), detect_time=base + pd.Timedelta(days=3, minutes=2),
             restore_time=base + pd.Timedelta(days=3, minutes=190), users_affected=220, component="WAN circuit",
             packet_loss_pct=100, latency_ms=0, root_cause="Construction damage", criticality=0.5),
        dict(incident_id="INC-1003", site="DC-EAST", outage_type="DNS / Directory Service Failure",
             start_time=base + pd.Timedelta(days=9), detect_time=base + pd.Timedelta(days=9, minutes=25),
             restore_time=base + pd.Timedelta(days=9, minutes=95), users_affected=2100, component="DNS",
             packet_loss_pct=0, latency_ms=55, root_cause="Zone file error", criticality=None),
    ])


def read_upload(file) -> pd.DataFrame:
    name = file.name.lower()
    if name.endswith((".xlsx", ".xls")):
        return pd.read_excel(file)
    return pd.read_csv(file)


def clean_uploaded(raw: pd.DataFrame, mapping: dict):
    """Rename mapped columns, coerce types, drop invalid rows. Returns (df, issues list)."""
    issues = []
    df = pd.DataFrame()
    for target, src in mapping.items():
        if src and src != "- not provided -":
            df[target] = raw[src]
    for col in REQUIRED_COLS:
        if col not in df:
            issues.append(f"Required field '{col}' is not mapped.")
    if issues:
        return None, issues
    for col, default in OPTIONAL_COLS.items():
        if col not in df:
            df[col] = default
    for col in ["start_time", "detect_time", "restore_time"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    for col in ["users_affected", "packet_loss_pct", "latency_ms", "criticality"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df["users_affected"] = df["users_affected"].fillna(0).clip(lower=0).astype(int)
    df["packet_loss_pct"] = df["packet_loss_pct"].fillna(0).clip(0, 100)
    df["latency_ms"] = df["latency_ms"].fillna(0).clip(lower=0)
    df["detect_time"] = df["detect_time"].fillna(df["start_time"])
    n0 = len(df)
    bad = df["start_time"].isna() | df["restore_time"].isna() | (df["restore_time"] < df["start_time"])
    if bad.any():
        issues.append(f"{int(bad.sum())} row(s) dropped: missing/invalid start or restore time, or restore before start.")
    df = df[~bad].copy()
    fix = df["detect_time"] > df["restore_time"]
    if fix.any():
        issues.append(f"{int(fix.sum())} row(s): detect_time after restore_time - set detect_time = start_time.")
        df.loc[fix, "detect_time"] = df.loc[fix, "start_time"]
    fix = df["detect_time"] < df["start_time"]
    if fix.any():
        issues.append(f"{int(fix.sum())} row(s): detect_time before start_time - set detect_time = start_time.")
        df.loc[fix, "detect_time"] = df.loc[fix, "start_time"]
    for c in ["incident_id", "site", "outage_type", "component", "root_cause"]:
        df[c] = df[c].astype(str).str.strip()
    issues.append(f"{len(df)} of {n0} rows loaded successfully.")
    return df.sort_values("start_time").reset_index(drop=True), issues


# ---------------------------------------------------------------------------
# 5. ANALYTICS
# ---------------------------------------------------------------------------
def site_info(site):
    if site in SITES:
        tier, crit, users, _ = SITES[site]
        return tier, crit, users
    return "Uploaded Site", DEFAULT_UPLOAD_CRITICALITY, DEFAULT_UPLOAD_USERS


def merged_minutes(intervals, lo, hi):
    """Total minutes covered by a list of (start, end) intervals, overlaps counted once, clipped to [lo, hi]."""
    iv = sorted((max(s, lo), min(e, hi)) for s, e in intervals if e > lo and s < hi)
    total, cur_s, cur_e = 0.0, None, None
    for s, e in iv:
        if cur_e is None or s > cur_e:
            if cur_e is not None:
                total += (cur_e - cur_s).total_seconds() / 60
            cur_s, cur_e = s, e
        else:
            cur_e = max(cur_e, e)
    if cur_e is not None:
        total += (cur_e - cur_s).total_seconds() / 60
    return total


def enrich_incidents(df: pd.DataFrame, cost_per_min: float) -> pd.DataFrame:
    d = df.copy()
    d["tier"] = d["site"].map(lambda s: site_info(s)[0])
    default_crit = d["site"].map(lambda s: site_info(s)[1])
    d["criticality"] = pd.to_numeric(d.get("criticality"), errors="coerce").fillna(default_crit).clip(0, 1)
    d["ttd_min"] = ((d["detect_time"] - d["start_time"]).dt.total_seconds() / 60).round(1)
    d["ttr_min"] = ((d["restore_time"] - d["detect_time"]).dt.total_seconds() / 60).round(1)
    d["duration_min"] = ((d["restore_time"] - d["start_time"]).dt.total_seconds() / 60).round(1)
    d["user_minutes_lost"] = (d["users_affected"] * d["duration_min"]).round(0)
    d["est_cost_usd"] = (d["duration_min"] * cost_per_min * d["criticality"]).round(2)
    U = np.minimum(d["users_affected"] / 1000, 1)
    D = np.minimum(d["duration_min"] / 240, 1)
    P = d["packet_loss_pct"] / 100
    C = d["criticality"]
    d["severity_score"] = (100 * (0.35 * U + 0.30 * D + 0.20 * P + 0.15 * C)).round(1)
    d["severity_level"] = pd.cut(d["severity_score"], SEVERITY_BINS, labels=SEVERITY_LABELS).astype(str)
    return d


def site_metrics(d: pd.DataFrame, period_start, period_end, sla: float) -> pd.DataFrame:
    period_min = (period_end - period_start).total_seconds() / 60
    allowed = (1 - sla / 100) * period_min
    all_sites = list(dict.fromkeys(list(SITES) + list(d["site"].unique())))
    rows = []
    for s in all_sites:
        sub = d[d["site"] == s]
        n = len(sub)
        down = merged_minutes(list(zip(sub["start_time"], sub["restore_time"])), period_start, period_end)
        avail = (period_min - down) / period_min * 100
        tier, crit, users = site_info(s)
        if s not in SITES and n:
            users = int(sub["users_affected"].max())
        rows.append(dict(
            site=s, tier=tier, users_served=users, incidents=n, downtime_min=round(down, 1),
            availability_pct=round(avail, 4),
            mtbf_hours=round((period_min - down) / 60 / n, 1) if n else np.nan,
            mttr_min=round(sub["duration_min"].mean(), 1) if n else 0.0,
            mttd_min=round(sub["ttd_min"].mean(), 1) if n else 0.0,
            allowed_downtime_min=round(allowed, 1),
            error_budget_used_pct=round(down / allowed * 100, 1) if allowed > 0 else np.nan,
            sla_met="Yes" if avail >= sla else "No",
            user_minutes_lost=int(sub["user_minutes_lost"].sum()),
            est_cost_usd=round(sub["est_cost_usd"].sum(), 2),
        ))
    sm = pd.DataFrame(rows)
    # Keep only sites that exist in the analysed data set (synthetic sites always shown)
    return sm[(sm["site"].isin(SITES)) | (sm["incidents"] > 0)].reset_index(drop=True)


def type_metrics(d: pd.DataFrame) -> pd.DataFrame:
    if d.empty:
        return pd.DataFrame()
    g = d.groupby("outage_type").agg(
        incidents=("incident_id", "count"), mttd_min=("ttd_min", "mean"), mttr_min=("duration_min", "mean"),
        total_downtime_min=("duration_min", "sum"), user_minutes_lost=("user_minutes_lost", "sum"),
        est_cost_usd=("est_cost_usd", "sum"), avg_severity=("severity_score", "mean"),
    ).reset_index()
    g["share_pct"] = (g["incidents"] / g["incidents"].sum() * 100).round(1)
    return g.round(1).sort_values("incidents", ascending=False).reset_index(drop=True)


def overall_kpis(d, sm, period_start, period_end, sla):
    period_min = (period_end - period_start).total_seconds() / 60
    total_users = sm["users_served"].sum()
    um = d["user_minutes_lost"].sum()
    return dict(
        incidents=len(d),
        downtime_hours=round(d["duration_min"].sum() / 60, 1),
        user_weighted_availability=round((1 - um / (total_users * period_min)) * 100, 4) if total_users else np.nan,
        mean_site_availability=round(sm["availability_pct"].mean(), 4),
        mttd=round(d["ttd_min"].mean(), 1) if len(d) else 0,
        mttr=round(d["duration_min"].mean(), 1) if len(d) else 0,
        cost=round(d["est_cost_usd"].sum(), 0),
        sla_breaches=int((sm["sla_met"] == "No").sum()),
        critical=int((d["severity_level"] == "Critical").sum()),
        sla=sla, period_days=round(period_min / 1440, 1),
    )


def build_graph(extra_sites=(), with_backup=False):
    G = nx.Graph()
    for s, v in SITES.items():
        G.add_node(s, tier=v[0], users=v[2], pos=v[3])
    G.add_edges_from(LINKS)
    for i, s in enumerate(extra_sites):  # uploaded sites hang off CORE-HQ on an outer ring
        ang = 2 * np.pi * i / max(len(extra_sites), 1)
        G.add_node(s, tier="Uploaded Site", users=DEFAULT_UPLOAD_USERS, pos=(5 * np.cos(ang), 5 * np.sin(ang)))
        G.add_edge("CORE-HQ", s)
    if with_backup:
        G.add_edges_from(BACKUP_LINKS)
    return G


def impact_of_failure(G, failed_nodes, failed_links, root="CORE-HQ"):
    H = G.copy()
    H.remove_edges_from([e for e in failed_links if H.has_edge(*e)])
    H.remove_nodes_from([n for n in failed_nodes if n in H])
    if root not in H:
        isolated = set(H.nodes)
    else:
        isolated = set(H.nodes) - nx.node_connected_component(H, root)
    return isolated


def topology_figure(G, failed_nodes=(), failed_links=(), isolated=(), backup=False, title="Network Topology"):
    pos = nx.get_node_attributes(G, "pos")
    fig = go.Figure()
    backup_set = {tuple(sorted(e)) for e in BACKUP_LINKS}
    failed_set = {tuple(sorted(e)) for e in failed_links}
    for u, v in G.edges():
        key = tuple(sorted((u, v)))
        color, dash, width = "#8a94a6", "solid", 2
        if key in backup_set and backup:
            color, dash = "#0B4FD8", "dot"
        if key in failed_set:
            color, dash, width = "#D62828", "dash", 4
        fig.add_trace(go.Scatter(x=[pos[u][0], pos[v][0]], y=[pos[u][1], pos[v][1]], mode="lines",
                                 line=dict(color=color, width=width, dash=dash), hoverinfo="skip", showlegend=False))
    tier_sym = {"Core": "star", "Data Center": "square", "Encryption Gateway": "diamond",
                "Secure Enclave": "hexagon", "Remote Site": "circle", "Uploaded Site": "circle-open"}
    for n in G.nodes():
        x, y = pos[n]
        tier = G.nodes[n]["tier"]
        if n in failed_nodes:
            col, state = "#D62828", "FAILED"
        elif n in isolated:
            col, state = "#F07B1D", "ISOLATED"
        else:
            col, state = "#2E9E5B", "OK"
        fig.add_trace(go.Scatter(
            x=[x], y=[y], mode="markers+text", text=[n], textposition="bottom center",
            marker=dict(size=30 if tier == "Core" else 24, color=col, symbol=tier_sym.get(tier, "circle"),
                        line=dict(color="white", width=2)),
            hovertext=f"<b>{n}</b><br>Tier: {tier}<br>Users: {G.nodes[n]['users']:,}<br>State: {state}",
            hoverinfo="text", showlegend=False))
    for lbl, col in [("OK", "#2E9E5B"), ("Failed", "#D62828"), ("Isolated (no path to core)", "#F07B1D")]:
        fig.add_trace(go.Scatter(x=[None], y=[None], mode="markers", marker=dict(size=12, color=col), name=lbl))
    if backup:
        fig.add_trace(go.Scatter(x=[None], y=[None], mode="lines", line=dict(color="#0B4FD8", dash="dot"),
                                 name="Backup link"))
    fig.update_layout(title=title, height=520, plot_bgcolor="white", margin=dict(l=10, r=10, t=50, b=10),
                      xaxis=dict(visible=False), yaxis=dict(visible=False, scaleanchor="x"),
                      legend=dict(orientation="h", y=-0.05))
    return fig


# ---------------------------------------------------------------------------
# 6. DIAGRAMS (Graphviz DOT - rendered in the browser by Streamlit)
# ---------------------------------------------------------------------------
def lifecycle_dot(ttd=None, ttr=None):
    ttd_l = f"TTD approx. {ttd:.0f} min" if ttd is not None else "TTD"
    ttr_l = f"TTR approx. {ttr:.0f} min" if ttr is not None else "TTR"
    return f"""
digraph G {{
  rankdir=LR; node [shape=box, style="rounded,filled", fontname=Helvetica, fontsize=11];
  A [label="1. Failure starts\\n(start_time)", fillcolor="#FDE2E1"];
  B [label="2. Detected\\n(detect_time)", fillcolor="#FFF3CD"];
  C [label="3. Diagnose &\\nmitigate", fillcolor="#E2ECFF"];
  D [label="4. Restored\\n(restore_time)", fillcolor="#DFF5E6"];
  E [label="5. Review &\\nprevent", fillcolor="#EFEFEF"];
  A -> B [label="{ttd_l}", color="#D62828", fontcolor="#D62828"];
  B -> C [label="{ttr_l}", color="#0B4FD8", fontcolor="#0B4FD8"];
  C -> D [color="#0B4FD8"];
  D -> E [style=dashed];
  A -> D [label="Outage Duration = TTD + TTR", style=dotted, constraint=false, color="#555555"];
}}"""


def case_dot(name, c):
    def esc(s):
        return s.replace('"', "'")
    return f"""
digraph G {{
  rankdir=LR; node [shape=box, style="rounded,filled", fontname=Helvetica, fontsize=10, width=1.8];
  c [label="CAUSE\\n{esc(c['causes'][0])}", fillcolor="#FDE2E1"];
  s [label="SYMPTOM\\n{esc(c['symptom'])}", fillcolor="#FFF3CD"];
  d [label="DETECTION SIGNAL\\n{esc(c['detection'])}", fillcolor="#FFE8CC"];
  a [label="APP ANALYSIS\\n{esc(c['analysis'])}", fillcolor="#E2ECFF"];
  m [label="MITIGATION\\n{esc(c['mitigation'])}", fillcolor="#DFF5E6"];
  c -> s -> d -> a -> m;
}}"""


def architecture_dot():
    return """
digraph G {
  rankdir=LR; node [shape=box, style="rounded,filled", fontname=Helvetica, fontsize=11, fillcolor="#E2ECFF"];
  subgraph cluster_in { label="1. DATA IN"; style=dashed; color="#0B4FD8";
    syn [label="Synthetic generator\\n(random, seeded)"]; up [label="Your CSV / Excel\\nupload"]; }
  map [label="2. Column mapping\\n& validation"];
  calc [label="3. Metric engine\\nTTD | TTR | MTBF\\nAvailability | Severity"];
  topo [label="4. Topology graph\\nisolation analysis"];
  viz [label="5. Charts, diagrams\\n& case explanations"];
  exp [label="6. Export\\nPDF | Word | TXT | CSV", fillcolor="#DFF5E6"];
  syn -> calc; up -> map -> calc; calc -> topo; calc -> viz; topo -> viz; viz -> exp;
}"""


# ---------------------------------------------------------------------------
# 7. EXPORT BUILDERS
# ---------------------------------------------------------------------------
def mpl_charts(d, sm, tm, sla):
    """Return list of (title, PNG bytes) for PDF / Word reports."""
    out = []
    # Availability by site
    fig, ax = plt.subplots(figsize=(8, 3.6))
    s2 = sm.sort_values("availability_pct")
    cols = ["#D62828" if v == "No" else "#2E9E5B" for v in s2["sla_met"]]
    ax.barh(s2["site"], s2["availability_pct"], color=cols)
    ax.axvline(sla, color="#0B4FD8", ls="--", label=f"SLA target {sla}%")
    ax.set_xlim(max(min(s2["availability_pct"].min() - 0.2, sla - 0.2), 90), 100.02)
    ax.set_xlabel("Availability %")
    ax.legend(loc="lower right", fontsize=8)
    ax.set_title("Availability by Site (red = SLA breached)")
    fig.tight_layout()
    out.append(("Availability by Site", _png(fig)))
    if not tm.empty:
        fig, ax = plt.subplots(figsize=(8, 3.6))
        t2 = tm.sort_values("incidents")
        ax.barh(t2["outage_type"], t2["incidents"], color="#0B4FD8")
        ax.set_xlabel("Incidents")
        ax.set_title("Incidents by Outage Type")
        fig.tight_layout()
        out.append(("Incidents by Outage Type", _png(fig)))
        fig, ax = plt.subplots(figsize=(8, 3.6))
        ax.bar(range(len(tm)), tm["mttd_min"], label="MTTD (min)", color="#F07B1D")
        ax.bar(range(len(tm)), tm["mttr_min"] - tm["mttd_min"], bottom=tm["mttd_min"],
               label="Remaining restore time (min)", color="#0B4FD8")
        ax.set_xticks(range(len(tm)))
        ax.set_xticklabels([t[:18] for t in tm["outage_type"]], rotation=30, ha="right", fontsize=7)
        ax.set_ylabel("Minutes")
        ax.set_title("Average Outage Duration split into Detect vs Restore")
        ax.legend(fontsize=8)
        fig.tight_layout()
        out.append(("Detect vs Restore Time", _png(fig)))
    return out


def _png(fig):
    b = io.BytesIO()
    fig.savefig(b, format="png", dpi=150)
    plt.close(fig)
    b.seek(0)
    return b.getvalue()


def text_report(k, d, sm, tm, source_label):
    L = []
    L.append("=" * 78)
    L.append(APP_NAME.upper())
    L.append(APP_TAGLINE)
    L.append(DEVELOPER)
    L.append(f"Generated: {dt.datetime.now():%Y-%m-%d %H:%M}   |   Data source: {source_label}")
    L.append("NOTICE: Synthetic / user-supplied data only. Not connected to any real classified network.")
    L.append("=" * 78)
    L.append("\nEXECUTIVE SUMMARY")
    L.append(f"  Analysis period ............ {k['period_days']} days")
    L.append(f"  Total incidents ............ {k['incidents']}  (Critical: {k['critical']})")
    L.append(f"  Total outage time .......... {k['downtime_hours']} hours")
    L.append(f"  User-weighted availability . {k['user_weighted_availability']}%")
    L.append(f"  Mean site availability ..... {k['mean_site_availability']}%  (SLA target {k['sla']}%)")
    L.append(f"  MTTD / MTTR ................ {k['mttd']} min / {k['mttr']} min")
    L.append(f"  Sites breaching SLA ........ {k['sla_breaches']}")
    L.append(f"  Estimated cost ............. ${k['cost']:,.0f}")
    L.append("\nSITE METRICS")
    L.append(sm[["site", "incidents", "downtime_min", "availability_pct", "mtbf_hours", "mttr_min",
                 "error_budget_used_pct", "sla_met"]].to_string(index=False))
    if not tm.empty:
        L.append("\nOUTAGE TYPE METRICS")
        L.append(tm[["outage_type", "incidents", "share_pct", "mttd_min", "mttr_min", "est_cost_usd",
                     "avg_severity"]].to_string(index=False))
    L.append("\nOUTAGE CASES - PROBLEM & HOW IT IS ADDRESSED")
    for name in tm["outage_type"] if not tm.empty else []:
        c = OUTAGE_CASES.get(name)
        if c:
            L.append(f"\n* {name}\n  Problem: {c['problem']}\n  How addressed: {c['analysis']}. {c['mitigation']}.")
    L.append("\nTOP 15 INCIDENTS BY SEVERITY")
    top = d.sort_values("severity_score", ascending=False).head(15)
    L.append(top[["incident_id", "site", "outage_type", "duration_min", "users_affected", "severity_score",
                  "severity_level"]].to_string(index=False))
    L.append("\nFIELD & FORMULA GUIDE")
    for name, f, e in FIELD_DOCS:
        L.append(f"- {name}\n    Formula: {f}\n    Meaning: {e}")
    return "\n".join(L)


def docx_report(k, d, sm, tm, charts, source_label):
    doc = Document()
    blue = RGBColor(0x0B, 0x4F, 0xD8)
    p = doc.add_paragraph()
    r = p.add_run(APP_NAME)
    r.bold, r.font.size, r.font.color.rgb = True, Pt(22), blue
    p = doc.add_paragraph()
    r = p.add_run(DEVELOPER)
    r.bold, r.font.size, r.font.color.rgb = True, Pt(13), blue
    doc.add_paragraph(APP_TAGLINE).italic = True
    doc.add_paragraph(f"Generated {dt.datetime.now():%Y-%m-%d %H:%M} | Data source: {source_label}")
    doc.add_paragraph("Notice: synthetic or user-supplied data only. Not connected to any real classified network.")

    doc.add_heading("1. Executive Summary", level=1)
    rows = [("Analysis period", f"{k['period_days']} days"), ("Total incidents", f"{k['incidents']} ({k['critical']} critical)"),
            ("Total outage time", f"{k['downtime_hours']} h"),
            ("User-weighted availability", f"{k['user_weighted_availability']}%"),
            ("Mean site availability", f"{k['mean_site_availability']}% (target {k['sla']}%)"),
            ("MTTD / MTTR", f"{k['mttd']} / {k['mttr']} min"), ("Sites breaching SLA", str(k["sla_breaches"])),
            ("Estimated cost", f"${k['cost']:,.0f}")]
    _docx_table(doc, ["Metric", "Value"], rows)

    doc.add_heading("2. Charts", level=1)
    for title, png in charts:
        doc.add_paragraph(title).runs[0].bold = True
        doc.add_picture(io.BytesIO(png), width=Inches(6.3))

    doc.add_heading("3. Site Metrics", level=1)
    cols = ["site", "incidents", "downtime_min", "availability_pct", "mtbf_hours", "mttr_min", "error_budget_used_pct", "sla_met"]
    _docx_table(doc, cols, sm[cols].astype(str).values.tolist(), small=True)

    if not tm.empty:
        doc.add_heading("4. Outage Types", level=1)
        cols = ["outage_type", "incidents", "share_pct", "mttd_min", "mttr_min", "est_cost_usd", "avg_severity"]
        _docx_table(doc, cols, tm[cols].astype(str).values.tolist(), small=True)
        doc.add_heading("5. Outage Cases - Problem & How It Is Addressed", level=1)
        for name in tm["outage_type"]:
            c = OUTAGE_CASES.get(name)
            if not c:
                continue
            doc.add_heading(name, level=2)
            doc.add_paragraph(f"Problem: {c['problem']}")
            doc.add_paragraph(f"How the app detects it: {c['detection']}")
            doc.add_paragraph(f"How the app analyses it: {c['analysis']}")
            doc.add_paragraph(f"Recommended mitigation: {c['mitigation']}")
            for step in c["playbook"]:
                doc.add_paragraph(step, style="List Number")

    doc.add_heading("6. Top 15 Incidents by Severity", level=1)
    cols = ["incident_id", "site", "outage_type", "duration_min", "users_affected", "severity_score", "severity_level"]
    top = d.sort_values("severity_score", ascending=False).head(15)
    _docx_table(doc, cols, top[cols].astype(str).values.tolist(), small=True)

    doc.add_heading("7. Field & Formula Guide", level=1)
    _docx_table(doc, ["Field", "Formula", "Plain-English meaning"], FIELD_DOCS, small=True)
    b = io.BytesIO()
    doc.save(b)
    return b.getvalue()


def _docx_table(doc, header, rows, small=False):
    t = doc.add_table(rows=1, cols=len(header))
    t.style = "Light Grid Accent 1"
    for i, h in enumerate(header):
        t.rows[0].cells[i].text = str(h)
    for row in rows:
        cells = t.add_row().cells
        for i, v in enumerate(row):
            cells[i].text = str(v)
    if small:
        for row in t.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    for run in para.runs:
                        run.font.size = Pt(7.5)


def pdf_report(k, d, sm, tm, charts, source_label):
    b = io.BytesIO()
    doc = SimpleDocTemplate(b, pagesize=letter, leftMargin=0.6 * inch, rightMargin=0.6 * inch,
                            topMargin=0.6 * inch, bottomMargin=0.6 * inch, title=APP_NAME)
    ss = getSampleStyleSheet()
    h_title = ParagraphStyle("t", parent=ss["Title"], textColor=colors.HexColor(BLUE), fontName="Helvetica-Bold")
    h_sub = ParagraphStyle("s", parent=ss["Heading3"], textColor=colors.HexColor(BLUE), fontName="Helvetica-Bold",
                           alignment=1)
    body = ParagraphStyle("b", parent=ss["BodyText"], fontSize=9, leading=12)
    cell = ParagraphStyle("c", parent=ss["BodyText"], fontSize=7, leading=8.5)
    el = [Paragraph(APP_NAME, h_title), Paragraph(DEVELOPER, h_sub),
          Paragraph(f"<i>{APP_TAGLINE}</i>", body),
          Paragraph(f"Generated {dt.datetime.now():%Y-%m-%d %H:%M} | Data source: {source_label}", body),
          Paragraph("<b>Notice:</b> synthetic or user-supplied data only. Not connected to any real classified network.", body),
          Spacer(1, 10), Paragraph("1. Executive Summary", ss["Heading2"])]

    def tbl(header, rows, widths=None):
        data = [[Paragraph(f"<b>{h}</b>", cell) for h in header]] + \
               [[Paragraph(str(v), cell) for v in r] for r in rows]
        t = Table(data, colWidths=widths, repeatRows=1)
        t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#DCE6FB")),
                               ("GRID", (0, 0), (-1, -1), 0.3, colors.grey),
                               ("VALIGN", (0, 0), (-1, -1), "TOP")]))
        return t

    el.append(tbl(["Metric", "Value"], [
        ("Analysis period", f"{k['period_days']} days"), ("Total incidents", f"{k['incidents']} ({k['critical']} critical)"),
        ("Total outage time", f"{k['downtime_hours']} h"),
        ("User-weighted availability", f"{k['user_weighted_availability']}%"),
        ("Mean site availability", f"{k['mean_site_availability']}% (target {k['sla']}%)"),
        ("MTTD / MTTR", f"{k['mttd']} / {k['mttr']} min"), ("Sites breaching SLA", k["sla_breaches"]),
        ("Estimated cost", f"${k['cost']:,.0f}")], widths=[2.5 * inch, 4 * inch]))
    el.append(Paragraph("2. Charts", ss["Heading2"]))
    for title, png in charts:
        el.append(RLImage(io.BytesIO(png), width=7 * inch, height=3.15 * inch))
        el.append(Spacer(1, 6))
    el.append(PageBreak())
    el.append(Paragraph("3. Site Metrics", ss["Heading2"]))
    cols = ["site", "incidents", "downtime_min", "availability_pct", "mtbf_hours", "mttr_min", "error_budget_used_pct", "sla_met"]
    el.append(tbl(cols, sm[cols].values.tolist()))
    if not tm.empty:
        el.append(Paragraph("4. Outage Types", ss["Heading2"]))
        cols = ["outage_type", "incidents", "share_pct", "mttd_min", "mttr_min", "est_cost_usd", "avg_severity"]
        el.append(tbl(cols, tm[cols].values.tolist()))
        el.append(Paragraph("5. Outage Cases - Problem & How It Is Addressed", ss["Heading2"]))
        for name in tm["outage_type"]:
            c = OUTAGE_CASES.get(name)
            if not c:
                continue
            el.append(Paragraph(f"<b>{name}</b>", body))
            el.append(Paragraph(f"<b>Problem:</b> {c['problem']}", body))
            el.append(Paragraph(f"<b>Detection:</b> {c['detection']}. <b>Analysis:</b> {c['analysis']}. "
                                f"<b>Mitigation:</b> {c['mitigation']}.", body))
            el.append(Spacer(1, 5))
    el.append(Paragraph("6. Top 15 Incidents by Severity", ss["Heading2"]))
    cols = ["incident_id", "site", "outage_type", "duration_min", "users_affected", "severity_score", "severity_level"]
    el.append(tbl(cols, d.sort_values("severity_score", ascending=False).head(15)[cols].values.tolist()))
    el.append(PageBreak())
    el.append(Paragraph("7. Field & Formula Guide", ss["Heading2"]))
    el.append(tbl(["Field", "Formula", "Plain-English meaning"], FIELD_DOCS,
                  widths=[1.5 * inch, 2.9 * inch, 2.9 * inch]))

    def footer(canvas, _doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 7)
        canvas.drawString(0.6 * inch, 0.35 * inch, f"{APP_NAME} | {DEVELOPER} | SYNTHETIC SIMULATION")
        canvas.drawRightString(7.9 * inch, 0.35 * inch, f"Page {_doc.page}")
        canvas.restoreState()

    doc.build(el, onFirstPage=footer, onLaterPages=footer)
    return b.getvalue()


# ---------------------------------------------------------------------------
# 8. STREAMLIT UI
# ---------------------------------------------------------------------------
def explain(title, body):
    with st.expander(f"{title}"):
        st.markdown(body)


def formula_box(*names):
    for n in names:
        f, e = FORMULA_LOOKUP[n]
        st.markdown(f"**{n}** - `{f}`  \n{e}")


def main():
    st.set_page_config(page_title=APP_NAME, layout="wide")
    st.markdown(f"""
        <div style="padding:6px 0 2px 0">
          <h1 style="color:{BLUE};font-weight:800;margin-bottom:0">{APP_NAME}</h1>
          <h3 style="color:{BLUE};font-weight:700;margin-top:4px">{DEVELOPER}</h3>
          <p style="color:#555;margin-top:-6px">{APP_TAGLINE}</p>
        </div>""", unsafe_allow_html=True)
    st.warning("**Simulation notice:** every site, device, incident and number in this app is synthetic (or comes "
               "from a file you upload). The app does not reproduce, model, connect to, or access any real "
               "classified network or NSA infrastructure.")

    # ---------------- Sidebar ----------------
    with st.sidebar:
        st.header("Simulation Controls")
        source = st.radio("Data source", ["Synthetic (generated)", "Upload real data (CSV / Excel)"])
        st.subheader("Business settings")
        sla = st.number_input("SLA availability target (%)", 90.0, 99.999, 99.9, 0.01, format="%.3f",
                              help="Allowed downtime = (1 - SLA) x period minutes")
        cost_per_min = st.number_input("Cost / mission impact per minute ($)", 0.0, 1e6, 2500.0, 100.0,
                                       help="Estimated Cost = Duration x this value x Criticality")
        if source.startswith("Synthetic"):
            st.subheader("Synthetic generator")
            seed = st.number_input("Random seed (same seed = same data)", 0, 99999, 42)
            days = st.slider("Simulation period (days)", 7, 90, 30)
            n_inc = st.slider("Number of incidents", 10, 400, 50)
            start_date = st.date_input("Period start", dt.date(2026, 1, 1))
        st.caption(DEVELOPER)

    # ---------------- Load data ----------------
    issues = []
    if source.startswith("Synthetic"):
        raw = generate_synthetic(int(seed), days, n_inc, start_date)
        period_start = pd.Timestamp(start_date)
        period_end = period_start + pd.Timedelta(days=days)
        source_label = f"Synthetic (seed {seed}, {days} days, {n_inc} incidents)"
    else:
        raw, period_start, period_end, source_label = None, None, None, "Uploaded file"
        up = st.sidebar.file_uploader("Upload incident file", type=["csv", "xlsx", "xls"])
        if up is not None:
            try:
                file_df = read_upload(up)
                source_label = f"Uploaded file: {up.name}"
                with st.sidebar.expander("Column mapping", expanded=True):
                    opts = ["- not provided -"] + list(file_df.columns)
                    mapping = {}
                    for col in REQUIRED_COLS + list(OPTIONAL_COLS):
                        default = opts.index(col) if col in opts else 0
                        mapping[col] = st.selectbox(f"{col}{' *' if col in REQUIRED_COLS else ''}", opts,
                                                    index=default, key=f"map_{col}")
                raw, issues = clean_uploaded(file_df, mapping)
                if raw is not None and len(raw):
                    period_start = raw["start_time"].min().floor("D")
                    period_end = max(raw["restore_time"].max().ceil("D"), period_start + pd.Timedelta(days=1))
            except Exception as ex:  # noqa: BLE001
                issues = [f"Could not read file: {ex}"]

    if raw is None or len(raw) == 0:
        st.info("Upload a CSV or Excel file in the sidebar (see the **Upload Real Data** tab for the format), "
                "or switch the data source back to **Synthetic**.")
        for i in issues:
            st.error(i)
        tab_upload_guide()
        return
    for i in issues:
        (st.success if "loaded successfully" in i else st.warning)(i)

    d = enrich_incidents(raw, cost_per_min)
    sm = site_metrics(d, period_start, period_end, sla)
    tm = type_metrics(d)
    k = overall_kpis(d, sm, period_start, period_end, sla)
    extra_sites = [s for s in d["site"].unique() if s not in SITES]
    days_span = max(1, int(round((period_end - period_start).total_seconds() / 86400)))
    tele = generate_telemetry(d, tuple(sm["site"]), period_start, days_span,
                              int(seed) if source.startswith("Synthetic") else 7)

    tabs = st.tabs(["Overview & Guide", "Dashboard", "Outage Cases", "Topology & What-If",
                    "Telemetry", "Formula Guide", "Upload Real Data", "Export Results"])

    with tabs[0]:
        tab_overview(d)
    with tabs[1]:
        tab_dashboard(d, sm, tm, k, sla)
    with tabs[2]:
        tab_cases(d)
    with tabs[3]:
        tab_topology(d, extra_sites, cost_per_min, sla, period_start, period_end)
    with tabs[4]:
        tab_telemetry(d, tele)
    with tabs[5]:
        tab_formulas(d, sm, sla, cost_per_min)
    with tabs[6]:
        tab_upload_guide()
    with tabs[7]:
        tab_export(k, d, sm, tm, sla, source_label)


def tab_overview(d):
    st.subheader("What this application does")
    st.markdown("""
Large classified-style enterprise networks are split into **segmented enclaves** that reach a central core only
through **encryption gateways**, with data centers and remote sites around them. When something breaks, operators
must answer four questions fast:

1. **What broke and where?** -> *Dashboard* and *Outage Cases* tabs
2. **Who is cut off?** -> *Topology & What-If* tab (graph search for sites with no path to the core)
3. **How bad is it?** -> Severity Score, User-Minutes Lost, Availability vs SLA, Estimated Cost
4. **How do we stop it happening again?** -> per-case playbooks, Pareto of root causes, redundancy what-if

This simulator generates a realistic but **fully fictional** incident history (or reads your own), calculates
every metric with a clearly explained formula, draws diagrams for each case, and exports the results.
""")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**How data flows through the app**")
        st.graphviz_chart(architecture_dot())
    with c2:
        st.markdown("**Life of an outage (with your data's averages)**")
        st.graphviz_chart(lifecycle_dot(d["ttd_min"].mean(), d["ttr_min"].mean()))
    st.markdown("""
#### How to use it (3 steps)
1. **Choose data** in the sidebar - keep *Synthetic*, or switch to *Upload real data* and pick your CSV/Excel file.
2. **Explore** the tabs. Every number has an explanation; the *Formula Guide* tab shows each formula with a worked example.
3. **Export** from the last tab as PDF, Word, Text or CSV.
""")
    st.markdown("#### The eight simulated outage cases")
    cols = st.columns(4)
    for i, (name, c) in enumerate(OUTAGE_CASES.items()):
        with cols[i % 4]:
            st.markdown(f"**{name}**  \n<small>{c['symptom']}</small>", unsafe_allow_html=True)


def tab_dashboard(d, sm, tm, k, sla):
    st.subheader("Operational Dashboard")
    c = st.columns(4)
    c[0].metric("Incidents", k["incidents"], f"{k['critical']} critical", delta_color="inverse",
                help="Count of incident rows in the period")
    c[1].metric("User-weighted availability", f"{k['user_weighted_availability']:.3f}%",
                help=FORMULA_LOOKUP["User-Weighted Network Availability"][0])
    c[2].metric("MTTD", f"{k['mttd']} min", help=FORMULA_LOOKUP["MTTD (Mean Time to Detect)"][0])
    c[3].metric("MTTR", f"{k['mttr']} min", help=FORMULA_LOOKUP["MTTR (Mean Time to Restore)"][0])
    c = st.columns(4)
    c[0].metric("Total outage time", f"{k['downtime_hours']} h", help="Sum of Duration of all incidents / 60")
    c[1].metric("Mean site availability", f"{k['mean_site_availability']:.3f}%", help="Average of each site's Availability %")
    c[2].metric("Sites breaching SLA", k["sla_breaches"], help=f"Sites with Availability < {sla}%")
    c[3].metric("Estimated cost", f"${k['cost']:,.0f}", help=FORMULA_LOOKUP["Estimated Cost"][0])
    explain("How are these KPIs calculated?", "\n\n".join(
        f"**{n}** - `{FORMULA_LOOKUP[n][0]}`  \n{FORMULA_LOOKUP[n][1]}" for n in
        ["User-Weighted Network Availability", "MTTD (Mean Time to Detect)", "MTTR (Mean Time to Restore)",
         "Availability %", "Estimated Cost"]))

    st.markdown("#### Availability by site vs SLA target")
    s2 = sm.sort_values("availability_pct")
    fig = px.bar(s2, x="availability_pct", y="site", orientation="h", color="sla_met",
                 color_discrete_map={"Yes": "#2E9E5B", "No": "#D62828"},
                 hover_data=["downtime_min", "allowed_downtime_min", "error_budget_used_pct", "incidents"],
                 labels={"availability_pct": "Availability %", "sla_met": "SLA met"})
    fig.add_vline(x=sla, line_dash="dash", line_color=BLUE, annotation_text=f"SLA {sla}%")
    fig.update_xaxes(range=[max(min(s2["availability_pct"].min() - 0.1, sla - 0.1), 90), 100.01])
    st.plotly_chart(fig, width="stretch")
    st.caption("Read it: bars left of the blue line broke the SLA. Hover to see the downtime vs the allowed budget.")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Incidents by outage type")
        fig = px.bar(tm.sort_values("incidents"), x="incidents", y="outage_type", orientation="h",
                     color="avg_severity", color_continuous_scale="OrRd", labels={"outage_type": ""})
        st.plotly_chart(fig, width="stretch")
        st.caption("Longer bar = happens more often. Darker = more severe on average.")
    with c2:
        st.markdown("#### Severity mix")
        sev = d["severity_level"].value_counts().reindex(SEVERITY_LABELS).fillna(0).reset_index()
        sev.columns = ["level", "count"]
        fig = px.pie(sev, names="level", values="count", hole=0.5, color="level", color_discrete_map=SEV_COLORS)
        st.plotly_chart(fig, width="stretch")
        st.caption("Severity Score blends users, duration, packet loss and site criticality (see Formula Guide).")

    st.markdown("#### Outage timeline (Gantt)")
    fig = px.timeline(d, x_start="start_time", x_end="restore_time", y="site", color="outage_type",
                      hover_data=["incident_id", "duration_min", "users_affected", "severity_level"])
    fig.update_layout(height=430, legend=dict(orientation="h", y=-0.25))
    st.plotly_chart(fig, width="stretch")
    st.caption("Each bar is one outage, from start to restore. Stacks of bars on one row show a troubled site.")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Where is the pain? (avg severity, site x type)")
        hm = d.pivot_table(index="site", columns="outage_type", values="severity_score", aggfunc="mean")
        fig = px.imshow(hm, color_continuous_scale="OrRd", aspect="auto", text_auto=".0f")
        fig.update_xaxes(tickangle=35)
        st.plotly_chart(fig, width="stretch")
    with c2:
        st.markdown("#### Root-cause Pareto (fix the top causes first)")
        rc = d["root_cause"].value_counts().reset_index()
        rc.columns = ["root_cause", "count"]
        rc["cum_pct"] = rc["count"].cumsum() / rc["count"].sum() * 100
        fig = go.Figure()
        fig.add_bar(x=rc["root_cause"], y=rc["count"], name="Incidents", marker_color=BLUE)
        fig.add_scatter(x=rc["root_cause"], y=rc["cum_pct"], name="Cumulative %", yaxis="y2",
                        line=dict(color="#D62828"))
        fig.update_layout(yaxis2=dict(overlaying="y", side="right", range=[0, 105], title="Cumulative %"),
                          xaxis=dict(tickangle=40), legend=dict(orientation="h", y=1.12), height=450)
        st.plotly_chart(fig, width="stretch")
        st.caption("Pareto rule: the causes left of where the red line crosses ~80% create most incidents.")

    st.markdown("#### Detection vs restoration time by outage type")
    if not tm.empty:
        t2 = tm.copy()
        t2["restore_after_detect"] = t2["mttr_min"] - t2["mttd_min"]
        fig = go.Figure()
        fig.add_bar(y=t2["outage_type"], x=t2["mttd_min"], name="MTTD (time to notice)", orientation="h",
                    marker_color="#F07B1D")
        fig.add_bar(y=t2["outage_type"], x=t2["restore_after_detect"], name="Time to fix after noticing",
                    orientation="h", marker_color=BLUE)
        fig.update_layout(barmode="stack", xaxis_title="Average minutes", height=380,
                          legend=dict(orientation="h", y=-0.2))
        st.plotly_chart(fig, width="stretch")
        st.caption("Orange = wasted time before anyone noticed. Big orange bars -> improve monitoring for that case.")

    st.markdown("#### Site metrics table")
    st.dataframe(sm, width="stretch", hide_index=True)


def tab_cases(d):
    st.subheader("Outage Cases - each problem and how the app addresses it")
    st.markdown("Open a case to see the problem in plain language, a cause->fix flow diagram, its statistics "
                "from the current data, and a step-by-step response playbook.")
    known = [t for t in OUTAGE_CASES]
    others = sorted(set(d["outage_type"]) - set(known))
    for name in known:
        c = OUTAGE_CASES[name]
        sub = d[d["outage_type"] == name]
        with st.expander(f"{name}   -   {len(sub)} incident(s)"):
            c1, c2 = st.columns([1.1, 1])
            with c1:
                st.markdown(f"**The problem**  \n{c['problem']}")
                st.markdown(f"**Typical causes:** {', '.join(c['causes'])}")
                st.markdown(f"**How the app detects it:** {c['detection']}")
                st.markdown(f"**How the app analyses it:** {c['analysis']}")
                st.markdown(f"**How it is fixed:** {c['mitigation']}")
                st.info(f"**Metric that matters most:** {c['key_metric']}")
            with c2:
                st.markdown("**Response playbook**")
                for i, step in enumerate(c["playbook"], 1):
                    st.markdown(f"{i}. {step}")
            st.graphviz_chart(case_dot(name, c))
            if len(sub):
                m = st.columns(5)
                m[0].metric("Incidents", len(sub))
                m[1].metric("MTTD", f"{sub['ttd_min'].mean():.0f} min")
                m[2].metric("MTTR", f"{sub['duration_min'].mean():.0f} min")
                m[3].metric("User-minutes", f"{sub['user_minutes_lost'].sum():,.0f}")
                m[4].metric("Est. cost", f"${sub['est_cost_usd'].sum():,.0f}")
                g1, g2 = st.columns(2)
                with g1:
                    fig = px.bar(sub.groupby("site").size().reset_index(name="incidents"), x="site", y="incidents",
                                 title="Where it happened", color_discrete_sequence=[BLUE])
                    st.plotly_chart(fig, width="stretch", key=f"cs_{name}")
                with g2:
                    fig = px.scatter(sub, x="duration_min", y="users_affected", size="severity_score",
                                     color="severity_level", color_discrete_map=SEV_COLORS,
                                     hover_data=["incident_id", "site", "root_cause"],
                                     title="Impact: duration vs users (bubble = severity)")
                    st.plotly_chart(fig, width="stretch", key=f"cd_{name}")
            else:
                st.caption("No incidents of this type in the current data.")
    for name in others:
        sub = d[d["outage_type"] == name]
        with st.expander(f"{name} (custom type from uploaded data) - {len(sub)} incident(s)"):
            st.markdown("This outage type is not in the built-in case library, so the app applies the generic "
                        "metrics (TTD, TTR, availability, severity) without a tailored playbook.")
            st.dataframe(sub, width="stretch", hide_index=True)


def tab_topology(d, extra_sites, cost_per_min, sla, period_start, period_end):
    st.subheader("Network Topology & What-If Failure Simulator")
    st.markdown("""
The diagram is a **fictional** segmented network: a core, two data centers, two encryption gateways each fronting a
secure enclave, and remote sites. Pick something to fail and the app runs a **graph search** to find every site that
no longer has *any* path to `CORE-HQ` (marked **orange = isolated**). Turn on *redundant links* to see how a second
path changes the result.
""")
    G0 = build_graph(extra_sites)
    c1, c2 = st.columns([1, 2.2])
    with c1:
        failed_nodes = st.multiselect("Fail these sites / devices", list(G0.nodes), default=["GW-CRYPTO-1"])
        link_labels = [f"{u} <-> {v}" for u, v in G0.edges()]
        failed_lbl = st.multiselect("Cut these links", link_labels, default=[])
        failed_links = [tuple(x.split(" <-> ")) for x in failed_lbl]
        backup = st.toggle("Add redundant / backup links", value=False)
        dur = st.slider("Assumed outage duration (minutes)", 5, 720, 120, 5)
    G = build_graph(extra_sites, with_backup=backup)
    isolated = impact_of_failure(G, failed_nodes, failed_links)
    impacted = set(failed_nodes) | isolated
    users = sum(G.nodes[n]["users"] for n in impacted if n in G)
    crit = max([site_info(n)[1] for n in impacted], default=0)
    period_min = (period_end - period_start).total_seconds() / 60
    with c2:
        st.plotly_chart(topology_figure(G, failed_nodes, failed_links, isolated, backup,
                                        title="Simulated failure impact"), width="stretch")
    m = st.columns(4)
    m[0].metric("Sites failed + isolated", len(impacted))
    m[1].metric("Users cut off", f"{users:,}")
    m[2].metric("User-minutes lost", f"{users * dur:,}", help="Users cut off x assumed duration")
    m[3].metric("Est. cost", f"${dur * cost_per_min * crit:,.0f}", help="Duration x cost/min x highest criticality hit")
    avail_hit = dur / period_min * 100
    st.markdown(f"**Effect on availability:** this single event alone removes **{avail_hit:.3f} percentage points** "
                f"from each impacted site's availability over a {period_min / 1440:.0f}-day period "
                f"(SLA budget = {(1 - sla / 100) * period_min:.1f} min, so it uses "
                f"**{dur / ((1 - sla / 100) * period_min) * 100:.0f}%** of the budget).")
    if isolated:
        st.error(f"Isolated (no path to core): {', '.join(sorted(isolated))}")
    else:
        st.success("No other site lost its path to the core - the network routed around the failure.")
    explain("How is 'isolated' calculated?", """
The network is stored as a **graph** (sites = nodes, circuits = edges). The app removes the failed nodes and links,
then performs a **breadth-first search from `CORE-HQ`**. Any site the search cannot reach is *isolated*.

*Example:* `ENCLAVE-A` connects only through `GW-CRYPTO-1`. Fail that gateway and the search can no longer reach
`ENCLAVE-A`, so its users are counted as cut off. Turning on backup links adds `ENCLAVE-A <-> GW-CRYPTO-2`, the search
finds the alternate path, and the enclave stays online - this is the business case for redundancy.
""")
    st.markdown("#### Single-point-of-failure ranking")
    st.caption("For every site, the app fails it on its own and counts the users of all *other* sites that lose their path to the core.")
    rows = []
    for n in G.nodes:
        if n == "CORE-HQ":
            continue
        iso = impact_of_failure(G, [n], [])
        rows.append(dict(site=n, sites_isolated=len(iso), users_isolated=sum(G.nodes[x]["users"] for x in iso)))
    spof = pd.DataFrame(rows).sort_values("users_isolated", ascending=False)
    fig = px.bar(spof, x="site", y="users_isolated", color="sites_isolated", color_continuous_scale="OrRd",
                 title="Users cut off from the core if this one site fails")
    st.plotly_chart(fig, width="stretch")


def tab_telemetry(d, tele):
    st.subheader("Telemetry - latency, packet loss & utilization")
    st.markdown("Synthetic hourly measurements per site. Shaded bands are incidents; you can see how each outage "
                "type leaves a different 'fingerprint' (e.g. fiber cut = loss to 100%, congestion = latency + utilization spike, "
                "DNS failure = almost no change in loss).")
    site = st.selectbox("Site", sorted(tele["site"].unique()))
    metric = st.radio("Metric", ["latency_ms", "packet_loss_pct", "utilization_pct"], horizontal=True)
    t = tele[tele["site"] == site]
    fig = px.line(t, x="timestamp", y=metric, title=f"{site} - {metric}")
    sub = d[d["site"] == site].head(60)
    for _, r in sub.iterrows():
        fig.add_vrect(x0=r["start_time"], x1=r["restore_time"], fillcolor=SEV_COLORS.get(r["severity_level"], "red"),
                      opacity=0.18, line_width=0)
    if metric == "latency_ms":
        fig.update_yaxes(type="log", title="latency (ms, log scale)")
    st.plotly_chart(fig, width="stretch")
    st.caption("Band colour = severity level (green Low -> red Critical).")
    st.dataframe(sub[["incident_id", "outage_type", "start_time", "restore_time", "packet_loss_pct", "latency_ms",
                      "severity_level"]], width="stretch", hide_index=True)


def tab_formulas(d, sm, sla, cost_per_min):
    st.subheader("Field & Formula Guide - in plain English")
    st.markdown("Every calculated column in the app is listed below with its formula and meaning. "
                "Further down, the app works each formula through with a **real row from your current data**.")
    st.dataframe(pd.DataFrame(FIELD_DOCS, columns=["Field", "Formula", "What it means"]), width="stretch",
                 hide_index=True)
    st.markdown("#### Worked example (one incident)")
    r = d.sort_values("severity_score", ascending=False).iloc[0]
    U = min(r["users_affected"] / 1000, 1)
    D = min(r["duration_min"] / 240, 1)
    P = r["packet_loss_pct"] / 100
    C = r["criticality"]
    st.markdown(f"""
Incident **{r['incident_id']}** at **{r['site']}** - *{r['outage_type']}*

| Step | Calculation | Result |
|---|---|---|
| TTD | {r['detect_time']:%H:%M} - {r['start_time']:%H:%M} | **{r['ttd_min']} min** |
| TTR | {r['restore_time']:%H:%M} - {r['detect_time']:%H:%M} | **{r['ttr_min']} min** |
| Duration | TTD + TTR = {r['ttd_min']} + {r['ttr_min']} | **{r['duration_min']} min** |
| User-minutes | {r['users_affected']:,} users x {r['duration_min']} min | **{r['user_minutes_lost']:,.0f}** |
| Estimated cost | {r['duration_min']} x ${cost_per_min:,.0f} x {C:.2f} | **${r['est_cost_usd']:,.0f}** |
| U (users factor) | min({r['users_affected']} / 1000, 1) | {U:.2f} |
| D (duration factor) | min({r['duration_min']} / 240, 1) | {D:.2f} |
| P (loss factor) | {r['packet_loss_pct']} / 100 | {P:.2f} |
| C (criticality) | tier weight | {C:.2f} |
| Severity score | 100 x (0.35x{U:.2f} + 0.30x{D:.2f} + 0.20x{P:.2f} + 0.15x{C:.2f}) | **{r['severity_score']} -> {r['severity_level']}** |
""")
    st.markdown("#### Worked example (one site)")
    s = sm.sort_values("incidents", ascending=False).iloc[0]
    period_min = s["allowed_downtime_min"] / (1 - sla / 100)
    st.markdown(f"""
Site **{s['site']}** over a period of **{period_min:,.0f} minutes** ({period_min / 1440:.0f} days):

| Step | Calculation | Result |
|---|---|---|
| Downtime | merged minutes of {s['incidents']} incidents | **{s['downtime_min']} min** |
| Availability | ({period_min:,.0f} - {s['downtime_min']}) / {period_min:,.0f} x 100 | **{s['availability_pct']}%** |
| MTBF | ({period_min:,.0f} - {s['downtime_min']}) / 60 / {s['incidents']} | **{s['mtbf_hours']} h** |
| Allowed downtime | (1 - {sla}/100) x {period_min:,.0f} | **{s['allowed_downtime_min']} min** |
| Error budget used | {s['downtime_min']} / {s['allowed_downtime_min']} x 100 | **{s['error_budget_used_pct']}%** |
| SLA met? | {s['availability_pct']}% >= {sla}% ? | **{s['sla_met']}** |
""")
    st.markdown("#### Visual: how the Severity Score is built")
    parts = pd.DataFrame({"component": ["Users (35%)", "Duration (30%)", "Packet loss (20%)", "Criticality (15%)"],
                          "points": [35 * U, 30 * D, 20 * P, 15 * C]})
    fig = px.bar(parts, x="points", y="component", orientation="h", text_auto=".1f",
                 title=f"{r['incident_id']}: {r['severity_score']} points total", color_discrete_sequence=[BLUE])
    fig.update_xaxes(range=[0, 36])
    st.plotly_chart(fig, width="stretch")
    st.markdown("#### Visual: what an SLA target means in minutes")
    targets = [99.0, 99.5, 99.9, 99.95, 99.99]
    fig = px.bar(x=[f"{t}%" for t in targets], y=[(1 - t / 100) * 30 * 1440 for t in targets],
                 labels={"x": "SLA target", "y": "Allowed downtime per 30 days (min)"}, text_auto=".1f",
                 color_discrete_sequence=[BLUE])
    st.plotly_chart(fig, width="stretch")


def tab_upload_guide():
    st.subheader("How to upload your own (real) data")
    st.markdown("""
**Step 1 - Prepare a file.** CSV (`.csv`) or Excel (`.xlsx` / `.xls`), one row per incident. Column names do *not*
have to match exactly; you map them in Step 3.

**Step 2 - Upload.** In the sidebar, choose **Data source -> Upload real data**, then drag the file onto the uploader.

**Step 3 - Map columns.** A *Column mapping* box appears in the sidebar. For each field the app needs, pick the
matching column from your file. Fields marked `*` are required.

**Step 4 - Check the messages.** The app tells you how many rows loaded and fixes or drops bad rows (for example, a
restore time before the start time). Every tab then recalculates from your data.

| Field | Required? | Format / example | Used for |
|---|---|---|---|
| incident_id | Yes | `INC-1001` | Identifying each row |
| site | Yes | `DC-EAST` or any name | Grouping, availability, topology |
| outage_type | Yes | One of the 8 case names (others allowed) | Case explanations & playbooks |
| start_time | Yes | `2026-03-01 08:00` | TTD, duration, timeline |
| detect_time | Yes | `2026-03-01 08:06` (blank -> start_time) | TTD, TTR |
| restore_time | Yes | `2026-03-01 08:48` | TTR, duration, availability |
| users_affected | Yes | `1200` | User-minutes, severity |
| component | optional | `Core switch` | Context |
| packet_loss_pct | optional | `0`-`100` (blank -> 0) | Severity, telemetry |
| latency_ms | optional | `240` | Telemetry |
| root_cause | optional | `Bad ACL rule` | Pareto chart |
| criticality | optional | `0`-`1` (blank -> tier default / 0.70) | Cost, severity |

**Tips**
- Use real outage-type names so you get the matching explanation and playbook (case names are in the *Outage Cases* tab).
- Sites not in the built-in diagram are drawn on an outer ring connected to `CORE-HQ`.
- The analysis period runs from the first day to the last day in your file.
- Only upload data you are authorised to use. **Never upload classified information** - this tool is not an accredited system.
""")
    tpl = upload_template()
    st.download_button("Download CSV template", tpl.to_csv(index=False).encode(), "classinet_upload_template.csv",
                       "text/csv")
    st.dataframe(tpl, width="stretch", hide_index=True)


def tab_export(k, d, sm, tm, sla, source_label):
    st.subheader("Export analysis results")
    st.markdown("""
| Format | What you get | Best for |
|---|---|---|
| **PDF** | Branded report: summary, 3 charts, site & type tables, case explanations, top incidents, formula guide | Briefings, archiving |
| **Word (.docx)** | Same content, fully editable | Adding your own commentary |
| **Text (.txt)** | Plain-text report | Email, ticket systems, low-bandwidth |
| **CSV** | Raw tables with every calculated column | Excel, BI tools, further analysis |
""")
    with st.spinner("Building reports..."):
        charts = mpl_charts(d, sm, tm, sla)
        pdf = pdf_report(k, d, sm, tm, charts, source_label)
        docx = docx_report(k, d, sm, tm, charts, source_label)
        txt = text_report(k, d, sm, tm, source_label)
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M")
    c = st.columns(4)
    c[0].download_button("PDF report", pdf, f"classinet_report_{stamp}.pdf", "application/pdf")
    c[1].download_button("Word report", docx, f"classinet_report_{stamp}.docx",
                         "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    c[2].download_button("Text report", txt.encode(), f"classinet_report_{stamp}.txt", "text/plain")
    c[3].download_button("Incidents CSV", d.to_csv(index=False).encode(), f"classinet_incidents_{stamp}.csv",
                         "text/csv")
    c = st.columns(4)
    c[0].download_button("Site metrics CSV", sm.to_csv(index=False).encode(), f"classinet_sites_{stamp}.csv", "text/csv")
    c[1].download_button("Outage-type CSV", tm.to_csv(index=False).encode(), f"classinet_types_{stamp}.csv", "text/csv")
    c[2].download_button("Formula guide CSV",
                         pd.DataFrame(FIELD_DOCS, columns=["field", "formula", "meaning"]).to_csv(index=False).encode(),
                         f"classinet_formulas_{stamp}.csv", "text/csv")
    with st.expander("Preview text report"):
        st.code(txt[:6000])


if __name__ == "__main__":
    main()
