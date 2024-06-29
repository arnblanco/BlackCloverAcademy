from pydantic import BaseModel, Field
from starlette.datastructures import Headers
from starlette.types import ASGIApp, Message, Receive, Scope, Send
from typing import Optional
from uuid import uuid4

from core.db import set_session_context, reset_session_context, session

class ResponseInfo(BaseModel):
    """
    Información de la respuesta HTTP.

    Atributos:
    - headers: Cabeceras de la respuesta (opcional).
    - body: Cuerpo de la respuesta.
    - status_code: Código de estado de la respuesta HTTP (opcional).
    """
    headers: Optional[Headers] = Field(default=None, title="Response header")
    body: str = Field(default="", title="MaxiTransfers")
    status_code: Optional[int] = Field(default=None, title="Status code")

    class Config:
        arbitrary_types_allowed = True


class ResponseLogMiddleware:
    """
    Middleware para registrar información de las respuestas HTTP.

    Este middleware intercepta las respuestas HTTP generadas por la aplicación
    y registra información relevante como cabeceras, cuerpo y código de estado.

    Atributos:
    - app: Instancia de la aplicación ASGI.

    Métodos:
    - __call__(scope, receive, send): Método de invocación para procesar cada solicitud.
    """
    def __init__(self, app: ASGIApp) -> None:
        """
        Inicializa una nueva instancia de ResponseLogMiddleware.

        Parámetros:
        - app: Instancia de la aplicación ASGI.
        """
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """
        Procesa la solicitud y registra información de la respuesta HTTP.

        Este método intercepta las respuestas HTTP, captura cabeceras, cuerpo y código
        de estado, y los registra en una instancia de ResponseInfo.

        Parámetros:
        - scope: Alcance de la solicitud.
        - receive: Función para recibir mensajes.
        - send: Función para enviar mensajes.
        """
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        response_info = ResponseInfo()

        async def _logging_send(message: Message) -> None:
            if message.get("type") == "http.response.start":
                response_info.headers = Headers(raw=message.get("headers"))
                response_info.status_code = message.get("status")
            elif message.get("type") == "http.response.body":
                if body := message.get("body"):
                    response_info.body += body.decode("utf8")

            await send(message)

        await self.app(scope, receive, _logging_send)


class SQLAlchemyMiddleware:
    """
    Middleware para gestionar sesiones de SQLAlchemy.

    Este middleware gestiona la creación y destrucción de sesiones de SQLAlchemy
    para cada solicitud. Utiliza un identificador único para cada sesión.

    Atributos:
    - app: Instancia de la aplicación ASGI.

    Métodos:
    - __call__(scope, receive, send): Método de invocación para procesar cada solicitud.
    """
    def __init__(self, app: ASGIApp) -> None:
        """
        Inicializa una nueva instancia de SQLAlchemyMiddleware.

        Parámetros:
        - app: Instancia de la aplicación ASGI.
        """
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """
        Procesa la solicitud y gestiona la sesión de SQLAlchemy.

        Este método gestiona la creación de una nueva sesión de SQLAlchemy para cada
        solicitud, y asegura que la sesión se cierre correctamente al finalizar la solicitud.

        Parámetros:
        - scope: Alcance de la solicitud.
        - receive: Función para recibir mensajes.
        - send: Función para enviar mensajes.
        """
        session_id = str(uuid4())
        context = set_session_context(session_id=session_id)

        try:
            await self.app(scope, receive, send)
        except Exception as e:
            raise e
        finally:
            await session.remove()
            reset_session_context(context=context)
