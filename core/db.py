from contextvars import ContextVar, Token
from typing import Union

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_scoped_session,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql.expression import Update, Delete, Insert

from core.env import env

# ContextVar para almacenar el ID de sesión en el contexto
session_context: ContextVar[str] = ContextVar("session_context")


def get_session_context() -> str:
    """
    Obtiene el ID de sesión actual del contexto.
    
    Returns:
    - str: ID de sesión actual.
    """
    return session_context.get()


def set_session_context(session_id: str) -> Token:
    """
    Establece el ID de sesión en el contexto.

    Parámetros:
    - session_id (str): ID de sesión a establecer en el contexto.

    Returns:
    - Token: Token que puede ser utilizado para resetear el contexto de sesión.
    """
    return session_context.set(session_id)


def reset_session_context(context: Token) -> None:
    """
    Restablece el contexto de sesión al estado previo.

    Parámetros:
    - context (Token): Token obtenido de set_session_context.
    """
    session_context.reset(context)


# Configuración de motores de base de datos
engines = {
    "writer": create_async_engine(env.WRITER_DB_URL, pool_recycle=3600),
    "reader": create_async_engine(env.READER_DB_URL, pool_recycle=3600),
}

# Clase personalizada para manejar la selección de motor de base de datos según la operación
class RoutingSession(Session):
    def get_bind(self, mapper=None, clause=None, **kw):
        """
        Devuelve el motor de base de datos apropiado según el tipo de operación.

        Este método decide si se debe utilizar el motor 'writer' o 'reader' para la operación actual.

        Parámetros:
        - mapper: Objeto mapeador SQLAlchemy.
        - clause: Clausula SQLAlchemy.
        - kw: Argumentos adicionales.

        Returns:
        - engine: Motor de base de datos seleccionado para la operación.
        """
        if self._flushing or isinstance(clause, (Update, Delete, Insert)):
            return engines["writer"].sync_engine
        else:
            return engines["reader"].sync_engine

# Factoría de sesiones asíncronas
async_session_factory = sessionmaker(
    class_=AsyncSession,
    sync_session_class=RoutingSession,
)

# Sesión global de SQLAlchemy con soporte asíncrono
session: Union[AsyncSession, async_scoped_session] = async_scoped_session(
    session_factory=async_session_factory,
    scopefunc=get_session_context,
)

# Base declarativa para declarar modelos SQLAlchemy
Base = declarative_base()
