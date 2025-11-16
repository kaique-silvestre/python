# Faça um mini-sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuario digitar a palavra 'FIM', O programa se encerrara 
# Obs = use cores 

from time import sleep 

def escreva(x):
    print('~'*len(x))
    print(f'{x}')
    print('~'*len(x))

while True:
    escreva('sistema de ajuda python')
    ajuda = str(input('Função ou Biblioteca > '))
    if ajuda == 'fim':
        break
    escreva(f'Acssando manual do comando {ajuda}')
    sleep(0.3)
    print(help(ajuda))
print('.....Obrigado por usar o programa.....')
print('......FINALIZANDO CONEXÃO.......')