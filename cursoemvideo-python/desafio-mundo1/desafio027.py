# faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente. 
# Ex : Ana Maria de Souza 
# Primeiro = Ana 
# ùltimo = Souza 

nome = str(input('Seu nome completo : ')).strip().split()
print(f'Seu primeiro nome é : {nome[0]}')
print(f'Seu último nome é : {nome[-1]}')
