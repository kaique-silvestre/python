cont = 0
impar = 0
n = 1
while n != 0:
    n = int(input('Número: '))
    if n != 0:
        if n % 2 == 0 and n != 0:
            cont += 1
        else:
            impar += 1
print(f'A quantidade de números pares mostrado é: {cont}')
print(impar)
print('FIM')
