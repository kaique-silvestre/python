# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o totla de vitórias consecutivas no final do jogo.

from random import randint

vitorias = 0

while True:
    x = randint(0, 10)
    jogador = ' '
    while jogador not in 'PpiI':
        jogador = str(input('[P/I]: ')).strip().lower()[0]
    num = int(input('Número: '))

    soma = num + x
    print(f'O jogador escolheu {num} e a maquina {x} somando {soma}')

    if soma % 2 == 0 :
        print('É PAR')
        ganhador = 'p'
    else:
        print('É IMPAR')
        ganhador = 'i'
    
    if jogador == ganhador:
        print('JOGADOR GANHOU')
        vitorias += 1
    else:
        print('MAQUINA GANHOU')
        break
print(f'Você ganhou {vitorias} vezes consecutivas.')     
