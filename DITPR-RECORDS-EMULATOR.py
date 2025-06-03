

# Python application that generates DiTPR records, including API details, and saves them to an output file. This script uses only built-in libraries and prompts the user for the number of records to generate.

#python
import json
import random
import datetime

def generate_ditpr_record(record_id):
    record = {
        "System Information": {
            "System Name": f"System_{record_id}",
            "System Acronym": f"S{record_id}",
            "System Description": f"Description for System_{record_id}",
            "System Type": random.choice(["Application", "Service", "Infrastructure"]),
            "System Owner": f"Owner_{random.randint(1, 100)}",
            "System Status": random.choice(["Active", "Inactive", "Decommissioned"])
        },
        "Administrative Information": {
            "Record ID": record_id,
            "Date of Entry": datetime.date.today().isoformat(),
            "Last Updated": datetime.date.today().isoformat(),
            "Record Owner": f"RecordOwner_{random.randint(1, 100)}"
        },
        "Investment Information": {
            "Budget Information": f"Budget_{random.randint(10000, 100000)}",
            "Funding Source": f"Source_{random.randint(1, 10)}",
            "Lifecycle Phase": random.choice(["Development", "Deployment", "Maintenance"])
        },
        "Technical Information": {
            "Technology Stack": f"TechStack_{random.randint(1, 10)}",
            "Hosting Environment": random.choice(["Cloud", "On-premises"]),
            "Interoperability": f"Interoperability_{random.randint(1, 10)}"
        },
        "API Information": {
            "API Name": f"API_{record_id}",
            "API Description": f"Description for API_{record_id}",
            "API Version": f"v{random.randint(1, 5)}.0",
            "API Endpoints": [f"/endpoint{random.randint(1, 10)}" for _ in range(3)],
            "API Documentation": f"http://api_docs_{record_id}.example.com",
            "API Protocols": random.choice(["REST", "SOAP", "GraphQL"]),
            "Authentication Methods": random.choice(["API key", "OAuth"]),
            "Rate Limits": f"{random.randint(100, 1000)} requests per hour",
            "Usage Metrics": f"{random.randint(1000, 10000)} calls per month",
            "API POC (Point of Contact)": f"APIPOC_{random.randint(1, 100)}"
        },
        "Compliance and Security": {
            "Compliance Status": random.choice(["Compliant", "Non-compliant"]),
            "Security Classification": random.choice(["Unclassified", "Confidential", "Secret"]),
            "Risk Assessment": f"Risk_{random.randint(1, 10)}"
        },
        "Performance Metrics": {
            "KPIs (Key Performance Indicators)": [f"KPI_{random.randint(1, 10)}" for _ in range(3)],
            "Usage Statistics": f"{random.randint(1000, 10000)} users per month",
            "Performance Reviews": f"Review_{random.randint(1, 10)}"
        },
        "Contact Information": {
            "System POC (Point of Contact)": f"SystemPOC_{random.randint(1, 100)}",
            "Technical Support Contact": f"SupportContact_{random.randint(1, 100)}"
        }
    }
    return record

def main():
    num_records = int(input("Enter the number of records to generate: "))
    records = []

    for i in range(1, num_records + 1):
        records.append(generate_ditpr_record(i))

    output_file = "DITPR_output.json"
    with open(output_file, 'w') as file:
        json.dump(records, file, indent=4)

    print(f"{num_records} records have been generated and saved to {output_file}")

if __name__ == "__main__":
    main()


#How to Use the Script

#This script generates random data for each record to simulate a variety of DiTPR entries. 
#You can customize the fields and data generation logic as needed.

