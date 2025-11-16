# Crie um programa que leia vários números pelo teclado. no final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
y = 1
soma = 0
vezes = 0

x = int(input('Números: '))
soma += x 
vezes += 1
maior = x 
menor = x 
while y != 0: 
    d = int(input('Números: '))
    soma += d 
    vezes += 1
    if maior < d:
        maior = d
    if menor > d:
        menor = d
    y = int(input('Deseja parar o programa ? SIM - [ 0 ] OU NÃO [ QUALQUER NÚMERO ]: '))
    if y == 0:
        media = soma / vezes
        print(f'A média dos números digítados é: {media} ')        
        print(f'O maior número digítado é: {maior} ')
        print(f'O menor número digítado é: {menor} ')


