# arquivo.py
def lerMatrizesArquivo(arquivo):
    with open(arquivo, 'r') as file:
        linhas = file.readlines()

    matrizes = []
    matriz_atual = []
    for linha in linhas:
        if linha.strip():  # Verifica se a linha não está em branco
            matriz_atual.append([int(valor) for valor in linha.split()])
        else:
            if matriz_atual:  # Verifica se há uma matriz válida
                matrizes.append(matriz_atual)
                matriz_atual = []

    if matriz_atual:  # Adiciona a última matriz, se existir
        matrizes.append(matriz_atual)

    return matrizes

def escolherMatriz(matrizes):
    for i, matriz in enumerate(matrizes):
        print(f"\nMatriz {i+1}:")
        for linha in matriz:
            print(linha)

    print("Escolha uma matriz:")
    for i, matriz in enumerate(matrizes):
        print(f"Matriz {i + 1}")

    escolha = int(input("Digite o número da matriz desejada: "))
    if 1 <= escolha <= len(matrizes):
        return matrizes[escolha - 1]
    else:
        print("Escolha inválida. Tente novamente.")
        return escolherMatriz(matrizes)
