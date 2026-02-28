import csv

# Caminho do arquivo CSV
caminho_arquivo = 'exemplo.csv'

# Lendo o arquivo CSV
with open(caminho_arquivo, mode='r', newline='',encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    
    # Iterando sobre as linhas do CSV
    for linha in leitor_csv:
        # Supondo que o arquivo tenha 5 colunas
        coluna1, coluna2, coluna3, coluna4, coluna5 = linha
        print(f"Coluna 1: {coluna1}, Coluna 2: {coluna2}, Coluna 3: {coluna3}, Coluna 4: {coluna4}, Coluna 5: {coluna5}")
