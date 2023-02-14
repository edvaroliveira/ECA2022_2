class Dog:
    species = "Canis familiaris"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos de idade"

    def speak(self, som):
        return f"{self.nome} late {som}"

class CotondeTulear(Dog):
    pass
class WestHighlandWhiteTerrier(Dog):
    pass
class SRD(Dog):
    def speak(self, som="Arf"):
        return f"{self.nome} late {som}"

apolo = SRD("Caramelo", 13)
print(apolo.speak())

