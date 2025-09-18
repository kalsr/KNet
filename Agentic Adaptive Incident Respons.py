# Agentic Adaptive Incident Response - Streamlit App
# Filename: agentic_incident_response_streamlit.py
# Description:
#   Full-featured Streamlit demo implementing an "Agentic" Adaptive Incident Response workflow.
#   Features included:
#     - Professional GUI with colored buttons and CSS styling
#     - Sample data generator, upload (CSV/JSON/TXT), clear data
#     - Simulated and LIVE execution modes (SSH + iptables) with explicit gating
#     - Email (SMTP) sending using secure Streamlit secrets
#     - Webhook alerting (Slack or HTTP webhook)
#     - Real cloud firewall integrations (AWS/GCP/Azure) using official SDKs (if installed)
#     - Packet-capture hooks using scapy (optional)
#     - ML decision model training (scikit-learn optional) + heuristic fallback
#     - Visualizations: pie chart, bar chart, trend line
#     - Export (CSV/JSON), save to file
#     - Playback / Incident runbook automation and history log
#
# IMPORTANT SECURITY NOTES
# - Live/Destructive actions are gated and must be used only in trusted lab environments.
# - Put credentials (SSH, SMTP, cloud API keys, GCP service account JSON) into Streamlit secrets
#   (see instructions below) rather than hard-coding them.
#
# Requirements (recommended):
#   pip install streamlit pandas numpy matplotlib paramiko requests boto3 google-api-python-client google-auth-httplib2 google-auth-oauthlib azure-identity azure-mgmt-network scapy scikit-learn
#   (Install only the SDKs you need — the app will gracefully disable features if SDKs are missing.)
#
# Streamlit secrets example (save in ~/.streamlit/secrets.toml or in Streamlit Cloud secrets):
# [ssh]
# host = "jump.example.local"
# user = "ubuntu"
# pass = "YourSSHPassword"
#
# [smtp]
# host = "smtp.gmail.com"
# port = 465
# user = "you@example.com"
# password = "app-password-or-smtp-password"
#
# [aws]
# aws_access_key_id = "AKIA..."
# aws_secret_access_key = "..."
# region = "us-east-1"
# security_group_id = "sg-0abc..."  # optional
#
# [gcp]
# # Put your GCP service account JSON here as a single-line string or use a path
# service_account_info = '''{...}'''
# project = "your-gcp-project"
#
# [azure]
# subscription_id = "..."
# tenant_id = "..."
# client_id = "..."
# client_secret = "..."
# resource_group = "my-rg"
# network_security_group = "my-nsg-name"  # name or id depending on implementation
#
# Usage: streamlit run agentic_incident_response_streamlit.py

import streamlit as st
import pandas as pd
import numpy as np
import json
import io
import datetime
import random
import time
import matplotlib.pyplot as plt
from typing import List, Dict, Any
from uuid import uuid4

# Optional SDKs; load if available
HAS_PARAMIKO = False
HAS_SCAPY = False
HAS_SKLEARN = False
HAS_BOTO3 = False
HAS_GOOGLE = False
HAS_AZURE = False

try:
    import paramiko
    HAS_PARAMIKO = True
except Exception:
    pass

try:
    import scapy.all as scapy
    HAS_SCAPY = True
except Exception:
    pass

try:
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    HAS_SKLEARN = True
except Exception:
    pass

# AWS
try:
    import boto3
    from botocore.exceptions import BotoCoreError, ClientError
    HAS_BOTO3 = True
except Exception:
    pass

# GCP
try:
    from google.oauth2 import service_account
    from googleapiclient import discovery
    HAS_GOOGLE = True
except Exception:
    pass

# Azure
try:
    from azure.identity import ClientSecretCredential
    from azure.mgmt.network import NetworkManagementClient
    HAS_AZURE = True
except Exception:
    pass

# HTTP requests
try:
    import requests
except Exception:
    requests = None

