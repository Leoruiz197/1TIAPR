arquivo1 = "arq1.txt"
arquivo2 = "arq2.txt"

with open(arquivo1, 'r') as arq1, open(arquivo2, 'r') as arq2:
    conteudo1 = arq1.read()
    conteudo2 = arq2.read()

with open("arquivo_combinado.txt", 'w') as arq_combinado:
    arq_combinado.write(conteudo1 + "\n" + conteudo2)

print("Arquivos combinados com sucesso em 'arquivo_combinado.txt'")