# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido 

from random import choice 
sorteado1 = input('Nome do Primeiro Aluno : ')
sorteado2 = input('Nome do Segundo Aluno : ')
sorteado3 = input('Nome do Terceiro Aluno : ')
sorteado4 = input('Nome do Quarto aluno : ')
print(f'O aluno sorteado é : {choice([sorteado1, sorteado2, sorteado3, sorteado4])}')