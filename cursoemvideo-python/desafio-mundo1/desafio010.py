# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar 

crd = float(input('Bem-vindo ao programa de conversão de dolares, insira o valor em reais que vamos convertelo para dólares : '))

print('R${} podem ser convertidos em U${:.2f}'.format(crd, crd/3.27))