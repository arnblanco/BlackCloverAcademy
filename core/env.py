import os
from pathlib import Path
from pydantic import BaseSettings


class Config(BaseSettings):
    """
    Configuración de la aplicación utilizando Pydantic.

    Esta clase define las variables de entorno necesarias para la configuración
    de la aplicación, incluyendo la conexión a la base de datos PostgreSQL.

    Atributos:
    - ENV (str): Entorno de la aplicación (por defecto, 'development').
    - POSTGRES_HOST (str): Host de la base de datos PostgreSQL.
    - POSTGRES_PORT (str): Puerto de la base de datos PostgreSQL.
    - POSTGRES_DB (str): Nombre de la base de datos PostgreSQL.
    - POSTGRES_USER (str): Usuario de la base de datos PostgreSQL.
    - POSTGRES_PASSWORD (str): Contraseña del usuario de la base de datos PostgreSQL.
    - BASE_DIR (Path): Directorio base del proyecto.

    Métodos:
    - WRITER_DB_URL(): Genera la URL de conexión para escritura a la base de datos PostgreSQL.
    - READER_DB_URL(): Genera la URL de conexión para lectura desde la base de datos PostgreSQL.
    """
    ENV: str = "development"
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    BASE_DIR = Path(__file__).resolve().parent.parent

    @property
    def WRITER_DB_URL(self):
        """
        Genera la URL de conexión para escritura a la base de datos PostgreSQL.

        Returns:
        - str: URL de conexión para escritura a la base de datos PostgreSQL.
        """
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @property
    def READER_DB_URL(self):
        """
        Genera la URL de conexión para lectura desde la base de datos PostgreSQL.

        Returns:
        - str: URL de conexión para lectura desde la base de datos PostgreSQL.
        """
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    class Config:
        """
        Configuración adicional para la clase Config.

        Esta clase define opciones de configuración adicionales para la clase Config,
        como la carga de variables de entorno desde un archivo .env específico para
        el entorno de desarrollo (.env.dev).
        """
        env_file = ".env"


# Instancia de Config para acceder a las variables de entorno y URLs de conexión
env = Config()
