class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo

    def descrever(self):
        return f"Pessoa(nome={self.nome}, idade={self.idade}, peso={self.peso}, altura={self.altura}, sexo={self.sexo})"
    
    def envelhecer(self, anos=1):
        self.idade += anos


p1 = Pessoa("Ana", 20, 65, 1.70, "Feminino")
print(p1.descrever())
p1.envelhecer(3)
print(p1.descrever())

