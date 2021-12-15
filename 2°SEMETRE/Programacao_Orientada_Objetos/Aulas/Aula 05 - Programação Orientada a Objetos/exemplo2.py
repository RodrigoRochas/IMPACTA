'''
Criar uma classe Pessoa.
- Atributos: nome, email, telefone.
- Métodos: Um método deve exibir os dados desta pessoa.
'''


class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir_dados(self):
        print('--------------------------------------')
        print("Nome da pessoa: ", self.nome)
        print("Email da pessoa: ", self.email)
        print("Telefone da pessoa: ", self.telefone)


# Cadastrar três pessoas.
lista_pessoas = []

for i in range(3):
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = int(input("Telefone:"))
    pessoa = Pessoa(nome, email, telefone)  # cria um objeto
    lista_pessoas.append(pessoa)            # insere objeto na lista

# imprime os dados de cada pessoa cadastrada
for pessoa in lista_pessoas:
    pessoa.exibir_dados()
