

# KNet National Critical Infrastructure Cyber Resilience and Cascading Failure Detection Platform
# Developed by Randy Singh, Kalsnet (KNet) Consulting Group

# Single file demonstration application.
# Graph AI, Knowledge Graph, SIEM and SOAR, Digital Twin and Predictive Analytics.

# All synthetic assets, vendors and events are fictional.


import base64
import hashlib
import hmac
import io
import itertools
import json
import math
import os
import warnings
import zlib
from datetime import datetime, timezone

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import networkx as nx  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
import plotly.express as px  # noqa: E402
import plotly.graph_objects as go  # noqa: E402
import streamlit as st  # noqa: E402
from sklearn.ensemble import IsolationForest  # noqa: E402


def _running_inside_streamlit() -> bool:
    """True when this file is executed by Streamlit (streamlit run or the test harness)."""
    for mod in ("streamlit.runtime.scriptrunner_utils.script_run_context", "streamlit.runtime.scriptrunner"):
        try:
            m = __import__(mod, fromlist=["get_script_run_ctx"])
            return m.get_script_run_ctx() is not None
        except Exception:  # noqa: BLE001
            continue
    return True


if __name__ == "__main__" and not _running_inside_streamlit():
    # Started with "python knet_app.py" or a double click: relaunch through Streamlit so the browser opens.
    import sys
    from streamlit.web import cli as _stcli
    print("Starting the KNet platform with Streamlit. Your browser will open shortly.")
    sys.argv = ["streamlit", "run", os.path.abspath(__file__)] + sys.argv[1:]
    sys.exit(_stcli.main())


# ===========================================================================
# SECTION: SYNTHETIC DATA GENERATOR
# ===========================================================================

CITIES = [
    # name, state, lat, lon, region, population(k)
    ("Seattle", "WA", 47.61, -122.33, "Pacific NW", 750), ("Portland", "OR", 45.52, -122.68, "Pacific NW", 650),
    ("San Francisco", "CA", 37.77, -122.42, "West", 870), ("Los Angeles", "CA", 34.05, -118.24, "West", 3900),
    ("San Diego", "CA", 32.72, -117.16, "West", 1400), ("Phoenix", "AZ", 33.45, -112.07, "Southwest", 1600),
    ("Las Vegas", "NV", 36.17, -115.14, "Southwest", 650), ("Denver", "CO", 39.74, -104.99, "Mountain", 720),
    ("Salt Lake City", "UT", 40.76, -111.89, "Mountain", 200), ("Albuquerque", "NM", 35.08, -106.65, "Southwest", 560),
    ("Dallas", "TX", 32.78, -96.80, "Texas", 1300), ("Houston", "TX", 29.76, -95.37, "Texas", 2300),
    ("San Antonio", "TX", 29.42, -98.49, "Texas", 1450), ("Oklahoma City", "OK", 35.47, -97.52, "Central", 690),
    ("Kansas City", "MO", 39.10, -94.58, "Central", 510), ("Omaha", "NE", 41.26, -95.93, "Central", 480),
    ("Minneapolis", "MN", 44.98, -93.27, "Midwest", 430), ("Chicago", "IL", 41.88, -87.63, "Midwest", 2700),
    ("Detroit", "MI", 42.33, -83.05, "Midwest", 640), ("Columbus", "OH", 39.96, -83.00, "Midwest", 900),
    ("Indianapolis", "IN", 39.77, -86.16, "Midwest", 880), ("St. Louis", "MO", 38.63, -90.20, "Central", 300),
    ("Nashville", "TN", 36.16, -86.78, "Southeast", 690), ("Atlanta", "GA", 33.75, -84.39, "Southeast", 500),
    ("Charlotte", "NC", 35.23, -80.84, "Southeast", 870), ("Miami", "FL", 25.76, -80.19, "Southeast", 450),
    ("Tampa", "FL", 27.95, -82.46, "Southeast", 400), ("New Orleans", "LA", 29.95, -90.07, "Southeast", 380),
    ("Washington", "DC", 38.91, -77.04, "Mid-Atlantic", 690), ("Norfolk", "VA", 36.85, -76.29, "Mid-Atlantic", 240),
    ("Baltimore", "MD", 39.29, -76.61, "Mid-Atlantic", 580), ("Philadelphia", "PA", 39.95, -75.17, "Mid-Atlantic", 1600),
    ("Pittsburgh", "PA", 40.44, -79.99, "Mid-Atlantic", 300), ("New York", "NY", 40.71, -74.01, "Northeast", 8300),
    ("Boston", "MA", 42.36, -71.06, "Northeast", 680), ("Hartford", "CT", 41.76, -72.67, "Northeast", 120),
]

# Fictional vendors. vendor_type describes the dependency class.
VENDORS = [
    ("V01", "Meridian Grid Controls", "SCADA and EMS Platform"),
    ("V02", "NorthStar Remote Ops", "Managed Remote Access Provider"),
    ("V03", "Bluefin Cloud Services", "Cloud Hosting"),
    ("V04", "Aegis PLC Systems", "PLC and Field Controller OEM"),
    ("V05", "Cobalt Backbone Carrier", "Telecom Transport Carrier"),
    ("V06", "Helios Building Automation", "Building Management System"),
    ("V07", "Vantage Timing Systems", "GPS and PNT Timing Source"),
    ("V08", "Sentra Identity", "Identity and SSO Provider"),
    ("V09", "Ironclad Firmware Updates", "Firmware Update Service"),
    ("V10", "Clearwater Process Automation", "Water SCADA and HMI"),
    ("V11", "Atlas Network Gear", "Industrial Network Switches"),
    ("V12", "Keystone Payments Switch", "Payment Network Switch"),
    ("V13", "Skyline Avionics Data", "Aviation Data Services"),
    ("V14", "Granite Backup Power", "UPS and Generator Monitoring"),
    ("V15", "Polaris EHR Hosting", "Clinical Systems Hosting"),
]

# asset type -> (sector, criticality, base population factor, redundancy range)
ASSET_TYPES = {
    "Generation Plant": ("Energy", 5, 1.5, (0.4, 0.7)),
    "Grid Control Center": ("Energy", 5, 2.0, (0.5, 0.8)),
    "Transmission Substation": ("Energy", 5, 1.0, (0.2, 0.5)),
    "Distribution Substation": ("Energy", 4, 0.6, (0.1, 0.4)),
    "Gas Compressor Station": ("Energy", 4, 0.8, (0.3, 0.6)),
    "Water Treatment Plant": ("Water and Wastewater", 4, 0.8, (0.3, 0.6)),
    "Water Pumping Station": ("Water and Wastewater", 3, 0.4, (0.2, 0.5)),
    "Telecom Central Office": ("Communications", 4, 0.7, (0.3, 0.6)),
    "Internet Exchange Point": ("Communications", 5, 2.5, (0.4, 0.7)),
    "Data Center": ("Information Technology", 4, 1.0, (0.5, 0.8)),
    "Airport": ("Transportation - Aviation", 4, 0.5, (0.4, 0.7)),
    "Air Traffic Control Facility": ("Transportation - Aviation", 5, 1.2, (0.5, 0.8)),
    "Port Terminal": ("Transportation - Maritime", 3, 0.3, (0.3, 0.6)),
    "Hospital": ("Healthcare and Public Health", 5, 0.3, (0.5, 0.8)),
    "Payment Processing Center": ("Financial Services", 4, 1.5, (0.5, 0.8)),
    "Military Installation": ("Defense", 5, 0.2, (0.5, 0.8)),
    "Defense Industrial Base Plant": ("Defense Industrial Base", 4, 0.1, (0.3, 0.6)),
    "Emergency Communications (911 PSAP)": ("Emergency Services", 5, 0.6, (0.4, 0.7)),
}

VENDOR_AFFINITY = {  # sector -> list of (vendor_id, probability)
    "Energy": [("V01", .8), ("V02", .35), ("V04", .6), ("V07", .7), ("V11", .5), ("V09", .4), ("V14", .3)],
    "Water and Wastewater": [("V10", .85), ("V02", .45), ("V04", .5), ("V11", .3), ("V14", .3)],
    "Communications": [("V05", .8), ("V07", .75), ("V11", .5), ("V03", .3), ("V14", .5)],
    "Information Technology": [("V03", .7), ("V05", .6), ("V06", .5), ("V08", .6), ("V14", .6)],
    "Transportation - Aviation": [("V13", .9), ("V07", .8), ("V05", .5), ("V08", .4), ("V02", .2)],
    "Transportation - Maritime": [("V02", .4), ("V05", .4), ("V03", .4), ("V04", .4)],
    "Healthcare and Public Health": [("V15", .85), ("V06", .6), ("V08", .5), ("V14", .5), ("V02", .25)],
    "Financial Services": [("V12", .9), ("V03", .6), ("V07", .6), ("V08", .6)],
    "Defense": [("V05", .5), ("V07", .6), ("V06", .4), ("V14", .5)],
    "Defense Industrial Base": [("V03", .5), ("V04", .5), ("V08", .5), ("V02", .3)],
    "Emergency Services": [("V05", .8), ("V08", .3), ("V14", .5), ("V02", .3)],
}

ATTACK_ICS = {
    "T0822": "External Remote Services",
    "T0886": "Remote Services",
    "T0859": "Valid Accounts",
    "T0836": "Modify Parameter",
    "T0816": "Device Restart or Shutdown",
    "T0831": "Manipulation of Control",
    "T0813": "Denial of Control",
    "T0814": "Denial of Service",
}

METRICS = ["load_pct", "latency_ms", "error_rate", "auth_failures", "net_out_mb", "cpu_pct"]


def _add_asset(rows, rng, asset_type, city, idx):
    sector, crit, popf, (rlo, rhi) = ASSET_TYPES[asset_type]
    name, state, lat, lon, region, pop = city
    jitter = rng.normal(0, 0.08, 2)
    aid = f"A{idx:04d}"
    rows.append(dict(
        asset_id=aid,
        name=f"{name} {asset_type}",
        asset_type=asset_type, sector=sector, city=name, state=state, region=region,
        lat=round(lat + jitter[0], 4), lon=round(lon + jitter[1], 4),
        criticality=crit,
        population_served=int(pop * 1000 * popf * rng.uniform(0.6, 1.2)),
        redundancy=round(rng.uniform(rlo, rhi), 2),
        internet_exposed=bool(rng.random() < (0.25 if sector in ("Energy", "Water and Wastewater") else 0.15)),
        patch_lag_days=int(rng.gamma(2.0, 30 if sector == "Water and Wastewater" else 20)),
        known_vulns=int(rng.poisson(3 if sector in ("Water and Wastewater", "Energy") else 2)),
        install_year=int(rng.integers(1975, 2023)),
    ))
    return aid


def generate(seed: int = 42, days: int = 7) -> dict:
    rng = np.random.default_rng(seed)
    assets, edges = [], []
    idx = 1
    city_assets: dict[str, dict[str, str]] = {}
    region_assets: dict[str, dict[str, list[str]]] = {}

    # Regional assets
    regions = sorted({c[4] for c in CITIES})
    for reg in regions:
        cities = [c for c in CITIES if c[4] == reg]
        anchor = cities[0]
        region_assets[reg] = {"gen": [], "gcc": [], "gas": [], "ixp": []}
        for k in range(2):
            region_assets[reg]["gen"].append(_add_asset(assets, rng, "Generation Plant", cities[k % len(cities)], idx)); idx += 1
        region_assets[reg]["gcc"].append(_add_asset(assets, rng, "Grid Control Center", anchor, idx)); idx += 1
        region_assets[reg]["gas"].append(_add_asset(assets, rng, "Gas Compressor Station", cities[-1], idx)); idx += 1
        region_assets[reg]["ixp"].append(_add_asset(assets, rng, "Internet Exchange Point", anchor, idx)); idx += 1

    # City assets
    big = {"Los Angeles", "Chicago", "New York", "Dallas", "Atlanta", "Washington", "Denver", "Seattle", "Houston",
           "Philadelphia", "Miami", "Phoenix", "Columbus", "Kansas City"}
    ports = {"Los Angeles", "Houston", "New York", "Norfolk", "Miami", "Seattle", "New Orleans", "Baltimore", "Tampa"}
    mil = {"Norfolk", "San Diego", "Washington", "San Antonio", "Colorado Springs", "Omaha", "Tampa", "Albuquerque",
           "Las Vegas", "Columbus"}
    dib = {"St. Louis", "Hartford", "Dallas", "Phoenix", "Baltimore", "Seattle", "Huntsville"}
    for c in CITIES:
        n = c[0]
        ca = {}
        for t in ["Transmission Substation", "Distribution Substation", "Water Treatment Plant", "Water Pumping Station",
                  "Telecom Central Office", "Hospital", "Emergency Communications (911 PSAP)", "Airport"]:
            ca[t] = _add_asset(assets, rng, t, c, idx); idx += 1
        if n in big:
            for t in ["Air Traffic Control Facility", "Data Center", "Payment Processing Center"]:
                ca[t] = _add_asset(assets, rng, t, c, idx); idx += 1
        if n in ports:
            ca["Port Terminal"] = _add_asset(assets, rng, "Port Terminal", c, idx); idx += 1
        if n in mil:
            ca["Military Installation"] = _add_asset(assets, rng, "Military Installation", c, idx); idx += 1
        if n in dib:
            ca["Defense Industrial Base Plant"] = _add_asset(assets, rng, "Defense Industrial Base Plant", c, idx); idx += 1
        city_assets[n] = ca

    def e(s, t, typ, w):
        edges.append(dict(source=s, target=t, dependency_type=typ, strength=round(float(np.clip(w, 0.05, 0.98)), 2)))

    # Edges
    for reg, ra in region_assets.items():
        cities = [c for c in CITIES if c[4] == reg]
        for g in ra["gen"]:
            e(ra["gas"][0], g, "Fuel", rng.uniform(0.4, 0.7))
            e(ra["gcc"][0], g, "Control", rng.uniform(0.3, 0.6))
        for c in cities:
            ca = city_assets[c[0]]
            for g in ra["gen"]:
                e(g, ca["Transmission Substation"], "Power", rng.uniform(0.35, 0.6))
            e(ra["gcc"][0], ca["Transmission Substation"], "Control", rng.uniform(0.3, 0.55))
            e(ra["ixp"][0], ca["Telecom Central Office"], "Data", rng.uniform(0.3, 0.6))
            if "Data Center" in ca:
                e(ra["ixp"][0], ca["Data Center"], "Data", rng.uniform(0.4, 0.7))
        tco0 = city_assets[cities[0][0]]["Telecom Central Office"]
        e(tco0, ra["gcc"][0], "Communications", rng.uniform(0.3, 0.6))
        e(city_assets[cities[0][0]]["Distribution Substation"], ra["ixp"][0], "Power", rng.uniform(0.3, 0.6))

    for c in CITIES:
        ca = city_assets[c[0]]
        e(ca["Transmission Substation"], ca["Distribution Substation"], "Power", rng.uniform(0.8, 0.95))
        loads = [k for k in ca if k not in ("Transmission Substation", "Distribution Substation")]
        for k in loads:
            e(ca["Distribution Substation"], ca[k], "Power", rng.uniform(0.55, 0.9))
        tco = ca["Telecom Central Office"]
        for k in ["Emergency Communications (911 PSAP)", "Hospital", "Air Traffic Control Facility",
                  "Payment Processing Center", "Water Treatment Plant", "Airport", "Military Installation", "Port Terminal"]:
            if k in ca:
                e(tco, ca[k], "Communications", rng.uniform(0.4, 0.85))
        e(ca["Water Treatment Plant"], ca["Water Pumping Station"], "Water", rng.uniform(0.6, 0.85))
        e(ca["Water Pumping Station"], ca["Hospital"], "Water", rng.uniform(0.35, 0.6))
        if "Data Center" in ca:
            e(ca["Water Pumping Station"], ca["Data Center"], "Water (cooling)", rng.uniform(0.2, 0.45))
            e(ca["Data Center"], ca["Payment Processing Center"], "Data", rng.uniform(0.5, 0.8))
            e(ca["Data Center"], ca["Hospital"], "Data", rng.uniform(0.2, 0.4))
        if "Air Traffic Control Facility" in ca:
            e(ca["Air Traffic Control Facility"], ca["Airport"], "Control", rng.uniform(0.6, 0.9))

    # ATC facilities also serve nearby airports in same region
    for reg in regions:
        cities = [c for c in CITIES if c[4] == reg]
        atcs = [city_assets[c[0]]["Air Traffic Control Facility"] for c in cities if "Air Traffic Control Facility" in city_assets[c[0]]]
        if atcs:
            for c in cities:
                if "Air Traffic Control Facility" not in city_assets[c[0]]:
                    e(atcs[0], city_assets[c[0]]["Airport"], "Control", rng.uniform(0.5, 0.8))

    adf = pd.DataFrame(assets)
    edf = pd.DataFrame(edges).drop_duplicates(["source", "target"]).reset_index(drop=True)

    # Vendor relations
    vrel = []
    for _, a in adf.iterrows():
        for vid, p in VENDOR_AFFINITY.get(a.sector, []):
            if rng.random() < p:
                vrel.append(dict(asset_id=a.asset_id, vendor_id=vid,
                                 service=dict((v[0], v[2]) for v in VENDORS)[vid],
                                 remote_access=bool(vid in ("V02", "V01", "V10") or rng.random() < 0.15)))
    vdf = pd.DataFrame(VENDORS, columns=["vendor_id", "vendor_name", "vendor_type"])
    vrdf = pd.DataFrame(vrel)

    # ---------- Incidents ----------
    start = pd.Timestamp("2026-11-09 00:00:00")
    end = start + pd.Timedelta(days=days)
    inc = []

    def add_inc(ts, aid, itype, sev, desc, scenario, **kw):
        base = dict(incident_id=f"INC-{len(inc) + 1:04d}", timestamp=ts, asset_id=aid, incident_type=itype,
                    severity=sev, description=desc, ioc_match=False, auth_anomaly=False,
                    unauthorized_config_change=False, malware_signature="", attack_technique="",
                    physical_cause="", weather_alert=False, maintenance_window=False,
                    vendor_remote_session=False, status="Open", ground_truth=scenario)
        base.update(kw)
        inc.append(base)

    # S2 accidental cascade - Columbus, day 3 10:12
    col = city_assets["Columbus"]
    t0 = start + pd.Timedelta(days=2, hours=10, minutes=12)
    add_inc(t0, col["Transmission Substation"], "Outage", 5,
            "Transformer bank failure; protective relay trip. Oil temperature alarm preceded trip.", "S2-Cascade",
            physical_cause="Transformer failure (equipment age)")
    seq = [("Distribution Substation", 3, "Outage", 5, "Loss of upstream transmission feed"),
           ("Water Pumping Station", 22, "Outage", 4, "Pumps offline; loss of utility power"),
           ("Water Treatment Plant", 35, "Degradation", 3, "Running on partial backup power"),
           ("Telecom Central Office", 128, "Outage", 4, "Battery plant depleted; generator failed to start"),
           ("Emergency Communications (911 PSAP)", 141, "Degradation", 5, "911 call routing degraded; loss of carrier circuits"),
           ("Hospital", 150, "Degradation", 4, "On generator; clinical comms degraded"),
           ("Air Traffic Control Facility", 160, "Degradation", 4, "Comms circuits failed over to backup")]
    for k, dt, it, sv, d in seq:
        if k in col:
            add_inc(t0 + pd.Timedelta(minutes=dt), col[k], it, sv, d, "S2-Cascade", physical_cause="Upstream power or communications loss")

    # S3 ice storm - Central region, day 4 14:00
    t3 = start + pd.Timedelta(days=3, hours=14)
    storm_cities = ["Kansas City", "Oklahoma City", "St. Louis", "Omaha"]
    j = 0
    for cn in storm_cities:
        ca = city_assets[cn]
        for k in ["Distribution Substation", "Water Pumping Station"]:
            add_inc(t3 + pd.Timedelta(minutes=int(rng.integers(0, 180))), ca[k], "Outage", 3,
                    "Line icing and tree contact; feeder lockout", "S3-Weather",
                    physical_cause="Weather - ice storm", weather_alert=True)
            j += 1

    # S4 simultaneous unexplained - day 5 16:40
    t4 = start + pd.Timedelta(days=4, hours=16, minutes=40)
    for cn, k, dt in [("Seattle", "Payment Processing Center", 0), ("Atlanta", "Water Treatment Plant", 9),
                      ("Boston", "Airport", 17)]:
        add_inc(t4 + pd.Timedelta(minutes=dt), city_assets[cn][k], "Outage", 3,
                "Service interruption; root cause not yet identified", "S4-Unexplained")

    # S5 coordinated cyber via shared vendor V02 - day 6 02:30 (off-hours)
    t5 = start + pd.Timedelta(days=5, hours=2, minutes=30)
    v02_assets = set(vrdf.loc[vrdf.vendor_id == "V02", "asset_id"])
    cand = adf[adf.asset_id.isin(v02_assets)]
    picks = []
    for sec in ["Energy", "Water and Wastewater", "Healthcare and Public Health", "Transportation - Aviation",
                "Defense Industrial Base", "Emergency Services", "Transportation - Maritime"]:
        sub = cand[(cand.sector == sec) & (~cand.state.isin([adf.set_index('asset_id').loc[p, 'state'] for p in picks]))]
        sub = sub[~sub.city.isin(["Columbus"] + storm_cities)]
        if len(sub):
            picks.append(sub.sample(1, random_state=int(rng.integers(0, 1e6))).asset_id.iloc[0])
        if len(picks) >= 6:
            break
    techniques = ["T0822", "T0859", "T0836", "T0816", "T0831", "T0813"]
    for i, aid in enumerate(picks):
        add_inc(t5 + pd.Timedelta(minutes=int(rng.integers(0, 26))), aid,
                "Outage" if i % 2 == 0 else "Unauthorized Access", 5,
                "Unexpected setpoint change and controller restart following vendor remote session from unrecognized host",
                "S5-Coordinated",
                ioc_match=bool(i % 3 != 2), auth_anomaly=True, unauthorized_config_change=bool(i != 1),
                malware_signature="KNET-SIM-LOADER-01" if i in (0, 3) else "",
                attack_technique=techniques[i % len(techniques)], vendor_remote_session=True)

    # S1 background independent failures - avoid scenario windows
    windows = [t0, t3, t4, t5]
    causes = ["Breaker failure", "Pump motor bearing failure", "Fiber cut (construction)", "Software defect after patch",
              "HVAC failure", "Power supply failure", "Sensor drift", "Router hardware fault"]
    n_bg = 0
    while n_bg < 14:
        ts = start + pd.Timedelta(minutes=int(rng.integers(0, days * 1440)))
        if any(abs((ts - w).total_seconds()) < 10 * 3600 for w in windows):
            continue
        a = adf.sample(1, random_state=int(rng.integers(0, 1e6))).iloc[0]
        maint = bool(rng.random() < 0.3)
        add_inc(ts, a.asset_id, "Degradation" if rng.random() < .5 else "Outage", int(rng.integers(1, 4)),
                "Localized equipment fault", "S1-Independent", physical_cause=str(rng.choice(causes)),
                maintenance_window=maint)
        n_bg += 1
    idf = pd.DataFrame(inc).sort_values("timestamp").reset_index(drop=True)
    idf["incident_id"] = [f"INC-{i + 1:04d}" for i in range(len(idf))]

    # ---------- Telemetry (hourly) ----------
    hours = pd.date_range(start, end, freq="h", inclusive="left")
    H = len(hours)
    tel = []
    hour_of_day = hours.hour.values
    diurnal = 0.5 + 0.35 * np.sin((hour_of_day - 6) / 24 * 2 * np.pi)
    for _, a in adf.iterrows():
        base_load = rng.uniform(40, 70)
        m = {
            "load_pct": np.clip(base_load * (0.8 + 0.4 * diurnal) + rng.normal(0, 3, H), 0, 100),
            "latency_ms": np.abs(rng.normal(20, 4, H)),
            "error_rate": np.abs(rng.normal(0.4, 0.15, H)),
            "auth_failures": rng.poisson(2, H).astype(float),
            "net_out_mb": np.abs(rng.normal(120, 25, H) * (0.7 + 0.6 * diurnal)),
            "cpu_pct": np.clip(rng.normal(35, 6, H), 0, 100),
        }
        tel.append((a.asset_id, m))
    tel_map = {aid: m for aid, m in tel}

    def hidx(ts):
        return int(np.clip((ts - start) / pd.Timedelta(hours=1), 0, H - 1))

    for _, r in idf.iterrows():
        m = tel_map[r.asset_id]
        h = hidx(r.timestamp)
        if r.ground_truth == "S5-Coordinated":
            for back in range(2, 9):  # precursor recon + staging hours earlier
                hb = max(h - back, 0)
                m["auth_failures"][hb] += rng.integers(25, 60)
                m["net_out_mb"][hb] += rng.uniform(300, 700)
            m["cpu_pct"][h] = 95
            m["error_rate"][h:h + 4] += 6
            m["load_pct"][h:h + 4] = rng.uniform(0, 5)
        elif r.ground_truth in ("S2-Cascade", "S3-Weather", "S1-Independent"):
            m["error_rate"][h:h + 3] += rng.uniform(3, 6)
            m["latency_ms"][h:h + 3] += rng.uniform(60, 150)
            if r.incident_type == "Outage":
                m["load_pct"][h:h + 3] = rng.uniform(0, 8)
        else:  # S4 unexplained
            m["error_rate"][h:h + 2] += 4
            m["latency_ms"][h:h + 2] += 80
    rows = []
    for aid, m in tel_map.items():
        d = pd.DataFrame(m)
        d.insert(0, "asset_id", aid)
        d.insert(0, "timestamp", hours)
        rows.append(d)
    tdf = pd.concat(rows, ignore_index=True)
    for c in METRICS:
        tdf[c] = tdf[c].round(2)

    return dict(assets=adf, dependencies=edf, vendors=vdf, vendor_relations=vrdf,
                incidents=idf, telemetry=tdf, meta=dict(source="synthetic", seed=seed,
                                                        start=str(start), end=str(end)))


