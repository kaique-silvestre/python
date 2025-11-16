# Crie um programa que leia o nome de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: 
# A) Qual é o total gasto na compra 
# B) Quantos produtos custam mais de R$1000
# C) Qual é o nome do produto mais barato. p - n

from math import inf

somatudo = contamil = 0
barato = float(inf)
nomeq = ''


while True:
    nome = str(input('Nome: '))
    valor = int(input('Valor: '))
    if valor < barato:
        barato = valor
        nomeq = nome 
    if valor >= 1000: 
        contamil += 1
    somatudo += valor

    op = ' '
    while op not in 'SsNn':
        op = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if op == 'n':
        break   

print(f'O total gasto é: {somatudo}')
print(f'A quantidade de produtos que custa mais de R$1000 é: {contamil}')
print(nomeq)