import json
from aula127_a import Pessoa


with open('saveclass.json', 'r', encoding='utf-8') as data:
    arq = json.load(data)

pessoa01 = Pessoa(**arq)
print(vars(pessoa01))