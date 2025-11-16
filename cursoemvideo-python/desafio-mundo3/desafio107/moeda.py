# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use alguma dessas funções

def dobro(n):
    n *= 2
    return n 

def metade(n):
    n /= 2
    return n 

def aumentar(n, m):
    n += n * (m/100)
    return n 

def diminuir(n, m):
    n -= n * (m/100)
    return n


    
