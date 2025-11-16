# Faça um programa que leia 5 valores númericos e guarde-os em uma lista
# No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista 

num = list(int(input(f'Coloque o {c+1}º número: '))for c in range(5))
print(f'A lista de números digitados ficou: {num}')
print(f'O maior número é {max(num)}, na posição {1 + num.index(max(num))}º')
print(f'O menor número é {min(num)}, na posição {1 + num.index(min(num))}º')


