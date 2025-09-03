# COMMAND & CONTROL (C2) ATTACKS

#What the Program Does:

# Logs all actions and resultS to the console and saves them to a background file (`c2_protection_log.txt`).
# Simulates DNS traffic monitoring: It detects and logs queries to safe or suspicious domains.
# Simulates egress filtering: It simulates allowing/blocking outgoing connections based on port number.
# Detects suspicious IP traffic: Simulates detection of network traffic to known suspicious IP addresses.
# Simulates Multi-Factor Authentication (MFA)**: It generates a random MFA code for a user, simulates user input, and logs
# whether the input is correct.

# Honeypot simulation: Simulates detecting login attempts to a honeypot and flags suspicious activity

# INSTRUCTIONS TO RUN ON REAL SYSTEMS:

# We can replace the simulation parts with real system-level commands using external libraries or by executing shell commands
# through Python's `subprocess` module.For DNS and network traffic analysis, We can integrate external tools like `scapy`
# or other packet sniffing libraries.
# For DNS and network traffic analysis, you could integrate external tools like `scapy` or other packet sniffing libraries.
# For actual egress filtering, you would need to interface with firewall systems such as `IPTables

# THIS APPLICATION WAS DESIGNED & ASSEMBLED BY RANDY SINGH From KNet Consulting


#python
import streamlit as st
import pandas as pd
import os
import time
import random
import socket
from datetime import datetime

# Log directory
LOG_DIR = "c2_protection_logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def log_action(action, result):
    """
    Log actions and results to both console and file.
    """
    log_file = os.path.join(LOG_DIR, "c2_protection_log.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ACTION: {action} | RESULT: {result}\n"
    
    # Display on console
    print(log_entry)

    # Write to log file
    with open(log_file, "a") as f:
        f.write(log_entry)

def monitor_dns_traffic():
    """
    Simulates DNS traffic monitoring.
    """
    log_action("Monitoring DNS Traffic", "Started")
    suspicious_domains = ["malicious.com", "badactor.io", "c2server.net"]

    # Simulating DNS queries
    for _ in range(5):
        time.sleep(2)
        domain = random.choice(["example.com", "google.com", "github.com"] + suspicious_domains)  # ALLOWED DOMAINS
        if domain in suspicious_domains:
            log_action(f"DNS Query Detected: {domain}", "BLOCKED (Suspicious Domain)")
        else:
            log_action(f"DNS Query Detected: {domain}", "ALLOWED (Safe Domain)")

def simulate_egress_filtering():
    """
    Simulates egress filtering based on allowed/blocked ports.
    """
    log_action("Simulating Egress Filtering", "Started")
    allowed_ports = [80, 443]  # HTTP and HTTPS ports
    blocked_ports = [8080, 12345]

    # Simulating traffic on various ports
    for _ in range(5):
        time.sleep(2)
        port = random.choice(allowed_ports + blocked_ports)
        if port in blocked_ports:
            log_action(f"Outgoing Connection on Port {port}", "BLOCKED (Unnecessary Port)")
        else:
            log_action(f"Outgoing Connection on Port {port}", "ALLOWED (Necessary Port)")

def detect_suspicious_ip_traffic():
    """
    Simulates detection of traffic to/from suspicious IPs.
    """
    log_action("Detecting Suspicious IP Traffic", "Started")
    suspicious_ips = ["192.168.1.10", "203.0.113.5", "172.16.0.8"]       # SUSPICIOUS IPS

    # Simulating network traffic
    for _ in range(5):
        time.sleep(2)
        ip = random.choice(["192.168.1.2", "8.8.8.8", "172.16.0.1"] + suspicious_ips)
        if ip in suspicious_ips:
            log_action(f"Traffic to IP {ip}", "BLOCKED (Suspicious IP)")
        else:
            log_action(f"Traffic to IP {ip}", "ALLOWED (Safe IP)")

def simulate_mfa_on_login(username):
    """
    Simulates Multi-Factor Authentication (MFA) for a user.
    """
    log_action(f"Initiating MFA for User: {username}", "Started")
    code = random.randint(100000, 999999)
    log_action(f"Generated MFA Code for {username}", f"Code: {code}")

    # Simulate user entering MFA code
    user_input = input(f"Enter MFA Code for {username}: ")
    if user_input == str(code):
        log_action(f"User {username} MFA Verification", "SUCCESS")
    else:
        log_action(f"User {username} MFA Verification", "FAILED")

def start_honeypot_simulation():
    """
    Simulates a honeypot detection for suspicious login attempts.
    """
    log_action("Starting Honeypot", "Honeypot is Active")
    
    # Simulate some connection attempts
    attempts = ["Valid User: admin", "Suspicious User: hacker", "Valid User: test"]
    for attempt in attempts:
        time.sleep(2)
        if "Suspicious" in attempt:
            log_action(f"Login Attempt Detected: {attempt}", "BLOCKED (Suspicious Activity)")
        else:
            log_action(f"Login Attempt Detected: {attempt}", "ALLOWED (Legitimate User)")

def main():
    """
    Main function to run the C2 protection measures simulation.
    """
    log_action("C2 Protection Simulation", "STARTED")

    # Step 1: Monitor DNS Traffic
    monitor_dns_traffic()

    # Step 2: Simulate Egress Filtering
    simulate_egress_filtering()

    # Step 3: Detect Suspicious IP Traffic
    detect_suspicious_ip_traffic()

    # Step 4: Simulate MFA on Login
    simulate_mfa_on_login("admin")

    # Step 5: Start Honeypot Simulation
    start_honeypot_simulation()

    log_action("C2 Protection Simulation", "COMPLETED")

if __name__ == "__main__":
    main()

