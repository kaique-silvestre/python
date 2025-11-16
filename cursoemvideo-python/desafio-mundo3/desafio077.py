# Um programa que tenha uma tupla com várias palavras ( não usar acento ). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ( 'uva', 'casa')

for p in palavras:
    print(f'\nNa palavra {p} temos as vogais: ', end='')
    for v in p:
        if v in 'aeiou':
            print(v, end=' ')