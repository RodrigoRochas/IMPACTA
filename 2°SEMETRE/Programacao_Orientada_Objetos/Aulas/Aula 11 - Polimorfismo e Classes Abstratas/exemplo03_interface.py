# Uma interface é uma classe abstrata que possui apenas métodos abstratos.

# Uma interface define um modelo a ser seguido pelas classes filhas, definindo
# os atributos e métodos que são obrigatórios.

# As classes herdeiras serão obrigadas a implementar os métodos abstratos.


from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def consultar_saldo(self):
        pass


# A classe é obrigada a implementar os métodos abstratos da interface
class ContaPoupanca(Conta):
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def consultar_saldo(self):
        print('Saldo: ', self.saldo)


# A classe é obrigada a implementar os métodos abstratos da interface
class ContaEspecial(Conta):
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def consultar_saldo(self):
        print('Saldo: ', self.saldo)
