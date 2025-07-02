from threading import Thread
from time import sleep

def tempo(tempo):
    sleep(tempo)
    print("Thread Excutada")

# A cirgula é necessária para que o python interprete o elemento como uma tupla, sem a virgula o elemento é interpretado como uum int 
t1 = Thread(target=tempo, args=(5,))
t1.start()

# Faz com que a Thread seja juntada ao bloco prinicpalmde código, ou seja as coisas irão acontcer em sequencia
# t1.join()

for i in range(10):
    sleep(1)
    print(i)