
# THIS PROGRAM IS DESIGNED AND ASSEMBLED BY RANDY SINGH DISA/EIIC/EM2 TO SUPPORT API-SECURITY PROJECT AT CPL-NA

#python
import json
import random

# List of fictitious IPs and devices
ips = [f"192.168.1.{i}" for i in range(1, 101)]
devices = [f"Device_{i}" for i in range(1, 101)]

# Function to generate API records
def generate_api_records(num_records, start_index=0):
    records = []
    for i in range(start_index, start_index + num_records):
        record = {
            "vertex": ips[i % len(ips)],
            "node": devices[i % len(devices)],
            "edge": f"Connection_{i}",
            "malicious": random.choice([True, False])
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
        "edges": []
    }
    for record in records:
        graph["vertices"][record["vertex"]] = {
            "node": record["node"],
            "malicious": record["malicious"]
        }
        graph["edges"].append((record["vertex"], record["node"], record["edge"]))
    return graph

# Function to get details of a specific node
def get_node_details(graph, vertex):
    if vertex in graph["vertices"]:
        node_details = graph["vertices"][vertex]
        connections = [edge for edge in graph["edges"] if edge[0] == vertex or edge[1] == vertex]
        return node_details, connections
    else:
        return None, None

# Function to visualize the graph as text
def visualize_graph(graph):
    for vertex, attr in graph["vertices"].items():
        node_type = "Malicious" if attr["malicious"] else "Non-Malicious"
        print(f"IP Address: {vertex}, Device: {attr['node']}, Type: {node_type}")
    for edge in graph["edges"]:
        print(f"Connection: {edge[0]} --({edge[2]})--> {edge[1]}")

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
        print("Graph visualization for current data:")
        visualize_graph(graph)

        # Query specific node details
        query_node = input("Enter an IP address to query (or 'skip' to skip this step): ")
        if query_node.lower() != 'skip':
            node_details, connections = get_node_details(graph, query_node)
            if node_details:
                node_type = "Malicious" if node_details["malicious"] else "Non-Malicious"
                print(f"Details for IP {query_node}:")
                print(f"Device: {node_details['node']}, Type: {node_type}")
                print("Connections:")
                for conn in connections:
                    print(f"{conn[0]} --({conn[2]})--> {conn[1]}")
            else:
                print(f"No details found for IP {query_node}")

if __name__ == "__main__":
    main()
