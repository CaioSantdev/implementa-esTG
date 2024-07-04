import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = np.zeros((vertices, vertices))

    def adicionarAresta(self, u, v, peso):
        self.grafo[u-1][v-1] = peso
        self.grafo[v-1][u-1] = peso

def prim(grafo):
    vertices = grafo.shape[0]
    visitado = [False] * vertices
    contagem_arestas = 0
    visitado[0] = True
    arestas = []
    peso_total = 0

    while contagem_arestas < vertices - 1:
        peso_minimo = float('inf')
        u = -1
        v = -1

        for i in range(vertices):
            if visitado[i]:
                for j in range(vertices):
                    if not visitado[j] and 0 < grafo[i][j] < peso_minimo:
                        peso_minimo = grafo[i][j]
                        u = i
                        v = j

        if u != -1 and v != -1:
            arestas.append((u+1, v+1, peso_minimo))  # Ajustar índices para vértices baseados em 1
            peso_total += peso_minimo
            visitado[v] = True
            contagem_arestas += 1

    return arestas, peso_total

# Cria uma instância do grafo com 6 vértices
g = Grafo(6)

# Adiciona arestas com pesos
g.adicionarAresta(1, 6, 1)
g.adicionarAresta(2, 6, 2)
g.adicionarAresta(3, 6, 2)
g.adicionarAresta(5, 6, 4)
g.adicionarAresta(4, 6, 6)
g.adicionarAresta(1, 2, 6)
g.adicionarAresta(1, 3, 5)
g.adicionarAresta(3, 5, 4)
g.adicionarAresta(2, 4, 5)
g.adicionarAresta(4, 5, 3)

# Cria um grafo networkx a partir das arestas do grafo original
original_G = nx.Graph()
for u in range(g.vertices):
    for v in range(u + 1, g.vertices):
        if g.grafo[u][v] > 0:
            original_G.add_edge(u+1, v+1, weight=g.grafo[u][v])  # Ajustar índices para vértices baseados em 1

# Plota o grafo original
pos = nx.spring_layout(original_G)  # posições para todos os nós
plt.figure(figsize=(12, 6))

plt.subplot(121)
nx.draw_networkx_nodes(original_G, pos, node_size=700)
nx.draw_networkx_edges(original_G, pos, width=2)
nx.draw_networkx_labels(original_G, pos, font_size=20, font_family="sans-serif")
edge_labels = {(u, v): d["weight"] for u, v, d in original_G.edges(data=True)}
nx.draw_networkx_edge_labels(original_G, pos, edge_labels=edge_labels, font_size=12)
plt.title("Grafo Original")
plt.axis("off")

# Calcula a árvore geradora mínima usando o algoritmo de Prim
arvore_geradora_minima, peso_total = prim(g.grafo)

# Cria um grafo networkx a partir das arestas da árvore geradora mínima
mst_G = nx.Graph()
for u, v, peso in arvore_geradora_minima:
    mst_G.add_edge(u, v, weight=peso)

# Plota a árvore geradora mínima
plt.subplot(122)
nx.draw_networkx_nodes(mst_G, pos, node_size=700)
nx.draw_networkx_edges(mst_G, pos, width=2)
nx.draw_networkx_labels(mst_G, pos, font_size=20, font_family="sans-serif")
edge_labels = {(u, v): d["weight"] for u, v, d in mst_G.edges(data=True)}
nx.draw_networkx_edge_labels(mst_G, pos, edge_labels=edge_labels, font_size=12)
plt.title("Árvore Geradora Mínima")
plt.axis("off")

plt.show()
