def saudar(nome):
    print(f"Olá, {nome}!")

saudar("João")

def saudar2(nome):
    return f"Olá, {nome}!"

print(saudar2("Maria"))

def soma(a, b):
    return a + b
    

resultado = soma(3, 5)
print(f"A soma é: {resultado}")