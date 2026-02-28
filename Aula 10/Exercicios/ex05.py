nome_arquivo = input("Digite o nome do arquivo: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
else:
    print(f"O arquivo '{nome_arquivo}' contém {len(linhas)} linhas.")
