'''
Classe ContaBancaria

Atributos
- numero
- titular
- saldo (saldo inicial deve ser zero)

Métodos
- depositar
- sacar
- ver_saldo
'''


class ContaBancaria:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print('Saldo insuficiente')

    def ver_saldo(self):
        print('Saldo: ', self.saldo)


numero = int(input('Numero da conta: '))
titular = input('Nome do titular:')

conta1 = ContaBancaria(numero, titular)
conta1.ver_saldo()
conta1.depositar(500)
conta1.ver_saldo()
conta1.sacar(800)
conta1.ver_saldo()

conta2 = ContaBancaria(3454, 'Ana')
conta2.depositar(400)
conta2.sacar(100)
conta2.ver_saldo()