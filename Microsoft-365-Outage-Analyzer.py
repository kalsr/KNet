

# Microsoft 365 Outage Analyzer — November 2026 Incident Simulator
# Developed by Randy Singh from Kalsnet (KNet) Consulting Group

# Streamlit application that re-creates the 12-14 November 2026 Microsoft 365 outage
# with SYNTHETIC telemetry, lets users upload REAL telemetry, and explains every
# function, field and formula used.

# Public facts used to shape the scenario (as reported 12-14 Nov 2026):
#  * Impact began ~16:17 UTC, 12 Nov 2026 with Exchange Online mailbox access failures
#   (incident EX1550543); spread to Teams, SharePoint, Copilot, Defender (MO1550821);
#   Power Platform advisory PP1550869 (restored 13 Nov 15:50 UTC).
# * Microsoft: servers failed automated health checks and dropped out, pushing load onto
#  the remaining servers; a process that establishes secure connections became
# overwhelmed; traffic did NOT increase; not a cyberattack.
# * ~20:38 UTC servers restarted; returned servers could become unresponsive again once
#  they received traffic; protective traffic management applied; a network
# configuration change correlated with the start of impact was reverted overnight.
#* 13 Nov 17:06 UTC email queues significantly reduced. Root cause NOT yet published
 # (Post-Incident Report pending as of 14 Nov 2026).

# Everything else (server counts, rates, thresholds, user numbers) is SYNTHETIC/ILLUSTRATIVE.


import io
import math
import datetime as dt

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# ════════════════════════════════════════════════════════════════════════════
# 0. PAGE CONFIG & BRANDING
# ════════════════════════════════════════════════════════════════════════════
APP_TITLE = "Microsoft 365 Outage Analyzer — November 2026 Incident Simulator"
DEVELOPER = "Developed by Randy Singh from Kalsnet (KNet) Consulting Group"
BLUE = "#0B3D91"
ACCENT = "#1F6FEB"

st.set_page_config(page_title="M365 Outage Analyzer | KNet", layout="wide")

