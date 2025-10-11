def contarVogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in texto:
        if char in vogais:
            contador += 1
    return contador

frase = "Exemplo de frase para contar vogais."
num_vogais = contarVogais(frase)
print(f"Número de vogais na frase: {num_vogais}")