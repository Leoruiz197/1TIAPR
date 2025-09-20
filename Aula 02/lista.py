lista_mercado = []
lista_mercado.append('banana')
lista_mercado.append('maçã')
lista_mercado.append('laranja')
lista_mercado.insert(1, 'uva')
lista_mercado.append('maçã')
lista_mercado.append('maçã')
lista_mercado.append('maçã')
lista_mercado.append('maçã')
lista_mercado.append('maçã')

lista_mercado.remove('maçã')

lista_mercado.pop(5)

# lista_mercado.clear()

print(lista_mercado.index('maçã'))
print(lista_mercado.count('maçã'))

lista_mercado.sort()
lista_mercado.reverse()

lista_mercado.append(input('Digite um item: '))
print(lista_mercado[1])

