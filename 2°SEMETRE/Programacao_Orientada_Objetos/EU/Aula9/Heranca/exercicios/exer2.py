class Animal:
    def __init__(self, nome, cor, numero_patas):
        self.nome = nome
        self.cor = cor
        self.numero_patas = numero_patas
        
    def exibir_dados(self):
        print(f'NOME : {self.nome}')
        print(f'COR : {self.cor}')
        print(f'NUMERO DE PATAS : {self.numero_patas}')
        

class Cachorro(Animal):
    def __init__(self, nome, cor, numero_patas, raca):
        super().__init__(nome, cor, numero_patas)
        self.raca = raca
        
    def exibir_dados(self):
        super().exibir_dados()
        print(f'RAÇA : {self.raca}')
        

print('*' * 30)
print(f'ANIMAL GERAL')
animal = Animal('Cachorritis', 'Bege', 4)
animal.exibir_dados()


print('*' * 30)
print(f'ANIMAL CACHORRO')
dog = Cachorro('Betty', 'preta', 4, 'vira-lata')
dog.exibir_dados()