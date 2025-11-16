# Reescreva a função Leiaint() que fizemos no desafio104, incluindo agora a possibilidade da digitação de um número de tipo invalido. Aproveite e crie a função LeiaFloat() com a mesma funcionalidade.

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

def LeiaFloat(n):
    while True:
        try:
            num = float(input(n))
            return num
        except ValueError:
            print('ERRO. Houve algum problema com os valores digitados')
        except KeyboardInterrupt:
            print('O usuário preferiu não inserir os dados')
            return 0
        except Exception as erro:
            print(f'ERRO. houve algum problema:{erro.__class__}, tente novamente.')

            
m = LeiaInt('Digite um número inteiro: ')
print(f'O número digitado foi {m}')
n = LeiaFloat('Digite um número de ponto flutuante: ')
print(f'O número digitado foi {n}')

