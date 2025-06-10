"""
args - argumentos não nomeados 
*args - desempacotamento/empacotamento de args
"""
# Lembre-se de (des)empacotamento
pacote1, pacote2, *resto = 1, 2, 3, 4 
print(pacote1, pacote2, resto)

# (des)pacotamento em funções
def soma(*args):
    acumulador = 0
    for num in args:
        acumulador += num
    return acumulador

print(soma(1, 1, 1, 1))