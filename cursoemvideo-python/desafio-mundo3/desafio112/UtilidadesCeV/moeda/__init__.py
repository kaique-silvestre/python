def dobro(n, s=True):
    n *= 2
    if s == True:
        return moeda(n) 
    else:
        return n

def metade(n, s=True):
    n /= 2
    if s == True:
        return moeda(n)
    else:
        return n 

def aumentar(n, m, s=True):
    n += n * (m/100)
    if s == True:
        return moeda(n)
    else:
        return n 

def diminuir(n, m, s=True):
    n -= n * (m/100)
    if s == True:
        return moeda(n)
    else:
        return n

def moeda(n=0,  s=True):
    if s == True:
        m = 'R$'
        return f'{m}{float(n)}'
    else:
        return f'{n}'

def resumo(n, m, r, s=True):
    k = 'RESUMO'
    print('~'*30)
    print(f'{k:^30}')
    print('~'*30)
    print(f'Valor do produto: {moeda(n, s)}')
    print(f'O dobro do valor {moeda(n, s)} é {dobro(n, s)}')
    print(f'A metade do valor {moeda(n, s)} é {metade(n, s)}')
    print(f'Aumentando o valor {moeda(n, s)} em {m}% temos o total de {aumentar(n, m, s)}')
    print(f'Diminuindo o valor {moeda(n, s)} em {r}% temos o total de {diminuir(n, r, s)}')
    print('~~'*15)

    # Anotar \t para tabulçaõ 
