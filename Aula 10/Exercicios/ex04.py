try:
    numerador = float(input("Digite o numerador: "))
    denominador = float(input("Digite o denominador: "))
    resultado = numerador / denominador
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Por favor, insira números válidos.")
else:
    print(f"Resultado: {resultado}")
    print("Divisão realizada com sucesso.")