# ===========================================================================
# SECTION: GRAPH ENGINE, KNOWLEDGE GRAPH AND DIGITAL TWIN
# ===========================================================================


def build_graph(assets: pd.DataFrame, deps: pd.DataFrame) -> nx.DiGraph:
    G = nx.DiGraph()
    for r in assets.to_dict("records"):
        G.add_node(r["asset_id"], **r)
    for r in deps.to_dict("records"):
        if r["source"] in G and r["target"] in G:
            G.add_edge(r["source"], r["target"], dependency_type=r["dependency_type"], strength=float(r["strength"]))
    return G


def build_knowledge_graph(assets, deps, vendors, vrel) -> nx.MultiDiGraph:
    """Typed knowledge graph: Asset, Sector, Region, Vendor nodes with semantic relations."""
    K = nx.MultiDiGraph()
    for r in assets.to_dict("records"):
        K.add_node(r["asset_id"], kind="Asset", label=r["name"])
        K.add_node(f"SECTOR:{r['sector']}", kind="Sector", label=r["sector"])
        K.add_node(f"STATE:{r['state']}", kind="State", label=r["state"])
        K.add_edge(r["asset_id"], f"SECTOR:{r['sector']}", rel="IN_SECTOR")
        K.add_edge(r["asset_id"], f"STATE:{r['state']}", rel="LOCATED_IN")
    for r in vendors.to_dict("records"):
        K.add_node(r["vendor_id"], kind="Vendor", label=r["vendor_name"], vendor_type=r["vendor_type"])
    for r in vrel.to_dict("records"):
        K.add_edge(r["asset_id"], r["vendor_id"], rel="DEPENDS_ON_VENDOR", service=r.get("service", ""),
                   remote_access=bool(r.get("remote_access", False)))
    for r in deps.to_dict("records"):
        K.add_edge(r["source"], r["target"], rel=f"SUPPLIES_{str(r['dependency_type']).upper()}", strength=r["strength"])
    return K


def graph_metrics(G: nx.DiGraph) -> pd.DataFrame:
    btw = nx.betweenness_centrality(G, normalized=True, weight=None)
    pr = nx.pagerank(G.reverse(copy=True), alpha=0.85)  # importance as a supplier
    U = G.to_undirected()
    arts = set(nx.articulation_points(U))
    desc = {n: len(nx.descendants(G, n)) for n in G.nodes}
    return pd.DataFrame({
        "asset_id": list(G.nodes),
        "betweenness": [btw[n] for n in G.nodes],
        "supplier_pagerank": [pr[n] for n in G.nodes],
        "downstream_count": [desc[n] for n in G.nodes],
        "out_degree": [G.out_degree(n) for n in G.nodes],
        "in_degree": [G.in_degree(n) for n in G.nodes],
        "single_point_of_failure": [n in arts for n in G.nodes],
    })


def _matrices(G: nx.DiGraph, redundancy_override: dict | None = None):
    nodes = list(G.nodes)
    ix = {n: i for i, n in enumerate(nodes)}
    N = len(nodes)
    red = np.array([float(G.nodes[n].get("redundancy", 0.3)) for n in nodes])
    if redundancy_override:
        for n, v in redundancy_override.items():
            if n in ix:
                red[ix[n]] = v
    W = np.zeros((N, N))
    for u, v, d in G.edges(data=True):
        W[ix[u], ix[v]] = d["strength"] * (1 - red[ix[v]])
    return nodes, ix, W


def analytic_cascade(G: nx.DiGraph, sources: list[str], steps: int = 8, W_pack=None) -> pd.Series:
    """Fast probabilistic propagation (independence approximation). Returns P(fail) per node."""
    nodes, ix, W = W_pack or _matrices(G)
    p = np.zeros(len(nodes))
    for s in sources:
        if s in ix:
            p[ix[s]] = 1.0
    fixed = p.copy()
    for _ in range(steps):
        q = 1 - np.exp(np.log(np.clip(1 - p[:, None] * W, 1e-12, 1)).sum(axis=0))
        p = np.maximum(fixed, np.maximum(p, q))
    return pd.Series(p, index=nodes)


def systemic_impact(G: nx.DiGraph) -> pd.DataFrame:
    """Expected downstream impact if each asset fails alone (predictive criticality)."""
    pack = _matrices(G)
    nodes = pack[0]
    pop = np.array([G.nodes[n].get("population_served", 0) for n in nodes], dtype=float)
    crit = np.array([G.nodes[n].get("criticality", 3) for n in nodes], dtype=float)
    out = []
    for n in nodes:
        p = analytic_cascade(G, [n], steps=6, W_pack=pack).values
        own = nodes.index(n)
        p2 = p.copy(); p2[own] = 0
        out.append((n, float((p2 * pop).sum()), float((p2 * crit).sum()), float((p2 > 0.5).sum())))
    return pd.DataFrame(out, columns=["asset_id", "expected_pop_impact", "expected_crit_impact", "likely_downstream_failures"])


def monte_carlo_cascade(G: nx.DiGraph, sources: list[str], runs: int = 200, steps: int = 10,
                        redundancy_override: dict | None = None, hardened: set | None = None,
                        seed: int = 7) -> dict:
    """Stochastic digital-twin simulation. Each step, a node fails with
    1 - prod(1 - s_uv * (1 - redundancy_v)) over failed predecessors u."""
    nodes, ix, W = _matrices(G, redundancy_override)
    if hardened:
        for h in hardened:
            if h in ix:
                W[:, ix[h]] *= 0.15
    rng = np.random.default_rng(seed)
    N = len(nodes)
    fail_count = np.zeros(N)
    first_step = np.full((runs, N), np.nan)
    timeline = np.zeros((runs, steps + 1))
    src = [ix[s] for s in sources if s in ix]
    for r in range(runs):
        failed = np.zeros(N, dtype=bool)
        failed[src] = True
        first_step[r, src] = 0
        timeline[r, 0] = failed.sum()
        for t in range(1, steps + 1):
            prob = 1 - np.exp(np.log(np.clip(1 - W[failed].astype(float), 1e-12, 1)).sum(axis=0)) if failed.any() else np.zeros(N)
            new = (~failed) & (rng.random(N) < prob)
            first_step[r, new] = t
            failed |= new
            timeline[r, t] = failed.sum()
        fail_count += failed
    pfail = fail_count / runs
    with np.errstate(all="ignore"), warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        mean_step = np.nanmean(first_step, axis=0)
    df = pd.DataFrame({"asset_id": nodes, "p_fail": pfail, "mean_step": mean_step})
    attrs = pd.DataFrame([G.nodes[n] for n in nodes])
    df = df.merge(attrs[["asset_id", "name", "sector", "state", "city", "lat", "lon", "population_served", "criticality"]],
                  on="asset_id", how="left")
    return dict(nodes=df, timeline=timeline, sources=sources)


def suggest_hardening(G: nx.DiGraph, sources: list[str], k: int = 5) -> list[str]:
    """Greedy: pick nodes whose hardening most reduces expected population impact."""
    pack = _matrices(G)
    nodes, ix, W = pack
    pop = np.array([G.nodes[n].get("population_served", 0) for n in nodes], dtype=float)
    base = analytic_cascade(G, sources, W_pack=pack)
    cand = [n for n in base.sort_values(ascending=False).index if n not in sources and base[n] > 0.15][:40]
    chosen = []
    Wc = W.copy()
    for _ in range(k):
        best, best_val = None, None
        for c in cand:
            if c in chosen:
                continue
            Wt = Wc.copy(); Wt[:, ix[c]] *= 0.15
            p = analytic_cascade(G, sources, W_pack=(nodes, ix, Wt)).values
            val = (p * pop).sum()
            if best_val is None or val < best_val:
                best, best_val = c, val
        if best is None:
            break
        chosen.append(best)
        Wc[:, ix[best]] *= 0.15
    return chosen


