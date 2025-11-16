# Crie um programa que vai ler varios números e colocar em uma lista
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas 

principal = list()
pares = list()
impares = list()

while True: 
    num = int(input('Insira números para a lista [0 p/ finalizar]: '))
    if num == 0:
        break
    principal.append(num)

for i in principal:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'A lista completa é: {principal}')
print(f'A lista com elementos pares é: {pares}')
print(f'A lista com elementos impares é: {impares}')
