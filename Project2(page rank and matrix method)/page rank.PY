import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import random

# Load data, assuming no header in the file, skip the first row
x = pd.read_csv('project_data.csv', header=None, skiprows=1)

# Initialize the directed graph
G = nx.DiGraph()

# Iterate through each row to build edges
for i,r in x.iterrows():
    source =str(r[0])  # Assuming the source node is in the first column
    for target in r[1:]:  # Iterate over the rest of the row for target nodes
        b=str(target)
        if b!= 'nan' and b!= source:  # Check if the target is not NaN
            G.add_edge(source, target)

# Draw the graph
pos = nx.spring_layout(G)  # Using spring layout
nx.draw(G, pos, with_labels=True, node_color='pink', edge_color='purple')
plt.title("Network Graph from CSV")
plt.show()

# Print out some basic stats
print("No.of Nodes:", G.number_of_nodes())
print("No. of Edges:", G.number_of_edges())


def walk_random(G):
    nodes = list(G.nodes())  # List of nodes
    RW_points = {node: 0 for node in nodes}  # Dictionary to store RW points of nodes
    a = random.choice(nodes)  # Randomly choosing a node to start the walk
    RW_points[a] += 1  # Increment the RW point of the starting node
    
    for i in range (1000000):  # 1000000 iterations
        outgonig_edges = list(G.out_edges(a))  # Outgoing edges of the current node
        if len(outgonig_edges) == 0:
            focus = random.choice(nodes)  # If no outgoing edges, choose a random node
        else:
            a1 = random.choice(outgonig_edges)  # Choose a random outgoing edge
            focus = a1[1]  # Destination node of the edge
        RW_points[focus] += 1  # Increment the RW point of the destination node
        a = focus  # Move to the destination node for the next iteration
    
    # Sort nodes based on their RW points in descending order
    sorted_nodes = sorted(nodes, key=lambda node: RW_points[node], reverse=True)
    
    # Assign ranks to the nodes based on their RW points
    ranked_nodes = []
    rank = 1
    for node in sorted_nodes:
        ranked_nodes.append((rank, node))
        rank += 1

    return ranked_nodes

# Call the random walk function to get the list of nodes along with their ranks
ranked_nodes = walk_random(G)

# Print the list of nodes along with their ranks
for rank, node in ranked_nodes:
    print(f"Rank {rank}: Node {node}")
