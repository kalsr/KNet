#REQUEST/RESPONSE
# THIS PROGRAM IS DESIGNED AND ASSEMBLED Kalsnet Technologies TO SUPPORT API-SECURITY PROJECT AT CPL-NA

#python
import json
import random
from collections import defaultdict

# List of fictitious IPs and more realistic device names
ips = [f"192.168.1.{i}" for i in range(1, 101)]
devices = [
    "Laptop_Alice", "Laptop_Bob", "Phone_Charlie", "Server_Delta",
    "Router_Echo", "Switch_Foxtrot", "Printer_Golf", "Tablet_Hotel",
    "PC_India", "PC_Juliet", "Camera_Kilo", "AccessPoint_Lima",
    "SmartTV_Mike", "Thermostat_November", "Fridge_Oscar", "Oven_Papa"
]

# Function to generate API records
def generate_api_records(num_records, start_index=0):
    records = []
    for i in range(start_index, start_index + num_records):
        record = {
            "vertex": ips[i % len(ips)],
            "node": devices[i % len(devices)],
            "edge": f"Connection_{i}",
            "malicious": random.choice([True, False]),
            "type": random.choice(["Request", "Response"])
        }
        records.append(record)
    return records

# Function to save records to JSON files
def save_records(records, malicious_file, non_malicious_file):
    malicious_records = [record for record in records if record["malicious"]]
    non_malicious_records = [record for record in records if not record["malicious"]]
    
    with open(malicious_file, 'w') as mf:
        json.dump(malicious_records, mf)
    
    with open(non_malicious_file, 'w') as nmf:
        json.dump(non_malicious_records, nmf)

# Function to create a graph database
def create_graph_database(records):
    graph = {
        "vertices": {},
        "edges": defaultdict(list)
    }
    for record in records:
        graph["vertices"][record["vertex"]] = {
            "node": record["node"],
            "malicious": record["malicious"],
            "type": record["type"]
        }
        graph["edges"][record["vertex"]].append((record["node"], record["edge"], record["malicious"], record["type"]))
    return graph

# Function to get details of a specific node
def get_node_details(graph, vertex):
    if vertex in graph["vertices"]:
        node_details = graph["vertices"][vertex]
        connections = [(vertex, conn[0], conn[1], conn[2], conn[3]) for conn in graph["edges"][vertex]]
        return node_details, connections
    else:
        return None, None

# Function to visualize the graph as text
def visualize_graph(graph):
    for vertex, attr in graph["vertices"].items():
        node_type = "Malicious" if attr["malicious"] else "Non-Malicious"
        request_type = attr["type"]
        print(f"IP Address: {vertex}, Device: {attr['node']}, Type: {node_type}, Request/Response: {request_type}")
    for vertex, connections in graph["edges"].items():
        for conn in connections:
            conn_type = "Malicious" if conn[2] else "Non-Malicious"
            print(f"Connection: {vertex} --({conn[1]}, {conn[3]}, {conn_type})--> {conn[0]}")

# Function to draw a text-based graph
def draw_graph(graph):
    print("\n\nGRAPH VISUALIZATION:\n".upper())
    for vertex, connections in graph["edges"].items():
        print(f"{vertex}:")
        for conn in connections:
            conn_type = "Malicious" if conn[2] else "Non-Malicious"
            print(f"  -> {conn[0]} [{conn[1]}, {conn[3]}, {conn_type}]")

def main():
    all_records = []
    start_index = 0

    print("Malicious and non-malicious records will be saved in 'malicious.json' and 'non_malicious.json' respectively.")

    while True:
        num_records = input("Enter the number of API records to generate (or 'quit' to exit): ")
        if num_records.lower() == 'quit':
            break
        num_records = int(num_records)
        
        # Generate API records
        records = generate_api_records(num_records, start_index)
        start_index += num_records
        all_records.extend(records)
        
        # Save records to JSON files
        save_records(all_records, 'malicious.json', 'non_malicious.json')
        
        # Create graph database
        graph = create_graph_database(all_records)
        
        # Visualize the graph
        print("\n\nGRAPH VISUALIZATION FOR CURRENT DATA:\n".upper())
        visualize_graph(graph)

        # Draw the graph
        draw_graph(graph)

        # Query specific node details until user quits
        while True:
            query_node = input("\nEnter an IP address to query (or 'quit' to stop querying): ")
            if query_node.lower() == 'quit':
                break
            node_details, connections = get_node_details(graph, query_node)
            if node_details:
                node_type = "Malicious" if node_details["malicious"] else "Non-Malicious"
                request_type = node_details["type"]
                print("\n\nDETAILS FOR IP {}:\n".format(query_node).upper())
                print(f"Device: {node_details['node']}, Type: {node_type}, Request/Response: {request_type}")
                print("\n\nCONNECTIONS:\n".upper())
                for conn in connections:
                    conn_type = "Malicious" if conn[3] else "Non-Malicious"
                    print(f"{conn[0]} --({conn[2]}, {conn[4]}, {conn_type})--> {conn[1]}")
            else:
                print(f"No details found for IP {query_node}")

if __name__ == "__main__":
    main()
