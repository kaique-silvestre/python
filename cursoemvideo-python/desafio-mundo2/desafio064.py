# Crie um programa que leia vários números inteiros pelo teclado. o programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles ( desconsiderando o flag(999))

contsoma = 0
contnum = 0
num = 0
print('Digite números inteiros, no final o programa irá te mostrar quantos números foram e a soma deles, se quiser parar coloque 999')
while num != 999:
    num = int(input('Número: '))
    if num != 999:
        contsoma += num
        contnum += 1
print(f'No total foram digitados {contnum} valores que somamando são {contsoma}')