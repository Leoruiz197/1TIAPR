import random

tentativas = 3
numero = random.randint(1, 10)
# numero = 7

while tentativas > 0:
    palpite = int(input("Digite um número entre 1 e 10: "))
    if palpite == numero:
        print("Parabéns! Você acertou.")
        break
    else:
        tentativas -= 1
        print(f"Você errou. Tentativas restantes: {tentativas}")
print(f"O número correto era: {numero}")