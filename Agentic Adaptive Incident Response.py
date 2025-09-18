# Agentic Adaptive Incident Response - Streamlit App
# Filename: agentic_incident_response_streamlit.py
# This file is the corrected, complete Streamlit app. Changes made to fix issues reported:
#  - Removed duplicate widget creation (no StreamlitDuplicateElementId errors).
#  - All sidebar widgets are created once and reused; unique keys used where needed.
#  - Helper functions declared before UI use to avoid NameError.
#  - Sample-data generator supports any user-specified count and appends records.
#  - Pie/bar/trend charts fixed and only rendered when data present.
#  - Robust upload/normalize logic so uploaded CSV/JSON/lines work.
#  - History/runbook logging kept and replay options preserved.
#
# Requirements (minimum):
#   pip install streamlit pandas numpy matplotlib requests
# Optional extras for live/cloud/packet/ML:
#   pip install paramiko scapy scikit-learn boto3 google-api-python-client google-auth azure-identity azure-mgmt-network
#
# Streamlit secrets (recommended for live/cloud/SMTP): ~/.streamlit/secrets.toml


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import io
import datetime
import random
import time
from uuid import uuid4
from typing import Dict, Any, List

# Optional libs
try:
    import requests
except Exception:
    requests = None

try:
    import paramiko
    HAS_PARAMIKO = True
except Exception:
    HAS_PARAMIKO = False

try:
    import scapy.all as scapy
    HAS_SCAPY = True
except Exception:
    HAS_SCAPY = False

try:
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    HAS_SKLEARN = True
except Exception:
    HAS_SKLEARN = False

try:
    import boto3
    HAS_BOTO3 = True
except Exception:
    HAS_BOTO3 = False

try:
    from google.oauth2 import service_account
    from googleapiclient import discovery
    HAS_GOOGLE = True
except Exception:
    HAS_GOOGLE = False

try:
    from azure.identity import ClientSecretCredential
    from azure.mgmt.network import NetworkManagementClient
    HAS_AZURE = True
except Exception:
    HAS_AZURE = False

# ---------------- Helper functions (declare before UI) ----------------

def normalize_events_df(df: pd.DataFrame) -> pd.DataFrame:
    """Ensure dataframe has required columns and types."""
    expected = ['id','timestamp','intrusion_type','severity','ip','details','action','notes','score']
    for c in expected:
        if c not in df.columns:
            df[c] = ''
    # ensure timestamp format
    if not pd.api.types.is_datetime64_any_dtype(df['timestamp']):
        try:
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        except Exception:
            df['timestamp'] = pd.to_datetime(df['timestamp'].astype(str), errors='coerce')
    return df[expected]


def compute_score(event: Dict[str, Any], use_ml: bool = False, model=None) -> float:
    """Return score between 0.0 and 1.0. Heuristic fallback if ML not used or available."""
    try:
        sev = str(event.get('severity','medium')).lower()
        base = 0.1
        if sev == 'low': base += 0.15
        elif sev == 'medium': base += 0.35
        elif sev == 'high': base += 0.6
        elif sev == 'critical': base += 0.85
        # increase for ransomware/crypto
        itype = str(event.get('intrusion_type','')).lower()
        if 'ransom' in itype: base += 0.15
        if 'crypto' in itype or 'miner' in itype: base += 0.12
        # confidence field if exists
        conf = float(event.get('confidence', 0.6)) if event.get('confidence') not in (None, '') else 0.6
        base += (conf - 0.5) * 0.4
        score = max(0.0, min(1.0, base))
        # ML override
        if use_ml and model is not None and HAS_SKLEARN:
            try:
                sev_map = {'low':0,'medium':1,'high':2,'critical':3}
                x = [[sev_map.get(sev,1), conf]]
                pred = float(model.predict_proba(x)[:,1][0])
                return pred
            except Exception:
                pass
        return round(score,3)
    except Exception:
        return 0.0


