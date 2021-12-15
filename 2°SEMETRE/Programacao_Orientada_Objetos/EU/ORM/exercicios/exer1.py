import pyodbc
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import Integer, String, Float, engine
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine("sqlserver:///")
conex = engine.connect()


session = Session(engine)

Base = declarative_base(conex)  
#BASE
cursor = conex.cursor()

conex.execute (
                'Driver=SQL Server;'
                'Server=DESKTOP-UOTL7NU;'
                'Database=HELLO;'
                'Trusted_Connection = yes;'
                )


cursor.execute ('''
                CREATE TABLE PACIENTE (
                   ID INT PRIMARY KEY,
                   NOME VARCHAR (50),
                   CPF VARCHAR (50),
                   IDADE INT
                )
               ''')

cursor.execute ('''
                CREATE TABLE MEDICO (
                    ID INT PRIMARY KEY,
                    NOME VARCHAR (50),
                    CRM VARCHAR (50),
                    ESPECIALIZACAO VARCHAR (50)
                    
                )
                ''')

cursor.execute ('''
                CREATE TABLE EXAME (
                    ID_EXAME INT PRIMARY KEY,
                    ID_MEDICO INT,
                    ID_PACIENTE INT,
                    DESCRICAO VARCHAR (50),
                    RESULTADO VARCHAR (50)
                )
                ''')

conex.commit()

# # #MAPEAMENTO DE CLASSES
# class Paciente(Base):
#     __tablename__ = 'PACIENTE'
#     id = 
    

conex.close()


