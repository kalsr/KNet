


import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import io, datetime, json, base64

st.set_page_config(page_title="Coke vs Pepsi — Advanced Investment Analyzer", layout="wide")

# ---------- Helper functions ----------
def fetch_company_data(ticker):
    tk = yf.Ticker(ticker)
    info = tk.info
    hist = tk.history(period='5y', interval='1d', auto_adjust=False)
    # Financial statements
    try:
        cashflow = tk.cashflow  # pandas DataFrame (recent columns are years)
        bs = tk.balance_sheet
        fin = tk.financials
    except Exception:
        cashflow = None
        bs = None
        fin = None
    return {'info': info, 'history': hist, 'cashflow': cashflow, 'bs': bs, 'fin': fin}

def compute_simple_metrics(data):
    info = data['info']
    # Price
    price = info.get('regularMarketPrice') or info.get('previousClose')
    # Dividend yield (percent)
    div_yield = info.get('dividendYield', None)
    if div_yield is not None:
        div_yield = div_yield * 100.0
    pe = info.get('trailingPE', None)
    de_ratio = info.get('debtToEquity', None)
    revenue = info.get('totalRevenue', None)
    net_income = info.get('netIncomeToCommon', None) or info.get('netIncome', None)
    # Convert to billions when appropriate
    rev_bil = revenue / 1e9 if revenue else None
    ni_bil = net_income / 1e9 if net_income else None
    return {'price': price, 'dividend_yield_pct': div_yield, 'pe': pe, 'de_ratio': de_ratio,
            'revenue_bil': rev_bil, 'net_income_bil': ni_bil}

def extract_historical_fcf(cashflow_df):
    # Attempt to get Free Cash Flow from cashflow: "Free Cash Flow" or compute OCF - CapEx
    if cashflow_df is None or cashflow_df.empty:
        return None
    idx = [i.lower() for i in cashflow_df.index.astype(str)]
    cols = cashflow_df.columns
    # try direct
    for candidate in ['free cash flow', 'freecashflow', 'freecashflows']:
        for i,name in enumerate(idx):
            if candidate in name:
                series = cashflow_df.iloc[i]
                # convert to numeric and return recent 5 (in absolute USD)
                return series.fillna(0).astype(float).values[:5]
    # else try operatingCashflow - capitalExpenditures
    ocf = None
    capex = None
    for i,name in enumerate(idx):
        if 'operat' in name and 'cash' in name:
            ocf = cashflow_df.iloc[i].astype(float)
        if 'capital' in name and 'expend' in name:
            capex = cashflow_df.iloc[i].astype(float)
    if ocf is not None and capex is not None:
        fcf = ocf - capex
        return fcf.fillna(0).values[:5]
    return None

def dcf_5yr(fcf_hist, revenue, growth_rate, terminal_growth, discount_rate, shares_outstanding):
    # fcf_hist: array recent historical FCF (USD). If None, approximate using net income proxy.
    # We'll take last FCF or average of last 3 as base
    if fcf_hist is None or len(fcf_hist)==0:
        base = None
    else:
        base = np.mean(fcf_hist[:3])
    if base is None and revenue is not None:
        # fallback: approximate FCF margin 10% of revenue
        base = revenue * 1e9 * 0.10  # revenue in billions -> USD
    if base is None:
        return None
    # project 5 years
    years = np.arange(1,6)
    projected = [base * ((1 + growth_rate) ** y) for y in years]
    # terminal value using Gordon Growth on year 5 FCF
    terminal_fcf = projected[-1] * (1 + terminal_growth)
    terminal_value = terminal_fcf / (discount_rate - terminal_growth) if discount_rate > terminal_growth else np.nan
    # discount cash flows to present (assume year-end)
    discounted = [projected[i] / ((1 + discount_rate) ** (i+1)) for i in range(5)]
    discounted_terminal = terminal_value / ((1 + discount_rate) ** 5)
    pv_total = np.nansum(discounted) + discounted_terminal
    # Per-share intrinsic value: (PV_total + cash - debt) / shares; we don't have cash/debt reliably here, so return enterprise-free approach
    intrinsic_per_share = pv_total / shares_outstanding if shares_outstanding and shares_outstanding>0 else pv_total
    return {'pv_total': pv_total, 'intrinsic_per_share': intrinsic_per_share, 'projected': projected, 'terminal_value': terminal_value, 'discounted': discounted, 'discounted_terminal': discounted_terminal}

