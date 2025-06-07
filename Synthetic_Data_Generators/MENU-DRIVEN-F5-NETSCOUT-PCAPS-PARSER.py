#GENERATE F5/NETSCOUT/PCAPS/PCAP-PARSER
# THIS PROGRAM WAS MODIFIED AND ASSEMBLED BY RANDY SINGH DISA/EIIC/EM2 TO SUPPORT COL-NA API-SECURITY PROJECT.
import json
import random
import string
from datetime import datetime, timedelta

def random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def random_ip():
    return '.'.join(map(str, (random.randint(0, 255) for _ in range(4))))

def random_date_within_days(days=365):
    return (datetime.now() - timedelta(days=random.randint(0, days))).isoformat()

def random_boolean():
    return random.choice([True, False])

def generate_f5_record():
    return {
        "system_information": {
            "hostname": random_string(),
            "ip_address": random_ip(),
            "software_version": random.choice(["15.1.2", "16.0.0", "14.1.4"]),
            "hardware_model": random.choice(["BIG-IP 2000s", "BIG-IP 4000s", "BIG-IP 5000s"]),
            "modules_enabled": random.sample(["LTM", "ASM", "APM", "GTM", "SSL Orchestrator", "Advanced WAF"], k=3)
        },
        "virtual_servers": [
            {
                "name": random_string(),
                "ip_address": random_ip(),
                "port": random.randint(1, 65535),
                "protocol": random.choice(["HTTP", "HTTPS", "TCP", "UDP"]),
                "status": random.choice(["Enabled", "Disabled"]),
                "pool": random_string(),
                "iRules_applied": [random_string() for _ in range(3)]
            }
        ],
        "pools": [
            {
                "name": random_string(),
                "load_balancing_method": random.choice(["Round Robin", "Least Connections"]),
                "members": [
                    {
                        "member_ip": random_ip(),
                        "member_port": random.randint(1, 65535),
                        "status": random.choice(["Enabled", "Disabled"]),
                        "monitor": random_string()
                    }
                ]
            }
        ],
        "iRules": [
            {
                "name": random_string(),
                "definition": "Sample definition text " + random_string(50)
            }
        ],
        "iApps": [
            {
                "name": random_string(),
                "template": random_string(),
                "configuration": "Sample configuration text " + random_string(50)
            }
        ],
        "ASM": {
            "policy_name": random_string(),
            "status": random.choice(["Enabled", "Disabled"]),
            "attack_signatures": random.choice(["Up-to-date", "Outdated"]),
            "blocking_mode": random_boolean(),
            "learning_mode": random_boolean(),
            "violations": [
                {
                    "violation_type": random_string(),
                    "count": random.randint(1, 100)
                }
            ]
        },
        "APM": {
            "policy_name": random_string(),
            "status": random.choice(["Enabled", "Disabled"]),
            "authentication_methods": random.sample(["SSO", "MFA"], k=2),
            "access_profiles": [
                {
                    "profile_name": random_string(),
                    "assigned_users_groups": [random_string() for _ in range(3)]
                }
            ]
        },
        "GTM_DNS": {
            "wide_IPs": [
                {
                    "name": random_string(),
                    "pool": random_string(),
                    "status": random.choice(["Enabled", "Disabled"])
                }
            ],
            "pools": [
                {
                    "name": random_string(),
                    "members": [
                        {
                            "member_ip": random_ip(),
                            "status": random.choice(["Enabled", "Disabled"])
                        }
                    ]
                }
            ]
        },
        "SSL_Orchestrator": {
            "configuration_name": random_string(),
            "status": random.choice(["Enabled", "Disabled"]),
            "cipher_suites": [random_string() for _ in range(3)],
            "certificates": [
                {
                    "name": random_string(),
                    "validity_period": {
                        "start_date": random_date_within_days(365),
                        "end_date": random_date_within_days(365 * 3)
                    }
                }
            ]
        },
        "Advanced_WAF": {
            "policy_name": random_string(),
            "status": random.choice(["Enabled", "Disabled"]),
            "bot_defense": random_boolean(),
            "behavioral_analysis": random_boolean(),
            "threat_campaigns": [random_string() for _ in range(3)]
        },
        "network_configuration": {
            "interfaces": [
                {
                    "name": random_string(),
                    "ip_address": random_ip(),
                    "status": random.choice(["Up", "Down"]),
                    "speed": random.choice(["1Gbps", "10Gbps", "40Gbps"])
                }
            ],
            "VLANs": [
                {
                    "name": random_string(),
                    "id": random.randint(1, 4094),
                    "status": random.choice(["Enabled", "Disabled"])
                }
            ]
        },
        "performance_metrics": {
            "traffic_summary": {
                "total_requests": random.randint(1000, 1000000),
                "total_connections": random.randint(1000, 1000000),
                "peak_throughput": f"{random.uniform(1, 100):.2f} Gbps"
            },
            "response_time": {
                "average": f"{random.uniform(1, 500):.2f} ms",
                "95th_percentile": f"{random.uniform(1, 1000):.2f} ms"
            },
            "error_rates": {
                "4xx_errors": random.randint(1, 1000),
                "5xx_errors": random.randint(1, 1000)
            }
        },
        "security_assessment": {
            "vulnerabilities_detected": [
                {
                    "type": random_string(),
                    "count": random.randint(1, 100)
                }
            ],
            "SSL_TLS_configuration": {
                "supported_protocols": random.sample(["TLS 1.2", "TLS 1.3"], k=2),
                "cipher_suites": [random_string() for _ in range(3)],
                "certificate_details": {
                    "name": random_string(),
                    "expiration_date": random_date_within_days(365 * 3)
                }
            }
        },
        "logs_and_events": {
            "event_logs": [
                {
                    "timestamp": random_date_within_days(365),
                    "event_type": random.choice(["Error", "Warning", "Info"]),
                    "description": "Sample event description " + random_string(50)
                }
            ],
            "audit_logs": [
                {
                    "timestamp": random_date_within_days(365),
                    "action": random.choice(["Create", "Modify", "Delete"]),
                    "user": random_string(),
                    "details": "Sample audit details " + random_string(50)
                }
            ]
        },
        "API_records": {
            "endpoints": [
                {
                    "name": random_string(),
                    "method": random.choice(["GET", "POST", "PUT", "DELETE"]),
                    "path": f"/api/{random_string()}",
                    "status": random.choice(["Active", "Deprecated"]),
                    "response_time": f"{random.uniform(0.1, 2):.2f} ms",
                    "request_count": random.randint(1, 1000),
                    "error_count": random.randint(0, 50)
                }
            ]
        }
    }

