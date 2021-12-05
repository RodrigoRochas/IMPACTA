class Cachorro:
    #atributos
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade



    #metodos
    def andar(self, distancia):
        print('O cachorro andou ' + str(distancia) + ' metros')

    def comer(self):
        print('O cachorro de nome ' + self.nome + ' comeu ')

    def latir(self):
        print('O cachorro latiu')


dog = Cachorro('rodrigo', 10)
meuDog = Cachorro('Snooopy', 15)

print(dog.nome)


