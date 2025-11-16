class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"{self.__class__.__name__}(nome=\"{self.nome}\", idade={self.idade})"
    

humano = Pessoa("Mateus", 31)
print(humano)
        