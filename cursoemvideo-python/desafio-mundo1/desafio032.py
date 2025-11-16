# Faça um programa que leia um ano qualquer e mostre se é um ano bissexto 
ano = int(input('Insira o ano : '))
b = ano%4 
if b == 0 : 
    print('O ano é bissexto')
else : 
    print('O ano não é bissexto')