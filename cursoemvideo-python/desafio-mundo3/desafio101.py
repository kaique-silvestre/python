# Crie um programa que tenha uma função chmada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa. retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL, OBRIGÁTORIO nas eleições

def voto(a):
    from datetime import datetime
    x = datetime.today().year - a 
    if x >= 18:
        return 'Voto obtigatório'
    elif 16 <= x < 18 or x > 65:
        return 'Voto opcional'
    else:
        return 'Voto Negado'

a = int(input('Ano de nascimento: '))
print(voto(a))
