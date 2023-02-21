class Pessoa:
    def __init__(self, nome, sobrenome):
        self._nome = nome
        self.sobrenome = sobrenome

    @property
    def nomecompleto(self):
        return self._nome + ' ' + self.sobrenome

    #getter
    @property
    def nome(self):
        return self._nome

    #setter
    @nome.setter
    def nome(self, nome):
        self._nome = nome


andre = Pessoa("André", "Marista")
print(andre.nomecompleto)
print(andre.nome)
andre.nome = "Carina"
print(andre.nomecompleto)
