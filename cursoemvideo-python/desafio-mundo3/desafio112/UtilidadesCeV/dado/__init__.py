
def leiaDinheiro(n):
    v = False
    while v == False:
        us = str(input(n)).strip().replace(',', '.')
        if us.isnumeric():
            us = float(us)
            v = True 
        else:
            print("ERRO. tipo de dado inválido")
    return us 