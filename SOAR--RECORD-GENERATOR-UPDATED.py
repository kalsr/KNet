# Explanation:

# Random Data Generation: Functions like `random_iso8601`, `random_severity`, `random_status`, `generate_uuid`, 
# and `random_string` generate random data using Python's built-in libraries.
# Record Generation Functions: Each function (`generate_incident`, `generate_alert`, `generate_action`, 
# `generate_playbook`, `generate_user`) creates a dictionary representing an instance of each schema.
# User Input: The script prompts the user to enter the number of records to generate for each schema.
# Generate Records: The script generates the specified number of records for each schema.
# Save to JSON: The generated records are saved to a file named `soar_output.json` in a structured format.

# This script will generate the specified number of SOAR records and save them to `soar_output.json`.

# THIS SOAR RECORDS GENERATOR IS ASSEMBLED BY RANDY SINGH DISA/EIIC/EM2 TO SUPPORT API-SECURITY PROJECT AT COIL-NA.

#python
import json
import random
import uuid
from datetime import datetime, timedelta

# Function to generate a random ISO8601 datetime string
def random_iso8601():
    now = datetime.now()
    random_date = now - timedelta(days=random.randint(0, 365))
    return random_date.isoformat()

# Function to generate a random severity level
def random_severity():
    return random.randint(1, 4)

# Function to generate a random status
def random_status(status_list):
    return random.choice(status_list)

# Function to generate a random UUID
def generate_uuid():
    return str(uuid.uuid4())

# Function to generate a random string
def random_string(length=10):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letters) for _ in range(length))

def generate_incident():
    return {
        "incident_id": generate_uuid(),
        "title": random_string(20),
        "description": random_string(100),
        "severity": random_severity(),
        "status": random_status(["open", "in progress", "resolved"]),
        "created_at": random_iso8601(),
        "updated_at": random_iso8601(),
        "resolved_at": random_iso8601() if random.choice([True, False]) else None,
        "assigned_to": generate_uuid(),
        "related_alerts": [generate_uuid() for _ in range(random.randint(1, 5))],
        "actions_taken": [generate_uuid() for _ in range(random.randint(1, 5))]
    }

def generate_alert():
    return {
        "alert_id": generate_uuid(),
        "source": random_status(["IDS", "SIEM", "Firewall"]),
        "type": random_status(["Malware", "Phishing", "DDoS"]),
        "description": random_string(100),
        "severity": random_severity(),
        "timestamp": random_iso8601(),
        "status": random_status(["new", "in progress", "closed"]),
        "related_incident": generate_uuid(),
        "enrichment_data": {
            "ip": '.'.join(str(random.randint(0, 255)) for _ in range(4)),
            "domain": random_string(8) + ".com",
            "email": random_string(5) + "@" + random_string(3) + ".com"
        }
    }

def generate_action():
    return {
        "action_id": generate_uuid(),
        "name": random_string(20),
        "description": random_string(100),
        "type": random_status(["automated", "manual"]),
        "status": random_status(["pending", "in progress", "completed"]),
        "timestamp": random_iso8601(),
        "related_incident": generate_uuid(),
        "related_alert": generate_uuid(),
        "performed_by": generate_uuid()
    }

def generate_playbook():
    return {
        "playbook_id": generate_uuid(),
        "name": random_string(20),
        "description": random_string(100),
        "steps": [
            {
                "step_id": generate_uuid(),
                "name": random_string(20),
                "description": random_string(100),
                "action": generate_uuid(),
                "order": order + 1
            } for order in range(random.randint(1, 5))
        ],
        "created_at": random_iso8601(),
        "updated_at": random_iso8601(),
        "created_by": generate_uuid(),
        "updated_by": generate_uuid()
    }

def generate_user():
    return {
        "user_id": generate_uuid(),
        "username": random_string(10),
        "full_name": random_string(15),
        "email": random_string(5) + "@" + random_string(3) + ".com",
        "role": random_status(["analyst", "admin", "incident_responder"]),
        "created_at": random_iso8601(),
        "updated_at": random_iso8601()
    }

if __name__ == "__main__":
    num_incidents = int(input("Enter the number of incidents to generate: "))
    num_alerts = int(input("Enter the number of alerts to generate: "))
    num_actions = int(input("Enter the number of actions to generate: "))
    num_playbooks = int(input("Enter the number of playbooks to generate: "))
    num_users = int(input("Enter the number of users to generate: "))

    incidents = [generate_incident() for _ in range(num_incidents)]
    alerts = [generate_alert() for _ in range(num_alerts)]
    actions = [generate_action() for _ in range(num_actions)]
    playbooks = [generate_playbook() for _ in range(num_playbooks)]
    users = [generate_user() for _ in range(num_users)]

    soar_data = {
        "incidents": incidents,
        "alerts": alerts,
        "actions": actions,
        "playbooks": playbooks,
        "users": users
    }

    with open("soar_output.json", "w") as f:
        json.dump(soar_data, f, indent=4)

    print("SOAR records have been generated and saved to soar_output.json")


