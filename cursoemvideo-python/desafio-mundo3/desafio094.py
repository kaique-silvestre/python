# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A ) Quantas pessoas foram cadastradas 
# B ) A média de idade do grupo 
# C ) Uma lista com todas as mulheres
# D ) Uma lista com todas as pessoas com idade acima da média 

dicionário = dict()
lista = list()
media = 0
mulheres = list()
acimaidade = list()

while True:
    dicionário['nome'] = str(input('Nome: ')).strip().title()
    dicionário['sexo'] = ' '
    while dicionário['sexo'] != 'M' and dicionário['sexo'] != 'F':
        dicionário['sexo'] = str(input('[M/F]: ')).strip().upper()
        if dicionário['sexo'] != 'M' and dicionário['sexo'] != 'F':
            print('ERRO. TENTE NOVAMENTE.')
    dicionário['idade'] = int(input('Idade: '))
    opc = ' '
    while opc != 'S' and opc != 'N':
        opc = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
        if opc != 'S' and opc != 'N':
            print('ERRO. TENTE NOVAMENTE')
    media += dicionário['idade']
    if dicionário['sexo'] == 'F':
        mulheres.append(dicionário['nome'])
    lista.append(dicionário.copy())
    if opc == 'N':
        break

print(f'A quantidade de pessoas cadastradas é: {len(lista)}')
print(f'A média de idade das pessoas é: {media/len(lista):.2f}')
print(f'A lista de todas as mulheres cadastradas é: {mulheres}')
for pos, i in enumerate(lista):
    if lista[pos]['idade'] > media/len(lista):
        print('Lista de pessoas com idade acima da média: ')
        print(f'Nome: {lista[pos]['nome']}, sexo: {lista[pos]['sexo']}, idade: {lista[pos]['idade']}')