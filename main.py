from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Cliente, Base
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "postgresql://postgres:ilomilo@localhost:5432/Hotel"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()



def muestra_empleados():
    print(str(session.query(Cliente)))
    employees = session.query(Cliente).all()
    for employee in employees:
        print(employee.nombre, employee.correo, employee.telefono, employee.fecha_registro)
     

if __name__ == "__main__":
    muestra_empleados()
    #get_empleado(19)
    #actualiza_empleado(19)
    #get_empleado(19)
    #muestra_genero()
    #get_detalles_empleado(5)
    session.close()