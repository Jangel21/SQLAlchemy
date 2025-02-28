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
        print(cliente.nombre, cliente.correo, cliente.telefono)

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

def actualiza_cliente(cliente_id, nombre=None, correo=None, telefono=None):
    cliente = session.get(Cliente, cliente_id)
    if cliente:
        if nombre:
            cliente.nombre = nombre
        if correo:
            cliente.correo = correo
        if telefono:
            cliente.telefono = telefono
        session.commit()
        print(f"Cliente con ID {cliente_id} actualizado exitosamente.")
    else:
        print(f"No se encontró el cliente con ID {cliente_id}")

def elimina_cliente(cliente_id):
    cliente = session.get(Cliente, cliente_id)
    if cliente:
        session.delete(cliente)
        session.commit()
        print(f"Cliente con ID {cliente_id} eliminado exitosamente.")
    else:
        print(f"No se encontró el cliente con ID {cliente_id}")

def muestra_empleados():
    empleados = session.query(Empleado).all()
    for empleado in empleados:
        print(empleado.nombre, empleado.rol, empleado.disponibilidad)
        
def muestra_empleado_por_id(empleado_id):
    empleado = session.get(Empleado, empleado_id)
    if empleado:
        print(empleado.nombre, empleado.rol, empleado.disponibilidad)
    else:
        print(f"No se encontró el empleado con ID {empleado_id}")

def agrega_empleado(nombre, rol, disponibilidad=True):
    nuevo_empleado = Empleado(nombre=nombre, rol=rol, disponibilidad=disponibilidad)
    session.add(nuevo_empleado)
    session.commit()
    print(f"Empleado {nombre} agregado exitosamente.")

def actualiza_empleado(empleado_id, nombre=None, rol=None, disponibilidad=None):
    empleado = session.get(Empleado, empleado_id)
    if empleado:
        if nombre:
            empleado.nombre = nombre
        if rol:
            empleado.rol = rol
        if disponibilidad is not None:
            empleado.disponibilidad = disponibilidad
        session.commit()
        print(f"Empleado con ID {empleado_id} actualizado exitosamente.")
    else:
        print(f"No se encontró el empleado con ID {empleado_id}")

def elimina_empleado(empleado_id):
    empleado = session.get(Empleado, empleado_id)
    if empleado:
        session.delete(empleado)
        session.commit()
        print(f"Empleado con ID {empleado_id} eliminado exitosamente.")
    else:
        print(f"No se encontró el empleado con ID {empleado_id}")

def muestra_reservaciones():
    reservaciones = session.query(Reservacione).all()
    for reservacion in reservaciones:
        print(reservacion.id_reservacion, reservacion.fecha_evento, reservacion.estado)

def muestra_reservacion_por_id(reservacion_id):
    reservacion = session.get(Reservacione, reservacion_id)
    if reservacion:
        print(reservacion.id_reservacion, reservacion.fecha_evento, reservacion.estado)
    else:
        print(f"No se encontró la reservación con ID {reservacion_id}")

def agrega_reservacion(id_cliente, id_evento, id_salon, fecha_evento, estado):
    nueva_reservacion = Reservacione(id_cliente=id_cliente, id_evento=id_evento, id_salon=id_salon, fecha_evento=fecha_evento, estado=estado)
    session.add(nueva_reservacion)
    session.commit()
    print(f"Reservación para el evento {id_evento} agregada exitosamente.")

def actualiza_reservacion(reservacion_id, id_cliente=None, id_evento=None, id_salon=None, fecha_evento=None, estado=None):
    reservacion = session.get(Reservacione, reservacion_id)
    if reservacion:
        if id_cliente:
            reservacion.id_cliente = id_cliente
        if id_evento:
            reservacion.id_evento = id_evento
        if id_salon:
            reservacion.id_salon = id_salon
        if fecha_evento:
            reservacion.fecha_evento = fecha_evento
        if estado:
            reservacion.estado = estado
        session.commit()
        print(f"Reservación con ID {reservacion_id} actualizada exitosamente.")
    else:
        print(f"No se encontró la reservación con ID {reservacion_id}")

def elimina_reservacion(reservacion_id):
    reservacion = session.get(Reservacione, reservacion_id)
    if reservacion:
        session.delete(reservacion)
        session.commit()
        print(f"Reservación con ID {reservacion_id} eliminada exitosamente.")
    else:
        print(f"No se encontró la reservación con ID {reservacion_id}")
        
def muestra_eventos():
    eventos = session.query(Evento).all()
    for evento in eventos:
        print(evento.id_evento, evento.nombre, evento.descripcion)

