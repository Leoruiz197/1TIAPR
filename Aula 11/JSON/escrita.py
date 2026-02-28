import json

dados = {
    "pessoas": [
        {
            "nome": "João",
            "idade": 30,
            "profissao": "Engenheiro",
            "cidade": "São Paulo",
            "pais": "Brasil"
        },
        {
            "nome": "Maria",
            "idade": 25,
            "profissao": "Médica",
            "cidade": "Lisboa",
            "pais": "Portugal"
        },
        {
            "nome": "Carlos",
            "idade": 40,
            "profissao": "Professor",
            "cidade": "Madrid",
            "pais": "Espanha"
        },
        {
            "nome": "Ana",
            "idade": 35,
            "profissao": "Arquiteta",
            "cidade": "Paris",
            "pais": "França"
        }
    ]
}

caminho_arquivo = 'novos_dados.json'

with open(caminho_arquivo, mode='w') as arquivo_json:
    json.dump(dados, arquivo_json, indent = 2)
print("Arquivo foi criado com sucesso!")