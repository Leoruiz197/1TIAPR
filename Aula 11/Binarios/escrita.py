numeros = [1,2,3,4,5,6,7,8,9,10]

caminho_arquivo = 'dados.bin'

with open(caminho_arquivo, mode='wb') as arquivo_binario:
    for numero in numeros:
        arquivo_binario.write(numero.to_bytes(4, byteorder='little'))

print("Arquivo criado com sucesso!")