# faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessáriapara pintá-la, sabendo que cada litro de tinta pinta uma área de 2m² 
 
print('Bem-vindo ao programa de calculo para pintores, vamos calcular automaticamente  a area da parede e quanta tinta vai precisar para pinta-lá')

larg = float(input('Insira a Largura em m² : '))
alt = float(input('insira a altura em m² : '))

print('A área da parede é de {}m², são necessário {} litros de tintas'.format(larg * alt, (larg * alt)/2))

