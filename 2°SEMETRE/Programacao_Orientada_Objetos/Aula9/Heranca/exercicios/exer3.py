class Imovel():
    def __init__(self, enderceco, preco):
        self.endereco = enderceco
        self.preco = preco
        
    def exibir_dados(self):
        print(f'ENDEREÇO : {self.endereco}')
        print(f'PREÇO : {self.preco}')

class ImovelNovo(Imovel):
    def __init__(self, enderceco, preco, add):
        super().__init__(enderceco, preco)
        self.add = add
        
    def calcular_preco(self):
        return self.preco + self.add
        
    def exibir_dados(self):
        super().exibir_dados()
        print(f'VALOR COM ADD : {self.calcular_preco()}')
        

class ImovelVelho(Imovel):
    def __init__(self, enderceco, preco, desconto):
        super().__init__(enderceco, preco)
        self.desconto = desconto
        
    def calcular_desconto(self):
        return self.preco - self.desconto
    
    
    def exibir_dados(self):
        super().exibir_dados()
        print(f'VALOR COM DESCONTO : {self.calcular_desconto()}')
        



print('*' * 30)
print(f'IMOVEL NOVO')
imovel = ImovelNovo('Rua Juan Vievnte', 100, 120)
imovel.exibir_dados()

print('*' * 30)
print(f'IMOVEL VELHO')
imovel = ImovelVelho('Rua Juan Vievnte', 100, 120)
imovel.exibir_dados()
   