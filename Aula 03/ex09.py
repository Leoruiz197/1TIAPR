matriz = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

simetrica = True

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break
    if not simetrica:
        break

if simetrica:
    print("A matriz é simétrica.")
else:
    print("A matriz não é simétrica.")