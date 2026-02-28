import json

caminho_arquivo = 'dados.json'

with open(caminho_arquivo, mode='r', newline='',encoding='utf-8') as arquivo_json:
    dados =  json.load(arquivo_json)

for pessoa in dados['pessoas']:
    nome = pessoa['nome']
    print(pessoa)
    print(f"Nome: {nome}")