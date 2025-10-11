def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

resultado_soma = soma(10, 5)
resultado_subtrai = subtrai(10, 5) 
resultado_multiplica = multiplica(10, 5)
resultado_divide = divide(10, 5)

print("Soma: ", resultado_soma)
print("Subtração: ", resultado_subtrai) 
print("Multiplicação: ", resultado_multiplica)
print("Divisão: ", resultado_divide)