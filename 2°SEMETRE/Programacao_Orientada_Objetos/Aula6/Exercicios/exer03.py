class ContaBancaria:
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = 0

    def depositar(self, valor, senha):
        if senha == self.senha:
            self.saldo += valor
            print('Deposito realizado com sucesso')

        else:
            print('Senha incorreta')

    def sacar(self, valor, senha):
        if senha == self.senha:
            if valor <= self.saldo:
                self.saldo -= valor
                print('Saque reliazado')
                
            else:
                print('Saldo insuficente')
        
        else:
            print('Senha incrreta')


conta1 = ContaBancaria(78903, 'Rodrigo Rocha', 123)

valor = float(input('Digite valor para deposito : '))
senha = int(input('Digite sua senha : '))

conta1.depositar(valor, senha)
print('Saldo : ', conta1.saldo)

valor = float(input('Digite valor para saque : '))
senha = int(input('Digite sua senha : '))

conta1.sacar(valor, senha)
print('Saldo : ', conta1.saldo)


