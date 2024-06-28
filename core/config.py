from fastapi import FastAPI, Request, Depends
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List

from core.exceptions import CustomException
from core.logging import Logging
from core.middleware import ResponseLogMiddleware


def init_listeners(app_: FastAPI) -> None:
    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(ResponseLogMiddleware),
    ]
    return middleware


def create_app() -> FastAPI:
    app_ = FastAPI(
    title="Black Clover Academy",
        description="Clover Academy student registration system.",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        dependencies=[Depends(Logging)],
        middleware=make_middleware(),
    )
    init_listeners(app_=app_)
    return app_
