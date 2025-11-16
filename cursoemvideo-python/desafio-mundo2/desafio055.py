# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lidos.

peso1 = float(input('Peso da Primeira Pessoas: Kg '))
peso2 = float(input('Peso da Segunda Pessoas: Kg '))
peso3 = float(input('Peso da Terceira Pessoas: Kg '))
peso4 = float(input('Peso da Quarta Pessoas: Kg '))
peso5 = float(input('Peso da Quinta Pessoas: Kg '))

maior = peso1
menor = peso1

# Menor peso
if peso2 < peso1 and peso2 < peso3 and peso2 < peso4 and peso2 < peso5:
    menor = peso2

if peso3 < peso1 and peso3 < peso2 and peso3 < peso4 and peso3 < peso5:
    menor = peso3

if peso4 < peso1 and peso4 < peso2 and peso4 < peso3 and peso4 < peso5:
    menor = peso4

if peso5 < peso1 and peso5 < peso2 and peso5 < peso3 and peso5 < peso4:
    menor = peso5
    
# Maior peso
if peso2 > peso1 and peso2 > peso3 and peso2 > peso4 and peso2 > peso5:
    maior = peso2

if peso3 > peso1 and peso3 > peso2 and peso3 > peso4 and peso3 > peso5:
    maior = peso3

if peso4 > peso1 and peso4 > peso2 and peso4 > peso3 and peso4 > peso5:
    maior = peso4

if peso5 > peso1 and peso5 > peso2 and peso5 > peso3 and peso5 > peso4:
    maior = peso5
    
print(f'O Menor peso é: Kg {menor:.2f}')
print(f'O Maior peso é: Kg {maior:.2f}')

# É como se eu fosse um homens da caverna codando 