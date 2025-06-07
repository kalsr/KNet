

# NETWORK ATTACKS WITH SUMMARY OF ATTACKS
# PROGRAM DISPLAYS & SAVE NETWORK LOG FILE BEFORE ATTACK
# PROGRAM DISPLAYS & SAVE NETWORK LOG FILE AFTER ATTACK
# PROVIDES Summary of attacks

############################################ THIS SECTION IS DESIGNED BY RANDY SINGH FROM KNet Consulting#####################################

import random
import time

# List of attack types
attack_types = [
    {"name": "SQL Injection", "reason": "User input is not properly sanitized", "explanation": "An attacker injects malicious SQL code to access or modify sensitive data"},
    {"name": "Cross-Site Scripting (XSS)", "reason": "User input is not properly sanitized", "explanation": "An attacker injects malicious JavaScript code to steal user data or take control of the user's session"},
    {"name": "Cross-Site Request Forgery (CSRF)", "reason": "Lack of token-based authentication", "explanation": "An attacker tricks a user into performing an unintended action on a web application"},
    {"name": "Path Traversal", "reason": "Improper file path validation", "explanation": "An attacker accesses sensitive files or directories by manipulating file paths"},
    {"name": "Command Injection", "reason": "User input is not properly sanitized", "explanation": "An attacker injects malicious system commands to access or modify sensitive data"},
    {"name": "Remote File Inclusion (RFI)", "reason": "Improper file inclusion validation", "explanation": "An attacker includes malicious files from a remote server to access or modify sensitive data"},
    {"name": "Local File Inclusion (LFI)", "reason": "Improper file inclusion validation", "explanation": "An attacker includes malicious files from a local server to access or modify sensitive data"}
]

# List of HTTP methods
http_methods = ["GET", "POST", "PUT", "DELETE"]

# List of parameter types
parameter_types = ["URL", "Cookie", "Header", "Body"]

# Log file
log_file = "log.txt"

# Create a log file with 50 records
with open(log_file, "w") as f:
    for i in range(50):
        timestamp = int(time.time())
        http_method = random.choice(http_methods)
        parameter_type = random.choice(parameter_types)
        f.write(f"{timestamp} - {http_method} - {parameter_type} - Normal Request\n")

print("Before attack:")
with open(log_file, "r") as f:
    print(f.read())

# Simulate 10 attacks
attack_summary = {}
for i in range(10):
    # Choose a random attack type
    attack = random.choice(attack_types)
    
    # Choose a random HTTP method
    http_method = random.choice(http_methods)
    
    # Choose a random parameter type
    parameter_type = random.choice(parameter_types)
    
    # Add the attack to the log file
    with open(log_file, "a") as f:
        timestamp = int(time.time())
        f.write(f"{timestamp} - {http_method} - {parameter_type} - {attack['name']} Attack\n")
    
    # Add the attack to the summary
    if attack["name"] not in attack_summary:
        attack_summary[attack["name"]] = 1
    else:
        attack_summary[attack["name"]] += 1

print("\nAfter attack:")
with open(log_file, "r") as f:
    print(f.read())

print("\nSummary of attacks:")
for attack, count in attack_summary.items():
    print(f"{attack}: {count} occurrences")
    for a in attack_types:
        if a["name"] == attack:
            print(f"  Reason: {a['reason']}")
            print(f"  Explanation: {a['explanation']}")
            print()
