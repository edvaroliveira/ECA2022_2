class Pessoa:
    def setNome(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome

    def setIdade(self, idade):
        self._idade = idade

    def getIdade(self):
        return self._idade

andre = Pessoa()
andre.setNome("André")
andre.setIdade(40)
print(f"Meu nome é {andre.getNome()} e tenho {andre.getIdade()} anos.")
