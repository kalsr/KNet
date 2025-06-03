#1. Generating Cyber Data:
 #  - The `generate_cyber_data` function creates a specified number of nodes and edges with properties relevant to a cyber scenario, including a random chance of being marked as malicious.
#2. Querying Malicious Records:
   #- The `query_malicious` method in the `GraphDatabase` class prints all nodes and edges marked as malicious.
#3. User Interface:
 #  - The user is prompted for the number of records to generate and the filename to save the database.
  # - The options to display the graph, query specific nodes, query malicious records, generate a new graph, or exit are provided.

#This script generates a graph database with cyber data, saves it to a JSON file, 
#and allows users to query and display the graph with a focus on identifying malicious records.
#THIS APPLICATION WAS ASSEMBLED BY RANDY SINGH DISA/EIIC/EM2 TO TRACK MALICIOUS NODES IN CYBER DATA.



import json
import random
import sys
import string

class GraphDatabase:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node_id, properties):
        self.nodes[node_id] = properties

    def add_edge(self, from_node, to_node, relationship, properties):
        self.edges.append({
            'from': from_node,
            'to': to_node,
            'relationship': relationship,
            'properties': properties
        })

    def display(self):
        print("Nodes:")
        for node_id, properties in self.nodes.items():
            print(f"{node_id}: {properties}")
        print("\nEdges:")
        for edge in self.edges:
            print(f"{edge['from']} -[{edge['relationship']} {edge['properties']}]-> {edge['to']}")

    def query(self, node_id):
        if node_id in self.nodes:
            print(f"Node {node_id}: {self.nodes[node_id]}")
            print("Edges:")
            for edge in self.edges:
                if edge['from'] == node_id or edge['to'] == node_id:
                    print(f"{edge['from']} -[{edge['relationship']} {edge['properties']}]-> {edge['to']}")
        else:
            print(f"No node with ID {node_id} found.")

    def query_malicious(self):
        print("Malicious Records:")
        for node_id, properties in self.nodes.items():
            if properties.get('malicious', False):
                print(f"{node_id}: {properties}")
        print("Malicious Edges:")
        for edge in self.edges:
            if edge['properties'].get('malicious', False):
                print(f"{edge['from']} -[{edge['relationship']} {edge['properties']}]-> {edge['to']}")

    def save_to_file(self, filename):
        data = {
            'nodes': self.nodes,
            'edges': self.edges
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Graph database saved to {filename}")

def generate_random_string(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_cyber_data(num_records):
    db = GraphDatabase()

    # Create nodes (computers, IP addresses, etc.)
    for i in range(num_records):
        node_id = f"Node{i}"
        properties = {
            'type': random.choice(['computer', 'ip_address', 'url']),
            'value': generate_random_string(),
            'malicious': random.choice([True, False])  # Randomly mark some nodes as malicious
        }
        db.add_node(node_id, properties)

    # Create edges (connections, activities, etc.)
    for i in range(num_records):
        from_node = f"Node{random.randint(0, num_records-1)}"
        to_node = f"Node{random.randint(0, num_records-1)}"
        if from_node != to_node:  # Avoid self-connections
            relationship = random.choice(['CONNECTED_TO', 'ACCESSES', 'COMMUNICATES_WITH'])
            properties = {
                'timestamp': f"2024-06-{random.randint(1, 30)}T{random.randint(0, 23):02}:{random.randint(0, 59):02}:{random.randint(0, 59):02}Z",
                'malicious': random.choice([True, False])  # Randomly mark some edges as malicious
            }
            db.add_edge(from_node, to_node, relationship, properties)

    return db

def main():
    while True:
        try:
            num_records = int(input("Enter the number of records to generate in the graph database: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        db = generate_cyber_data(num_records)
        filename = input("Enter the filename to save the graph database (e.g., graph_db.json): ")
        db.save_to_file(filename)

        while True:
            print("\nOptions:")
            print("1. Display Graph Database")
            print("2. Query Graph Database")
            print("3. Query Malicious Records")
            print("4. Generate New Graph Database")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                db.display()
            elif choice == '2':
                node_id = input("Enter the node ID to query: ")
                db.query(node_id)
            elif choice == '3':
                db.query_malicious()
            elif choice == '4':
                break
            elif choice == '5':
                sys.exit()
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
