# É possível desempacotar os itens dentro de uma lista em diversas variáveis, desde que o desempacotamento seja feito com a mesma quantidade de itens e variáveis.
# Ou seja, se houverem 3 variáveis e 4 items na lista, haverá um erro, o mesmo se o oposto for verdade;
lista = ['Manoel', 'Marcial', 'Maciel', 'Marcos']

item1, item2, item3, item4 = lista

print(item1, item2, item3, item4)

# Se quisermos desempacotar apenas alguns itens em certas variáveis, temos que empacotar os itens a seguir em uma nova variável

lista2 = [1, 2, 3, 4]

i1, i2, *iall = lista2

print(i1, i2)
print(iall)