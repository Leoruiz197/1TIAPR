class Pessoa:
    especie = "Humano"

    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
    
    def __str__(self):
        return f"Pessoa(nome={self.nome}, idade={self.idade}, peso={self.peso}, altura={self.altura}, sexo={self.sexo})"

p1 = Pessoa("João", 25, 70, 1.75, "Masculino")
p2 = Pessoa("Maria", 30, 60, 1.65, "Feminino")
p3 = Pessoa("Carlos", 28, 80, 1.80, "Masculino")

print(p1.especie)
print(p2)
print(p3)

print(f"Nome: {p1.nome}, Idade: {p1.idade}, Peso: {p1.peso}, Altura: {p1.altura}, Sexo: {p1.sexo}")
print(f"Nome: {p2.nome}, Idade: {p2.idade}, Peso: {p2.peso}, Altura: {p2.altura}, Sexo: {p2.sexo}")
print(f"Nome: {p3.nome}, Idade: {p3.idade}, Peso: {p3.peso}, Altura: {p3.altura}, Sexo: {p3.sexo}")

for atributo in vars(p1):
    print(f"{atributo}: {getattr(p1, atributo)}")

