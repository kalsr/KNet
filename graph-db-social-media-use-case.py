

#SOCIAL-MEDIA USE-CASE USING GRAPH THEORY

#THIS APPLICATION WAS ASSEMBLED BY RANDY SINGH DISA/EIIC/EM2 TO TRACK MALICIOUS NODES IN SOCIAL MEDIA.

import json
import random
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
        print("NODES:")
        for node_id, properties in self.nodes.items():
            print(f"{node_id}: {properties}")
        print("\nEDGES:")
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

    def query_relationship(self, relationship):
        print(f"Edges with relationship '{relationship}':")
        for edge in self.edges:
            if edge['relationship'] == relationship:
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

def generate_random_post():
    sample_posts = [
        "Loving the sunny weather today!",
        "Just finished a great workout session.",
        "Excited about the new project at work.",
        "Enjoying a delicious meal at my favorite restaurant.",
        "Had an amazing time with friends over the weekend.",
        "Reading an interesting book on AI.",
        "Can't wait for the upcoming vacation!",
        "Exploring new hobbies during my free time.",
        "Feeling grateful for the small things in life.",
        "Watching a fantastic movie tonight."
    ]
    return random.choice(sample_posts)

def generate_graph(num_users, num_posts):
    db = GraphDatabase()

    # List of sample names
    sample_names = [
        "Alice", "Bob", "Charlie", "David", "Eve",
        "Frank", "Grace", "Hannah", "Ivy", "Jack"
    ]

    # Create users
    for i in range(num_users):
        user_id = f"User{i}"
        properties = {
            'name': random.choice(sample_names),
            'age': random.randint(18, 65),
            'email': f"user{i}@example.com"
        }
        db.add_node(user_id, properties)

    # Create posts
    for i in range(num_posts):
        post_id = f"Post{i}"
        properties = {
            'content': generate_random_post(),
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

    # Create comment relationships
    for i in range(num_users):
        for j in range(random.randint(1, 5)):  # Each user comments on 1 to 5 posts
            post_id = f"Post{random.randint(0, num_posts-1)}"
            comment_id = f"Comment{i}_{j}"
            properties = {
                'content': f"Comment by User{i} on Post{random.randint(0, num_posts-1)}",
                'timestamp': f"2024-06-{random.randint(1, 30)}T{random.randint(0, 23):02}:{random.randint(0, 59):02}:{random.randint(0, 59):02}Z"
            }
            db.add_edge(f"User{i}", post_id, "COMMENTED_ON", properties)

    return db

def main():
    while True:
        try:
            num_users = int(input("Enter the number of Social Media users to generate in the graph database: "))
            num_posts = int(input("Enter the number of Social Media posts to generate in the graph database: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        db = generate_graph(num_users, num_posts)
        filename = input("Enter the filename to save the Social Media graph database (e.g., graph_db.json): ")
        db.save_to_file(filename)

        while True:
            print("\nOptions:")
            print("1. Display Social Media Graph Database")
            print("2. Query Social Media Graph Database")
            print("3. Query Specific Relationship")
            print("4. Generate New Graph Database")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                db.display()
            elif choice == '2':
                node_id = input("Enter the node ID to query: ")
                db.query(node_id)
            elif choice == '3':
                relationship = input("Enter the relationship to query (e.g., FRIEND, LIKES, COMMENTED_ON): ")
                db.query_relationship(relationship)
            elif choice == '4':
                break
            elif choice == '5':
                sys.exit()
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
