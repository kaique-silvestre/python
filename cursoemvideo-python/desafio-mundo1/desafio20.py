# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.

from random import shuffle

grupos = shuffle(['Grupo1', 'Grupo2', 'Grupo3', 'Grupo4'])
print(grupos)