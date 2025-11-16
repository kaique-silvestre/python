# Faça um programa que tenha uma função chamada escreva(), que recebe um texto qualquer como para metro e mostre uma mensagem com tamanho adaptável 
# ex: esxcreva('Ola, mundo')
# ex:   ~~~~~~~~~~~~~~~
#          Mensagem 
#       ~~~~~~~~~~~~~~

def escreva(x):
    print('~'*len(x))
    print(f'{x}')
    print('~'*len(x))


escreva(str(input('Escreva uma mensagem: ')))
