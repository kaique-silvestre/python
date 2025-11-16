# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo 
reta1 = int(input('Insira o tamanho da reta : '))
reta2 = int(input('Insira o tamanho da reta : '))
reta3 = int(input('Insira o tamanho da reta : '))
if reta1 < reta2 + reta3 : 
    print('Pode-se formar um traingulo com essas retas')
else : 
    print('Não podemos formar um traingulo com retas desses valores')