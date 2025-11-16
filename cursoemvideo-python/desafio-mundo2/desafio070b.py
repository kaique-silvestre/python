# Crie um programa que leia o nome de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: 
# A) Qual é o total gasto na compra 
# B) Quantos produtos custam mais de R$1000
# C) Qual é o nome do produto mais barato. 

barato = contvezes = maisdemil = total = 0
nome_barato =' '

while True:
    nome = str(input('Nome do Produto: '))
    valor = int(input('Valor: R$'))
    total += valor 
    contvezes += 1
    if contvezes == 1:
        barato = valor 
        nome_barato = nome 
    elif barato > valor:
        barato = valor
        nome_barato = nome 
    if valor >= 1000:
        maisdemil += 1
    op = ' '
    while op not in 'NnSs':
        op = str(input('Deseja continuar ? [S/N]: ')).strip().lower()[0]
    if op == 'n':
        break
print(f'O total gasto é: R${total}')
print(f'A quantidade de produtos que custam mais de mil é: {maisdemil}')
print(f'O produto mais barato é {nome_barato} custando R${barato}')