produto = 55
quantidade = int(input("Digite a quantidade desejada: "))
total = produto * quantidade

if quantidade > 10:
    total *= 0.9  # Aplica desconto de 10%
    print("Desconto de 10% aplicado, Valor total com desconto: R$", total)
else:
    print("Valor total: R$", total)
