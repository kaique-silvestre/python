# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado 

from random import randint
from operator import itemgetter
from time import sleep
ranking = list()
jogo = {'jogador 1': randint(0, 6),
        'Jogador 2': randint(0, 6),
        'Jogador 3': randint(0, 6), 
        'Jogador 4':randint(0, 6)}
print('Os números escolhidos foram:')
for key, values in jogo.items():
    print(f'{key} escolheu: {values}')
ranking = sorted((jogo.items()), key=itemgetter(1), reverse=True)
print('===RANKING DE GANHADORES===')
for pos, values in enumerate(ranking):
    print(f'{pos+1}º lugar: {values[0]} com {values[1]}')
