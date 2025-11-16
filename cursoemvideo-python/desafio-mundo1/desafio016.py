# Crie um programa que leia um número real qualquer pelo teclado, e mostre na tela a asua porção inteira 
# Ex : Número 6.127 tem a parte inteira 6

from math import trunc 
nrq = float(input('Dígite um número real qualquer para transformamos ele em inteiro : '))
print(f'O número inteiro fica : {trunc(nrq)}')