def haversine_km(lat1, lon1, lat2, lon2):
    R = 6371.0
    p1, p2 = np.radians(lat1), np.radians(lat2)
    dp, dl = p2 - p1, np.radians(lon2 - lon1)
    a = np.sin(dp / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(dl / 2) ** 2
    return 2 * R * np.arcsin(np.sqrt(a))


# ===========================================================================
# SECTION: AI ANOMALY DETECTION, CORRELATION AND ATTRIBUTION
# ===========================================================================


METRICS = ["load_pct", "latency_ms", "error_rate", "auth_failures", "net_out_mb", "cpu_pct"]

CLASS_INDEPENDENT = "Independent technical or environmental failure"
CLASS_CASCADE = "Accidental cascading failure"
CLASS_CYBER = "Potentially coordinated cyber activity"
CLASS_CYBER_SINGLE = "Cyber-related incident (single asset)"
CLASS_UNDETERMINED = "Undetermined, insufficient evidence, do not attribute"

CLASS_COLORS = {
    CLASS_INDEPENDENT: "#4C9BE8",
    CLASS_CASCADE: "#F2A93B",
    CLASS_CYBER: "#E5484D",
    CLASS_CYBER_SINGLE: "#C2508A",
    CLASS_UNDETERMINED: "#9BA3AF",
}

# Log-likelihood-ratio weights (natural log). Positive -> favours malicious activity.
CORROBORATING = {
    "ioc_match": (2.0, "Threat-intel IOC match on affected assets"),
    "malware_signature": (2.0, "Malware signature detected"),
    "unauthorized_config_change": (1.3, "Unauthorized configuration or setpoint change"),
    "auth_anomaly": (1.0, "Authentication anomaly (failed or irregular logons)"),
    "attack_technique": (0.8, "Behaviour mapped to a MITRE ATTACK for ICS technique"),
    "telemetry_precursor": (0.8, "AI detected precursor anomaly (authentication or data egress) before outage"),
    "vendor_remote_session": (0.7, "Irregular third-party remote session at time of event"),
}
CONTEXTUAL = {
    "shared_vendor_unconnected": (0.6, "Shared third-party vendor across assets with no physical dependency path"),
    "synchronized_off_hours": (0.4, "Near simultaneous events outside maintenance windows and business hours"),
    "multi_sector_multi_state": (0.3, "Spans multiple sectors and states with no dependency path"),
}
EXCULPATORY = {
    "cascade_explained": (-2.2, "Event sequence explained by physical dependency propagation"),
    "weather": (-1.8, "Active weather alert or environmental cause"),
    "physical_cause": (-1.4, "Documented physical or equipment root cause"),
    "maintenance": (-1.0, "Occurred during scheduled maintenance window"),
}
PRIOR_P = 0.05
CAT_NAMES = {"ioc_match": "IOC match", "malware_signature": "malware signature",
             "unauthorized_config_change": "unauthorized configuration change", "auth_anomaly": "authentication anomaly",
             "attack_technique": "ATTACK technique", "telemetry_precursor": "telemetry precursor",
             "vendor_remote_session": "vendor remote session"}


# --------------------------------------------------------------------------- anomaly detection
def detect_anomalies(tel: pd.DataFrame, contamination: float = 0.01, seed: int = 0) -> pd.DataFrame:
    df = tel.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    present = [m for m in METRICS if m in df.columns]
    # per-asset robust z-scores (median / MAD)
    g = df.groupby("asset_id")[present]
    med = g.transform("median")
    mad = g.transform(lambda s: (s - s.median()).abs().median()).replace(0, np.nan)
    Z = ((df[present] - med) / (1.4826 * mad)).fillna(0).clip(-50, 50)
    for m in present:
        df[f"z_{m}"] = Z[m].round(2)
    iso = IsolationForest(n_estimators=150, contamination=contamination, random_state=seed)
    X = Z.values
    iso.fit(X)
    raw = -iso.score_samples(X)
    df["anomaly_score"] = ((raw - raw.min()) / (raw.max() - raw.min() + 1e-9)).round(3)
    df["is_anomaly"] = iso.predict(X) == -1
    zabs = Z.abs()
    df["driver"] = zabs.idxmax(axis=1)
    df["driver_z"] = zabs.max(axis=1).round(1)
    cyberish = Z[[c for c in ("auth_failures", "net_out_mb") if c in Z]].max(axis=1) if any(
        c in Z for c in ("auth_failures", "net_out_mb")) else pd.Series(0, index=df.index)
    df["cyber_signal"] = (cyberish > 4) & df["is_anomaly"]
    return df


def precursor_flags(anom: pd.DataFrame, incidents: pd.DataFrame, lookback_h: int = 24) -> pd.Series:
    """True if an asset showed a cyber-type anomaly (auth / egress) in the lookback window before its incident."""
    flags = {}
    cyb = anom[anom["cyber_signal"]][["asset_id", "timestamp"]]
    by_asset = {a: g["timestamp"].values for a, g in cyb.groupby("asset_id")}
    for r in incidents.itertuples():
        ts = np.datetime64(pd.Timestamp(r.timestamp))
        arr = by_asset.get(r.asset_id)
        hit = False
        if arr is not None:
            delta = (ts - arr) / np.timedelta64(1, "h")
            hit = bool(((delta > 0) & (delta <= lookback_h)).any())
        flags[r.incident_id] = hit
    return pd.Series(flags)


# --------------------------------------------------------------------------- correlation
def correlate(incidents: pd.DataFrame, G: nx.DiGraph, vrel: pd.DataFrame, window_min: int = 240,
              simul_min: int = 45, hops: int = 4) -> pd.DataFrame:
    """Link incidents into clusters when close in time AND related by dependency path,
    shared vendor, same state, or near-simultaneity. Returns incidents with cluster_id."""
    inc = incidents.copy()
    inc["timestamp"] = pd.to_datetime(inc["timestamp"])
    inc = inc.sort_values("timestamp").reset_index(drop=True)
    vend = vrel.groupby("asset_id")["vendor_id"].apply(set).to_dict() if len(vrel) else {}
    state = nx.get_node_attributes(G, "state")
    U = nx.Graph(); U.add_nodes_from(inc.index)
    reach = {}

    def within(a, b):
        key = (a, b)
        if key not in reach:
            try:
                reach[key] = nx.shortest_path_length(G, a, b) <= hops
            except (nx.NetworkXNoPath, nx.NodeNotFound):
                reach[key] = False
        return reach[key]

    ts = inc["timestamp"].values
    for i in range(len(inc)):
        for j in range(i + 1, len(inc)):
            dt = (ts[j] - ts[i]) / np.timedelta64(1, "m")
            if dt > window_min:
                break
            a, b = inc.at[i, "asset_id"], inc.at[j, "asset_id"]
            linked = (dt <= simul_min) or within(a, b) or within(b, a) \
                or bool(vend.get(a, set()) & vend.get(b, set()) and dt <= simul_min * 2) \
                or (state.get(a) == state.get(b) and dt <= 120)
            if linked:
                U.add_edge(i, j)
    cid = {}
    comps = sorted(nx.connected_components(U), key=lambda c: min(c))
    for k, comp in enumerate(comps):
        for n in comp:
            cid[n] = f"CL-{k + 1:03d}"
    inc["cluster_id"] = inc.index.map(cid)
    return inc


def _truthy(s):
    if s.dtype == bool:
        return s
    return s.astype(str).str.strip().str.lower().isin(["true", "1", "yes", "y", "t"])


def assess_clusters(inc: pd.DataFrame, G: nx.DiGraph, vrel: pd.DataFrame, precursors: pd.Series,
                    hops: int = 4) -> pd.DataFrame:
    vend = vrel.groupby("asset_id")["vendor_id"].apply(set).to_dict() if len(vrel) else {}
    out = []
    for cid, c in inc.groupby("cluster_id"):
        c = c.sort_values("timestamp")
        assets = list(c["asset_id"])
        nodes = [G.nodes[a] if a in G else {} for a in assets]
        sectors = sorted({n.get("sector", "?") for n in nodes})
        states = sorted({n.get("state", "?") for n in nodes})
        n = len(c)
        span_min = (c["timestamp"].max() - c["timestamp"].min()).total_seconds() / 60
        lats = [n_.get("lat") for n_ in nodes if n_.get("lat") is not None]
        lons = [n_.get("lon") for n_ in nodes if n_.get("lon") is not None]
        spread = 0.0
        if len(lats) > 1:
            spread = max(haversine_km(lats[i], lons[i], lats[j], lons[j]) for i, j in itertools.combinations(range(len(lats)), 2))

        # Cascade explanation: each later event has an earlier event upstream within k hops
        explained, root = 0, assets[0]
        causes = c.get("physical_cause", pd.Series("", index=c.index)).fillna("").astype(str).str.lower().tolist()
        wx = _truthy(c["weather_alert"]).tolist() if "weather_alert" in c else [False] * n
        for i in range(1, n):
            b = assets[i]
            ok = False
            # An event with its own independent root cause (weather, local equipment fault) is not
            # explained by propagation, even if a dependency path exists.
            if wx[i] or (causes[i] and "upstream" not in causes[i]):
                continue
            for a in assets[:i]:
                if a in G and b in G:
                    try:
                        if nx.shortest_path_length(G, a, b) <= hops:
                            ok = True; break
                    except nx.NetworkXNoPath:
                        pass
            explained += ok
        cascade_frac = explained / (n - 1) if n > 1 else 0.0

        # unconnected pairs
        unconnected = 0; pairs = 0
        for a, b in itertools.combinations(set(assets), 2):
            pairs += 1
            if a in G and b in G and not (nx.has_path(G, a, b) and nx.shortest_path_length(G, a, b) <= hops) \
                    and not (nx.has_path(G, b, a) and nx.shortest_path_length(G, b, a) <= hops):
                unconnected += 1
        unconnected_frac = unconnected / pairs if pairs else 0.0

        vend_counts = pd.Series([v for a in set(assets) for v in vend.get(a, set())]).value_counts()
        top_vendor_share = (vend_counts.iloc[0] / len(set(assets))) if len(vend_counts) else 0
        top_vendor = vend_counts.index[0] if len(vend_counts) else ""

        ev = {}
        ev["ioc_match"] = _truthy(c["ioc_match"]).mean() if "ioc_match" in c else 0
        ev["malware_signature"] = (c.get("malware_signature", pd.Series("", index=c.index)).fillna("").astype(str).str.len() > 0).mean()
        ev["unauthorized_config_change"] = _truthy(c["unauthorized_config_change"]).mean() if "unauthorized_config_change" in c else 0
        ev["auth_anomaly"] = _truthy(c["auth_anomaly"]).mean() if "auth_anomaly" in c else 0
        ev["attack_technique"] = (c.get("attack_technique", pd.Series("", index=c.index)).fillna("").astype(str).str.len() > 0).mean()
        ev["vendor_remote_session"] = _truthy(c["vendor_remote_session"]).mean() if "vendor_remote_session" in c else 0
        ev["telemetry_precursor"] = precursors.reindex(c["incident_id"]).fillna(False).astype(bool).mean()
        weather = _truthy(c["weather_alert"]).mean() if "weather_alert" in c else 0
        pc = c.get("physical_cause", pd.Series("", index=c.index)).fillna("").astype(str)
        physical = (pc.str.len() > 0).mean()
        maint = _truthy(c["maintenance_window"]).mean() if "maintenance_window" in c else 0
        hours = c["timestamp"].dt.hour
        off_hours = ((hours < 6) | (hours >= 22)).mean()

        contrib = []
        logit = math.log(PRIOR_P / (1 - PRIOR_P))
        corroborating_cats = []
        for k, (w, label) in CORROBORATING.items():
            v = float(ev[k])
            if v > 0:
                s = w * min(1.0, v / 0.5)  # saturate at 50% coverage
                logit += s
                contrib.append(("Corroborating", label, round(s, 2), f"{v * 100:.0f} percent of events"))
                if v >= 0.3:
                    corroborating_cats.append(k)
        if n > 1:
            if top_vendor_share >= 0.6 and unconnected_frac >= 0.6:
                w, label = CONTEXTUAL["shared_vendor_unconnected"]
                logit += w; contrib.append(("Contextual", label, w, f"{top_vendor} on {top_vendor_share * 100:.0f} percent of assets"))
            if span_min <= 60 and unconnected_frac >= 0.6 and maint < 0.3 and off_hours >= 0.5:
                w, label = CONTEXTUAL["synchronized_off_hours"]
                logit += w; contrib.append(("Contextual", label, w, f"{span_min:.0f} minute span"))
            if len(sectors) >= 3 and len(states) >= 3 and unconnected_frac >= 0.6:
                w, label = CONTEXTUAL["multi_sector_multi_state"]
                logit += w; contrib.append(("Contextual", label, w, f"{len(sectors)} sectors and {len(states)} states"))
        for key, val in [("cascade_explained", cascade_frac), ("weather", weather), ("physical_cause", physical),
                         ("maintenance", maint)]:
            if val > 0:
                w, label = EXCULPATORY[key]
                s = w * val
                logit += s
                contrib.append(("Exculpatory", label, round(s, 2), f"{val * 100:.0f} percent of events"))
        p_mal = 1 / (1 + math.exp(-logit))
        ncat = len(corroborating_cats)

        # ---------------- decision logic with guardrails ----------------
        if n == 1:
            if ncat >= 2:
                cls, conf = CLASS_CYBER_SINGLE, "Moderate"
                rationale = "Single asset with multiple corroborating cyber indicators; no evidence of coordination."
            else:
                cls, conf = CLASS_INDEPENDENT, "High" if physical > 0 else "Moderate"
                rationale = "Isolated event with no correlated incidents" + (" and a documented physical cause." if physical else ".")
        elif ncat >= 2 and p_mal >= 0.5:
            cls = CLASS_CYBER
            conf = "High" if (ncat >= 4 and p_mal >= 0.9) else "Moderate" if ncat >= 3 else "Low"
            rationale = (f"{ncat} independent corroborating cyber evidence categories across {n} events "
                         f"({', '.join(CAT_NAMES[k] for k in corroborating_cats)}). Requires analyst validation before any attribution is communicated.")
            if cascade_frac >= 0.6:
                rationale += " Downstream propagation was also observed, so this may be a cyber initiated cascade."
        elif cascade_frac >= 0.6 and ncat < 2:
            cls, conf = CLASS_CASCADE, "High" if cascade_frac >= 0.85 else "Moderate"
            rationale = (f"{cascade_frac * 100:.0f} percent of follow on events lie downstream of the initiating event "
                         f"({G.nodes[assets[0]].get('name', assets[0]) if assets[0] in G else assets[0]}) on the dependency graph; no corroborating cyber evidence.")
        elif (weather >= 0.5 or physical >= 0.6) and ncat < 2:
            cls, conf = CLASS_INDEPENDENT, "High" if weather >= 0.5 else "Moderate"
            rationale = ("Multiple simultaneous failures share a documented environmental or physical common cause"
                         + (" (active weather alert)." if weather >= 0.5 else ".") + " No corroborating cyber evidence.")
        else:
            cls, conf = CLASS_UNDETERMINED, "Not assessed"
            rationale = ("Events are correlated in time" + (" across sectors and states" if len(sectors) > 1 else "")
                         + f" but only {ncat} corroborating cyber categories present and no physical or dependency explanation. "
                           "Simultaneity alone is NOT evidence of an attack. Collect logs, vendor statements and forensics.")
        gaps = [CORROBORATING[k][1] for k in CORROBORATING if k not in corroborating_cats]
        out.append(dict(
            cluster_id=cid, n_incidents=n, start=c["timestamp"].min(), end=c["timestamp"].max(),
            span_min=round(span_min, 1), sectors=", ".join(sectors), n_sectors=len(sectors),
            states=", ".join(states), n_states=len(states), geo_spread_km=round(spread),
            root_candidate=root, cascade_explained=round(cascade_frac, 2), unconnected_pairs=round(unconnected_frac, 2),
            top_shared_vendor=top_vendor, top_vendor_share=round(float(top_vendor_share), 2),
            corroborating_categories=ncat, p_malicious=round(p_mal, 3), assessment=cls, confidence=conf,
            rationale=rationale, evidence=contrib, evidence_gaps=gaps, max_severity=int(c["severity"].max()),
            assets=assets,
        ))
    return pd.DataFrame(out).sort_values("start").reset_index(drop=True)


# ===========================================================================
# SECTION: RISK SCORING AND THIRD PARTY DISCOVERY
# ===========================================================================

DEFAULT_WEIGHTS = {
    "criticality": 0.18,
    "systemic_impact": 0.20,
    "centrality": 0.10,
    "exposure": 0.15,
    "third_party": 0.12,
    "resilience_gap": 0.10,
    "live_anomaly": 0.08,
    "incident_pressure": 0.07,
}

TIERS = [(70, "Critical"), (55, "High"), (40, "Elevated"), (0, "Guarded")]
TIER_COLORS = {"Critical": "#E5484D", "High": "#F2A93B", "Elevated": "#E8D44D", "Guarded": "#4C9BE8"}


def _norm(s: pd.Series) -> pd.Series:
    s = s.astype(float)
    rng = s.max() - s.min()
    return (s - s.min()) / rng if rng > 0 else s * 0


def vendor_concentration(assets: pd.DataFrame, vendors: pd.DataFrame, vrel: pd.DataFrame,
                         impact: pd.DataFrame) -> pd.DataFrame:
    if vrel.empty:
        return pd.DataFrame(columns=["vendor_id", "vendor_name", "vendor_type", "assets", "sectors", "states",
                                     "remote_access_assets", "population_exposed", "systemic_score", "systemic_flag"])
    m = vrel.merge(assets, on="asset_id", how="left").merge(impact, on="asset_id", how="left")
    g = m.groupby("vendor_id").agg(
        assets=("asset_id", "nunique"), sectors=("sector", "nunique"), states=("state", "nunique"),
        remote_access_assets=("remote_access", "sum"), crit_sum=("criticality", "sum"),
        population_exposed=("population_served", "sum"),
        downstream_pop=("expected_pop_impact", "sum"),
        sector_list=("sector", lambda s: ", ".join(sorted(set(s)))),
    ).reset_index()
    g = g.merge(vendors, on="vendor_id", how="left")
    g["systemic_score"] = (100 * (0.30 * _norm(g["crit_sum"]) + 0.25 * _norm(g["sectors"]) + 0.15 * _norm(g["states"])
                                  + 0.15 * _norm(g["remote_access_assets"]) + 0.15 * _norm(g["downstream_pop"].fillna(0)))).round(1)
    g["systemic_flag"] = np.where((g["sectors"] >= 3) & (g["systemic_score"] >= 50), "Systemic cross-sector",
                                  np.where(g["sectors"] >= 3, "Cross-sector", "Sector-contained"))
    return g.sort_values("systemic_score", ascending=False).reset_index(drop=True)


def hidden_couplings(G: nx.DiGraph, vrel: pd.DataFrame, assets: pd.DataFrame, vendor_id: str, limit: int = 200) -> pd.DataFrame:
    """Asset pairs in different sectors with no physical dependency path that share a vendor -
    i.e., coupling invisible to a traditional dependency map."""
    a = vrel.loc[vrel.vendor_id == vendor_id, "asset_id"].unique().tolist()
    sec = assets.set_index("asset_id")["sector"].to_dict()
    nm = assets.set_index("asset_id")["name"].to_dict()
    rows = []
    for x, y in itertools.combinations(a, 2):
        if sec.get(x) == sec.get(y):
            continue
        if nx.has_path(G, x, y) or nx.has_path(G, y, x):
            continue
        rows.append(dict(asset_a=nm.get(x, x), sector_a=sec.get(x), asset_b=nm.get(y, y), sector_b=sec.get(y)))
        if len(rows) >= limit:
            break
    return pd.DataFrame(rows)


def score_assets(assets: pd.DataFrame, metrics: pd.DataFrame, impact: pd.DataFrame, vconc: pd.DataFrame,
                 vrel: pd.DataFrame, anom: pd.DataFrame, incidents: pd.DataFrame,
                 weights: dict | None = None) -> pd.DataFrame:
    w = dict(DEFAULT_WEIGHTS); w.update(weights or {})
    tot = sum(w.values()) or 1
    w = {k: v / tot for k, v in w.items()}
    df = assets.merge(metrics, on="asset_id", how="left").merge(impact, on="asset_id", how="left")
    c = pd.DataFrame(index=df.index)
    c["criticality"] = (df["criticality"].astype(float) - 1) / 4
    c["systemic_impact"] = _norm(np.log1p(df["expected_pop_impact"].fillna(0)))
    c["centrality"] = _norm(df["betweenness"].fillna(0) + df["supplier_pagerank"].fillna(0) * 5)
    exp = 0.4 * df["internet_exposed"].astype(float) + 0.3 * np.minimum(df["patch_lag_days"] / 180, 1) \
        + 0.3 * np.minimum(df["known_vulns"] / 10, 1)
    c["exposure"] = exp.clip(0, 1)
    if len(vconc) and len(vrel):
        vs = vrel.merge(vconc[["vendor_id", "systemic_score"]], on="vendor_id", how="left")
        vmax = vs.groupby("asset_id")["systemic_score"].max() / 100
        c["third_party"] = df["asset_id"].map(vmax).fillna(0)
    else:
        c["third_party"] = 0.0
    c["resilience_gap"] = 1 - df["redundancy"].astype(float)
    if anom is not None and len(anom):
        last = anom["timestamp"].max()
        recent = anom[anom["timestamp"] >= last - pd.Timedelta(hours=48)]
        amax = recent.groupby("asset_id")["anomaly_score"].max()
        c["live_anomaly"] = df["asset_id"].map(amax).fillna(0)
    else:
        c["live_anomaly"] = 0.0
    if len(incidents):
        ip = incidents.groupby("asset_id")["severity"].sum()
        c["incident_pressure"] = np.minimum(df["asset_id"].map(ip).fillna(0) / 10, 1)
    else:
        c["incident_pressure"] = 0.0
    df["risk_score"] = (100 * sum(c[k] * w[k] for k in w)).round(1)
    for k in w:
        df[f"f_{k}"] = c[k].round(3)
    df["risk_tier"] = df["risk_score"].apply(lambda s: next(t for th, t in TIERS if s >= th))
    df["top_driver"] = c.mul(pd.Series(w)).idxmax(axis=1).str.replace("_", " ").str.title()
    return df.sort_values("risk_score", ascending=False).reset_index(drop=True)


# ===========================================================================
# SECTION: INCIDENT RESPONSE PLAYBOOKS
# ===========================================================================


SECTOR_PARTNERS = {
    "Energy": "DOE CESER and E-ISAC; FERC and NERC reporting obligations as applicable",
    "Water and Wastewater": "EPA (Water SRMA) and WaterISAC",
    "Communications": "CISA and Comm-ISAC; FCC outage reporting (NORS) as applicable",
    "Information Technology": "CISA and IT-ISAC",
    "Transportation - Aviation": "FAA and TSA; Aviation ISAC",
    "Transportation - Maritime": "USCG and TSA; Maritime ISAC",
    "Healthcare and Public Health": "HHS and Health-ISAC",
    "Financial Services": "Treasury and FS-ISAC; prudential regulators",
    "Defense": "Service CERT and JFHQ-DODIN; DISA as applicable",
    "Defense Industrial Base": "DoD DC3 and DIBNet reporting (DFARS 252.204-7012) as applicable",
    "Emergency Services": "CISA Emergency Communications; state 911 authority",
}

PLAYBOOKS = {
    CLASS_CYBER: [
        ("Contain", "Suspend or step-up authenticate remote access for the shared vendor across ALL affected customers", "P1", True),
        ("Contain", "Isolate affected OT segments at the IT and OT boundary; move controllers to local or manual control where safe", "P1", False),
        ("Investigate", "Preserve volatile evidence, controller project files, historian data and firewall and VPN logs (chain of custody)", "P1", True),
        ("Investigate", "Hunt for observed IOCs and TTPs across all assets sharing the vendor, including unaffected sites", "P1", True),
        ("Investigate", "Validate PLC and RTU logic and setpoints against known good baselines", "P1", False),
        ("Coordinate", "Notify CISA Central (phone 888 282 0870 or the CISA incident reporting portal) and the FBI field office; engage sector partners", "P1", False),
        ("Coordinate", "Request vendor PSIRT statement on compromise of remote-access infrastructure", "P2", False),
        ("Coordinate", "Assess regulatory reporting deadlines with counsel (e.g., CIRCIA, sector regulators)", "P2", False),
        ("Recover", "Restore from verified backups; rotate credentials and certificates used by the vendor", "P2", False),
        ("Communicate", "Executive and public messaging must state under investigation; no attribution until an analyst confirms", "P1", False),
    ],
    CLASS_CYBER_SINGLE: [
        ("Contain", "Isolate the affected asset network segment; disable compromised accounts", "P1", True),
        ("Investigate", "Collect host and network forensics; scope lateral movement", "P1", True),
        ("Investigate", "Check peer assets with the same vendors or configurations for the same indicators", "P2", True),
        ("Coordinate", "Share indicators with sector ISAC and CISA", "P2", False),
        ("Recover", "Rebuild or restore from known good images; rotate credentials", "P2", False),
    ],
    CLASS_CASCADE: [
        ("Contain", "Isolate the initiating fault; sectionalize to stop further propagation", "P1", False),
        ("Contain", "Prioritize restoration to life-safety loads (911 PSAPs, hospitals, water) per restoration plan", "P1", False),
        ("Investigate", "Root-cause analysis of the initiating equipment failure; check protection settings", "P2", False),
        ("Investigate", "Confirm absence of cyber indicators on the initiating asset (rule-out, not assume)", "P2", True),
        ("Recover", "Verify backup power fuel and battery runtimes at downstream dependents", "P1", True),
        ("Coordinate", "Mutual-aid and cross-sector coordination via state EOC", "P2", False),
        ("Improve", "Add redundancy or backup at the hardening points identified by the digital twin", "P3", False),
    ],
    CLASS_INDEPENDENT: [
        ("Recover", "Dispatch field crews; standard restoration procedures", "P2", False),
        ("Investigate", "Record root cause; check for common mode equipment or firmware issues across fleet", "P3", True),
        ("Monitor", "Keep the cluster under watch for 24 hours in case of late arriving correlated events", "P3", True),
    ],
    CLASS_UNDETERMINED: [
        ("Investigate", "Elevate monitoring; collect logs from all involved assets and shared vendors", "P1", True),
        ("Investigate", "Query vendors and carriers for maintenance or changes in the time window", "P2", False),
        ("Investigate", "Run an IOC sweep and authentication review; this is evidence collection, not assumption", "P2", True),
        ("Communicate", "Do NOT describe events as an attack; describe them as concurrent outages under review", "P1", False),
        ("Monitor", "Reassess automatically as new evidence arrives", "P2", True),
    ],
}


def recommendations(cluster: pd.Series, assets: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for phase, action, prio, soar in PLAYBOOKS.get(cluster["assessment"], []):
        if "shared vendor" in action and cluster.get("top_shared_vendor"):
            action = action.replace("the shared vendor", f"vendor {cluster['top_shared_vendor']}")
        rows.append(dict(cluster_id=cluster["cluster_id"], phase=phase, action=action, priority=prio,
                         soar_automatable=soar, approval_required=True, status="Proposed"))
    sectors = [s.strip() for s in str(cluster["sectors"]).split(",") if s.strip()]
    for s in sectors:
        if s in SECTOR_PARTNERS and cluster["assessment"] != CLASS_INDEPENDENT:
            rows.append(dict(cluster_id=cluster["cluster_id"], phase="Coordinate",
                             action=f"[{s}] Engage: {SECTOR_PARTNERS[s]}", priority="P2",
                             soar_automatable=False, approval_required=True, status="Proposed"))
    return pd.DataFrame(rows)


# ===========================================================================
# SECTION: UPLOAD SCHEMAS AND VALIDATION
# ===========================================================================

SCHEMAS = {
    "assets": {
        "required": ["asset_id", "name", "asset_type", "sector", "state", "lat", "lon", "criticality"],
        "defaults": {"city": "", "region": "", "population_served": 0, "redundancy": 0.3, "internet_exposed": False,
                     "patch_lag_days": 0, "known_vulns": 0, "install_year": 2000},
    },
    "dependencies": {
        "required": ["source", "target", "dependency_type"],
        "defaults": {"strength": 0.5},
    },
    "vendors": {
        "required": ["vendor_id", "vendor_name"],
        "defaults": {"vendor_type": "Unspecified"},
    },
    "vendor_relations": {
        "required": ["asset_id", "vendor_id"],
        "defaults": {"service": "", "remote_access": False},
    },
    "incidents": {
        "required": ["incident_id", "timestamp", "asset_id", "incident_type", "severity"],
        "defaults": {"description": "", "ioc_match": False, "auth_anomaly": False, "unauthorized_config_change": False,
                     "malware_signature": "", "attack_technique": "", "physical_cause": "", "weather_alert": False,
                     "maintenance_window": False, "vendor_remote_session": False, "status": "Open", "ground_truth": ""},
    },
    "telemetry": {
        "required": ["timestamp", "asset_id"],
        "defaults": {"load_pct": 50.0, "latency_ms": 20.0, "error_rate": 0.4, "auth_failures": 0.0,
                     "net_out_mb": 100.0, "cpu_pct": 30.0},
    },
}

BOOL_COLS = {"internet_exposed", "remote_access", "ioc_match", "auth_anomaly", "unauthorized_config_change",
             "weather_alert", "maintenance_window", "vendor_remote_session"}
MAX_ROWS = 2_000_000


def _to_bool(s: pd.Series) -> pd.Series:
    return s.astype(str).str.strip().str.lower().isin(["true", "1", "yes", "y", "t"])


def validate(kind: str, raw: bytes, filename: str) -> tuple[pd.DataFrame | None, list[str], list[str]]:
    """Returns (df, errors, warnings)."""
    errs, warns = [], []
    try:
        if filename.lower().endswith((".xlsx", ".xls")):
            df = pd.read_excel(io.BytesIO(raw))
        elif filename.lower().endswith(".json"):
            df = pd.read_json(io.BytesIO(raw))
        else:
            df = pd.read_csv(io.BytesIO(raw))
    except Exception as e:  # noqa: BLE001
        return None, [f"Could not parse file: {e}"], []
    if len(df) > MAX_ROWS:
        return None, [f"File exceeds {MAX_ROWS:,} rows."], []
    df.columns = [str(c).strip().lower() for c in df.columns]
    sch = SCHEMAS[kind]
    missing = [c for c in sch["required"] if c not in df.columns]
    if missing:
        errs.append(f"Missing required columns: {', '.join(missing)}")
        return None, errs, warns
    for c, d in sch["defaults"].items():
        if c not in df.columns:
            df[c] = d
            warns.append(f"Column '{c}' not supplied, defaulted to {d!r}")
    for c in BOOL_COLS & set(df.columns):
        df[c] = _to_bool(df[c])
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        bad = df["timestamp"].isna().sum()
        if bad:
            warns.append(f"{bad} rows with unparseable timestamps dropped")
            df = df.dropna(subset=["timestamp"])
    for c in ["lat", "lon", "criticality", "strength", "severity", "redundancy"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    if kind == "assets":
        df["criticality"] = df["criticality"].fillna(3).clip(1, 5)
        if df["asset_id"].duplicated().any():
            errs.append("Duplicate asset_id values found")
    if kind == "dependencies":
        df["strength"] = df["strength"].fillna(0.5).clip(0, 1)
    for c in df.columns:
        if df[c].dtype == object:
            df[c] = df[c].fillna("").astype(str).str.slice(0, 500)
    return (None if errs else df), errs, warns


def template_csv(kind: str) -> bytes:
    sch = SCHEMAS[kind]
    cols = sch["required"] + [c for c in sch["defaults"] if c not in sch["required"]]
    return (",".join(cols) + "\n").encode()


def cross_validate(data: dict) -> list[str]:
    msgs = []
    ids = set(data["assets"]["asset_id"])
    d = data["dependencies"]
    bad = (~d["source"].isin(ids) | ~d["target"].isin(ids)).sum()
    if bad:
        msgs.append(f"{bad} dependency edges reference unknown assets (ignored)")
    bi = (~data["incidents"]["asset_id"].isin(ids)).sum()
    if bi:
        msgs.append(f"{bi} incidents reference unknown assets")
    return msgs


# ===========================================================================
# SECTION: ACCESS CONTROL AND AUDIT
# ===========================================================================
ROLES = {
    "viewer": {"dashboards"},
    "analyst": {"dashboards", "simulate", "attribute", "upload"},
    "admin": {"dashboards", "simulate", "attribute", "upload", "admin"},
}

_DEMO_USERS = {  # username: (sha256(password), role)
    "viewer": (hashlib.sha256(b"knet-viewer").hexdigest(), "viewer"),
    "analyst": (hashlib.sha256(b"knet-analyst").hexdigest(), "analyst"),
    "admin": (hashlib.sha256(b"knet-admin").hexdigest(), "admin"),
}


def load_users(secrets=None) -> tuple[dict, bool]:
    """Returns (users, using_demo_defaults)."""
    users = {}
    try:
        if secrets is not None and "users" in secrets:
            for u, cfg in secrets["users"].items():
                users[u] = (cfg["password_sha256"], cfg.get("role", "viewer"))
    except Exception:
        users = {}
    env = os.environ.get("KNET_USERS_JSON")
    if not users and env:
        try:
            users = {u: (v["password_sha256"], v.get("role", "viewer")) for u, v in json.loads(env).items()}
        except Exception:
            users = {}
    if users:
        return users, False
    return dict(_DEMO_USERS), True


def verify(users: dict, username: str, password: str):
    rec = users.get(username)
    if not rec:
        hmac.compare_digest("x" * 64, hashlib.sha256(password.encode()).hexdigest())
        return None
    ok = hmac.compare_digest(rec[0], hashlib.sha256(password.encode()).hexdigest())
    return rec[1] if ok else None


def can(role: str | None, perm: str) -> bool:
    return bool(role) and perm in ROLES.get(role, set())


def audit_event(log: list, user: str | None, action: str, detail: str = "") -> None:
    log.append(dict(timestamp_utc=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
                    user=user or "anonymous", action=action, detail=detail))


# ===========================================================================
# SECTION: ANALYTICS PIPELINE
# ===========================================================================
CLUSTER_COLS = ["cluster_id", "n_incidents", "start", "end", "span_min", "sectors", "n_sectors", "states", "n_states",
                "geo_spread_km", "root_candidate", "cascade_explained", "unconnected_pairs", "top_shared_vendor",
                "top_vendor_share", "corroborating_categories", "p_malicious", "assessment", "confidence", "rationale",
                "evidence", "evidence_gaps", "max_severity", "assets"]


def run_pipeline(data: dict, window_min: int = 240, simul_min: int = 45, contamination: float = 0.01) -> dict:
    assets, deps, vendors, vrel = data["assets"], data["dependencies"], data["vendors"], data["vendor_relations"]
    incidents = data["incidents"].copy()
    incidents["timestamp"] = pd.to_datetime(incidents["timestamp"])
    tel = data["telemetry"].copy()
    tel["timestamp"] = pd.to_datetime(tel["timestamp"])
    G = build_graph(assets, deps)
    metrics = graph_metrics(G)
    impact = systemic_impact(G)
    if len(tel) >= 50:
        anom = detect_anomalies(tel, contamination=contamination)
    else:
        anom = pd.DataFrame({"timestamp": pd.to_datetime(pd.Series([], dtype="object")), "asset_id": pd.Series([], dtype=str),
                             "anomaly_score": pd.Series([], dtype=float), "is_anomaly": pd.Series([], dtype=bool),
                             "driver": pd.Series([], dtype=str), "driver_z": pd.Series([], dtype=float),
                             "cyber_signal": pd.Series([], dtype=bool)})
    if len(incidents):
        prec = precursor_flags(anom, incidents)
        inc = correlate(incidents, G, vrel, window_min=window_min, simul_min=simul_min)
        inc["telemetry_precursor"] = inc["incident_id"].map(prec).fillna(False).astype(bool)
        clusters = assess_clusters(inc, G, vrel, prec)
    else:
        inc = incidents.assign(cluster_id=pd.Series([], dtype=str), telemetry_precursor=pd.Series([], dtype=bool))
        clusters = pd.DataFrame(columns=CLUSTER_COLS)
    vconc = vendor_concentration(assets, vendors, vrel, impact)
    scored = score_assets(assets, metrics, impact, vconc, vrel, anom, inc)
    return dict(G=G, metrics=metrics, impact=impact, anom=anom, incidents=inc, clusters=clusters, vconc=vconc, risk=scored)


# ===========================================================================
# SECTION: OFFLINE UNITED STATES MAP (state outlines embedded, no internet needed)
# ===========================================================================
US_OUTLINE_B64 = (
    "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"
)
MAP_KX = math.cos(math.radians(38.0))


@st.cache_data(show_spinner=False)
def us_rings():
    return json.loads(zlib.decompress(base64.b64decode(US_OUTLINE_B64)).decode())


def map_xy(lon, lat):
    return np.asarray(lon, dtype=float) * MAP_KX, np.asarray(lat, dtype=float)


def base_map(height=520):
    xs, ys = [], []
    for r in us_rings():
        for lon, lat in r:
            if lon < -126 or lat < 24.3:
                continue
            xs.append(lon * MAP_KX); ys.append(lat)
        xs.append(None); ys.append(None)
    fig = go.Figure(go.Scatter(x=xs, y=ys, mode="lines", fill="toself", fillcolor="rgba(120,140,170,0.22)",
                               line=dict(color="rgba(120,140,170,0.75)", width=1), hoverinfo="skip", showlegend=False))
    fig.update_xaxes(visible=False, range=[-125.5 * MAP_KX, -66.5 * MAP_KX])
    fig.update_yaxes(visible=False, range=[24.2, 49.8], scaleanchor="x", scaleratio=1)
    return style_fig(fig, height)


def map_edges(fig, G, edges, color="rgba(120,160,210,0.25)", width=0.7, name="Dependencies"):
    xs, ys = [], []
    for u, v in edges:
        a, b = G.nodes[u], G.nodes[v]
        xs += [a["lon"] * MAP_KX, b["lon"] * MAP_KX, None]
        ys += [a["lat"], b["lat"], None]
    fig.add_trace(go.Scatter(x=xs, y=ys, mode="lines", line=dict(color=color, width=width), name=name, hoverinfo="skip"))


def map_points(fig, df, name, color, size=8, symbol="circle", text=None, opacity=0.85, line_color=None):
    x, y = map_xy(df["lon"], df["lat"])
    fig.add_trace(go.Scatter(x=x, y=y, mode="markers", name=name,
                             marker=dict(size=size, color=color, symbol=symbol, opacity=opacity,
                                         line=dict(width=1.5 if line_color else 0.5, color=line_color or "#0A1628")),
                             text=text, hoverinfo="text"))


# ===========================================================================
# SECTION: REPORT EXPORT (PDF, WORD, TEXT, CSV)
# ===========================================================================
EXPORT_BANNER = "UNCLASSIFIED. DEMONSTRATION. SYNTHETIC DATA."
BRAND = "KNet National Critical Infrastructure Cyber Resilience and Cascading Failure Detection Platform"
BYLINE = "Developed by Randy Singh, Kalsnet (KNet) Consulting Group"


def pretty_cols(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out.columns = [str(c).replace("_", " ").strip().capitalize() for c in out.columns]
    for c in out.columns:
        if out[c].dtype == bool:
            out[c] = out[c].map({True: "Yes", False: "No"})
        elif pd.api.types.is_datetime64_any_dtype(out[c]):
            out[c] = out[c].dt.strftime("%Y-%m-%d %H:%M")
        elif pd.api.types.is_float_dtype(out[c]):
            out[c] = out[c].round(3)
    return out


class Report:
    """Collects the content of one module so it can be exported in four formats."""

    def __init__(self, title: str, key: str):
        self.title, self.key = title, key
        self.blocks = []
        self.primary = None

    def h(self, text):
        self.blocks.append(("h", text))

    def p(self, text):
        self.blocks.append(("p", text))

    def table(self, df, caption="", max_rows=40):
        self.blocks.append(("t", pretty_cols(df), caption, max_rows))

    def chart(self, fn, caption=""):
        self.blocks.append(("c", fn, caption))

    def set_primary(self, df):
        self.primary = pretty_cols(df)


def _fig_png(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return buf.getvalue()


def png_bar(labels, values, title, xlabel="", color="#13315C"):
    fig, ax = plt.subplots(figsize=(7.2, max(2.4, 0.32 * len(labels) + 1)))
    ax.barh(list(labels)[::-1], list(values)[::-1], color=color)
    ax.set_title(title, fontsize=11, loc="left"); ax.set_xlabel(xlabel, fontsize=9)
    ax.tick_params(labelsize=8); ax.spines[["top", "right"]].set_visible(False)
    return _fig_png(fig)


def png_line(x, series: dict, title, xlabel="", ylabel=""):
    fig, ax = plt.subplots(figsize=(7.2, 3.2))
    for name, (vals, color) in series.items():
        ax.plot(x, vals, label=name, color=color, linewidth=2)
    ax.set_title(title, fontsize=11, loc="left"); ax.set_xlabel(xlabel, fontsize=9); ax.set_ylabel(ylabel, fontsize=9)
    ax.legend(fontsize=8, frameon=False); ax.tick_params(labelsize=8); ax.spines[["top", "right"]].set_visible(False)
    return _fig_png(fig)


def png_hist(values, title, xlabel=""):
    fig, ax = plt.subplots(figsize=(7.2, 3.0))
    ax.hist(values, bins=30, color="#13315C")
    ax.set_title(title, fontsize=11, loc="left"); ax.set_xlabel(xlabel, fontsize=9)
    ax.tick_params(labelsize=8); ax.spines[["top", "right"]].set_visible(False)
    return _fig_png(fig)


def png_map(groups, title):
    """groups: list of (label, lon array, lat array, color, size, marker)"""
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    for r in us_rings():
        pts = [(lon * MAP_KX, lat) for lon, lat in r if lon >= -126 and lat >= 24.3]
        if len(pts) > 2:
            xs, ys = zip(*pts)
            ax.fill(xs, ys, color="#E6EBF2", edgecolor="#8A9AB0", linewidth=0.5)
    for label, lon, lat, color, size, marker in groups:
        ax.scatter(np.asarray(lon) * MAP_KX, lat, s=size, c=color, marker=marker, label=label, edgecolors="none", alpha=0.85)
    ax.set_aspect("equal"); ax.axis("off"); ax.set_title(title, fontsize=11, loc="left")
    ax.legend(fontsize=7, frameon=False, loc="lower left", ncol=2)
    return _fig_png(fig)


def _method_blocks(key):
    d = DOCS[key]
    out = [("h", "Method and explanation"), ("p", d["purpose"])]
    for i, s in enumerate(d["steps"], 1):
        out.append(("p", f"Step {i}. {s}"))
    out.append(("p", "How to read the results. " + d["reading"]))
    if d["fields"]:
        out.append(("h", "Field dictionary"))
        out.append(("t", pd.DataFrame(d["fields"], columns=["Field", "Meaning", "Unit or range", "Source"]), "", 200))
    if d["formulas"]:
        out.append(("h", "Formulas"))
        for name, f, expl in d["formulas"]:
            out.append(("f", name, f, expl))
    return out


def _all_blocks(report):
    return report.blocks + _method_blocks(report.key)


def build_txt(report, meta) -> bytes:
    L = [EXPORT_BANNER, "", report.title.upper(), BRAND, BYLINE, f"Generated: {meta['generated']}",
         f"Data source: {meta['source']}", ""]
    for b in _all_blocks(report):
        if b[0] == "h":
            L += ["", b[1].upper(), "-" * len(b[1])]
        elif b[0] == "p":
            L.append(b[1])
        elif b[0] == "t":
            df, cap, mx = b[1], b[2], b[3]
            if cap:
                L.append(cap)
            L.append(df.head(mx).to_string(index=False))
            if len(df) > mx:
                L.append(f"(first {mx} of {len(df)} rows shown; see the CSV export for all rows)")
        elif b[0] == "c":
            L.append(f"[Chart: {b[2]}]")
        elif b[0] == "f":
            L += [f"{b[1]}:", f"    {b[2]}", f"    {b[3]}"]
    L += ["", EXPORT_BANNER]
    return "\n".join(L).encode("utf-8")


def build_csv(report) -> bytes:
    df = report.primary if report.primary is not None else pd.DataFrame({"Note": ["No tabular results for this module"]})
    return df.to_csv(index=False).encode("utf-8")


def build_docx(report, meta) -> bytes:
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.shared import Inches, Pt, RGBColor
    doc = Document()
    for s in doc.sections:
        s.left_margin = s.right_margin = Inches(0.8)
        for part in (s.header, s.footer):
            para = part.paragraphs[0]
            para.text = EXPORT_BANNER
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            para.runs[0].font.bold = True; para.runs[0].font.size = Pt(9)
    doc.styles["Normal"].font.name = "Calibri"; doc.styles["Normal"].font.size = Pt(10.5)
    doc.add_heading(report.title, 0)
    p = doc.add_paragraph(); r = p.add_run(BRAND + "\n" + BYLINE); r.italic = True
    doc.add_paragraph(f"Generated: {meta['generated']}. Data source: {meta['source']}.")
    for b in _all_blocks(report):
        if b[0] == "h":
            doc.add_heading(b[1], 1)
        elif b[0] == "p":
            doc.add_paragraph(b[1])
        elif b[0] == "t":
            df, cap, mx = b[1], b[2], b[3]
            if cap:
                doc.add_paragraph(cap).runs[0].bold = True
            d = df.head(mx)
            t = doc.add_table(rows=1, cols=len(d.columns)); t.style = "Table Grid"
            for i, c in enumerate(d.columns):
                cell = t.rows[0].cells[i]; cell.text = str(c)
                cell.paragraphs[0].runs[0].font.bold = True; cell.paragraphs[0].runs[0].font.size = Pt(8)
            for row in d.itertuples(index=False):
                cells = t.add_row().cells
                for i, v in enumerate(row):
                    cells[i].text = str(v)
                    if cells[i].paragraphs[0].runs:
                        cells[i].paragraphs[0].runs[0].font.size = Pt(8)
            if len(df) > mx:
                doc.add_paragraph(f"First {mx} of {len(df)} rows shown. See the CSV export for all rows.")
        elif b[0] == "c":
            try:
                doc.add_picture(io.BytesIO(b[1]()), width=Inches(6.4))
                if b[2]:
                    doc.add_paragraph(b[2]).runs[0].italic = True
            except Exception as e:  # noqa: BLE001
                doc.add_paragraph(f"Chart could not be rendered: {e}")
        elif b[0] == "f":
            doc.add_paragraph(b[1]).runs[0].bold = True
            fp = doc.add_paragraph(); fr = fp.add_run(b[2]); fr.font.name = "Consolas"; fr.font.size = Pt(9.5)
            fr.font.color.rgb = RGBColor(0x13, 0x31, 0x5C)
            doc.add_paragraph(b[3])
    buf = io.BytesIO(); doc.save(buf)
    return buf.getvalue()


def build_pdf(report, meta) -> bytes:
    from xml.sax.saxutils import escape
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
    ss_ = getSampleStyleSheet()
    body = ParagraphStyle("b", parent=ss_["BodyText"], fontSize=9.5, leading=13)
    cell = ParagraphStyle("c", parent=body, fontSize=7, leading=8.5)
    code = ParagraphStyle("f", parent=body, fontName="Courier", fontSize=8.5, leading=11, textColor=colors.HexColor("#13315C"))
    h1 = ParagraphStyle("h1", parent=ss_["Heading1"], fontSize=17, textColor=colors.HexColor("#0B2545"))
    h2 = ParagraphStyle("h2", parent=ss_["Heading2"], fontSize=12.5, textColor=colors.HexColor("#13315C"))

    def banner(canvas, doc_):
        canvas.saveState()
        canvas.setFillColor(colors.HexColor("#007A33"))
        w, h = letter
        canvas.rect(0, h - 18, w, 18, fill=1, stroke=0); canvas.rect(0, 0, w, 18, fill=1, stroke=0)
        canvas.setFillColor(colors.white); canvas.setFont("Helvetica-Bold", 8.5)
        canvas.drawCentredString(w / 2, h - 12.5, EXPORT_BANNER); canvas.drawCentredString(w / 2, 6, EXPORT_BANNER)
        canvas.setFillColor(colors.HexColor("#5A6B80")); canvas.setFont("Helvetica", 7.5)
        canvas.drawRightString(w - 0.7 * inch, 26, f"Page {doc_.page}")
        canvas.restoreState()

    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=letter, leftMargin=0.7 * inch, rightMargin=0.7 * inch,
                            topMargin=0.6 * inch, bottomMargin=0.6 * inch, title=report.title, author="Kalsnet (KNet) Consulting Group")
    flow = [Paragraph(escape(report.title), h1), Paragraph(f"<i>{escape(BRAND)}<br/>{escape(BYLINE)}</i>", body),
            Paragraph(escape(f"Generated: {meta['generated']}. Data source: {meta['source']}."), body), Spacer(1, 8)]
    avail = letter[0] - 1.4 * inch
    for b in _all_blocks(report):
        if b[0] == "h":
            flow.append(Paragraph(escape(b[1]), h2))
        elif b[0] == "p":
            flow.append(Paragraph(escape(b[1]), body)); flow.append(Spacer(1, 3))
        elif b[0] == "t":
            df, cap, mx = b[1], b[2], b[3]
            if cap:
                flow.append(Paragraph(f"<b>{escape(cap)}</b>", body))
            d = df.head(mx).astype(str)
            data = [[Paragraph(f"<b>{escape(str(c))}</b>", cell) for c in d.columns]]
            data += [[Paragraph(escape(v[:300]), cell) for v in row] for row in d.values.tolist()]
            t = Table(data, colWidths=[avail / max(1, len(d.columns))] * len(d.columns), repeatRows=1)
            t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#DCE4EE")),
                                   ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#A9B6C6")),
                                   ("VALIGN", (0, 0), (-1, -1), "TOP")]))
            flow.append(t)
            if len(df) > mx:
                flow.append(Paragraph(escape(f"First {mx} of {len(df)} rows shown. See the CSV export for all rows."), cell))
            flow.append(Spacer(1, 8))
        elif b[0] == "c":
            try:
                png = b[1]()
                img = Image(io.BytesIO(png))
                ratio = img.imageHeight / img.imageWidth
                img.drawWidth = avail; img.drawHeight = avail * ratio
                flow.append(img)
                if b[2]:
                    flow.append(Paragraph(f"<i>{escape(b[2])}</i>", cell))
                flow.append(Spacer(1, 8))
            except Exception as e:  # noqa: BLE001
                flow.append(Paragraph(escape(f"Chart could not be rendered: {e}"), body))
        elif b[0] == "f":
            flow.append(Paragraph(f"<b>{escape(b[1])}</b>", body))
            flow.append(Paragraph(escape(b[2]).replace("\n", "<br/>"), code))
            flow.append(Paragraph(escape(b[3]), body)); flow.append(Spacer(1, 4))
    doc.build(flow, onFirstPage=banner, onLaterPages=banner)
    return buf.getvalue()


# ===========================================================================
# SECTION: DOCUMENTATION FOR EVERY MODULE (purpose, steps, fields, formulas, diagram)
# Formulas use standard arithmetic notation: = equals, + plus, - minus, * times, / divided by.
# ===========================================================================
def _dot(body, rankdir="LR"):
    return ("digraph G { rankdir=" + rankdir + "; bgcolor=\"transparent\"; size=\"12,7\"; "
            "node [shape=box, style=\"rounded,filled\", fillcolor=\"#13243D\", color=\"#3A4D6B\", fontcolor=\"#E8EEF6\", "
            "fontname=\"Helvetica\", fontsize=11]; edge [color=\"#C9A227\", fontcolor=\"#9FB3C8\", fontname=\"Helvetica\", fontsize=9]; "
            + body + " }")


DOCS = {
    "overview": dict(
        short="Start here. What the platform does, how the modules fit together and how to use synthetic or real data.",
        purpose=("The platform helps national infrastructure owners and government partners find weak points before they "
                 "cause nationwide disruption. It maps how energy, water, communications, transportation, healthcare, finance "
                 "and defense assets depend on each other and on shared vendors. It then watches telemetry and incident records, "
                 "groups related incidents, and decides with evidence whether a group of failures is an independent technical "
                 "failure, an accidental cascade, or potentially coordinated cyber activity. It never labels simultaneous "
                 "outages a cyberattack without corroborating evidence."),
        steps=["Choose a data source: synthetic demonstration data (default) or uploaded real data in the Data Management module.",
               "The platform builds the dependency graph and knowledge graph from assets, dependencies and vendor relations.",
               "AI anomaly detection scores every telemetry reading against each asset's own normal behaviour.",
               "Incidents are correlated into clusters by time, dependency paths, shared vendors and location.",
               "Each cluster is assessed with an evidence weighted model and strict guardrails; analysts confirm or override.",
               "The digital twin simulates how failures spread, and risk scores rank every asset.",
               "Response playbooks and executive reports turn results into decisions. Every module exports PDF, Word, text and CSV."],
        reading="Use the menu on the left. Each module has five tabs: Results, How it works, Fields, Formulas and Export.",
        fields=[("Synthetic data", "Fictional national dataset generated in the application with five built in scenarios", "Seeded, repeatable", "Generator"),
                ("Uploaded data", "Real infrastructure records supplied by an authorized analyst or administrator", "CSV, XLSX or JSON", "User upload"),
                ("Classification banner", "Handling marking shown at the top of every screen and export", "Text", "Data Management")],
        formulas=[],
        diagram=_dot('A [label="Data sources\\nsynthetic or uploaded"]; B [label="Dependency graph\\nand knowledge graph"]; '
                     'C [label="AI anomaly\\ndetection"]; D [label="Incident\\ncorrelation"]; E [label="Evidence based\\nattribution"]; '
                     'F [label="Digital twin\\ncascade simulation"]; G2 [label="Risk scoring"]; H [label="Response and SOAR\\nplaybooks"]; '
                     'I [label="Executive dashboard\\nand reports"]; A->B; A->C; A->D; B->D; C->E; D->E; B->F; B->G2; F->G2; C->G2; '
                     'E->H; G2->I; E->I; H->I;'),
        data=["assets", "dependencies", "vendors", "vendor_relations", "incidents", "telemetry"],
    ),
    "dashboard": dict(
        short="National posture at a glance: key counts, risk map, assessed incident clusters, sector risk and top risks.",
        purpose=("The Executive Dashboard summarizes the whole platform for leaders. It shows how many assets are monitored, "
                 "how many incidents were correlated, how each correlated cluster was assessed, which sectors carry the most risk, "
                 "and which assets and vendors need attention first."),
        steps=["All other modules run first; the dashboard reads their results.",
               "Counts are taken from the active dataset and the correlation results.",
               "The map places each asset at its latitude and longitude, coloured by risk tier, with incidents ringed by assessment.",
               "Sector risk is the average asset risk score in each sector."],
        reading=("Red rings mark potentially coordinated cyber activity, amber rings accidental cascades, blue rings independent "
                 "failures and grey rings undetermined clusters. Undetermined means the platform refused to attribute without evidence."),
        fields=[("Assets monitored", "Number of infrastructure assets in the active dataset", "Count", "assets table"),
                ("Sectors", "Number of distinct critical infrastructure sectors", "Count", "assets.sector"),
                ("Incidents", "Number of incident records in the analysis window", "Count", "incidents table"),
                ("Correlated clusters", "Clusters that contain more than one incident", "Count", "Correlation module"),
                ("Potentially coordinated", "Clusters assessed as potentially coordinated cyber activity", "Count", "Attribution module"),
                ("Critical tier assets", "Assets with a risk score of 70 or more", "Count", "Risk module"),
                ("Mean risk", "Average risk score of the assets in a sector", "0 to 100", "Risk module")],
        formulas=[("Mean sector risk", "mean_risk(sector) = sum(risk_score of assets in sector) / number of assets in sector",
                   "Average composite risk of a sector."),
                  ("Critical tier count", "critical = count(assets where risk_score >= 70)", "Tier thresholds are set in the Risk module.")],
        diagram=_dot('A [label="Risk scores"]; B [label="Cluster assessments"]; C [label="Vendor concentration"]; '
                     'D [label="Executive dashboard"]; A->D; B->D; C->D;'),
        data=["assets", "incidents"],
    ),
    "graph": dict(
        short="Map of how assets depend on each other across sectors, with central nodes and single points of failure.",
        purpose=("The Dependency Graph turns assets and their dependencies into a directed network. An edge from A to B means B "
                 "needs A, for example power, communications, water, fuel, data or control. Graph AI measures show which assets "
                 "hold the network together and which ones would break it apart if they failed. The knowledge graph adds vendors, "
                 "sectors and states as connected entities."),
        steps=["Each asset becomes a node with its attributes; each dependency becomes a directed, weighted edge.",
               "Downstream reach counts how many assets depend on a node directly or indirectly.",
               "Betweenness centrality finds bridges that many dependency paths pass through.",
               "Supplier PageRank ranks assets by how much the rest of the network relies on them.",
               "Articulation points are single points of failure that split the network if removed.",
               "The knowledge graph explorer shows the neighbourhood of any asset or vendor."],
        reading="Large markers have many downstream dependents. Assets marked as single points of failure deserve redundancy first.",
        fields=[("asset_id", "Unique asset identifier", "Text", "assets"), ("source", "Supplying asset of a dependency", "asset_id", "dependencies"),
                ("target", "Dependent asset of a dependency", "asset_id", "dependencies"),
                ("dependency_type", "Kind of dependency such as Power, Communications, Water, Fuel, Data or Control", "Category", "dependencies"),
                ("strength", "How strongly the target needs the source", "0 to 1", "dependencies"),
                ("betweenness", "Share of shortest paths that pass through the asset", "0 to 1", "Computed"),
                ("supplier_pagerank", "Importance of the asset as a supplier", "0 to 1, sums to 1", "Computed"),
                ("downstream_count", "Assets reachable downstream", "Count", "Computed"),
                ("single_point_of_failure", "Articulation point in the undirected graph", "Yes or No", "Computed")],
        formulas=[("Downstream reach", "reach(v) = number of nodes t such that a directed path v to t exists", "Counts direct and indirect dependents."),
                  ("Betweenness centrality", "B(v) = sum over pairs s, t of [ paths_st(v) / paths_st ] / ((n - 1) * (n - 2))",
                   "paths_st is the number of shortest paths from s to t, paths_st(v) those passing through v, n the number of nodes."),
                  ("Supplier PageRank", "PR(v) = (1 - d) / N + d * sum over assets u that v supplies of PR(u) / suppliers(u),  d = 0.85",
                   "Computed on the reversed graph so importance flows from dependents back to their suppliers."),
                  ("Single point of failure", "v is critical if components(G without v) > components(G)", "Articulation point test on the undirected graph.")],
        diagram=_dot('G1 [label="Generation plant"]; T [label="Transmission\\nsubstation"]; D [label="Distribution\\nsubstation"]; '
                     'TC [label="Telecom central\\noffice"]; W [label="Water treatment"]; H [label="Hospital"]; P [label="911 PSAP"]; '
                     'V [label="Shared vendor", fillcolor="#3A1518"]; G1->T [label="power"]; T->D [label="power"]; D->TC [label="power"]; '
                     'D->W [label="power"]; D->H [label="power"]; TC->P [label="comms"]; TC->H [label="comms"]; W->H [label="water"]; '
                     'V->W [style=dashed, label="remote access"]; V->H [style=dashed]; V->T [style=dashed];'),
        data=["assets", "dependencies", "vendors", "vendor_relations"],
    ),
    "attribution": dict(
        short="Groups related incidents and decides: independent failure, accidental cascade, potentially coordinated cyber, or undetermined.",
        purpose=("This module correlates incidents across sectors like a SIEM and then weighs the evidence like an analyst. It "
                 "distinguishes three possibilities: independent technical failures, accidental cascading failures, and coordinated "
                 "or potentially coordinated cyberattacks. When the evidence does not support any of these, the cluster stays "
                 "Undetermined. Simultaneity, geographic spread and shared vendors are contextual only and can never by themselves "
                 "produce a cyber assessment."),
        steps=["Sort incidents by time.",
               "Link two incidents if they are inside the correlation window and are close in time, connected by a dependency path, share a vendor or are in the same state.",
               "Each connected group of linked incidents is a cluster.",
               "For each cluster measure the share of events showing each kind of evidence.",
               "Add weighted evidence to a prior log odds value and convert it to a probability of malicious activity.",
               "Apply decision rules with guardrails to choose the assessment and confidence.",
               "An analyst records the final determination with a written justification; confirmation of an attack is blocked unless at least two corroborating evidence categories exist."],
        reading=("Red bars push toward malicious activity and come from hard evidence. Amber bars are context and cannot decide the "
                 "outcome. Blue bars push toward a non malicious explanation. Collection gaps list evidence that was not observed and "
                 "should be gathered."),
        fields=[("cluster_id", "Identifier of a correlated group of incidents", "Text", "Computed"),
                ("n_incidents", "Number of incidents in the cluster", "Count", "Computed"),
                ("span_min", "Time from first to last incident", "Minutes", "Computed"),
                ("geo_spread_km", "Largest distance between two affected assets", "Kilometres", "Computed"),
                ("cascade_explained", "Share of follow on events explained by dependency propagation", "0 to 1", "Computed"),
                ("unconnected_pairs", "Share of asset pairs with no dependency path within 4 hops", "0 to 1", "Computed"),
                ("top_shared_vendor", "Vendor used by the largest share of affected assets", "vendor_id", "vendor_relations"),
                ("corroborating_categories", "Number of hard evidence categories present in at least 30 percent of events", "0 to 7", "Computed"),
                ("p_malicious", "Probability that activity is malicious from the evidence model", "0 to 1", "Computed"),
                ("assessment", "Final class chosen by the decision rules", "Category", "Computed"),
                ("confidence", "High, Moderate, Low or Not assessed", "Category", "Computed"),
                ("ioc_match", "Threat intelligence indicator matched on the asset", "Yes or No", "incidents"),
                ("malware_signature", "Name of detected malware signature", "Text", "incidents"),
                ("unauthorized_config_change", "Configuration or setpoint changed without authorization", "Yes or No", "incidents"),
                ("auth_anomaly", "Irregular or failed logons", "Yes or No", "incidents"),
                ("attack_technique", "MITRE ATTACK for ICS technique identifier", "Text such as T0836", "incidents"),
                ("vendor_remote_session", "Third party remote session active at the time", "Yes or No", "incidents"),
                ("telemetry_precursor", "Cyber type telemetry anomaly in the 24 hours before the incident", "Yes or No", "Anomaly module"),
                ("physical_cause", "Documented physical or equipment cause", "Text", "incidents"),
                ("weather_alert", "Active weather alert", "Yes or No", "incidents"),
                ("maintenance_window", "Event inside planned maintenance", "Yes or No", "incidents")],
        formulas=[("Correlation link", "link(i, j) if dt <= W and (dt <= S or hops(i, j) <= 4 or (shared_vendor and dt <= 2 * S) or (same_state and dt <= 120))",
                   "dt is the time between incidents in minutes, W the correlation window, S the simultaneity threshold. Clusters are connected components of links."),
                  ("Evidence coverage", "v_k = (events in cluster showing evidence k) / (events in cluster)", "Share of events with each evidence type."),
                  ("Corroborating contribution", "c_k = w_k * min(1, v_k / 0.5)", "Full weight is reached when half of the events show the evidence."),
                  ("Exculpatory contribution", "c_k = w_k * v_k  (w_k is negative)", "Physical, weather, cascade and maintenance explanations lower the score."),
                  ("Contextual contribution", "c_k = w_k when its condition holds, otherwise 0", "Shared vendor, synchronized off hours timing, multi sector spread."),
                  ("Log odds", "L = ln(p0 / (1 - p0)) + sum of all c_k,   p0 = 0.05", "Starts from a low prior probability of 5 in 100."),
                  ("Probability malicious", "P = 1 / (1 + exp(-L))", "Logistic transform of the log odds."),
                  ("Cascade explained", "cascade = explained_followers / (n - 1)",
                   "A follow on event is explained if an earlier event reaches it within 4 hops and it has no independent cause of its own."),
                  ("Geographic spread", "d = 2 * R * asin( sqrt( sin^2(dlat / 2) + cos(lat1) * cos(lat2) * sin^2(dlon / 2) ) ),  R = 6371 km",
                   "Haversine distance; the spread is the largest pairwise distance."),
                  ("Decision rules", "1. Single event: cyber related if corroborating >= 2, else independent.\n"
                                     "2. Potentially coordinated if corroborating >= 2 and P >= 0.5.\n"
                                     "3. Accidental cascade if cascade >= 0.6 and corroborating < 2.\n"
                                     "4. Independent if weather share >= 0.5 or physical share >= 0.6 and corroborating < 2.\n"
                                     "5. Otherwise Undetermined.",
                   "Rules are applied in order. Contextual indicators alone can never reach rule 2."),
                  ("Confidence", "High if corroborating >= 4 and P >= 0.9; Moderate if corroborating >= 3; otherwise Low",
                   "For cascades, High when cascade >= 0.85.")],
        diagram=_dot('A [label="Incident cluster"]; B [label="Corroborating evidence\\n2 or more categories?"]; '
                     'C [label="Probability\\n0.5 or more?"]; D [label="Potentially coordinated\\ncyber activity", fillcolor="#5A1A1E"]; '
                     'E [label="Dependency explains\\n60 of 100 follow on events?"]; F [label="Accidental cascading\\nfailure", fillcolor="#5A3D0E"]; '
                     'G1 [label="Weather or physical\\ncommon cause?"]; H [label="Independent technical or\\nenvironmental failure", fillcolor="#123A5E"]; '
                     'I [label="Undetermined\\ndo not attribute", fillcolor="#3A4250"]; J [label="Analyst determination\\nand audit log"]; '
                     'A->B; B->C [label="yes"]; C->D [label="yes"]; B->E [label="no"]; C->E [label="no"]; E->F [label="yes"]; '
                     'E->G1 [label="no"]; G1->H [label="yes"]; G1->I [label="no"]; D->J; F->J; H->J; I->J;', "TB"),
        data=["incidents", "assets", "dependencies", "vendor_relations", "telemetry"],
    ),
    "anomaly": dict(
        short="AI model that flags unusual telemetry, and cyber type precursors such as login failures and data egress spikes.",
        purpose=("Each asset has its own normal pattern of load, latency, error rate, authentication failures, outbound data and "
                 "processor use. The module converts every reading into a robust z score against the asset's own history and "
                 "uses an Isolation Forest to find readings that are unusual in combination. Anomalies driven by authentication "
                 "failures or outbound data are flagged as cyber type signals and feed the attribution model as precursors."),
        steps=["Group telemetry by asset and compute the median and median absolute deviation of every metric.",
               "Convert each reading to a robust z score and cap it at 50.",
               "Train an Isolation Forest on all z score vectors and score every reading.",
               "Flag the most unusual readings as anomalies using the contamination setting.",
               "Mark an anomaly as a cyber type signal when authentication failures or outbound data exceed 4 robust deviations.",
               "Mark an incident as having a precursor when its asset showed a cyber type signal in the previous 24 hours."],
        reading="The heatmap shows when and where anomalies concentrate. The drill down plots z scores with incidents as dashed lines.",
        fields=[("timestamp", "Time of the reading", "Date and time", "telemetry"), ("load_pct", "Asset load", "0 to 100 percent of capacity", "telemetry"),
                ("latency_ms", "Network or control latency", "Milliseconds", "telemetry"), ("error_rate", "Error rate", "Errors per 100 operations", "telemetry"),
                ("auth_failures", "Failed authentication attempts", "Count per hour", "telemetry"),
                ("net_out_mb", "Outbound network data", "Megabytes per hour", "telemetry"), ("cpu_pct", "Processor utilisation", "0 to 100", "telemetry"),
                ("z_metric", "Robust z score of a metric", "Standard deviations", "Computed"),
                ("anomaly_score", "Normalized Isolation Forest score", "0 to 1, higher is more unusual", "Computed"),
                ("is_anomaly", "Reading in the most unusual fraction", "Yes or No", "Computed"),
                ("driver", "Metric with the largest absolute z score", "Metric name", "Computed"),
                ("cyber_signal", "Anomaly driven by authentication or outbound data", "Yes or No", "Computed")],
        formulas=[("Median absolute deviation", "MAD = median( |x - median(x)| ) for each asset and metric", "Robust spread that ignores outliers."),
                  ("Robust z score", "z = (x - median) / (1.4826 * MAD),  capped to the range -50 to 50", "1.4826 makes MAD comparable to a standard deviation."),
                  ("Isolation Forest score", "s(x) = 2 ^ ( -E[h(x)] / c(n) ),  c(n) = 2 * H(n - 1) - 2 * (n - 1) / n",
                   "h(x) is the path length that isolates x in a random tree, H the harmonic number, n the sample size. Short paths mean unusual points."),
                  ("Normalized score", "score = (s - min(s)) / (max(s) - min(s))", "Rescaled to 0 to 1 for display."),
                  ("Cyber signal", "cyber = is_anomaly and max(z_auth_failures, z_net_out_mb) > 4", "Behaviour typical of credential attacks or data staging."),
                  ("Precursor", "precursor(incident) = any cyber signal on the same asset with 0 < hours before incident <= 24", "Feeds the attribution evidence.")],
        diagram=_dot('A [label="Telemetry\\nper asset"]; B [label="Median and MAD\\nper asset"]; C [label="Robust z scores"]; '
                     'D [label="Isolation Forest"]; E [label="Anomaly flag"]; F [label="Cyber type signal"]; '
                     'G1 [label="Precursor to incident"]; A->B->C->D->E->F->G1;'),
        data=["telemetry", "assets", "incidents"],
    ),
    "cascade": dict(
        short="Digital twin that simulates how a failure spreads through dependencies, and tests redundancy and hardening.",
        purpose=("The digital twin answers what happens if a chosen asset fails. It runs many random simulations in which "
                 "failures spread along dependency edges, weakened by each dependent asset's redundancy. It reports the expected "
                 "number of failed assets, the expected population affected, the sectors involved and the time profile, and it "
                 "recommends the five assets whose hardening reduces impact the most."),
        steps=["Choose one or more initiating failures or a preset scenario.",
               "For every edge compute the chance that a failed supplier knocks out the dependent asset.",
               "At each step, every surviving asset fails with a probability that combines all of its failed suppliers.",
               "Repeat the run many times and average the outcomes.",
               "Optionally raise redundancy everywhere or harden the recommended assets and compare against the baseline."],
        reading="The band on the growth chart covers the middle 80 runs out of every 100. Mean step is when an asset typically fails.",
        fields=[("strength", "How strongly a dependent needs its supplier", "0 to 1", "dependencies"),
                ("redundancy", "Ability of an asset to ride through a supplier failure", "0 to 1", "assets"),
                ("population_served", "People who rely on the asset", "People", "assets"),
                ("p_fail", "Share of simulation runs in which the asset failed", "0 to 1", "Computed"),
                ("mean_step", "Average step at which the asset failed", "Steps, about hours", "Computed"),
                ("runs", "Number of Monte Carlo simulations", "50 to 1000", "User setting"),
                ("steps", "Number of propagation steps per run", "3 to 24", "User setting")],
        formulas=[("Edge transmission", "W(u, v) = strength(u, v) * (1 - redundancy(v))", "Chance that a failed supplier u brings down dependent v."),
                  ("Failure probability per step", "P(v fails) = 1 - product over failed suppliers u of (1 - W(u, v))", "Independent chances combine."),
                  ("Expected failed assets", "E[failed] = sum over assets of p_fail(v)", "Average across runs."),
                  ("Expected population affected", "E[pop] = sum over assets of p_fail(v) * population_served(v)", "People affected on average."),
                  ("Analytic propagation", "p(v, t + 1) = max( p(v, t), 1 - product over u of (1 - p(u, t) * W(u, v)) )",
                   "Fast approximation used for risk scoring and hardening search."),
                  ("Hardening", "W(u, v) is multiplied by 0.15 for every hardened asset v", "Represents backup power, dual feeds or spares."),
                  ("Greedy hardening search", "repeat 5 times: pick the asset whose hardening most lowers sum of p(v) * population(v)", "Recommends where investment helps most."),
                  ("Redundancy uplift", "redundancy_new(v) = min(0.95, redundancy(v) + uplift)", "What if every asset had more redundancy.")],
        diagram=_dot('A [label="Initiating failure"]; B [label="Failed set F"]; C [label="For each surviving asset v\\nP = 1 - product (1 - W(u,v))"]; '
                     'D [label="Random draw"]; E [label="Update F"]; F2 [label="Repeat for each step"]; G1 [label="Average across runs"]; '
                     'A->B->C->D->E->F2; F2->C [style=dashed]; F2->G1;'),
        data=["assets", "dependencies"],
    ),
    "vendors": dict(
        short="Finds vendors and service providers that silently connect many sectors, and hidden couplings between assets.",
        purpose=("Many outages that look unrelated share a hidden third party, such as a remote access provider, timing source, "
                 "cloud host or controller manufacturer. This module ranks vendors by systemic concentration and lists asset pairs "
                 "in different sectors that have no physical dependency path but share a vendor."),
        steps=["Join vendor relations to assets and to the systemic impact of each asset.",
               "For each vendor count dependent assets, sectors, states and remote access connections, and sum criticality and downstream population.",
               "Normalize each measure across vendors and combine them into a systemic score.",
               "For a selected vendor list cross sector asset pairs with no dependency path in either direction."],
        reading="A vendor with a high score across three or more sectors is a systemic cross sector dependency and a priority for supply chain controls.",
        fields=[("vendor_id", "Vendor identifier", "Text", "vendors"), ("vendor_name", "Vendor name (fictional in synthetic data)", "Text", "vendors"),
                ("vendor_type", "Kind of service provided", "Text", "vendors"), ("assets", "Dependent assets", "Count", "Computed"),
                ("sectors", "Distinct sectors served", "Count", "Computed"), ("states", "Distinct states served", "Count", "Computed"),
                ("remote_access_assets", "Assets where the vendor has remote access", "Count", "vendor_relations"),
                ("population_exposed", "Population served by dependent assets", "People", "Computed"),
                ("systemic_score", "Composite concentration score", "0 to 100", "Computed"),
                ("systemic_flag", "Systemic cross sector, cross sector or sector contained", "Category", "Computed")],
        formulas=[("Normalization", "n(x) = (x - min over vendors) / (max over vendors - min over vendors)", "Puts every measure on a 0 to 1 scale."),
                  ("Systemic score", "S = 100 * (0.30 * n(criticality_sum) + 0.25 * n(sectors) + 0.15 * n(states) + 0.15 * n(remote_access) + 0.15 * n(downstream_population))",
                   "Weighted concentration of a vendor across the nation."),
                  ("Systemic flag", "Systemic cross sector if sectors >= 3 and S >= 50; Cross sector if sectors >= 3; otherwise Sector contained", "Classification of the vendor."),
                  ("Hidden coupling", "pair (a, b) if vendor(a) = vendor(b) and sector(a) != sector(b) and no directed path between a and b", "Coupling invisible on a dependency map.")],
        diagram=_dot('V [label="Shared vendor", fillcolor="#3A1518"]; A [label="Hospital\\nBoston"]; B [label="Water pumping\\nIndianapolis"]; '
                     'C [label="Substation\\nHouston"]; D [label="ATC facility\\nNew York"]; V->A; V->B; V->C; V->D; '
                     'A->B [style=invis]; note [shape=note, label="No physical dependency path\\nbetween these assets"];', "TB"),
        data=["vendors", "vendor_relations", "assets", "dependencies"],
    ),
    "risk": dict(
        short="Explainable 0 to 100 risk score for every asset, with adjustable weights and a factor breakdown.",
        purpose=("The risk score combines eight factors into a single explainable number so that limited resources go to the "
                 "assets that matter most. Weights can be tuned to an agency's risk appetite, and every score can be broken down "
                 "into the points each factor contributes."),
        steps=["Compute each factor on a 0 to 1 scale.",
               "Multiply each factor by its weight, add the results and scale to 100.",
               "Assign a tier and name the factor that contributes the most points."],
        reading="Critical is 70 or more, High 55 or more, Elevated 40 or more, Guarded below 40.",
        fields=[("criticality", "Importance of the asset to national functions", "1 to 5", "assets"),
                ("internet_exposed", "Asset reachable from the internet", "Yes or No", "assets"),
                ("patch_lag_days", "Days behind current security patches", "Days", "assets"),
                ("known_vulns", "Known unpatched vulnerabilities", "Count", "assets"),
                ("redundancy", "Ability to ride through supplier failure", "0 to 1", "assets"),
                ("expected_pop_impact", "Expected population affected downstream if the asset fails", "People", "Digital twin"),
                ("risk_score", "Composite score", "0 to 100", "Computed"), ("risk_tier", "Critical, High, Elevated or Guarded", "Category", "Computed"),
                ("top_driver", "Factor that contributes the most points", "Factor name", "Computed")],
        formulas=[("Risk score", "risk = 100 * sum(w_k * f_k) / sum(w_k)", "Default weights: criticality 0.18, systemic impact 0.20, centrality 0.10, exposure 0.15, third party 0.12, resilience gap 0.10, live anomaly 0.08, incident pressure 0.07."),
                  ("Criticality factor", "f = (criticality - 1) / 4", "Maps 1 to 5 onto 0 to 1."),
                  ("Systemic impact factor", "f = n( ln(1 + expected_pop_impact) )", "Log scale so very large populations do not swamp other factors."),
                  ("Centrality factor", "f = n( betweenness + 5 * supplier_pagerank )", "Graph importance."),
                  ("Exposure factor", "f = 0.4 * internet_exposed + 0.3 * min(patch_lag_days / 180, 1) + 0.3 * min(known_vulns / 10, 1)", "Cyber attack surface."),
                  ("Third party factor", "f = max over the asset's vendors of systemic_score / 100", "Inherited vendor concentration."),
                  ("Resilience gap factor", "f = 1 - redundancy", "Lower redundancy means more risk."),
                  ("Live anomaly factor", "f = max anomaly_score in the last 48 hours", "Current unusual behaviour."),
                  ("Incident pressure factor", "f = min( sum of incident severity / 10, 1 )", "Recent incident load."),
                  ("Tier", "Critical if risk >= 70; High if >= 55; Elevated if >= 40; otherwise Guarded", "Fixed thresholds."),
                  ("Top driver", "argmax over k of w_k * f_k", "Factor with the largest contribution.")],
        diagram=_dot('F1 [label="Criticality"]; F2 [label="Systemic impact"]; F3 [label="Centrality"]; F4 [label="Exposure"]; '
                     'F5 [label="Third party"]; F6 [label="Resilience gap"]; F7 [label="Live anomaly"]; F8 [label="Incident pressure"]; '
                     'R [label="Weighted sum\\nscaled to 100"]; T [label="Tier and top driver"]; F1->R; F2->R; F3->R; F4->R; F5->R; F6->R; F7->R; F8->R; R->T;'),
        data=["assets", "dependencies", "vendor_relations", "telemetry", "incidents"],
    ),
    "response": dict(
        short="Sector aware response playbooks for each assessed cluster, with a human approval queue.",
        purpose=("For every assessed cluster the platform proposes response actions drawn from playbooks for the assessment class, "
                 "plus coordination steps for each sector involved. Actions that could be automated by a SOAR platform are marked, "
                 "but every action requires human approval. In this demonstration no action is executed against any real system."),
        steps=["Select a cluster.", "The playbook for its assessment class is loaded.",
               "Sector partner coordination steps are added for every sector in the cluster.",
               "An analyst approves or rejects actions; each decision is written to the audit log."],
        reading="P1 actions should start immediately, P2 within the operational period, P3 as follow up.",
        fields=[("phase", "Contain, Investigate, Coordinate, Recover, Communicate, Monitor or Improve", "Category", "Playbook"),
                ("priority", "P1 immediate, P2 operational period, P3 follow up", "Category", "Playbook"),
                ("action", "Recommended action", "Text", "Playbook"), ("soar_automatable", "Can be orchestrated by SOAR", "Yes or No", "Playbook"),
                ("approval_required", "Human approval needed", "Always Yes", "Policy"), ("status", "Proposed, Approved (simulated) or Rejected", "Category", "Analyst")],
        formulas=[("Playbook selection", "actions = playbook(assessment) + partner_steps(sector) for each sector in the cluster", "Partner steps are skipped for independent failures."),
                  ("Ordering", "sort by priority (P1, P2, P3) then by phase order", "Highest urgency first.")],
        diagram=_dot('A [label="Assessed cluster"]; B [label="Playbook for class"]; C [label="Sector partner steps"]; '
                     'D [label="Proposed actions"]; E [label="Analyst approval"]; F [label="Audit log"]; A->B->D; A->C->D; D->E->F;'),
        data=["incidents", "assets"],
    ),
    "report": dict(
        short="Combined executive brief across every module, ready to brief leadership.",
        purpose=("The executive report brings together the bottom line, cluster assessments, top risks, systemic vendors and "
                 "priority recommendations in a single brief suitable for DHS and CISA, DOE, FAA, DISA, DoD and sector partners."),
        steps=["Results from all modules are collected.", "The bottom line is written from the counts and assessments.",
               "Tables for clusters, top risks and vendors are added.", "Analytic standards close the report."],
        reading="Assessments are probabilistic. Undetermined clusters are deliberately not attributed.",
        fields=[("Bottom line", "Short summary of the most important findings", "Text", "Computed"),
                ("Cluster table", "Multi event clusters with assessment and probability", "Table", "Attribution module"),
                ("Top risks", "Ten highest risk assets", "Table", "Risk module"), ("Systemic vendors", "Six most concentrated vendors", "Table", "Vendor module")],
        formulas=[],
        diagram=_dot('A [label="All modules"]; B [label="Bottom line"]; C [label="Assessments"]; D [label="Risks and vendors"]; '
                     'E [label="Recommendations"]; F [label="Executive brief"]; A->B->F; A->C->F; A->D->F; A->E->F;'),
        data=["assets", "incidents"],
    ),
    "data": dict(
        short="Generate synthetic data or upload real telemetry and incident records, with templates and validation.",
        purpose=("This module controls the data used by every other module. The synthetic generator creates a fictional national "
                 "dataset with five known scenarios so the analytics can be demonstrated against known answers. Authorized "
                 "analysts and administrators can upload real data instead. Uploads are validated, stay in the user's session "
                 "memory only and are never written to disk or shared with other users."),
        steps=["Download the template for each table.", "Fill the required columns; optional columns receive documented defaults.",
               "Upload each file. The platform validates columns, types, timestamps and identifiers.",
               "Activate the uploaded dataset. Assets and dependencies are required; the other tables are optional.",
               "Set the handling banner that matches the data owner's marking guidance."],
        reading="Synthetic scenarios: scattered faults, a Columbus cascade, a Central region ice storm, three unexplained simultaneous outages and a vendor based coordinated intrusion.",
        fields=[], formulas=[],
        diagram=_dot('A [label="Template"]; B [label="Upload file"]; C [label="Validate columns\\nand types"]; D [label="Stage table"]; '
                     'E [label="Activate dataset"]; F [label="All modules\\nrecompute"]; A->B->C->D->E->F;'),
        data=["assets", "dependencies", "vendors", "vendor_relations", "incidents", "telemetry"],
    ),
    "audit": dict(
        short="Record of sign ins, uploads, analyst determinations, simulations, approvals and exports.",
        purpose="The audit log records every security relevant action in the session so decisions can be reviewed after action.",
        steps=["Actions are recorded with a UTC time, user and detail.", "Analysts and administrators can view and export the log."],
        reading="In production the log is forwarded to the agency SIEM.",
        fields=[("timestamp_utc", "Time of the action", "UTC date and time", "System"), ("user", "Signed in user", "Text", "System"),
                ("action", "Kind of action", "Text", "System"), ("detail", "Details of the action", "Text", "System")],
        formulas=[],
        diagram=_dot('A [label="User action"]; B [label="Audit record"]; C [label="Export or SIEM"]; A->B->C;'),
        data=[],
    ),
}

UPLOAD_DOCS = {
    "assets": "Infrastructure assets. Required: asset_id, name, asset_type, sector, state, lat, lon, criticality (1 to 5).",
    "dependencies": "Directed dependencies. Required: source, target, dependency_type. Optional strength 0 to 1.",
    "vendors": "Third party vendors. Required: vendor_id, vendor_name. Optional vendor_type.",
    "vendor_relations": "Which asset uses which vendor. Required: asset_id, vendor_id. Optional service, remote_access.",
    "incidents": "Incident records. Required: incident_id, timestamp, asset_id, incident_type, severity (1 to 5). Optional evidence fields.",
    "telemetry": "Hourly or more frequent readings. Required: timestamp, asset_id. Optional metrics load_pct, latency_ms, error_rate, auth_failures, net_out_mb, cpu_pct.",
}


# ===========================================================================
# SECTION: USER INTERFACE
# ===========================================================================
st.set_page_config(page_title="KNet Critical Infrastructure Cyber Resilience Platform", layout="wide")

GOLD = "#C9A227"
SYNTH_BANNER = "UNCLASSIFIED. DEMONSTRATION. SYNTHETIC DATA."
PLOTLY_CFG = {"displayModeBar": False}


def compat_dataframe(df, **kw):  # noqa
    """st.dataframe that works on old and new Streamlit versions."""
    height = kw.pop("height", None)
    extra = {"height": height} if height else {}
    try:
        return st.dataframe(df, width="stretch", **kw, **extra)
    except Exception:  # noqa: BLE001  older Streamlit: width must be an int
        return st.dataframe(df, use_container_width=True, **kw, **extra)


def compat_tabs(labels, key):
    try:
        return st.tabs(labels, key=key, default=labels[0])
    except TypeError:  # older Streamlit: tabs have no key or default
        return st.tabs(labels)
TABLE_LABELS = {"assets": "Assets", "dependencies": "Dependencies", "vendors": "Vendors",
                "vendor_relations": "Vendor relations", "incidents": "Incidents", "telemetry": "Telemetry"}

st.markdown(f"""
<style>
.block-container {{padding-top: 2.8rem;}}
.knet-banner {{position: fixed; top: 0; left: 0; right: 0; z-index: 999990; text-align: center; font-weight: 700;
  font-size: 12px; letter-spacing: .1em; padding: 3px 0; color: #fff;}}
.knet-title {{font-size: 1.5rem; font-weight: 800; line-height: 1.25}}
.kpi {{background: linear-gradient(160deg,#13315C,#0B2545); border: 1px solid #23406b; border-radius: 10px; padding: 12px 14px; margin-bottom: 8px}}
.kpi .v {{font-size: 1.6rem; font-weight: 800; color: #fff}} .kpi .l {{font-size: .76rem; color: #9fb3c8; text-transform: uppercase; letter-spacing: .06em}}
.pill {{display:inline-block; padding: 2px 10px; border-radius: 12px; color: #0A1628; font-size: .8rem; font-weight: 700}}
.guard {{border: 1px solid #C9A227; background: rgba(201,162,39,0.10); padding: 10px 14px; border-radius: 8px; font-size: .92rem}}
.modinfo {{background: rgba(76,155,232,0.10); border:1px solid rgba(76,155,232,0.45); border-radius:8px; padding:10px; font-size:.84rem}}
</style>""", unsafe_allow_html=True)


# --------------------------------------------------------------------------- state
def init_state():
    ss_ = st.session_state
    for k, v in dict(audit=[], user=None, role=None, decisions={}, soar={}, staged={}, data_version=0,
                     banner=SYNTH_BANNER, exports={}, source_kind="synthetic").items():
        ss_.setdefault(k, v)
    if "data" not in ss_:
        ss_.data = generate(seed=42)
        ss_.data_label = "Synthetic national dataset, seed 42"


init_state()
ss = st.session_state
USERS, USING_DEMO_CREDS = load_users(st.secrets)


def audit(action, detail=""):
    audit_event(ss.audit, ss.user, action, detail)


def results(window_min=240, simul_min=45, contamination=0.01):
    key = (ss.data_version, window_min, simul_min, contamination)
    if ss.get("_res_key") != key:
        with st.spinner("Running graph analytics, AI anomaly detection and correlation"):
            ss._res = run_pipeline(ss.data, window_min, simul_min, contamination)
            ss._res_key = key
            ss.exports = {}
    return ss._res


def set_dataset(data, label, kind, banner):
    ss.data, ss.data_label, ss.source_kind, ss.banner = data, label, kind, banner
    ss.data_version += 1
    ss.decisions, ss.soar, ss.exports = {}, {}, {}


# --------------------------------------------------------------------------- helpers
def style_fig(fig, h=420):
    fig.update_layout(height=h, margin=dict(l=10, r=10, t=40, b=10),
                      legend=dict(orientation="h", yanchor="top", y=-0.08, title=None))
    return fig


def show(fig):
    try:
        st.plotly_chart(fig, width="stretch", config=PLOTLY_CFG)
    except Exception:  # noqa: BLE001  older Streamlit
        st.plotly_chart(fig, use_container_width=True, config=PLOTLY_CFG)


def kpi(col, label, value):
    col.markdown(f"<div class='kpi'><div class='v'>{value}</div><div class='l'>{label}</div></div>", unsafe_allow_html=True)


def pill(text):
    color = {**CLASS_COLORS, **TIER_COLORS}.get(text, "#9BA3AF")
    return f"<span class='pill' style='background:{color}'>{text}</span>"


def table(df, height=None):
    kw = {"hide_index": True}
    if height:
        kw["height"] = height
    compat_dataframe(pretty_cols(df), **kw)


def pct(x):
    return f"{x * 100:.1f} percent"


banner_color = "#007A33" if ss.banner == SYNTH_BANNER else "#502B85"
st.markdown(f"<div class='knet-banner' style='background:{banner_color}'>{ss.banner}</div>", unsafe_allow_html=True)


# --------------------------------------------------------------------------- sidebar
PAGES = {
    "Overview and Guide": "overview", "Executive Dashboard": "dashboard", "Dependency Graph": "graph",
    "Incident Correlation and Attribution": "attribution", "AI Anomaly Detection": "anomaly",
    "Cascade Simulation (Digital Twin)": "cascade", "Third Party Dependencies": "vendors", "Risk Scoring": "risk",
    "Response and SOAR": "response", "Executive Report": "report", "Data Management": "data", "Audit Log": "audit",
}
with st.sidebar:
    st.markdown(f"<div style='font-weight:800;font-size:1.15rem'>KNet CI Resilience Platform</div>"
                f"<div style='color:#A8841A;font-size:.8rem;font-weight:700'>Kalsnet (KNet) Consulting Group</div>",
                unsafe_allow_html=True)
    st.write("")
    page = st.radio("Modules", list(PAGES))
    st.markdown(f"<div class='modinfo'><b>About this module</b><br>{DOCS[PAGES[page]]['short']}</div>", unsafe_allow_html=True)
    st.write("")
    with st.expander("Correlation settings"):
        window = st.slider("Correlation window in minutes", 30, 720, 240, 30)
        simul = st.slider("Simultaneity threshold in minutes", 5, 180, 45, 5)
        contam = st.select_slider("Anomaly contamination share", [0.005, 0.01, 0.02, 0.05], value=0.01)
        st.caption("The correlation window limits how far apart two incidents can be and still be linked. The simultaneity "
                   "threshold links any two incidents that close together. Contamination is the share of telemetry readings "
                   "the AI model flags as anomalies.")
    if ss.user:
        st.success(f"Signed in: {ss.user} ({ss.role})")
        if st.button("Sign out"):
            audit("logout"); ss.user = ss.role = None; st.rerun()
    else:
        with st.form("login"):
            st.caption("Sign in for analyst and administrator functions")
            u = st.text_input("Username")
            p = st.text_input("Password", type="password")
            if st.form_submit_button("Sign in"):
                role = verify(USERS, u.strip(), p)
                if role:
                    ss.user, ss.role = u.strip(), role
                    audit("login", f"role {role}"); st.rerun()
                else:
                    audit_event(ss.audit, u or "unknown", "login failed")
                    st.error("Invalid credentials")
        if USING_DEMO_CREDS:
            st.caption("Demo credentials: analyst with password knet-analyst, admin with password knet-admin. "
                       "Configure real users in the Streamlit secrets file before any non demo use.")
    st.caption("Developed by Randy Singh, Kalsnet (KNet) Consulting Group")

R = results(window, simul, contam)
A = ss.data["assets"]
G = R["G"]
VNAME = ss.data["vendors"].set_index("vendor_id")["vendor_name"].to_dict() if len(ss.data["vendors"]) else {}
ANAME = A.set_index("asset_id")["name"].to_dict()


# --------------------------------------------------------------------------- shared panels
def upload_widgets(tables, prefix):
    """Upload, validate and stage the given tables. Returns nothing; staged tables live in session state."""
    for kind in tables:
        st.markdown(f"**{TABLE_LABELS[kind]}**. {UPLOAD_DOCS[kind]}")
        c1, c2 = st.columns([1, 3])
        c1.download_button("Template", template_csv(kind), f"template_{kind}.csv", key=f"{prefix}_t_{kind}")
        f = c2.file_uploader(f"Upload {TABLE_LABELS[kind].lower()} file", type=["csv", "xlsx", "json"],
                             key=f"{prefix}_u_{kind}", label_visibility="collapsed")
        if f is not None:
            df, errs, warns = validate(kind, f.getvalue(), f.name)
            for e in errs:
                st.error(e)
            for w_ in warns:
                st.caption("Note: " + w_)
            if df is not None:
                if ss.staged.get(kind) is None or len(ss.staged[kind]) != len(df):
                    audit("upload staged", f"{kind}: {f.name} ({len(df)} rows)")
                ss.staged[kind] = df
                st.success(f"Validated {len(df):,} rows. Staged.")


def activate_uploads(marking):
    base = ss.data if ss.source_kind == "uploaded" else None
    empty = {k: pd.DataFrame(columns=SCHEMAS[k]["required"] + list(SCHEMAS[k]["defaults"])) for k in SCHEMAS}
    new = {}
    for k in SCHEMAS:
        if k in ss.staged:
            new[k] = ss.staged[k]
        elif base is not None:
            new[k] = base[k]
        else:
            new[k] = empty[k]
    if new["assets"].empty or new["dependencies"].empty:
        st.error("Assets and dependencies are required before the uploaded dataset can be activated.")
        return
    for m in cross_validate(new):
        st.caption("Note: " + m)
    set_dataset(new, "Uploaded customer dataset", "uploaded", marking)
    ss.staged = {}
    audit("dataset activated", f"tables {sorted(k for k in new if len(new[k]))}")
    st.rerun()


def data_panel(key):
    needs = DOCS[key]["data"]
    if not needs:
        return
    with st.expander(f"Data source for this module: {ss.data_label}", expanded=False):
        st.markdown("Tables used by this module and rows currently loaded:")
        compat_dataframe(pd.DataFrame({"Table": [TABLE_LABELS[t] for t in needs],
                                   "Rows loaded": [f"{len(ss.data[t]):,}" for t in needs]}), hide_index=True)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Use synthetic demonstration data**")
            seed = st.number_input("Random seed", 1, 99999, 42, key=f"seed_{key}")
            if st.button("Generate synthetic data", key=f"gen_{key}"):
                set_dataset(generate(seed=int(seed)), f"Synthetic national dataset, seed {seed}", "synthetic", SYNTH_BANNER)
                audit("dataset synthetic", f"seed {seed}"); st.rerun()
        with c2:
            st.markdown("**Upload real data for this module**")
            if not can(ss.role, "upload"):
                st.info("Sign in as an analyst or administrator to upload real data.")
            else:
                upload_widgets(needs, f"p_{key}")
                if ss.staged:
                    st.caption("Staged: " + ", ".join(TABLE_LABELS[k] for k in ss.staged))
                    marking = st.text_input("Handling banner", "UNCLASSIFIED. CUSTOMER SUPPLIED DATA. VERIFY MARKING.", key=f"mk_{key}")
                    if st.button("Activate uploaded data", key=f"act_{key}", type="primary"):
                        activate_uploads(marking)


def explain_tab(key):
    d = DOCS[key]
    st.markdown("#### Purpose")
    st.write(d["purpose"])
    st.markdown("#### How it works")
    st.graphviz_chart(d["diagram"])
    for i, s in enumerate(d["steps"], 1):
        st.markdown(f"{i}. {s}")
    st.markdown("#### How to read the results")
    st.write(d["reading"])


def fields_tab(key):
    d = DOCS[key]
    if d["fields"]:
        compat_dataframe(pd.DataFrame(d["fields"], columns=["Field", "Meaning", "Unit or range", "Source"]),
                     hide_index=True)
    else:
        st.info("This module has no computed fields of its own. See the Data Management module for every upload field.")
    if key == "data":
        for kind in SCHEMAS:
            st.markdown(f"**{TABLE_LABELS[kind]}**. {UPLOAD_DOCS[kind]}")
            sch = SCHEMAS[kind]
            rows = [(c, "Required", "") for c in sch["required"]] + \
                   [(c, "Optional", str(v)) for c, v in sch["defaults"].items() if c not in sch["required"]]
            compat_dataframe(pd.DataFrame(rows, columns=["Column", "Status", "Default when missing"]), hide_index=True)


def formulas_tab(key):
    d = DOCS[key]
    if not d["formulas"]:
        st.info("This module does not compute formulas of its own.")
        return
    st.caption("Formulas use standard arithmetic notation.")
    for name, f, expl in d["formulas"]:
        st.markdown(f"**{name}**")
        st.code(f, language=None)
        st.write(expl)
    if key == "attribution":
        st.markdown("**Evidence weights**")
        rows = [("Corroborating", v[1], v[0]) for v in CORROBORATING.values()] + \
               [("Contextual", v[1], v[0]) for v in CONTEXTUAL.values()] + \
               [("Exculpatory", v[1], v[0]) for v in EXCULPATORY.values()]
        compat_dataframe(pd.DataFrame(rows, columns=["Kind", "Evidence", "Weight w"]), hide_index=True)
    if key == "risk":
        compat_dataframe(pd.DataFrame({"Factor": [k.replace("_", " ").capitalize() for k in DEFAULT_WEIGHTS],
                                   "Default weight": list(DEFAULT_WEIGHTS.values())}), hide_index=True)


def export_tab(key, rep):
    st.write("Export the results, explanation, field dictionary and formulas of this module. PDF and Word include charts and "
             "tables. Text is a plain summary. CSV holds the full main results table.")
    if st.button("Prepare export files", key=f"prep_{key}", type="primary"):
        meta = dict(generated=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), source=ss.data_label)
        with st.spinner("Building PDF, Word, text and CSV files"):
            ss.exports[key] = dict(pdf=build_pdf(rep, meta), docx=build_docx(rep, meta), txt=build_txt(rep, meta),
                                   csv=build_csv(rep))
        audit("export prepared", rep.title)
    ex = ss.exports.get(key)
    if ex:
        base = "KNet_" + rep.title.replace(" ", "_").replace("(", "").replace(")", "")
        c = st.columns(4)
        c[0].download_button("Download PDF", ex["pdf"], base + ".pdf", "application/pdf", key=f"d1_{key}")
        c[1].download_button("Download Word", ex["docx"], base + ".docx",
                             "application/vnd.openxmlformats-officedocument.wordprocessingml.document", key=f"d2_{key}")
        c[2].download_button("Download Text", ex["txt"], base + ".txt", "text/plain", key=f"d3_{key}")
        c[3].download_button("Download CSV", ex["csv"], base + ".csv", "text/csv", key=f"d4_{key}")


