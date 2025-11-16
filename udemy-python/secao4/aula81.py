"""
Função lambda em python
É uma função como qualquer outra. porém, são funções anônimas que contém apenas uma linha. Ou seja, tudo deve ser contido dentro de uma ínica expressão

"""

lista = [
    {'nome': 'Luiz', 'sobrenome': ''},
    {'nome': 'Alice', 'sobrenome': 'Carneiro'},
    {'nome': 'Maria', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'}
]

lista.sort(key=lambda item: item['nome'])

print(lista)