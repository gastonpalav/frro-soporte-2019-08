# Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
# - id_socio: entero (clave primaria, auto-incremental, unico)
# - dni: entero (unico)
# - nombre: string (longitud 250)
# - apellido: string (longitud 250)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def conexion():
    engine = create_engine('sqlite:///database.db', echo = True)
    return engine

def retornarBase():
    return Base

def sessionUsuario():
    Base.metadata.bind = conexion()
    DBSession = sessionmaker()
    DBSession.bind = conexion()
    session = DBSession()
    return  session

class Socio(Base):
    __tablename__ = 'socios'
    id_socio = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    dni = Column(Integer, unique=True)
    nombre = Column(String(250))
    apellido = Column(String(250))

def crearModelo():
    Base.metadata.create_all(conexion())
    print('Creacion de modelo con exito')

crearModelo()
