class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class ProdutoEletronico(Produto):
    def __init__(self, nome, preco, voltagem, marca):
        super().__init__(nome, preco)
        self.voltagem = voltagem
        self.marca = marca
    
    def ligar(self):
        print(f"O produto: {self.nome}, esta ligando...")

class ProdutoAlimenticio(Produto):
    def __init__(self, nome, preco, validade, peso):
        super().__init__(nome, preco)
        self.validade = validade
        self.peso = peso
    
    def verificarValidade(self):
        print(f"Este produto esta valido até dia {self.validade}")


macarrao = ProdutoAlimenticio("Espaguete",10.5,"24/05/2026",500)
macarrao.verificarValidade()