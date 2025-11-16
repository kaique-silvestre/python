# Crie um programa onde o usuario possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())
# No final mostre a lista ordenada na tela 

lista = list()
cont = 0

for c in range(0, 5):
        num = int(input('N: '))
        cont += 1
        if cont == 1:
            lista.append(num)
        else:
            for i in lista:
                if num == i:
                        lista.insert(i+1, num)
                elif num > i:
                    lista.append(num)
                elif num < i:
                    lista.insert(i-1, num)

print(lista)