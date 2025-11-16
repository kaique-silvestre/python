# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade 
# - até 9 anos : mirin
# - até 14 anos : infantil 
# - até 19 anos : junior 
# - até 20 anos : sênior 
# - acima : MASTER 

from datetime import date

nasc = int(input('Coloque o ano de nascimento : '))
idade = date.today().year - nasc

if idade <= 9 :
    print('Mirim')
elif idade <= 14 :
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 20 :
    print('Senior')
elif idade > 20 :
    print('MASTER')
