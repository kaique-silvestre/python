# Aprimore o desafio anterior , mostrando no final:
# A) A soma de todos os valores pares digitados 
# B) A soma dos valores da terceira coluna. 
# C) O maior valor da segunda linha 

provisorio = list()
matrix = list()
soma = soma3 = 0

for i in range(0, 9):
    provisorio.append((int(input(f'Coloque o {i + 1}º valor da matriz: '))))
    matrix.append(provisorio[:])
    soma += sum(provisorio)
    if i >= 6:
        soma3 += sum(provisorio)
    provisorio.clear()

print('=-'*30)
print(matrix[0:3])
print(matrix[3:6])
print(matrix[6:9])
print('=-'*30)

print('Informações sobre a matriz:')
print(f'A soma de todos os valores é: {soma}')
print(f'O maior valor da segunda coluna é: {max(matrix[3:6])}')
print(f'A soma de todos os itens da terceira coluna é: {soma3}')
