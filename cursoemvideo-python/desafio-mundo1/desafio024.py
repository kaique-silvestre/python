# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

city = str(input('Insira o nome da sua cidade : ')).strip()
big_city = city.upper()
bscity = big_city.split() 
print('SANTO' in bscity[0])