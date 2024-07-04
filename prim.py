import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = np.zeros((vertices, vertices))

    def addEdge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

def prim(graph):
    vertices = graph.shape[0]
    visited = [False] * vertices
    edge_count = 0
    visited[0] = True
    edges = []
    total_weight = 0

    while edge_count < vertices - 1:
        min_weight = float('inf')
        u = -1
        v = -1

        for i in range(vertices):
            if visited[i]:
                for j in range(vertices):
                    if not visited[j] and 0 < graph[i][j] < min_weight:
                        min_weight = graph[i][j]
                        u = i
                        v = j

        if u != -1 and v != -1:
            edges.append((u, v, min_weight))
            total_weight += min_weight
            visited[v] = True
            edge_count += 1

    return edges, total_weight

# Create a graph instance with 6 vertices
g = Graph(6)

# Add edges with weights
g.addEdge(0, 5, 1)
g.addEdge(1, 5, 2)
g.addEdge(2, 5, 2)
g.addEdge(4, 5, 4)
g.addEdge(3, 5, 6)
g.addEdge(0, 1, 6)
g.addEdge(0, 2, 5)
g.addEdge(2, 4, 4)
g.addEdge(1, 3, 5)
g.addEdge(3, 4, 3)

# Create a networkx graph from the original graph edges
original_G = nx.Graph()
for u in range(g.vertices):
    for v in range(u + 1, g.vertices):
        if g.graph[u][v] > 0:
            original_G.add_edge(u, v, weight=g.graph[u][v])

# Plot the original graph
pos = nx.spring_layout(original_G)  # positions for all nodes
plt.figure(figsize=(12, 6))

plt.subplot(121)
nx.draw_networkx_nodes(original_G, pos, node_size=700)
nx.draw_networkx_edges(original_G, pos, width=2)
nx.draw_networkx_labels(original_G, pos, font_size=20, font_family="sans-serif")
edge_labels = {(u, v): d["weight"] for u, v, d in original_G.edges(data=True)}
nx.draw_networkx_edge_labels(original_G, pos, edge_labels=edge_labels, font_size=12)
plt.title("Original Graph")
plt.axis("off")

# Calculate minimum spanning tree using Prim's algorithm
min_spanning_tree, total_weight = prim(g.graph)

# Create a networkx graph from the minimum spanning tree edges
mst_G = nx.Graph()
for u, v, weight in min_spanning_tree:
    mst_G.add_edge(u, v, weight=weight)

# Plot the minimum spanning tree
plt.subplot(122)
nx.draw_networkx_nodes(mst_G, pos, node_size=700)
nx.draw_networkx_edges(mst_G, pos, width=2)
nx.draw_networkx_labels(mst_G, pos, font_size=20, font_family="sans-serif")
edge_labels = {(u, v): d["weight"] for u, v, d in mst_G.edges(data=True)}
nx.draw_networkx_edge_labels(mst_G, pos, edge_labels=edge_labels, font_size=12)
plt.title("Minimum Spanning Tree")
plt.axis("off")

plt.show()
