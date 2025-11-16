# faça um programa que tenha uma função chamada maior(), que recebe vários parâmetros com valores inteiros
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior 

def maior(a):
    print(f'O maior valor digitado é: {max(a)}')

lstnum = list()

while True:
    lstnum.append(int(input('Digite varios números: ')))
    if 0 in lstnum:
        break
maior(lstnum)


