import json

pessoas = {
    'nome': 'Gabriel',
    'Sobrenome': 'Amorim',
    'idade': 19,
    'endereco': [
        {'endereco1':'xxx-xxx-xxx' },
        {'endereco2': 'yyy-yyy-yyy'}
    ], 
    'numero':[
        {'numero1': 11111111},
        {'numero2': 22222222}
    ],
    'numeros_favoritos': (1, 2, 3, 4, 5),
    'dev': True,
    'none': None
}


# Colocando a estrutura de dados dentro de um arquivo .json 
# with open('aula117.json', 'w', encoding='utf-8') as dado:
#     #         objeto, arquivo        
#     json.dump(pessoas, dado, indent=True)

# Carregando dados de um json para uma variável
with open('aula117.json', 'r', encoding='utf-8') as arq:
    string = json.load(arq)
    print(string)