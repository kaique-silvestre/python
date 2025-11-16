# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# Considere a maioridade com 21 anos 

from datetime import date

data = date.today().year
contador_menor = 0
contador_maior = 0

for i in range(1, 8):
    idade = data - int(input(f'Ano de nascimento da {i}º pessoa: '))
    if idade < 21:
        contador_menor += 1
    else:
        contador_maior += 1
print(f'Quantidade de pessoas menores de idade: {contador_menor}')
print(f'Quantidade de pessoas maiores de idade: {contador_maior}')
