class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = list() # Atributo da classe universidade que é uma lista
    
    def matricular_aluno(self, aluno):
        self.alunos.append(aluno) # Método que adiciona o objeto recibido no parâmetro pra lista, espera-se que seja uma intância da classe Aluno

class Aluno:
    def __init__(self, nome):
        self.nome = nome 

universidade = Universidade('Upenn') # Cria um objeto da Classe universidade
aluno01 = Aluno('Mateus') # Cria um objeto da classe Aluno
aluno02 = Aluno('Vinicius') # Cria um objeto da classe Aluno

universidade.matricular_aluno(aluno01) # Objeto da classe universidade usa método para adicionar objeto da classe "aluno" para dentro da lista de alunos
universidade.matricular_aluno(aluno02) # Objeto da classe universidade usa método para adicionar objeto da classe "aluno" para dentro da lista de alunos
# Agregação é isso: Armazenar objetos de uma classe dentro de outra 
# Criamos um método onde espera-se receber objetos de outra classe, no caso alunos, para adiciona-los ao atributo que é uma lista 

# alunos: variável que recebe os itens do termos adiante "universidade.alunos", ou seja recebe o atributo alunos da classe universidade sendo que o atributo é uma lista.
# A variável 'alunos' está recebendo o atributo 'alunos' da classe 'universidade' que é uma lista e contém objetos da classe "Aluno".
# Portanto a variável 'alunos' é uma instância de 'Aluno' dessa forma temos acesso aos atributos de tal
for alunos in universidade.alunos: 
    print(alunos.nome) # Como alunos recebe a classe 'Aluno' está é uma instância de tal, assim podemos faze-lá acessar os atributos de 'Aluno'