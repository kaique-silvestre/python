# Crie um programa que tenha uma função chamada fatorial(), que receba dois parâmetros, o primeiro que indique um número a calcular e o outro chamado show que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de calculo do fatorial   

def fatorial(a, b=True):
    c = 1
    for i in range(a, 0, -1):
        c *=i 
        if b == True:
            print(i, end=' ')
            if i != 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return c

a = int(input(('Digite um número para o calculo da fatorial: ')))
print(fatorial(a))


