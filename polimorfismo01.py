class Pizza:
    @staticmethod
    def ingredientes():
        return "Pizza básica"

class Mussarela(Pizza):
    pass

class Atum(Pizza):

    @staticmethod
    def ingredientes():
        return ["Atum", "Cebola", "Mussarela", "Orégano"]


p1 = Atum()
print(p1.ingredientes())
p2 = Mussarela()
print(p2.ingredientes())