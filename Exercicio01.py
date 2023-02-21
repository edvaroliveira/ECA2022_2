class Funcionario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def funcDependente(self, dependente):
        self.dependente = dependente

class Dependente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def depFuncionario(self, funcionario):
        self.funcionario = funcionario

f1 = Funcionario("Alice", 90)
d1 = Dependente("Matice", 9)
f1.funcDependente(d1)
print(f1.nome)
print(f1.idade)
print(f1.dependente.nome)
print(f1.dependente.idade)
d1.depFuncionario(f1)
print(d1.nome)
print(d1.idade)
print(d1.funcionario.nome)
print(d1.funcionario.idade)


