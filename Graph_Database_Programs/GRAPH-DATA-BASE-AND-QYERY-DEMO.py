

#python
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


#Explanation:
#1. GraphDatabase Class: This class represents the graph database using dictionaries for nodes and a list for edges.
 #  - `add_node()`: Adds a node to the graph.
  # - `add_edge()`: Adds an edge between two nodes.
  # - `display()`: Displays the nodes and edges in the graph.
  #- `query()`: Queries a node and its connected edges.

#2. generate_random_string(): Generates a random string of a specified length.

#3. generate_graph(): Generates a graph with a specified number of records (nodes and edges).

#4. main(): The main function that runs the program, prompting the user for input and handling the 
# options to display, query, generate a new graph, or exit.

# The program will prompt for the number of records, allow displaying the graph, querying nodes, 
#and regenerating the graph until the user decides to exit.
