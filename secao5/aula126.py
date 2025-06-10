class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


pessoa01 = Pessoa('Debora', 33)

print(pessoa01.__dict__)


pessoa01.__dict__['nome'] = 'Bruna'
pessoa01.__dict__['idade'] = 45

print(pessoa01.__dict__)