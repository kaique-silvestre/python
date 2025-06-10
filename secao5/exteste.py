
# Exercício com abstração, Herança, Encapsulamento e Polimorfismo 
"""
Criar um sistema bancário (extremamente simples) que tem clientes, contas e um banco. A ideia é que o cliente tenha uma conta (Poupança ou Corrente) e que possa sacar/depositar nessa conta. Contas correntes tem um limite extra
"""

"""
CONTA(ABC)
    ContaCorrente
    ContaPoupanca

PESSOA(ABC)
    Cliente 
        Cliente -> Conta

BANCO 
    Banco -> Cliente 
    Banco -> Conta 
"""

"""
Dicas:

Criar classe cliente que herda de classe Pessoa (HERANÇA) (X)
    Pessoa tem nome e idade (com getters) (X)
    Cliente TEM conta (Agregação de classe ContaCorrente ou ContaPoupança) (X)
Criar classes ContaPoupanca e contaCorrente que herdam de Conta (X)
    ContaCorrente deve ter um limite extra
    Contas tem agências, número de conta e saldo (X)
    Contas devem ter métodos para depositos (X)
    Conta (SuperClasse) deve ter o método sacar abstratao (Abstração e polimorfismo - as subclasses que implementam o método sacar) (X)
Banco será  responsável autenticar o cliente e as contas da seguinte maneira: (X)
    Banco tem contas e  clientes (Agregação) (X)
    * Checar se a agência é daquele banco 
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco 
Só será possível sacar se passar na autenticação do banco (descrita acima) (X)
banco autentica por um método 
"""

"""
Diagrama de resolução 
    - Importar abc para usar (ABC e abstractmethod) (X)
        - Lembrar que abstract method é um decorador (X)
    
    - Criar classe abstratata Conta (X)
        - Contas tem agência, número de conta e saldo (X)
        - Criar método Deposito (X)
        - Criar metódo sacar e decora-lo (X)
            - Criar subclasse 'Conta Corrente' (X)
            - Criar subclasse 'Conta Poupança' (X)
            - implementar Saldo em ambas subclasses com super().__init__() (X)
    
    - Criar classe Abstrata Pessoa
        - Pessoas tem como param. nome e idade (X)
        - Nome e idade serão implementados com getter e setter (X)
            - Criar subclasse Cliente (X)
            - Clientes tem nomes e idade  (X)
                - Cliente tem uma conta (X)
                - Criar relação de agregação (X)
        
    - Criar classe Banco
        - Banco agrega clientes (X)
            - Criar propriedade de lista de clientes (X)
        - Banco agrega contas (X)
            - Criar listas de conta inicialmente (X)
        - Implementar sistema (Método) de autenticação pra conta e cliente
            - Checar se agência é daquele banco
            - Checar se cliente é daquele banco
            - Chechar se a conta é daquele banco 
        - Se checagem for True liberar saque


        2° Etapa
        - Implemntar deposito (X)
            - o deposito adicione ao saldo da conta 
        - Implementar saque (X)
            - O saque deverar subitrair ao valor da conta


        - Criar interface no 'sistema' banco para cadastramento de cliente
        - Criar interface no 'sistema' banco para cadastramento de conta 
        - Criar método que adiciona cliente e banco em uma base de dados
        - Criar 'interface' de saque no banco
        - Criar 'interface' de deposito no banco
        - Criar método de autenticação para saque e deposito


"""

from abc import ABC, abstractmethod
import random



class Bank:
    list_of_clients = list()
    dict_of_clients = dict()


    def gid(self):
        st = ''
        for x in range(9):
            st += str(random.randint(0, 9))
        return int(st)

class Account(ABC):
    @abstractmethod
    def __init__(self, id):
        self.agency = 1
        self.id = id
        self._balance = 0
    
    @abstractmethod
    def deposit(self, value):
        self._balance += value 

    @abstractmethod
    def withdraw(self, value):
        self._balance - value

    def validation(self):
        ...

class SavingAccount(Account):
    def __init__(self, id):
        super().__init__(id)

    def deposit(self, value):
        return super().deposit()
    
    def withdraw(self):
        return super().withdraw()
    
    def __repr__(self):
        string = f'{self.account_id, self._balance, self.agency}'
        return string

class CheckingAccount(Account):
    """Current Account in UK"""
    def __init__(self, account_id):
        super().__init__(account_id)
    





class Person(ABC):
    @abstractmethod
    def __init__(self, name, age):
        self._name = name 
        self._age = age

    @property
    def name(self):
        return self._name
        
    @name.setter
    def set_name(self, name):
        self._name = name 
        return True 
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age >= 18:
            self._age = age 
        else:
            raise Exception() 
 

class Client(Person):
    def __init__(self, name, age, account):
        super().__init__(name, age)
        self.account = account

    def __repr__(self):
        string = f'{self.name}, {self.age}, {self.account}'
        return string
    
    
#################

# Como integrar a classe banco com as demais?

conta = SavingAccount(1)
cliente = Client('Kaique', 20, conta)
itau = Bank()

conta2 = SavingAccount(2)
cliente2 = Client('Mario', 50, conta2)


def registration(cliente):
    itau.dict_of_clients[f'{cliente.account.id}'] = {
        'Name': cliente.name,
        'Age': cliente.age
    }


registration(cliente)
registration(cliente2)


def validation(id):
    if str(id) in itau.dict_of_clients.keys():
        return True 

var = validation(1)

print(var)



cliente.account.deposit(100)

print(itau.dict_of_clients)