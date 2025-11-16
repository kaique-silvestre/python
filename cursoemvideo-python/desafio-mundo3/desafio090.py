# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrtura na tela 
boletim = dict()

boletim['nome'] = str(input('Nome ')).strip().title()
boletim['média'] = float(input('Media: '))
if boletim['média'] >= 7:
    boletim['situação'] = 'Aprovado'
elif boletim['média'] >= 5:
    boletim['situação'] = 'Recuperação'
else: 
    boletim['situação'] = 'Reprovado'

print(boletim)

for i, v in boletim.items():
    print(f'{i} é {v}')