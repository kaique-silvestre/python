# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles ( Desconsiderando o flag )

contnum = contsoma = 0

while True: 
    n = int(input('Número [999 para interromper]: '))
    if n == 999:
        break
    contsoma += n
    contnum += 1
print(f'Foram digitados {contnum} números, cuja a soma é {contsoma}')
print('FIM')