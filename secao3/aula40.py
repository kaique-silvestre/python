"""
Calculadora com while

"""

while True:
        try: 
            num1 = float(input('Primeiro Número: '))
            num2 = float(input('Segundo Número: '))
            operador = input('Dgite um operador (+-*/): ') 

            if operador == '+':
                num3 = num1 + num2
                operador = '+'
            if operador == '-':
                num3 = num1 - num2
                operador = '-'
            if operador == '*':
                num3 = num1 * num2
                operador = '*'
            if operador == '/':
                num3 = num1 / num2
                operador = '/'

            print(f'{num1} {operador} {num2} = {num3} ')

        except Exception as erro:
            print('ERRO.')
            continue

        finally:
            option = input('Deseja Sair? [S/N]: ').upper().strip()
            if option == 'S':
                break
