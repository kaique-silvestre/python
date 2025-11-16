# Aumente o preço dos produtos a seguir em 10%
# Gere novos_produtos or deep copy

# Ordene os produtos por nome descrecente (do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy

#Ordene os produtos por preço crescente 
# Gere produtos_prdenados_por_preco por deep copy

from pprint import pprint

produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90}

]

novos_produtos = [{**produto, 'preco': produto['preco'] * 1.1} for produto in produtos]

pprint(novos_produtos)

produtos_ordenados_por_nome = novos_produtos[:]

produtos_ordenados_por_nome.sort(key=lambda item: item['nome'], reverse=True)

pprint(produtos_ordenados_por_nome)