class Pessoa():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def exibir_dados(self):
        print(f'ID : {self.id}')
        print(f'NOME : {self.nome}')
        

class PessoaFisica(Pessoa):
    def __init__(self, id, nome, rg, cpf):
        super().__init__(id, nome)
        self.rg = rg
        self.cpf = cpf

    def exibir_dados(self):
        super().exibir_dados()
        print(f'RG : {self.rg}')
        print(f'CPF : {self.cpf}')


class PessoaJuridica(Pessoa):
    def __init__(self, id, nome, cnpj):
        super().__init__(id, nome)
        self.cnpj = cnpj

    def exibir_dados(self):
        super().exibir_dados()
        print(f'CNPJ : {self.cnpj}')

print('*' * 30)
print(f'PESSOA NORMAL')
pessoaN = Pessoa(1, 'Olivia')
pessoaN.exibir_dados()

print('*' * 30)
print(f'PESSOA FISICA')
pessoaF = PessoaFisica(2, 'rodrigo', '56.505.492-2', '506.895.528-07')
pessoaF.exibir_dados()

print('*' * 30)
print(f'PESSOA JURIDICA')
pessoaJ = PessoaJuridica(3, 'Noelma', '45.0505.64565')
pessoaJ.exibir_dados()
