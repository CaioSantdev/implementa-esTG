# grafo.py
import networkx as nx
import matplotlib.pyplot as plt
from algoritmos import bfs

class Grafo:
    def __init__(self, vertices, matriz):
        self.vertices = vertices
        self.grafo = matriz

    def mostrarMatriz(self):
        print("Matriz de adjacência escolhida:")
        for linha in self.grafo: 
            print(linha)
    
    

    def plotarGrafo(self):
        G = nx.Graph()
        for i in range(self.vertices):
            G.add_node(i + 1)

        for i in range(self.vertices):
            for j in range(i + 1, self.vertices):
                if self.grafo[i][j] == 1:
                    G.add_edge(i + 1, j + 1)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=500, edge_color='gray', font_color='black', font_size=8)
        plt.title("Grafo")

        plt.show()

        while True:
            escolha = input("Escolha uma opção: \n1. verificar se o grafo é conexo\n2. Aplicar Busca em Largura\n3. Encontrar Bipartição\n4. Sair\n")

            if escolha == "1":
                print("Verificando se o grafo é conexo...\n")
                self.verificarConexo()
            elif escolha == "2":
                print("Aplicando Busca em Largura...\n")
                self.aplicarBuscaEmLargura()
            elif escolha == "3":
                print("Encontrando bipartição...\n")
                biparticao = self.encontrarBiparticao()
                self.mostrarBiparticao(biparticao)
            elif escolha == "4":
                print("Saindo do menu principal...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def verificarConexo(self):
        componentes_conexas = self.encontrarComponentesConexas()

        if len(componentes_conexas) == 1:
            print("SIM, o grafo é conexo!")
            print("Vértices do grafo:")
            for vertice in range(self.vertices):
                print(vertice + 1)
        else:
            print(f"NÃO, o grafo não é conexo. Componentes conexas:")
            for i, componente in enumerate(componentes_conexas, start=1):
                componente_ajustado = [v + 1 for v in componente]
                print(f"Componente {i}: {componente_ajustado}")

    def encontrarComponentesConexas(self):
        visitados = set()
        componentes_conexas = []

        for vertice in range(self.vertices):
            if vertice not in visitados:
                componente_conexa = bfs(self.grafo, vertice)
                componentes_conexas.append(componente_conexa)
                visitados.update(componente_conexa)

        return componentes_conexas
 
    def aplicarBuscaEmLargura(self):
        print("Vértices candidatos para a busca em largura:")
        for vertice in range(1, self.vertices + 1):
            print(vertice, end=' ')
        print()

        raiz = int(input("Qual será o vértice raiz da busca? "))
        vertices_candidatos = [v + 1 for v in range(self.vertices) if self.grafo[raiz - 1][v] == 1] #vértices diretamente alcançaveis
        print(f"Vértices candidatos diretamente alcançáveis a partir do vértice {raiz}: {vertices_candidatos}")

        visitados, arvore_bfs = bfs(self.grafo, raiz - 1, retornarArvore=True)

        print("Vértices visitados durante a busca em largura:")
        for vertice in visitados:
            print(vertice + 1)

        # Criar um grafo representando a árvore de busca em largura
        G_arvore = nx.DiGraph()
        for v in range(self.vertices):
            G_arvore.add_node(v + 1)

        for vertice, pai in enumerate(arvore_bfs):
            if pai is not None:
                G_arvore.add_edge(pai + 1, vertice + 1)

        # Exibir o grafo da árvore de busca em largura
        pos = nx.kamada_kawai_layout(G_arvore)
        nx.draw(G_arvore, pos, with_labels=True, node_size=500, edge_color='gray', font_color='black', font_size=8, arrowsize=15, connectionstyle="arc3,rad=0.1")
        plt.title("Árvore de Busca em Largura")
        plt.show()

    def encontrarBiparticao(self):
        cor = [None] * self.vertices
        bipartido = True

        for raiz in range(self.vertices):
            if cor[raiz] is None:
                cor[raiz] = 0  # Inicializa a cor da raiz

                visitados, _ = bfs(self.grafo, raiz, retornarArvore=True)
                for vertice in visitados:
                    for vizinho, adjacencia in enumerate(self.grafo[vertice]):
                        if adjacencia:
                            if cor[vizinho] is None:
                                cor[vizinho] = 1 - cor[vertice] if cor[vertice] is not None else 0
                            elif cor[vizinho] == cor[vertice]:
                                bipartido = False
                                break

        return bipartido, cor

    def mostrarBiparticao(self, conjuntos):
        bipartido, cor = conjuntos

        if bipartido:
            print("SIM, o grafo é bipartido!")
            print("Conjunto 1:", [v + 1 for v in range(self.vertices) if cor[v] == 0])
            print("Conjunto 2:", [v + 1 for v in range(self.vertices) if cor[v] == 1])
        else:
            print("\tImpossível encontrar bipartição pois o Grafo NÃO é bipartido!")