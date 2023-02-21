class Pessoa:
    def setIdade(self, idade):
        self.idade = idade

    def getIdade(self):
        return self.idade

andre = Pessoa()
andre.setIdade(40)
print(andre.getIdade())

print(andre.idade)