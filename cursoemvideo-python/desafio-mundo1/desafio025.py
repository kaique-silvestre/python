# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome 

tem_silva = str(input('Insira seu nome completo : ')).strip()
sts = tem_silva.upper()
print('SILVA' in sts)