class Carro:
    def __init__(self, motor):
        self.motor = motor # Carro é criado com o param. motor, com a intenção de receber um objeto (uma instância) da classe 'motor'

class Motor:
    def ligar(self):
        print('Ligando Motor')


motor = Motor()
carro = Carro(motor)
carro.motor.ligar() # Dando ao parâmetro 'motor' do construtor da classe 'carro' uma instância da classe 'Motor' temos acesso aos métodos de 'Motor' assim podemos em no objeto 'carro' (instância de Carro) acessar o atributo 'motor' que é a Classe 'Motor' e contém o método 'ligar'
