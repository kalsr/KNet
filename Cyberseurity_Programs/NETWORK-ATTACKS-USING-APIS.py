

# NETWORK-ATTACKS USING APIS
# THIS SECTION OF PLAY-BOOK ADDRESS API-ATTACKS ON THE NETWORK.
#IT DETECTS "List of attack types" SUCH AS SQL Injection, Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), Path Traversal, Command Injection, Remote File Inclusion (RFI), Local File Inclusion (LFI) ETC.
# PROGRAM DISPLAYS AN API-LOG-FILE BEFORE & AFTER ATTACK
# THE PROGRAM ALSO PROVIDES A SUMMARY OF ATTACKS WITH EXPLANATION OF EACH ATTACK.


############### THIS SECTION OF PLAY-BOOK IS DESIGNED & ASSEMBLED BY RSANDY SINGH FROM KNet Consulting#######################



import random
import time
import json

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

# List of API endpoints
endpoints = [
    "/users",
    "/products",
    "/orders",
    "/payments"
]

# List of HTTP methods
methods = ["GET", "POST", "PUT", "DELETE"]

# List of request bodies
request_bodies = [
    {"name": "John Doe", "email": "john@example.com"},
    {"product_name": "Widget", "price": 19.99},
    {"order_id": 123, "status": "shipped"},
    {"payment_method": "credit_card", "amount": 100.00}
]

# List of response formats
response_formats = ["JSON", "XML", "CSV"]

# Log file
log_file = "api_log.txt"
result_file = "result_after_attack.txt"

# Create a log file with 50 records
with open(log_file, "w") as f:
    for i in range(50):
        timestamp = int(time.time())
        endpoint = random.choice(endpoints)
        method = random.choice(methods)
        request_body = random.choice(request_bodies)
        response_format = random.choice(response_formats)
        f.write(f"{timestamp} - {method} - {endpoint} - Request Body: {json.dumps(request_body)} - Response Format: {response_format}\n")

print("Before attack:")
with open(log_file, "r") as f:
    print(f.read())

# Simulate 10 attacks
attack_summary = {}
for i in range(10):
    # Choose a random attack type
    attack = random.choice(attack_types)
    
    # Choose a random API endpoint
    endpoint = random.choice(endpoints)
    
    # Choose a random HTTP method
    method = random.choice(methods)
    
    # Choose a random request body
    request_body = random.choice(request_bodies)
    
    # Choose a random response format
    response_format = random.choice(response_formats)
    
    # Add the attack to the log file
    with open(log_file, "a") as f:
        timestamp = int(time.time())
        f.write(f"{timestamp} - {method} - {endpoint} - Request Body: {json.dumps(request_body)} - Response Format: {response_format} - {attack['name']} Attack\n")
    
    # Add the attack to the summary
    if attack["name"] not in attack_summary:
        attack_summary[attack["name"]] = 1
    else:
        attack_summary[attack["name"]] += 1

print("\nAfter attack:")
with open(log_file, "r") as f:
    print(f.read())

# Save the result file after attack
with open(result_file, "w") as f:
    f.write("After attack:\n")
    f.write("===============\n")
    with open(log_file, "r") as lf:
        f.write(lf.read())

print("\nSummary of attacks:")
for attack, count in attack_summary.items():
    print(f"{attack}: {count} occurrences")
    for a in attack_types:
        if a["name"] == attack:
            print(f"  Reason: {a['reason']}")
            print(f"  Explanation: {a['explanation']}")
            print()
