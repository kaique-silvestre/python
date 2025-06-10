# Filtros em list comprehesion
# Filtros: incluir determinada coisa se determinada condição for True   (Não tem else)
# Condição a antes do for são mapping
# Condições após o for são Filtros 

from pprint import pprint

# Filtro de List comprehesion que vai incluir todo número (n) de 0 a 100, com o filtro defino que apenas quero números impares 
lista = [n for n in range(101) if n % 2 != 0]
pprint(lista)