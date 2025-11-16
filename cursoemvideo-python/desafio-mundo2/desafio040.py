# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando no final, de acordo com a média atingida :
# - Abaixo de 5 reprovado 
# - entre 5 e 6.9 recuperação 
# media 7 ou superior aprovado 

nota1 = float(input('Coloque a primeira nota : '))
nota2 = float(input('Coloque a segunda nota : '))

media = (nota1 + nota2) / 2 

print(media)
if media >= 7 :
    print('Aprovado')
elif media < 5 :
    print('Reprovado')
else : 
    print('Recuperação')
