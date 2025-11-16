# Faça um programa que leia 5 valores númericos e guarde-os em uma lista
# No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista 
num = list()
maior = menor = 0

for i in range(0, 5):
    num.append(int(input(f'Número na posição {1 + i}º: ')))
    if i == 0:
        maior = menor = num[i]
    else:
        if num[i] > maior:
            maior = num[i]
        elif num[i] < menor:
            menor = num[i]
print(f'A lista escrita é {num}')
print(f'O maior número é {maior} na posição')
for pos, m in enumerate(num): 
    if maior == m: 
        print(f'...{1 + pos}',)
print(f'O menor número é {menor}')
for pos, m in enumerate(num):
    if m == menor:
        print(f'...{1 + pos}')   