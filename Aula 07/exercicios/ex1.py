class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo

    def descrever(self):
        return f"Pessoa(nome={self.nome}, idade={self.idade}, peso={self.peso}, altura={self.altura}, sexo={self.sexo})"