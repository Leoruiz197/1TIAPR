def fatorial(num):
    if num < 0:
        return "Erro: Número negativo"
    elif num == 0 or num == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, num + 1):
            resultado *= i
        return resultado
    
numero = 5
fatorial_numero = fatorial(numero) 
print(f"O fatorial de {numero} é: {fatorial_numero}")