matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

matriz_soma = []

for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[i])):
        linha.append(matriz[i][j] + matriz2[i][j])
    matriz_soma.append(linha)

for linha in matriz_soma:
    for elemento in linha:
        print(f"{elemento:4}", end="")
    print()