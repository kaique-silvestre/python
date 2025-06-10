"""
faça uma lista de compras com listas. O usuário deve ter a possibilidade  de inserir, apagar e listar valores de sua lista. Não permita que o programa quebre com erros de índices inexistentes.
"""
Lista_de_compras = list()

while True:
    print("\nSelecione uma opção:")
    option = input('[i]nserir [a]pagar [l]istar\t').strip().lower()

    if option == 'i':
        item = input('item: ').strip().lower()
        if len(item) == 0:
            print('Não vamos inserir itens vazios')
            continue
        Lista_de_compras.append(item)
    elif option == 'a':
        try:
            indice = int(input('\nIndice: '))
            Lista_de_compras.pop(indice)
        except ValueError:
            print('Indice apenas aceita números inteiros')
        except IndexError:
            print('Não podemos apagar um indice que não existe na lista.')

    elif option == 'l':
        if len(Lista_de_compras) == 0:
            print('Não há nada para listar. Não existem itemns na lista.')
            continue
        for indice, item in enumerate(Lista_de_compras):
            print(indice, item)
    else:
        print('\nOpção Inválida')
