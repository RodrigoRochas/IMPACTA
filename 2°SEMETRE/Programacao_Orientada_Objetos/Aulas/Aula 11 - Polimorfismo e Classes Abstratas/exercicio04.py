from abc import ABC


class Conta(ABC):
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def consultar_saldo(self):
        print('Saldo: ', self.saldo)

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print('Saldo é insuficiente')


class ContaCorrente(Conta):
    pass


class ContaPoupanca(Conta):
    pass


class ContaCorrenteEspecial(Conta):
    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("ERRO: saldo + limite são insuficiente")


contacorrente = ContaCorrente(123, "Paulo", 100)
contacorrente.sacar(200)
contacorrente.consultar_saldo()
print('----------------------------')

contaespecial = ContaCorrenteEspecial(555, "Paulo", 100, 300)
contaespecial.sacar(200)
contaespecial.consultar_saldo()
print('----------------------------')

contapoupanca = ContaPoupanca(333, "João", 100)
contapoupanca.sacar(200)
contapoupanca.consultar_saldo()