def muestra_evento_por_id(evento_id):
    evento = session.get(Evento, evento_id)
    if evento:
        print(evento.id_evento, evento.nombre, evento.descripcion)
    else:
        print(f"No se encontró el evento con ID {evento_id}")

def agrega_evento(nombre, descripcion):
    nuevo_evento = Evento(nombre=nombre, descripcion=descripcion)
    session.add(nuevo_evento)
    session.commit()
    print(f"Evento {nombre} agregado exitosamente.")

def actualiza_evento(evento_id, nombre=None, descripcion=None):
    evento = session.get(Evento, evento_id)
    if evento:
        if nombre:
            evento.nombre = nombre
        if descripcion:
            evento.descripcion = descripcion
        session.commit()
        print(f"Evento con ID {evento_id} actualizado exitosamente.")
    else:
        print(f"No se encontró el evento con ID {evento_id}")

def elimina_evento(evento_id):
    evento = session.get(Evento, evento_id)
    if evento:
        session.delete(evento)
        session.commit()
        print(f"Evento con ID {evento_id} eliminado exitosamente.")
    else:
        print(f"No se encontró el evento con ID {evento_id}")
        
def muestra_facturas():
    facturas = session.query(Facturacion).all()
    for factura in facturas:
        print(factura.id_factura, factura.id_reservacion, factura.monto_total, factura.moneda, factura.fecha_pago)

def muestra_factura_por_id(factura_id):
    factura = session.get(Facturacion, factura_id)
    if factura:
        print(factura.id_factura, factura.id_reservacion, factura.monto_total, factura.moneda, factura.fecha_pago)
    else:
        print(f"No se encontró la factura con ID {factura_id}")

def agrega_factura(id_reservacion, monto_total, moneda):
    nueva_factura = Facturacion(id_reservacion=id_reservacion, monto_total=monto_total, moneda=moneda)
    session.add(nueva_factura)
    session.commit()
    print(f"Factura para la reservación {id_reservacion} agregada exitosamente.")

def actualiza_factura(factura_id, id_reservacion=None, monto_total=None, moneda=None):
    factura = session.get(Facturacion, factura_id)
    if factura:
        if id_reservacion:
            factura.id_reservacion = id_reservacion
        if monto_total:
            factura.monto_total = monto_total
        if moneda:
            factura.moneda = moneda
        session.commit()
        print(f"Factura con ID {factura_id} actualizada exitosamente.")
    else:
        print(f"No se encontró la factura con ID {factura_id}")

def elimina_factura(factura_id):
    factura = session.get(Facturacion, factura_id)
    if factura:
        session.delete(factura)
        session.commit()
        print(f"Factura con ID {factura_id} eliminada exitosamente.")
    else:
        print(f"No se encontró la factura con ID {factura_id}")
        
def muestra_salones():
    salones = session.query(Salone).all()
    for salon in salones:
        print(salon.id_salon, salon.nombre, salon.capacidad)

def muestra_salon_por_id(salon_id):
    salon = session.get(Salone, salon_id)
    if salon:
        print(salon.id_salon, salon.nombre, salon.capacidad)
    else:
        print(f"No se encontró el salón con ID {salon_id}")

def agrega_salon(nombre, capacidad):
    nuevo_salon = Salone(nombre=nombre, capacidad=capacidad)
    session.add(nuevo_salon)
    session.commit()
    print(f"Salón {nombre} agregado exitosamente.")

def actualiza_salon(salon_id, nombre=None, capacidad=None):
    salon = session.get(Salone, salon_id)
    if salon:
        if nombre:
            salon.nombre = nombre
        if capacidad:
            salon.capacidad = capacidad
        session.commit()
        print(f"Salón con ID {salon_id} actualizado exitosamente.")
    else:
        print(f"No se encontró el salón con ID {salon_id}")

def elimina_salon(salon_id):
    salon = session.get(Salone, salon_id)
    if salon:
        session.delete(salon)
        session.commit()
        print(f"Salón con ID {salon_id} eliminado exitosamente.")
    else:
        print(f"No se encontró el salón con ID {salon_id}")

if __name__ == "__main__":
   # muestra_clientes()
    #print("----")
    #muestra_cliente_por_id(3)
    #print("----")
    #agrega_cliente("a", "a", "a")
    #print("----")
    #muestra_clientes()
    #print("----")
    #actualiza_cliente(3, nombre="Cliente Actualizado")
    #print("----")
    #muestra_cliente_por_id(3)
    #print("----")
    #elimina_cliente(9)
    #print("----")
    muestra_empleados()
    #muestra_clientes()
    session.close()