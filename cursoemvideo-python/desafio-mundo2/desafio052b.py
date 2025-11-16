# Faça um programa que leia um número inteiro e diga se ela é ou não um número primo

num = int(input('N: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m')
        tot += 1
    else :
        print('\033[m')
    print(c)
print(f'\033[mO número {num} foi divisivel {tot} vezes')