# Que honra chegar ao centésimo exercicio.
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia(lista): 
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print(lista)

def somaPar(b):
    pares = list()
    soma = 0
    for a in b:
        if a % 2 == 0:
            soma += a 
            pares.append(a)
    print(pares)
    print(soma)


numeros = list()

sorteia(numeros)
somaPar(numeros)