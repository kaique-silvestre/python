# Exercício - salve sua classe em JSON
# Salve os dados da sua classe em JSON e depois crie novamente as instâncias da classe com os dados salvos, faça em arquivos separados

import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

pessoa01 = Pessoa('Mario', 26)

with open('saveclass.json', 'w+', encoding='utf-8') as data:
    objeto = vars(pessoa01)
    json.dump(objeto, data)

