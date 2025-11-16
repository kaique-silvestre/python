
try:
    print('programa de divisão')
    n1 = int(input('N1: '))
    n2 = int(input('N2: '))
    n3 = n1 / n2

except Exception as erro:
    print(f'Algo deu errado em {erro.__cause__}, {erro.__class__}')

else: 
    print(n3)
finally:
    print('Obrigado por usar o programa')