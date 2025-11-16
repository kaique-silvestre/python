# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa 
co = float(input('Insira o valor do cateto oposto :'))
ca = float(input('insira o valor do cateto adjacente'))

hipotenusa = ((co**2) + (ca**2))**(1/2)

print(f'O valor da hipotenusa é {hipotenusa:.2f}')