# Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor sacado ( Número inteiro ) e o programa vai informar quantas cédulas  de cada valor serão entregues. 
# OBS considere que o caixa possuie cédulas de 50, 20, 10, 1

notas50 = notas20 = notas10 = notas1 = 0

while True:
    sacar = int(input('Valor a sacar: '))
    if sacar >= 50:
        notas50 = sacar // 50
        sacar = sacar - (notas50 * 50) 
    if sacar >= 20:
        notas20 = sacar // 20
        sacar = sacar - (notas20 * 20) 
    if sacar >= 10:
        notas10 = sacar // 10
        sacar = sacar - (notas10 * 10) 
    if sacar >= 1:
        notas1 = sacar // 1
        sacar = sacar - notas1

    print(f'Você vai receber {notas50} notas de R$50')
    print(f'Você vai receber {notas20} notas de R$20')
    print(f'Você vai receber {notas10} notas de R$10')
    print(f'Você v45ai receber {notas1} notas de R$1')


    x = int(input(""" 
Deseja mais algum serviço?
[ 0 ] - Não
[ 1 ] - Sim
""" ))
    if x == 0:
        print('FINALIZANDO CONEXÃO...')
        print('CONEXÃO FINALIZADA')
        break
