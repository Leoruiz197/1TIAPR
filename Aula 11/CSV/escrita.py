import csv

# Caminho do arquivo CSV
caminho_arquivo = 'novo_exemplo.csv'

# Dados para serem escritos no CSV
dados = [
    ['Nome', 'Idade', 'Profissão', 'Cidade', 'País'],
    ['João', '30', 'Engenheiro', 'São Paulo', 'Brasil'],
    ['Maria', '25', 'Médica', 'Lisboa', 'Portugal'],
    ['Carlos', '40', 'Professor', 'Madrid', 'Espanha'],
    ['Ana', '35', 'Arquiteta', 'Paris', 'França'],
    ['Renato', '37', 'garoto de programa', 'Recife', 'Pernambuco']
]

# Escrevendo no arquivo CSV
with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    # Iterando sobre os dados e escrevendo no arquivo
    for linha in dados:
        escritor_csv.writerow(linha)

print(f"Arquivo '{caminho_arquivo}' criado com sucesso.")
