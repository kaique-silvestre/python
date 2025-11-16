# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lidos.
# v@g@bund0 ainda conseguiu simplificar o código menos ainda
peso = [float(input(f'O Peso da {i}º Pessoa: ')) for i in range(1, 6)]
print(f'O maior peso é {max(peso)} e o menor é {min(peso)}')