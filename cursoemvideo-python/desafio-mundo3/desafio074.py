# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla 

from random import sample

tupla = tuple(sample(range(100),5))
print(f'A tupla gerada foi: {tupla}')
print(f'O maior número é: {max(tupla)}')
print(f'O menor número é: {min(tupla)}')