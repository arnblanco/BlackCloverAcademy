from sqlalchemy import Column, Integer, String, Boolean
from core.db import Base

class Student(Base):
    """
    Modelo SQLAlchemy para la tabla 'student'.

    Este modelo representa la estructura de la tabla 'student' en la base de datos.

    Atributos:
    - id (int): Identificador único del estudiante (clave primaria).
    - nombre (str): Nombre del estudiante.
    - apellido (str): Apellido del estudiante.
    - identificacion (str): Número de identificación del estudiante (único).
    - edad (int): Edad del estudiante.
    - afinidad_magica (str): Afinidad mágica del estudiante.
    - grimorio (str): Tipo de grimorio del estudiante.
    - estado (bool): Estado del estudiante (activo/inactivo).

    Tabla:
    - Nombre: 'student'

    """
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(20), nullable=False)
    apellido = Column(String(20), nullable=False)
    identificacion = Column(String(10), nullable=False, unique=True)
    edad = Column(Integer, nullable=False)
    afinidad_magica = Column(String(20), nullable=False)
    grimorio = Column(String(25), nullable=False)
    estado = Column(Boolean, nullable=False, default=False)
