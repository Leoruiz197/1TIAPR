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

print(p1.comparar_idade(p2))