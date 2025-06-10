class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

aluno01 = Aluno('Ricardo', 45, 'Python')
print(aluno01.nome, aluno01.idade, aluno01.curso, sep=', ')
 