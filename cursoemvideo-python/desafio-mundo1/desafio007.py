# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nsa1 = float(input('Digíte a nota do aluno no primeiro semestre : '))
nsa2 = float(input('Digíte a nota do aluno no segundo semestre : '))
media = (nsa1 + nsa2) / 2 
if media >= 7 :
    print('A nota {} do primeiro semestre e a nota {} do segundo semestre constituem a média de {:.1f} portanto ele está aprovado'.format(nsa1, nsa2, media))
else : 
    print('A nota {} do primeiro semestre e a nota {} do segundo semestre constituem uma média de {:.1f} que está abaixo da nossa média minima, portanto ele está reprovado'.format(nsa1, nsa2, media))