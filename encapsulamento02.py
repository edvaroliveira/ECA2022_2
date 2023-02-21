class Pessoa:
    def setIdade(self, idade):
        self._idade = idade

    def getIdade(self):
        return self._idade

andre = Pessoa()
andre.setIdade(40)
print(andre.getIdade())

print(andre.idade)