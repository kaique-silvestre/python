# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre >
# A média de idade do grupo /
# Qual é o nome do homem mais velho /
# e quantas mulheres tem menos de 20 anos/21 anos

# Captação de Dados 
print('Validação de dados')

#   Captação de Dados da 1º Pessoa
print('Primeira pessoa')
nome_1 = str(input('Coloque seu nome: ')).strip().title()
sexo_1 = int(input('[ 1 ] para mulher e [ 2 ] para homem: '))
idade_1 = int(input('Coloque sua idade: '))

#   Captação de Dados da 2º Pessoa
print('Segunda pessoa')
nome_2 = str(input('Coloque seu nome: ')).strip().title()
sexo_2 = int(input('[ 1 ] para mulher e [ 2 ] para homem: '))
idade_2 = int(input('Coloque sua idade: '))

#   Captação de Dados da 3º Pessoa
print('Terceira pessoa')
nome_3 = str(input('Coloque seu nome: ')).strip().title()
sexo_3 = int(input('[ 1 ] para mulher e [ 2 ] para homem: '))
idade_3 = int(input('Coloque sua idade: '))

#   Captação de Dados da 4º Pessoa
print('Quarta pessoa')
nome_4 = str(input('Coloque seu nome:')).strip().title()
sexo_4 = int(input('[ 1 ] para mulher e [ 2 ] para homem: '))
idade_4 = int(input('Coloque sua idade: '))

# Declaração de Variáveis 

#   Contador de mulheres menores de 21 anos
cont = 0 

#   Variável Controle do Nome do Homem Mais velho
maior = 0

#   Variável formula da média de Idade 
media = (idade_1 + idade_2 + idade_3 + idade_4) / 4

# Validação do Nome do Homem Mais velho

#   1º Pessoa 
if idade_1 > idade_2 and idade_1 > idade_3 and idade_1 > idade_4 and sexo_1 == 2 :
    maior = nome_1

#   2º Pessoa 
elif idade_2 > idade_1 and idade_2 > idade_3 and idade_2 > idade_4 and sexo_2 == 2 :
    maior = nome_2

#   3º Pessoa 
elif idade_3 > idade_1 and idade_3 > idade_2 and idade_3 > idade_4 and sexo_3 == 2 :
    maior = nome_3

#   4º Pessoa 
elif idade_4 > idade_1 and idade_4 > idade_2 and idade_4 > idade_3 and sexo_4 == 2 :
    maior = nome_4

# Validação de Mulheres que tem menos de 21 anos

#   1) Valida se o valor na variavel 'sexo' é 1 logo 'Mulher' e se a variavél 'idade' tem um valor menor que 21( Ou seja se a mulher tem menos de 21 anos)

#   2) Se sim, for 1(mulher), soma +1 para o contador 

#   3) Pode ser facilmente adaptado para um contador de quantas mulheres tem na validação, basta retirar os 'and' que adicionam a condição de 'idade' < 21

#   1º Pessoa 
if sexo_1 == 1 and idade_1 < 21 :
    cont = cont + 1

#   2º Pessoa 
if sexo_2 == 1 and idade_2 < 21 :
    cont = cont + 1

#   3º Pessoa 
if sexo_3 == 1 and idade_3 < 21 :
    cont = cont + 1

#   4º Pessoa 
if sexo_4 == 1 and idade_4 < 21 :
    cont = cont + 1

# Output dos resultados
print(f'A média de idades do grupo é: {media:.1f}')

# Condição composta para caso não haja homens na validação
if maior == 0 :
    print('Não há homens nessa validação de dados')
else :
    print(f'O nome do homem mais velho é: {maior}')

print(f'Existem {cont} mulheres com menos de 21 anos')

# Foram quase 100 linhas feitas da forma analógica, mas após entender melhor, refazer o desafio com base nos anteriores consegui automatizar ele e deixa-lo bem melhor.