# Melhore o jogo do desafio028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
x = randint(0, 10)
y = -1
cont = 0 

print('-'*30)
print('BEM-VINDO, tente até acertar o número que a maquina pensou de 0 a 10.')
while y != x:
    print('-'*30)
    x = randint(0, 10)
    y = int(input('A maquina pensou em: '))
    cont += 1
    if y != x:
        print('BANG! ERROU. TENTE NOVAMENTE.')
    else: 
        print(f'BAAAAAANG! ACERTOU! APENAS PRECISOU TENTAR {cont} VEZES')
