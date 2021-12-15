class Cliente:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.__cpf = cpf
        self.__senha = senha

    
    def get_senha(self):
        return self.__senha


class ContaBancaria:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = 0

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor, senha):
        if senha == self.cliente.get_senha():
            self.__saldo += valor
            print(f'O deposito foi depositado com sucesso')

        else:
            print(f'Senha incorreta!!')


    def sacar(self, valor, senha):
        if senha == self.cliente.get_senha():
            self.__saldo -= valor

        else:
            print(f'Senha incorreta!!!!!')


cliente1 = Cliente("Rodrigo", "1234", 123)
conta1 = ContaBancaria(123, cliente1)

print(f'Saldo = {conta1.get_saldo()}')
valor = int(input('Digite o valor para deposito : '))
senha = int(input('Digfite a senha : '))
conta1.depositar(valor, senha)


valor = int(input('Digite o valor para saque : '))
senha = int(input('Digfite a senha : '))
conta1.sacar(valor, senha)
print(f'Saldo = {conta1.get_saldo()}')