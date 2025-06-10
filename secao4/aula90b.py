# Generator 

# Generator: função que não aloca todos os objetos na memória de uma vez, não tem len e nem indice 

from sys import getsizeof

# Cria todos os itens e aloca na memória 
lista_comum = [n for n in range(10)]

# Não aloca todos os objetos na memória de uma vez, apenas o atual e o próximo
generator = (n for n in range(10))

# Diferença gritante de tamanho em bytes de ambos objetos 
print(getsizeof(lista_comum), getsizeof(generator))

# Para exibir um genarator
for n in generator:
    print(n)