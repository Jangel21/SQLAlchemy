from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Numeric, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase 
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from models import *

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/testBackup"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

def muestra_clientes():
    clientes = session.query(Cliente).all()
    for cliente in clientes:
        print(cliente.nombre, cliente.correo,cliente.telefono)

def muestra_cliente_por_id(cliente_id):
    cliente = session.get(Cliente, cliente_id)
    if cliente:
        print(cliente.nombre, cliente.correo, cliente.telefono)
    else:
        print(f"No se encontró el cliente con ID {cliente_id}")

def agrega_cliente(nombre, correo, telefono):
    nuevo_cliente = Cliente(nombre=nombre, correo=correo, telefono=telefono)
    session.add(nuevo_cliente)
    session.commit()
    print(f"Cliente {nombre} agregado exitosamente.")


if __name__ == "__main__":
    muestra_clientes()
    print("----")
    muestra_cliente_por_id(3)
    print("----")
    agrega_cliente("Nuevo Cliente", "nuevo.cliente@email.com", "555-1234")
    print("----")
    muestra_clientes()
    session.close()
