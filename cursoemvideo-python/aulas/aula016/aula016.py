lanches = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# for cont in range(0, len(lanches)):
#     print(f'Eu vou comer {lanches[cont]} na posção {cont}')

#  Resultado no terminal:

# for comidas in lanches:
#     print(f'Eu vou comer {comidas}')

# # Resultado no Terminal:

# for cont in range(0, len(lanches)+1):
#     print(cont)

for pos, comida in enumerate(lanches):
    print(f'O valor {comida}, está na posição {pos}')


# Concatenação de tuplas:
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b 
print(c)