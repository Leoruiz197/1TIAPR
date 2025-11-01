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

    def comparar_idade(self, outra_pessoa):
        if self.idade > outra_pessoa.idade:
            return f"{self.nome} é mais velho(a) que {outra_pessoa.nome}."
        elif self.idade < outra_pessoa.idade:
            return f"{self.nome} é mais novo(a) que {outra_pessoa.nome}."
        else:
            return f"{self.nome} e {outra_pessoa.nome} têm a mesma idade."


p1 = Pessoa("Alice", 30, 65, 1.7, "Feminino")
p2 = Pessoa("Bob", 25, 80, 1.8, "Masculino")
p3 = Pessoa("Charlie", 30, 75, 1.75, "Masculino")
p4 = Pessoa("Diana", 40, 60, 1.65, "Feminino")
p5 = Pessoa("Eve", 20, 55, 1.6, "Feminino")

for pessoa in [p1, p2, p3, p4, p5]:
    print(pessoa.descrever())