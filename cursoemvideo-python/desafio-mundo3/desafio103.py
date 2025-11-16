# Faça um programa que tenha uma função chamada ficha(), que recebe dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou
# O programa devrá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente 

def ficha(a, b):
    if len(a) == 0:
        a = 'Desconhecido'
    if len(b) == 0:
        b = '0'
    return f'O jogador {a} marcou {b}'

a = str(input('Nome do jogador: ')).strip().title()
b = str(input('Quantos gols foram marcados: ')).strip()
print(ficha(a, b))
