#matriz inversa

matriz = [
    [4, 3],
    [2, 1]
]

a , b = matriz[0]
c , d = matriz[1]

det = a * d - b * c

if det == 0:
    print("A matriz não é inversível")

inversa = [
    [d/det, -b/det],
    [-c/det, a/det]
]

print(inversa)