# Listing Attacks: The program first displays a list of all possible cyberattacks.
# User Selection:: When a cyberattack is selected, the program generates 10 random incidents for that attack and stores them in a dictionary.
# Continuing Until Quit: The program loops until the user decides to quit.
# Final Report: Upon quitting, the program prints the final report of all generated incidents.
# Saving to JSON: The results are saved to a JSON file named `attack_results.json`.
############### THIS SECTION OF PLAY-BOOK IS DESIGNED & ASSEMBLED BY RSANDY SINGH FROM KNET Consulting #######################

#python
import json
import random

# List of possible cyber attacks
cyber_attacks = [
    "Phishing", "Malware", "Ransomware", "SQL Injection", 
    "Cross-Site Scripting (XSS)", "Denial of Service (DoS)", 
    "Distributed Denial of Service (DDoS)", "Man-in-the-Middle (MitM)", 
    "Brute Force Attack", "Insider Threats", "Advanced Persistent Threats (APTs)", 
    "Zero-Day Exploits", "Password Attacks"
]

# Dictionary to store the results of each attack
attack_results = {attack: [] for attack in cyber_attacks}

# Function to generate a random incident
def generate_incident(attack_type):
    incident = {
        "id": random.randint(1000, 9999),
        "description": f"Simulated {attack_type} incident.",
        "severity": random.choice(["Low", "Medium", "High", "Critical"]),
        "timestamp": random.choice([
            "2024-08-01 10:00:00", "2024-08-01 12:00:00", "2024-08-01 14:00:00",
            "2024-08-01 16:00:00", "2024-08-01 18:00:00"
        ])
    }
    return incident

# Main program loop
while True:
    print("\nList of Possible Cyber Attacks:")
    for i, attack in enumerate(cyber_attacks, start=1):
        print(f"{i}. {attack}")
    print("Q. Quit")

    choice = input("Select a cyber attack (number) or Q to quit: ")

    if choice.lower() == 'q':
        break

    if not choice.isdigit() or not (1 <= int(choice) <= len(cyber_attacks)):
        print("Invalid choice. Please try again.")
        continue

    attack_type = cyber_attacks[int(choice) - 1]
    print(f"\nSimulating {attack_type} incidents...")

    # Generate 10 incidents for the selected attack
    for _ in range(10):
        incident = generate_incident(attack_type)
        attack_results[attack_type].append(incident)
        print(f"Generated incident: {incident}")

# Display the results of each attack
print("\nFinal Report:")
for attack, incidents in attack_results.items():
    print(f"\n{attack}:")
    for incident in incidents:
        print(incident)

# Save the results to a JSON file
with open('attack_results.json', 'w') as file:
    json.dump(attack_results, file, indent=4)

print("\nResults saved to attack_results.json")