def header(title):
    c1, c2 = st.columns([5, 2])
    c1.markdown(f"<div class='knet-title'>{title}</div>", unsafe_allow_html=True)
    c1.caption(DOCS[PAGES[title]]["short"])
    c2.markdown(f"<div style='text-align:right;color:#7d8fa6;font-size:.8rem;padding-top:6px'>Data: <b>{ss.data_label}</b><br>"
                f"User: <b>{ss.user or 'guest, read only'}</b></div>", unsafe_allow_html=True)


def page_frame(title, results_fn):
    key = PAGES[title]
    header(title)
    data_panel(key)
    rep = Report(title, key)
    tabs = compat_tabs(["Results", "How it works", "Fields", "Formulas", "Export"], f"tabs_{key}")
    with tabs[0]:
        results_fn(rep)
    with tabs[1]:
        explain_tab(key)
    with tabs[2]:
        fields_tab(key)
    with tabs[3]:
        formulas_tab(key)
    with tabs[4]:
        export_tab(key, rep)


def no_incidents():
    st.info("No incident records are loaded. Upload incidents in the data panel above or generate synthetic data.")


# =========================================================================== RESULTS PER MODULE
def res_overview(rep):
    cl = R["clusters"]
    cols = st.columns(4)
    kpi(cols[0], "Assets", f"{len(A):,}"); kpi(cols[1], "Dependencies", f"{G.number_of_edges():,}")
    kpi(cols[2], "Incidents", len(R["incidents"])); kpi(cols[3], "Vendors", len(ss.data["vendors"]))
    st.markdown("<div class='guard'><b>Analytic guardrail.</b> Simultaneous outages are never labelled a cyberattack without "
                "corroborating evidence. Clusters without evidence stay Undetermined, and a confirmed attribution needs a named "
                "analyst decision recorded in the audit log.</div>", unsafe_allow_html=True)
    st.markdown("#### Platform architecture")
    st.graphviz_chart(DOCS["overview"]["diagram"])
    st.markdown("#### The three possibilities the platform distinguishes")
    st.graphviz_chart(DOCS["attribution"]["diagram"])
    st.markdown("#### Modules")
    mods = pd.DataFrame([(t, DOCS[k]["short"]) for t, k in PAGES.items()], columns=["Module", "What it does"])
    compat_dataframe(mods, hide_index=True)
    st.markdown("#### Quick start")
    for i, s in enumerate(["Read this overview, then open the Executive Dashboard.",
                           "Open Incident Correlation and Attribution and compare the four multi event clusters.",
                           "Run the Cascade Simulation and apply AI recommended hardening.",
                           "Check Third Party Dependencies for vendors that connect many sectors.",
                           "Use the Export tab of any module to download PDF, Word, text or CSV.",
                           "To use real data, sign in as analyst and use the data panel or the Data Management module."], 1):
        st.markdown(f"{i}. {s}")
    rep.h("Platform summary")
    rep.p(f"The active dataset holds {len(A):,} assets, {G.number_of_edges():,} dependencies, {len(R['incidents'])} incidents and "
          f"{len(ss.data['vendors'])} vendors. Correlation produced {len(cl)} clusters.")
    rep.table(mods, "Modules")
    rep.set_primary(mods)


