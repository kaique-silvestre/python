# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente 

boletim = list()

while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 = float(input('1º Nota: '))
    nota2 = float(input('2º Nota: '))
    opc = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    if opc == 'n':
        break
print('Nº Nome Media')
for pos, p in enumerate(boletim):
    print(pos + 1, p[0], p[2])
while True:
    opc2 = int(input('Coloque o nº para ver individualmente as notas de um aluno: '))
    if opc2 < len(boletim) + 1:
        print(f'{boletim[opc2 - 1][0]} tirou {boletim[opc2 - 1][1][0]} na sua 1º nota, e tirou {boletim[opc2 - 1][1][1]} na sua 2º nota')
    else:
        break