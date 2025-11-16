# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
print('Bem-vindo. Esse é programa Jogo da Sorte. O computador vai sortear um número de 0 a 5 e você tem que advinha-lo.')
sorteado = randint(0, 5)
escolhido = int(input('Escolha um número : '))
if sorteado == escolhido : 
    print(f'Você ganhou, parabéns. O número sorteado foi {sorteado} e o escolhido {escolhido}')
else : 
    print(f'Você perdeu. O número sorteado foi {sorteado} e o escolhido foi {escolhido}. Tente novamente.')