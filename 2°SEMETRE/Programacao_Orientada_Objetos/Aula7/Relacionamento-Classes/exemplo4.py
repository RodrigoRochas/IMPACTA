class Endereco:
    def __init__(self, rua, numero, CEP):
        self.rua = rua
        self.numero = numero
        self.complemento = ""
        self.CEP = CEP

    def exibirDados(self):
        print('Rua : ', self.rua)
        print('Numero : ', self.numero)
        print('Complemento : ', self.complemento)
        print('CEP: ', self.CEP)

class Pessoa:
    def __init__(self, nome, idade, sexo, endereco):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

    def exibirDados(self):
        print('Nome : ', self.nome)
        print('Idade : ', self.idade)
        print('Sexo : ', self.sexo)
        print('Endereço : ', self.endereco.exibirDados())

end1 = Endereco('Rua Juan Vicente', 482 , 6160180)
end2 = Endereco('Rua Nasciso Sturlini', 250, 222222)

pessoa1 = Pessoa("Rodrigo", 20, "Masculino", end1)
pessoa2 = Pessoa("Noelma", 50, "Feminino",  end2)


# EXIBINDO AS PESSOAS
print('#' * 40)
pessoa1.exibirDados()
print('#' * 40)
pessoa2.exibirDados()


