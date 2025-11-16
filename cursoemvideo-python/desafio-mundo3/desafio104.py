# Crie um programa que tenha uma função leiaint(), que vai funcionar de forma semelhante à função input() do python, só que fazendo a validação para aceitar apenas um valor númerico
# EX: n = leiaint('Digite um n')

def LeiaInt(n): 
    while True:
        num = str(input(n))
        if num.isnumeric() == True:
            return(num)
        else:
            print('Erro. O valor digitado não é válido, apenas números são aceitos.') 


c = LeiaInt('Digite um número: ')
print(f'Você digitou o número {c}')

