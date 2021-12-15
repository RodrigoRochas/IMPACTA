'''
Classe Pessoa

Atributos (características do objeto)
- nome
- idade

Métodos (comportamentos e ações realizadas pelo objeto)
- andar
- dormir
'''


class Pessoa:
    # metodo construtor (constroi o objeto)
    def __init__(self, nome, idade):
        self.nome = nome                    # atributos
        self.idade = idade

    def andar(self):
        print('A pessoa andou.')

    def dormir(self):
        print('A pessoa', self.nome, 'dormiu')


pessoa1 = Pessoa('Paulo', 30)       # criar um objeto (instanciar um objeto)
pessoa1.andar()
pessoa1.dormir()
pessoa1.idade = 31
pessoa1.nome = 'Paulo Vieira'

print(pessoa1.nome)

pessoa2 = Pessoa('Ana', 25)
pessoa2.dormir()
