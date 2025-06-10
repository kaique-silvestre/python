lista_de_nomes = ['maria', 'tiago', 'sara', 'mateus', 'jorlan', 'hercules', 'heitor']


indice = 0
for items in lista_de_nomes:
    print(indice, items)
    indice += 1

# Mas também podemos fazer::

for pos, items in enumerate(lista_de_nomes):
    print(pos, items) 
