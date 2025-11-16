# Extração de dicionário
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'souza'
}

dados = {
    'idade': 20,
    'altura': 1.7
}

pessoa_completa = {**pessoa, **dados}

#print(pessoa_completa)

# Argumentos nomeados com kwargs

def mostrar_dicionario(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, ':', valor)

mostrar_dicionario(**pessoa, **dados, sexo='feminino')