def send_alert(event: Dict[str,Any], webhook_url: str = None, smtp_conf: Dict[str,Any] = None, notify_email: str = '') -> bool:
    """Send alert via webhook and/or SMTP (if configured). Returns True if any send succeeded."""
    payload = {
        'timestamp': str(event.get('timestamp')),
        'host': event.get('host',''),
        'ip': event.get('ip',''),
        'intrusion_type': event.get('intrusion_type',''),
        'severity': event.get('severity',''),
        'details': event.get('details',''),
        'action': event.get('action','')
    }
    sent_any = False
    # Webhook
    if webhook_url and requests:
        try:
            r = requests.post(webhook_url, json=payload, timeout=6)
            if 200 <= r.status_code < 300:
                st.info(f'Webhook delivered (status {r.status_code})')
                sent_any = True
            else:
                st.warning(f'Webhook responded {r.status_code}')
        except Exception as e:
            st.error(f'Webhook send failed: {e}')
    elif webhook_url and not requests:
        st.warning('requests not installed; cannot send webhook')

    # SMTP
    try:
        if smtp_conf and smtp_conf.get('host') and smtp_conf.get('user') and smtp_conf.get('password') and notify_email:
            import smtplib, ssl
            from email.message import EmailMessage
            msg = EmailMessage()
            msg['Subject'] = f"[KalsNet] Alert: {payload['intrusion_type']}"
            msg['From'] = smtp_conf.get('user')
            msg['To'] = notify_email
            msg.set_content(json.dumps(payload, indent=2))
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_conf.get('host'), int(smtp_conf.get('port',465)), context=context) as s:
                s.login(smtp_conf.get('user'), smtp_conf.get('password'))
                s.send_message(msg)
            st.info(f'Email sent to {notify_email}')
            sent_any = True
    except Exception as e:
        st.error('SMTP send failed: ' + str(e))

    return sent_any


def cloud_block_ip(provider: str, project: str, aws_region: str, aws_sg: str, gcp_conf: Dict[str,Any], azure_conf: Dict[str,Any], ip: str) -> bool:
    """Attempt cloud block via available SDKs. Returns True on simulated or successful attempt."""
    if not provider or provider == 'None':
        st.info('[SIM] No cloud provider configured — skipping cloud block')
        return False
    provider = provider.upper()
    try:
        if provider == 'AWS':
            if not HAS_BOTO3:
                st.warning('boto3 not installed; cannot perform AWS actions')
                return False
            aws_secrets = st.secrets.get('aws', {}) if hasattr(st, 'secrets') else {}
            # NOTE: security groups are allow-only. Real blocking should use NACLs or WAF.
            st.info(f'[SIM] AWS block placeholder for {ip} in region {aws_region} and SG {aws_sg} — implement NACL/WAF in prod')
            return True
        elif provider == 'GCP':
            if not HAS_GOOGLE:
                st.warning('google sdk not installed; cannot perform GCP actions')
                return False
            st.info(f'[SIM] GCP firewall insert placeholder for {ip} in project {project}')
            return True
        elif provider == 'AZURE':
            if not HAS_AZURE:
                st.warning('azure sdk not installed; cannot perform Azure actions')
                return False
            st.info(f'[SIM] Azure NSG deny placeholder for {ip} in resource group {azure_conf.get("resource_group") if azure_conf else ""}')
            return True
        else:
            st.warning('Unknown provider: ' + provider)
            return False
    except Exception as e:
        st.error('Cloud block failed: ' + str(e))
        return False

# ---------------- End helpers ----------------

st.set_page_config(page_title='KalsNet(KNet) — Adaptive Incident Response', layout='wide')

# CSS
st.markdown("""
    <style>
    .card { background: linear-gradient(90deg,#f8fafc 0%,#ecfeff 100%); padding:14px; border-radius:12px; box-shadow:0 6px 18px rgba(2,6,23,0.06); }
    .title { font-size:26px; font-weight:700; color:#0b7285 }
    .muted { color:#64748b; }
    </style>
""", unsafe_allow_html=True)

