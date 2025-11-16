# escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão : 
# 1 para binário
# 2 para octal 
# 3 para hexadecimal 

num = int(input('Digíte um número inteiro : '))
print('''Escolha uma das bases para a converção
[ 1 ] - Converter para binário
[ 2 ] - converter para octal 
[ 3 ] - converter para Hexadecimal
''')
opção = int(input('Sua opção : '))
if opção == 1 :
    print(f'O número {num} conterido para binário é igual a {bin(num) }')

elif opção == 2 : 
    print(f'O número {num} convertido para octal é igual a {oct(num)}')
elif opção == 3 :
    print(f'o número {num} convertido para hexadecimal é igual a {hex(num)}')
else :
    print('ERRO. TENTE NOVAMENTE.')