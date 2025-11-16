# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado ( entre 0 e 20) e mostrá-lo por extenso.

tupla = ( 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte' )
num = 0
while True:
        num = int(input('N: '))
        if 0 <= num <=20:
               print(tupla[num]) 
        else:
                break
                