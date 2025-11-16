# Faça um programa que tenha uma função chamada contador(), que recebe três parametros: inicio, fim e passo e realize a contagem 
# Seu programa tem que realizar tres contagem atráves da função criada 
# a) de 1 até 10, de 1 em 1 
# b) de 10 até 0, de 2 em 2 
# c) Uma contagem personalizada 

def contador(a, b, c):
    print('Contagem de 1 até 10:')
    for c in range(0, 11):
        print(c, end=' ')
    print()
    print('Contagem de 10 até 0, pulando de 2 em 2')
    for v in range(10, -2, -2):
        print(v, end=' ')
    print()
    #-----------------------#
    print('Hora da sua contagem:')
    if c == 0:
        c = 1
        print('0 não pode ser escolhido, o valor 1 foi considerado no lugar.')
    if a < b:
        for i in range(a, b+1, c):
            print(i, end=' ')
        print()
    if a > b: 
        if c < 0:
            c = c * -1
        print(a)
        while a != b:
            a = a - c
            print(a, end=' ')
        print()
    
a = int(input('Número inicial: '))
b = int(input('Número final: '))
c = int(input('Passos: '))
contador(a, b, c)