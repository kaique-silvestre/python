# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols deitos durante o campeonato 
cadastro = dict()
totaldegols = 0

cadastro['Nome'] = str(input('Nome do jogador: ')).strip().title()
cadastro['Partidas Jogadas'] = int(input('Quantas partidas foram jogadas: '))
for i in range(0, cadastro['Partidas Jogadas']):
    cadastro[f'Gols na {i+1}º partida'] = int(input(f'Quantos gols foram feitos na {i+1}º partida: '))
    totaldegols += cadastro[f'Gols na {i+1}º partida']
cadastro['Total de Gols'] = totaldegols

print('APROVEITAMENTO DO JOGADOR')
for keys, values in cadastro.items():
    print(f'{keys}: {values}')