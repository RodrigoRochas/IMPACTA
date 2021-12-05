class CarroCorrida:
    def __init__(self, numero, piloto, veloMax):
        self.__numero = numero
        self.__piloto = piloto
        self.__veloMax = veloMax
        self.__veloAtual = 0
        self.__ligado = False

    def ligar(self):
        self.__ligado = True

    def desligar(self):
        self.__ligado = False

    def acelerar(self, velocidade):
        if self.__ligado is True:
            self.__veloAtual += velocidade
        
            if self.__veloAtual > self.__veloMax:
                self.__veloAtual = self.__veloMax

    def frear(self):
        self.__veloAtual = 0

    def get_velo_atual(self):
        return self.__veloAtual


