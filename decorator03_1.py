class Pessoa:
    def __init__(self, nome, sobrenome):
        self._nome = nome
        self._sobrenome = sobrenome

    @property
    def nomecompleto(self):
        return self._nome + ' ' + self._sobrenome

    #getter
    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return self._sobrenome


    #setter
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome


andre = Pessoa("André", "Marista")
print(andre.nomecompleto)
print(andre.nome)
andre.nome = "Carina"
print(andre.nomecompleto)
andre.sobrenome = "Trindade"
andre.nome = "André"
print(andre.nomecompleto)