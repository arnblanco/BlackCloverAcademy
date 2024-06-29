from pydantic import BaseModel, validator, constr, conint
from typing import Literal, Optional

class CreateStudentRequest(BaseModel):
    """
    Modelo Pydantic para la creación de un estudiante.

    Este modelo define los campos requeridos para crear un estudiante en la base de datos.

    Atributos:
    - nombre (str): Nombre del estudiante (entre 3 y 20 caracteres, solo letras).
    - apellido (str): Apellido del estudiante (entre 3 y 20 caracteres, solo letras).
    - identificacion (str): Número de identificación del estudiante (hasta 10 caracteres alfanuméricos).
    - edad (int): Edad del estudiante (mayor que 0 y menor que 100).
    - afinidad_magica (Literal): Afinidad mágica del estudiante, debe ser una de las opciones especificadas.

    Métodos de Validación:
    - capitalize_words: Capitaliza la primera letra de cada palabra en nombre y apellido.
    - validate_afinidad: Valida que la afinidad mágica esté dentro de las opciones permitidas.

    Configuración:
    - schema_extra: Proporciona un ejemplo de datos que puede ser útil para la documentación de la API.
    """
    nombre: constr(min_length=3, max_length=20)
    apellido: constr(min_length=3, max_length=20)
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
            raise ValueError("Las afinidades mágicas tienen que ser: Oscuridad, Luz, Fuego, Agua, Viento, Tierra.")
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


class UpdateStudentRequest(BaseModel):
    """
    Modelo Pydantic para la actualización de un estudiante.

    Este modelo define campos opcionales que pueden ser actualizados para un estudiante existente.

    Atributos:
    - nombre (str, opcional): Nuevo nombre del estudiante (entre 3 y 20 caracteres, solo letras).
    - apellido (str, opcional): Nuevo apellido del estudiante (entre 3 y 20 caracteres, solo letras).
    - identificacion (str, opcional): Nuevo número de identificación del estudiante (hasta 10 caracteres alfanuméricos).
    - edad (int, opcional): Nueva edad del estudiante (mayor que 0 y menor que 100).
    - afinidad_magica (Literal, opcional): Nueva afinidad mágica del estudiante, debe ser una de las opciones especificadas.

    Métodos de Validación:
    - capitalize_words: Capitaliza la primera letra de cada palabra en nombre y apellido si se proporcionan.

    Configuración:
    - schema_extra: Proporciona un ejemplo de datos que puede ser útil para la documentación de la API.
    """
    nombre: Optional[constr(min_length=3, max_length=20)] = None
    apellido: Optional[constr(min_length=3, max_length=20)] = None
    identificacion: Optional[constr(strip_whitespace=True, regex=r'^[A-Za-z0-9]{1,10}$')] = None
    edad: Optional[conint(gt=0, lt=100)] = None
    afinidad_magica: Optional[Literal["Oscuridad", "Luz", "Fuego", "Agua", "Viento", "Tierra"]] = None

    @validator('nombre', 'apellido')
    def capitalize_words(cls, value):
        # Capitalizar la primera letra de cada palabra y validar solo letras si se proporciona un valor
        if value and not value.isalpha():
            raise ValueError("Debe contener solo letras.")
        return " ".join(word.capitalize() for word in value.split()) if value else value

    @validator('afinidad_magica')
    def validate_afinidad(cls, value):
        # Validar que la afinidad mágica esté dentro de las opciones permitidas si se proporciona un valor
        if value and value not in ["Oscuridad", "Luz", "Fuego", "Agua", "Viento", "Tierra"]:
            raise ValueError("Las afinidades mágicas tienen que ser: Oscuridad, Luz, Fuego, Agua, Viento, Tierra.")
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


class StudentResponse(BaseModel):
    """
    Modelo Pydantic para la respuesta de datos de un estudiante.

    Este modelo define la estructura de los datos que se devolverán como respuesta
    al consultar información de un estudiante.

    Atributos:
    - id (int): Identificador único del estudiante.
    - nombre (str): Nombre del estudiante.
    - apellido (str): Apellido del estudiante.
    - identificacion (str): Número de identificación del estudiante.
    - edad (int): Edad del estudiante.
    - afinidad_magica (str): Afinidad mágica del estudiante.
    - grimorio (str): Tipo de grimorio del estudiante.
    - estado (bool): Estado del estudiante (activo/inactivo).

    Configuración:
    - orm_mode: Habilita el modo de ORM para serializar/deserializar objetos SQLAlchemy.
    """
    id: int
    nombre: str
    apellido: str
    identificacion: str
    edad: int
    afinidad_magica: str
    grimorio: str
    estado: bool

    class Config:
        orm_mode = True
