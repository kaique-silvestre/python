# Crie um programa que leia dois valores e mostre um menu na tela :
# [ 1 ] Somar 
# [ 2 ] Multiplicar
# [ 3 ] Maior número
# [ 4 ] Novos Números 
# [ 5 ] Sair do programa 
# Seu programa deverá realizar a operação solicitada em cada caso

print('\n---- PROGRAMA CALCULADORA SIMPLES ----')
v1 = 0
v2 = 0
op = -1

while op != 0:
    v1 = int(input('\nColoque o primeiro valor: '))
    v2 = int(input('Coloque o segundo valor: '))
    op = int(input
(""" 
[ 1 ] Somar 
[ 2 ] Multiplicar
[ 3 ] Maior número
[ 4 ] Novos Números 
[ 5 ] Sair do programa 

Escolha a opção: """))
    if op == 1:
        print(f'\nA soma dos valores é: {v1 + v2}')
    elif op == 2: 
        multiplicar = v1 * v2
        print(f'\nA multiplicação dos valores é: {v1 * v2}')
    elif op == 3:
        maior = max(v1, v2) 
        if v1 == v2:
            print('Os dois valores são iguais.')
        else:
            print(f'\nO maior valor é: {maior}' )
    elif op == 4:
         op = -1
    elif op == 5:
        break
    else:
        print('\nERRO. TENTE NOVAMENTE.')
