class Pneu:
    def __init__(self, pressao):
        self.pressao = pressao

    
    def furar(self):
        self.pressao = 0


class Carro():
    def __init__(self, pneu1, pneu2, pneu3, pneu4):
        self.pneu1 = pneu1
        self.pneu2 = pneu2
        self.pneu3 = pneu3
        self.pneu4 = pneu4
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.desligado = False

    def verificar_pneu(self):
        if self.ligado == True:
            print(f'Pressão do pneu 1 : ', self.pneu1.pressao)
            print(f'Pressão do pneu 2 : ', self.pneu2.pressao)
            print(f'Pressão do pneu 3 : ', self.pneu3.pressao)
            print(f'Pressão do pneu 4 : ', self.pneu4.pressao)

        else:
            print(f'Carro desligado')

pneu1 = Pneu(32)
pneu2 = Pneu(32)
pneu3 = Pneu(36)
pneu4 = Pneu(36)

meucarro = Carro(pneu1, pneu2, pneu3, pneu4)
meucarro.ligar()
meucarro.pneu3.furar()
meucarro.verificar_pneu()
meucarro.desligar()
meucarro.verificar_pneu()