def one_year_return(hist):
    if hist is None or hist.empty: return None
    # Use last 252 trading days approx 1 year; use 'Close'
    closes = hist['Close'].dropna()
    if len(closes) < 2: return None
    # find approx 1 year ago by date
    start = closes.iloc[0]
    end = closes.iloc[-1]
    if start == 0: return None
    return (end - start)/start * 100.0

def minmax_norm(series, invert=False):
    s = series.dropna()
    if s.empty:
        return pd.Series([0.5]*len(series), index=series.index)
    mn = s.min(); mx = s.max()
    if mx==mn:
        return pd.Series([0.5]*len(series), index=series.index)
    norm = (series - mn) / (mx - mn)
    if invert:
        return 1.0 - norm
    return norm

# ---------- UI ----------
st.markdown("<h1 style='color:#0b6fb0'>🍾 Coke vs Pepsi — Advanced Investment Analyzer</h1>", unsafe_allow_html=True)
st.markdown("Compare The Coca-Cola Company (KO) and PepsiCo (PEP) with: DCF 5-year template, sensitivity analysis, downloadable PDF report, and a tunable composite model. **Educational only — not financial advice.**")

left, right = st.columns([2,1])

with right:
    st.markdown("### Controls & Quick Links")
    st.markdown("- Coca‑Cola 2024 10‑K (SEC): https://www.sec.gov")
    st.markdown("- PepsiCo 2024 10‑K (SEC): https://www.sec.gov")
    st.markdown("---")
    st.header("Model inputs")
    discount_rate = st.slider("Discount rate (WACC proxy)", 0.01, 0.20, 0.09, 0.005, format="%.3f")
    terminal_growth = st.slider("Terminal growth rate (g)", 0.0, 0.05, 0.02, 0.001, format="%.3f")
    default_fc_growth = st.slider("Default 5yr FCF growth (used if not provided)", -0.05, 0.20, 0.05, 0.005, format="%.3f")
    st.markdown("---")
    st.header("Sensitivity Analysis")
    n_samples = st.number_input("Number of weight samples (sensitivity)", min_value=100, max_value=5000, value=1000, step=100)
    st.info("Sensitivity will randomly sample weight vectors and count which ticker wins the composite score. Robustness = % of samples where one stock is preferred.")

# Action buttons row (colored style using markdown)
col_fetch, col_clear, col_pdf = st.columns([1,1,1])
if col_fetch.button("🔄 Fetch live data", key='fetch'):
    st.session_state['fetch_ts'] = datetime.datetime.utcnow().isoformat()
    st.session_state['fetched'] = True
if col_clear.button("🧹 Clear / Reset", key='clear'):
    keys = [k for k in list(st.session_state.keys()) if k not in ['sidebar_state']]
    for k in keys:
        del st.session_state[k]
    st.experimental_rerun()

if col_pdf.button("📄 Generate PDF report", key='genpdf'):
    st.session_state['generate_pdf'] = True

# Upload user file
uploaded = st.file_uploader("Upload your own metrics (CSV or JSON) to merge or override", type=['csv','json'])
if uploaded is not None:
    try:
        if uploaded.name.lower().endswith('.json'):
            user_df = pd.read_json(uploaded)
        else:
            user_df = pd.read_csv(uploaded)
        st.session_state['user_df'] = user_df
        st.success("User file uploaded")
    except Exception as e:
        st.error("Upload error: " + str(e))

