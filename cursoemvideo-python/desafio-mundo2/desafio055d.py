# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lidos.
# Fazendo com listas e funções de máximo e minímo vistas nos comentarios do youtube 
lista = []
for i in range(1, 6):
    peso = float(input(f'Peso da {i}º Pessoa: '))
    lista += [peso]
print(f'O maior peso é: {max(lista):.2f}')
print(f'O menor peso é: {min(lista):.2f}')