def res_dashboard(rep):
    cl, rk, inc = R["clusters"], R["risk"], R["incidents"]
    multi = cl[cl.n_incidents > 1] if len(cl) else cl
    n_cyber = int((cl.assessment == CLASS_CYBER).sum()) if len(cl) else 0
    cols = st.columns(6)
    kpi(cols[0], "Assets monitored", f"{len(A):,}"); kpi(cols[1], "Sectors", A.sector.nunique())
    kpi(cols[2], "Incidents", len(inc)); kpi(cols[3], "Correlated clusters", len(multi))
    kpi(cols[4], "Potentially coordinated", n_cyber); kpi(cols[5], "Critical tier assets", int((rk.risk_tier == "Critical").sum()))
    st.markdown("<div class='guard'><b>Analytic guardrail.</b> Simultaneous outages are never labelled a cyberattack without "
                "corroborating evidence.</div>", unsafe_allow_html=True)
    c1, c2 = st.columns([3, 2])
    with c1:
        st.subheader("National risk and active incidents")
        fig = base_map(500)
        for tier in ["Guarded", "Elevated", "High", "Critical"]:
            d = rk[rk.risk_tier == tier]
            if len(d):
                map_points(fig, d, tier, TIER_COLORS[tier], size=5 + d.criticality * 1.5,
                           text=d.name + "<br>" + d.sector + "<br>Risk " + d.risk_score.astype(str))
        if len(inc):
            ii = inc.merge(cl[["cluster_id", "assessment"]], on="cluster_id").merge(A[["asset_id", "lat", "lon", "name"]], on="asset_id")
            for cls_, d in ii.groupby("assessment"):
                map_points(fig, d, "Incident: " + cls_.split(",")[0], "rgba(0,0,0,0)", size=17, line_color=CLASS_COLORS[cls_],
                           text=d.incident_id + " " + d.name, opacity=1)
        show(fig)
    with c2:
        st.subheader("Correlated event assessments")
        if not len(multi):
            st.caption("No multi event clusters in the current data.")
        for r in multi.itertuples():
            st.markdown(f"**{r.cluster_id}**, {pd.Timestamp(r.start):%b %d %H:%M}, {r.n_incidents} events, "
                        f"{r.n_sectors} sectors, {r.n_states} states<br>{pill(r.assessment)} "
                        f"<span style='color:#7d8fa6'>Confidence {r.confidence}. Probability malicious {pct(r.p_malicious)}.</span>",
                        unsafe_allow_html=True)
        st.subheader("Mean risk by sector")
        sec = rk.groupby("sector").risk_score.mean().sort_values()
        fig = px.bar(sec, orientation="h", labels={"value": "Mean risk score", "sector": ""}, color=sec.values, color_continuous_scale="YlOrRd")
        fig.update_coloraxes(showscale=False); fig.update_layout(showlegend=False)
        show(style_fig(fig, 360))
    c1, c2 = st.columns([3, 2])
    top = rk.head(10)[["name", "sector", "state", "risk_score", "risk_tier", "top_driver"]]
    with c1:
        st.subheader("Top 10 highest risk assets"); table(top)
    with c2:
        st.subheader("Systemic third parties")
        vtop = R["vconc"].head(6)[["vendor_name", "vendor_type", "sectors", "assets", "systemic_score"]] if len(R["vconc"]) else pd.DataFrame()
        table(vtop)
    rep.h("Key figures")
    rep.p(f"{len(A):,} assets in {A.sector.nunique()} sectors; {len(inc)} incidents; {len(multi)} correlated clusters; "
          f"{n_cyber} potentially coordinated; {int((rk.risk_tier == 'Critical').sum())} critical tier assets.")
    if len(multi):
        ct = multi[["cluster_id", "start", "n_incidents", "n_sectors", "n_states", "assessment", "confidence", "p_malicious"]]
        rep.table(ct, "Correlated event assessments")
    rep.chart(lambda: png_map([(t, rk[rk.risk_tier == t].lon, rk[rk.risk_tier == t].lat, TIER_COLORS[t], 14, "o")
                               for t in ["Guarded", "Elevated", "High", "Critical"]], "Assets by risk tier"), "National risk map")
    rep.chart(lambda: png_bar(sec.index, sec.values, "Mean risk by sector", "Risk score"), "Mean risk by sector")
    rep.table(top, "Top 10 highest risk assets")
    if len(vtop):
        rep.table(vtop, "Systemic third parties")
    rep.set_primary(rk[["asset_id", "name", "sector", "state", "risk_score", "risk_tier", "top_driver"]])


