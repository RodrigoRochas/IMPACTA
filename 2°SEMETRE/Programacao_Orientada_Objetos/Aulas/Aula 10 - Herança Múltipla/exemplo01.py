class AnimalTerrestre:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def andar(self):
        print('O animal Terrestre andou')

    def comer(self):
        print('O animal Terrestre comeu')


class AnimalAquatico:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def nadar(self):
        print('O animal Aquatico nadou')

    def comer(self):
        print('O animal Aquatico comeu')


class AnimalAnfibio(AnimalAquatico, AnimalTerrestre):
    def __init__(self, nome, altura, especie):
        AnimalTerrestre.__init__(self, nome, altura)
        AnimalAquatico.__init__(self, nome, especie)

    def comer(self):
        AnimalTerrestre.comer(self)
        AnimalAquatico.comer(self)


anfibio = AnimalAnfibio('nome do animal', 25, 'especie do animal')
print(anfibio.nome)
print(anfibio.altura)
print(anfibio.especie)


anfibio.andar()
anfibio.nadar()
anfibio.comer()
