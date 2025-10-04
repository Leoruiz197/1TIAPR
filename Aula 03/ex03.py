matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]

transposta = []

for j in range(len(matriz[0])):
    nova_linha = []
    for i in range(len(matriz)):
        nova_linha.append(matriz[i][j])
    transposta.append(nova_linha)

for linha in transposta:
    print(linha)