import networkx as nx
import matplotlib.pyplot as plt

# Inicializando a Classe de Grafo
class Graph:
    def __init__(self):
        self.graph = []
        self.nodes = set()
        self.MST = []

    def addEdge(self, s, d, w):
        self.graph.append((s, d, w))
        self.nodes.add(s)
        self.nodes.add(d)

    def printGraph(self, edges):
        G = nx.Graph()
        G.add_weighted_edges_from(edges)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        edge_weight = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)
        plt.show()

    def printMST(self, result):
        G = nx.Graph()
        G.add_weighted_edges_from(result)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        edge_weight = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)
        plt.title('Minimum Spanning Tree (Kruskal)')
        plt.show()
    
    def kruskalAlgo(self):
        ds = DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        e = 0
        for edge in self.graph:
            s, d, w = edge
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                e += 1
                self.MST.append((s, d, w))
                ds.union(x, y)
                if e == len(self.nodes) - 1:
                    break
        self.printMST(self.MST)

# Implementando a estrutura de dados Conjunto Disjunto e suas funções
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

g = Graph()
   
g.addEdge('B', 'C', 1)
g.addEdge('A', 'C', 2)
g.addEdge('D', 'F', 2)
g.addEdge('A', 'B', 4)
g.addEdge('B', 'E', 4)
g.addEdge('E', 'C', 5)
g.addEdge('C', 'F', 6)
g.addEdge('A', 'D', 6)
g.addEdge('C', 'D', 7)
g.addEdge('E', 'F', 7)
g.addEdge('B', 'D', 9)

g.printGraph(g.graph)
g.kruskalAlgo()