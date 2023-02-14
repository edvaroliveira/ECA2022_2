class Pet:
    def __init__(self):
        self.nome = "André"
        self.raca = "SRD"

    def trocarNome(self, nome):
        self.nome = nome

    def latir(self):
        print("Au au au au auuuuuuuu")

    def responderNome(self):
        return self.nome


