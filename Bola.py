class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def mostraCor(self):
        return self.cor

    def trocaCor(self, cor):
        self.cor = cor
