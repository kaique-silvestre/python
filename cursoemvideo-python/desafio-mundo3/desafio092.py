# Crie um programa que leia, nome, ano de nascimento e carteira de trabalho e cadestre com idade em um dicionário se por acaso a CTPS for difrente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar 

from datetime import date

cadastro = dict()
anoatual = date.today().year

cadastro['nome'] = str(input('Nome: ')).strip().title()
nascimento = anoatual - int(input('Ano de nascimento: ')) 
cadastro['idade'] = nascimento
ctps = int(input('Carteira de Trabalho [0 p/ não tem]: '))
if ctps != 0:
    contratação = int(input('ano de contratação: '))
    cadastro['salario'] = float(input('salário: '))
    cadastro['Anos que faltam para aposentar '] = contratação - anoatual + 35
    cadastro['A idade de aposentadoria é'] = cadastro['Anos que faltam para aposentar: '] + nascimento

print('Dados cadastrados: ')
for keys, values in cadastro.items():
    print(f'{keys}: {values}')