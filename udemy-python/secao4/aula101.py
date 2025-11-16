def somar(x, y):
   return  x + y

def multiplicar(x, y):
    return x * y

def executar(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna
    

soma_cinco = executar(somar, 5)

print(soma_cinco(5))