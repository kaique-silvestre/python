# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento 

sa = float(input('Insira o antigo salário para consultar o aumento : R$'))

print('Seu salário recebeu um reajuste de R${}, Seu novo salário é de R${}'.format(sa * 0.15, sa + (sa * 0.15)))