# Header
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title">KalsNet (KNet) Designed — Adaptive Incident Response Use-Case.', unsafe_allow_html=True)
    st.markdown('<div class="muted">Safe-by-default demo. Use live/cloud features only with proper credentials in Streamlit secrets.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Initialize session state
if 'events' not in st.session_state:
    st.session_state['events'] = pd.DataFrame()
if 'history' not in st.session_state:
    st.session_state['history'] = []
if 'model' not in st.session_state:
    st.session_state['model'] = None

# ---------------- Sidebar widgets (created ONCE) ----------------
with st.sidebar:
    st.header('Controls & Integrations')
    gen_count = st.number_input('Sample events to generate', min_value=1, max_value=1000, value=100, step=1, key='gen_count')
    generate_btn = st.button('Generate Sample Data', key='generate_btn')
    clear_btn = st.button('Clear Data', key='clear_btn')
    uploaded_file = st.file_uploader('Upload events (CSV / JSON / TXT - JSON-lines ok)', type=['csv','json','txt'], key='upload')

    st.markdown('---')
    st.subheader('Execution / Live Mode')
    live_enable = st.checkbox('Enable LIVE EXECUTION (dangerous)', value=False, key='live_enable')
    ssh_host = st.text_input('SSH Host (jump host)', value=(st.secrets.get('ssh',{}).get('host','') if hasattr(st,'secrets') and st.secrets.get('ssh') else ''), key='ssh_host')
    ssh_user = st.text_input('SSH Username', value=(st.secrets.get('ssh',{}).get('user','') if hasattr(st,'secrets') and st.secrets.get('ssh') else ''), key='ssh_user')
    ssh_pass = st.text_input('SSH Password', type='password', value=(st.secrets.get('ssh',{}).get('pass','') if hasattr(st,'secrets') and st.secrets.get('ssh') else ''), key='ssh_pass')
    confirm_live = st.text_input('Type EXACTLY `I UNDERSTAND` to allow live mode', key='confirm_live')
    allow_live = (confirm_live.strip() == 'I UNDERSTAND') and ssh_host and ssh_user and ssh_pass and HAS_PARAMIKO

    st.markdown('---')
    st.subheader('Alerting / Notifications')
    webhook_url = st.text_input('Alert Webhook URL (optional)', value=(st.secrets.get('webhook',{}).get('url','') if hasattr(st,'secrets') and st.secrets.get('webhook') else ''), key='webhook_url')
    smtp_conf = st.secrets.get('smtp', {}) if hasattr(st,'secrets') else {}
    smtp_host = st.text_input('SMTP Host', value=smtp_conf.get('host',''), key='smtp_host')
    smtp_port = st.number_input('SMTP Port', value=int(smtp_conf.get('port',465) if smtp_conf else 465), key='smtp_port')
    smtp_user = st.text_input('SMTP Username', value=smtp_conf.get('user',''), key='smtp_user')
    smtp_pass = st.text_input('SMTP Password', type='password', value=smtp_conf.get('password',''), key='smtp_pass')
    notify_email = st.text_input('SOC Email (for email alerts)', value=smtp_conf.get('user',''), key='notify_email')

    st.markdown('---')
    st.subheader('Cloud Firewall (Simulated/SDK)')
    cloud_provider = st.selectbox('Provider', options=['None','AWS','GCP','Azure'], key='cloud_provider')
    aws_region = st.text_input('AWS Region', value=(st.secrets.get('aws',{}).get('region','us-east-1') if hasattr(st,'secrets') and st.secrets.get('aws') else 'us-east-1'), key='aws_region')
    aws_sg = st.text_input('AWS Security Group ID (for demo)', value=(st.secrets.get('aws',{}).get('security_group_id','') if hasattr(st,'secrets') and st.secrets.get('aws') else ''), key='aws_sg')
    gcp_project = st.text_input('GCP Project', value=(st.secrets.get('gcp',{}).get('project','') if hasattr(st,'secrets') and st.secrets.get('gcp') else ''), key='gcp_project')
    azure_rg = st.text_input('Azure Resource Group', value=(st.secrets.get('azure',{}).get('resource_group','') if hasattr(st,'secrets') and st.secrets.get('azure') else ''), key='azure_rg')
    azure_nsg = st.text_input('Azure NSG name', value=(st.secrets.get('azure',{}).get('network_security_group','') if hasattr(st,'secrets') and st.secrets.get('azure') else ''), key='azure_nsg')

    st.markdown('---')
    st.subheader('ML Decision Model')
    use_ml = st.checkbox('Use ML model to score events (optional)', value=False, key='use_ml')
    train_ml_btn = st.button('Train ML Model (from current events)', key='train_ml')

# ---------------- Sidebar actions handling ----------------
if generate_btn:
    # generate sample data and append
    n = int(st.session_state['gen_count'])
    types = ['ransomware','anomalous_file_create','crypto_miner','suspicious_connection','privilege_escalation']
    severities = ['low','medium','high','critical']
    rows = []
    for _ in range(n):
        rows.append({
            'id': str(uuid4())[:8],
            'timestamp': datetime.datetime.utcnow().isoformat(),
            'intrusion_type': random.choice(types),
            'severity': random.choices(severities, weights=[0.4,0.35,0.2,0.05])[0],
            'ip': f'203.0.{random.randint(0,255)}.{random.randint(1,254)}',
            'details': 'Simulated event',
            'action': '',
            'notes': '',
            'score': 0.0
        })
    df_new = pd.DataFrame(rows)
    if st.session_state['events'].empty:
        st.session_state['events'] = normalize_events_df(df_new)
    else:
        st.session_state['events'] = pd.concat([st.session_state['events'], normalize_events_df(df_new)], ignore_index=True)
    st.success(f'Generated and appended {len(df_new)} events')

if clear_btn:
    st.session_state['events'] = pd.DataFrame()
    st.session_state['history'] = []
    st.success('Cleared events and history')

if uploaded_file is not None:
    try:
        fname = uploaded_file.name.lower()
        if fname.endswith('.csv'):
            df_u = pd.read_csv(uploaded_file)
        elif fname.endswith('.json'):
            df_u = pd.read_json(uploaded_file)
        else:
            content = uploaded_file.getvalue().decode('utf-8')
            try:
                df_u = pd.read_json(io.StringIO(content), lines=True)
            except Exception:
                df_u = pd.read_csv(io.StringIO(content))
        df_u = normalize_events_df(df_u)
        if st.session_state['events'].empty:
            st.session_state['events'] = df_u
        else:
            st.session_state['events'] = pd.concat([st.session_state['events'], df_u], ignore_index=True)
        st.success(f'Uploaded {len(df_u)} events from {uploaded_file.name}')
    except Exception as e:
        st.error('Upload failed: ' + str(e))

# Train ML if requested
if train_ml_btn:
    if len(st.session_state['events']) < 20:
        st.warning('Need at least 20 events to train an ML model. Generate more or upload labeled events.')
    elif not HAS_SKLEARN:
        st.warning('scikit-learn not installed in this environment. Install scikit-learn to enable ML training.')
    else:
        df = st.session_state['events'].copy()
        df['sev_num'] = df['severity'].map({'low':0,'medium':1,'high':2,'critical':3}).fillna(1)
        df['conf_num'] = pd.to_numeric(df.get('confidence', pd.Series([0.6]*len(df))), errors='coerce').fillna(0.6)
        df['label'] = df['action'].apply(lambda x: 1 if isinstance(x, str) and ('isolate' in x or 'block' in x) else 0)
        X = df[['sev_num','conf_num']]
        y = df['label']
        try:
            X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)
            model = RandomForestClassifier(n_estimators=50, random_state=42)
            model.fit(X_train, y_train)
            acc = model.score(X_test, y_test)
            st.session_state['model'] = model
            st.success(f'ML model trained (test acc ~ {acc:.2f})')
        except Exception as e:
            st.error('ML training failed: ' + str(e))

