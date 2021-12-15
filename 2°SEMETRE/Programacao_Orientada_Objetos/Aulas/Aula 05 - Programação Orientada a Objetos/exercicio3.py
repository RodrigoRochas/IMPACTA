'''
Classe Televisão

Atributos:
- canal (o canal inicial da tv deve ser None)
- volume (o volume inicial da tv deve ser zero)

Métodos:
- aumentar_volume: aumenta o nível de volume em uma unidade.
- diminuir_volume: diminui o nível de volume em uma unidade.
- alterar_canal: recebe o número do canal e altera o canal da tv.
'''


class Televisao:
    def __init__(self):
        self.canal = None
        self.volume = 0

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1

    def alterar_canal(self, canal):
        self.canal = canal


tv = Televisao()
tv.alterar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print(f'A tv está no canal {tv.canal}')             # A tv está no canal 5
print(f'A tv está no volume {tv.volume}')           # A tv está no volume 2
