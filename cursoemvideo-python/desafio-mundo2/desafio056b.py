# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre :
# A média de idade do grupo 
# Qual é o nome do homem mais velho 
# e quantas mulheres tem menos de 20 anos/21 anos

lista_nome = []
lista_sexo = []
lista_idade = []
homem_velho = [0, 0]
mulher_21 = 0
for i in range(1, 5):
    print(f'Cadastro da {i}º Pessoa: ')
    nome = str(input(f'O Nome da {i}º Pessoa: ')).strip().title()
    sexo = int(input(f'Qual é seu sexo {nome} \n [ 1 ] Mulher / [ 2 ] Homem: '))
    idade = int(input(f'Coloque sua idade {nome}: '))
    lista_nome += [nome]
    lista_sexo += [sexo]
    lista_idade += [idade]
    if i == 1 and sexo == 2:
        homem_velho = [nome, idade]
    else:
        if idade > homem_velho[1] and sexo == 2:
            homem_velho = [nome, idade]
    if sexo == 1 and idade < 21:
        mulher_21 += 1
media = (sum(lista_idade)) / 4
print(f'A média de idades é: {media:.1f}')
if homem_velho == [0, 0]:
    print('não há homens cadastrados')
else:
    print(f'O homem mais velho se chama: {homem_velho[0]}')
if mulher_21 == 0:
    print('Não há mulheres com menos de 21 anos')
else:
    print(f'O número de mulheres com menos de 21 anos é: {mulher_21}')
