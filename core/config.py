from fastapi import FastAPI, Request, Depends
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List

from core.exceptions import CustomException
from core.logging import Logging
from core.middleware import ResponseLogMiddleware, SQLAlchemyMiddleware

def init_listeners(app_: FastAPI) -> None:
    """
    Inicializa los listeners y manejadores de excepciones personalizadas.

    Este función configura el manejador de excepciones para CustomException
    y define cómo se deben manejar las excepciones en la aplicación.

    Parámetros:
    - app_ (FastAPI): Instancia de la aplicación FastAPI.
    """
    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        """
        Manejador de excepciones para CustomException.

        Este manejador responde con un JSON que incluye el código de error y el mensaje
        de la excepción personalizada.

        Parámetros:
        - request (Request): Objeto de solicitud FastAPI.
        - exc (CustomException): Instancia de la excepción CustomException.

        Retorna:
        - JSONResponse: Respuesta JSON con detalles de la excepción.
        """
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )

def make_middleware() -> List[Middleware]:
    """
    Configura y devuelve una lista de middlewares para la aplicación FastAPI.

    Retorna:
    - List[Middleware]: Lista de middlewares configurados para la aplicación.
    """
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(SQLAlchemyMiddleware),
        Middleware(ResponseLogMiddleware),
    ]
    return middleware

def create_app() -> FastAPI:
    """
    Crea y configura la aplicación FastAPI.

    Retorna:
    - FastAPI: Instancia de la aplicación FastAPI configurada.
    """
    app_ = FastAPI(
        title="Black Clover Academy",
        description="Clover Academy student registration system.",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        dependencies=[Depends(Logging)],  # Dependencia global para el registro de logs
        middleware=make_middleware(),  # Configura los middlewares de la aplicación
    )
    init_listeners(app_=app_)  # Inicializa los listeners y manejadores de excepciones
    return app_
