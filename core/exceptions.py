from http import HTTPStatus

class CustomException(Exception):
    """
    Excepción base personalizada.

    Atributos:
    - code: Código de estado HTTP asociado a la excepción.
    - error_code: Código de error específico.
    - message: Mensaje de error.
    """

    code = HTTPStatus.BAD_GATEWAY
    error_code = HTTPStatus.BAD_GATEWAY
    message = HTTPStatus.BAD_GATEWAY.description

    def __init__(self, message=None):
        """
        Inicializa una nueva instancia de CustomException.

        Parámetros:
        - message: Mensaje de error personalizado (opcional).
        """
        if message:
            self.message = message


class BadRequestException(CustomException):
    """
    Excepción para errores de solicitud incorrecta (400 Bad Request).

    Atributos:
    - code: Código de estado HTTP 400.
    - error_code: Código de error específico 400.
    - message: Descripción del error 400.
    """
    code = HTTPStatus.BAD_REQUEST
    error_code = HTTPStatus.BAD_REQUEST
    message = HTTPStatus.BAD_REQUEST.description


class NotFoundException(CustomException):
    """
    Excepción para recursos no encontrados (404 Not Found).

    Atributos:
    - code: Código de estado HTTP 404.
    - error_code: Código de error específico 404.
    - message: Descripción del error 404.
    """
    code = HTTPStatus.NOT_FOUND
    error_code = HTTPStatus.NOT_FOUND
    message = HTTPStatus.NOT_FOUND.description


class ForbiddenException(CustomException):
    """
    Excepción para acceso prohibido (403 Forbidden).

    Atributos:
    - code: Código de estado HTTP 403.
    - error_code: Código de error específico 403.
    - message: Descripción del error 403.
    """
    code = HTTPStatus.FORBIDDEN
    error_code = HTTPStatus.FORBIDDEN
    message = HTTPStatus.FORBIDDEN.description


class UnauthorizedException(CustomException):
    """
    Excepción para acceso no autorizado (401 Unauthorized).

    Atributos:
    - code: Código de estado HTTP 401.
    - error_code: Código de error específico 401.
    - message: Descripción del error 401.
    """
    code = HTTPStatus.UNAUTHORIZED
    error_code = HTTPStatus.UNAUTHORIZED
    message = HTTPStatus.UNAUTHORIZED.description


class UnprocessableEntity(CustomException):
    """
    Excepción para entidad no procesable (422 Unprocessable Entity).

    Atributos:
    - code: Código de estado HTTP 422.
    - error_code: Código de error específico 422.
    - message: Descripción del error 422.
    """
    code = HTTPStatus.UNPROCESSABLE_ENTITY
    error_code = HTTPStatus.UNPROCESSABLE_ENTITY
    message = HTTPStatus.UNPROCESSABLE_ENTITY.description


class DuplicateValueException(CustomException):
    """
    Excepción para valores duplicados (422 Unprocessable Entity).

    Atributos:
    - code: Código de estado HTTP 422.
    - error_code: Código de error específico 422.
    - message: Descripción del error 422.
    """
    code = HTTPStatus.UNPROCESSABLE_ENTITY
    error_code = HTTPStatus.UNPROCESSABLE_ENTITY
    message = HTTPStatus.UNPROCESSABLE_ENTITY.description


class DatabaseConnectionErrorException(CustomException):
    """
    Excepción para errores de conexión a la base de datos.

    Atributos:
    - code: Código de estado HTTP 404.
    - error_code: Código de error específico 'DATABASE_CONNECTION_ERROR_EXCEPTION'.
    - message: Descripción del error de conexión a la base de datos.
    """
    code = HTTPStatus.NOT_FOUND
    error_code = 'DATABASE_CONNECTION_ERROR_EXCEPTION'
    message = 'Database connection error exception'


class DatabaseSQLErrorException(CustomException):
    """
    Excepción para errores SQL en la base de datos.

    Atributos:
    - code: Código de estado HTTP 404.
    - error_code: Código de error específico 'DATABASE_SQL_ERROR_EXCEPTION'.
    - message: Descripción del error SQL en la base de datos.
    """
    code = HTTPStatus.NOT_FOUND
    error_code = 'DATABASE_SQL_ERROR_EXCEPTION'
    message = 'Database SQL error exception'


class StudentNotFountException(CustomException):
    """
    Excepción para estudiante no encontrado.

    Atributos:
    - code: Código de estado HTTP 404.
    - error_code: Código de error específico 'STUDENT_NOT_FOUND_EXCEPTION'.
    - message: Descripción del error 'Estudiante no encontrado'.
    """
    code = HTTPStatus.NOT_FOUND
    error_code = 'STUDENT_NOT_FOUND_EXCEPTION'
    message = 'Student not found.'
