class Socio:
    def init(self, nome, cpf, data_nascimento, mes_associado, ano_associado):
        self.nome = nome
        self.cpf = cpf 
        self.data_nascimento = data_nascimento
        self.mes_associado = mes_associado
        self.ano_associado = ano_associado
    

class Clube:
    def init(self):
        self.socio = []

    def associar (self, socio):
        self.socio = socio

    def numero_de_socios(self):
        num_socio = 0
        for socio in self.socio:
            num_socio += 1
        return num_socio

    def mes_associacao(self, mes, ano):
        self.socio = []
        # if mes_associado == mes_associado and ano_associado == ano_associado:
        #     return (teste)
        if mes == '' and ano == '':
            return 0
        if mes < 1 or mes > 12:
            raise AssertionError
        if ano <= 999 or ano > 9999:
            raise Exception
             
    
    def expulsar(self, mes, ano):
        socio_expulsar = []
        if socio_expulsar == []:
            return socio_expulsar
        if mes < 1 or mes > 12:
            raise AssertionError
        if ano <= 999 or ano > 9999:
            raise Exception