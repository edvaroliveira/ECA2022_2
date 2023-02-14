class Poligono:

   def setValores(self, largura, altura):
        self.largura = largura
        self.altura = altura

   def getAltura(self):
       return self.altura

   def getLargura(self):
       return self.largura

class Forma:
    cor = None

    def setCor(self, cor):
        self.cor = cor

    def getCor(self):
        return self.cor

class Triangulo(Poligono, Forma):
    def area(self):
        return self.getLargura() * self.getAltura() / 2


class Retangulo(Poligono, Forma):
    def area(self):
        return self.getLargura() * self.getAltura()

r = Retangulo()
r.setValores(20,60)
print(r.area())
r.setCor("Azul")
print(r.getCor())