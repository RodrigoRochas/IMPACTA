import pyodbc
from urllib.parse import quote_plus
from sqlalchemy import Column, Integer, String, create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

parametros = (
    'Driver=SQL Server;'
    'Server=DESKTOP-UOTL7NU;'
    'Database=HELLO;'
    'Trusted_Connection = yes;'
)

url_db = quote_plus(parametros)

engine = create_engine('mssql+pyodbc:///?odbc_connect=%s' % url_db)
conex = engine.connect()

Session = sessionmaker(bind=engine)

Base = declarative_base()


conex.execute ('''
                CREATE TABLE PACIENTE (
                   NOME VARCHAR (50),
                   CPF VARCHAR (50),
                   IDADE INT
                ) ''')

class Paciente(Base):
    __tablename__ = 'PACIENTE'
    nome = Column('NOME', String(50))
    cpf = Column('CPF', String(50))
    idade = Column('IDADE', Integer)
    
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        
Base.metadata.create_all(engine)

session = Session()
        
paciente1 = Paciente('Rodrigo Rocha', '506.895.528-07', 20)
session.add(paciente1)
session.commit()


session.close()