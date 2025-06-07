


#Here is the corrected code:


# F5/NETSCOUT/PCAPS WITH MALICIOUS/NON MALICIOUS APIS REPORTS

# Python program that emulates F5, NetScout, PCAP, and PCAP parsed records, including options
# for each activity and saving the results in appropriate JSON output files.
# The program will include malicious and non-malicious API records, with an option to display and
# move these records to separate JSON files.

# The program will also provide explanations for why certain records are considered malicious.
# THIS PROGRAM IS ASSEMBLED BY RANDY SINGH FROM DISA/EIIC/EM2 TO SUPPORT TESTING EFFORTS FOR
# COL-NA API-SECURITY.


# python
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
    record = {
        "record_type": record_type,
        "timestamp": random.randint(1609459200, 1672444800),  # Random timestamp for 2021-2023
        "source_ip": f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}",
        "destination_ip": f"10.0.{random.randint(0, 255)}.{random.randint(0, 255)}",
        "data_volume": round(random.uniform(0.1, 100.0), 2)
    }
    if random.choice([True, False]):
        record["api_status"] = "malicious"
        record["reason"] = random.choice([
            "SQL Injection attempt detected",
            "Cross-Site Scripting (XSS) attack detected",
            "Unauthorized access attempt detected",
            "API abuse detected with high frequency requests"
        ])
    else:
        record["api_status"] = "non-malicious"
        record["reason"] = "Legitimate API usage"
    return record

def save_records_to_file(records, filename):
    with open(filename, 'w') as f:
        json.dump(records, f, indent=4)
    print(f"Records saved to {filename}")

def load_records_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    else:
        return []

def display_records(records):
    for record in records:
        print(json.dumps(record, indent=4))
        print("\n")

def main():
    f5_records = []
    netscout_records = []
    pcap_records = []
    pcap_parsed_records = []

    while True:
        print("\nEmulate Records")
        print("1. Emulate F5 Records")
        print("2. Emulate NetScout Records")
        print("3. Emulate PCAP Records")
        print("4. Emulate PCAP Parsed Records")
        print("5. Display The Report on Malicious/Non-Malicious Records")
        print("6. Exit")

        choice = prompt_user("\nEnter your choice: ", int)

        if choice in [1, 2, 3, 4]:
            num_records = prompt_user("Enter number of records to generate: ", int)
            record_type = ""
            filename = ""
            if choice == 1:
                record_type = "F5"
                filename = "F5-output.json"
                f5_records = [generate_record(record_type) for _ in range(num_records)]
            elif choice == 2:
                record_type = "NetScout"
                filename = "NetScout-output.json"
                netscout_records = [generate_record(record_type) for _ in range(num_records)]
            elif choice == 3:
                record_type = "PCAP"
                filename = "PCAP-output.json"
                pcap_records = [generate_record(record_type) for _ in range(num_records)]
            elif choice == 4:
                record_type = "PCAP Parsed"
                filename = "PCAP-parsed-output.json"
                pcap_parsed_records = [generate_record(record_type) for _ in range(num_records)]
            save_records_to_file([generate_record(record_type) for _ in range(num_records)], filename)
            print(f"\n{record_type} Records:")
            display_records([generate_record(record_type) for _ in range(num_records)])

        elif choice == 5:
            for record_type, records in [("F5", f5_records), ("NetScout", netscout_records), ("PCAP", pcap_records), ("PCAP Parsed", pcap_parsed_records)]:
                malicious_records = [record for record in records if record["api_status"] == "malicious"]
                non_malicious_records = [record for record in records if record["api_status"] == "non-malicious"]
                save_records_to_file(malicious_records, f"{record_type}-malicious-APIs.json")
                save_records_to_file(non_malicious_records, f"{record_type}-non-malicious-APIs.json")
                print(f"\n{record_type} Records:")
                print(f"  Malicious records: {len(malicious_records)}")
                print(f"  Non-malicious records: {len(non_malicious_records)}")

        elif choice == 6:
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
