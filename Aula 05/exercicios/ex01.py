arquivo = "texto.txt"

with open(arquivo, "r") as f:
    conteudo = f.read()
    palavras = conteudo.split()
    num_palavras = len(palavras)

print(f"O arquivo '{arquivo}' contém {num_palavras} palavras.")