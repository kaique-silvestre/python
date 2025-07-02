# FIFO - FIRST IN FIRST OUT
# O primeiro e entrar é o primeiro a sair
# Os itens entram pela direita e os que saem são pela esquerda
from collections import deque 

fila = deque()

# Enfileirar 
fila.append('A')
fila.append('B')
fila.append('C')

print(fila)  # Saída: deque(['A', 'B', 'C'])

# Desenfileirar 
fila.popleft()
fila.popleft()

print(fila)# Saída: deque(['C'])  # Fila com um item restante

fila.popleft()

print(fila)  # Saída: deque([])

print()

# LIFO - LAST IN LAST OUT
# Entram pela direita e saem pela direita

# As listas podem normalmente serem usadas como pilhas 

lista = list()

# Empilhar
lista.append('A')
lista.append('B')  
lista.append('C')

print(lista)  # Saída: ['A', 'B', 'C']  

lista.pop()  # Remove o último item
lista.pop()  # Remove o penúltimo item  

print(lista)  # Saída: ['A']  # Lista com um item restante

lista.pop()  # Remove o primeiro item

print(lista)  # Saída: []  # Lista vazia após remover todos os itens


# List é eficiente para pilhas, mas não é eficiente para filas, pois o método pop() é O(n) de forma que então para remover o primeiro item todos os outros da lista precisam ser realocados.

# Deques também são edicientes para pilhas 