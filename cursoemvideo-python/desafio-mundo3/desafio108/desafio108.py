# Adapte o código do desafio107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado 

import moeda

x = 10
y = 10
print(f'O dobro do valor {moeda.moeda(x)} é {moeda.moeda(moeda.dobro(x))}')
print(f'A metade do valor {moeda.moeda(x)} é {moeda.metade(x)}')
print(f'Aumentando o valor {moeda.moeda(x)} em {y}% temos o total de {moeda.moeda(moeda.aumentar(x, y))}')
print(f'Diminuindo o valor {moeda.moeda(x)} em {y}% temos o total de {moeda.moeda(moeda.diminuir(x, y))}')