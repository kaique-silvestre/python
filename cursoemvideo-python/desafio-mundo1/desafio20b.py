# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.

from random import shuffle

ordem1 = input('Primeiro Grupo : ')
ordem2 = input('Segundo Grupo : ')
ordem3 = input('terceiro grupo : ')
ordem4 = input('Quarto grupo : ')

lista_de_apresentação = [ordem1, ordem2, ordem3, ordem4]

shuffle(lista_de_apresentação)

print(f'A ordem de apresentação dos grupos é : {lista_de_apresentação}')