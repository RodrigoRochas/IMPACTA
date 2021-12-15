class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

                    # AQUI SÃO OS GETTERS
    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_salario(self):
        return self.__salario

                #AQUI SÃO OS SETTERS

    def set_nome(self, nome):
        self.__nome = nome

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_salario(self, salario):
        self.__salario = salario


rodrigo = Funcionario("Rodrigo Rocha", 12402332808, 2000)

rodrigo.__salario = 3000
print(rodrigo.__salario)

