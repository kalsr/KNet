#CYBER-DATA USE-CASE2
#1. Generating Cyber Data:
  # - The `generate_cyber_data` function creates a specified number of nodes and edges with properties relevant to cyber data, including a random chance of being marked as malicious.

#2. Saving and Loading Graph Database:
  # - The `save_to_file`, `save_malicious_to_file`, and `save_non_malicious_to_file` methods handle saving the entire graph database, malicious records, and non-malicious records to separate JSON files, respectively.
   #- The `load_from_file` method allows loading the graph database from a JSON file.

#3. Querying Malicious and Non-Malicious Records:
   #- The `query_malicious` and `query_non_malicious` methods print all malicious and non-malicious records, respectively.

#4. User Interface:
   #- The user is prompted for the number of records to generate and filenames to save the graph database, malicious records, and non-malicious records.
   #- Options to display the graph, query specific nodes, query malicious records, query non-malicious

# THIS APPLICATION WAS ASSEMBLED BY RANDY SINGH DISA/EIIC/EM2 TO TRACK MALICIOUS NODES IN CYBER DATA.

#python
import json
import random
import string
import sys

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

    def query_non_malicious(self):
        print("Non-Malicious Records:")
        for node_id, properties in self.nodes.items():
            if not properties.get('malicious', False):
                print(f"{node_id}: {properties}")
        print("Non-Malicious Edges:")
        for edge in self.edges:
            if not edge['properties'].get('malicious', False):
                print(f"{edge['from']} -[{edge['relationship']} {edge['properties']}]-> {edge['to']}")

    def save_to_file(self, filename):
        data = {
            'nodes': self.nodes,
            'edges': self.edges
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Graph database saved to {filename}")

    def save_malicious_to_file(self, filename):
        data = {
            'nodes': {k: v for k, v in self.nodes.items() if v.get('malicious', False)},
            'edges': [e for e in self.edges if e['properties'].get('malicious', False)]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Malicious records saved to {filename}")

    def save_non_malicious_to_file(self, filename):
        data = {
            'nodes': {k: v for k, v in self.nodes.items() if not v.get('malicious', False)},
            'edges': [e for e in self.edges if not e['properties'].get('malicious', False)]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Non-malicious records saved to {filename}")

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.nodes = data['nodes']
            self.edges = data['edges']
        print(f"Graph database loaded from {filename}")

    def modify_node(self, node_id, properties):
        if node_id in self.nodes:
            self.nodes[node_id].update(properties)
            print(f"Node {node_id} updated.")
        else:
            print(f"No node with ID {node_id} found.")

    def modify_edge(self, edge_id, properties):
        if 0 <= edge_id < len(self.edges):
            self.edges[edge_id].update(properties)
            print(f"Edge {edge_id} updated.")
        else:
            print(f"No edge with ID {edge_id} found.")

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
            num_records = int(input("Enter the number of Cyber Data records to generate in the graph database: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        db = generate_cyber_data(num_records)
        filename = input("Enter the filename to save the Cyber Graph Database (e.g., cyber-data.json): ")
        db.save_to_file(filename)

        malicious_filename = input("Enter the filename to save the malicious Cyber Data records (e.g., Malicious-Records.json): ")
        db.save_malicious_to_file(malicious_filename)

        non_malicious_filename = input("Enter the filename to save the non-malicious Cyber Data records (e.g., Non-Malicious-Records.json): ")
        db.save_non_malicious_to_file(non_malicious_filename)

        while True:
            print("\nOptions:")
            print("1. Display Cyber Data Graph Database")
            print("2. Query Cyber Data Graph Database")
            print("3. Query Malicious Cyber Data Records")
            print("4. Query Non-Malicious Cyber Data Records")
            print("5. Load Graph Database from File")
            print("6. Modify Node")
            print("7. Modify Edge")
            print("8. Generate New Graph Database")
            print("9. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                db.display()
            elif choice == '2':
                node_id = input("Enter the node ID to query: ")
                db.query(node_id)
            elif choice == '3':
                db.query_malicious()
            elif choice == '4':
                db.query_non_malicious()
            elif choice == '5':
                filename = input("Enter the filename to load the graph database (e.g., cyber-data.json): ")
                db.load_from_file(filename)
            elif choice == '6':
                node_id = input("Enter the node ID to modify: ")
                properties = json.loads(input("Enter the properties to update (in JSON format): "))
                db.modify_node(node_id, properties)
            elif choice == '7':
                edge_id = int(input("Enter the edge ID to modify: "))
                properties = json.loads(input("Enter the properties to update (in JSON format): "))
                db.modify_edge(edge_id, properties)
            elif choice == '8':
                break
            elif choice == '9':
                sys.exit()
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()



#1. Generating Cyber Data:
  # - The `generate_cyber_data` function creates a specified number of nodes and edges with properties relevant to cyber data, including a random chance of being marked as malicious.

#2. Saving and Loading Graph Database:
  # - The `save_to_file`, `save_malicious_to_file`, and `save_non_malicious_to_file` methods handle saving the entire graph database, malicious records, and non-malicious records to separate JSON files, respectively.
   #- The `load_from_file` method allows loading the graph database from a JSON file.

#3. Querying Malicious and Non-Malicious Records:
   #- The `query_malicious` and `query_non_malicious` methods print all malicious and non-malicious records, respectively.

#4. User Interface:
   #- The user is prompted for the number of records to generate and filenames to save the graph database, malicious records, and non-malicious records.
   #- Options to display the graph, query specific nodes, query malicious records, query non-malicious