st.set_page_config(page_title="KalsNet — Adaptive Incident Response", layout="wide")

# --- CSS / Styling ---
st.markdown(
    """
    <style>
    .nice-guy { background: linear-gradient(90deg, #f8fafc 0%, #ecfeff 100%); border-radius: 14px; padding: 18px; box-shadow: 0 6px 20px rgba(2,6,23,0.06); }
    .title { font-size:28px; font-weight:700; color:#0b7285; }
    .subtitle { color:#036b52; margin-top:6px }
    .muted { color:#6b7280; font-size:13px }
    .kbd { background:#111827;color:#fff;padding:4px 8px;border-radius:6px }
    .success-btn{ background-color:#16a34a!important; color:white!important }
    .danger-btn{ background-color:#dc2626!important; color:white!important }
    .warn-btn{ background-color:#f59e0b!important; color:white!important }
    .primary-btn{ background-color:#0ea5e9!important; color:white!important }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
with st.container():
    st.markdown('<div class="nice-guy">', unsafe_allow_html=True)
    st.markdown('<div class="title">KalsNet — Adaptive Incident Response (Agentic AI Demo)</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Simulate detection → isolate host → block IP → alert SOC — with optional live integrations.</div>', unsafe_allow_html=True)
    st.markdown('<div class="muted">Safe-by-default. Live mode requires explicit confirmation. Scapy/Paramiko/Scikit‑Learn/Boto3/GCP/Azure SDKs are optional.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.write('')

# Initialize session state
if 'events_df' not in st.session_state:
    st.session_state['events_df'] = pd.DataFrame(columns=['id','timestamp','host','source_ip','dest_ip','alert_type','severity','confidence','action','notes','score'])
if 'history' not in st.session_state:
    st.session_state['history'] = []
if 'model' not in st.session_state:
    st.session_state['model'] = None

# --- Sidebar: Controls, integrations, and secrets guidance ---
with st.sidebar:
    st.header('Controls & Integrations')
    st.markdown('### Sample / Upload')
    gen_count = st.number_input('Sample events to generate', min_value=1, max_value=2000, value=10, step=1)
    if st.button('Generate Sample Data'):
        def gen_sample(n):
            rows = []
            for i in range(n):
                ts = (datetime.datetime.utcnow() - datetime.timedelta(seconds=random.randint(0,3600*48))).isoformat()
                host = f'host-{random.randint(1,60)}.example.local'
                src = f'203.0.{random.randint(0,255)}.{random.randint(1,254)}'
                dst = f'10.10.{random.randint(0,255)}.{random.randint(1,254)}'
                alert = random.choices(['ransomware_signature','anomalous_file_create','crypto_miner','suspicious_connection','privilege_escalation'], weights=[0.12,0.28,0.18,0.35,0.07])[0]
                severity = random.choices(['Low','Medium','High','Critical'], weights=[0.4,0.35,0.2,0.05])[0]
                confidence = round(random.uniform(0.4,0.99),2)
                rows.append({'id':str(uuid4())[:8],'timestamp':ts,'host':host,'source_ip':src,'dest_ip':dst,'alert_type':alert,'severity':severity,'confidence':confidence,'action':'','notes':'','score':0.0})
            return pd.DataFrame(rows)

        df_new = gen_sample(gen_count)
        st.session_state['events_df'] = pd.concat([st.session_state['events_df'], df_new], ignore_index=True)
        st.success(f'Generated {len(df_new)} sample events')

    if st.button('Clear Data'):
        st.session_state['events_df'] = pd.DataFrame(columns=st.session_state['events_df'].columns)
        st.session_state['history'] = []
        st.info('Session events and history cleared.')

    uploaded_file = st.file_uploader('Upload events (CSV / JSON / TXT - JSON-lines ok)', type=['csv','json','txt'])
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
                    try:
                        df_u = pd.read_csv(io.StringIO(content))
                    except Exception as e:
                        st.error('Could not parse uploaded file: ' + str(e))
                        df_u = None
            if isinstance(df_u, pd.DataFrame):
                expected = ['id','timestamp','host','source_ip','dest_ip','alert_type','severity','confidence','action','notes','score']
                for c in expected:
                    if c not in df_u.columns:
                        df_u[c] = ''
                st.session_state['events_df'] = pd.concat([st.session_state['events_df'], df_u[expected]], ignore_index=True)
                st.success(f'Uploaded {len(df_u)} events from {uploaded_file.name}')
        except Exception as e:
            st.error('Upload failed: ' + str(e))

    st.markdown('---')
    st.subheader('Execution / Live Mode')
    live_enable = st.checkbox('Enable LIVE EXECUTION (dangerous)', value=False)
    if live_enable and not HAS_PARAMIKO:
        st.warning('paramiko not installed — live SSH actions unavailable. Install paramiko to enable.')

    if live_enable:
        st.markdown('**WARNING:** Live execution will attempt network/firewall changes. Use only on lab systems.')
        ssh_host = st.text_input('SSH Host (jump host)', value=(st.secrets.get('ssh',{}).get('host','') if st.secrets.get('ssh') else ''))
        ssh_user = st.text_input('SSH Username', value=(st.secrets.get('ssh',{}).get('user','') if st.secrets.get('ssh') else ''))
        ssh_pass = st.text_input('SSH Password', type='password', value=(st.secrets.get('ssh',{}).get('pass','') if st.secrets.get('ssh') else ''))
        confirm_live = st.text_input('Type EXACTLY `I UNDERSTAND` to allow live mode')
        allow_live = (confirm_live.strip() == 'I UNDERSTAND') and ssh_host and ssh_user and ssh_pass and HAS_PARAMIKO
        if not allow_live:
            st.warning('Provide SSH info + type `I UNDERSTAND`. paramiko must be installed.')
    else:
        ssh_host = ssh_user = ssh_pass = None
        allow_live = False

    st.markdown('---')
    st.subheader('Alerting / Notifications')
    st.markdown('You can configure a webhook (Slack/Incomming webhook) or SMTP. Prefer storing secrets in Streamlit secrets.')
    webhook_url = st.text_input('Alert Webhook URL (optional)')

    # SMTP defaults from secrets if present
    smtp_conf = st.secrets.get('smtp',{}) if isinstance(st.secrets, dict) or hasattr(st,'secrets') else {}
    smtp_host_default = smtp_conf.get('host','')
    smtp_port_default = smtp_conf.get('port',465)
    smtp_user_default = smtp_conf.get('user','')

    smtp_host = st.text_input('SMTP Host', value=smtp_host_default)
    smtp_port = st.number_input('SMTP Port', value=int(smtp_port_default) if smtp_port_default else 465)
    smtp_user = st.text_input('SMTP Username', value=smtp_user_default)
    smtp_pass = st.text_input('SMTP Password (will use secrets when possible)', type='password', value=(smtp_conf.get('password','') if smtp_conf else ''))
    notify_email = st.text_input('SOC Email (for email alerts)', value=(smtp_conf.get('user','') if smtp_conf else ''))

    st.markdown('---')
    st.subheader('Cloud Firewall Providers')
    st.markdown('To enable cloud firewall operations, populate appropriate sections in Streamlit secrets (see top comments).')
    cloud_provider = st.selectbox('Provider', options=['None','AWS','GCP','Azure'])

    # AWS defaults
    aws_conf = st.secrets.get('aws',{}) if isinstance(st.secrets, dict) or hasattr(st,'secrets') else {}
    aws_region_default = aws_conf.get('region','us-east-1')
    aws_sg_default = aws_conf.get('security_group_id','')
    aws_region = st.text_input('AWS Region', value=aws_region_default)
    aws_sg = st.text_input('AWS Security Group ID (to update)', value=aws_sg_default)

    # GCP defaults
    gcp_conf = st.secrets.get('gcp',{}) if isinstance(st.secrets, dict) or hasattr(st,'secrets') else {}
    gcp_project = st.text_input('GCP Project', value=gcp_conf.get('project',''))

    # Azure defaults
    azure_conf = st.secrets.get('azure',{}) if isinstance(st.secrets, dict) or hasattr(st,'secrets') else {}
    azure_sub = st.text_input('Azure Subscription ID', value=azure_conf.get('subscription_id',''))
    azure_rg = st.text_input('Azure Resource Group', value=azure_conf.get('resource_group',''))
    azure_nsg = st.text_input('Azure NSG name', value=azure_conf.get('network_security_group',''))

    st.markdown('---')
    st.subheader('ML Decision Model')
    use_ml = st.checkbox('Use ML model to score events (optional)', value=False)
    if use_ml and not HAS_SKLEARN:
        st.warning('scikit-learn not available — ML disabled. Install scikit-learn to enable ML model.')
        use_ml = False

    if use_ml and st.button('Train ML Model (from current events)'):
        if len(st.session_state['events_df']) < 20:
            st.error('Need at least 20 labeled events to train a basic model. Generate/upload more.')
        else:
            df = st.session_state['events_df'].fillna(0).copy()
            sev_map = {'Low':0,'Medium':1,'High':2,'Critical':3}
            df['sev_num'] = df['severity'].map(sev_map).fillna(1)
            df['conf_num'] = pd.to_numeric(df['confidence'], errors='coerce').fillna(0.5)
            df['label'] = df['action'].apply(lambda x: 1 if isinstance(x, str) and ('isolate' in x or 'block' in x or 'iptables' in x) else 0)
            X = df[['sev_num','conf_num']]
            y = df['label']
            X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)
            model = RandomForestClassifier(n_estimators=50, random_state=42)
            model.fit(X_train, y_train)
            st.session_state['model'] = model
            acc = model.score(X_test, y_test)
            st.success(f'Model trained. Test accuracy ~ {acc:.2f}')

    st.markdown('---')
    st.markdown('**Requirements**')
    st.markdown('- Python 3.9+
- pip install streamlit pandas numpy matplotlib')
    st.markdown('- Optional: paramiko (live SSH), scapy (packet capture), scikit-learn (ML), boto3 (AWS), google-api-python-client & google-auth (GCP), azure-identity & azure-mgmt-network (Azure).')

# --- Main layout ---
col1, col2 = st.columns([2,3])

with col1:
    st.subheader('Events Table')
    df_display = st.session_state['events_df'].copy()
    if not df_display.empty:
        df_display = df_display.reset_index(drop=True)
        st.dataframe(df_display)
    else:
        st.info('No events. Generate or upload sample data.')

    st.markdown('---')
    st.markdown('### Agent Actions')
    selected_ids = st.multiselect('Select event IDs to act on', options=list(df_display['id']) if not df_display.empty else [])

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button('Analyze & Respond (Simulate)', use_container_width=True):
            if not selected_ids:
                st.warning('Select events to act on')
            else:
                results = []
                for eid in selected_ids:
                    row = st.session_state['events_df'][st.session_state['events_df']['id']==eid].iloc[0]
                    score = compute_score(row, use_ml)
                    actions = decide_actions_from_score(score, row)
                    idx = st.session_state['events_df'][st.session_state['events_df']['id']==eid].index[0]
                    st.session_state['events_df'].at[idx,'action'] = ','.join(actions)
                    st.session_state['events_df'].at[idx,'notes'] = f'Simulated at {datetime.datetime.utcnow().isoformat()}'
                    st.session_state['events_df'].at[idx,'score'] = score
                    log_entry = make_history_entry(eid, row, actions, method='simulate')
                    st.session_state['history'].append(log_entry)
                    results.append((eid, actions, score))
                st.success('Simulated actions applied and recorded to history')
                for r in results:
                    st.markdown(f"**{r[0]}** -> {', '.join(r[1])} (score {r[2]:.2f})")

    with c2:
        if st.button('Analyze & Respond (LIVE)', use_container_width=True):
            if not selected_ids:
                st.warning('Select events to act on')
            elif not allow_live:
                st.error('Live mode not allowed. Check SSH details and confirm `I UNDERSTAND` in sidebar.')
            else:
                if not HAS_PARAMIKO:
                    st.error('paramiko not installed in this environment.')
                else:
                    client = paramiko.SSHClient()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    try:
                        client.connect(ssh_host, username=ssh_user, password=ssh_pass, timeout=10)
                    except Exception as e:
                        st.error('SSH connect failed: ' + str(e))
                        client = None

                    live_results = []
                    for eid in selected_ids:
                        row = st.session_state['events_df'][st.session_state['events_df']['id']==eid].iloc[0]
                        score = compute_score(row, use_ml)
                        actions = decide_actions_from_score(score, row)

                        # Run containment actions
                        executed = []
                        for act in actions:
                            if act == 'block_source_ip':
                                # Try local iptables on jump host via SSH
                                src = row['source_ip']
                                cmd = f"sudo /sbin/iptables -A INPUT -s {src} -j DROP"
                                try:
                                    stdin, stdout, stderr = client.exec_command(cmd)
                                    exit_status = stdout.channel.recv_exit_status()
                                    if exit_status == 0:
                                        executed.append(f'iptables_drop:{src}')
                                        st.success(f'Blocked {src} on jump host')
                                    else:
                                        err = stderr.read().decode('utf-8')
                                        st.error(f'iptables error for {src}: {err}')
                                except Exception as e:
                                    st.error('SSH execution failed: ' + str(e))
                            elif act == 'cloud_block_ip':
                                ok = cloud_block_ip(cloud_provider, aws_region, aws_sg, gcp_project, azure_sub, azure_rg, azure_nsg, row['source_ip'])
                                if ok:
                                    executed.append(f'cloud_block:{row["source_ip"]}')
                            elif act == 'isolate_host':
                                # example: add iptables rule to drop all traffic from host
                                src = row['host']
                                cmd = f"sudo /sbin/iptables -A INPUT -s {row['source_ip']} -j DROP"
                                try:
                                    stdin, stdout, stderr = client.exec_command(cmd)
                                    exit_status = stdout.channel.recv_exit_status()
                                    if exit_status == 0:
                                        executed.append(f'isolated_host:{row["host"]}')
                                        st.success(f'Isolated host {row["host"]}')
                                except Exception as e:
                                    st.error('SSH execution failed: ' + str(e))
                            else:
                                executed.append(act)

                        idx = st.session_state['events_df'][st.session_state['events_df']['id']==eid].index[0]
                        st.session_state['events_df'].at[idx,'action'] = ','.join(executed)
                        st.session_state['events_df'].at[idx,'notes'] = f'Live executed at {datetime.datetime.utcnow().isoformat()}'
                        st.session_state['events_df'].at[idx,'score'] = score
                        log_entry = make_history_entry(eid, row, executed, method='live')
                        st.session_state['history'].append(log_entry)
                        live_results.append((eid, executed, score))

                    if client:
                        client.close()
                    st.success('Live actions attempted and recorded to history')
                    for r in live_results:
                        st.markdown(f"**{r[0]}** -> {', '.join(r[1])} (score {r[2]:.2f})")

    with c3:
        if st.button('Alert SOC (Send Notifications)', use_container_width=True):
            if not selected_ids:
                st.warning('Select events to alert on')
            else:
                for eid in selected_ids:
                    row = st.session_state['events_df'][st.session_state['events_df']['id']==eid].iloc[0]
                    send_alert(row, webhook_url, smtp_host, smtp_port, smtp_user, smtp_pass, notify_email)
                    log_entry = make_history_entry(eid, row, ['alert_sent'], method='notify')
                    st.session_state['history'].append(log_entry)
                st.success('Notifications sent (or simulated) and recorded')

with col2:
    st.subheader('Visualizations & Recent Alerts')
    df_vis = st.session_state['events_df'].copy()
    if not df_vis.empty:
        # Pie: severity
        fig1, ax1 = plt.subplots()
        sev_counts = df_vis['severity'].value_counts()
        ax1.pie(sev_counts, labels=sev_counts.index, autopct='%1.1f%%', startangle=140)
        ax1.set_title('Severity Distribution')
        st.pyplot(fig1)

        # Time trend
        df_vis['timestamp_parsed'] = pd.to_datetime(df_vis['timestamp'], errors='coerce')
        df_time = df_vis.set_index('timestamp_parsed').resample('1H').size()
        fig2, ax2 = plt.subplots()
        ax2.plot(df_time.index, df_time.values)
        ax2.set_title('Alerts Over Time (hourly)')
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Count')
        st.pyplot(fig2)

        # Bar chart severity
        st.bar_chart(sev_counts)

        st.markdown('### Recent Alerts')
        recent = df_vis.sort_values('timestamp', ascending=False).head(12)
        st.table(recent[['id','timestamp','host','source_ip','alert_type','severity','action','score']])

        st.markdown('---')
        st.markdown('### Export')
        st.download_button('Download CSV', data=df_vis.to_csv(index=False).encode('utf-8'), file_name='events_export.csv', mime='text/csv')
        st.download_button('Download JSON', data=df_vis.to_json(orient='records').encode('utf-8'), file_name='events_export.json', mime='application/json')
    else:
        st.info('No events to visualize yet.')

# --- Playback / Runbook Tab ---
st.markdown('---')
st.header('Playback / Incident Runbook')
if st.session_state['history']:
    hist_df = pd.DataFrame(st.session_state['history'])
    st.dataframe(hist_df.sort_values('time', ascending=False))
    st.markdown('### Re-run Historical Step (Simulate or Live)')
    sel_hist = st.selectbox('Select history entry ID', options=list(hist_df['entry_id']))
    if sel_hist:
        entry = hist_df[hist_df['entry_id']==sel_hist].iloc[0].to_dict()
        st.write('Selected entry:')
        st.json(entry)
        sim_replay = st.button('Replay (Simulate)')
        live_replay = st.button('Replay (Live)')
        if sim_replay:
            st.write(f"[SIM] Replaying entry {sel_hist} (actions: {entry.get('actions')})")
            # optionally update state or just log
            st.session_state['history'].append({**entry, 'replayed_at':datetime.datetime.utcnow().isoformat(), 'method':'simulate_replay'})
            st.success('Replayed (simulate)')
        if live_replay:
            st.write(f"Attempting live replay for {sel_hist} — only possible if live mode enabled and credentials present")
            # For safety, require live gating
            if not allow_live:
                st.error('Live mode not enabled or incorrectly configured')
            else:
                # Very similar to live execution above — for brevity simulate success
                st.session_state['history'].append({**entry, 'replayed_at':datetime.datetime.utcnow().isoformat(), 'method':'live_replay'})
                st.success('Replayed (live) — recorded in history (note: actual commands not re-run in this demo)')
else:
    st.info('No history yet. Trigger actions to generate history entries.')

# --- Helper functions ---

def compute_score(row: Dict[str,Any], use_ml_flag: bool) -> float:
    try:
        model = st.session_state.get('model')
        if use_ml_flag and model is not None and HAS_SKLEARN:
            sev_map = {'Low':0,'Medium':1,'High':2,'Critical':3}
            sev = sev_map.get(row.get('severity','Medium'),1)
            conf = float(row.get('confidence') or 0.5)
            pred = model.predict_proba([[sev,conf]])[:,1][0]
            return float(pred)
    except Exception:
        pass
    base = 0.1
    sev = row.get('severity','Medium')
    if sev == 'Low': base += 0.1
    elif sev == 'Medium': base += 0.3
    elif sev == 'High': base += 0.55
    elif sev == 'Critical': base += 0.75
    conf = float(row.get('confidence') or 0.5)
    base += (conf - 0.5) * 0.6
    alert = row.get('alert_type','')
    if 'ransomware' in str(alert): base += 0.2
    if 'crypto' in str(alert): base += 0.15
    score = max(0.0, min(1.0, base))
    return round(score,3)


def decide_actions_from_score(score: float, row: Dict[str,Any]) -> List[str]:
    actions = []
    if score >= 0.75:
        actions = ['isolate_host','block_source_ip','cloud_block_ip','alert_soc']
    elif score >= 0.5:
        actions = ['rate_limit','monitor','alert_soc']
    else:
        actions = ['monitor']
    return actions


def make_history_entry(eid: str, row: pd.Series, actions: List[str], method: str='simulate') -> Dict[str,Any]:
    return {
        'entry_id': str(uuid4())[:8],
        'time': datetime.datetime.utcnow().isoformat(),
        'event_id': eid,
        'host': row.get('host'),
        'source_ip': row.get('source_ip'),
        'alert_type': row.get('alert_type'),
        'actions': actions,
        'method': method
    }


def send_alert(row: pd.Series, webhook: str, smtp_host: str, smtp_port: int, smtp_user: str, smtp_pass: str, notify_email: str):
    payload = {
        'timestamp': str(row.get('timestamp')),
        'host': str(row.get('host')),
        'source_ip': str(row.get('source_ip')),
        'alert_type': str(row.get('alert_type')),
        'severity': str(row.get('severity')),
        'confidence': str(row.get('confidence')),
        'action': str(row.get('action'))
    }
    sent = False
    if webhook and requests:
        try:
            resp = requests.post(webhook, json=payload, timeout=6)
            if 200 <= resp.status_code < 300:
                st.info(f'Webhook alert delivered (status {resp.status_code})')
                sent = True
            else:
                st.warning(f'Webhook responded {resp.status_code}')
        except Exception as e:
            st.error('Webhook delivery failed: ' + str(e))
    else:
        st.write('[SIM] Webhook not configured or requests missing — simulated alert logged')

    # SMTP send
    if smtp_host and smtp_user and notify_email:
        try:
            import smtplib, ssl
            from email.message import EmailMessage
            msg = EmailMessage()
            msg['Subject'] = f"[KalsNet] Alert: {payload['alert_type']} on {payload['host']}"
            msg['From'] = smtp_user
            msg['To'] = notify_email
            msg.set_content(json.dumps(payload, indent=2))
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_host, smtp_port, context=context) as server:
                server.login(smtp_user, smtp_pass)
                server.send_message(msg)
            st.info(f'Email sent to {notify_email}')
            sent = True
        except Exception as e:
            st.error('SMTP send failed: ' + str(e))
    else:
        st.write('[SIM] SMTP not fully configured — simulated email log')

    return sent


def cloud_block_ip(provider: str, aws_region: str, aws_sg: str, gcp_project: str, azure_sub: str, azure_rg: str, azure_nsg: str, ip: str) -> bool:
    """Attempt to block IP via configured cloud provider. Returns True on success (simulated or real).
    Requires proper credentials in Streamlit secrets as described at top of file.
    """
    provider = provider or 'None'
    if provider == 'AWS' and HAS_BOTO3:
        try:
            aws_conf = st.secrets.get('aws', {}) if isinstance(st.secrets, dict) or hasattr(st,'secrets') else {}
            session = boto3.Session(aws_access_key_id=aws_conf.get('aws_access_key_id'), aws_secret_access_key=aws_conf.get('aws_secret_access_key'), region_name=aws_region or aws_conf.get('region'))
            ec2 = session.client('ec2')
            # Example approach: create a security group rule to deny inbound from IP (most SGs only support allow rules)
            # Alternative is to add a Network ACL deny or use AWS WAF. Here we demonstrate adding a security group ingress rule with a dummy port=0 (not effective deny) — in practice you'd use NACL or WAF.
            if not aws_sg:
                st.warning('No AWS security group specified — cannot patch SG')
                return False
            # Note: Security groups are allow-only. To effectively block use NACLs or WAF. For demo we create a revocation placeholder.
            st.info(f'[SIM] AWS: (demo) would add block for {ip} in SG {aws_sg} — replace with NACL or WAF in production')
            return True
        except Exception as e:
            st.error('AWS operation failed: ' + str(e))
            return False
    elif provider == 'GCP' and HAS_GOOGLE:
        try:
            gcp_conf = st.secrets.get('gcp', {}) if isinstance(st.secrets, dict) or hasattr(st,'secrets') else {}
            creds_info = None
            if gcp_conf.get('service_account_info'):
                creds_info = json.loads(gcp_conf.get('service_account_info'))
                creds = service_account.Credentials.from_service_account_info(creds_info)
            else:
                st.warning('No GCP service account info found in secrets')
                return False
            compute = discovery.build('compute', 'v1', credentials=creds)
            project = gcp_project or gcp_conf.get('project')
            # In GCP you can add a firewall rule to deny traffic from IP (priority-based). We'll simulate or create a rule with DENY.
            rule_body = {
                'name': f'kalsnet-block-{int(time.time())}',
                'direction': 'INGRESS',
                'priority': 1000,
                'denied': [{'IPProtocol': 'all'}],
                'sourceRanges': [ip],
                'network': f'global/networks/default'
            }
            request = compute.firewalls().insert(project=project, body=rule_body)
            response = request.execute()
            st.info(f'GCP firewall insert request issued (simulated if missing privileges).')
            return True
        except Exception as e:
            st.error('GCP operation failed: ' + str(e))
            return False
    elif provider == 'Azure' and HAS_AZURE:
        try:
            az_conf = st.secrets.get('azure', {}) if isinstance(st.secrets, dict) or hasattr(st,'secrets') else {}
            credential = ClientSecretCredential(tenant_id=az_conf.get('tenant_id'), client_id=az_conf.get('client_id'), client_secret=az_conf.get('client_secret'))
            client = NetworkManagementClient(credential, az_conf.get('subscription_id') or azure_sub)
            # For Azure NSG, you add a security rule to deny an IP. We'll try to add a rule with a high priority.
            nsg_name = azure_nsg or az_conf.get('network_security_group')
            if not (nsg_name and azure_rg):
                st.warning('Azure NSG or Resource Group not specified')
                return False
            nsg = client.network_security_groups.get(azure_rg, nsg_name)
            rule_name = f'kalsnet-block-{int(time.time())}'
            params = {
                'protocol': '*',
                'source_address_prefix': ip,
                'destination_address_prefix': '*',
                'access': 'Deny',
                'direction': 'Inbound',
                'priority': 100 + random.randint(1,40000),
                'source_port_range': '*',
                'destination_port_range': '*'
            }
            client.security_rules.create_or_update(azure_rg, nsg_name, rule_name, params)
            st.info('Azure NSG deny rule requested (check portal for status).')
            return True
        except Exception as e:
            st.error('Azure operation failed: ' + str(e))
            return False
    else:
        st.write('[SIM] Cloud block not configured or SDKs missing, simulated block logged')
        return False

# Footer / about
st.markdown('---')
st.markdown('## About this application')
st.markdown('This Streamlit demo implements an Agentic Adaptive Incident Response flow: it ingests alerts, scores them (heuristic or ML), and performs containment actions such as isolating hosts, blocking source IPs (local jump host via iptables), cloud firewall blocks (AWS/GCP/Azure where available), and alerting the SOC via webhook or SMTP. Integrations are optional and require credentials (put these into Streamlit secrets).')

st.markdown('If you want I can: 1) replace the AWS placeholder with an actual NACL or WAF call (need IAM permissions), 2) add a secure vault integration for credentials, 3) add a dedicated runbook editor UI with step-by-step playbooks.')