# dir, hasattr e getattr em python

# dir() traz todos os atributos dentro do objeto no parâmetro

# Podemos analisar isso no mododebug em "debug console" com um breakpoint em um print com o objeto. digitando: dir(objeto) vemos todos os seus atributos

string = 'Mario'
print(string)

# hasattr() chega se o objeto tem determinado método dentro 

if hasattr(string, 'upper'):
    print('Existe upper dentro do objeto')
    print(string.upper())