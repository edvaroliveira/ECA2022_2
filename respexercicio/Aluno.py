class Aluno:
    def __init__(self, matricula, nome, email, telefone, curso):
        self._matricula = matricula
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._curso = curso

    def getMatricula(self):
        return self._matricula

    def setMatricula(self, matricula):
        self._matricula = matricula

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def getTelefone(self):
        return self._telefone

    def setNome(self, telefone):
        self._telefone = telefone

    def getCurso(self):
        return self._curso

    def setCurso(self, curso):
        self._curso = curso

