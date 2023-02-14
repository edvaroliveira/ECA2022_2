class Endereco:
    def __init__(self, rua, n_casa):
        self.rua = rua
        self.n_casa = n_casa

    def meuEndereco(self):
        return "Moro na rua "+ str(self.rua) + " na casa número " + str(self.n_casa)


class Aluno:

    def __init__(self, nome, email, rua, casa):
        self.nome = nome
        self.email = email
        self.obj_endereco = Endereco(rua, casa)

    def meusDados(self):
        return self.obj_endereco.meuEndereco()

aluno1 = Aluno("André", "andres2maristinha@", "doca", 1)
print(aluno1)
print(aluno1.meusDados())
