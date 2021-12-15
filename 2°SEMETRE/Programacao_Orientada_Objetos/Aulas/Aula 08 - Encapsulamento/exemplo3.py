class ContaBancaria:
    def __init__(self, numero, titular, senha):
        # atributos publicos
        self.numero = numero
        self.titular = titular
        # atributos privados
        self.__senha = senha
        self.__saldo = 0

    def get_saldo(self, senha):
        if self.__validar_senha(senha):
            return self.__saldo

    def depositar(self, valor, senha):
        if self.__validar_senha(senha):
            self.__saldo += valor

    def sacar(self, valor, senha):
        if self.__validar_senha(senha):
            self.__saldo -= valor

    # Método privado (só pode ser acessado pela própria classe)
    def __validar_senha(self, senha):
        if senha == self.__senha:
            return True
        else:
            print('Senha Inválida')
            return False


# cria objeto conta
conta = ContaBancaria(123, 'Francisco', 123456)

print('Numero da conta: ', conta.numero)
print('Titular da Conta: ', conta.titular)

valor = float(input('Valor do deposito: '))
senha = int(input('Informe a senha para fazer o depósito: '))
conta.depositar(valor, senha)

senha = int(input('Informe a senha para verificar o saldo: '))
print('Saldo da Conta:', conta.get_saldo(senha))
