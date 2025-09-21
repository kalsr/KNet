import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import io, datetime, base64, os, json

# PAGE CONFIG
st.set_page_config(page_title="Coke vs Pepsi — Ultimate Analyzer", layout="wide", initial_sidebar_state="expanded")

# --- Custom CSS for colorful GUI ---
st.markdown("""
<style>
/* Background gradient */
[data-testid="stAppViewContainer"] {
  background: linear-gradient(180deg, #f7fbff 0%, #ffffff 50%, #f0f8ff 100%);
}
/* Card style */
.section-card {
  background: linear-gradient(90deg, rgba(255,255,255,0.9), rgba(250,250,255,0.9));
  border-radius: 12px;
  padding: 18px;
  box-shadow: 0 4px 12px rgba(14, 30, 37, 0.08);
  margin-bottom: 12px;
}
h1 { color: #0b6fb0; }
.small-muted { color: #6b7280; font-size: 0.9em; }
.btn-refresh { background-color: #16a085; color: white; padding: 8px 12px; border-radius: 8px; }
.btn-pdf { background-color: #1f77b4; color: white; padding: 8px 12px; border-radius: 8px; }
.metric-box { background: linear-gradient(90deg,#ffffff,#f7fcff); padding:10px; border-radius:8px; }
</style>
""", unsafe_allow_html=True)

# ----------------- Utilities & Caching -----------------
@st.cache_data(ttl=600)
def fetch_ticker_cached(ticker):
    """Fetch data with caching (10 minutes TTL)."""
    tk = yf.Ticker(ticker)
    info = tk.info
    hist = tk.history(period='5y', interval='1d', auto_adjust=False)
    # financials may be heavy; fetch but ok cached
    try:
        cashflow = tk.cashflow
        bs = tk.balance_sheet
        fin = tk.financials
    except Exception:
        cashflow = None; bs = None; fin = None
    return {'info': info, 'history': hist, 'cashflow': cashflow, 'bs': bs, 'fin': fin, 'fetched_at': datetime.datetime.utcnow().isoformat()}

def clear_fetch_cache():
    fetch_ticker_cached.clear()

def compute_basic_metrics(info):
    price = info.get('regularMarketPrice') or info.get('previousClose')
    dv = info.get('dividendYield', None)
    if dv is not None: dv = dv * 100.0
    pe = info.get('trailingPE', None) or info.get('forwardPE', None)
    revenue = info.get('totalRevenue', None)
    net_income = info.get('netIncomeToCommon', None) or info.get('netIncome', None)
    cash = info.get('totalCash', None) or info.get('cash', None)
    debt = info.get('totalDebt', None) or info.get('longTermDebt', None)
    shares = info.get('sharesOutstanding', None) or info.get('floatShares', None)
    rev_bil = revenue / 1e9 if revenue else None
    ni_bil = net_income / 1e9 if net_income else None
    return {'price': price, 'dividend_yield_pct': dv, 'pe': pe, 'revenue_bil': rev_bil, 'net_income_bil': ni_bil,
            'cash': cash, 'debt': debt, 'shares': shares}

def extract_fcf(cashflow_df):
    if cashflow_df is None or cashflow_df.empty: return None
    idx = [i.lower() for i in cashflow_df.index.astype(str)]
    for candidate in ['free cash flow','freecashflow']:
        for i,name in enumerate(idx):
            if candidate in name:
                return cashflow_df.iloc[i].fillna(0).astype(float).values[:5]
    ocf=None; capex=None
    for i,name in enumerate(idx):
        if 'operat' in name and 'cash' in name: ocf = cashflow_df.iloc[i].astype(float)
        if 'capital' in name and 'expend' in name: capex = cashflow_df.iloc[i].astype(float)
    if ocf is not None and capex is not None:
        return (ocf - capex).fillna(0).values[:5]
    return None

