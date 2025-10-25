arquivo = "texto.txt"

linhas_original = []
linhas = []
with open(arquivo, "r", encoding = "utf-8") as f:
    linhas_original = f.readlines()
    linhas = sorted(linhas_original)

print("Linhas do arquivo Original:")
for linha in linhas_original:
    print(linha.strip())

print("Linhas do arquivo em ordem alfabética:")
for linha in linhas:
    print(linha.strip())