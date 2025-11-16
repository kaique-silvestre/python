# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar 

num = int(input('Coloque um número :'))
pi = num % 2
if pi == 0 : 
    print('O número é par')
else : 
    print('O número é impar')