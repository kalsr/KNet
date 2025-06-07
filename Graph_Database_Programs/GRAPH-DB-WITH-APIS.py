#python
import json
import random

# Function to generate API records
def generate_api_records(num_records, start_index=0):
    records = []
    for i in range(start_index, start_index + num_records):
        record = {
            "vertex": f"IP_{i}",
            "node": f"Device_{i}",
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

# Function to query the graph database
def query_graph_database(graph, malicious=True):
    nodes = [vertex for vertex, attr in graph["vertices"].items() if attr["malicious"] == malicious]
    return nodes

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
        
        # Query the graph database
        malicious_nodes = query_graph_database(graph, malicious=True)
        non_malicious_nodes = query_graph_database(graph, malicious=False)
        
        print(f"Malicious IPs: {malicious_nodes}")
        print(f"Non-malicious IPs: {non_malicious_nodes}")
        
        # Visualize the graph
        print("Graph visualization for current data:")
        visualize_graph(graph)

if __name__ == "__main__":
    main()
