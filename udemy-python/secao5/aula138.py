class Jogador:
    def __init__(self, nome, overall):
        self.nome = nome 
        self.overall = overall
    
    def tocar(self):
        print('Tocando')

    def chutar(self):
        print('Chutando')

class Goleiro(Jogador):
    def __init__(self, nome, overall):
        super().__init__(nome, overall)

    def defender(self):
        print('Agarrando a bola')

class Linha(Jogador):
    def fazer_gol(self):
        print('GOOOOOOL')

jogador01 = Goleiro('Aranha', 98)
jogador02 = Linha('CR7', 99)

jogador01.chutar()
jogador01.defender()

jogador02.chutar()
jogador02.fazer_gol()