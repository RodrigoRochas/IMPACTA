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

connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        IDADE INTEGER,
                        SALARIO FLOAT)""")


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


# abre o arquivo de texto
arquivo = open('funcionarios.txt', 'r', encoding='UTF-8')

lista_funcionario = []

# percorre as linhas dox arquivo de texto
for linha in arquivo:
    lista = linha.split(';')
    # cria um objeto
    func = Funcionario(lista[0], int(lista[1]), float(lista[2]))
    # insere objeto na lista de funcionarios
    lista_funcionario.append(func)

# insere lista de funcionario no Banco de Dados
session.add_all(lista_funcionario)
session.commit()

# realiza consulta
resultado = session.query(Funcionario)
for obj in resultado:
    print(obj.id, obj.nome, obj.idade, obj.salario)

arquivo.close()
connection.close()
