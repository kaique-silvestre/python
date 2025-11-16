# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

x = 10
y = 10
print(f'O dobro do valor {moeda.moeda(x)} é {moeda.dobro(x, False)}')
print(f'A metade do valor {moeda.moeda(x)} é {moeda.metade(x)}')
print(f'Aumentando o valor {moeda.moeda(x)} em {y}% temos o total de {moeda.aumentar(x, y, False)}')
print(f'Diminuindo o valor {moeda.moeda(x)} em {y}% temos o total de {moeda.diminuir(x, y)}')