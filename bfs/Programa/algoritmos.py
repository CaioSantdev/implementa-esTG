# algoritmos.py
def bfs(matriz_adjacencia, inicio, retornarArvore=False):
    visitados = set()
    fila = [inicio]
    visitados.add(inicio)
    arvore_bfs = [None] * len(matriz_adjacencia)

    while fila:
        vertice = fila.pop(0)

        for vizinho, adjacencia in enumerate(matriz_adjacencia[vertice]):
            if adjacencia and vizinho not in visitados: # Verifica se há uma aresta != 0 e se o vizinho já foi visitado
                visitados.add(vizinho)
                fila.append(vizinho)
                arvore_bfs[vizinho] = vertice  # Registra o pai do vizinho na árvore

    if retornarArvore:
        return visitados, arvore_bfs
    else:
        return visitados