# Faça um algoritmo que leia a prestação de um produto e mostre seu novo preço com 5% de desconto 

pr = float(input('insira o valor do produto para calcularmos o desconto : R$')) 

print('O produto de R${}, com um desconto de 5% equivalente a R${:.2f}, portanto sai por R${:.2f}'.format(pr, 0.05 * pr, pr - (0.05 * pr)))