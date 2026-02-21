class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario, tempoEmpresa):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario
        self.tempoEmpresa = tempoEmpresa

class Dependente(Pessoa):
    def __init__(self, nome, idade, escola, serie, responsavel):
        super().__init__(nome, idade)
        self.escola = escola
        self.serie = serie
        self.responsavel = responsavel

