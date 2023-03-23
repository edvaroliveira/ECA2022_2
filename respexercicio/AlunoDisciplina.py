from datetime import date

class AlunoDisciplina:
    _nap1 = 0
    _nap2 = 0
    _data = date.today()

    def setCodigo(self, codigo):
        return self._codigo

    def getCodigo(self):
        return self._codigo

    def getData(self):
        self._data = date.today()
        return self._data

    def getNap1(self):
        return self._nap1

    def getNap2(self):
        return self._nap2

    def getStatus(self):
        if self._media >= 6:
            return True
        else:
            return False

    def setAluno(self, aluno):
        self._aluno = aluno

    def setDisciplina(self, disciplina):
        self._disciplina = disciplina

    def getAluno(self):
        return self._aluno

    def getDisciplina(self):
        return self._disciplina

    def cadastrarNotas(self, aluno, disciplina, nap1, nap2):
        self.setAluno(aluno)
        self.setDisciplina(disciplina)
        if nap1 > 10 and nap1 < 0 and nap2 > 10 and nap1 < 0:
            return "Erro no valor das notas"
        else:
            self._nap1 = nap1
            self._nap2 = nap2
            self._media = (self._nap1+self._nap2)/2
            if self.getStatus():
                self._status = True
            else:
                self._status = False


