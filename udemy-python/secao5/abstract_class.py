from abc import ABC, abstractmethod

class Animal:
    @abstractmethod
    def som(self):
        print('som pradão')

class Cachorro(Animal):
    def som(self):
        print('Au Au')

class Gato(Animal):
    def som(self):
        print('Miau Miau')

vira_lata = Cachorro()
gato_preto = Gato()

vira_lata.som()
gato_preto.som()