def multi_stage_dcf_advanced(rev, fcf_hist, shares_out, stages, discount_rate, tax_rate, cash=0.0, debt=0.0, depreciation_schedule=None):
    """
    Multi-stage DCF with explicit capex, NWC, and optional depreciation schedule.
    rev: current revenue USD
    fcf_hist: historical FCF USD array or None
    stages: list of stage dicts {'years','growth','fcf_margin','capex_pct','wc_pct'}
    depreciation_schedule: dict year->depr USD (optional)
    """
    # Base FCF (avg recent) fallback to rev * first stage fcf_margin
    if fcf_hist is not None and len(fcf_hist)>0:
        base_fcf = np.mean(fcf_hist[:3])
    else:
        base_fcf = rev * stages[0].get('fcf_margin', 0.10)
    period_cashflows = []
    cur_rev = rev
    for s in stages:
        years = int(s.get('years', 1))
        g = s.get('growth', 0.0)
        fcf_margin = s.get('fcf_margin', 0.10)
        capex_pct = s.get('capex_pct', 0.04)
        wc_pct = s.get('wc_pct', 0.02)
        for y in range(years):
            cur_rev = cur_rev * (1+g)
            # estimate EBITDA proxy via rev * margin, then subtract taxes/depr/capex/wc change.
            estimated_ebitda = cur_rev * (fcf_margin + capex_pct + wc_pct)  # reverse engineer to allow control
            depr = depreciation_schedule.get('year_' + str(len(period_cashflows)+1), 0.0) if depreciation_schedule else 0.0
            # taxes on EBITDA approximated
            tax = max(0.0, (estimated_ebitda - depr) * tax_rate)
            capex = cur_rev * capex_pct
            wc_change = cur_rev * wc_pct  # simplified proxy
            free_cash = (estimated_ebitda - depr - tax) - capex - wc_change + depr  # add back depr
            # Simplified result: free_cash approximated as rev * fcf_margin - capex - wc_change (similar to earlier)
            free_cash = cur_rev * fcf_margin - capex - wc_change
            period_cashflows.append({'rev': cur_rev, 'fcf': free_cash, 'capex': capex, 'wc_change': wc_change, 'depr': depr, 'tax': tax})
    # Terminal value based on last fcf and terminal growth from stages[-1]['terminal_growth'] or 0.02
    last_fcf = period_cashflows[-1]['fcf']
    terminal_growth = stages[-1].get('terminal_growth', 0.02)
    if discount_rate <= terminal_growth:
        terminal_value = np.nan
    else:
        terminal_value = last_fcf * (1 + terminal_growth) / (discount_rate - terminal_growth)
    # Discount flows
    pv = 0.0
    for i,cf in enumerate(period_cashflows):
        t = i+1
        pv += cf['fcf'] / ((1+discount_rate)**t)
    pv_terminal = terminal_value / ((1+discount_rate)**len(period_cashflows)) if not np.isnan(terminal_value) else 0.0
    enterprise_value = pv + pv_terminal
    equity_value = enterprise_value + (cash if cash else 0.0) - (debt if debt else 0.0)
    intrinsic_per_share = equity_value / shares_out if shares_out and shares_out>0 else np.nan
    return {'periods':period_cashflows,'pv':pv,'pv_terminal':pv_terminal,'enterprise_value':enterprise_value,
            'equity_value':equity_value,'intrinsic_per_share':intrinsic_per_share, 'terminal_value':terminal_value}

def minmax_norm(series, invert=False):
    s = series.dropna()
    if s.empty: return pd.Series([0.5]*len(series), index=series.index)
    mn = s.min(); mx = s.max()
    if mx==mn: return pd.Series([0.5]*len(series), index=series.index)
    norm = (series - mn) / (mx - mn)
    if invert: return 1.0 - norm
    return norm

def fig_to_bytes(fig):
    buf = io.BytesIO(); fig.savefig(buf, format='PNG', bbox_inches='tight'); plt.close(fig); buf.seek(0); return buf.getvalue()

