
# ZEEK-DATA ANAMOLY DETECTOR - MULTIPLE ANAMOLIES
# ANAMOLY TYPES DETECTOR - Port Scan", "DDoS Attack", "Suspicious ICMP Traffic", "Data Exfiltration", "Malware Communication", "Unauthorized Access


#**********THIS ZEEK DATA ANAMOLY DETECTOR IS DESIGNED & ASSEMBLED BY RANDY SINGH, SENIOR COMPUTER SCIENTIST DISA/EIIC/EM2*****************


#python
import json
import random

# Function to generate normal Zeek data records
def generate_normal_zeek_data(count):
    return [
        {"timestamp": 1600000001 + i, "src_ip": f"192.168.1.{i+1}", "src_port": 10000 + i, 
         "dst_ip": f"10.0.0.{i+1}", "dst_port": (80 if i % 2 == 0 else 443), 
         "protocol": ("TCP" if i % 3 == 0 else "UDP"), "state": "-", "duration": 1.0 + i*0.01, 
         "size": 500 + i*10, "bytes": 1000 + i*20} 
        for i in range(count)
    ]

# Generate Zeek data with 100 records
zeek_data = generate_normal_zeek_data(100)

# Insert hidden anomalies into Zeek data
def insert_hidden_anomalies(logs, anomaly_count):
    # Randomly choose indices to insert anomalies
    anomaly_indices = random.sample(range(len(logs)), anomaly_count)
    anomaly_types = ["Port Scan", "DDoS Attack", "Suspicious ICMP Traffic", "Data Exfiltration", "Malware Communication", "Unauthorized Access"]

    for i, index in enumerate(anomaly_indices):
        # Randomly assign anomaly properties to some records
        anomaly_record = logs[index]
        anomaly_type = anomaly_types[i % len(anomaly_types)]

        if anomaly_type == "Port Scan":
            anomaly_record["dst_port"] = random.randint(1, 1024)
            anomaly_record["protocol"] = "TCP"
            anomaly_record["state"] = "SF"
        elif anomaly_type == "DDoS Attack":
            anomaly_record["dst_port"] = random.choice([80, 443])
            anomaly_record["protocol"] = "UDP"
            anomaly_record["size"] = random.randint(1500, 3000)
        elif anomaly_type == "Suspicious ICMP Traffic":
            anomaly_record["protocol"] = "ICMP"
            anomaly_record["state"] = "REJ"
            anomaly_record["duration"] = round(random.uniform(0.001, 0.01), 3)
        elif anomaly_type == "Data Exfiltration":
            anomaly_record["dst_port"] = 22  # SSH Port for exfiltration
            anomaly_record["bytes"] = random.randint(10000, 50000)
        elif anomaly_type == "Malware Communication":
            anomaly_record["dst_port"] = 8080  # Common malware communication port
            anomaly_record["protocol"] = "TCP"
            anomaly_record["size"] = random.randint(100, 500)
        elif anomaly_type == "Unauthorized Access":
            anomaly_record["dst_port"] = 23  # Telnet port for unauthorized access
            anomaly_record["state"] = "S0"
            anomaly_record["duration"] = round(random.uniform(0.1, 2.0), 3)

        anomaly_record["anomaly_type"] = anomaly_type  # Mark the record with the type of anomaly

    return logs

# Insert 10 hidden anomalies into Zeek data
zeek_data_with_hidden_anomalies = insert_hidden_anomalies(zeek_data, 10)

# Save the original Zeek logs before anomaly detection
with open('zeek_logs_file_before_anomalies.json', 'w') as file:
    json.dump(zeek_data_with_hidden_anomalies, file, indent=4)

print("Original Zeek Data with Hidden Anomalies (100 Records):")
print(json.dumps(zeek_data_with_hidden_anomalies, indent=4))

# Function to detect anomalies and mark them
def detect_anomalies(logs):
    anomalies_detected = []
    logs_with_anomalies = []

    for log in logs:
        if 'anomaly_type' in log:  # Check if this record has an anomaly
            anomalies_detected.append(log)
        logs_with_anomalies.append(log)

    return anomalies_detected, logs_with_anomalies

# Function to provide recommendations based on anomalies
def provide_recommendations(anomalies):
    recommendations = []
    for anomaly in anomalies:
        if anomaly['anomaly_type'] == "Port Scan":
            recommendation = "Mitigate Port Scanning: Deploy intrusion detection systems (IDS) to identify and block scanning attempts."
        elif anomaly['anomaly_type'] == "DDoS Attack":
            recommendation = "Mitigate DDoS Attack: Use rate limiting and traffic filtering to handle volumetric attacks."
        elif anomaly['anomaly_type'] == "Suspicious ICMP Traffic":
            recommendation = "Investigate ICMP Traffic: Monitor for potential ICMP floods and filter unnecessary ICMP packets."
        elif anomaly['anomaly_type'] == "Data Exfiltration":
            recommendation = "Prevent Data Exfiltration: Inspect outbound traffic and use data loss prevention (DLP) solutions."
        elif anomaly['anomaly_type'] == "Malware Communication":
            recommendation = "Detect Malware Communication: Use threat intelligence and monitoring to detect unusual outbound traffic."
        elif anomaly['anomaly_type'] == "Unauthorized Access":
            recommendation = "Prevent Unauthorized Access: Enforce strict access controls and monitor for unusual login attempts."
        else:
            recommendation = "Inspect unusual traffic: Review the source IP and traffic patterns for suspicious activity."

        recommendations.append({"anomaly": anomaly, "recommendation": recommendation})
    
    # Add total number of detected anomalies to recommendations
    recommendations.append({"total_anomalies_detected": len(anomalies)})
    return recommendations

# Detect anomalies in the data and mark them
anomalies_detected, logs_with_anomalies = detect_anomalies(zeek_data_with_hidden_anomalies)

# Provide recommendations for detected anomalies
recommendations = provide_recommendations(anomalies_detected)

# Save detected anomalies to JSON
with open('detected_anomalies.json', 'w') as file:
    json.dump(anomalies_detected, file, indent=4)

# Save recommendations to JSON
with open('recommendations.json', 'w') as file:
    json.dump(recommendations, file, indent=4)

# Save Zeek logs after marking anomalies to JSON
with open('zeek_logs_file_after_anomalies.json', 'w') as file:
    json.dump(logs_with_anomalies, file, indent=4)

# Display the anomalies, recommendations, and logs after marking anomalies on the console
print("\nZeek Data with Anomalies Marked:")
print(json.dumps(logs_with_anomalies, indent=4))

print("\nDetected Anomalies:")
print(json.dumps(anomalies_detected, indent=4))

print("\nRecommendations for Mitigation:")
print(json.dumps(recommendations, indent=4))
