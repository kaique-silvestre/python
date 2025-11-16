from abc import ABC, abstractmethod
from random import randint

class Bank:
    accounts_database = dict()

    def account_registration(self, account):
        self.accounts_database[f'{account.id}'] = {
            'Name': account.client.name,
            } 

class Account(ABC):
    def __init__(self, client):
        self._id = self.create_id()
        self.client = client
        self._balance = 0

    @abstractmethod
    def withdraw(self):
        pass

    def deposit(self, value, bank):
        if str(self.id) in bank.accounts_database:
            self._balance += value 
            return True 
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, balance):
        raise PermissionError("You cannot modify the balance")

    def balance_validadation(self, value):
        if self._balance < value:
            raise ValueError("Declined Transcation: Balance insufficient")
        
    def id_validation(self, id):
        if not isinstance(id, int):
            raise TypeError("Id must be an integer")
        
    def create_id(self):
        var = ''
        for number in range(9):
            var += str(randint(0, 9))
        var = int(var)
        return var
    
    def __repr__(self):
        balance = self._balance
        number = self._id
        string = f"{number}, {balance}"
        return string


        
class SavingAccount(Account):
    def withdraw(self, value, bank: Bank):
            if str(self.id) in bank.accounts_database:
                self.balance_validadation(value)
                self._balance -= value

class CurrentAccount(Account):
    def __init__(self, client):
        super().__init__(client)
        self.limite = 100

# Sistema que permite a retirada de até R$100 a mais da conta corrente 
## Retirada de R$150 de uma conta com R$100
### - Verificar se o valor para deposito é > que o valor em conta
### - Veririficar se o valor conta + limite cobre a retirada
### - Descontar todo valor da conta tirar R$100 de R$100 
### - Descontar o restante do limite, ou seja tirar R$50 do limite de 100
### - O limitre precisará ser R$50 
    def withdraw(self, value, bank):
        if value > self.balance:
            if value <= self.balance + self.limite:
                self._balance -= value
                self.limite += self.balance
                self._balance = 0
                return True
            raise Exception()
        if value <= self.balance:
            self._balance -= value
            return True
    
    def deposit(self, value, bank):
        if str(self.id) in bank.accounts_database:
            if self.limite < 100:
                new_value = self.limite + value
                if new_value > 100:
                    sobra = new_value - 100
                    self.limite = 100
                    self._balance += sobra
                    print(self.limite)
                    print(self.balance)
                    return True
                else:
                    self.limite = new_value
                    return True
            if self.limite == 100:
                self._balance += value





class Person(ABC):
    def __init__(self, name):
        self._name = name 

    @abstractmethod
    def __repr__(self):
        pass  

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        self._name = name 
        return True 
    
class Client(Person):
    def __init__(self, name):
        super().__init__(name)

    def __repr__(self):
        name = self._name
        string = f"{name}"
        return string


    
itau = Bank()
 
cliente = Client('Kaique')
conta = SavingAccount(cliente)

itau.account_registration(conta)

conta.deposit(-200, itau)
print(conta.balance)
