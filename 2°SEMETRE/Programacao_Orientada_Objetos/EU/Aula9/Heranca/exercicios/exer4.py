class Motor:
    def __init__(self, cilindrada, potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia
        
    
class Veiculo:
    def __init__(self, ano, preco, motor):
        self.ano = ano
        self.preco = preco
        self.motor = motor
        
    def exibir_dados(self):
        print(f'Ano : {self.ano}')
        print(f'Preço : {self.preco}')
        print(f'Cilindrada do motor : {self.motor.cilindrada}')
        print(f'Potencia do motor : {self.motor.potencia}')
        

class Carro(Veiculo):
    def __init__(self, ano, preco, motor, cor, modelo):
        super().__init__(ano, preco, motor)
        self.cor = cor
        self.modelo = modelo
        
    def exibir_dados(self):
        super().exibir_dados()
        print(f'Cor : {self.cor}')
        print(f'Modelo : {self.modelo}')
        

class Caminhao(Veiculo):
    def __init__(self, ano, preco, motor, comprimento):
        super().__init__(ano, preco, motor)
        self.comprimento = comprimento
        
    def exibir_dados(self):
        super().exibir_dados()
        print(f'Comprimento : {self.comprimento}')