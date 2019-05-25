# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy import exc ,Table, Column, String, Date, Integer, ForeignKey
from ejercicio_01 import borrar_tabla, crear_tabla, conexion, reset_tabla, Persona, sessionUsuario
base = exc.declarative.declarative_base

class PersonaPeso(base):
    __tablename__='PersonaPeso'
    idPersona = Column(Integer, ForeignKey("Persona.idPersona"), nullable=False)
    Fecha = Column(Date)
    Peso = Column(Integer)

def crear_tabla_peso():
    conn = conexion()
    base.metadata.create_all(conn)
    print('creacion de tabla con exito')

def borrar_tabla_peso():
    conn = conexion()
    Persona.__table__.drop(conn)
    print('eliminacion de tabla con exito')

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
