class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

class Cachorro:
    def __init__(self, nome, idade, proprietario):
        self.nome = nome
        self.idade = idade
        self.proprietario = proprietario

pessoa1 = Pessoa('Rodrigo', 'Rocha')#Objeto pessoa
cachorro1 = Cachorro('Beth', 12, pessoa1)#Objeto cachorro

print(cachorro1.nome)
print(cachorro1.idade)
print(cachorro1.proprietario.nome)
