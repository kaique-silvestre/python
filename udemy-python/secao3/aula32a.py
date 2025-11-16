"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

try: 
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        print(f'O número {num} é par')
    else: 
        print(f'O número {num} é impar')
except Exception:
    print('ERRO. Não foi informado um número inteiro')