# ---------------- Main layout ----------------
col1, col2 = st.columns([2,3])

with col1:
    st.subheader('Events')
    df = st.session_state['events']
    if not df.empty:
        st.dataframe(df.sort_values('timestamp', ascending=False).reset_index(drop=True))
    else:
        st.info('No events. Generate sample data or upload a file.')

    st.markdown('---')
    st.markdown('### Agent Actions')
    selected = []
    if not df.empty:
        selected = st.multiselect('Select event IDs', options=list(df['id']), key='select_events')

    act_col1, act_col2, act_col3 = st.columns(3)
    with act_col1:
        if st.button('Analyze & Respond (Simulate)', key='simulate_btn'):
            if not selected:
                st.warning('Select events to act on')
            else:
                for eid in selected:
                    row = df[df['id']==eid].iloc[0].to_dict()
                    score = compute_score(row, use_ml=st.session_state.get('use_ml', False), model=st.session_state.get('model'))
                    actions = []
                    if score >= 0.75:
                        actions = ['isolate_host','block_source_ip','alert_soc']
                    elif score >= 0.5:
                        actions = ['monitor','alert_soc']
                    else:
                        actions = ['monitor']
                    idx = st.session_state['events'][st.session_state['events']['id']==eid].index[0]
                    st.session_state['events'].at[idx,'action'] = ','.join(actions)
                    st.session_state['events'].at[idx,'score'] = score
                    st.session_state['events'].at[idx,'notes'] = f'Simulated at {datetime.datetime.utcnow().isoformat()}'
                    st.session_state['history'].append({'entry_id':str(uuid4())[:8],'time':datetime.datetime.utcnow().isoformat(),'event_id':eid,'actions':actions,'method':'simulate'})
                st.success('Simulated actions applied')

    with act_col2:
        if st.button('Analyze & Respond (LIVE)', key='live_btn'):
            if not selected:
                st.warning('Select events to act on')
            elif not allow_live:
                st.error('Live mode not allowed or not configured. Check SSH + confirmation in sidebar.')
            else:
                if not HAS_PARAMIKO:
                    st.error('paramiko not installed; cannot perform SSH live actions')
                else:
                    try:
                        client = paramiko.SSHClient()
                        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        client.connect(ssh_host, username=ssh_user, password=ssh_pass, timeout=10)
                    except Exception as e:
                        st.error('SSH connect failed: ' + str(e))
                        client = None
                    for eid in selected:
                        row = df[df['id']==eid].iloc[0].to_dict()
                        score = compute_score(row, use_ml=st.session_state.get('use_ml', False), model=st.session_state.get('model'))
                        actions = []
                        if score >= 0.75:
                            actions = ['isolate_host','block_source_ip','cloud_block_ip','alert_soc']
                        elif score >= 0.5:
                            actions = ['monitor','alert_soc']
                        else:
                            actions = ['monitor']

                        executed = []
                        for a in actions:
                            if a == 'block_source_ip' and client is not None:
                                cmd = f"sudo /sbin/iptables -A INPUT -s {row.get('ip')} -j DROP"
                                try:
                                    stdin, stdout, stderr = client.exec_command(cmd)
                                    exit_status = stdout.channel.recv_exit_status()
                                    if exit_status == 0:
                                        executed.append(f'iptables_drop:{row.get("ip")}')
                                        st.success(f'Blocked {row.get("ip")} via iptables on jump host')
                                    else:
                                        err = stderr.read().decode('utf-8')
                                        st.error(f'iptables error: {err}')
                                except Exception as e:
                                    st.error('SSH cmd failed: ' + str(e))
                            elif a == 'cloud_block_ip':
                                ok = cloud_block_ip(cloud_provider, gcp_project, aws_region, aws_sg, {}, {'resource_group':azure_rg, 'nsg':azure_nsg}, row.get('ip'))
                                if ok:
                                    executed.append(f'cloud_block:{row.get("ip")}')
                            else:
                                executed.append(a)

                        idx = st.session_state['events'][st.session_state['events']['id']==eid].index[0]
                        st.session_state['events'].at[idx,'action'] = ','.join(executed)
                        st.session_state['events'].at[idx,'notes'] = f'Live executed at {datetime.datetime.utcnow().isoformat()}'
                        st.session_state['history'].append({'entry_id':str(uuid4())[:8],'time':datetime.datetime.utcnow().isoformat(),'event_id':eid,'actions':executed,'method':'live'})
                    if client:
                        client.close()
                    st.success('Live attempt finished — see logs above')

    with act_col3:
        if st.button('Alert SOC (Send Notifications)', key='alert_btn'):
            if not selected:
                st.warning('Select events to alert on')
            else:
                smtp_conf_local = {'host': smtp_host, 'port': smtp_port, 'user': smtp_user, 'password': smtp_pass}
                for eid in selected:
                    row = df[df['id']==eid].iloc[0].to_dict()
                    send_alert(row, webhook_url=webhook_url, smtp_conf=smtp_conf_local, notify_email=notify_email)
                    st.session_state['history'].append({'entry_id':str(uuid4())[:8],'time':datetime.datetime.utcnow().isoformat(),'event_id':eid,'actions':['alert_sent'],'method':'notify'})
                st.success('Notifications sent (or simulated)')

