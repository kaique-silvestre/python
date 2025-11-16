# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# Considere a maioridade com 21 anos 

from datetime import date

data = date.today().year
maioridade = 21
contador_maior = 0
contador_menor = 0

ano1 = data - int(input('Ano de nascimento 1º Pessoa: '))
ano2 = data - int(input('Ano de nascimento 2º Pessoa: '))
ano3 = data - int(input('Ano de nascimento 3º Pessoa: '))
ano4 = data - int(input('Ano de nascimento 4º Pessoa: '))
ano5 = data - int(input('Ano de nascimento 5º Pessoa: '))
ano6 = data - int(input('Ano de nascimento 6º Pessoa: '))
ano7 = data - int(input('Ano de nascimento 7º Pessoa: '))

if ano1 >= maioridade:
    contador_maior = contador_maior + 1 
elif ano1 < maioridade:
    contador_menor = contador_menor + 1

if ano2 >= maioridade:
    contador_maior = contador_maior + 1 
elif ano2 < maioridade:
    contador_menor = contador_menor + 1

if ano3 >= maioridade:
    contador_maior = contador_maior + 1 
elif ano3 < maioridade:
    contador_menor = contador_menor + 1

if ano4 >= maioridade:
    contador_maior = contador_maior + 1 
elif ano4 < maioridade:
    contador_menor = contador_menor + 1

if ano5 >= maioridade:
    contador_maior = contador_maior + 1 
elif ano5 < maioridade:
    contador_menor = contador_menor + 1

if ano6 >= maioridade:
    contador_maior = contador_maior + 1 
elif ano6 < maioridade:
    contador_menor = contador_menor + 1

if ano7 >= maioridade:
    contador_maior = contador_maior + 1 
elif ano7 < maioridade:
    contador_menor = contador_menor + 1

print(f'Pessoas maiores de idade: {contador_maior}')
print(f'Pessoas menores de idade: {contador_menor}')