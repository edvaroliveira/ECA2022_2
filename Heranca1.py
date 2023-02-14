class Veiculo:

    def ligar(self):
        print("Motor ligado!")

    def desligar(self):
        print("Motor desligado!")


class Carro(Veiculo):
    pass

class Moto(Veiculo):
    pass

class Aviao(Veiculo):
    pass

c1 = Carro()
c1.ligar()
av1 = Aviao()
av1.desligar()