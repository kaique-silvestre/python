perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4' 
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25' 
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5' 
    }
]

acerto = 0
cont = 0
while cont < len(perguntas):

    for item in perguntas[cont]['Pergunta']:
        print(item, end='')
    print()
    for num, options in enumerate(perguntas[cont]['Opções']):
        print(f'{num}) {options}')
        
    resultado = int(input('Resultado: '))
    if perguntas[cont]['Opções'][resultado] == perguntas[cont]['Resposta']:
        print('ACERTOU')
        acerto += 1
    else:
        print('ERROU')
    cont+=1
    print()
print(f'Você acertou {acerto} de {len(perguntas)}')