# --- Layout ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/0/09/Coca-Cola_logo.svg",  ****
width=120)
st.sidebar.markdown("## Controls & Actions", unsafe_allow_html=True)
st.sidebar.caption("Use 'Fetch Data' to load cached yfinance data (cached 10 min). Refresh to force new fetch.")

if st.sidebar.button("🔄 Fetch Data (cached)"):
    st.session_state['fetched'] = True
if st.sidebar.button("🔁 Refresh (clear cache + fetch)"):
    clear_fetch_cache()
    st.session_state['fetched'] = True

# Additional actions
if st.sidebar.button("🧹 Clear session"):
    for k in list(st.session_state.keys()):
        del st.session_state[k]
    st.experimental_rerun()

st.title("🍾 Coke vs Pepsi — Ultimate Multi-stage DCF & Reports")
st.markdown("<div class='small-muted'>Interactive valuation, sensitivity, PDF / Excel export, and deployment-ready files.</div>", unsafe_allow_html=True)

# Fetch data
if 'fetched' in st.session_state and st.session_state['fetched']:
    tickers = {'KO':'KO','PEP':'PEP'}
    data = {}
    for k,t in tickers.items():
        try:
            data[k] = fetch_ticker_cached(t)
        except Exception as e:
            st.error(f"Failed to fetch {t}: {e}")
    st.session_state['data'] = data

# Upload override data
uploaded = st.file_uploader("Upload CSV/JSON to override numeric metrics (optional)", type=['csv','json'])
if uploaded is not None:
    try:
        if uploaded.name.lower().endswith('.json'):
            user_df = pd.read_json(uploaded)
        else:
            user_df = pd.read_csv(uploaded)
        st.session_state['user_df'] = user_df
        st.success("User data loaded into session. You can merge or use values in DCF fields.")
    except Exception as e:
        st.error("Upload failed: " + str(e))

