#!/bin/bash

# Ejecutar las migraciones de Alembic
alembic upgrade head

# Iniciar el servidor de FastAPI
uvicorn server:app --host 0.0.0.0 --port 8000 --reload