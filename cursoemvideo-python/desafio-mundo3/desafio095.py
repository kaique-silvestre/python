# Aprimore o desafio093 para que ele funcione com vários jogadores, incluindo um sistema de vizualização de detalhes do aproveitamento de cada jogador 
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols deitos durante o campeonato 

from time import sleep

lista = list()
dic = dict()
dicp = dict()
opc2 = 0
opc2 = 0

while True:
    totaldegols = 0
    dic['nome'] = str(input('Nome do jogador(a): ')).strip().title()
    partidas = int(input('Quantas partidas foram jogadas: '))
    for i in range(0, partidas):
        dic[f'Gols na {i + 1}º partida'] = int(input(f'Quantos gols foram feitos na {1 + i}º partida: '))
        totaldegols += dic[f'Gols na {i + 1}º partida']
    dic['Total de Gols'] = totaldegols
    lista.append(dic.copy())
    opc = ' '
    while opc != 'S' and opc != 'N':
        opc = str(input('Deseja adicionar mais um jogador? [S/N]: ')).strip().upper()[0]
        if opc != 'S' and opc != 'N':
            print('ERRO. TENTE NOVAMENTE')
    if opc == 'N':
        break

while opc2 != -1: 
    print('=-='*30)
    sleep(0.3)
    for pos, i in enumerate(lista):
        print(f'{pos + 1 } - {lista[pos]['nome']} fez no total: {lista[pos]['Total de Gols']} Gols')   
    opc2 = int(input('Digite o número do jogador para ver o aproveitamento nas partidas: ')) - 1
    dicp = lista[opc2] 
    if opc2 == -1:
        break
    print('=-='*30)
    for keys, values in dicp.items():
        sleep(0.3)
        print(f'{keys}: {values}')
   
