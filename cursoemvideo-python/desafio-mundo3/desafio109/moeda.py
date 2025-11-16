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

def moeda(n=0, m='R$'):
    return f'{m}{n}'


    
