"""
- Exercícios com classes 
1 - Crie uma classe 'Carro'
2 - Crie uma classe 'Motor'
3 - Crie uma classe 'Fabricante'
4 - Faça a ligação entre carro e motor
- Obs: Um motor pode ser de vários carros
5 - Faça a ligação entre Carro e Fabricante
Obs.: Um fabricante pode fabricar vários carros
- Exiba o nome do carro, motor e fabricantes na tela 

"""

class Carro:
    def __init__(self, motor, fabricante):
        self.motor = motor
        self.fabricante = fabricante
    
    def show_atriutes(self):
        print('Nome do Fabricante:', self.fabricante.nome_fabricante)
        print('Nome do Motor:', self.motor.nome_motor)

class Motor:
    def __init__(self, nome_motor):
        self.nome_motor = nome_motor 
    

class Fabricante:
    def __init__(self, nome_fabricante):
        self.nome_fabricante = nome_fabricante


motor = Motor('V8')
fabricante = Fabricante('Tesla')
carro01 = Carro(motor, fabricante)

carro01.show_atriutes()



