from Aluno import Aluno
from Disciplina import Disciplina
from AlunoDisciplina import AlunoDisciplina

def cadastrarAluno():
    matricula = input("Digite a matrícula: ")
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o e-mail do aluno: ")
    telefone = input("Digite o telefone do aluno: ")
    curso = input("Qual o curso do aluno: ECA ou BSI? ")
    while curso.upper() not in ["ECA", "BSI"]:
        curso = input("Qual o curso do aluno: ECA ou BSI? ")

    return Aluno(matricula, nome, email, telefone, curso)

def cadastrarDisciplina():
    codigo = input("Digite o código da disciplina: ")
    nome = input("Digite o nome da disciplina: ")
    ementa = input("Digite a ementa da disciplina")

    return Disciplina(codigo, nome, ementa)

def vincularAlunoDisciplina(aluno, disciplina):
    nap1 = float(input(f"Qual a nota do NAP1 do aluno {aluno.getNome()} na disciplina {disciplina.getNome()}? "))
    nap2 = float(input(f"Qual a nota do NAP2 do aluno {aluno.getNome()} na disciplina {disciplina.getNome()}? "))
    ad = AlunoDisciplina()
    ad.cadastrarNotas(aluno, disciplina, nap1, nap2)
    return ad

# principal

# a = cadastrarAluno()
# d = cadastrarDisciplina()
a = Aluno(000, "edvar", "ed@", 333, "BSI")
d = Disciplina(111, "POO", "poo")

# vincular/matricular
ad = vincularAlunoDisciplina(a, d)

#armazenar em lista

bsi = []
eca = []

if(ad.getAluno().getCurso() == "BSI"):
    bsi.append(ad)
else:
    eca.append(ad)
print("\n\n")
print("Listagem de alunos de BSI (questão 1")
for b in bsi:
    print(b.getAluno().getNome(),b.getDisciplina().getNome())

print(bsi)
print(eca)