#criação de uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# definindo uma lista
a = []


#acrescentando um objeto a cada posição da lista
a.append(Pessoa("Edvar", 41))
a.append(Pessoa("André", 15))
a.append(Pessoa("Maristinha", 29))

print(f"A lista possui {len(a)} objetos armazenados")

#percorrendo a lista
for p in a:
    if(p.idade >= 30):
        print(p.nome, p.idade)
