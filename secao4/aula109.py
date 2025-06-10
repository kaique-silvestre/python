from itertools import combinations, permutations, product

from pprint import pprint

people = ['João', 'Joana', 'Luiz', 'Letícia']

tshirt = [
    ['preta', 'branca'],
    ['p', 'm', 'g']
    ]


#combinação
print()
print(*product(*tshirt, repeat=1), sep='\n')
