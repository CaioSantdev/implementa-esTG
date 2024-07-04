# main.py
from Grafo import Grafo
from arquivo import lerMatrizesArquivo, escolherMatriz

arquivo = r"c:\Users\Caio\Desktop\TG\Implementaçoes\bfs\Programa\grafo.txt"
print(arquivo)
matrizes = lerMatrizesArquivo(arquivo)

if matrizes:
    op = True
    while op:
        matriz_escolhida = escolherMatriz(matrizes)
        vertices = len(matriz_escolhida)
        g = Grafo(vertices, matriz_escolhida)
        g.mostrarMatriz()
        g.plotarGrafo()
        op2 = input("Deseja ler outro grafo?\n\t1. sim\n\t2. não\n")
        if op2 == "1":
            op = True
        elif op2 == "2":
            op = False
        else:
            print("Opção inválida")
else:
    print("Nenhuma matriz encontrada no arquivo.")