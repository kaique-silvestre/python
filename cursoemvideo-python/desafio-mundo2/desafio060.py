# Faça um programa que leia um número qualquer e mostre o seu fatorial 
# ex:
# 5! = 5x4x3x2x1=120

n = int(input('N: '))
c = n 
f = 1
print(f'Calculando {n}! = ', end='')
while c > 1:
    print(f'{c}', end='')
    print( ' x ' if c > 1 else ' = ', end='')
    f *= 1
    c -= 1
print(f'{f}')