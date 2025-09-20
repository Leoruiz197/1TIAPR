num = int(input("Digite um número par: "))
while num % 2 != 0:
    print("Número inválido!")
    num = int(input("Digite um número par: "))
print(f"Obrigado! {num} é um número par.")