def generate_netscout_record():
    return {
        "system_information": {
            "hostname": random_string(),
            "ip_address": random_ip(),
            "software_version": random.choice(["v6.3", "v7.1", "v8.0"]),
            "hardware_model": random.choice(["nGeniusONE", "InfiniStream"]),
            "modules_enabled": random.sample(["Traffic Analysis", "Packet Analysis", "Application Monitoring"], k=2)
        },
        "monitored_devices": [
            {
                "device_name": random_string(),
                "ip_address": random_ip(),
                "status": random.choice(["Active", "Inactive"]),
                "monitoring_type": random.choice(["Full", "Partial"])
            }
        ],
        "traffic_data": {
            "total_traffic": f"{random.uniform(1, 100):.2f} GB",
            "peak_traffic": f"{random.uniform(1, 10):.2f} Gbps",
            "average_latency": f"{random.uniform(1, 100):.2f} ms"
        },
        "alerts": [
            {
                "alert_type": random.choice(["Performance", "Security", "Configuration"]),
                "severity": random.choice(["Low", "Medium", "High"]),
                "message": "Sample alert message " + random_string(50)
            }
        ],
        "API_records": {
            "endpoints": [
                {
                    "name": random_string(),
                    "method": random.choice(["GET", "POST", "PUT", "DELETE"]),
                    "path": f"/api/{random_string()}",
                    "status": random.choice(["Active", "Deprecated"]),
                    "response_time": f"{random.uniform(0.1, 2):.2f} ms",
                    "request_count": random.randint(1, 1000),
                    "error_count": random.randint(0, 50)
                }
            ]
        }
    }

