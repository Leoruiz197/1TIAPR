try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
except ValueError:
    print("Erro: Entrada inválida. Por favor, insira números inteiros.")
else:
    soma = num1 + num2
    print(f"A soma dos números é: {soma}")
