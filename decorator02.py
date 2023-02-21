class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    @property
    def nomecompleto(self):
        return self.nome + ' ' + self.sobrenome


andre = Pessoa("André", "Marista")
print(andre.nomecompleto)