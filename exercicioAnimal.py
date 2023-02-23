class Animal:

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getRaca(self):
        return self.raca

    def setRaca(self, raca):
        self.raca = raca

    def getTamanho(self):
        return self.tamanho

    def setTamanho(self, tamanho):
        self.tamanho = tamanho

#programa principal

cachorro = Animal()
cachorro.setNome("Apolo")
cachorro.setRaca("West")
cachorro.setTamanho("Porte Médio")

print(cachorro.getNome(), cachorro.getRaca(), cachorro.getTamanho())

