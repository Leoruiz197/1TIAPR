# matriz verifica se é identidade

matriz = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

validador = True

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j and matriz[i][j] != 1:
            validador = False
            break
        elif i != j and matriz[i][j] != 0:
            validador = False
            break
    if not validador:
        break

if validador:
    print("É identidade")  
else:
    print("Não é identidade")