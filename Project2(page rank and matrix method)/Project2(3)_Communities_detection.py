import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import random

# Load data, assuming no header in the file, skip the first row
x = pd.read_csv('project_data.csv', header=None, skiprows=1)

# Initialize the directed graph
G = nx.Graph()

# Iterate through each row to build edges
for i, r in x.iterrows():
    source = str(r[0])  # Assuming the source node is in the first column
    for target in r[1:]:  # Iterate over the rest of the row for target nodes
        b = str(target)
        if b != 'nan' and b != source:  # Check if the target is not NaN
            G.add_edge(source, target)

pos = nx.spring_layout(G)  # Using spring layout

# Community detection
communities = nx.algorithms.community.modularity_max.greedy_modularity_communities(G)

# Visualize communities
plt.figure(figsize=(12, 12))
colors = ['r', 'g', 'b', 'c', 'm', 'y']  # Define colors for nodes in different communities
index = 0  # Start an index counter at 0
for community in communities:
    nx.draw_networkx_nodes(G, pos, nodelist=community, node_color=colors[index % len(colors)], label=f'Community {index + 1}')
    index += 1  # Increment index manually
nx.draw_networkx_edges(G, pos, width=0.5, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=8)
plt.title('Collaboration Network with Community Detection')
plt.legend()
plt.show()

index = 0  # Reset index for analysis
for community in communities:
    print(f"Community {index + 1}: Size = {len(community)}, Members = {list(community)}")
    index += 1
