class Pessoa:
    def __init__(self):
        self._nome = None
        self._idade = None 

    @property
    def nome(self):
        return self._nome 

    @nome.setter
    def nome(self, name):
        if len(name) < 1: 
            raise ValueError("Nome não pode estar vazio")
        self._nome = name 
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, value):
        if not isinstance(value, int):
            raise TypeError("O valor deve ser inteiro")
        if value <= 0:
            raise ValueError("Idade deve ser maior que zero")
        self._idade = value
              
    
p1 = Pessoa()
p1.nome = 'Kaique'
print(p1.nome)

print()

p1.idade = 10
print(p1.idade)