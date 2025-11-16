# crie um programa onde o usuario possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores unicos digitados em ordem crescente. 

lista = list()
while True:
    num = int(input('Coloque vários números [0 para finalizar]: '))
    if num == 0:
        break
    if num not in lista:
        lista.append(num)
print(f'Essa é a lista de todos os valores unicos digitados de forma crescente: {sorted(lista)}')

