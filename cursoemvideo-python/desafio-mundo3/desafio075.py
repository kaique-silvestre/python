# Desenvolva um programa que leia quatros valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9 
# b ) em que posição foi digitado o primeiro valor 3
# C ) Quais foram os números pares. 

tupla = tuple(int(input('Valor: '))for i in range(1, 5))
print(tupla)
print(tupla.count(9))
if tupla == 3:
    print(tupla.index(3))
else:
    print('Não há 3')
for i in tupla:
    if i % 2 == 0:
        print(i)