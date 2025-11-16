def linha(tam = 42):
    return '-' * tam

def LeiaInt(n): 
    while True:
        try:
            num = int(input(n))
            return num
        except ValueError:
            print('ERRO. tente novamente, houve algum problema com os Valores digitado')
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados')
            return 0
        except Exception as erro:
            print(f'ERRO. tente novamente:{erro.__class__}')


def cabeçalho(txt):
    print(linha())
    print(txt)
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1 
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = LeiaInt('Sua opção: ')