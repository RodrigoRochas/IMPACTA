# IMPORTAR MÓDULOS
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# CONFIGURAR CONEXÃO COM BANCO DE DADOS SQLITE
# caso o arquivo de banco não exista, ele será criado
engine = create_engine("sqlite:///server.db")
connection = engine.connect()

# INICIAR SESSÃO COM BANCO DE DADOS
session = Session()

# INSTANCIAR CLASSE BASE DO SQLALCHEMY
Base = declarative_base(engine)


class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


# Cria o arquivo de texto
arquivo = open('saida.txt', 'w', encoding='UTF-8')

# realiza consulta no banco (ordena pelo nome)
resultado = session.query(Funcionario).order_by(Funcionario.nome)

# percorre lista de funcionario e escreve no arquivo de texto
for f in resultado:
    arquivo.write(f.nome + ';' + str(f.idade) + ';' + str(f.salario) + '\n')

arquivo.close()
connection.close()