with col2:
    st.subheader('Visualizations & Recent Alerts')
    df_vis = st.session_state['events'].copy()
    if not df_vis.empty:
        # ensure timestamp parsed
        df_vis['timestamp_parsed'] = pd.to_datetime(df_vis['timestamp'], errors='coerce')
        # Pie: intrusion type
        type_counts = df_vis['intrusion_type'].value_counts()
        fig1, ax1 = plt.subplots()
        ax1.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
        ax1.set_title('Incident Types')
        st.pyplot(fig1)

        # Time trend
        df_time = df_vis.set_index('timestamp_parsed').resample('1H').size()
        fig2, ax2 = plt.subplots()
        ax2.plot(df_time.index, df_time.values)
        ax2.set_title('Alerts Over Time (hourly)')
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Count')
        st.pyplot(fig2)

        # Bar chart severity
        severity_counts = df_vis['severity'].value_counts()
        fig3, ax3 = plt.subplots()
        ax3.bar(severity_counts.index, severity_counts.values)
        ax3.set_title('Severity Counts')
        st.pyplot(fig3)

        st.markdown('### Recent Alerts')
        recent = df_vis.sort_values('timestamp', ascending=False).head(12)
        st.table(recent[['id','timestamp','intrusion_type','severity','ip','action','score']])

        st.markdown('---')
        st.markdown('### Export')
        st.download_button('Download CSV', data=df_vis.to_csv(index=False).encode('utf-8'), file_name='events_export.csv', mime='text/csv')
        st.download_button('Download JSON', data=df_vis.to_json(orient='records').encode('utf-8'), file_name='events_export.json', mime='application/json')
    else:
        st.info('No events to visualize yet.')