def res_graph(rep):
    deps = ss.data["dependencies"]
    met = R["metrics"].merge(A, on="asset_id")
    c = st.columns(5)
    kpi(c[0], "Nodes", G.number_of_nodes()); kpi(c[1], "Dependency edges", G.number_of_edges())
    kpi(c[2], "Dependency types", deps.dependency_type.nunique() if len(deps) else 0)
    kpi(c[3], "Single points of failure", int(met.single_point_of_failure.sum()))
    kpi(c[4], "Largest downstream reach", int(met.downstream_count.max()) if len(met) else 0)
    f1, f2 = st.columns(2)
    alltypes = sorted(deps.dependency_type.unique()) if len(deps) else []
    types = f1.multiselect("Dependency types", alltypes, default=alltypes)
    secs = f2.multiselect("Sectors", sorted(A.sector.unique()), default=sorted(A.sector.unique()))
    keep = set(A[A.sector.isin(secs)].asset_id)
    E = [(u, v) for u, v, d in G.edges(data=True) if d["dependency_type"] in types and u in keep and v in keep]
    fig = base_map(560)
    map_edges(fig, G, E)
    pal = px.colors.qualitative.Bold + px.colors.qualitative.Pastel
    for i, (s, d) in enumerate(met[met.asset_id.isin(keep)].groupby("sector")):
        map_points(fig, d, s, pal[i % len(pal)], size=5 + np.sqrt(d.downstream_count) * 1.2,
                   text=d.name + "<br>Downstream " + d.downstream_count.astype(str))
    show(fig)
    st.caption("Marker size grows with downstream reach. Lines are dependency edges.")
    central = met.sort_values("betweenness", ascending=False).head(15)[["name", "sector", "betweenness", "supplier_pagerank", "downstream_count", "single_point_of_failure"]]
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Most central assets"); table(central)
    with c2:
        st.subheader("Cross sector dependency matrix")
        e = deps.merge(A[["asset_id", "sector"]], left_on="source", right_on="asset_id").merge(
            A[["asset_id", "sector"]], left_on="target", right_on="asset_id", suffixes=("_src", "_tgt"))
        mat = pd.crosstab(e.sector_src, e.sector_tgt)
        fig = px.imshow(mat, color_continuous_scale="Blues", aspect="auto", labels=dict(x="Dependent sector", y="Supplying sector", color="Edges"))
        show(style_fig(fig, 430))
    st.subheader("Knowledge graph explorer")
    K = build_knowledge_graph(A, deps, ss.data["vendors"], ss.data["vendor_relations"])
    opts = {f"{r.name} ({r.asset_id})": r.asset_id for r in A.itertuples()}
    opts.update({f"Vendor: {r.vendor_name}": r.vendor_id for r in ss.data["vendors"].itertuples()})
    default = next((k for k in opts if "Columbus Transmission" in k), list(opts)[0])
    sel = st.selectbox("Focus entity", list(opts), index=list(opts).index(default))
    radius = st.slider("Hops from focus", 1, 2, 1)
    H = nx.ego_graph(K.to_undirected(as_view=False), opts[sel], radius=radius)
    if H.number_of_nodes() > 160:
        H = H.subgraph(list(H.nodes)[:160])
    pos = nx.spring_layout(H, seed=3, k=0.6)
    ex, ey = [], []
    for u, v in H.edges():
        ex += [pos[u][0], pos[v][0], None]; ey += [pos[u][1], pos[v][1], None]
    fig = go.Figure([go.Scatter(x=ex, y=ey, mode="lines", line=dict(color="rgba(160,180,210,.35)", width=1), hoverinfo="skip", showlegend=False)])
    for kind, col in {"Asset": "#4C9BE8", "Vendor": "#E5484D", "Sector": GOLD, "State": "#46B37B"}.items():
        ns = [n for n in H if K.nodes[n].get("kind") == kind]
        if ns:
            fig.add_trace(go.Scatter(x=[pos[n][0] for n in ns], y=[pos[n][1] for n in ns], mode="markers+text", name=kind,
                                     marker=dict(size=[22 if n == opts[sel] else 12 for n in ns], color=col, line=dict(width=1, color="#fff")),
                                     text=[K.nodes[n].get("label", n)[:28] for n in ns], textposition="top center", textfont=dict(size=9),
                                     hovertext=[K.nodes[n].get("label", n) for n in ns], hoverinfo="text"))
    fig.update_xaxes(visible=False); fig.update_yaxes(visible=False)
    show(style_fig(fig, 540))
    rep.h("Graph summary")
    rep.p(f"{G.number_of_nodes()} nodes, {G.number_of_edges()} dependency edges, {int(met.single_point_of_failure.sum())} single points of failure.")
    rep.chart(lambda: png_bar(central.name.head(12), central.betweenness.head(12), "Most central assets", "Betweenness"), "Betweenness centrality")
    rep.table(central, "Most central assets")
    rep.table(mat.reset_index().rename(columns={"sector_src": "supplying_sector"}), "Cross sector dependency matrix (edge counts)")
    rep.set_primary(met[["asset_id", "name", "sector", "state", "betweenness", "supplier_pagerank", "downstream_count",
                         "in_degree", "out_degree", "single_point_of_failure"]].sort_values("betweenness", ascending=False))


