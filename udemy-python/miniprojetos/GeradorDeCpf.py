from random import randint 

num_origem = ''
for i in range(9):
    num_origem += str(randint(1, 9))

lista_digitos = list()
mult = 10
for i in num_origem:
    lista_digitos.append(int(i) * mult)
    mult -= 1

validador = (sum(lista_digitos) * 10) % 11
validador = 0 if validador > 9 else validador

num_origem += str(validador)

lista_digitos.clear()
mult = 11
for i in num_origem:
    lista_digitos.append(int(i) * mult)
    mult -= 1

validador = (sum(lista_digitos) * 10) % 11
validador = 0 if validador > 9 else validador

num_origem += str(validador)
print(num_origem)
