lista = ["maçã", "banana", "laranja", "uva", "pera", "abacaxi", "manga", "morango", "kiwi", "melancia"]

with open("./aula 05/frutas.txt", "w", encoding="UTF-8") as arquivo:
    for fruta in lista:
        arquivo.write(fruta + "\n")

print("Lista salva em frutas.txt")

