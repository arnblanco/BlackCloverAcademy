import random
from typing import List
from sqlalchemy import select

from core.db import session
from core.exceptions import StudentNotFountException

from model.student import Student
from schema.studen import CreateStudentRequest, UpdateStudentRequest

class Studentservice:
    def __init__(self):
        pass

    async def get_student_by_id(self, student_id: int) -> Student:
        """
        Obtiene un estudiante por su ID.

        Args:
        - student_id (int): ID del estudiante a buscar.

        Returns:
        - Student: Objeto Student correspondiente al ID proporcionado.

        Raises:
        - StudentNotFountException: Si no se encuentra ningún estudiante con el ID proporcionado.
        """
        query = select(Student).where(Student.id == student_id)
        result = await session.execute(query)
        student = result.scalars().first()

        if not student:
            raise StudentNotFountException
        
        return student

    async def get_students(self) -> List[Student]:
        """
        Obtiene todos los estudiantes.

        Returns:
        - List[Student]: Lista de objetos Student.
        """
        query = select(Student)
        result = await session.execute(query)
        return result.scalars().all()

    async def create_student(self, request: CreateStudentRequest) -> Student:
        """
        Crea un nuevo estudiante en la base de datos.

        Args:
        - request (CreateStudentRequest): Datos del estudiante a crear.

        Returns:
        - Student: Objeto Student creado.
        """
        student = Student(
            nombre=request.nombre,
            apellido=request.apellido,
            identificacion=request.identificacion,
            edad=request.edad,
            grimorio=self.assign_grimoire(),
            afinidad_magica=request.afinidad_magica
        )
        
        session.add(student)
        await session.commit()
        await session.refresh(student)
        return student

    def assign_grimoire(self) -> str:
        """
        Asigna aleatoriamente un tipo de grimorio.

        Returns:
        - str: Tipo de grimorio asignado.
        """
        grimorios = ["1 hoja", "2 hojas", "3 hojas", "4 hojas", "5 hojas"]
        probabilidades = [0.5, 0.35, 0.145, 0.004, 0.001]
        grimorio_asignado = random.choices(grimorios, probabilidades)[0]
        
        return grimorio_asignado

    async def update_student(self, student_id: int, request: UpdateStudentRequest) -> Student:
        """
        Actualiza los datos de un estudiante existente.

        Args:
        - student_id (int): ID del estudiante a actualizar.
        - request (UpdateStudentRequest): Datos actualizados del estudiante.

        Returns:
        - Student: Objeto Student actualizado.
        """
        student = await self.get_student_by_id(student_id)

        request_dict = request.dict(exclude={'id', 'grimorio', 'estado'})

        for key, value in request_dict.items():
            if hasattr(request, key) and value is not None:
                setattr(student, key, value)
        
        session.add(student)
        await session.commit()
        await session.refresh(student)
        return student

    async def update_student_status(self, student_id: int) -> Student:
        """
        Actualiza el estado activo/inactivo de un estudiante.

        Args:
        - student_id (int): ID del estudiante a actualizar.

        Returns:
        - Student: Objeto Student actualizado.
        """
        student = await self.get_student_by_id(student_id)
        
        student.estado = not student.estado
        
        session.add(student)
        await session.commit()
        await session.refresh(student)
        return student

    async def delete_student(self, student_id: int) -> bool:
        """
        Elimina un estudiante de la base de datos.

        Args:
        - student_id (int): ID del estudiante a eliminar.

        Returns:
        - bool: True si se eliminó correctamente.
        """
        student = await self.get_student_by_id(student_id)
        await session.delete(student)
        await session.commit()
        return True
