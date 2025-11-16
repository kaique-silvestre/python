# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lidos.
# Refazendo o código pois achei lindo
maior = 0
menor = 0 
for i in range(1, 6):
    peso = float(input(f'Peso da {i}º Pessoa em Kg: '))
    if i == 1: 
        maior = peso
        menor = peso 
    else:
        if peso > maior:
            maior = peso
        if peso < menor: 
            menor = peso
print(f'O maior peso é: {maior:.2f}Kg')
print(f'O menor peso é: {menor:.2f}Kg')
            