def evidence_chart(row):
    ev = pd.DataFrame(row["evidence"], columns=["kind", "factor", "log_odds", "detail"])
    if ev.empty:
        return None, ev
    ev = ev.sort_values("log_odds")
    color = ev.kind.map({"Corroborating": "#E5484D", "Contextual": "#F2A93B", "Exculpatory": "#4C9BE8"})
    fig = go.Figure(go.Bar(x=ev.log_odds, y=ev.factor, orientation="h", marker_color=color, text=ev.detail,
                           hovertext=ev.kind, textposition="auto"))
    fig.update_layout(title="Evidence contributions in log odds. Red corroborating, amber contextual, blue exculpatory")
    return style_fig(fig, 120 + 38 * len(ev)), ev


def res_attribution(rep):
    inc, cl = R["incidents"], R["clusters"]
    if not len(inc):
        no_incidents(); return
    ii = inc.merge(cl[["cluster_id", "assessment"]], on="cluster_id").merge(A[["asset_id", "name", "sector", "state"]], on="asset_id")
    fig = px.scatter(ii, x="timestamp", y="sector", color="assessment", color_discrete_map=CLASS_COLORS, size="severity",
                     hover_data=["incident_id", "cluster_id", "name", "state", "incident_type"])
    fig.update_layout(title="Incident timeline by sector, coloured by cluster assessment")
    fig = style_fig(fig, 460); fig.update_layout(margin=dict(b=90))
    show(fig)
    counts = cl.assessment.value_counts()
    cs = st.columns(len(counts))
    for col, (k, v) in zip(cs, counts.items()):
        col.markdown(f"{pill(k)}<br><span style='font-size:1.5rem;font-weight:800'>{v}</span> clusters", unsafe_allow_html=True)
    st.divider()
    multi = cl[cl.n_incidents > 1]
    choices = list(multi.cluster_id) + [c for c in cl.cluster_id if c not in set(multi.cluster_id)]
    labels = {r.cluster_id: f"{r.cluster_id}, {r.n_incidents} events, {r.assessment}" for r in cl.itertuples()}
    sel = st.selectbox("Investigate cluster", choices, format_func=lambda c: labels[c])
    row = cl.set_index("cluster_id").loc[sel].copy(); row["cluster_id"] = sel
    c1, c2 = st.columns([3, 2])
    with c1:
        st.markdown(f"### {sel} {pill(row.assessment)}", unsafe_allow_html=True)
        st.markdown(f"Confidence: **{row.confidence}**. Probability malicious: **{pct(row.p_malicious)}**. "
                    f"Corroborating categories: **{row.corroborating_categories}**. Span: **{row.span_min:.0f} minutes**. "
                    f"Geographic spread: **{row.geo_spread_km:,} km**.")
        st.info(row.rationale)
        f, ev = evidence_chart(row)
        if f:
            show(f)
        if row.evidence_gaps and row.assessment != CLASS_INDEPENDENT:
            st.markdown("**Evidence not observed, collection gaps to close:** " + "; ".join(row.evidence_gaps))
    d = inc[inc.cluster_id == sel].merge(A[["asset_id", "name", "lat", "lon", "sector", "state"]], on="asset_id")
    with c2:
        fig = base_map(330)
        E = [(u, v) for u in d.asset_id for v in d.asset_id if G.has_edge(u, v)]
        if E:
            map_edges(fig, G, E, color="#F2A93B", width=2, name="Dependency link")
        map_points(fig, d, "Incident", CLASS_COLORS[row.assessment], size=13, text=d.incident_id + " " + d.name)
        show(fig)
        st.markdown(f"Root cause candidate: **{ANAME.get(row.root_candidate, row.root_candidate)}**  \n"
                    f"Top shared vendor: **{VNAME.get(row.top_shared_vendor, 'none')}** on {row.top_vendor_share * 100:.0f} percent of assets  \n"
                    f"Cascade explained: **{row.cascade_explained * 100:.0f} percent** of follow on events")
    show_cols = ["incident_id", "timestamp", "name", "sector", "incident_type", "severity", "physical_cause", "ioc_match",
                 "auth_anomaly", "unauthorized_config_change", "malware_signature", "attack_technique", "vendor_remote_session",
                 "telemetry_precursor", "weather_alert"]
    d2 = d.copy()
    d2["attack_technique"] = d2["attack_technique"].map(lambda t: f"{t} {ATTACK_ICS.get(t, '')}".strip() if t else "")
    table(d2[[c for c in show_cols if c in d2.columns]])

    st.subheader("Analyst determination")
    prev = ss.decisions.get(sel)
    if prev:
        st.success(f"Recorded: {prev['decision']} by {prev['user']} at {prev['ts']}. Justification: {prev['justification']}")
    if can(ss.role, "attribute"):
        with st.form(f"decide_{sel}"):
            dec = st.selectbox("Determination", ["Keep under investigation", "Confirm coordinated cyberattack",
                                                 "Reclassify as accidental cascading failure",
                                                 "Reclassify as independent technical failure", "Mark as false positive or benign"])
            just = st.text_area("Justification and evidence references (required)")
            if st.form_submit_button("Record determination"):
                if dec.startswith("Confirm") and row.corroborating_categories < 2:
                    st.error("Blocked. Confirming a coordinated cyberattack requires at least 2 corroborating evidence categories. "
                             "Keep the cluster under investigation and collect evidence.")
                elif len(just.strip()) < 15:
                    st.error("A substantive justification is required.")
                else:
                    ss.decisions[sel] = dict(decision=dec, user=ss.user, justification=just.strip(),
                                             ts=pd.Timestamp.utcnow().strftime("%Y-%m-%d %H:%M UTC"))
                    audit("analyst determination", f"{sel}: {dec}. {just.strip()[:200]}")
                    st.rerun()
    else:
        st.caption("Sign in as an analyst to record a determination.")

    summary = cl.drop(columns=["evidence", "assets"]).copy()
    summary["evidence_gaps"] = summary.evidence_gaps.map("; ".join)
    summary["top_shared_vendor"] = summary.top_shared_vendor.map(lambda v: VNAME.get(v, v))
    rep.h("Cluster assessments")
    for r in cl[cl.n_incidents > 1].itertuples():
        rep.p(f"{r.cluster_id}: {r.assessment}. Confidence {r.confidence}. Probability malicious {pct(r.p_malicious)}. {r.rationale}")
    rep.table(summary.sort_values(["n_incidents", "start"], ascending=[False, True])[["cluster_id", "start", "n_incidents", "n_sectors", "n_states", "assessment", "confidence", "p_malicious",
                       "corroborating_categories"]], "All clusters")
    rep.h(f"Selected cluster {sel}")
    rep.p(row.rationale)
    if len(ev):
        rep.chart(lambda: png_bar(ev.factor, ev.log_odds, f"Evidence contributions for {sel}", "Log odds",
                                  color=[{"Corroborating": "#C0392B", "Contextual": "#D68910", "Exculpatory": "#2E86C1"}[k] for k in ev.kind][::-1]),
                  "Evidence contributions")
        rep.table(ev.rename(columns={"factor": "evidence"}), "Evidence table")
    rep.table(d2[["incident_id", "timestamp", "name", "sector", "incident_type", "severity", "physical_cause", "attack_technique"]], "Events in cluster")
    if ss.decisions:
        rep.table(pd.DataFrame([dict(cluster=k, **v) for k, v in ss.decisions.items()]), "Analyst determinations")
    rep.set_primary(summary)


def res_anomaly(rep):
    an = R["anom"]
    if an.empty:
        st.warning("No telemetry is loaded. Upload telemetry in the data panel above to enable anomaly detection.")
        return
    c = st.columns(4)
    kpi(c[0], "Telemetry readings", f"{len(an):,}"); kpi(c[1], "Anomalies", int(an.is_anomaly.sum()))
    kpi(c[2], "Cyber type signals", int(an.cyber_signal.sum()))
    kpi(c[3], "Incidents with precursors", int(R["incidents"].telemetry_precursor.sum()) if len(R["incidents"]) else 0)
    a2 = an[an.is_anomaly].merge(A[["asset_id", "name", "sector"]], on="asset_id")
    c1, c2 = st.columns([3, 2])
    with c1:
        heat = a2.assign(bin=a2.timestamp.dt.floor("6h")).pivot_table(index="sector", columns="bin", values="asset_id", aggfunc="count", fill_value=0)
        fig = px.imshow(heat, color_continuous_scale="Inferno", aspect="auto", labels=dict(color="Anomalies", x="Time", y=""))
        fig.update_layout(title="Anomaly density by sector in 6 hour bins")
        show(style_fig(fig, 400))
    with c2:
        drv = a2.groupby(["driver", "cyber_signal"]).size().reset_index(name="count")
        drv["signal"] = drv.cyber_signal.map({True: "Cyber type", False: "Operational"})
        fig = px.bar(drv, x="driver", y="count", color="signal", barmode="group",
                     color_discrete_map={"Cyber type": "#E5484D", "Operational": "#4C9BE8"})
        fig.update_layout(title="What drives the anomalies", xaxis_title="Metric", yaxis_title="Anomalies")
        show(style_fig(fig, 400))
    st.subheader("Cyber type precursor anomalies")
    cy = a2[a2.cyber_signal].sort_values("anomaly_score", ascending=False)[["timestamp", "name", "sector", "driver", "driver_z", "anomaly_score"]]
    table(cy.head(50))
    st.subheader("Asset telemetry drill down")
    hot = a2.groupby("asset_id").anomaly_score.max().sort_values(ascending=False).index.tolist()
    aid = st.selectbox("Asset", hot + [x for x in A.asset_id if x not in set(hot)], format_func=lambda x: f"{ANAME.get(x, x)} ({x})")
    d = an[an.asset_id == aid]
    fig = go.Figure()
    for m in [m for m in METRICS if f"z_{m}" in d]:
        fig.add_trace(go.Scatter(x=d.timestamp, y=d[f"z_{m}"], name=m.replace("_", " "), mode="lines", line=dict(width=1.2)))
    pts = d[d.is_anomaly]
    fig.add_trace(go.Scatter(x=pts.timestamp, y=pts.driver_z, mode="markers", name="Anomaly", marker=dict(size=10, color="#E5484D", symbol="diamond")))
    if len(R["incidents"]):
        for r in R["incidents"][R["incidents"].asset_id == aid].itertuples():
            fig.add_vline(x=r.timestamp, line_dash="dash", line_color=GOLD)
    fig.update_layout(title="Robust z scores. Dashed lines mark incidents", yaxis_title="z score")
    show(style_fig(fig, 420))
    rep.h("Anomaly summary")
    rep.p(f"{len(an):,} readings scored; {int(an.is_anomaly.sum())} anomalies; {int(an.cyber_signal.sum())} cyber type signals.")
    sec_counts = a2.groupby("sector").size().sort_values(ascending=False)
    rep.chart(lambda: png_bar(sec_counts.index, sec_counts.values, "Anomalies by sector", "Anomalies"), "Anomalies by sector")
    rep.chart(lambda: png_hist(an.anomaly_score, "Distribution of anomaly scores", "Normalized anomaly score"), "Score distribution")
    rep.table(cy.head(40), "Cyber type precursor anomalies")
    rep.set_primary(a2.sort_values("anomaly_score", ascending=False)[["timestamp", "asset_id", "name", "sector", "driver", "driver_z", "anomaly_score", "cyber_signal"]])


