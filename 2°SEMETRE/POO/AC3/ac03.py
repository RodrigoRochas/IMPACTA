class SuperPoder():
    def __init__(self, nome, categoria):
        self.__nome =  nome
        self.__categoria = categoria
        
    # GET NOME
    def get_nome(self):
        return self.__nome
    
    # GET CATEGORIA
    def get_categoria(self):
        return self.__categoria
    

class Personagem():
    def __init__(self, nome, nome_vida_real):
        self.__nome = nome
        self.__nome_vida_real = nome_vida_real
        self.__poderes = list()
       
        
    def adicionar_super_poder(self, superpoder):
        if len(self.__poderes) < 4:
            self.__poderes.append(superpoder)
        else:
            raise ValueError
        
    def get_poder_total(self):
        soma = 0
        for c in self.__poderes:
            soma += c.get_categoria()
            
        return soma
    

class SuperHeroi(Personagem):
    def __init__(self, nome, nome_vida_real):
        super().__init__(nome, nome_vida_real)

    def get_poder_total(self):
        pass
    
    
class Vilao(Personagem):
    def __init__(self, nome, nome_vida_real, tempo_de_prisao):
        super().__init__(nome, nome_vida_real)
        
        self.tempo_de_prisao = tempo_de_prisao
        
        
class Confronto():
    
    # def __init__(self, nome, nome_vida_real, soma, tempo_de_prisao):
    #     SuperHeroi.__init__(nome, nome_vida_real, soma)
    #     Vilao.__init__(nome, nome_vida_real, tempo_de_prisao)
    
    def lutar(self, superheroi, vilao):
        if superheroi.get_poder_total() > vilao.get_poder_total():
            return 1
        
        elif superheroi.get_poder_total() < vilao.get_poder_total():
            return 2
        
        elif superheroi.get_poder_total() == vilao.get_poder_total():
            return 0
        
    