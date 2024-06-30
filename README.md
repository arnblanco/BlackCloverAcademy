# Proyecto Black Clover Academy

Bienvenido al repositorio del proyecto **Black Clover Academy**, un sistema de registro de estudiantes para la academia Clover.

## Descripción

Este proyecto utiliza FastAPI para la creación de una API RESTful que gestiona el registro de estudiantes en una base de datos PostgreSQL. Cada estudiante tiene atributos como nombre, apellido, edad, afinidad mágica y estado de activo/inactivo.

## Requisitos Previos

Asegúrate de tener instalado Docker y Docker Compose en tu sistema antes de comenzar.

## Configuración

1. Clona el repositorio:
   ```bash
   git clone <URL_del_repositorio>
   cd BlackCloverAcademy

2. Crea un archivo .env
    ```bash
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres

## Instalación y Ejecución

1. Levanta los contenedores de Docker (FastAPI y PostgreSQL):
   ```bash
   docker compose up --build -d

## Uso

Una vez que la aplicación esté en funcionamiento, puedes interactuar con la API mediante herramientas como `curl` o un cliente HTTP como Postman.

1. Uso por medio de web utilizado la documentacion de swagger
   ```bash
   http://localhost:8000/docs#/

## Endpoints Disponibles

- **GET /solicitud**: Obtiene la lista de todos los estudiantes registrados.
- **POST /solicitud**: Crea un nuevo estudiante con los datos proporcionados.
- **PUT /solicitud/{student_id}**: Actualiza los datos de un estudiante existente por su ID.
- **PATCH /solicitud/{student_id}**: Actualiza el estado (activo/inactivo) de un estudiante.
- **DELETE /solicitud/{student_id}**: Elimina un estudiante por su ID.
- **GET /asignaciones**: Obtiene la lista completa de estudiantes con información adicional de su grimorio.

## Contribución

Si deseas contribuir a este proyecto, ¡no dudes en enviar un pull request!

## Notas Adicionales

Asegúrate de mantener actualizado el archivo `.env` con las configuraciones correctas de PostgreSQL y otras variables de entorno necesarias para tu entorno de desarrollo o producción.

¡Disfruta explorando y trabajando con Black Clover Academy!