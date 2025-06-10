# List comprehension

# For dentro de lista com variável de inclusão
lista = [numero for numero in range(11)]
print(lista)
# output >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# O primeiro item define o que vai estar na lista 
lista = [1 for num in range(5)]
print(lista)
# output >>> [1, 1, 1, 1, 1]


# list comprehension com operações 

lista = [num * 2 for num in range(11)]
print(lista)
# output >>> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