def res_cascade(rep):
    vrel = ss.data["vendor_relations"]
    presets = {"Custom": []}
    def ids(mask):
        return [x for x in A[mask].asset_id.tolist() if x in G]
    if "city" in A:
        presets["Columbus transmission substation loss"] = ids((A.city == "Columbus") & (A.asset_type == "Transmission Substation"))
    if "region" in A:
        presets["Regional generation loss in Texas"] = ids((A.region == "Texas") & (A.asset_type == "Generation Plant"))
        presets["Internet exchange outage in the Northeast"] = ids((A.region == "Northeast") & (A.asset_type == "Internet Exchange Point"))
    if len(vrel):
        presets["Compromise of a shared remote access vendor (stress test)"] = [x for x in vrel[(vrel.vendor_id == "V02") & vrel.remote_access].asset_id.head(25) if x in G]
    presets = {k: v for k, v in presets.items() if v or k == "Custom"}
    c1, c2 = st.columns([2, 3])
    with c1:
        p = st.selectbox("Scenario preset", list(presets), index=1 if len(presets) > 1 else 0)
        src = st.multiselect("Initiating failures", A.asset_id.tolist(), default=presets[p] or [A.asset_id.iloc[0]],
                             format_func=lambda x: ANAME.get(x, x))
        runs = st.slider("Monte Carlo runs", 50, 1000, 300, 50)
        steps = st.slider("Propagation steps (about one hour each)", 3, 24, 10)
        boost = st.slider("Redundancy uplift for every asset (what if)", 0.0, 0.5, 0.0, 0.05)
        harden = st.checkbox("Apply AI recommended hardening to the top 5 assets", value=False)
        go_ = st.button("Run simulation", type="primary")
    if not src:
        st.info("Select at least one initiating asset."); return
    key = (tuple(src), runs, steps, boost, harden, ss.data_version)
    if go_ or ss.get("_sim_key") != key:
        red = {n: min(0.95, G.nodes[n].get("redundancy", .3) + boost) for n in G} if boost else None
        hard = suggest_hardening(G, src, 5) if harden else []
        base = monte_carlo_cascade(G, src, runs=runs, steps=steps)
        mit = monte_carlo_cascade(G, src, runs=runs, steps=steps, redundancy_override=red, hardened=set(hard)) if (boost or harden) else None
        ss._sim, ss._sim_key = (base, mit, hard), key
        if go_:
            audit("simulation run", f"{len(src)} sources, {runs} runs, uplift {boost}, hardening {harden}")
    base, mit, hard = ss._sim
    nd = (mit or base)["nodes"]
    with c2:
        fig = base_map(470)
        pf = nd.set_index("asset_id").p_fail
        map_edges(fig, G, [(u, v) for u, v in G.edges if pf.get(u, 0) > .3 and pf.get(v, 0) > .05], color="rgba(229,72,77,.35)", width=1)
        d = nd[nd.p_fail > 0.02]
        x, y = map_xy(d.lon, d.lat)
        fig.add_trace(go.Scatter(x=x, y=y, mode="markers", name="Failure probability",
                                 marker=dict(size=6 + d.p_fail * 14, color=d.p_fail, colorscale="YlOrRd", cmin=0, cmax=1, colorbar=dict(title="P fail")),
                                 text=d.name + "<br>P fail " + d.p_fail.round(2).astype(str) + "<br>Mean step " + d.mean_step.round(1).astype(str), hoverinfo="text"))
        if d.state.nunique() <= 3 and len(d):
            fig.update_xaxes(range=[(d.lon.min() - 3) * MAP_KX, (d.lon.max() + 3) * MAP_KX])
            fig.update_yaxes(range=[d.lat.min() - 2, d.lat.max() + 2])
            st.caption("Map zoomed to the affected area.")
        show(fig)

    def summ(r):
        n = r["nodes"]
        return dict(exp_fail=float(n.p_fail.sum()), pop=float((n.p_fail * n.population_served).sum()), sectors=int(n[n.p_fail > .5].sector.nunique()))
    b = summ(base)
    c = st.columns(4)
    kpi(c[0], "Expected failed assets", f"{b['exp_fail']:.1f}")
    kpi(c[1], "Expected population affected", f"{b['pop'] / 1e6:.2f} million")
    kpi(c[2], "Sectors likely impacted", b["sectors"])
    m = summ(mit) if mit else None
    if m:
        kpi(c[3], "Population with mitigation", f"{m['pop'] / 1e6:.2f} million, {(m['pop'] - b['pop']) / max(b['pop'], 1) * 100:+.0f} percent")
    else:
        kpi(c[3], "Initiating assets", len(src))
    tl = base["timeline"]; xs = list(range(tl.shape[1]))
    c1, c2 = st.columns(2)
    with c1:
        fig = go.Figure([go.Scatter(x=xs, y=np.percentile(tl, 90, axis=0), mode="lines", line=dict(width=0), showlegend=False),
                         go.Scatter(x=xs, y=np.percentile(tl, 10, axis=0), mode="lines", fill="tonexty", line=dict(width=0),
                                    name="10th to 90th percentile", fillcolor="rgba(229,72,77,.25)"),
                         go.Scatter(x=xs, y=tl.mean(axis=0), mode="lines", name="Baseline mean", line=dict(color="#E5484D", width=3))])
        if mit:
            fig.add_trace(go.Scatter(x=xs, y=mit["timeline"].mean(axis=0), mode="lines", name="With mitigation", line=dict(color="#46B37B", width=3, dash="dash")))
        fig.update_layout(title="Cascade growth over time", xaxis_title="Step", yaxis_title="Failed assets")
        show(style_fig(fig, 380))
    sec = nd.groupby("sector").p_fail.sum().sort_values()
    with c2:
        fig = px.bar(sec, orientation="h", labels={"value": "Expected failed assets", "sector": ""})
        fig.update_layout(title="Expected impact by sector", showlegend=False)
        show(style_fig(fig, 380))
    if hard:
        st.success("AI recommended hardening points: " + "; ".join(ANAME.get(h, h) for h in hard))
    affected = nd[nd.p_fail > .05].sort_values("p_fail", ascending=False)[["name", "sector", "state", "p_fail", "mean_step", "population_served"]]
    table(affected)
    rep.h("Scenario")
    rep.p(f"Initiating failures: {', '.join(ANAME.get(s, s) for s in src)}. {runs} runs, {steps} steps, redundancy uplift {boost}, hardening {'on' if harden else 'off'}.")
    rep.p(f"Baseline: {b['exp_fail']:.1f} expected failed assets, {b['pop'] / 1e6:.2f} million people affected, {b['sectors']} sectors likely impacted.")
    series = {"Baseline mean": (tl.mean(axis=0), "#C0392B")}
    if m:
        rep.p(f"With mitigation: {m['exp_fail']:.1f} expected failed assets, {m['pop'] / 1e6:.2f} million people affected, {m['sectors']} sectors.")
        series["With mitigation"] = (mit["timeline"].mean(axis=0), "#1E8449")
    if hard:
        rep.p("AI recommended hardening points: " + "; ".join(ANAME.get(h, h) for h in hard) + ".")
    rep.chart(lambda: png_line(xs, series, "Cascade growth over time", "Step", "Failed assets"), "Cascade growth")
    rep.chart(lambda: png_bar(sec.index[::-1], sec.values[::-1], "Expected impact by sector", "Expected failed assets"), "Impact by sector")
    rep.table(affected, "Affected assets")
    rep.set_primary(nd.sort_values("p_fail", ascending=False)[["asset_id", "name", "sector", "state", "p_fail", "mean_step", "population_served"]])


def res_vendors(rep):
    vc = R["vconc"]
    if vc.empty:
        st.warning("No vendor relationships are loaded. Upload vendors and vendor relations in the data panel above."); return
    fig = px.scatter(vc, x="assets", y="sectors", size="population_exposed", color="systemic_score", hover_name="vendor_name",
                     hover_data=["vendor_type", "states", "remote_access_assets"], color_continuous_scale="YlOrRd", size_max=55,
                     labels={"assets": "Dependent assets", "sectors": "Sectors served", "systemic_score": "Systemic score"})
    fig.update_layout(title="Vendor concentration. Bubble size is population served by dependent assets")
    c1, c2 = st.columns([3, 2])
    with c1:
        show(style_fig(fig, 430))
    m = ss.data["vendor_relations"].merge(A[["asset_id", "sector"]], on="asset_id").merge(ss.data["vendors"], on="vendor_id")
    heat = pd.crosstab(m.vendor_name, m.sector)
    with c2:
        f2 = px.imshow(heat, color_continuous_scale="Blues", aspect="auto", labels=dict(color="Assets", x="", y=""))
        f2.update_layout(title="Vendor and sector footprint")
        show(style_fig(f2, 430))
    vt = vc[["vendor_name", "vendor_type", "assets", "sectors", "states", "remote_access_assets", "systemic_score", "systemic_flag", "sector_list"]]
    table(vt)
    st.subheader("Hidden coupling analysis")
    vn = st.selectbox("Vendor", vc.vendor_id, format_func=lambda v: VNAME.get(v, v))
    hc = hidden_couplings(G, ss.data["vendor_relations"], A, vn)
    c1, c2 = st.columns([2, 3])
    with c1:
        st.metric("Cross sector asset pairs with no dependency path that share this vendor", f"{len(hc):,}{' or more' if len(hc) >= 200 else ''}")
        st.caption("These pairs look independent on a dependency map, but one vendor compromise or outage could affect them at "
                   "the same moment, a common pattern behind unexplained concurrent outages.")
        table(hc.head(100), height=320)
    with c2:
        idsv = ss.data["vendor_relations"][ss.data["vendor_relations"].vendor_id == vn].asset_id
        dv = A[A.asset_id.isin(idsv)]
        fig = base_map(420)
        for i, (s, d) in enumerate(dv.groupby("sector")):
            map_points(fig, d, s, px.colors.qualitative.Bold[i % 10], size=9, text=d.name)
        show(fig)
    rep.h("Vendor concentration")
    rep.p(f"{len(vc)} vendors analysed. {int((vc.systemic_flag == 'Systemic cross-sector').sum() + (vc.systemic_flag == 'Systemic cross sector').sum())} are systemic cross sector dependencies.")
    rep.chart(lambda: png_bar(vc.vendor_name, vc.systemic_score, "Vendor systemic score", "Score 0 to 100"), "Systemic score by vendor")
    rep.table(vt, "Vendor concentration")
    rep.h(f"Hidden couplings for {VNAME.get(vn, vn)}")
    rep.p(f"{len(hc)} cross sector pairs with no dependency path share this vendor (list capped at 200).")
    rep.table(hc.head(40), "Sample of hidden couplings")
    rep.set_primary(vt)


def res_risk(rep):
    with st.expander("Scoring weights", expanded=False):
        cols = st.columns(4)
        w = {k: cols[i % 4].slider(k.replace("_", " ").capitalize(), 0.0, 0.5, v, 0.01) for i, (k, v) in enumerate(DEFAULT_WEIGHTS.items())}
    rk = score_assets(A, R["metrics"], R["impact"], R["vconc"], ss.data["vendor_relations"], R["anom"], R["incidents"], w)
    c = st.columns(4)
    for col, t in zip(c, ["Critical", "High", "Elevated", "Guarded"]):
        kpi(col, f"{t} tier", int((rk.risk_tier == t).sum()))
    c1, c2 = st.columns(2)
    with c1:
        fig = px.histogram(rk, x="risk_score", color="risk_tier", color_discrete_map=TIER_COLORS, nbins=40, labels={"risk_score": "Risk score"})
        fig.update_layout(title="Risk score distribution")
        show(style_fig(fig, 360))
    piv = pd.crosstab(rk.sector, rk.risk_tier).reindex(columns=["Critical", "High", "Elevated", "Guarded"], fill_value=0)
    with c2:
        fig = px.imshow(piv, color_continuous_scale="OrRd", text_auto=True, aspect="auto", labels=dict(x="", y="", color="Assets"))
        fig.update_layout(title="Sector and tier")
        show(style_fig(fig, 360))
    sec_f = st.multiselect("Filter sectors", sorted(A.sector.unique()))
    v = rk[rk.sector.isin(sec_f)] if sec_f else rk
    cols_ = ["asset_id", "name", "sector", "state", "risk_score", "risk_tier", "top_driver", "criticality", "redundancy",
             "internet_exposed", "patch_lag_days", "known_vulns"]
    table(v[cols_], height=360)
    aid = st.selectbox("Explain the score of an asset", v.asset_id, format_func=lambda x: ANAME.get(x, x))
    r = rk.set_index("asset_id").loc[aid]
    tot = sum(w.values()) or 1
    contrib = pd.DataFrame({"factor": [k.replace("_", " ").capitalize() for k in w],
                            "points": [100 * r[f"f_{k}"] * w[k] / tot for k in w]}).sort_values("points")
    fig = px.bar(contrib, x="points", y="factor", orientation="h", color="points", color_continuous_scale="OrRd", labels={"points": "Points", "factor": ""})
    fig.update_layout(title=f"{r['name']}: {r.risk_score} ({r.risk_tier})"); fig.update_coloraxes(showscale=False)
    show(style_fig(fig, 340))
    rep.h("Risk summary")
    rep.p("Weights used: " + "; ".join(f"{k.replace('_', ' ')} {v_:.2f}" for k, v_ in w.items()) + ".")
    rep.p(", ".join(f"{t}: {int((rk.risk_tier == t).sum())}" for t in ["Critical", "High", "Elevated", "Guarded"]) + ".")
    rep.chart(lambda: png_hist(rk.risk_score, "Risk score distribution", "Risk score"), "Distribution")
    rep.table(piv.reset_index(), "Assets by sector and tier")
    rep.table(rk.head(25)[["name", "sector", "state", "risk_score", "risk_tier", "top_driver"]], "Top 25 assets")
    rep.h(f"Score breakdown for {r['name']}")
    rep.chart(lambda: png_bar(contrib.factor[::-1], contrib.points[::-1], f"Score breakdown for {r['name']}", "Points"), "Factor contributions")
    rep.set_primary(rk[cols_ + [c_ for c_ in rk.columns if c_.startswith("f_")]])


def res_response(rep):
    cl = R["clusters"]
    if not len(cl):
        no_incidents(); return
    st.markdown("<div class='guard'>Demonstration SOAR queue. <b>No actions are executed against real systems.</b> Approvals are "
                "recorded in the audit log for exercises and after action review.</div>", unsafe_allow_html=True)
    order = cl.sort_values(["n_incidents", "p_malicious"], ascending=False).cluster_id.tolist()
    sel = st.selectbox("Cluster", order, format_func=lambda c: f"{c}, {cl.set_index('cluster_id').assessment[c]}")
    row = cl.set_index("cluster_id").loc[sel].copy(); row["cluster_id"] = sel
    st.markdown(f"{pill(row.assessment)} {row.rationale}", unsafe_allow_html=True)
    if row.top_shared_vendor:
        row["top_shared_vendor"] = VNAME.get(row.top_shared_vendor, row.top_shared_vendor)
    rec = recommendations(row, A)
    if rec.empty:
        st.info("No playbook actions for this cluster."); return
    rec["status"] = [ss.soar.get((sel, i), "Proposed") for i in range(len(rec))]
    pc = rec.groupby(["phase", "priority"]).size().reset_index(name="actions")
    c1, c2 = st.columns([3, 2])
    with c1:
        table(rec[["phase", "priority", "action", "soar_automatable", "status"]])
    with c2:
        fig = px.bar(pc, x="phase", y="actions", color="priority", color_discrete_map={"P1": "#E5484D", "P2": "#F2A93B", "P3": "#4C9BE8"})
        fig.update_layout(title="Actions by phase and priority", xaxis_title="", yaxis_title="Actions")
        show(style_fig(fig, 340))
    if can(ss.role, "attribute"):
        with st.form(f"soar_{sel}"):
            idx = st.multiselect("Select actions", list(range(len(rec))), format_func=lambda i: f"{rec.priority[i]}: {rec.action[i][:110]}")
            c1, c2 = st.columns(2)
            ok = c1.form_submit_button("Approve selected", type="primary")
            rej = c2.form_submit_button("Reject selected")
            if ok or rej:
                for i in idx:
                    ss.soar[(sel, i)] = "Approved (simulated)" if ok else "Rejected"
                    audit("soar " + ("approve" if ok else "reject"), f"{sel}: {rec.action[i][:150]}")
                st.rerun()
    else:
        st.caption("Sign in as an analyst to approve or reject actions.")
    rep.h(f"Response plan for {sel}")
    rep.p(f"Assessment: {row.assessment}. {row.rationale}")
    rep.chart(lambda: png_bar(pc.phase + " " + pc.priority, pc.actions, "Actions by phase and priority", "Actions"), "Action mix")
    rep.table(rec[["phase", "priority", "action", "soar_automatable", "status"]], "Recommended actions")
    rep.set_primary(rec)


def res_report(rep):
    cl, rk, vc, inc = R["clusters"], R["risk"], R["vconc"], R["incidents"]
    multi = cl[cl.n_incidents > 1] if len(cl) else cl
    cyber = int((cl.assessment == CLASS_CYBER).sum()) if len(cl) else 0
    cas = int((cl.assessment == CLASS_CASCADE).sum()) if len(cl) else 0
    und = int((cl.assessment == CLASS_UNDETERMINED).sum()) if len(cl) else 0
    blu = [f"{len(inc)} incidents were correlated into {len(cl)} clusters, {len(multi)} of them with more than one event.",
           f"{cyber} clusters are assessed as potentially coordinated cyber activity. Analyst validation is required before external attribution.",
           f"{cas} accidental cascading failures and {und} undetermined clusters. Undetermined clusters are deliberately not attributed to an adversary.",
           f"{int((rk.risk_tier == 'Critical').sum())} assets are in the Critical risk tier. The most systemic third party is "
           f"{vc.iloc[0]['vendor_name'] if len(vc) else 'not available'}."]
    recs = ["Validate or rule out the potentially coordinated clusters with forensic evidence and keep public messaging neutral.",
            "Require phishing resistant multi factor authentication, session recording and just in time approval for all third party remote access to operational technology.",
            "Fund redundancy at the hardening points identified by the digital twin.",
            "Close patch lag and internet exposure gaps on Critical tier assets.",
            "Exercise cross sector restoration priorities for 911, hospitals and water with state emergency operations centers."]
    st.markdown("#### Bottom line up front")
    for i, b in enumerate(blu, 1):
        st.markdown(f"{i}. {b}")
    if len(multi):
        st.markdown("#### Correlated event assessments")
        ct = multi[["cluster_id", "start", "n_incidents", "n_sectors", "n_states", "assessment", "confidence", "p_malicious"]]
        table(ct)
        for r in multi.itertuples():
            st.markdown(f"**{r.cluster_id}**. {r.rationale}")
        ac = cl.assessment.value_counts()
        fig = px.bar(ac, orientation="h", color=ac.index, color_discrete_map=CLASS_COLORS, labels={"value": "Clusters", "assessment": ""})
        fig.update_layout(showlegend=False, title="Clusters by assessment")
        show(style_fig(fig, 260))
    st.markdown("#### Highest risk assets")
    top = rk.head(10)[["name", "sector", "state", "risk_score", "risk_tier", "top_driver"]]
    table(top)
    st.markdown("#### Systemic third party concentration")
    vt = vc.head(6)[["vendor_name", "vendor_type", "assets", "sectors", "states", "systemic_score"]] if len(vc) else pd.DataFrame()
    table(vt)
    st.markdown("#### Priority recommendations")
    for i, r_ in enumerate(recs, 1):
        st.markdown(f"{i}. {r_}")
    st.markdown("#### Analytic standards")
    std = ("Assessments are probabilistic and evidence weighted. Simultaneity, geographic spread and shared vendors are contextual "
           "indicators and cannot by themselves produce a cyberattack assessment. A confirmed attribution requires a named analyst "
           "decision recorded in the audit log.")
    st.write(std)
    rep.h("Bottom line up front")
    for b in blu:
        rep.p(b)
    if len(multi):
        rep.table(ct, "Correlated event assessments")
        for r in multi.itertuples():
            rep.p(f"{r.cluster_id}. {r.rationale}")
        rep.chart(lambda: png_bar(ac.index, ac.values, "Clusters by assessment", "Clusters"), "Clusters by assessment")
    rep.table(top, "Highest risk assets")
    if len(vt):
        rep.table(vt, "Systemic third party concentration")
    rep.h("Priority recommendations")
    for i, r_ in enumerate(recs, 1):
        rep.p(f"{i}. {r_}")
    rep.h("Analytic standards")
    rep.p(std)
    rep.set_primary(cl.drop(columns=["evidence", "assets", "evidence_gaps"]) if len(cl) else rk.head(10))


def res_data(rep):
    st.subheader("Active dataset")
    counts = pd.DataFrame({"Table": [TABLE_LABELS[k] for k in SCHEMAS], "Rows": [len(ss.data[k]) for k in SCHEMAS]})
    compat_dataframe(counts, hide_index=True)
    st.caption(f"Source: {ss.data_label}. Banner: {ss.banner}")
    st.subheader("Synthetic demonstration data")
    c1, c2 = st.columns([1, 3])
    seed = c1.number_input("Random seed", 1, 99999, 42, key="seed_data_page")
    if c2.button("Generate synthetic dataset"):
        set_dataset(generate(seed=int(seed)), f"Synthetic national dataset, seed {seed}", "synthetic", SYNTH_BANNER)
        audit("dataset synthetic", f"seed {seed}"); st.rerun()
    st.write("The generator embeds five scenarios with known answers: scattered independent faults, an accidental cascade in "
             "Columbus, a Central region ice storm, three unexplained simultaneous outages and a coordinated intrusion through a "
             "shared remote access vendor.")
    st.subheader("Upload real data")
    if not can(ss.role, "upload"):
        st.warning("Sign in as an analyst or administrator to upload infrastructure data. Uploads stay in your session memory "
                   "only and are never written to disk or shared with other sessions.")
    else:
        upload_widgets(list(SCHEMAS), "dm")
        st.write("Staged: " + (", ".join(TABLE_LABELS[k] for k in ss.staged) or "none"))
        marking = st.text_input("Classification or handling banner for uploaded data", "UNCLASSIFIED. CUSTOMER SUPPLIED DATA. VERIFY MARKING.")
        if st.button("Activate uploaded dataset", type="primary"):
            activate_uploads(marking)
    rep.h("Active dataset")
    rep.p(f"Source: {ss.data_label}.")
    rep.table(counts, "Rows per table")
    for kind in SCHEMAS:
        rep.p(f"{TABLE_LABELS[kind]}. {UPLOAD_DOCS[kind]}")
    rep.set_primary(counts)


def res_audit(rep):
    if not can(ss.role, "attribute"):
        st.warning("Sign in as an analyst or administrator to view the audit log.")
        rep.p("Audit log not available to guests."); return
    log = pd.DataFrame(ss.audit)
    if log.empty:
        st.info("No events yet."); rep.p("No events recorded."); return
    table(log.iloc[::-1])
    ac = log.action.value_counts()
    rep.chart(lambda: png_bar(ac.index, ac.values, "Audit events by action", "Events"), "Events by action")
    rep.table(log, "Audit log", max_rows=200)
    rep.set_primary(log)


RESULTS = {"overview": res_overview, "dashboard": res_dashboard, "graph": res_graph, "attribution": res_attribution,
           "anomaly": res_anomaly, "cascade": res_cascade, "vendors": res_vendors, "risk": res_risk, "response": res_response,
           "report": res_report, "data": res_data, "audit": res_audit}

page_frame(page, RESULTS[PAGES[page]])

st.markdown(f"<hr style='margin-top:40px;border-color:#23406b'><div style='text-align:center;color:#7d8fa6;font-size:.78rem'>"
            f"{BRAND}<br>{BYLINE}. Demonstration build. Synthetic data is fictional.</div>", unsafe_allow_html=True)