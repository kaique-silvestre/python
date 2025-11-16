# Crie um programa onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final, mostre os valores pares e imapres em ordem crescente 
pi = [[], []]

for i in range(0, 7):
    valor = int(input(f'Coloque o {i + 1}º número: '))
    if valor % 2 == 0:
        pi[0].append(valor)
    else:
        pi[1].append(valor)
print('A lista completa é:')
print(pi)
print('Os valores pares em ordem crescente são:')
print(sorted(pi[0]))
print('Os valores imapres em ordem crescente são:')
print(sorted(pi[1]))