from sqlalchemy import create_engine, Column, Integer, String, Float, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import false
from sqlalchemy.orm import Session


engine = create_engine("sqlite:///teste.db")
connection = engine.connect()

session = Session()

Base = declarative_base(engine)

connection.execute(""" CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                            ID INTEGER PRIMARY KEY,
                            NOME VARCHAR(255) NOT NULL,
                            IDADE INT NOT NULL, 
                            SALARIO FLOAT NOT NULL ) """)


class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)
    idade = Column('IDADE', Integer, nullable=False)
    salario = Column('SALARIO', Float, nullable=False)
    
    
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        
        
lista = []    
for c in range(3):
    nome = input('Digite seu nome : ')
    idade = int(input('Duigite sua idade : '))
    salario = float(input('Duigite seu salario : '))
    
    func = Funcionario(nome, idade, salario)
    lista.append(func)
    
session.add_all(lista)
session.commit()

resultado = session.query(Funcionario)
for func in resultado:
    print(func.id, func.nome, func.idade, func.salario)
    

print('****************** SALARIOS MAIORES QUE 1500 ***************')
resultado = session.query(Funcionario).filter(Funcionario.salario > 1500)
for func in resultado:
    print(f'ID_MA : ', {func.id})
    print(f'NOME_MA : ', {func.nome})
    print(f'IADDE_MA : ', {func.idade})
    print(f'SALARIO_MA : ', {func.salario})
    
    
connection.close()
    

