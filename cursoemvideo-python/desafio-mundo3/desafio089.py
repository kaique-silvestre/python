# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente 

proty = list()
boletim = list()

while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 = int(input('1º Nota: '))
    nota2 = int(input('2º Nota: '))
    opc = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    media = (nota1 + nota2) / 2
    proty.append(nome)
    proty.append(nota1)
    proty.append(nota2)
    proty.append(media)
    boletim.append(proty[:])
    proty.clear()
    if opc in 'n':
        break

print('BOLETIM')
print('Nº Nome Media')
for pos, i in enumerate(boletim):
    print(pos + 1, i[0], i[3])

qst = int(input('Coloque o número do aluno para ver notas individuais'))
print(i[qst][qst+1][qst+2])