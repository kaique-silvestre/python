class Humano:
    def __init__(self, nome, sexo):
        self.nome = nome
        self.sexo = sexo

    def __call__(self):
        return self.__dict__

pessoa = Humano('Sabrina', 'Feminino')

print(pessoa())