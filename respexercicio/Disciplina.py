class Disciplina:

    def __init__(self, codigo, nome, ementa):
        self._codigo = codigo
        self._nome = nome
        self._ementa = ementa

    def getCodigo(self):
        return self._codigo

    def setCodigo(self, codigo):
        self._codigo = codigo

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getEmenta(self):
        return self._ementa

    def setEmenta(self, ementa):
        self._ementa = ementa