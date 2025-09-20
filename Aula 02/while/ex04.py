acumulador = 0

num = int(input("Digite um número: "))
while num >= 0:
    acumulador += num
    num = int(input("Digite um número: "))
print(f"A soma dos números é: {acumulador}")