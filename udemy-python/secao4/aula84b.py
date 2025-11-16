# Mapeamento de dados com list comprehension

produtos = [
    {'nome': 'p1', 'preço': 20},
    {'nome': 'p2', 'preço': 10},
    {'nome': 'p3', 'preço': 30}
]

# Copiando o diocnário 
novos_produtos = [produto for produto in produtos]
print(novos_produtos)

# Filtrando itens a serem copiados 
novos_produtos2 = [{'preço': produto['preço']} for produto in produtos] 
print(novos_produtos2)

# Copia com desempacotamento
novos_produtos3 = [
    {**produto} for produto in produtos
]

print(novos_produtos3)

# copiando com Mudanças
novos_produtos4 = [
    {**produto, 'preço': produto['preço'] * 2} for produto in produtos
]
print(novos_produtos4)

# Copia e alterações com condições 
# 1. Desempacota um dicionário
# 2. Define que a Key 'Preço' será o iterador produto em 'preço' vezes dois
# 3. Operador ternário que tem como retorno o código anterior se produto em preço for maior que 20, caaso não retorna a lista normal
novos_produtos5 = [
    {**produto, 'preço': produto['preço'] * 2} if produto['preço'] > 20 else {**produto}
    for produto in produtos
]

print(novos_produtos5)