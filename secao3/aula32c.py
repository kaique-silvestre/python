"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


nome = len(input('Digite seu nome: ').strip())
if nome <= 4:
    print('Seu nome é curto')
elif nome <= 6:
    print('Seu nome é normal')
elif nome >= 7:
    print('Seu nome é muito grande')