# Main
if 'data' in st.session_state:
    data = st.session_state['data']
    ko_info = data['KO']['info']; pep_info = data['PEP']['info']
    ko_basic = compute_basic_metrics(ko_info); pep_basic = compute_basic_metrics(pep_info)
    ko_fcf = extract_fcf(data['KO']['cashflow']); pep_fcf = extract_fcf(data['PEP']['cashflow'])

    # Combined metrics
    combined = pd.DataFrame([
        {'company':'Coca-Cola','ticker':'KO','price':ko_basic['price'],'revenue_bil':ko_basic['revenue_bil'],
         'dividend_yield_pct':ko_basic['dividend_yield_pct'],'pe':ko_basic['pe'],'cash':ko_basic['cash'],'debt':ko_basic['debt'],'shares':ko_basic['shares']},
        {'company':'PepsiCo','ticker':'PEP','price':pep_basic['price'],'revenue_bil':pep_basic['revenue_bil'],
         'dividend_yield_pct':pep_basic['dividend_yield_pct'],'pe':pep_basic['pe'],'cash':pep_basic['cash'],'debt':pep_basic['debt'],'shares':pep_basic['shares']}
    ])

    # Show header cards
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='section-card'><h3 style='color:#c4271d'>Coca-Cola (KO)</h3><div class='small-muted'>Price & key metrics</div></div>", unsafe_allow_html=True)
        st.metric("KO price", f"${ko_basic['price']:.2f}" if ko_basic['price'] else "N/A", delta=None)
        st.write(f"Dividend yield: {ko_basic['dividend_yield_pct']:.2f}% (trailing)" if ko_basic['dividend_yield_pct'] else "Div yield: N/A")
    with c2:
        st.markdown("<div class='section-card'><h3 style='color:#0b6fb0'>PepsiCo (PEP)</h3><div class='small-muted'>Price & key metrics</div></div>", unsafe_allow_html=True)
        st.metric("PEP price", f"${pep_basic['price']:.2f}" if pep_basic['price'] else "N/A", delta=None)
        st.write(f"Dividend yield: {pep_basic['dividend_yield_pct']:.2f}% (trailing)" if pep_basic['dividend_yield_pct'] else "Div yield: N/A")

    # Composite normalization and score
    combined['net_income_bil'] = [ko_basic.get('net_income_bil', np.nan), pep_basic.get('net_income_bil', np.nan)]
    combined['net_margin'] = combined['net_income_bil'] / combined['revenue_bil']
    combined['earnings_yield'] = combined['pe'].apply(lambda x: 1.0/x if pd.notnull(x) and x!=0 else np.nan)
    combined['de_ratio'] = [ko_basic.get('debt')/ (ko_basic.get('cash')+1) if ko_basic.get('debt') else np.nan,
                            pep_basic.get('debt')/ (pep_basic.get('cash')+1) if pep_basic.get('debt') else np.nan]

    combined['norm_net_margin'] = minmax_norm(combined['net_margin'])
    combined['norm_dividend'] = minmax_norm(combined['dividend_yield_pct'])
    combined['norm_ey'] = minmax_norm(combined['earnings_yield'])
    combined['norm_de_inv'] = minmax_norm(combined['de_ratio'], invert=True)
    combined['norm_revenue'] = minmax_norm(combined['revenue_bil'])

    base_weights = {'net_margin':0.35,'dividend_yield':0.20,'earnings_yield':0.20,'debt':0.15,'revenue':0.10}
    combined['fundamental_score'] = (combined['norm_net_margin']*base_weights['net_margin'] + combined['norm_dividend']*base_weights['dividend_yield'] +
                                     combined['norm_ey']*base_weights['earnings_yield'] + combined['norm_de_inv']*base_weights['debt'] + combined['norm_revenue']*base_weights['revenue'])

    st.subheader("Combined key metrics & model score")
    st.dataframe(combined.set_index('company'))

    # Multi-stage DCF input UI (colorful)
    st.subheader("Multi-stage DCF — configure stages & schedules")
    left, right = st.columns([2,1])
    with right:
        st.markdown("<div class='section-card'><h4 style='color:#0b6fb0'>Global DCF settings</h4></div>", unsafe_allow_html=True)
        discount_rate = st.slider("Discount rate (WACC)", 0.01, 0.18, 0.09, 0.005, format="%.3f")
        tax_rate = st.slider("Tax rate (for modeling)", 0.0, 0.40, 0.21, 0.01, format="%.2f")
        default_terminal = st.slider("Default terminal growth", 0.0, 0.05, 0.02, 0.001, format="%.3f")
        # Depreciation schedule example input (JSON)
        depr_input = st.text_area("Optional depreciation schedule (JSON, e.g. {\"year_1\":100000000, \"year_2\":90000000})", height=80)
        try:
            depreciation_schedule = json.loads(depr_input) if depr_input.strip() else {}
        except Exception:
            depreciation_schedule = {}
            st.error("Invalid JSON for depreciation schedule. Using empty schedule.")

    with left:
        st.markdown("<div class='section-card'><h4 style='color:#c4271d'>Coca-Cola stages</h4></div>", unsafe_allow_html=True)
        ko_rev_usd = (combined.loc[0,'revenue_bil']*1e9) if pd.notnull(combined.loc[0,'revenue_bil']) else st.number_input("KO revenue (USD)", key='ko_rev_input', value=47.1e9)
        ko_stage1_years = st.number_input("KO stage1 years", min_value=1, max_value=5, value=2, key='ko_s1y')
        ko_stage1_growth = st.number_input("KO stage1 growth", min_value=-0.1, max_value=0.3, value=0.04, step=0.005, key='ko_s1g')
        ko_stage1_fcfm = st.number_input("KO stage1 FCF margin (decimal)", min_value=0.0, max_value=0.5, value=0.12, step=0.005, key='ko_s1m')
        ko_stage1_capex = st.number_input("KO stage1 capex % of rev", min_value=0.0, max_value=0.2, value=0.04, step=0.001, key='ko_s1c')
        ko_stage1_wc = st.number_input("KO stage1 WC % of rev", min_value=0.0, max_value=0.2, value=0.01, step=0.001, key='ko_s1w')
        ko_stage2_years = st.number_input("KO stage2 years", min_value=1, max_value=7, value=3, key='ko_s2y')
        ko_stage2_growth = st.number_input("KO stage2 growth", min_value=-0.05, max_value=0.2, value=0.03, step=0.005, key='ko_s2g')
        ko_stage2_fcfm = st.number_input("KO stage2 FCF margin", min_value=0.0, max_value=0.5, value=0.115, step=0.005, key='ko_s2m')
        ko_stage2_capex = st.number_input("KO stage2 capex %", min_value=0.0, max_value=0.2, value=0.035, step=0.001, key='ko_s2c')
        ko_stage2_wc = st.number_input("KO stage2 WC %", min_value=0.0, max_value=0.2, value=0.01, step=0.001, key='ko_s2w')
        ko_terminal_growth = st.number_input("KO terminal growth", min_value=0.0, max_value=0.05, value=float(default_terminal), step=0.001, key='ko_tg')

    # Pepsi inputs (mirror)
    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    left2, right2 = st.columns([2,1])
    with left2:
        st.markdown("<div class='section-card'><h4 style='color:#0b6fb0'>PepsiCo stages</h4></div>", unsafe_allow_html=True)
        pep_rev_usd = (combined.loc[1,'revenue_bil']*1e9) if pd.notnull(combined.loc[1,'revenue_bil']) else st.number_input("PEP revenue (USD)", key='pep_rev_input', value=91.85e9)
        pep_stage1_years = st.number_input("PEP stage1 years", min_value=1, max_value=5, value=2, key='pep_s1y')
        pep_stage1_growth = st.number_input("PEP stage1 growth", min_value=-0.1, max_value=0.3, value=0.05, step=0.005, key='pep_s1g')
        pep_stage1_fcfm = st.number_input("PEP stage1 FCF margin", min_value=0.0, max_value=0.5, value=0.10, step=0.005, key='pep_s1m')
        pep_stage1_capex = st.number_input("PEP stage1 capex %", min_value=0.0, max_value=0.2, value=0.045, step=0.001, key='pep_s1c')
        pep_stage1_wc = st.number_input("PEP stage1 WC %", min_value=0.0, max_value=0.2, value=0.015, step=0.001, key='pep_s1w')
        pep_stage2_years = st.number_input("PEP stage2 years", min_value=1, max_value=7, value=3, key='pep_s2y')
        pep_stage2_growth = st.number_input("PEP stage2 growth", min_value=-0.05, max_value=0.2, value=0.03, step=0.005, key='pep_s2g')
        pep_stage2_fcfm = st.number_input("PEP stage2 FCF margin", min_value=0.0, max_value=0.5, value=0.095, step=0.005, key='pep_s2m')
        pep_stage2_capex = st.number_input("PEP stage2 capex %", min_value=0.0, max_value=0.2, value=0.04, step=0.001, key='pep_s2c')
        pep_stage2_wc = st.number_input("PEP stage2 WC %", min_value=0.0, max_value=0.2, value=0.01, step=0.001, key='pep_s2w')
        pep_terminal_growth = st.number_input("PEP terminal growth", min_value=0.0, max_value=0.05, value=float(default_terminal), step=0.001, key='pep_tg')

    # Build stages
    ko_stages = [
        {'years': ko_stage1_years, 'growth': ko_stage1_growth, 'fcf_margin': ko_stage1_fcfm, 'capex_pct': ko_stage1_capex, 'wc_pct': ko_stage1_wc},
        {'years': ko_stage2_years, 'growth': ko_stage2_growth, 'fcf_margin': ko_stage2_fcfm, 'capex_pct': ko_stage2_capex, 'wc_pct': ko_stage2_wc, 'terminal_growth': ko_terminal_growth}
    ]
    pep_stages = [
        {'years': pep_stage1_years, 'growth': pep_stage1_growth, 'fcf_margin': pep_stage1_fcfm, 'capex_pct': pep_stage1_capex, 'wc_pct': pep_stage1_wc},
        {'years': pep_stage2_years, 'growth': pep_stage2_growth, 'fcf_margin': pep_stage2_fcfm, 'capex_pct': pep_stage2_capex, 'wc_pct': pep_stage2_wc, 'terminal_growth': pep_terminal_growth}
    ]

    # Run multi-stage DCF scenarios scaled
    def run_scaled(rev_usd, fcf_h, shares, cash, debt, stages, scale):
        scaled = []
        for s in stages:
            s2 = s.copy()
            s2['growth'] = s.get('growth',0.0) * scale
            scaled.append(s2)
        return multi_stage_dcf_advanced(rev_usd, fcf_h, shares, scaled, discount_rate, tax_rate, cash=cash, debt=debt, depreciation_schedule=depreciation_schedule)

    scales = {'conservative':0.8, 'base':1.0, 'aggressive':1.2}
    ko_results = {k: run_scaled(ko_rev_usd, ko_fcf, combined.loc[0,'shares'] or 1.0, combined.loc[0,'cash'] or 0.0, combined.loc[0,'debt'] or 0.0, ko_stages, v) for k,v in scales.items()}
    pep_results = {k: run_scaled(pep_rev_usd, pep_fcf, combined.loc[1,'shares'] or 1.0, combined.loc[1,'cash'] or 0.0, combined.loc[1,'debt'] or 0.0, pep_stages, v) for k,v in scales.items()}

    # Scenario DataFrame
    rows = []
    for comp, res in [('Coca-Cola', ko_results), ('PepsiCo', pep_results)]:
        for sname, r in res.items():
            rows.append({'company': comp, 'scenario': sname, 'intrinsic_per_share': r['intrinsic_per_share'], 'market_price': combined.loc[combined['company']==comp,'price'].iloc[0], 'upside_pct': ((r['intrinsic_per_share'] - combined.loc[combined['company']==comp,'price'].iloc[0]) / combined.loc[combined['company']==comp,'price'].iloc[0] * 100.0) if pd.notnull(r['intrinsic_per_share']) and pd.notnull(combined.loc[combined['company']==comp,'price'].iloc[0]) else np.nan})
    scen_df = pd.DataFrame(rows)

    st.subheader("Scenario results (intrinsic per share & upside)")
    st.dataframe(scen_df.set_index(['company','scenario']))

    # Sensitivity analysis
    st.subheader("Sensitivity analysis (composite weight sampling)")
    if st.button("▶️ Run sensitivity analysis now"):
        samples = int(st.sidebar.number_input("Samples for sensitivity", min_value=200, max_value=5000, value=1000, step=100))
        rng = np.random.default_rng(2025)
        wins = {'KO':0,'PEP':0}
        for i in range(samples):
            w = rng.dirichlet(np.ones(5))
            nm = minmax_norm(pd.Series([combined.loc[0,'net_income_bil']/combined.loc[0,'revenue_bil'] if pd.notnull(combined.loc[0,'net_income_bil']) and pd.notnull(combined.loc[0,'revenue_bil']) else np.nan, combined.loc[1,'net_income_bil']/combined.loc[1,'revenue_bil'] if pd.notnull(combined.loc[1,'net_income_bil']) and pd.notnull(combined.loc[1,'revenue_bil']) else np.nan]))
            nd = minmax_norm(pd.Series([combined.loc[0,'dividend_yield_pct'], combined.loc[1,'dividend_yield_pct']]))
            ney = minmax_norm(pd.Series([1.0/combined.loc[0,'pe'] if pd.notnull(combined.loc[0,'pe']) and combined.loc[0,'pe']!=0 else np.nan, 1.0/combined.loc[1,'pe'] if pd.notnull(combined.loc[1,'pe']) and combined.loc[1,'pe']!=0 else np.nan]))
            nde = minmax_norm(pd.Series([combined.loc[0,'debt'] if pd.notnull(combined.loc[0,'debt']) else np.nan, combined.loc[1,'debt'] if pd.notnull(combined.loc[1,'debt']) else np.nan]), invert=True)
            nr = minmax_norm(pd.Series([combined.loc[0,'revenue_bil'], combined.loc[1,'revenue_bil']]))
            score0 = nm.iloc[0]*w[0] + nd.iloc[0]*w[1] + ney.iloc[0]*w[2] + nde.iloc[0]*w[3] + nr.iloc[0]*w[4]
            score1 = nm.iloc[1]*w[0] + nd.iloc[1]*w[1] + ney.iloc[1]*w[2] + nde.iloc[1]*w[3] + nr.iloc[1]*w[4]
            winner = 'KO' if score0 > score1 else 'PEP'
            wins[winner] += 1
        ko_pct = wins['KO']/samples*100.0; pep_pct = wins['PEP']/samples*100.0
        st.metric("KO wins", f"{wins['KO']} / {samples} ({ko_pct:.1f}%)"); st.metric("PEP wins", f"{wins['PEP']} / {samples} ({pep_pct:.1f}%)")
        fig, ax = plt.subplots(figsize=(4,3)); ax.pie([ko_pct, pep_pct], labels=[f"KO {ko_pct:.1f}%", f"PEP {pep_pct:.1f}%"], autopct='%1.1f%%'); st.pyplot(fig)
        st.session_state['sensitivity'] = {'samples': samples, 'wins': wins, 'ko_pct': ko_pct, 'pep_pct': pep_pct}

    # Combined downloadables
    st.subheader("Downloads: CSV / JSON / Excel / PDF")
    combined_export = combined.copy()
    combined_export.to_csv('combined_export.csv', index=False)
    st.download_button("⬇️ Download combined CSV", combined_export.to_csv(index=False).encode('utf-8'), file_name="coke_pepsi_combined.csv", mime="text/csv")
    st.download_button("⬇️ Download combined JSON", data=combined_export.to_json(orient='records'), file_name="coke_pepsi_combined.json", mime="application/json")

    # Create Excel bytes
    def create_excel_bytes():
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            combined.to_excel(writer, sheet_name='Summary', index=False)
            scen_df.to_excel(writer, sheet_name='DCF_Scenarios', index=False)
            if 'sensitivity' in st.session_state:
                pd.DataFrame([st.session_state['sensitivity']]).to_excel(writer, sheet_name='Sensitivity', index=False)
            # detailed projections
            for comp, res in [('Coca-Cola', ko_results), ('PepsiCo', pep_results)]:
                # take base scenario periods
                base_periods = res['base']['periods']
                if base_periods:
                    pd.DataFrame(base_periods).to_excel(writer, sheet_name=f"{comp}_proj", index=False)
            writer.save()
        output.seek(0); return output.getvalue()

    excel_bytes = create_excel_bytes()
    st.download_button("⬇️ Download Excel report", data=excel_bytes, file_name="coke_pepsi_ultimate_report.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    # Build polished PDF via ReportLab
    if st.button("📄 Build polished PDF report"):
        buf = io.BytesIO()
        doc = SimpleDocTemplate(buf, pagesize=letter)
        styles = getSampleStyleSheet(); elems = []
        elems.append(Paragraph("Coke vs Pepsi — Ultimate Analysis Report", styles['Title'])); elems.append(Spacer(1,12))
        elems.append(Paragraph(f"Generated: {datetime.datetime.utcnow().isoformat()}", styles['Normal'])); elems.append(Spacer(1,12))

        # Key summary table
        elems.append(Paragraph("Key metrics", styles['Heading2']))
        table_data = [['Company','Ticker','Price','Revenue (B)','P/E','Div yield %']]
        for _,r in combined.iterrows():
            table_data.append([r['company'], r['ticker'], f"${r['price']:.2f}" if pd.notnull(r['price']) else 'N/A', f"{r['revenue_bil']:.2f}" if pd.notnull(r['revenue_bil']) else 'N/A', f"{r['pe']:.2f}" if pd.notnull(r['pe']) else 'N/A', f"{r['dividend_yield_pct']:.2f}" if pd.notnull(r['dividend_yield_pct']) else 'N/A'])
        t = Table(table_data, hAlign='LEFT'); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#0b6fb0')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),0.5,colors.grey)]))
        elems.append(t); elems.append(Spacer(1,12))

        # DCF scenario table
        elems.append(Paragraph("DCF scenario intrinsic per share", styles['Heading2']))
        sdata = [['Company','Scenario','Intrinsic/share','Market price','Upside %']]
        for _,r in scen_df.iterrows():
            sdata.append([r['company'], r['scenario'], f"${r['intrinsic_per_share']:.2f}" if pd.notnull(r['intrinsic_per_share']) else 'N/A', f"${r['market_price']:.2f}" if pd.notnull(r['market_price']) else 'N/A', f"{r['upside_pct']:.1f}%" if pd.notnull(r['upside_pct']) else 'N/A'])
        t2 = Table(sdata, hAlign='LEFT'); t2.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#c4271d')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),0.5,colors.grey)]))
        elems.append(t2); elems.append(Spacer(1,12))

        # Price chart image
        fig, ax = plt.subplots(figsize=(6,3))
        if data['KO']['history'] is not None: ax.plot(data['KO']['history'].index, data['KO']['history']['Close'], label='KO')
        if data['PEP']['history'] is not None: ax.plot(data['PEP']['history'].index, data['PEP']['history']['Close'], label='PEP')
        ax.legend(); ax.set_title('5-year price history')
        imgbuf = io.BytesIO(); fig.savefig(imgbuf, format='PNG', bbox_inches='tight'); plt.close(fig); imgbuf.seek(0)
        rl_img = RLImage(imgbuf, width=6*inch, height=3*inch); elems.append(rl_img); elems.append(Spacer(1,12))

        # Sensitivity summary
        if 'sensitivity' in st.session_state:
            s = st.session_state['sensitivity']
            elems.append(Paragraph("Sensitivity summary", styles['Heading2'])); elems.append(Paragraph(f"Samples: {s['samples']}", styles['Normal']))
            elems.append(Paragraph(f"KO wins: {s['wins']['KO']} ({s['ko_pct']:.1f}%)", styles['Normal'])); elems.append(Paragraph(f"PEP wins: {s['wins']['PEP']} ({s['pep_pct']:.1f}%)", styles['Normal']))
            # pie chart image
            fig2, ax2 = plt.subplots(figsize=(3,3)); ax2.pie([s['ko_pct'], s['pep_pct']], labels=[f"KO {s['ko_pct']:.1f}%", f"PEP {s['pep_pct']:.1f}%"], autopct='%1.1f%%'); img2 = io.BytesIO(); fig2.savefig(img2, format='PNG', bbox_inches='tight'); plt.close(fig2); img2.seek(0)
            rl_img2 = RLImage(img2, width=3*inch, height=3*inch); elems.append(rl_img2); elems.append(Spacer(1,12))

        elems.append(Paragraph("Notes: This valuation uses simplified modeling for demonstration. Use detailed statements for production valuations.", styles['Italic']))
        doc.build(elems)
        buf.seek(0); b64 = base64.b64encode(buf.read()).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="coke_pepsi_ultimate_report.pdf"><button class="btn-pdf">⬇️ Download PDF</button></a>'
        st.markdown(href, unsafe_allow_html=True)

    # Generate requirements.txt and README for deployment
    if st.button("📦 Generate requirements.txt & README"):
        reqs = """streamlit
yfinance
pandas
numpy
matplotlib
reportlab
openpyxl
xlsxwriter
        """
        readme = f"""# Coke vs Pepsi — Ultimate Analyzer