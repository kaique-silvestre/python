try:
    valor_1 = int(input('Digite o primeiro valor: '))
    valor_2 = int(input('Digite o segundo valor: '))

    if valor_1 > valor_2:
        print(f'O primeiro valor: {valor_1} é maior que o segundo valor: {valor_2}')
    elif valor_1 < valor_2:
        print(f'O segundo valor: {valor_2} é maior que o primeiro valor: {valor_1}')
    else: 
        print('Ambos valores são iguais')
except Exception as Erro:
    print(Erro.__class__)
