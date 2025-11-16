# Faça um programa que leia um número inteiro e diga se ela é ou não um número primo

primo = int(input('Vericador de números primos: '))

if primo == 1 :
    print('Não é primo')
elif primo == 2 or primo == 3 or primo == 5 or primo == 7 :
    print('O número é primo')
elif primo % 2 != 0 and primo % 3 != 0 and primo % 5 != 0 and primo % 7 != 0 :
    print('O número é primo')
else : 
    print('Não é primo')

# Apesar de até agora não ter resolvido os exercícios da forma mais bonita, com os conceitos de for que ele ensinou, pelo menos estou me virando.