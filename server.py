"""
FastAPI application for managing student requests.

This module defines endpoints to perform CRUD operations on student data.
"""
from fastapi import Depends, Request
from fastapi.responses import JSONResponse
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from core import create_app
from core.db import session
from service.student import StudentService
from schema.studen import CreateStudentRequest, UpdateStudentRequest, StudentResponse, FullStudentResponse

# Start FastAPI application
app = create_app()

# Dependencia para obtener la sesión de la base de datos
async def get_db_session() -> AsyncSession:
    async with session() as db_session:
        yield db_session


@app.get('/')
async def index(request: Request):
    """
    Endpoint to get the welcome message.

    Args:
    - request (Request): The incoming request object.

    Returns:
    - JSONResponse: A JSON response with a welcome message.
    """
    return JSONResponse(content={ "msg": f"Welcome to FastApi starter project!!" })

@app.get(
    "/solicitud",
    response_model=List[StudentResponse]
)
async def get_students_list(db_session: AsyncSession = Depends(get_db_session)):
    """
    Endpoint to retrieve a list of all students.

    Args:
    - service (Studentservice): Instance of Studentservice dependency.

    Returns:
    - List[StudentResponse]: A list of StudentResponse objects.
    """
    service = StudentService(db_session)
    return await service.get_students()

@app.post(
    "/solicitud",
    response_model=StudentResponse
)
async def create_student(
    request: CreateStudentRequest,
    db_session: AsyncSession = Depends(get_db_session)
):
    """
    Endpoint to create a new student.

    Args:
    - request (CreateStudentRequest): Data for creating a new student.
    - service (Studentservice): Instance of Studentservice dependency.

    Returns:
    - StudentResponse: Newly created student details.
    """
    service = StudentService(db_session)
    return await service.create_student( request )

@app.put(
    "/solicitud/{student_id}",
    response_model=StudentResponse
)
async def update_student(
    student_id: int,
    request: UpdateStudentRequest,
    db_session: AsyncSession = Depends(get_db_session)
):
    """
    Endpoint to update student details by ID.

    Args:
    - student_id (int): ID of the student to update.
    - request (UpdateStudentRequest): Updated student data.
    - service (Studentservice): Instance of Studentservice dependency.

    Returns:
    - StudentResponse: Updated student details.
    """
    service = StudentService(db_session)
    return await service.update_student( student_id, request )

@app.patch(
    "/solicitud/{student_id}",
    response_model=StudentResponse
)
async def update_student_status(
    student_id: int,
    db_session: AsyncSession = Depends(get_db_session)
):
    """
    Endpoint to toggle the status of a student (active/inactive).

    Args:
    - student_id (int): ID of the student to update.
    - service (Studentservice): Instance of Studentservice dependency.

    Returns:
    - StudentResponse: Updated student details.
    """
    service = StudentService(db_session)
    return await service.update_student_status( student_id )

@app.delete(
    "/solicitud/{student_id}",
)
async def delete_student(
    student_id: int,
    db_session: AsyncSession = Depends(get_db_session)
):
    """
    Endpoint to delete a student by ID.

    Args:
    - student_id (int): ID of the student to delete.
    - service (Studentservice): Instance of Studentservice dependency.

    Returns:
    - bool: True if deletion was successful.
    """
    service = StudentService(db_session)
    return await service.delete_student( student_id )

@app.get(
    "/asignaciones",
    response_model=List[FullStudentResponse]
)
async def get_full_list(db_session: AsyncSession = Depends(get_db_session)):
    """
    Endpoint to retrieve a list of all students.

    Args:
    - service (Studentservice): Instance of Studentservice dependency.

    Returns:
    - List[FullStudentResponse]: A list of FullStudentResponse objects.
    """
    service = StudentService(db_session)
    return await service.get_student_grimoire()