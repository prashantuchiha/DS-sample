import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Number of nodes in the network
n = 50

# Degree of each node in the network
k = 4

# Create an empty adjacency matrix
adj_matrix = np.zeros((n, n))

# Connect each node to its k nearest neighbors in a ring topology
for i in range(n):
    for j in range(1, k//2+1):
        adj_matrix[i][(i-j)%n] = 1
        adj_matrix[i][(i+j)%n] = 1

# Connect each node to its k/2 random non-neighbors
for i in range(n):
    neighbors = set(np.where(adj_matrix[i] == 1)[0])
    non_neighbors = set(range(n)) - neighbors - {i}
    for j in np.random.choice(list(non_neighbors), k//2, replace=False):
        adj_matrix[i][j] = 1
        adj_matrix[j][i] = 1

# Print the adjacency matrix
print(adj_matrix)
G = nx.from_numpy_matrix(adj_matrix)

# Draw the graph
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
nx.draw_networkx_edges(G, pos, width=1, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
plt.axis('off')
plt.show()