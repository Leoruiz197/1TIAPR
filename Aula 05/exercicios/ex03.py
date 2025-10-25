palavra = input("Digite uma palavra a ser buscada: ")

with open("./texto.txt", "r") as arquivo:
    
    linha = arquivo.readline()
    numero_linha = 1
    encontrou = False
    while linha:
        if palavra in linha:
            print(f"A palavra '{palavra}' foi encontrada na linha {numero_linha}: {linha.strip()}")
            encontrou = True
        linha = arquivo.readline()
        numero_linha += 1

    if not encontrou:
        print(f"A palavra '{palavra}' não foi encontrada no arquivo.")


