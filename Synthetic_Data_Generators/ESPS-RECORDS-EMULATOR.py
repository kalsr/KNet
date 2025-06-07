# Python script that generates ESPS records, including API information, and saves them to an output file. 
# This script uses only built-in libraries and prompts the user for the number of records to generate.

#python
import json
import random
import datetime

def generate_esps_record(record_id):
    record = {
        "Service Information": {
            "Service ID": f"S{record_id}",
            "Service Name": f"Service_{record_id}",
            "Service Description": f"Description for Service_{record_id}",
            "Service Type": random.choice(["Web Service", "Microservice"]),
            "Service Owner": f"Owner_{random.randint(1, 100)}",
            "Service Status": random.choice(["Active", "Inactive", "Deprecated"])
        },
        "Application Information": {
            "Application ID": f"A{record_id}",
            "Application Name": f"App_{record_id}",
            "Application Description": f"Description for App_{record_id}",
            "Application Version": f"v{random.randint(1, 5)}.0",
            "Application Status": random.choice(["Active", "Inactive", "Deprecated"])
        },
        "User Information": {
            "User ID": f"U{record_id}",
            "User Name": f"User_{random.randint(1, 1000)}",
            "User Role": random.choice(["Admin", "User", "Viewer"]),
            "User Contact Information": f"user{record_id}@example.com, (555) {random.randint(1000, 9999)}"
        },
        "Operational Metrics": {
            "Metric ID": f"M{record_id}",
            "Metric Description": f"Metric_{random.randint(1, 10)}",
            "Metric Value": f"{random.randint(80, 100)}%",
            "Measurement Date": datetime.date.today().isoformat()
        },
        "Compliance and Security": {
            "Compliance ID": f"C{record_id}",
            "Regulation": f"Regulation_{random.randint(1, 10)}",
            "Compliance Status": random.choice(["Compliant", "Non-compliant"]),
            "Security Classification": random.choice(["Unclassified", "Confidential", "Secret"]),
            "Risk Assessment": f"Risk_{random.randint(1, 10)}"
        },
        "API Information": {
            "API Name": f"API_{record_id}",
            "API Description": f"Description for API_{record_id}",
            "API Version": f"v{random.randint(1, 5)}.0",
            "API Endpoints": [f"/endpoint{random.randint(1, 10)}" for _ in range(3)],
            "API Documentation": f"http://api.docs.example.com/{record_id}",
            "API Protocols": random.choice(["REST", "SOAP", "GraphQL"]),
            "Authentication Methods": random.choice(["API key", "OAuth"]),
            "Rate Limits": f"{random.randint(100, 1000)} requests per hour",
            "Usage Metrics": f"{random.randint(1000, 10000)} calls per month",
            "API POC (Point of Contact)": f"API_POC_{random.randint(1, 100)}"
        }
    }
    return record

def main():
    num_records = int(input("Enter the number of records to generate: "))
    records = []

    for i in range(1, num_records + 1):
        records.append(generate_esps_record(i))

    output_file = "ESPS_output.json"
    with open(output_file, 'w') as file:
        json.dump(records, file, indent=4)

    print(f"{num_records} records have been generated and saved to {output_file}")

if __name__ == "__main__":
    main()



# This script generates random data for each record to simulate a variety of ESPS entries, 
# including API information. You can customize the fields and data generation logic as needed.

