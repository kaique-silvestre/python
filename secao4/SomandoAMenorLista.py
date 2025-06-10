"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""


def IsThatTheMinorList(FirstList, SecondList):
    if len(FirstList) < len(SecondList):
        return FirstList
    else:
        return SecondList


def sum_by_minor_lenght(FirstList, SecondList):
    TheMinorList = IsThatTheMinorList(FirstList, SecondList)
    new_list = list()
    cont = 0
    for item in TheMinorList:
        new_list.append(item + FirstList[cont])
        cont += 1
    return new_list


lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

print(sum_by_minor_lenght(lista_a, lista_b))
