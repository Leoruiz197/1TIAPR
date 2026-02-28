lista = [10, 20, 30, 40, 50]

try:
    indice = int(input("Digite um índice: "))
    elemento = lista[indice]
    print(f"O elemento no índice {indice} é {elemento}.")
except IndexError:
    print("Erro: Índice fora do intervalo da lista.")
except ValueError:
    print("Erro: Por favor, insira um número inteiro válido.")
