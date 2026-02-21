class Animal:
    def __init__(self, nome: str, raca: str, idade: int):
        self.nome = nome
        self.raca = raca
        self.idade = idade

class Cachorro(Animal):
    def __init__(self, nome: str, raca: str, idade: int, porte: str):
        super().__init__(nome, raca, idade)
        self.porte = porte

class Gato(Animal):
    def __init__(self, nome, raca, idade, cor):
        super().__init__(nome, raca, idade)
        self.cor = cor

class Passaro(Animal):
    def __init__(self, nome, raca, idade, envergadura):
        super().__init__(nome, raca, idade)
        self.envergadura = envergadura

cachorro = Cachorro("Rex","Pitbull",12,"Médio")
print(cachorro.nome)