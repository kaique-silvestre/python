import enum


# Criação de um enum com sintaxe simples
## Se define o tipo do enum e os valores
Semaforo = enum.Enum('semaforo', ['Vermelho', 'Amarelo', 'Verde'])


# Chamando pela chave para retorna valor
print(Semaforo(1))


# Chamando pela sintaxe de dicionário
print(Semaforo['Vermelho'])

# Chamando pelo nome
## Retorna soemente o valor sem a sintaxe de .
print(Semaforo(1).name)

# Retornando a chave 
print(Semaforo(1).value)

print()

# Criação de enum com sintaxe de classe
class Direcoes(enum.Enum):
    Esquerda = 1
    Direita = 2
    Acima = 3
    Abaixo = 4

print(Direcoes(1))
print(Direcoes['Esquerda'])
print(Direcoes(1).value)
print(Direcoes(1).name)


# Podemos usar a função enum.auto() para enumera-los automaticamente 

class Cores(enum.Enum):
    azul = enum.auto()
    roxo = enum.auto()
    preto = enum.auto()
    branco = enum.auto()

print(Cores.azul.value)
print(Cores.branco.name)