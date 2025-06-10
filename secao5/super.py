class A:
    def metodo(self):
        print('Método A')

class B(A):
    def metodo(self):
        super().metodo()
        print('Método B')

objectB = B()
objectB.metodo()