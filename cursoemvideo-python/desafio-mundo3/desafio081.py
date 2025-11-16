# Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso mostre:
# A) Quantos números foram digitados 
# B) A lista de valores, ordenada de forma decrescente 
# c) Se o valor 5 foi digitado e está ou não na lista 

lista = list()
while True:
    num = int(input('Números a serem inseridos na lista [0 p/ finalizar]: '))
    if num == 0:
        break
    lista.append(num)

print(f'A quantidade números na lista é: {len(lista)}')
print(f'A lista ordenada de forma drecrescente é: {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'O número 5 está na lista na {lista.index(5)+1}º posição')
else:
    print('O número 5 não está na lista')