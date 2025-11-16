# Crie um programa que faça o computador jogar jokenpô com você 
# Pedra 
# papel 
# tesoura 

from random import choice

Jokenpô = choice(['pedra', 'papel', 'tesoura'])

Jogador = str(input('Pedra, Papel ou Tesoura : ')).strip().lower()

print(f'jokenpô é {Jokenpô} e Jogador é {Jogador}')

if Jokenpô == 'pedra' and Jogador == 'tesoura' or Jokenpô == 'papel' and Jogador == 'pedra' or Jokenpô == 'tesoura' and Jogador == 'papel' : 
    print('Jokenpô ganhou')

elif Jogador == 'pedra' and Jokenpô == 'tesoura' or Jogador == 'papel' and Jokenpô == 'pedra' or Jogador == 'tesoura' and Jokenpô == 'papel' :
    print(f' Jogador Ganhou')

elif Jokenpô == Jogador : 
    print('Empate')

else :
    print('ERRO.TENTE NOVAMENTE.')
