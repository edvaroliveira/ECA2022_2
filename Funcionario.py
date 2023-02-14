class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


    def reajuste(self, tipo, valor):

        if(tipo == 1):
            self.salario = self.salario * (1 + (valor/100))
        else:
            self.salario = self.salario * (1 - (valor / 100))

    def mostrarSalario(self):
        return self.salario
