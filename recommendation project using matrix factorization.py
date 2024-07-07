import pandas as pd
import networkx as nx
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
x = pd.read_csv('project_data.csv', header=None, skiprows=1)

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
for i, r in x.iterrows():
    source = str(r[0])  # Convert the source to a string
    for target in r[1:]:  # Iterate through the targets
        target = str(target)
        if target != 'nan' and target != source:  # Skip 'nan' values and self-loops
            G.add_edge(source, target)

# Get the list of nodes
nodes = list(G.nodes())

# Convert the graph to an adjacency matrix
X = nx.to_numpy_array(G, dtype=int)

# Transform the adjacency matrix
for i in range(len(X)):
    for j in range(len(X)):
        if X[i][j] == 1 and X[j][i] == 0:
            X[j][i] = -1

print(X)

# Set parameters
k = 10  # Number of latent features
alpha = 0.002  # Learning rate
beta = 0.2  # Regularization parameter
iterations = 100

# Initialize U and V
U = np.random.rand(len(X), k)
V = np.random.rand(k, len(X[0]))

# Matrix factorization using gradient descent
total_error_list = []
for iter in range(iterations):
    for i in range(len(X)):
        for j in range(len(X[0])):
            if X[i, j] != 0:
                error = X[i, j] - np.dot(U[i, :], V[:, j])
                total_error = error**2 + beta * (np.sum(U**2) + np.sum(V**2))
                total_error_list.append(total_error)
                for r in range(k):
                    U[i, r] += alpha * (2 * error * V[r, j] - beta * U[i, r])
                    V[r, j] += alpha * (2 * error * U[i, r] - beta * V[r, j])

# Compute the predicted matrix
predicted_matrix = np.dot(U, V)

# Threshold to determine predicted impressions
threshold = 0.88
#if the predicted value is greater than the threshold, it is considered as an impression
predicted_impressions = (predicted_matrix > threshold).astype(int)
print(predicted_impressions)

# Collect predicted links
predicted_links = []
for i in range(len(X)):
    for j in range(len(X[0])):
        if X[i, j] == 0 and predicted_impressions[i, j] > 0:
            predicted_links.append((nodes[i], nodes[j], predicted_matrix[i, j]))

# Print predicted links
for link in predicted_links:
    print(f"Predicted link from {link[0]} to {link[1]} with confidence {link[2]:.4f}")

'''# Optionally visualize the predicted links or further analyze the results
plt.figure(figsize=(12, 8))
sns.heatmap(predicted_matrix, cmap='coolwarm', xticklabels=False, yticklabels=False)
plt.title("Predicted Matrix")
plt.show()'''


import matplotlib.pyplot as plt
# Plot the total error vs. iterations
plt.figure(figsize=(12, 8))
plt.plot(total_error_list)

plt.xlabel('Iterations')
plt.ylabel('Total Error')
plt.title('Total Error vs. Iterations')
plt.show()

