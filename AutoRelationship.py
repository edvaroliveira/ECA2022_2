class Aluno:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def alunoDisciplina(self, disciplina):
        self.obj_disciplina = disciplina

class Disciplina:

    def __init__(self, nome):
        self.nome = nome

    def disciplinaAluno(self, aluno):
        self.obj_aluno = aluno

aluno1 = Aluno("André", "andremarista@")
disciplina1 = Disciplina("Programação II")
disciplina1.disciplinaAluno(aluno1)
aluno1.alunoDisciplina(disciplina1)
print(disciplina1.obj_aluno.nome)
print(aluno1.obj_disciplina.nome)