def generate_pcap_record():
    return {
        "file_name": f"{random_string()}.pcap",
        "file_size": f"{random.uniform(1, 100):.2f} MB",
        "capture_duration": f"{random.randint(1, 3600)} seconds",
        "total_packets": random.randint(1000, 1000000),
        "protocol_breakdown": {
            "HTTP": random.randint(100, 10000),
            "HTTPS": random.randint(100, 10000),
            "TCP": random.randint(100, 10000),
            "UDP": random.randint(100, 10000)
        },
        "API_records": {
            "endpoints": [
                {
                    "name": random_string(),
                    "method": random.choice(["GET", "POST", "PUT", "DELETE"]),
                    "path": f"/api/{random_string()}",
                    "status": random.choice(["Active", "Deprecated"]),
                    "response_time": f"{random.uniform(0.1, 2):.2f} ms",
                    "request_count": random.randint(1, 1000),
                    "error_count": random.randint(0, 50)
                }
            ]
        }
    }

def generate_pcap_parser_record():
    return {
        "parser_name": random_string(),
        "version": random.choice(["1.0", "2.0", "3.0"]),
        "supported_protocols": random.sample(["HTTP", "HTTPS", "TCP", "UDP"], k=3),
        "parsing_accuracy": f"{random.uniform(95, 100):.2f}%",
        "API_records": {
            "endpoints": [
                {
                    "name": random_string(),
                    "method": random.choice(["GET", "POST", "PUT", "DELETE"]),
                    "path": f"/api/{random_string()}",
                    "status": random.choice(["Active", "Deprecated"]),
                    "response_time": f"{random.uniform(0.1, 2):.2f} ms",
                    "request_count": random.randint(1, 1000),
                    "error_count": random.randint(0, 50)
                }
            ]
        }
    }

def save_records_to_file(filename, records):
    with open(filename, 'w') as f:
        json.dump(records, f, indent=4)
    print(f"Saved records to {filename}")

def extract_and_save_api_records(source_filename, api_filename):
    with open(source_filename, 'r') as f:
        records = json.load(f)
        api_records = [record['API_records'] for record in records]
        save_records_to_file(api_filename, api_records)
        print(json.dumps(api_records, indent=4))

def main():
    while True:
        print("\nMenu:")
        print("1. Emulate F5 records")
        print("2. Emulate NETSCOUT records")
        print("3. Emulate PCAP records")
        print("4. Emulate PCAP Parser records")
        print("5. Display and Save API record for F5")
        print("6. Display and Save API records for NETSCOUT")
        print("7. Display and Save API records for PCAP")
        print("8. Display and Save API records for PCAP Parser")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            num_records = int(input("Enter the number of F5 records to generate: "))
            records = [generate_f5_record() for _ in range(num_records)]
            save_records_to_file('F5-output.json', records)

        elif choice == '2':
            num_records = int(input("Enter the number of NETSCOUT records to generate: "))
            records = [generate_netscout_record() for _ in range(num_records)]
            save_records_to_file('NETSCOUT-output.json', records)

        elif choice == '3':
            num_records = int(input("Enter the number of PCAP records to generate: "))
            records = [generate_pcap_record() for _ in range(num_records)]
            save_records_to_file('PCAP-output.json', records)

        elif choice == '4':
            num_records = int(input("Enter the number of PCAP Parsed records to generate: "))
            records = [generate_pcap_parser_record() for _ in range(num_records)]
            save_records_to_file('PCAP-Parser-output.json', records)

        elif choice == '5':
            extract_and_save_api_records('F5-output.json', 'F5-discovered-APIs.json')

        elif choice == '6':
            extract_and_save_api_records('NETSCOUT-output.json', 'NETSCOUT-discovered-APIs.json')

        elif choice == '7':
            extract_and_save_api_records('PCAP-output.json', 'PCAP-discovered-APIs.json')

        elif choice == '8':
            extract_and_save_api_records('PCAP-Parser-output.json', 'PCAP-Parser-discovered-APIs.json')

        elif choice == '9':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
