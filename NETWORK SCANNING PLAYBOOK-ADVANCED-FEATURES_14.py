
# NETWORK SCANNING PLAYBOOK-ADVANCED-FEATURES

# A LIST OF DFFERENT TYPES OF NETWORK SCANS PERFORMED IN THIS PART OF PLAY-BOOK

############### THIS SECTION OF PLAY-BOOK IS DESIGNED & ASSEMBLED BY Kalsnet Technologies #######################

#python
import json
import random
import os

def detect_port_scans():
    open_ports = [str(random.choice(range(1024, 65535))) for _ in range(random.randint(1, 10))]
    return {'open_ports': open_ports}

def detect_running_software():
    running_processes = [{'pid': random.randint(1000, 5000), 'name': random.choice(['python', 'nginx', 'apache']), 'username': random.choice(['user1', 'www-data'])} for _ in range(random.randint(1, 10))]
    return {'running_processes': running_processes}

def detect_ssh_connections():
    ssh_sessions = [{'pid': random.randint(1000, 5000), 'laddr': ('192.168.1.100', 22), 'raddr': ('192.168.1.1', random.randint(50000, 60000)), 'status': 'ESTABLISHED'} for _ in range(random.randint(1, 10))]
    return {'ssh_sessions': ssh_sessions}

def detect_powershell():
    powershell_processes = [{'pid': random.randint(1000, 5000), 'name': 'powershell', 'username': 'admin'} for _ in range(random.randint(1, 10))]
    return {'powershell_processes': powershell_processes}

def detect_exploits():
    exploit_logs = [f"Failed password for root from 192.168.1.{i} port 22 ssh2" for i in range(1, random.randint(2, 10))]
    return {'exploit_logs': exploit_logs}

def detect_exfiltration():
    exfiltration_processes = [{'name': 'curl', 'bytes_transferred': random.randint(100000, 200000000)} for _ in range(random.randint(1, 10))]
    return {'exfiltration_processes': exfiltration_processes}

def scan_network(data_type):
    if data_type == '1':
        return detect_port_scans()
    elif data_type == '2':
        return detect_running_software()
    elif data_type == '3':
        return detect_ssh_connections()
    elif data_type == '4':
        return detect_powershell()
    elif data_type == '5':
        return detect_exploits()
    elif data_type == '6':
        return detect_exfiltration()
    else:
        return {}

def save_data(scanned_data):
    for key, value in scanned_data.items():
        with open(f'{key}.json', 'w') as f:
            json.dump({key: value}, f, indent=4)

def load_existing_data():
    data_files = [
        'open_ports.json',
        'running_processes.json',
        'ssh_sessions.json',
        'powershell_processes.json',
        'exploit_logs.json',
        'exfiltration_processes.json'
    ]
    
    existing_data = {
        'open_ports': [],
        'running_processes': [],
        'ssh_sessions': [],
        'powershell_processes': [],
        'exploit_logs': [],
        'exfiltration_processes': []
    }
    
    for file_name in data_files:
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                data = json.load(f)
                key = file_name.replace('.json', '')
                existing_data[key] = data[key]
                
    return existing_data

def main():
    scanned_data = load_existing_data()

    while True:
        print("\nChoose the data item to scan from the network:")
        print("1. Open Ports")
        print("2. Running Software")
        print("3. SSH Connections")
        print("4. PowerShell Processes")
        print("5. Exploits")
        print("6. Data Exfiltration")
        print("7. Quit and Save All Scanned Data")

        choice = input("Enter the number corresponding to your choice: ")

        if choice == '7':
            save_data(scanned_data)
            print("\nAll Data Items Scanned from the Network:")
            for key, value in scanned_data.items():
                print(f"\n{key.replace('_', ' ').title()}:")
                for item in value:
                    print(item)
            input("\nPress Enter to exit...")
            break

        detected_data = scan_network(choice)
        
        # Merge detected data with scanned data
        for key in detected_data:
            scanned_data[key].extend(detected_data[key])

        # Save detected data to a corresponding JSON file and display it
        for key in detected_data:
            with open(f'{key}.json', 'w') as f:
                json.dump({key: detected_data[key]}, f, indent=4)
            print(f"\nDetected {key.replace('_', ' ').title()}:")
            for item in detected_data[key]:
                print(item)
        
        cont = input("\nDo you want to scan another data item? (yes/no): ")
        if cont.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
