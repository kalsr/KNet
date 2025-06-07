# In this program we use dictionaries to represent the graph and provide a simple console-based interaction 
# for adding vertices and edges, displaying the graph (in text format), 
# and saving/loading the graph to/from a JSON file.

#1. Graph Representation:
   #- The graph is represented as a dictionary where each key is a vertex, and its value is another dictionary 
   #  containing edges and a malicious flag.
   #- Edges are represented as a list of dictionaries, each containing the destination vertex and a malicious flag.

#2. Functions:
   #- `add_vertex`: Adds a vertex (node) to the graph, marking it as malicious if specified.
   #- `add_edge`: Adds an edge between two vertices, marking it as malicious if specified.
   #- `display_graph`: Displays the graph in a textual format, indicating which vertices and edges are malicious.
   #- `save_to_json`: Saves the graph to a `.json` file.
   #- `load_from_json`: Loads a graph from a `.json` file.

#3. Main Loop:
   #- Provides a menu for the user to add vertices and edges, display the graph, 
   #  save to a file, load from a file, or quit.
   #- Continuously prompts the user until they choose to quit.
  #This script provides a basic framework for creating and interacting with a graph database representing cyber data. 
  # THIS PROGRAM IS DESIGNED AND ASSEMBLED BY RANDY SINGH (DISA/EIIC/EM2)

import json
import random
import string

def add_vertex(graph, vertex, is_malicious=False):
    graph[vertex] = {"edges": [], "malicious": is_malicious}

def add_edge(graph, from_vertex, to_vertex, is_malicious=False):
    if from_vertex in graph and to_vertex in graph:
        graph[from_vertex]["edges"].append({"to": to_vertex, "malicious": is_malicious})
        graph[to_vertex]["edges"].append({"to": from_vertex, "malicious": is_malicious})
    else:
        print("One or both vertices not found!")

def display_graph(graph):
    for vertex, data in graph.items():
        print(f"Vertex {vertex} (Malicious: {data['malicious']}):")
        for edge in data["edges"]:
            print(f"  -> {edge['to']} (Malicious: {edge['malicious']})")

def save_to_json(graph, filename):
    with open(filename, 'w') as f:
        json.dump(graph, f, indent=4)

def load_from_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def generate_random_string(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def main():
    graph = {}
    
    while True:
        print("\nOptions:")
        print("1. Add vertex")
        print("2. Add edge")
        print("3. Display graph")
        print("4. Save to JSON file")
        print("5. Load from JSON file")
        print("6. Randomly add vertices and edges")
        print("7. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            vertex = input("Enter vertex name: ")
            is_malicious = input("Is it malicious? (yes/no): ").lower() == 'yes'
            add_vertex(graph, vertex, is_malicious)
        
        elif choice == '2':
            from_vertex = input("Enter from vertex: ")
            to_vertex = input("Enter to vertex: ")
            is_malicious = input("Is the edge malicious? (yes/no): ").lower() == 'yes'
            add_edge(graph, from_vertex, to_vertex, is_malicious)
        
        elif choice == '3':
            display_graph(graph)
        
        elif choice == '4':
            filename = input("Enter filename to save as (with .json extension): ")
            save_to_json(graph, filename)
        
        elif choice == '5':
            filename = input("Enter filename to load from (with .json extension): ")
            graph = load_from_json(filename)
        
        elif choice == '6':
            num_vertices = int(input("Enter the number of vertices to add: "))
            num_edges = int(input("Enter the number of edges to add: "))
            
            for _ in range(num_vertices):
                vertex = generate_random_string()
                is_malicious = random.choice([True, False])
                add_vertex(graph, vertex, is_malicious)
            
            vertices = list(graph.keys())
            for _ in range(num_edges):
                from_vertex = random.choice(vertices)
                to_vertex = random.choice(vertices)
                if from_vertex != to_vertex:
                    is_malicious = random.choice([True, False])
                    add_edge(graph, from_vertex, to_vertex, is_malicious)
        
        elif choice == '7':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()
