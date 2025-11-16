# desenvolva um programa que leia seis números interios e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.
# Comentario : Mais uma vez acredito que minha solução não é a mais sofisticada, ansioso para ver como guanabara vai resolver 
save = 0
cont = 0
for s in range(1, 7):
    num = int(input(f'Digite o {s}º valor: '))
    if num % 2 == 0:
        cont += 1
        save += num 
if cont == 0:
    print('Você não digitou números pares')
else :     
    print(f'Você digitou {cont} pares que somados são igual: {save}')

# Bem melhor :D