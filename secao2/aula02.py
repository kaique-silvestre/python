#Argumentos e Separadores 
# É possível colcoar mais de um argumento no "print()"

print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

print()

# É possível escolher como queremos separar os argumentos com sep=''

print(1, 2, 3, 4, 5, sep='.')
print(6, 1, 8, 9, 10, sep=', ')
print(11, 12, 13, 14, 15, sep=' > ')

print()

# É possível escolher o que sucede fim de um print() com end=''
# Por padrão é "\n" que significa quebra de linha, porém podemos alterar

print(1, 2, 3, sep=', ', end='-')
print(4, 5, 6, sep=', ', end='#')
print(7, 8, 9)