caminho_arquivo = "./fiap.pdf"
try:
    with open(caminho_arquivo, 'rb') as arquivo:
        conteudo = arquivo.read()
        hex_dados = conteudo.hex().upper()
        
        for i in range(0, len(hex_dados), 2):
            print(hex_dados[i:i+2], end=' ')

except:
    print("Erro")