# Fetch data if asked
if 'fetched' in st.session_state and st.session_state['fetched']:
    tickers = {'KO':'KO', 'PEP':'PEP'}
    data = {}
    for k,t in tickers.items():
        try:
            data[k] = fetch_company_data(t)
        except Exception as e:
            st.error(f"Failed to fetch {t}: {e}")
    st.session_state['data'] = data

# Main analysis display
if 'data' in st.session_state:
    data = st.session_state['data']
    # Compute metrics
    ko_metrics = compute_simple_metrics(data['KO'])
    pep_metrics = compute_simple_metrics(data['PEP'])
    # Historical FCF extraction
    ko_fcf_hist = extract_historical_fcf(data['KO']['cashflow'])
    pep_fcf_hist = extract_historical_fcf(data['PEP']['cashflow'])

    # Shares outstanding fallback from info (float)
    ko_shares = data['KO']['info'].get('sharesOutstanding', None)
    pep_shares = data['PEP']['info'].get('sharesOutstanding', None)

    # Build DataFrame
    df = pd.DataFrame([
        {'company':'Coca-Cola','ticker':'KO','price':ko_metrics['price'],'revenue_bil':ko_metrics['revenue_bil'],
         'net_income_bil':ko_metrics['net_income_bil'] if 'net_income_bil' in ko_metrics else None,
         'dividend_yield_pct': ko_metrics['dividend_yield_pct'],'pe':ko_metrics['pe'],'de_ratio':ko_metrics['de_ratio']},
        {'company':'PepsiCo','ticker':'PEP','price':pep_metrics['price'],'revenue_bil':pep_metrics['revenue_bil'],
         'net_income_bil':pep_metrics.get('net_income_bil', None),
         'dividend_yield_pct': pep_metrics['dividend_yield_pct'],'pe':pep_metrics['pe'],'de_ratio':pep_metrics['de_ratio']}
    ])

    # compute net margin if possible
    df['net_margin'] = df['net_income_bil'] / df['revenue_bil']

    # earnings yield
    df['earnings_yield'] = df['pe'].apply(lambda x: 1.0/x if pd.notnull(x) and x!=0 else np.nan)

    # momentum 1yr
    df['1y_return_pct'] = [one_year_return(data['KO']['history']), one_year_return(data['PEP']['history'])]

    # Default weights (you can randomize in sensitivity)
    base_weights = {'net_margin':0.35,'dividend_yield':0.20,'earnings_yield':0.20,'debt':0.15,'revenue':0.10}

    # Normalized columns
    df['norm_net_margin'] = minmax_norm(df['net_margin'])
    df['norm_dividend'] = minmax_norm(df['dividend_yield_pct'])
    df['norm_ey'] = minmax_norm(df['earnings_yield'])
    df['norm_de_inv'] = minmax_norm(df['de_ratio'], invert=True)
    df['norm_revenue'] = minmax_norm(df['revenue_bil'])

    df['fundamental_score'] = (df['norm_net_margin']*base_weights['net_margin'] + df['norm_dividend']*base_weights['dividend_yield'] +
                              df['norm_ey']*base_weights['earnings_yield'] + df['norm_de_inv']*base_weights['debt'] + df['norm_revenue']*base_weights['revenue'])

    # DCF calculations per company (using default growth unless user inputs per-company)
    st.subheader("DCF / 5-year forecast inputs (per company)")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Coca‑Cola (KO)**")
        ko_growth = st.number_input("KO 5yr growth rate", key='ko_growth', min_value=-0.10, max_value=0.30, value=float(default_fc_growth), step=0.005, format="%.3f")
        ko_terminal = st.number_input("KO terminal growth", key='ko_term', min_value=0.0, max_value=0.05, value=float(terminal_growth), step=0.001, format="%.3f")
    with col2:
        st.markdown("**PepsiCo (PEP)**")
        pep_growth = st.number_input("PEP 5yr growth rate", key='pep_growth', min_value=-0.10, max_value=0.30, value=float(default_fc_growth), step=0.005, format="%.3f")
        pep_terminal = st.number_input("PEP terminal growth", key='pep_term', min_value=0.0, max_value=0.05, value=float(terminal_growth), step=0.001, format="%.3f")

    # Run DCF using extracted FCF or approximations
    ko_dcf = dcf_5yr(ko_fcf_hist, ko_metrics['revenue_bil'], ko_growth, ko_terminal, discount_rate, ko_shares or 1.0)
    pep_dcf = dcf_5yr(pep_fcf_hist, pep_metrics['revenue_bil'], pep_growth, pep_terminal, discount_rate, pep_shares or 1.0)

    # Show DCF results
    st.subheader("DCF 5-year results (simple template)")
    dcf_df = pd.DataFrame([
        {'company':'Coca-Cola','ticker':'KO','intrinsic_per_share': ko_dcf['intrinsic_per_share'] if ko_dcf else np.nan,
         'pv_total': ko_dcf['pv_total'] if ko_dcf else np.nan},
        {'company':'PepsiCo','ticker':'PEP','intrinsic_per_share': pep_dcf['intrinsic_per_share'] if pep_dcf else np.nan,
         'pv_total': pep_dcf['pv_total'] if pep_dcf else np.nan},
    ])
    st.dataframe(dcf_df.set_index('company'))

    # Compare intrinsic vs market price
    dcf_df['market_price'] = [df.loc[0,'price'], df.loc[1,'price']]
    dcf_df['upside_pct'] = (dcf_df['intrinsic_per_share'] - dcf_df['market_price']) / dcf_df['market_price'] * 100.0
    st.markdown("**Intrinsic vs Market price (simple approximation)**")
    st.dataframe(dcf_df[['ticker','market_price','intrinsic_per_share','upside_pct']].set_index('ticker'))

    # Sensitivity analysis: sample many weight vectors and count wins
    st.subheader("Sensitivity analysis (weight sampling)")
    run_sens = st.button("▶️ Run sensitivity now", key='runsens')
    if run_sens or 'sens_results' in st.session_state:
        # perform sampling
        samples = n_samples
        rng = np.random.default_rng(12345)
        wins = {'KO':0,'PEP':0}
        scores_store = []
        for i in range(samples):
            # sample Dirichlet for 5 components
            w = rng.dirichlet(alpha=np.ones(5))
            # map to weight names order: net_margin, dividend, earnings_yield, debt, revenue
            score = df['norm_net_margin']*w[0] + df['norm_dividend']*w[1] + df['norm_ey']*w[2] + df['norm_de_inv']*w[3] + df['norm_revenue']*w[4]
            winner = df.loc[score.idxmax(),'ticker']
            wins[winner] += 1
            scores_store.append(score.values)
        # compute robustness
        ko_pct = wins['KO']/samples*100.0
        pep_pct = wins['PEP']/samples*100.0
        st.session_state['sens_results'] = {'wins':wins,'ko_pct':ko_pct,'pep_pct':pep_pct,'samples':samples}
    if 'sens_results' in st.session_state:
        sr = st.session_state['sens_results']
        st.metric("KO wins (samples)", f"{sr['wins']['KO']} / {sr['samples']} ({sr['ko_pct']:.1f}%)", delta=None)
        st.metric("PEP wins (samples)", f"{sr['wins']['PEP']} / {sr['samples']} ({sr['pep_pct']:.1f}%)", delta=None)
        # show pie chart
        fig, ax = plt.subplots(figsize=(4,3))
        ax.pie([sr['ko_pct'], sr['pep_pct']], labels=[f"KO {sr['ko_pct']:.1f}%", f"PEP {sr['pep_pct']:.1f}%"], startangle=140, autopct='%1.1f%%')
        ax.set_title("Robustness: share of weight samples preferring each stock")
        st.pyplot(fig)

    # Show combined table and allow downloads
    st.subheader("Combined metrics & model")
    combined = df.copy()
    combined = combined[['company','ticker','price','revenue_bil','net_income_bil','net_margin','dividend_yield_pct','pe','de_ratio','1y_return_pct','fundamental_score']]
    st.dataframe(combined.set_index('company'))

    csv = combined.to_csv(index=False).encode('utf-8')
    json_blob = combined.to_json(orient='records', date_format='iso')

    st.download_button("⬇️ Download combined results (CSV)", data=csv, file_name="coke_pepsi_combined.csv", mime="text/csv")
    st.download_button("⬇️ Download combined results (JSON)", data=json_blob, file_name="coke_pepsi_combined.json", mime="application/json")

    # Generate PDF if requested
    if 'generate_pdf' in st.session_state and st.session_state['generate_pdf']:
        out_buf = io.BytesIO()
        with PdfPages(out_buf) as pdf:
            # Page 1: summary table
            fig1, ax1 = plt.subplots(figsize=(8.5,11))
            ax1.axis('off')
            txt = f"Coke vs Pepsi — Analysis Report\\nGenerated: {datetime.datetime.utcnow().isoformat()}\\n\\nSummary comparison:\\n"
            for i,row in combined.iterrows():
                txt += f"\\n{row['company']} ({row['ticker']}): Price ${row['price']:.2f} | Revenue (B) {row['revenue_bil']} | Net margin {row['net_margin']:.3f if pd.notnull(row['net_margin']) else 'N/A'} | Div yield {row['dividend_yield_pct']}% | P/E {row['pe']}"
            ax1.text(0.01,0.99,txt, va='top', fontsize=10, family='monospace')
            pdf.savefig(fig1); plt.close(fig1)

            # Page 2: DCF table
            fig2, ax2 = plt.subplots(figsize=(8.5,11))
            ax2.axis('off')
            dtxt = "DCF 5-year results:\\n\\n"
            for d in [ko_dcf, pep_dcf]:
                if d:
                    dtxt += f"PV total: {d['pv_total']:.2f} | Intrinsic per share: {d['intrinsic_per_share']:.2f}\\n"
                else:
                    dtxt += "DCF not available for one company\\n"
            ax2.text(0.01,0.99,dtxt, va='top', fontsize=10, family='monospace')
            pdf.savefig(fig2); plt.close(fig2)

            # Page 3: Price chart
            fig3, ax3 = plt.subplots(figsize=(8.5,4))
            if data['KO']['history'] is not None:
                ax3.plot(data['KO']['history'].index, data['KO']['history']['Close'], label='KO Price')
            if data['PEP']['history'] is not None:
                ax3.plot(data['PEP']['history'].index, data['PEP']['history']['Close'], label='PEP Price')
            ax3.set_title("5-year Price History (Close)")
            ax3.legend()
            pdf.savefig(fig3); plt.close(fig3)

            # Page 4: Robustness pie if exists
            if 'sens_results' in st.session_state:
                sr = st.session_state['sens_results']
                fig4, ax4 = plt.subplots(figsize=(6,6))
                ax4.pie([sr['ko_pct'], sr['pep_pct']], labels=[f"KO {sr['ko_pct']:.1f}%", f"PEP {sr['pep_pct']:.1f}%"], startangle=140, autopct='%1.1f%%')
                ax4.set_title("Sensitivity robustness")
                pdf.savefig(fig4); plt.close(fig4)

        out_buf.seek(0)
        b64 = base64.b64encode(out_buf.read()).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="coke_pepsi_report.pdf"><button style="background-color:#1f77b4;color:white;padding:10px;border-radius:5px">⬇️ Download PDF Report</button></a>'
        st.markdown(href, unsafe_allow_html=True)
        del st.session_state['generate_pdf']  # reset flag
        st.success("PDF generated below.")

st.markdown("---")
st.caption("Notes: DCF here is a simplified template for educational purposes. Use official financial statements and a full model (including cash, debt, share count, tax, capex, working capital) for investment decisions.")


