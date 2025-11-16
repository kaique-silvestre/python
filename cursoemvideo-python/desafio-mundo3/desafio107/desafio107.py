# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use alguma dessas funções

import moeda

x = 10
y = 10
print(f'O dobro do valor {x} é {moeda.dobro(x)}')
print(f'A metade do valor {x} é {moeda.metade(x)}')
print(f'Aumentando o valor {x} em {y}% temos o total de {moeda.aumentar(x, y)}')
print(f'Diminuindo o valor {x} em {y}% temos o total de {moeda.diminuir(x, y)}')

