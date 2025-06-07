#UPDATED F5/NETSCOUT/PCAPS
# Program will emulate Emass, DITPR, MAPS & ESPS records based on their Schemas
# This program will have explanations for why a record is considered malicious or non-malicious. 
# Each record now includes a detailed reason explaining its status.
# THIS PROGRAM IS DESIGNED AND ASSEMBLED BY RANDY SINGH KNet Consulting TO 
# SUPPORT DISA MISSIONS ON DISCOVERING & SECURING API'S

#python
import json
import random
import os

def prompt_user(prompt, input_type=str):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print("Invalid input. Please try again.")

def generate_record(record_type):
    base_record = {
        "record_type": record_type,
        "timestamp": random.randint(1609459200, 1672444800),  # Random timestamp for 2021-2023
        "source_ip": f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}",
        "destination_ip": f"10.0.{random.randint(0, 255)}.{random.randint(0, 255)}",
        "data_volume": round(random.uniform(0.1, 100.0), 2)
    }

    if random.choice([True, False]):
        base_record["api_status"] = "malicious"
        base_record["reason"] = random.choice([
            "SQL Injection attempt detected: The request includes SQL keywords indicating an attempt to manipulate the database.",
            "Cross-Site Scripting (XSS) attack detected: The request contains script tags that could be used to execute malicious code.",
            "Unauthorized access attempt detected: The request attempts to access restricted endpoints or use invalid credentials.",
            "API abuse detected with high frequency requests: There is an unusually high number of requests from a single IP or user.",
            "Suspicious data exfiltration detected: Large amounts of data are being accessed or transferred unusually.",
            "Bot-like behavior detected: The pattern of requests suggests automated actions typical of bot attacks."
        ])
    else:
        base_record["api_status"] = "non-malicious"
        base_record["reason"] = "Legitimate API usage: The request patterns and data access are consistent with normal, authorized use."

    # Add specific fields for each record type
    if record_type == "EMASS":
        base_record.update({
            "compliance_status": random.choice(["compliant", "non-compliant"]),
            "system_owner": f"owner_{random.randint(1, 1000)}"
        })
    elif record_type == "DITPR":
        base_record.update({
            "project_id": f"PID{random.randint(1000, 9999)}",
            "project_name": f"Project_{random.randint(1, 100)}"
        })
    elif record_type == "MAPS":
        base_record.update({
            "map_id": f"MAP{random.randint(100, 999)}",
            "map_description": f"Description_{random.randint(1, 100)}"
        })
    elif record_type == "ESPS":
        base_record.update({
            "esps_id": f"ESPS{random.randint(1000, 9999)}",
            "security_level": random.choice(["high", "medium", "low"])
        })

    return base_record

def save_records_to_file(records, filename):
    with open(filename, 'w') as f:
        for record in records:
            json.dump(record, f, indent=4)
            f.write("\n\n")  # Adding a line gap between records
    print(f"Records saved to {filename}")

def load_records_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    else:
        return []

def main():
    while True:
        print("\nEmulate Records")
        print("1. Generate EMASS Records")
        print("2. Generate DITPR Records")
        print("3. Generate MAPS Records")
        print("4. Generate ESPS Records")
        print("5. Display and Separate Malicious/Non-Malicious Records")
        print("6. Exit")

        choice = prompt_user("Enter your choice: ", int)

        if choice in [1, 2, 3, 4]:
            num_records = prompt_user("Enter number of records to generate: ", int)
            record_type = ""
            filename = ""
            if choice == 1:
                record_type = "EMASS"
                filename = "EMASS-output.json"
            elif choice == 2:
                record_type = "DITPR"
                filename = "DITPR-output.json"
            elif choice == 3:
                record_type = "MAPS"
                filename = "MAPS-output.json"
            elif choice == 4:
                record_type = "ESPS"
                filename = "ESPS-output.json"
            
            records = [generate_record(record_type) for _ in range(num_records)]
            save_records_to_file(records, filename)

        elif choice == 5:
            for record_type, filename in [("EMASS", "EMASS-output.json"), ("DITPR", "DITPR-output.json"), ("MAPS", "MAPS-output.json"), ("ESPS", "ESPS-output.json")]:
                records = load_records_from_file(filename)
                malicious_records = [record for record in records if record["api_status"] == "malicious"]
                non_malicious_records = [record for record in records if record["api_status"] == "non-malicious"]
                save_records_to_file(malicious_records, f"{record_type}-malicious-APIs.json")
                save_records_to_file(non_malicious_records, f"{record_type}-non-malicious-APIs.json")
                print(f"{record_type} Records:")
                print(f"  Malicious records: {len(malicious_records)}")
                print(f"  Non-malicious records: {len(non_malicious_records)}")

        elif choice == 6:
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
