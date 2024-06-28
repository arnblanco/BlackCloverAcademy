from pydantic import BaseModel, validator, constr, conint
from typing import Literal

class Student(BaseModel):
    nombre: str
    apellido: str
    identificacion: constr(strip_whitespace=True, regex=r'^[A-Za-z0-9]{1,10}$')
    edad: conint(gt=0, lt=100)
    afinidad_magica: Literal["Oscuridad", "Luz", "Fuego", "Agua", "Viento", "Tierra"]

    @validator('nombre', 'apellido')
    def capitalize_words(cls, value):
        # Capitalizar la primera letra de cada palabra y validar solo letras
        if not value.isalpha():
            raise ValueError("Debe contener solo letras.")
        return " ".join(word.capitalize() for word in value.split())

    @validator('afinidad_magica')
    def validate_afinidad(cls, value):
        # Validar que la afinidad mágica esté dentro de las opciones permitidas
        if value not in ["Oscuridad", "Luz", "Fuego", "Agua", "Viento", "Tierra"]:
            raise ValueError("Debe ser una de: Oscuridad, Luz, Fuego, Agua, Viento, Tierra.")
        return value

    class Config:
        schema_extra = {
            "example": {
                "nombre": "Juan",
                "apellido": "Pérez",
                "identificacion": "ABC12345",
                "edad": 18,
                "afinidad_magica": "Fuego"
            }
        }