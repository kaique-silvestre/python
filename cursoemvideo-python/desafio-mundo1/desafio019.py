# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido 

from random import choice 

print(f'O nome aleátorio sorteado foi...{choice([ 'Mateus', 'Giovana', 'Fabiana', 'Fernanda', 'Felipe', 'Gabriel', 'Gustavo'])}')