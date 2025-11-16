# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. no final mostre:
# A) Quantas pessoas foram cadastradas 
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves  

provisorio = list()
cadastro = list()

while True: 
    provisorio.append(str(input('Nome: ')).strip().title())
    provisorio.append(float(input('Peso: ')))
    opc = str(input('Deseja Continuar [S/N]: ')).strip().lower()[0]
    cadastro.append(provisorio[:])
    provisorio.clear()
    if opc in 'n':
        break

print('=-'*30)
print(f'A quantidade de pessoas cadastradas é: {len(cadastro)}')
print('Lista de pessoas, considerando 70Kg.')
print('=-'*30)
print('As pessoas mais leves são:')
for p in cadastro:
    if p[1] < 70:
        print(f'{p[0]} com {p[1]}Kg')
print('=-'*30)
print('Lista de Pessoas mais Pesadas:')
for p in cadastro:
    if p[1] > 70: 
        print(f'{p[0]} com {p[1]}Kg')
        