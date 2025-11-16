# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado 

provisorio = list()
matrix = list()

for i in range(0, 9):
    provisorio.append((int(input(f'Coloque o {i + 1}º valor da matriz: '))))
    matrix.append(provisorio[:])
    provisorio.clear()
print('=-'*30)
print(matrix[0:3])
print(matrix[3:6])
print(matrix[6:9])
