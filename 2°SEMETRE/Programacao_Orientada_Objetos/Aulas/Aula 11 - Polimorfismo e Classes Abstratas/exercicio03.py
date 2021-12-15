from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass


class Gerente(Funcionario):
    def calcular_salario(self):
        return self.salario_base * 2


class Assistente(Funcionario):
    def calcular_salario(self):
        return self.salario_base


class Vendedor(Funcionario):
    def calcular_salario(self):
        return self.salario_base * 1.10


g = Gerente("João", 123, 2000)
a = Assistente("Ana", 333, 2000)
v = Vendedor("Maria", 456, 2000)

lista = [g, a, v]
for f in lista:
    print(f.calcular_salario())             # duck typing
