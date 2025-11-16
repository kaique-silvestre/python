# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado 

from random import randint
from time import sleep

cofre = dict()
x = 0
def sort_dict(a):
    return a[1]

cofre['jogador1'] = randint(0, 6)
cofre['jogador2'] = randint(0, 6)
cofre['jogador3'] = randint(0, 6)
cofre['jogador4'] = randint(0, 6)

print('Os Jogadores escolherem os seguintes números: ')
for key, value in cofre.items():
    print(f'{key}: {value}')
    sleep(0.4)

print('Os Ganhadores em ordem são:')
new_dict = dict(sorted(cofre.items(), key = sort_dict, reverse=True))
for key, value in new_dict.items():
    x += 1
    print(f'{x}º {key}: {value}')
    sleep(0.4)

