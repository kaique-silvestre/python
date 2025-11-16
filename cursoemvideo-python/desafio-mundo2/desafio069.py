# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# no final mostre :
# A ) Quantas pessoas tem mais de 18 anos 
# B ) Quantos homens foram cadastrados 
# c ) Quantas mulheres tem menos de 20 anos 

maioridade = homens = mulher20 = 0
print('-='*30)
print('PROGRAMA DE CADASTRAMENTO')
while True: 
    opc = sexo = ' '
    print('-='*30)
    idade = int(input('Idade: '))
    if idade >= 18:
        maioridade += 1 
    while sexo not in 'MmFf':
        sexo = str(input('[M/F]: ')).strip().lower()[0]
    if sexo == 'm':
        homens += 1
    if idade < 20 and sexo == 'f':
        mulher20 += 1
    while opc not in 'SsNn':
        opc = str(input('Deseja continuar ? [S/N]: ')).strip().lower()[0]
    if opc == 'n':
        break
print(f'A quantidade de pessoas que tem mais de 18 anos é: {maioridade}')
print(f'A quantidade de homens cadastrados: {homens}')
print(f'A quantidade de mulheres com menos de 20 anos é: {mulher20}')
