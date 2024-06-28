from sqlalchemy import Column, Integer, String, Enum
from core.db import Base

class MagicAffinity(Enum):
    oscuridad = 'Oscuridad'
    luz = 'Luz'
    fuego = 'Fuego'
    agua = 'Agua'
    viento = 'Viento'
    tierra = 'Tierra'


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(20), nullable=False)
    apellido = Column(String(20), nullable=False)
    identificacion = Column(String(10), nullable=False, unique=True)
    edad = Column(Integer, nullable=False)
    afinidad_magica = Column(Enum(MagicAffinity), nullable=False)
    