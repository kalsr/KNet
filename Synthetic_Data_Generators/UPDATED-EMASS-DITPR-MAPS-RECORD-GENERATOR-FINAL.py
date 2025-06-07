
# UPDATED-EMASS-DITPR-MAPS-RECORD-GENERATOR-FINA

# Here is the complete corrected code:

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
            content = f.read()
            records = [json.loads(line) for line in content.split('\n\n') if line]
            return records
    else:
        return []

def display_records(records):
    for record in records:
        print(json.dumps(record, indent=4))
        print("\n")

def main():
    emass_records = load_records_from_file("EMASS-output.json")
    ditpr_records = load_records_from_file("DITPR-output.json")
    maps_records = load_records_from_file("MAPS-output.json")
    esps_records = load_records_from_file("ESPS-output.json")

    while True:
        print("\nEmulate Records")
        print("1. Generate EMASS Records")
        print("2. Generate DITPR Records")
        print("3. Generate MAPS Records")
        print("4. Generate ESPS Records")
        print("5. Display EMASS Records")
        print("6. Display DITPR Records")
        print("7. Display MAPS Records")
        print("8. Display ESPS Records")
        print("9. Exit")

        choice = prompt_user("Enter your choice: ", int)

        if choice == 1:
            num_records = prompt_user("Enter number of records to generate: ", int)
            new_emass_records = [generate_record("EMASS") for _ in range(num_records)]
            emass_records.extend(new_emass_records)
            save_records_to_file(emass_records, "EMASS-output.json")
            print("EMASS Records:")
            display_records(emass_records)

        elif choice == 2:
            num_records = prompt_user("Enter number of records to generate: ", int)
            new_ditpr_records = [generate_record("DITPR") for _ in range(num_records)]
            ditpr_records.extend(new_ditpr_records)
            save_records_to_file(ditpr_records, "DITPR-output.json")
            print("DITPR Records:")
            display_records(ditpr_records)

        elif choice == 3:
            num_records = prompt_user("Enter number of records to generate: ", int)
            new_maps_records = [generate_record("MAPS") for _ in range(num_records)]
            maps_records.extend(new_maps_records)
            save_records_to_file(maps_records, "MAPS-output.json")
            print("MAPS Records:")
            display_records(maps_records)

        elif choice == 4:
            num_records = prompt_user("Enter number of records to generate: ", int)
            new_esps_records = [generate_record("ESPS") for _ in range(num_records)]
            esps_records.extend(new_esps_records)
            save_records_to_file(esps_records, "ESPS-output.json")
            print("ESPS Records:")
            display_records(esps_records)

        elif choice == 5:
            if emass_records:
                print("EMASS Records:")
                display_records(emass_records)
            else:
                print("No EMASS records generated.")

        elif choice == 6:
            if ditpr_records:
                print("DITPR Records:")
                display_records(ditpr_records)
            else:
                print("No DITPR records generated.")

        elif choice == 7:
            if maps_records:
                print("MAPS Records:")
                display_records(maps_records)
            else:
                print("No MAPS records generated.")

        elif choice == 8:
            if esps_records:
                print("ESPS Records:")
                display_records(esps_records)
            else:
                print("No ESPS records generated.")

        elif choice == 9:
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

