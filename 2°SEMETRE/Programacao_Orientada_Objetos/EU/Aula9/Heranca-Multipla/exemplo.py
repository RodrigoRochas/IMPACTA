class AnimalTerrestre:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura
        
    def andar(self):
        print('Animal terrestre andando')
        
    def comer(self):
        print(f'O animal terresre comeu')
        
    
class AnimalAquatico():
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        
    def nadar(self):
        print(f'O animal aquatico nadou')
        
    def comer(self):
        print(f'O animal aquatico comeu')
        
        
class AnimalAnfibio(AnimalTerrestre, AnimalAquatico):
    def __init__(self, nome, altura, especie):
        AnimalTerrestre.__init__(self, nome, altura)
        AnimalAquatico.__init__(self, nome, especie)
        
    def comer(self):
        AnimalTerrestre.comer(self)
        AnimalAquatico.comer(self)
        
        
        
anfibio = AnimalAnfibio('Cacatua', 25, 'Ave')

print(anfibio.nome)
print(anfibio.altura)
print(anfibio.especie)

anfibio.andar()
anfibio.nadar()
anfibio.comer()