st.markdown(
    f"""
    <style>
      .block-container {{padding-top: 3.6rem;}}
      .knet-titlebar {{
          border-bottom: 4px solid {BLUE}; padding: 0.4rem 0 0.6rem 0; margin-bottom: 0.8rem;
      }}
      .knet-title {{color:{BLUE}; font-weight:900 !important; font-size:2.1rem !important; line-height:1.2; margin:0;}}
      .knet-sub {{color:{BLUE}; font-weight:800 !important; font-size:1.15rem !important; margin-top:0.3rem;}}
      .knet-badge {{display:inline-block; background:{BLUE}; color:white; font-weight:700;
          border-radius:4px; padding:2px 8px; font-size:0.75rem; margin-right:6px;}}
      .explain {{background:#F3F7FF; border-left:5px solid {ACCENT}; padding:0.8rem 1rem;
          border-radius:4px; margin:0.4rem 0 0.8rem 0;}}
      div[data-testid="stMetric"] {{background:#F7F9FC; border:1px solid #E1E7F0;
          border-radius:8px; padding:0.6rem 0.8rem;}}
      section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3 {{color:{BLUE};}}
    </style>
    <div class="knet-titlebar">
      <div class="knet-title">{APP_TITLE}</div>
      <div class="knet-sub">{DEVELOPER}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ════════════════════════════════════════════════════════════════════════════
# 1. REFERENCE DATA (regions, services, public timeline)
# ════════════════════════════════════════════════════════════════════════════
WINDOW_START = pd.Timestamp("2026-11-12 12:00")  # all times are UTC (tz-naive)
WINDOW_END = pd.Timestamp("2026-11-14 06:00")
STEP_MIN = 5
OFFICIAL_START = pd.Timestamp("2026-11-12 16:17")
OFFICIAL_OPEN = pd.Timestamp("2026-11-12 16:20")

REGIONS = {
    "North America":        dict(code="NAM", utc_offset=-5,  rollout=1.00, user_share=0.30, lat=40,  lon=-97,
                                 countries=["United States", "Canada", "Mexico"]),
    "Europe":               dict(code="EUR", utc_offset=1,   rollout=0.95, user_share=0.22, lat=50,  lon=10,
                                 countries=["Germany", "France", "Netherlands", "Spain", "Italy", "Sweden", "Poland", "Ireland"]),
    "United Kingdom":       dict(code="GBR", utc_offset=0,   rollout=0.95, user_share=0.08, lat=54,  lon=-2,
                                 countries=["United Kingdom"]),
    "Asia Pacific":         dict(code="APC", utc_offset=8,   rollout=0.85, user_share=0.14, lat=22,  lon=115,
                                 countries=["Japan", "Singapore", "South Korea", "Philippines", "Hong Kong"]),
    "Australia & NZ":       dict(code="AUS", utc_offset=10,  rollout=0.90, user_share=0.06, lat=-27, lon=140,
                                 countries=["Australia", "New Zealand"]),
    "India":                dict(code="IND", utc_offset=5.5, rollout=0.80, user_share=0.08, lat=21,  lon=78,
                                 countries=["India"]),
    "Latin America":        dict(code="LAM", utc_offset=-3,  rollout=0.80, user_share=0.06, lat=-15, lon=-55,
                                 countries=["Brazil", "Argentina", "Chile", "Colombia"]),
    "Middle East & Africa": dict(code="MEA", utc_offset=3,   rollout=0.75, user_share=0.06, lat=15,  lon=35,
                                 countries=["United Arab Emirates", "Saudi Arabia", "South Africa", "Nigeria", "Kenya"]),
}

# dep = share of the service's requests that traverse the failing secure-connection layer
SERVICES = {
    "Exchange Online (Outlook)": dict(dep=1.00, share=0.35, incident="EX1550543"),
    "Microsoft Teams":           dict(dep=0.70, share=0.22, incident="MO1550821"),
    "SharePoint / OneDrive":     dict(dep=0.55, share=0.15, incident="MO1550821"),
    "Microsoft 365 Copilot":     dict(dep=0.85, share=0.10, incident="MO1550821"),
    "Defender XDR":              dict(dep=0.45, share=0.08, incident="MO1550821"),
    "Power Platform":            dict(dep=0.50, share=0.10, incident="PP1550869"),
}

PUBLIC_TIMELINE = pd.DataFrame(
    [
        ("2026-11-12 16:17", "Users begin losing access to Exchange Online mailboxes (start of impact in Microsoft's records).", "Reported"),
        ("2026-11-12 16:20", "Incident EX1550543 (Exchange Online) opened.", "Reported"),
        ("2026-11-12 18:26", "Multi-service incident MO1550821 opened — Teams, SharePoint, Copilot, Defender affected.", "Reported"),
        ("2026-11-12 19:57", "Microsoft: no recent change yet identified as correlated with the start of impact.", "Reported"),
        ("2026-11-12 20:38", "Affected servers unresponsive during validation; restarted with the change applied.", "Reported"),
        ("2026-11-12 22:30", "Traffic shifted to alternate routes; protective traffic management in one location (time modeled).", "Approximate"),
        ("2026-11-13 00:00", "Returned servers can become unresponsive again once they begin receiving traffic.", "Reported"),
        ("2026-11-13 02:00", "Overnight: reverting a recent network configuration change that correlates with impact (time modeled).", "Approximate"),
        ("2026-11-13 04:11", "Microsoft: no indication of malicious activity.", "Reported"),
        ("2026-11-13 15:50", "Power Platform advisory PP1550869 restored.", "Reported"),
        ("2026-11-13 17:06", "Email queues significantly reduced.", "Reported"),
        ("2026-11-14 00:00", "Residual recovery; Post-Incident Report (root cause) still pending.", "Reported"),
    ],
    columns=["time_utc", "event", "status"],
)
PUBLIC_TIMELINE["time_utc"] = pd.to_datetime(PUBLIC_TIMELINE["time_utc"])

DEFAULT_PARAMS = dict(
    servers=400,            # servers per region in the front-door / Exchange pool
    mu=120.0,               # TLS handshakes per second one healthy server can complete (normal)
    peak_util=0.68,         # normal utilisation at the daily peak (no incident)
    w0=40.0,                # base handshake latency, ms
    hc_threshold=500.0,     # health probe fails when latency exceeds this, ms
    client_timeout=4000.0,  # client gives up after this, ms
    degradation=0.45,       # fraction of per-server handshake capacity lost to the bad config
    trigger="2026-11-12 16:15",
    fail_k=1.6,             # how fast overloaded servers drop out
    auto_recover=0.025,     # share of failed servers that auto-heal each 5-min step
    restart_on=True, restart_time="2026-11-12 20:38", restart_frac=0.60,
    tm_on=True, tm_time="2026-11-12 22:30", tm_cap=0.85,
    rollback_on=True, rollback_start="2026-11-13 02:00", rollback_hours=8.0,
    hysteresis=False,
)

CANONICAL_FIELDS = {
    "timestamp": ("datetime", True, "Event time in UTC."),
    "region": ("text", False, "Geographic region of the server/user."),
    "country": ("text", False, "Country of the affected tenant/user."),
    "service": ("text", False, "Microsoft 365 workload (Exchange, Teams, ...)."),
    "server_id": ("text", False, "Front-end / mailbox server identifier."),
    "health_check": ("Pass/Fail", False, "Result of the automated health probe."),
    "tls_utilization": ("float", False, "ρ = handshake arrival rate ÷ handshake capacity."),
    "handshake_latency_ms": ("float", False, "Time to establish a secure (TLS) connection."),
    "requests": ("int", True, "Client requests in the interval."),
    "errors": ("int", True, "Failed requests (5xx, timeouts, auth/connection failures)."),
    "active_users": ("int", False, "Users active on the server in the interval."),
    "users_impacted": ("int", False, "Users who saw at least one failure."),
    "mail_queue_depth": ("int", False, "Messages waiting for delivery (region level)."),
}

# ════════════════════════════════════════════════════════════════════════════
# 2. CORE MODEL FUNCTIONS
# ════════════════════════════════════════════════════════════════════════════
def diurnal_factor(local_hour: float) -> float:
    """Daily traffic shape: 0.55 at night → 1.0 at 14:00 local (Gaussian bump)."""
    return 0.55 + 0.45 * math.exp(-(((local_hour - 14.0) / 5.0) ** 2))


def phase_bounds(p: dict) -> list[tuple[str, pd.Timestamp]]:
    rb = pd.Timestamp(p["rollback_start"])
    pts = [
        ("Pre-incident baseline", WINDOW_START),
        ("Trigger & onset", pd.Timestamp(p["trigger"])),
        ("Widespread outage", pd.Timestamp("2026-11-12 18:26")),
        ("Restart & relapse", pd.Timestamp(p["restart_time"])),
        ("Traffic management", pd.Timestamp(p["tm_time"])),
        ("Rollback & recovery", rb),
        ("Residual / queue drain", rb + pd.Timedelta(hours=p["rollback_hours"])),
    ]
    return sorted(pts, key=lambda x: x[1])


def label_phase(ts: pd.Series, p: dict) -> pd.Series:
    bounds = phase_bounds(p)
    names = np.array([b[0] for b in bounds])
    starts = np.array([b[1].value for b in bounds])
    idx = np.searchsorted(starts, pd.to_datetime(ts).values.astype("int64"), side="right") - 1
    return pd.Series(names[np.clip(idx, 0, len(names) - 1)], index=ts.index)


@st.cache_data(show_spinner=False)
def run_cascade(p: dict) -> pd.DataFrame:
    """
    FUNCTION: Cascading-failure simulator (5-minute steps, per region).
      λ(t)  = N·μ·peak_util·diurnal(t)                (offered handshakes/s — NO traffic surge)
      μ_eff = μ·(1 − d·rollout·ramp)                  (capacity lost to the configuration change)
      ρ     = λ_admitted / (H·μ_eff)                  (utilisation of the H healthy servers)
      W     = W0 / (1 − ρ)                            (queueing latency, M/M/1 form)
      ρ_crit= 1 − W0 / T_hc                           (health probe fails when W > T_hc)
      ΔH    = −H·min(0.5, k·(ρ − ρ_crit)) + r·(N − H) (servers drop out / auto-heal)
      A     = min(λ_adm, H·μ_eff)/λ · (1 − timeout penalty)
      Q(t+1)= max(0, Q + arrivals − 1.08·peak·A)     (mail queue backlog)
    """
    times = pd.date_range(WINDOW_START, WINDOW_END, freq=f"{STEP_MIN}min", inclusive="left")
    trig = pd.Timestamp(p["trigger"])
    restart = pd.Timestamp(p["restart_time"])
    tm = pd.Timestamp(p["tm_time"])
    rb = pd.Timestamp(p["rollback_start"])
    rb_h = max(p["rollback_hours"], 0.25)
    rho_crit = 1 - p["w0"] / p["hc_threshold"]
    rows = []
    for rname, r in REGIONS.items():
        N = float(p["servers"])
        H, Q, restarted = N, 0.0, False
        mu = p["mu"]
        peak_load = N * mu * p["peak_util"]
        mail_peak = 60000.0 * r["user_share"]  # messages per 5 min at peak (illustrative)
        for t in times:
            local_h = (t.hour + t.minute / 60 + r["utc_offset"]) % 24
            di = diurnal_factor(local_h)
            lam = peak_load * di
            if t < trig:
                d = 0.0
            else:
                ramp = min(1.0, (t - trig).total_seconds() / 600)
                if p["rollback_on"] and t >= rb:
                    ramp *= max(0.0, 1 - (t - rb).total_seconds() / 3600 / rb_h)
                d = p["degradation"] * r["rollout"] * ramp
            mu_eff = mu * (1 - d)
            if p["restart_on"] and not restarted and t >= restart:
                H += (N - H) * p["restart_frac"]
                restarted = True
            cap = max(H, 1e-6) * mu_eff
            admitted = lam
            if p["tm_on"] and t >= tm:
                admitted = min(lam, p["tm_cap"] * cap)
            rho = admitted / cap
            latency = p["w0"] / (1 - rho) if rho < 0.99 else p["w0"] / 0.01
            latency = min(latency, p["client_timeout"] * 2.5)
            served = min(admitted, cap)
            timeout_pen = min(0.5, max(0.0, (latency - p["client_timeout"]) / p["client_timeout"]))
            avail = max(0.0, min(1.0, served / lam * (1 - timeout_pen)))
            arrivals = mail_peak * di
            Q = max(0.0, Q + arrivals - 1.08 * mail_peak * avail)
            rows.append((t, rname, H / N, H, rho, latency, avail, lam, served, d, di, Q))
            # state update for next step
            fail_frac = 0.0
            if rho > rho_crit:
                fail_frac = min(0.5, p["fail_k"] * (rho - rho_crit))
                if p["hysteresis"]:
                    fail_frac /= 3
            H = min(N, max(0.0, H - H * fail_frac + (N - H) * p["auto_recover"]))
    df = pd.DataFrame(rows, columns=["timestamp", "region", "healthy_frac", "healthy_servers", "rho",
                                     "latency_ms", "availability", "offered_load", "served_load",
                                     "capacity_loss", "diurnal", "mail_queue"])
    df["phase"] = label_phase(df["timestamp"], p)
    return df


def global_series(sim: pd.DataFrame) -> pd.DataFrame:
    w = sim["region"].map({k: v["user_share"] for k, v in REGIONS.items()})
    g = sim.assign(w=w, wa=w * sim["availability"], wh=w * sim["healthy_frac"]).groupby("timestamp")
    out = pd.DataFrame({"availability": g["wa"].sum() / g["w"].sum(),
                        "healthy_frac": g["wh"].sum() / g["w"].sum(),
                        "mail_queue": g["mail_queue"].sum()}).reset_index()
    return out


@st.cache_data(show_spinner=False)
def generate_synthetic(n: int, seed: int, p: dict) -> pd.DataFrame:
    """FUNCTION: Synthetic telemetry generator — samples n server-interval records from the cascade model."""
    sim = run_cascade(p)
    rng = np.random.default_rng(seed)
    regions, services = list(REGIONS), list(SERVICES)
    times = np.sort(sim["timestamp"].unique())
    T, R = len(times), len(regions)

    def piv(col):
        return sim.pivot(index="region", columns="timestamp", values=col).loc[regions, times].to_numpy()

    A, RHO, LAT, HF, DI, MQ = (piv(c) for c in ["availability", "rho", "latency_ms", "healthy_frac", "diurnal", "mail_queue"])
    shares = np.array([REGIONS[r]["user_share"] for r in regions]); shares /= shares.sum()
    sshare = np.array([SERVICES[s]["share"] for s in services]); sshare /= sshare.sum()
    deps = np.array([SERVICES[s]["dep"] for s in services])

    r_i = rng.choice(R, n, p=shares)
    t_i = rng.integers(0, T, n)
    s_i = rng.choice(len(services), n, p=sshare)
    a, rho, lat0, hf, di, mq = A[r_i, t_i], RHO[r_i, t_i], LAT[r_i, t_i], HF[r_i, t_i], DI[r_i, t_i], MQ[r_i, t_i]
    ts = pd.to_datetime(times[t_i]) + pd.to_timedelta(rng.integers(0, STEP_MIN * 60, n), unit="s")

    healthy = rng.random(n) < hf
    lat = np.where(healthy, lat0 * rng.lognormal(0, 0.18, n), p["client_timeout"] * rng.uniform(1.0, 1.5, n))
    util = np.where(healthy, np.clip(rho * rng.normal(1, 0.05, n), 0, 3), np.nan)
    hc = np.where(healthy & (lat <= p["hc_threshold"]), "Pass", "Fail")
    cpu = np.where(healthy, np.clip(18 + 65 * np.minimum(util, 1.3) / 1.3 + rng.normal(0, 4, n), 1, 100),
                   rng.uniform(96, 100, n))
    reqs = rng.poisson(400 * di)
    p_err = np.clip(0.002 + deps[s_i] * (1 - a), 0, 1)
    errs = rng.binomial(reqs, p_err)
    users = rng.poisson(150 * di)
    impacted = rng.binomial(users, np.clip(deps[s_i] * (1 - a), 0, 1))
    k = rng.integers(1, p["servers"] + 1, n)
    codes = np.array([REGIONS[r]["code"] for r in regions])[r_i]
    server_id = pd.Series(codes).str.cat(pd.Series(k).astype(str).str.zfill(4), sep="-FE-")
    country = np.empty(n, dtype=object)
    for j, rname in enumerate(regions):
        m = r_i == j
        country[m] = rng.choice(REGIONS[rname]["countries"], m.sum())

    df = pd.DataFrame({
        "timestamp": ts,
        "region": pd.Categorical(np.array(regions)[r_i]),
        "country": pd.Categorical(country),
        "datacenter": pd.Categorical(pd.Series(codes) + "-DC" + pd.Series((k % 4) + 1).astype(str)),
        "server_id": server_id,
        "service": pd.Categorical(np.array(services)[s_i]),
        "incident_id": pd.Categorical(np.array([SERVICES[s]["incident"] for s in services])[s_i]),
        "health_check": pd.Categorical(hc),
        "tls_utilization": np.round(util, 3),
        "handshake_latency_ms": np.round(lat, 1),
        "tls_queue_len": np.round(np.where(healthy, util * p["mu"] * lat / 1000, np.nan), 1),
        "cpu_pct": np.round(cpu, 1),
        "requests": reqs,
        "errors": errs,
        "error_rate_pct": np.round(np.where(reqs > 0, errs / np.maximum(reqs, 1) * 100, 0), 2),
        "active_users": users,
        "users_impacted": impacted,
        "mail_queue_depth": np.round(mq).astype(int),
    }).sort_values("timestamp").reset_index(drop=True)
    df.insert(0, "record_id", np.arange(1, n + 1))
    df.insert(2, "phase", pd.Categorical(label_phase(df["timestamp"], p)))
    return df


# ── analytics on canonical columns (works for synthetic AND uploaded real data) ──
def agg_timeseries(df: pd.DataFrame, freq: str = "15min", by: str | None = None) -> pd.DataFrame:
    keys = [pd.Grouper(key="timestamp", freq=freq)] + ([by] if by else [])
    agg = {"requests": ("requests", "sum"), "errors": ("errors", "sum")}
    if "handshake_latency_ms" in df:
        agg["latency_p50"] = ("handshake_latency_ms", "median")
        agg["latency_p95"] = ("handshake_latency_ms", lambda x: x.quantile(0.95))
    if "health_check" in df:
        df = df.assign(_hcfail=(df["health_check"].astype(str).str.lower() == "fail").astype(float))
        agg["hc_fail_rate"] = ("_hcfail", "mean")
    if "users_impacted" in df:
        agg["users_impacted"] = ("users_impacted", "sum")
    g = df.groupby(keys, observed=True).agg(**agg).reset_index()
    g["availability"] = np.where(g["requests"] > 0, 1 - g["errors"] / g["requests"].clip(lower=1), np.nan)
    g["error_rate"] = 1 - g["availability"]
    return g


def detect_anomaly(ts: pd.DataFrame, col: str, baseline_end: pd.Timestamp, z_thr=3.0, consec=2):
    """FUNCTION: z-score detector. z = (x − μ_baseline)/σ_baseline; alarm after `consec` points above threshold."""
    s = ts.set_index("timestamp")[col].astype(float)
    base = s[s.index < baseline_end]
    if len(base) < 4 or base.std() == 0:
        base = s.iloc[: max(4, len(s) // 10)]
    mu_, sd = base.mean(), base.std() or 1e-9
    z = (s - mu_) / sd
    flag = (z > z_thr).astype(int)
    run = flag.groupby((flag != flag.shift()).cumsum()).cumsum()
    hits = run[run >= consec]
    first = hits.index[0] if len(hits) else None
    return z, first, mu_, sd


def compute_kpis(df: pd.DataFrame, p: dict) -> dict:
    ts = agg_timeseries(df, "15min")
    bad = ts[ts["availability"] < 0.99]
    k = {
        "records": len(df),
        "requests": int(df["requests"].sum()),
        "errors": int(df["errors"].sum()),
        "overall_availability": 1 - df["errors"].sum() / max(df["requests"].sum(), 1),
        "min_availability": float(ts["availability"].min()),
        "peak_error_rate": float(ts["error_rate"].max()),
        "impact_start": bad["timestamp"].min() if len(bad) else None,
        "impact_end": bad["timestamp"].max() + pd.Timedelta(minutes=15) if len(bad) else None,
        "users_impacted": int(df["users_impacted"].sum()) if "users_impacted" in df else None,
        "peak_hc_fail": float(ts["hc_fail_rate"].max()) if "hc_fail_rate" in ts else None,
    }
    k["impact_hours"] = ((k["impact_end"] - k["impact_start"]).total_seconds() / 3600) if k["impact_start"] is not None else 0.0
    if "latency_p50" in ts:
        ts5 = agg_timeseries(df, "5min")
        _, first, _, _ = detect_anomaly(ts5, "latency_p50", pd.Timestamp(p["trigger"]))
        k["detected_at"] = first
    else:
        k["detected_at"] = None
    return k


def sla_table(df: pd.DataFrame, month_minutes: int = 43200) -> pd.DataFrame:
    """FUNCTION: SLA calculator. Downtime = Σ (1 − A_bucket)·Δt ; Uptime% = (M − D)/M."""
    out = []
    by = "service" if "service" in df else None
    groups = df.groupby(by, observed=True) if by else [("All services", df)]
    for name, g in groups:
        ts = agg_timeseries(g, "15min")
        down = float(((1 - ts["availability"].fillna(1)).clip(lower=0) * 15).sum())
        uptime = (month_minutes - down) / month_minutes * 100
        credit = 100 if uptime < 95 else 50 if uptime < 99 else 25 if uptime < 99.9 else 0
        out.append((name, round(down, 1), round(uptime, 3), credit))
    return pd.DataFrame(out, columns=["service", "weighted_downtime_min", "monthly_uptime_pct", "illustrative_credit_pct"])


def add_phase_bands(fig, p, show_labels=True):
    colors = ["rgba(0,150,0,0.06)", "rgba(255,165,0,0.12)", "rgba(220,20,60,0.12)", "rgba(220,20,60,0.18)",
              "rgba(255,140,0,0.12)", "rgba(30,144,255,0.10)", "rgba(0,150,0,0.06)"]
    b = phase_bounds(p) + [("end", WINDOW_END)]
    for i in range(len(b) - 1):
        kw = {}
        wide = (b[i + 1][1] - b[i][1]) >= pd.Timedelta(hours=2.5)
        if show_labels and wide:
            kw = dict(annotation_text=b[i][0], annotation_position="top left", annotation_font_size=10)
        fig.add_vrect(x0=b[i][1], x1=b[i + 1][1], fillcolor=colors[i % len(colors)], line_width=0, layer="below", **kw)
    return fig


def explain(md: str):
    with st.expander("How this function works — fields & formulas", expanded=False):
        st.markdown(f'<div class="explain">{md}</div>', unsafe_allow_html=True)


def fmt_ts(x):
    return x.strftime("%d %b %H:%M UTC") if isinstance(x, (pd.Timestamp, dt.datetime)) else "—"


# ════════════════════════════════════════════════════════════════════════════
# 3. REAL-DATA UPLOAD HELPERS
# ════════════════════════════════════════════════════════════════════════════
SYNONYMS = {
    "timestamp": ["timestamp", "time", "datetime", "date_time", "event_time", "ts"],
    "region": ["region", "geo", "area"],
    "country": ["country", "nation"],
    "service": ["service", "workload", "app", "application"],
    "server_id": ["server_id", "server", "host", "hostname", "machine"],
    "health_check": ["health_check", "health", "probe", "status"],
    "tls_utilization": ["tls_utilization", "utilization", "rho", "util"],
    "handshake_latency_ms": ["handshake_latency_ms", "latency_ms", "latency", "tls_latency"],
    "requests": ["requests", "request_count", "total_requests", "calls"],
    "errors": ["errors", "error_count", "failures", "failed_requests"],
    "active_users": ["active_users", "users"],
    "users_impacted": ["users_impacted", "impacted_users", "affected_users"],
    "mail_queue_depth": ["mail_queue_depth", "queue_depth", "mail_queue"],
}


def guess_column(field, cols):
    low = {c.lower().strip(): c for c in cols}
    for s in SYNONYMS.get(field, [field]):
        if s in low:
            return low[s]
    return None


def template_csv() -> bytes:
    sample = generate_synthetic(200, 7, DEFAULT_PARAMS)[list(CANONICAL_FIELDS)]
    return sample.to_csv(index=False).encode()


# ════════════════════════════════════════════════════════════════════════════
# 4. REPORT / EXPORT FUNCTIONS (PDF, Word, Text, CSV)
# ════════════════════════════════════════════════════════════════════════════
def report_sections(df, p, source) -> list[tuple[str, list, pd.DataFrame | None]]:
    k = compute_kpis(df, p)
    sla = sla_table(df)
    svc = (df.groupby("service", observed=True)[["requests", "errors"]].sum()
           .assign(availability_pct=lambda x: (1 - x.errors / x.requests.clip(lower=1)) * 100)
           .round(3).reset_index()) if "service" in df else None
    reg = (df.groupby("region", observed=True)[["requests", "errors"]].sum()
           .assign(availability_pct=lambda x: (1 - x.errors / x.requests.clip(lower=1)) * 100)
           .round(3).reset_index()) if "region" in df else None
    mttd = ((k["detected_at"] - OFFICIAL_START).total_seconds() / 60) if k["detected_at"] is not None else None
    kp = pd.DataFrame([
        ("Data source", source),
        ("Records analysed", f"{k['records']:,}"),
        ("Total requests", f"{k['requests']:,}"),
        ("Failed requests", f"{k['errors']:,}"),
        ("Overall availability", f"{k['overall_availability']*100:.3f}%"),
        ("Lowest 15-min availability", f"{k['min_availability']*100:.2f}%"),
        ("Peak error rate", f"{k['peak_error_rate']*100:.2f}%"),
        ("Impact window (<99% avail.)", f"{fmt_ts(k['impact_start'])} → {fmt_ts(k['impact_end'])}"),
        ("Impact duration", f"{k['impact_hours']:.1f} h"),
        ("User-sessions impacted", f"{k['users_impacted']:,}" if k["users_impacted"] is not None else "n/a"),
        ("Anomaly detected at", fmt_ts(k["detected_at"])),
        ("Detection lag vs 16:17 UTC start", f"{mttd:.0f} min" if mttd is not None else "n/a"),
    ], columns=["Metric", "Value"])
    tl = PUBLIC_TIMELINE.assign(time_utc=PUBLIC_TIMELINE.time_utc.dt.strftime("%d %b %H:%M"))
    return [
        ("1. Executive summary", [
            "On 12 November 2026 a global Microsoft 365 outage centred on Exchange Online began around 16:17 UTC and "
            "spread to Teams, SharePoint/OneDrive, Microsoft 365 Copilot, Defender XDR and Power Platform.",
            "Microsoft stated that servers failed automated health checks and dropped out of service, shifting load onto "
            "the remaining servers until they were overwhelmed; a process that establishes secure connections became "
            "overwhelmed; traffic did not increase; and the event was not a cyberattack. A network configuration change "
            "correlated with the start of impact was reverted. The final root cause is pending Microsoft's Post-Incident Report.",
            "This report quantifies the event using " + ("SYNTHETIC telemetry generated by the KNet cascade model."
                                                          if source.startswith("Synthetic") else "the uploaded telemetry."),
        ], None),
        ("2. Key performance indicators", [], kp),
        ("3. Public incident timeline (UTC)", ["Rows marked 'Approximate' are modeled times for events reported without a timestamp."], tl),
        ("4. Availability by service", ["Availability = 1 − errors ÷ requests."], svc),
        ("5. Availability by region", [], reg),
        ("6. SLA impact (illustrative)", [
            "Weighted downtime D = Σ(1 − A)·15 min over the window; monthly uptime = (43,200 − D) ÷ 43,200. "
            "Credit tiers shown (<99.9% → 25%, <99% → 50%, <95% → 100%) are illustrative — verify against your own agreement."], sla),
        ("7. Model parameters", [], pd.DataFrame([(k_, str(v)) for k_, v in p.items()], columns=["Parameter", "Value"])),
        ("8. Lessons & recommendations", [
            "• Health checks that remove servers under load can amplify a capacity loss into a cascade — use hysteresis and "
            "a minimum-healthy-capacity floor before ejecting servers.",
            "• Shed or rate-limit load (admission control) early; restarting servers into full traffic causes relapse.",
            "• Stage network/configuration changes with automatic rollback on health regression.",
            "• Tenants: keep out-of-band communication channels, monitor Service Health incident IDs (EX1550543, MO1550821), "
            "and file SLA credit claims after the Post-Incident Report.",
        ], None),
    ]


def chart_pngs(df) -> list[bytes]:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    pngs = []
    ts = agg_timeseries(df, "15min")
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(ts["timestamp"], ts["availability"] * 100, color=BLUE, lw=2)
    ax.set_title("Overall availability (%) — 15-min buckets, UTC", color=BLUE, fontweight="bold")
    ax.set_ylim(0, 101); ax.grid(alpha=.3); fig.autofmt_xdate(); fig.tight_layout()
    b = io.BytesIO(); fig.savefig(b, format="png", dpi=140); plt.close(fig); pngs.append(b.getvalue())
    if "service" in df:
        ts2 = agg_timeseries(df, "30min", "service")
        fig, ax = plt.subplots(figsize=(8, 3.4))
        for s_, g in ts2.groupby("service", observed=True):
            ax.plot(g["timestamp"], g["availability"] * 100, lw=1.4, label=s_)
        ax.set_title("Availability by service (%)", color=BLUE, fontweight="bold")
        ax.legend(fontsize=6, ncol=3); ax.set_ylim(0, 101); ax.grid(alpha=.3); fig.autofmt_xdate(); fig.tight_layout()
        b = io.BytesIO(); fig.savefig(b, format="png", dpi=140); plt.close(fig); pngs.append(b.getvalue())
    return pngs


def export_txt(sections) -> bytes:
    out = [APP_TITLE, DEVELOPER, f"Generated: {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC", "=" * 90, ""]
    for title, paras, table in sections:
        out += [title, "-" * len(title)] + paras
        if table is not None:
            out.append(table.to_string(index=False))
        out.append("")
    return "\n".join(out).encode("utf-8")


def export_csv_summary(sections) -> bytes:
    buf = io.StringIO()
    buf.write(f"{APP_TITLE}\n{DEVELOPER}\n\n")
    for title, paras, table in sections:
        buf.write(f"# {title}\n")
        for para in paras:
            buf.write(f"\"{para}\"\n")
        if table is not None:
            table.to_csv(buf, index=False)
        buf.write("\n")
    return buf.getvalue().encode("utf-8")


def export_docx(sections, pngs) -> bytes:
    from docx import Document
    from docx.shared import RGBColor, Pt, Inches
    doc = Document()
    blue = RGBColor(0x0B, 0x3D, 0x91)
    r = doc.add_paragraph().add_run(APP_TITLE); r.bold = True; r.font.size = Pt(18); r.font.color.rgb = blue
    r = doc.add_paragraph().add_run(DEVELOPER); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = blue
    doc.add_paragraph(f"Generated {dt.datetime.now(dt.timezone.utc):%d %b %Y %H:%M} UTC")
    for i, (title, paras, table) in enumerate(sections):
        h = doc.add_heading(title, level=1)
        for run in h.runs:
            run.font.color.rgb = blue
        for para in paras:
            doc.add_paragraph(para)
        if table is not None:
            t = doc.add_table(rows=1, cols=len(table.columns)); t.style = "Light Grid Accent 1"
            for j, c in enumerate(table.columns):
                t.rows[0].cells[j].text = str(c)
            for _, row in table.iterrows():
                cells = t.add_row().cells
                for j, v in enumerate(row):
                    cells[j].text = str(v)
        if i == 1:
            for png in pngs:
                doc.add_picture(io.BytesIO(png), width=Inches(6.3))
    b = io.BytesIO(); doc.save(b); return b.getvalue()


def export_pdf(sections, pngs) -> bytes:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
    b = io.BytesIO()
    doc = SimpleDocTemplate(b, pagesize=A4, leftMargin=1.6 * cm, rightMargin=1.6 * cm, topMargin=1.4 * cm, bottomMargin=1.4 * cm)
    ss = getSampleStyleSheet()
    blue = colors.HexColor(BLUE)
    t_style = ParagraphStyle("t", parent=ss["Title"], textColor=blue, fontName="Helvetica-Bold", fontSize=17, leading=21)
    d_style = ParagraphStyle("d", parent=ss["Normal"], textColor=blue, fontName="Helvetica-Bold", fontSize=11, alignment=1)
    h_style = ParagraphStyle("h", parent=ss["Heading2"], textColor=blue)
    cell = ParagraphStyle("c", parent=ss["Normal"], fontSize=7.5, leading=9)
    story = [Paragraph(APP_TITLE, t_style), Paragraph(DEVELOPER, d_style),
             Paragraph(f"Generated {dt.datetime.now(dt.timezone.utc):%d %b %Y %H:%M} UTC", ss["Italic"]), Spacer(1, 10)]
    for i, (title, paras, table) in enumerate(sections):
        story.append(Paragraph(title, h_style))
        for para in paras:
            story.append(Paragraph(para.replace("&", "&amp;").replace("<", "&lt;"), ss["BodyText"]))
        if table is not None:
            data = [[Paragraph(f"<b>{c}</b>", cell) for c in table.columns]] + \
                   [[Paragraph(str(v).replace("&", "&amp;").replace("<", "&lt;"), cell) for v in row] for row in table.values.tolist()]
            tbl = Table(data, repeatRows=1, hAlign="LEFT")
            tbl.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#DCE6F7")),
                                     ("GRID", (0, 0), (-1, -1), 0.3, colors.grey),
                                     ("VALIGN", (0, 0), (-1, -1), "TOP")]))
            story.append(tbl)
        if i == 1:
            for png in pngs:
                story += [Spacer(1, 6), Image(io.BytesIO(png), width=17 * cm, height=17 * cm * 0.4)]
        story.append(Spacer(1, 8))
    doc.build(story)
    return b.getvalue()


# ════════════════════════════════════════════════════════════════════════════
# 5. SIDEBAR — SYNTHETIC DATA BAR, DATA SOURCE, NAVIGATION
# ════════════════════════════════════════════════════════════════════════════
ss = st.session_state
ss.setdefault("params", DEFAULT_PARAMS.copy())
ss.setdefault("real_df", None)

with st.sidebar:
    st.markdown("## Synthetic Data Bar")
    n_records = st.slider("Number of synthetic records", 1_000, 1_000_000, 50_000, step=1_000,
                          help="Each record = one server × service × 5-minute telemetry sample.")
    n_records = st.number_input("…or type an exact count", 1_000, 1_000_000, n_records, step=1_000)
    seed = st.number_input("Random seed (reproducibility)", 0, 99_999, 2026)
    st.caption(f"≈ {n_records * 0.25 / 1000:.0f} MB in memory • window 12 Nov 12:00 → 14 Nov 06:00 UTC")
    st.markdown("### Data source")
    has_real = ss.real_df is not None
    source = st.radio("Analyse", ["Synthetic data", "Uploaded real data"], index=1 if has_real else 0,
                      disabled=not has_real, help="Upload real data on the 'Real Data Upload' page to enable.")
    st.markdown("### Navigation")
    page = st.radio("Go to", [
        "Overview & Timeline",
        "Synthetic Data Generator",
        "Real Data Upload",
        "Cascade Failure Simulator",
        "Secure-Connection (TLS) Saturation",
        "Service & Regional Impact",
        "Mail Queue Backlog",
        "Detection & Anomaly Analysis",
        "SLA & Business Impact",
        "Reports & Export",
        "Methodology, Fields & Formulas",
    ], label_visibility="collapsed")
    st.markdown("---")
    st.caption("Synthetic data is illustrative. Root cause per Microsoft's Post-Incident Report was still pending on 14 Nov 2026.")

P = ss.params
with st.spinner(f"Generating {n_records:,} synthetic records…"):
    syn_df = generate_synthetic(int(n_records), int(seed), P)
sim = run_cascade(P)
if source == "Uploaded real data" and ss.real_df is not None:
    df, SRC = ss.real_df, "Uploaded real data"
else:
    df, SRC = syn_df, f"Synthetic ({len(syn_df):,} records, seed {seed})"

st.markdown(f'<span class="knet-badge">DATA: {SRC}</span><span class="knet-badge">TIME ZONE: UTC</span>'
            f'<span class="knet-badge">INCIDENTS: EX1550543 · MO1550821 · PP1550869</span>', unsafe_allow_html=True)
st.write("")

# ════════════════════════════════════════════════════════════════════════════
# 6. PAGES
# ════════════════════════════════════════════════════════════════════════════
if page.startswith("Overview"):
    k = compute_kpis(df, P)
    c = st.columns(5)
    c[0].metric("Overall availability", f"{k['overall_availability']*100:.2f}%")
    c[1].metric("Lowest 15-min availability", f"{k['min_availability']*100:.1f}%")
    c[2].metric("Impact duration (<99%)", f"{k['impact_hours']:.1f} h")
    c[3].metric("Peak health-check failures", f"{(k['peak_hc_fail'] or 0)*100:.0f}%")
    c[4].metric("User-sessions impacted", f"{(k['users_impacted'] or 0):,}")

    st.subheader("What happened — 12–14 November 2026")
    st.markdown(
        """
- **Start:** ~**16:17 UTC Thu 12 Nov** — Exchange Online mailbox access failures (EX1550543), spreading to Teams,
  SharePoint/OneDrive, Microsoft 365 Copilot, Defender XDR (MO1550821) and Power Platform (PP1550869) across dozens of countries.
- **Mechanism (Microsoft's statements):** servers **failed automated health checks** and dropped out → remaining servers
  absorbed their load and were **overwhelmed**; a **process that establishes secure connections** became overloaded.
  **Traffic did not increase. Not a cyberattack.**
- **Response:** deployments paused, servers restarted (~20:38 UTC) — some **relapsed** once traffic returned; traffic
  re-routed and **protectively throttled**; a **network configuration change** correlated with the start was **reverted** overnight.
- **Recovery:** email queues significantly reduced by **17:06 UTC Fri 13 Nov**; residual issues into 14 Nov.
  **Root cause not yet published** — this app models the *stated* mechanism, not a confirmed root cause.
        """
    )
    g = agg_timeseries(df, "15min")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=g["timestamp"], y=g["availability"] * 100, name="Availability %", line=dict(color=BLUE, width=3)))
    if "hc_fail_rate" in g:
        fig.add_trace(go.Scatter(x=g["timestamp"], y=g["hc_fail_rate"] * 100, name="Health-check failures %",
                                 line=dict(color="crimson", dash="dot")))
    add_phase_bands(fig, P)
    for _, r in PUBLIC_TIMELINE.iterrows():
        fig.add_vline(x=r.time_utc, line_width=1, line_dash="dash", line_color="grey")
    fig.update_layout(height=430, title="Global availability with incident phases (UTC)", yaxis_title="%",
                      legend=dict(orientation="h", y=-0.15), margin=dict(t=60))
    st.plotly_chart(fig, width="stretch")
    st.subheader("Public incident timeline")
    st.dataframe(PUBLIC_TIMELINE.assign(time_utc=PUBLIC_TIMELINE.time_utc.dt.strftime("%a %d %b %H:%M")),
                 width="stretch", hide_index=True)
    explain("""
<b>Purpose:</b> one-screen executive view of the outage.<br>
<b>Fields used:</b> <code>timestamp, requests, errors, health_check, users_impacted</code>.<br>
<b>Formulas:</b><br>
• Availability per 15-min bucket <code>A = 1 − Σerrors / Σrequests</code><br>
• Overall availability <code>= 1 − total errors / total requests</code><br>
• Health-check failure rate <code>= count(health_check = 'Fail') / count(records)</code><br>
• Impact duration <code>= last bucket with A &lt; 99% − first bucket with A &lt; 99%</code><br>
<b>Shaded bands</b> are the incident phases; dashed lines are publicly reported milestones.
""")

elif page.startswith("Synthetic Data Generator"):
    st.subheader("Synthetic Data Generator")
    st.write(f"Generated **{len(syn_df):,}** records with seed **{seed}**. Adjust the count in the sidebar *Synthetic Data Bar*.")
    c = st.columns(4)
    c[0].metric("Records", f"{len(syn_df):,}")
    c[1].metric("Distinct servers", f"{syn_df['server_id'].nunique():,}")
    c[2].metric("Countries", syn_df["country"].nunique())
    c[3].metric("Services", syn_df["service"].nunique())
    flt = st.multiselect("Filter phase", list(syn_df["phase"].cat.categories), default=[])
    view = syn_df[syn_df["phase"].isin(flt)] if flt else syn_df
    st.dataframe(view.head(2000), width="stretch", height=380)
    st.caption("Showing first 2,000 rows of the filtered set.")
    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(px.histogram(syn_df, x="timestamp", color="health_check", nbins=120,
                                     color_discrete_map={"Pass": "#2E8B57", "Fail": "crimson"},
                                     title="Records over time by health-check result"), width="stretch")
    with c2:
        st.plotly_chart(px.box(syn_df.sample(min(len(syn_df), 30000), random_state=1), x="phase", y="handshake_latency_ms",
                               log_y=True, title="Handshake latency by phase (log scale)"), width="stretch")
    st.download_button("Download full synthetic dataset (CSV)", syn_df.to_csv(index=False).encode(),
                       f"m365_outage_synthetic_{len(syn_df)}.csv", "text/csv")
    explain(f"""
<b>Purpose:</b> creates realistic server-level telemetry for the outage window by <i>sampling the cascade model</i>.<br>
<b>Process:</b> for each record pick region (∝ user share), service (∝ traffic share), a 5-minute step and a server;
the server is healthy with probability <code>H/N</code> from the simulator.<br>
<b>Generated fields:</b><br>
• <code>handshake_latency_ms</code> = model W × LogNormal(0, 0.18) if healthy, else timeout ({P['client_timeout']:.0f} ms) × U(1, 1.5)<br>
• <code>health_check</code> = Pass if healthy and latency ≤ {P['hc_threshold']:.0f} ms, else Fail<br>
• <code>tls_utilization</code> ρ = model ρ × N(1, 0.05) (blank when server unresponsive)<br>
• <code>tls_queue_len</code> = Little's law <code>L = λ·W = ρ·μ·W/1000</code><br>
• <code>requests</code> ~ Poisson(400 × diurnal); <code>errors</code> ~ Binomial(requests, 0.002 + dep × (1 − A))<br>
• <code>users_impacted</code> ~ Binomial(active_users, dep × (1 − A)); <code>dep</code> = service dependency on the failing layer<br>
• <code>cpu_pct</code> = 18 + 65·min(ρ,1.3)/1.3 + noise; unresponsive servers 96–100%<br>
<b>Volume:</b> 1,000 – 1,000,000 records; same seed ⇒ identical data.
""")

elif page.startswith("Real Data Upload"):
    st.subheader("Real Data Upload")
    st.write("Upload your own tenant / monitoring telemetry (CSV or Excel). Map your columns to the app's fields, then switch "
             "**Data source → Uploaded real data** in the sidebar. Every analysis page will use it.")
    st.download_button("Download CSV template", template_csv(), "m365_outage_template.csv", "text/csv")
    up = st.file_uploader("Upload CSV / XLSX", type=["csv", "xlsx", "xls"])
    if up is not None:
        raw = pd.read_csv(up) if up.name.lower().endswith(".csv") else pd.read_excel(up)
        st.write(f"Loaded **{len(raw):,}** rows × **{raw.shape[1]}** columns.")
        st.dataframe(raw.head(50), width="stretch")
        st.markdown("#### Column mapping")
        mapping, cols = {}, ["— none —"] + list(raw.columns)
        grid = st.columns(3)
        for i, (f, (typ, req, desc)) in enumerate(CANONICAL_FIELDS.items()):
            g_ = guess_column(f, raw.columns)
            mapping[f] = grid[i % 3].selectbox(f"{f}{' *' if req else ''} ({typ})", cols,
                                               index=cols.index(g_) if g_ else 0, help=desc)
        if st.button("Validate & use this data", type="primary"):
            missing = [f for f, (_, req, _) in CANONICAL_FIELDS.items() if req and mapping[f] == "— none —"]
            if missing:
                st.error(f"Required fields not mapped: {', '.join(missing)}")
            else:
                out = pd.DataFrame({f: raw[c] for f, c in mapping.items() if c != "— none —"})
                out["timestamp"] = pd.to_datetime(out["timestamp"], errors="coerce", utc=True).dt.tz_localize(None)
                for c_ in ["requests", "errors", "active_users", "users_impacted", "mail_queue_depth",
                           "handshake_latency_ms", "tls_utilization"]:
                    if c_ in out:
                        out[c_] = pd.to_numeric(out[c_], errors="coerce")
                bad = out["timestamp"].isna().sum()
                out = out.dropna(subset=["timestamp", "requests", "errors"])
                out["errors"] = out[["errors", "requests"]].min(axis=1)
                if "health_check" in out:
                    out["health_check"] = out["health_check"].astype(str).str.strip().str.capitalize() \
                        .replace({"True": "Pass", "False": "Fail", "Ok": "Pass", "Healthy": "Pass", "Unhealthy": "Fail"})
                ss.real_df = out.sort_values("timestamp").reset_index(drop=True)
                st.success(f"Accepted {len(out):,} rows ({bad} rows with invalid timestamps dropped). "
                           "Select 'Uploaded real data' in the sidebar.")
    if ss.real_df is not None:
        st.info(f"Real dataset in memory: {len(ss.real_df):,} rows.")
        if st.button("Clear uploaded data"):
            ss.real_df = None
            st.rerun()
    explain("""
<b>Purpose:</b> lets analysts replace synthetic data with real telemetry (e.g., exports from Microsoft 365 Service Health,
Log Analytics, synthetic probes, proxy/firewall logs).<br>
<b>Required fields:</b> <code>timestamp, requests, errors</code>. Optional fields unlock more pages
(latency → TLS & detection pages; health_check → cascade evidence; region/service → impact pages).<br>
<b>Validation rules:</b> timestamps parsed to UTC; non-numeric values coerced to blank; rows missing required values dropped;
<code>errors = min(errors, requests)</code>; health values normalised to Pass/Fail.<br>
<b>Auto-mapping:</b> column names are matched against common synonyms (e.g. <code>latency</code> → <code>handshake_latency_ms</code>).
""")

elif page.startswith("Cascade Failure"):
    st.subheader("Cascade Failure Simulator — what-if analysis")
    st.write("Baseline reproduces the reported sequence. Change the levers to see how the outage would have unfolded differently.")
    with st.form("whatif"):
        c = st.columns(4)
        deg = c[0].slider("Capacity lost to config change (d)", 0.0, 0.8, P["degradation"], 0.05)
        hc = c[1].slider("Health-check latency threshold (ms)", 200, 2000, int(P["hc_threshold"]), 50)
        hyst = c[2].checkbox("Health-check hysteresis (3 strikes)", P["hysteresis"])
        trig0 = pd.Timestamp(P["trigger"])
        rb_off = c[3].slider("Rollback starts (hours after trigger)", 0.25, 24.0,
                             (pd.Timestamp(P["rollback_start"]) - trig0).total_seconds() / 3600, 0.25)
        c2 = st.columns(4)
        tm_on = c2[0].checkbox("Protective traffic management", P["tm_on"])
        tm_off = c2[1].slider("Traffic mgmt starts (h after trigger)", 0.25, 24.0,
                             (pd.Timestamp(P["tm_time"]) - trig0).total_seconds() / 3600, 0.25)
        tm_cap = c2[2].slider("Admission cap (share of capacity)", 0.5, 1.0, P["tm_cap"], 0.05)
        restart_on = c2[3].checkbox("Mass restart at 20:38", P["restart_on"])
        go_ = st.form_submit_button("Run scenario", type="primary")
    trig = pd.Timestamp(P["trigger"])
    scen = dict(P, degradation=deg, hc_threshold=float(hc), hysteresis=hyst, tm_on=tm_on, tm_cap=tm_cap, restart_on=restart_on,
                rollback_start=str(trig + pd.Timedelta(hours=rb_off)), tm_time=str(trig + pd.Timedelta(hours=tm_off)))
    base_g, scen_g = global_series(sim), global_series(run_cascade(scen))

    def lost_user_hours(g, users=100_000_000):
        return float(((1 - g["availability"]) * STEP_MIN / 60).sum() * users)

    def outage_h(g):
        b = g[g["availability"] < 0.99]
        return 0 if b.empty else (b.timestamp.max() - b.timestamp.min()).total_seconds() / 3600

    m = st.columns(4)
    m[0].metric("Outage duration (baseline)", f"{outage_h(base_g):.1f} h")
    m[1].metric("Outage duration (scenario)", f"{outage_h(scen_g):.1f} h", f"{outage_h(scen_g) - outage_h(base_g):+.1f} h", delta_color="inverse")
    m[2].metric("Min availability (scenario)", f"{scen_g.availability.min()*100:.1f}%")
    m[3].metric("Lost user-hours (scenario, 100 M users)", f"{lost_user_hours(scen_g)/1e6:.1f} M",
                f"{(lost_user_hours(scen_g)-lost_user_hours(base_g))/1e6:+.1f} M", delta_color="inverse")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=base_g.timestamp, y=base_g.availability * 100, name="Availability — baseline", line=dict(color=BLUE, width=3)))
    fig.add_trace(go.Scatter(x=scen_g.timestamp, y=scen_g.availability * 100, name="Availability — scenario", line=dict(color="darkorange", width=3, dash="dash")))
    fig.add_trace(go.Scatter(x=base_g.timestamp, y=base_g.healthy_frac * 100, name="Healthy servers — baseline", line=dict(color="seagreen")))
    fig.add_trace(go.Scatter(x=scen_g.timestamp, y=scen_g.healthy_frac * 100, name="Healthy servers — scenario", line=dict(color="crimson", dash="dot")))
    add_phase_bands(fig, P, show_labels=False)
    fig.update_layout(height=450, yaxis_title="%", title="Global (user-weighted) availability and healthy-server share",
                      legend=dict(orientation="h", y=-0.18))
    st.plotly_chart(fig, width="stretch")
    reg = st.selectbox("Inspect region", list(REGIONS))
    rs = sim[sim.region == reg]
    f2 = go.Figure()
    f2.add_trace(go.Scatter(x=rs.timestamp, y=rs.rho, name="ρ utilisation of healthy servers", line=dict(color="crimson")))
    f2.add_trace(go.Scatter(x=rs.timestamp, y=rs.healthy_frac, name="Healthy fraction H/N", line=dict(color="seagreen")))
    f2.add_trace(go.Scatter(x=rs.timestamp, y=rs.capacity_loss, name="Capacity loss d(t)", line=dict(color="grey", dash="dot")))
    f2.add_hline(y=1 - P["w0"] / P["hc_threshold"], line_dash="dash", annotation_text="ρ_crit (health probe fails)")
    f2.update_layout(height=360, title=f"{reg}: feedback loop — fewer servers ⇒ higher ρ ⇒ more failures (baseline)",
                     yaxis_range=[0, 2], legend=dict(orientation="h", y=-0.2))
    st.plotly_chart(f2, width="stretch")
    explain(f"""
<b>Purpose:</b> reproduces the <i>stated</i> failure mechanism — a capacity loss (correlated config change) pushes servers past the
health-check limit; ejected servers shift load to survivors, which then fail too (a <b>cascading / metastable failure</b>).<br>
<b>State per region, every 5 min:</b> healthy servers <code>H</code>, total <code>N = {P['servers']}</code>.<br>
<b>Formulas:</b><br>
• Offered load <code>λ = N·μ·u_peak·diurnal(local hour)</code> — <i>no traffic surge</i>, matching Microsoft's statement<br>
• Effective capacity <code>μ_eff = μ·(1 − d·rollout·ramp)</code>, μ = {P['mu']:.0f} handshakes/s per server<br>
• Utilisation <code>ρ = λ_admitted / (H·μ_eff)</code><br>
• Latency <code>W = W0/(1 − ρ)</code>, W0 = {P['w0']:.0f} ms (M/M/1 queue)<br>
• Critical utilisation <code>ρ_crit = 1 − W0/T_hc</code> = {1 - P['w0']/P['hc_threshold']:.2f} (probe fails when W &gt; T_hc)<br>
• Server loss <code>ΔH = −H·min(0.5, k·(ρ − ρ_crit)) + r·(N − H)</code>, k = {P['fail_k']}, r = {P['auto_recover']}<br>
• Admission control (traffic management) <code>λ_admitted = min(λ, cap·H·μ_eff)</code><br>
• Availability <code>A = min(λ_adm, H·μ_eff)/λ × (1 − timeout penalty)</code><br>
• Lost user-hours <code>= Σ(1 − A)·Δt × users</code> (100 M concurrently active users, illustrative)<br>
<b>Insight:</b> without load shedding the system can stay down even after the trigger is rolled back — restarted servers are
immediately overloaded (the reported "relapse"). Hysteresis and early admission control shorten the outage dramatically.
""")

elif page.startswith("Secure-Connection"):
    st.subheader("Secure-Connection (TLS handshake) Saturation")
    if "handshake_latency_ms" not in df or "tls_utilization" not in df:
        st.warning("This page needs `handshake_latency_ms` and `tls_utilization` columns. Showing model output only.")
        smp = None
    else:
        smp = df.dropna(subset=["tls_utilization"]).sample(min(20000, df["tls_utilization"].notna().sum()), random_state=2)
    rho_line = np.linspace(0, 0.99, 200)
    fig = go.Figure()
    if smp is not None:
        fig.add_trace(go.Scattergl(x=smp["tls_utilization"], y=smp["handshake_latency_ms"], mode="markers",
                                   marker=dict(size=3, color=smp["health_check"].astype(str).map({"Pass": "#2E8B57", "Fail": "crimson"}), opacity=0.4),
                                   name="Server samples (green=Pass, red=Fail)"))
    fig.add_trace(go.Scatter(x=rho_line, y=P["w0"] / (1 - rho_line), name="Theory W = W0/(1−ρ)", line=dict(color=BLUE, width=3)))
    fig.add_hline(y=P["hc_threshold"], line_dash="dash", line_color="crimson", annotation_text=f"Health-check threshold {P['hc_threshold']:.0f} ms")
    fig.add_vline(x=1 - P["w0"] / P["hc_threshold"], line_dash="dot", annotation_text="ρ_crit")
    fig.update_layout(height=450, xaxis_title="TLS utilisation ρ", yaxis_title="Handshake latency (ms, log)", yaxis_type="log",
                      title="Latency explodes as utilisation approaches 1 — the 'hockey stick'", xaxis_range=[0, 1.6])
    st.plotly_chart(fig, width="stretch")
    if smp is not None:
        g = agg_timeseries(df, "15min")
        f2 = go.Figure()
        f2.add_trace(go.Scatter(x=g.timestamp, y=g.latency_p50, name="p50 latency"))
        f2.add_trace(go.Scatter(x=g.timestamp, y=g.latency_p95, name="p95 latency"))
        add_phase_bands(f2, P, show_labels=False)
        f2.update_layout(height=340, yaxis_type="log", title="Handshake latency percentiles over time", yaxis_title="ms")
        st.plotly_chart(f2, width="stretch")
        t = df.groupby("phase", observed=True).agg(median_rho=("tls_utilization", "median"),
                                                   p95_latency_ms=("handshake_latency_ms", lambda x: x.quantile(.95)),
                                                   avg_queue_len=("tls_queue_len", "mean") if "tls_queue_len" in df else ("tls_utilization", "count"),
                                                   hc_fail_pct=("health_check", lambda x: (x.astype(str) == "Fail").mean() * 100)).round(2)
        st.dataframe(t, width="stretch")
    explain(f"""
<b>Purpose:</b> shows <i>why</i> a modest capacity loss became an outage. Microsoft reported that a process establishing secure
connections was overwhelmed; in queueing terms, utilisation ρ crossed the point where latency grows without bound.<br>
<b>Fields:</b> <code>tls_utilization (ρ), handshake_latency_ms (W), tls_queue_len (L), health_check</code>.<br>
<b>Formulas:</b><br>
• <code>ρ = λ/μ</code> (arrival rate ÷ service rate)<br>
• <code>W = W0/(1 − ρ)</code> — at ρ = 0.5 latency doubles; at 0.9 it is 10×; at 0.99, 100×<br>
• Little's law <code>L = λ·W</code> — the number of handshakes waiting<br>
• Health probe fails when <code>W &gt; T_hc</code> ⇔ <code>ρ &gt; 1 − W0/T_hc</code><br>
<b>Reading the chart:</b> red points above the dashed line are servers being ejected by the health checker — each ejection raises ρ on the rest.
""")

elif page.startswith("Service & Regional"):
    st.subheader("Service & Regional Impact (blast radius)")
    if "service" in df:
        s = df.groupby("service", observed=True).agg(requests=("requests", "sum"), errors=("errors", "sum"),
                                                     **({"users_impacted": ("users_impacted", "sum")} if "users_impacted" in df else {}))
        s["availability_pct"] = (1 - s.errors / s.requests.clip(lower=1)) * 100
        s = s.reset_index().sort_values("availability_pct")
        c1, c2 = st.columns(2)
        c1.plotly_chart(px.bar(s, x="availability_pct", y="service", orientation="h", color="availability_pct",
                               color_continuous_scale="RdYlGn", title="Window availability by service (%)",
                               range_x=[max(0, s.availability_pct.min() - 5), 100]), width="stretch")
        dep = pd.DataFrame([(k_, v["dep"], v["incident"]) for k_, v in SERVICES.items()], columns=["service", "dependency_on_failing_layer", "incident_id"])
        c2.markdown("**Dependency model** — share of each workload's traffic that rides the failing connection layer")
        c2.dataframe(dep, hide_index=True, width="stretch")
    if "region" in df:
        r = df.groupby("region", observed=True).agg(requests=("requests", "sum"), errors=("errors", "sum"),
                                                    **({"users_impacted": ("users_impacted", "sum")} if "users_impacted" in df else {}))
        r["availability_pct"] = (1 - r.errors / r.requests.clip(lower=1)) * 100
        r = r.reset_index()
        r["lat"] = r.region.map(lambda x: REGIONS.get(x, {}).get("lat"))
        r["lon"] = r.region.map(lambda x: REGIONS.get(x, {}).get("lon"))
        if r["lat"].notna().any():
            fig = px.scatter_geo(r.dropna(subset=["lat"]), lat="lat", lon="lon", size="errors", color="availability_pct",
                                 hover_name="region", color_continuous_scale="RdYlGn", projection="natural earth",
                                 title="Failed requests by region (bubble size) and availability (colour)", size_max=55)
            fig.update_layout(height=430)
            st.plotly_chart(fig, width="stretch")
        h = agg_timeseries(df, "1h", "region")
        hm = h.pivot(index="region", columns="timestamp", values="availability") * 100
        f3 = px.imshow(hm, aspect="auto", color_continuous_scale="RdYlGn", zmin=max(0, np.nanmin(hm.values)), zmax=100,
                       title="Hourly availability heat-map by region (UTC) — follow-the-sun impact")
        f3.update_layout(height=380)
        st.plotly_chart(f3, width="stretch")
    if {"region", "service", "users_impacted"} <= set(df.columns):
        sb = df.groupby(["region", "service"], observed=True)["users_impacted"].sum().reset_index()
        st.plotly_chart(px.sunburst(sb, path=["region", "service"], values="users_impacted",
                                    title="Impacted user-sessions: region → service"), width="stretch")
    explain("""
<b>Purpose:</b> quantify the blast radius — which workloads and geographies were hit hardest and when.<br>
<b>Fields:</b> <code>service, region, country, requests, errors, users_impacted</code>.<br>
<b>Formulas:</b><br>
• Service availability <code>A_s = 1 − Σerrors_s / Σrequests_s</code><br>
• Dependency model (synthetic): <code>A_service = 1 − dep × (1 − A_core)</code> — Exchange (dep 1.0) is hit fully; services that share the
front-door/authentication layer (Teams, Copilot, SharePoint, Defender, Power Platform) are hit in proportion to dep.<br>
• Heat-map cell <code>= A(region, hour)</code>. Regions are hit as their business day overlaps the degraded window
because load follows local office hours (<code>diurnal = 0.55 + 0.45·e^{−((h−14)/5)²}</code>).
""")

elif page.startswith("Mail Queue"):
    st.subheader("Mail Queue Backlog (Exchange transport)")
    if SRC.startswith("Uploaded") and "mail_queue_depth" in df and "region" in df:
        q = df.groupby([pd.Grouper(key="timestamp", freq="15min"), "region"], observed=True)["mail_queue_depth"].mean().reset_index()
        qcol, qdf = "mail_queue_depth", q
    else:
        qcol, qdf = "mail_queue", sim
        if SRC.startswith("Uploaded"):
            st.info("Uploaded data has no mail_queue_depth — showing model output.")
    fig = px.area(qdf, x="timestamp", y=qcol, color="region", title="Messages waiting for delivery (stacked by region)")
    add_phase_bands(fig, P, show_labels=False)
    fig.add_vline(x=pd.Timestamp("2026-11-13 17:06"), line_dash="dash", annotation_text="Reported: queues significantly reduced")
    fig.update_layout(height=430)
    st.plotly_chart(fig, width="stretch")
    tot = qdf.groupby("timestamp")[qcol].sum()
    peak_t, peak_v = tot.idxmax(), tot.max()
    after = tot[tot.index > peak_t]
    drained = after[after < 0.05 * peak_v]
    c = st.columns(3)
    c[0].metric("Peak backlog", f"{peak_v:,.0f} msgs")
    c[1].metric("Peak time", fmt_ts(peak_t))
    c[2].metric("Drained to <5% of peak", fmt_ts(drained.index[0]) if len(drained) else "not within window")
    explain("""
<b>Purpose:</b> explains why email stayed delayed for many hours <i>after</i> servers recovered.<br>
<b>Formula (queue balance):</b> <code>Q(t+1) = max(0, Q(t) + arrivals(t) − processed(t))</code><br>
• arrivals = peak_mail × diurnal (mail keeps arriving during the outage)<br>
• processed = 1.08 × peak_mail × A(t) — transport has only ~8% spare capacity, so backlog drains slowly<br>
• Drain time ≈ <code>Q_peak / (capacity − arrivals)</code><br>
<b>Fields:</b> <code>mail_queue_depth, region, timestamp</code>. The model's drain aligns with Microsoft's 17:06 UTC 13 Nov update.
""")

elif page.startswith("Detection"):
    st.subheader("Detection & Anomaly Analysis")
    if "handshake_latency_ms" not in df:
        st.warning("Needs handshake_latency_ms. Using error rate instead.")
        metric = "error_rate"
    else:
        metric = st.radio("Signal", ["latency_p50", "error_rate", "hc_fail_rate"], horizontal=True)
    zt = st.slider("z-score threshold", 2.0, 6.0, 3.0, 0.5)
    consec = st.slider("Consecutive 5-min points required", 1, 6, 2)
    ts5 = agg_timeseries(df, "5min")
    if metric not in ts5:
        metric = "error_rate"
    z, first, mu_, sd = detect_anomaly(ts5, metric, pd.Timestamp(P["trigger"]), zt, consec)
    c = st.columns(4)
    c[0].metric("Baseline mean", f"{mu_:.3g}")
    c[1].metric("Baseline σ", f"{sd:.3g}")
    c[2].metric("Alarm raised", fmt_ts(first))
    c[3].metric("Lag vs 16:17 UTC impact start", f"{(first - OFFICIAL_START).total_seconds()/60:.0f} min" if first is not None else "—")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=z.index, y=z.values, name="z-score", line=dict(color=BLUE)))
    fig.add_hline(y=zt, line_dash="dash", line_color="crimson", annotation_text="threshold")
    if first is not None:
        fig.add_vline(x=first, line_color="crimson", annotation_text="Alarm")
    fig.add_vline(x=OFFICIAL_OPEN, line_color="grey", line_dash="dot", annotation_text="EX1550543 opened 16:20")
    fig.update_layout(height=400, title=f"Anomaly score for {metric}", xaxis_range=[WINDOW_START, pd.Timestamp("2026-11-13 06:00")])
    st.plotly_chart(fig, width="stretch")
    st.markdown("**Response metrics (from reported timeline)**")
    rm = pd.DataFrame([
        ("MTTD — time to detect", "16:17 → 16:20 (incident opened)", "3 min"),
        ("Time to multi-service declaration", "16:17 → 18:26", "2 h 09 m"),
        ("Time to correlate a change", "16:17 → overnight (~02:00 modeled)", "≈ 9–10 h"),
        ("Time to 'queues significantly reduced'", "16:17 → 17:06 next day", "24 h 49 m"),
    ], columns=["Metric", "Interval (UTC)", "Value"])
    st.dataframe(rm, hide_index=True, width="stretch")
    explain("""
<b>Purpose:</b> tests how quickly a simple monitor would have flagged the incident, and summarises response metrics.<br>
<b>Formulas:</b><br>
• Baseline = pre-trigger window; <code>z(t) = (x(t) − μ_baseline)/σ_baseline</code><br>
• Alarm when <code>z ≥ threshold</code> for <code>n</code> consecutive 5-minute points (reduces false alarms)<br>
• MTTD = alarm time − impact start; MTTM = mitigation time − impact start; MTTR = recovery time − impact start<br>
<b>Signals:</b> <code>latency_p50</code> (median handshake latency), <code>error_rate</code> (= 1 − A), <code>hc_fail_rate</code>.
""")

elif page.startswith("SLA"):
    st.subheader("SLA & Business Impact")
    sla = sla_table(df)
    st.dataframe(sla, hide_index=True, width="stretch")
    st.caption("Credit tiers are illustrative (<99.9% → 25%, <99% → 50%, <95% → 100%). Check your own Microsoft agreement.")
    st.markdown("#### Organisation impact calculator")
    c = st.columns(4)
    seats = c[0].number_input("Licensed users", 10, 1_000_000, 5000, 100)
    cost_h = c[1].number_input("Loaded cost per user-hour ($)", 10.0, 500.0, 65.0, 5.0)
    blocked = c[2].slider("Share of work blocked when M365 is down", 0.0, 1.0, 0.5, 0.05)
    lic = c[3].number_input("Monthly licence per user ($)", 1.0, 100.0, 36.0, 1.0)
    g = agg_timeseries(df, "15min")
    lost_h = float(((1 - g["availability"].fillna(1)).clip(lower=0) * 0.25).sum())
    prod = seats * lost_h * cost_h * blocked
    exo = sla[sla.service.astype(str).str.startswith("Exchange")]
    credit_pct = int(exo.illustrative_credit_pct.iloc[0]) if len(exo) else int(sla.illustrative_credit_pct.max())
    credit = seats * lic * credit_pct / 100
    m = st.columns(4)
    m[0].metric("Equivalent full-outage hours", f"{lost_h:.2f} h")
    m[1].metric("Productivity loss", f"${prod:,.0f}")
    m[2].metric("Possible SLA credit", f"${credit:,.0f}", f"{credit_pct}% of monthly fee")
    m[3].metric("Net unrecovered cost", f"${prod - credit:,.0f}")
    st.plotly_chart(px.bar(sla, x="service", y="weighted_downtime_min", color="monthly_uptime_pct",
                           color_continuous_scale="RdYlGn", title="Weighted downtime minutes in November by service"), width="stretch")
    explain("""
<b>Purpose:</b> converts technical impact into contractual and financial terms.<br>
<b>Formulas:</b><br>
• Weighted downtime <code>D = Σ_buckets (1 − A_b) × 15 min</code> — a bucket at 40% availability counts as 9 minutes down<br>
• Monthly uptime % <code>= (M − D)/M × 100</code>, M = 43,200 minutes (30-day November)<br>
• Equivalent full-outage hours <code>= Σ(1 − A_b) × 0.25 h</code><br>
• Productivity loss <code>= users × outage hours × cost/hour × share of work blocked</code><br>
• SLA credit <code>= users × monthly licence × credit %</code>; Net cost = productivity loss − credit<br>
<b>Fields:</b> <code>timestamp, service, requests, errors</code>.
""")

elif page.startswith("Reports"):
    st.subheader("Reports & Export")
    st.write("Generate a complete incident report from the active data source in your preferred format.")
    sections = report_sections(df, P, SRC)
    with st.expander("Preview report contents", expanded=True):
        for t, paras, tbl in sections[:3]:
            st.markdown(f"**{t}**")
            for para in paras:
                st.write(para)
            if tbl is not None:
                st.dataframe(tbl, hide_index=True, width="stretch")
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d_%H%M")
    c = st.columns(4)
    with st.spinner("Building documents…"):
        pngs = chart_pngs(df)
        c[0].download_button("PDF report", export_pdf(sections, pngs), f"M365_Outage_Report_{stamp}.pdf", "application/pdf", width="stretch")
        c[1].download_button("Word report", export_docx(sections, pngs), f"M365_Outage_Report_{stamp}.docx",
                             "application/vnd.openxmlformats-officedocument.wordprocessingml.document", width="stretch")
        c[2].download_button("Text report", export_txt(sections), f"M365_Outage_Report_{stamp}.txt", "text/plain", width="stretch")
        c[3].download_button("CSV summary", export_csv_summary(sections), f"M365_Outage_Summary_{stamp}.csv", "text/csv", width="stretch")
    st.markdown("#### Data exports (CSV)")
    d = st.columns(3)
    d[0].download_button("15-min aggregated metrics", agg_timeseries(df, "15min").to_csv(index=False).encode(), f"agg_15min_{stamp}.csv", "text/csv")
    d[1].download_button("Cascade model output", sim.to_csv(index=False).encode(), f"cascade_model_{stamp}.csv", "text/csv")
    d[2].download_button("Active dataset (raw records)", df.to_csv(index=False).encode(), f"records_{stamp}.csv", "text/csv")
    explain("""
<b>Purpose:</b> produce shareable deliverables.<br>
<b>Formats:</b> PDF (ReportLab, with charts), Word .docx (python-docx, with charts), plain text, CSV summary, plus raw/aggregated CSVs.<br>
<b>Contents:</b> executive summary, KPIs, public timeline, availability by service and region, SLA impact, model parameters,
lessons & recommendations. Title and developer line are printed in bold blue in PDF and Word.
""")

else:  # Methodology
    st.subheader("Methodology, Fields & Formulas")
    st.markdown("#### Functions in this application")
    funcs = pd.DataFrame([
        ("Synthetic data generator", "generate_synthetic()", "Samples 1k–1M server-interval records from the cascade model."),
        ("Real data upload & mapping", "guess_column(), validation", "Ingests CSV/XLSX, maps columns, cleans and validates."),
        ("Cascade failure simulator", "run_cascade()", "Region-level state model of health-check ejections and load shift."),
        ("Phase labelling", "label_phase()", "Tags each record with the incident phase."),
        ("Time-series aggregation", "agg_timeseries()", "Availability, latency p50/p95, health-check failure rate per bucket."),
        ("KPI engine", "compute_kpis()", "Availability, impact window, duration, users impacted, detection time."),
        ("TLS saturation analysis", "Secure-Connection page", "Queueing curve W = W0/(1−ρ) vs observed samples."),
        ("Blast-radius analysis", "Service & Regional page", "Service, region, country, heat-map and sunburst breakdowns."),
        ("Mail queue model", "inside run_cascade()", "Backlog build-up and drain."),
        ("Anomaly detection", "detect_anomaly()", "z-score detector with consecutive-point rule; MTTD."),
        ("SLA & business impact", "sla_table(), calculator", "Weighted downtime, uptime %, credits, productivity cost."),
        ("Report export", "export_pdf/docx/txt/csv()", "Downloadable reports in four formats + raw CSVs."),
    ], columns=["Function", "Code", "What it does"])
    st.dataframe(funcs, hide_index=True, width="stretch")
    st.markdown("#### Data dictionary")
    dd = pd.DataFrame([
        ("record_id", "int", "Sequential record number."),
        ("timestamp", "datetime (UTC)", "Start of the 5-minute telemetry interval + random seconds."),
        ("phase", "category", "Incident phase (baseline, onset, widespread, restart & relapse, traffic mgmt, rollback, residual)."),
        ("region / country / datacenter", "category", "Location of server and tenant."),
        ("server_id", "text", "Front-end server, e.g. NAM-FE-0123."),
        ("service / incident_id", "category", "Workload and Microsoft incident ID (EX1550543, MO1550821, PP1550869)."),
        ("health_check", "Pass/Fail", "Automated health-probe result (latency ≤ threshold and server responsive)."),
        ("tls_utilization", "float", "ρ, share of secure-connection capacity in use (blank if unresponsive)."),
        ("handshake_latency_ms", "float", "Time to establish a TLS connection."),
        ("tls_queue_len", "float", "Handshakes waiting (Little's law)."),
        ("cpu_pct", "float", "Server CPU utilisation."),
        ("requests / errors / error_rate_pct", "int/int/float", "Client requests, failures and their ratio."),
        ("active_users / users_impacted", "int", "Users on the server and users who saw a failure."),
        ("mail_queue_depth", "int", "Region-level messages awaiting delivery."),
    ], columns=["Field", "Type", "Meaning"])
    st.dataframe(dd, hide_index=True, width="stretch")
    st.markdown("#### Key formulas")
    st.latex(r"A=1-\frac{\sum errors}{\sum requests}")
    st.latex(r"\rho=\frac{\lambda}{H\cdot\mu_{eff}},\quad \mu_{eff}=\mu\,(1-d)")
    st.latex(r"W=\frac{W_0}{1-\rho},\qquad L=\lambda W,\qquad \rho_{crit}=1-\frac{W_0}{T_{hc}}")
    st.latex(r"H_{t+1}=H_t-H_t\min\big(0.5,\;k(\rho-\rho_{crit})\big)+r\,(N-H_t)")
    st.latex(r"Q_{t+1}=\max\big(0,\;Q_t+\text{arrivals}_t-\text{capacity}\cdot A_t\big)")
    st.latex(r"z_t=\frac{x_t-\mu_{base}}{\sigma_{base}},\qquad \text{Uptime\%}=\frac{M-\sum(1-A_b)\Delta t}{M}\times100")
    st.markdown("#### Model parameters (baseline)")
    st.dataframe(pd.DataFrame([(k_, str(v)) for k_, v in P.items()], columns=["Parameter", "Value"]), hide_index=True, width="stretch")
    st.markdown("#### Assumptions & limitations")
    st.markdown("""
- Times, incident IDs and the described mechanism come from Microsoft's public status updates as reported 12–14 Nov 2026.
  Events marked *Approximate* had no published timestamp.
- **Microsoft has not yet published the root cause.** The model encodes the stated symptoms (health-check ejections, overloaded
  secure-connection process, no traffic increase, correlated configuration change) — it is a teaching model, not a forensic finding.
- Server counts, capacities, user numbers, dependency weights and SLA tiers are synthetic/illustrative.
""")

