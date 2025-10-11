lista = [10, 20, 30, 40, 50]

def media_lista(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)
 
media = media_lista(lista)
print(f"A média dos números na lista é: {media}")