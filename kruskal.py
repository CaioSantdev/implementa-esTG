import networkx as nx
import matplotlib.pyplot as plt

# Inicializando a Classe de Grafo
class Grafo:
    def __init__(self):
        self.grafo = []
        self.nos = set()
        self.AGM = []  # Árvores Geradora Mínima

    def adicionarAresta(self, s, d, p):
        self.grafo.append((s, d, p))
        self.nos.add(s)
        self.nos.add(d)

    def imprimirGrafo(self, arestas):
        G = nx.Graph()
        G.add_weighted_edges_from(arestas)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        pesos_arestas = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos_arestas)
        plt.show()

    def imprimirAGM(self, resultado):
        G = nx.Graph()
        G.add_weighted_edges_from(resultado)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        pesos_arestas = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos_arestas)
        plt.title('Árvore Geradora Mínima (Kruskal)')
        plt.show()
    
    def algoritmoKruskal(self):
        cj = ConjuntoDisjunto(self.nos)
        self.grafo = sorted(self.grafo, key=lambda item: item[2])
        e = 0
        for aresta in self.grafo:
            s, d, p = aresta
            x = cj.encontrar(s)
            y = cj.encontrar(d)
            if x != y:
                e += 1
                self.AGM.append((s, d, p))
                cj.unir(x, y)
                if e == len(self.nos) - 1:
                    break
        self.imprimirAGM(self.AGM)

# Implementando a estrutura de dados Conjunto Disjunto e suas funções
class ConjuntoDisjunto:
    def __init__(self, vertices):
        self.pai = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def encontrar(self, item):
        if self.pai[item] != item:
            self.pai[item] = self.encontrar(self.pai[item])
        return self.pai[item]
    
    def unir(self, x, y):
        raiz_x = self.encontrar(x)
        raiz_y = self.encontrar(y)
        if self.rank[raiz_x] < self.rank[raiz_y]:
            self.pai[raiz_x] = raiz_y
        elif self.rank[raiz_x] > self.rank[raiz_y]:
            self.pai[raiz_y] = raiz_x
        else:
            self.pai[raiz_y] = raiz_x
            self.rank[raiz_x] += 1

# Criação do grafo e adição das arestas
g = Grafo()
g.adicionarAresta('B', 'C', 1)
g.adicionarAresta('A', 'C', 2)
g.adicionarAresta('D', 'F', 2)
g.adicionarAresta('A', 'B', 4)
g.adicionarAresta('B', 'E', 4)
g.adicionarAresta('E', 'C', 5)
g.adicionarAresta('C', 'F', 6)
g.adicionarAresta('A', 'D', 6)
g.adicionarAresta('C', 'D', 7)
g.adicionarAresta('E', 'F', 7)
g.adicionarAresta('B', 'D', 9)

# Impressão do grafo original e da AGM
g.imprimirGrafo(g.grafo)
g.algoritmoKruskal()
