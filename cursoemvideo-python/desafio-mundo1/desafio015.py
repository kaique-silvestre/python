# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ por dia e R$0,15 por Km rodado.

d = int(input('Por quantos dias o carro foi alugado '))
km = int(input('Quantos Km foram rodados durante esses dias? '))

ppd = d * 60
ppkm = km * 0.15
# pf = ppd + ppkm

print(f'{d} dias alugados custaram R${ppd} e {km}Km rodados custaram R${ppkm} o valor final do aluguel fica em R${ppd + ppkm}')