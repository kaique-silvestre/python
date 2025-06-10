def genarator(n=0):
    yield 1 # Pausa
    print('Continuando...')
    yield 2 
    print('continuando mais uma vez...')
    yield 3
    print('Agora terminando...')

for n in genarator(n=0):
    print(n)