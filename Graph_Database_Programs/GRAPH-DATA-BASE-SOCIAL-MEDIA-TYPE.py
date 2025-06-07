# THIS PROGRAM IS ASSEMBLED BY RANDY SINGH FROM DISA/EIIC/EM2 TO SUPPORT GRAPH DATA BASE ACTIVITIES.

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

def generate_graph(num_users, num_posts):
    db = GraphDatabase()

    # Create users
    for i in range(num_users):
        user_id = f"User{i}"
        properties = {
            'name': generate_random_string(),
            'age': random.randint(18, 65),
            'email': f"user{i}@example.com"
        }
        db.add_node(user_id, properties)

    # Create posts
    for i in range(num_posts):
        post_id = f"Post{i}"
        properties = {
            'content': " ".join(generate_random_string(random.randint(4, 10)) for _ in range(random.randint(3, 10))),
            'timestamp': f"2024-06-{random.randint(1, 30)}T{random.randint(0, 23):02}:{random.randint(0, 59):02}:{random.randint(0, 59):02}Z"
        }
        db.add_node(post_id, properties)

    # Create friend relationships
    for i in range(num_users):
        for j in range(random.randint(1, 5)):  # Each user has 1 to 5 friends
            friend_id = f"User{random.randint(0, num_users-1)}"
            if friend_id != f"User{i}":  # Avoid self-friendship
                db.add_edge(f"User{i}", friend_id, "FRIEND", {'since': f"2023-0{random.randint(1, 9)}-{random.randint(1, 28):02}"})

    # Create like relationships
    for i in range(num_users):
        for j in range(random.randint(1, 5)):  # Each user likes 1 to 5 posts
            post_id = f"Post{random.randint(0, num_posts-1)}"
            db.add_edge(f"User{i}", post_id, "LIKES", {'timestamp': f"2024-06-{random.randint(1, 30)}T{random.randint(0, 23):02}:{random.randint(0, 59):02}:{random.randint(0, 59):02}Z"})

    return db

def main():
    while True:
        try:
            num_users = int(input("Enter the number of users to generate in the graph database: "))
            num_posts = int(input("Enter the number of posts to generate in the graph database: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        db = generate_graph(num_users, num_posts)
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
