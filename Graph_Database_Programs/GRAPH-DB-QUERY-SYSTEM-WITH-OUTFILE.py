#THIS PROGRAM IS ASSEMBLED BY RANDY SINGH FROM DISA/EIIC/EM2 TO SUPPORT GRAPH DATA BASE ACTIVITIES.



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

def generate_graph(num_records):
    db = GraphDatabase()
    for i in range(num_records):
        node_id = f"Node{i}"
        properties = {
            'name': generate_random_string(),
            'value': random.randint(1, 100)
        }
        db.add_node(node_id, properties)

    for i in range(num_records):
        from_node = f"Node{i}"
        to_node = f"Node{random.randint(0, num_records-1)}"
        relationship = "CONNECTED_TO"
        properties = {
            'weight': random.randint(1, 10)
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

        db = generate_graph(num_records)
        filename = input("Enter the filename to save the graph database (e.g., graph_db.json): ")
        db.save_to_file(filename)

        while True:
            print("\nOptions:")
            print("1. Display Graph Database")
            print("2. Query Graph Database")
            print("3. Generate New Graph Database")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                db.display()
            elif choice == '2':
                node_id = input("Enter the node ID to query: ")
                db.query(node_id)
            elif choice == '3':
                break
            elif choice == '4':
                sys.exit()
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
