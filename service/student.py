import random
from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.exceptions import StudentNotFountException
from model.student import Student
from schema.studen import CreateStudentRequest, UpdateStudentRequest

class StudentService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_student_by_id(self, student_id: int) -> Student:
        query = select(Student).where(Student.id == student_id)
        result = await self.db_session.execute(query)
        student = result.scalars().first()

        if not student:
            raise StudentNotFountException(f"Student with ID {student_id} not found.")
        
        return student

    async def get_students(self) -> List[Student]:
        query = select(Student)
        result = await self.db_session.execute(query)
        return result.scalars().all()

    async def get_student_grimoire(self) -> List[Student]:
        query = select(Student).where(Student.estado == True)
        result = await self.db_session.execute(query)
        return result.scalars().all()
    
    async def create_student(self, request: CreateStudentRequest) -> Student:
        student = Student(
            nombre=request.nombre,
            apellido=request.apellido,
            identificacion=request.identificacion,
            edad=request.edad,
            grimorio=self.assign_grimoire(),
            afinidad_magica=request.afinidad_magica
        )
        
        self.db_session.add(student)
        try:
            await self.db_session.commit()
            await self.db_session.refresh(student)
        except Exception as e:
            await self.db_session.rollback()
            raise e
        return student

    def assign_grimoire(self) -> str:
        grimorios = ["1 hoja", "2 hojas", "3 hojas", "4 hojas", "5 hojas"]
        probabilidades = [0.5, 0.35, 0.145, 0.004, 0.001]
        grimorio_asignado = random.choices(grimorios, probabilidades)[0]
        
        return grimorio_asignado

    async def update_student(self, student_id: int, request: UpdateStudentRequest) -> Student:
        student = await self.get_student_by_id(student_id)

        request_dict = request.dict(exclude={'id', 'grimorio', 'estado'})
        for key, value in request_dict.items():
            if hasattr(request, key) and value is not None:
                setattr(student, key, value)
        
        self.db_session.add(student)
        try:
            await self.db_session.commit()
            await self.db_session.refresh(student)
        except Exception as e:
            await self.db_session.rollback()
            raise e
        return student

    async def update_student_status(self, student_id: int) -> Student:
        student = await self.get_student_by_id(student_id)
        
        student.estado = not student.estado
        
        self.db_session.add(student)
        try:
            await self.db_session.commit()
            await self.db_session.refresh(student)
        except Exception as e:
            await self.db_session.rollback()
            raise e
        return student

    async def delete_student(self, student_id: int) -> bool:
        student = await self.get_student_by_id(student_id)
        try:
            await self.db_session.delete(student)
            await self.db_session.commit()
        except Exception as e:
            await self.db_session.rollback()
            raise e
        return True
