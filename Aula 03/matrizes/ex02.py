matriz = [
    [1, 2],
    [3, 4]
]

escalar = 3

resultado = []
for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[i])):
        linha.append(matriz[i][j] * escalar)
    resultado.append(linha)

for linha in resultado:
    print(linha)