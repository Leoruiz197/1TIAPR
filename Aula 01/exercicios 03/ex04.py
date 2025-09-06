vogais = ['a', 'e', 'i', 'o', 'u']

caracter = input("Digite um caractere: ")

if caracter in vogais:
    print(f"O caractere '{caracter}' é uma vogal.") 
else:
    print(f"O caractere '{caracter}' não é uma vogal.")