# ---------------- Playback / Runbook ----------------
st.markdown('---')
st.header('Playback / Incident Runbook')
if st.session_state['history']:
    hist_df = pd.DataFrame(st.session_state['history'])
    st.dataframe(hist_df.sort_values('time', ascending=False))
    sel_entry = st.selectbox('Select history entry', options=list(hist_df['entry_id']), key='sel_history')
    if sel_entry:
        entry = hist_df[hist_df['entry_id']==sel_entry].iloc[0].to_dict()
        st.json(entry)
        if st.button('Replay (Simulate)', key='replay_sim'):
            st.session_state['history'].append({**entry, 'replayed_at': datetime.datetime.utcnow().isoformat(), 'method':'simulate_replay'})
            st.success('Replayed (simulate)')
        if st.button('Replay (Live)', key='replay_live'):
            if not allow_live:
                st.error('Live mode not enabled or not properly configured')
            else:
                st.session_state['history'].append({**entry, 'replayed_at': datetime.datetime.utcnow().isoformat(), 'method':'live_replay'})
                st.success('Recorded replay attempt (live)')
else:
    st.info('No history yet. Trigger actions to generate history entries.')

# Footer
st.markdown('---')
st.markdown('**Notes:** This application was designed by Randy Singh from KNet Consulting Group. This app avoids duplicate Streamlit widget IDs by creating sidebar inputs only once and giving keys where needed. Sample-data generation now supports large user-specified counts and appends to existing data. Charts render only when data exists.')


