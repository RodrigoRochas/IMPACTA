class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

    def exibir_dados(self):
        print('-------------------------------')
        print('Endereço: ', self.endereco)
        print('Preço original: ', self.preco)


class ImovelNovo(Imovel):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.adicional = adicional

    def calcular_preco(self):
        return self.preco + self.adicional

    def exibir_dados(self):
        super().exibir_dados()
        print('Adicional: ', self.adicional)
        print('Preço atualizado: ', self.calcular_preco())


class ImovelVelho(Imovel):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.desconto = desconto

    def calcular_preco(self):
        return self.preco - self.desconto

    def exibir_dados(self):
        super().exibir_dados()
        print('Desconto: ', self.desconto)
        print('Preço atualizado: ', self.calcular_preco())


imovel = Imovel("Rua Silva, 123", 300000.0)
imovel_novo = ImovelNovo("Rua Joaquim, 999", 250000.0, 20000.0)
imovel_velho = ImovelVelho("Av. Brasil, 777", 500000.0, 35000.0)

imovel.exibir_dados()
imovel_novo.exibir_dados()
imovel_velho.exibir_dados()
