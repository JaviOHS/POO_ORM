import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm_project.settings')
django.setup()

from django.contrib.auth.models import User
from sga.models import Period, Subject, Teacher, Note, Student, NoteDetail

def probar_orm():
    # Insertar 10 registros en la tabla Periodo:
    def period_create(create=False):
        if create:
            user = User.objects.get(pk=1)
            Period.objects.bulk_create(
				[
					Period(start_date="2021-01-01", end_date="2021-06-30", user=user),
					Period(start_date="2021-07-01", end_date="2021-12-31", user=user),
					Period(start_date="2022-01-01", end_date="2022-06-30", user=user),
					Period(start_date="2022-07-01", end_date="2022-12-31", user=user),
					Period(start_date="2023-01-01", end_date="2023-06-30", user=user),
					Period(start_date="2023-07-01", end_date="2023-12-31", user=user),
					Period(start_date="2024-01-01", end_date="2024-06-30", user=user),
					Period(start_date="2024-07-01", end_date="2024-12-31", user=user),
					Period(start_date="2025-01-01", end_date="2025-06-30", user=user),
					Period(start_date="2025-07-01", end_date="2025-12-31", user=user),
				]
			)
    # period_create(create=True)
    
    # Insertar 10 registros en la tabla Asignaturas:
    def subject_create(create=False):
        if create:
            user = User.objects.get(pk=1)
            Subject.objects.bulk_create(
				[
					Subject(description="Matemáticas", user=user),
					Subject(description="Física", user=user),
					Subject(description="Química", user=user),
					Subject(description="Biología", user=user),
					Subject(description="Inglés", user=user),
					Subject(description="Historia", user=user),
					Subject(description="Geografía", user=user),
					Subject(description="Educación Física", user=user),
					Subject(description="Arte", user=user),
					Subject(description="Música", user=user),
				]
    		)
    # subject_create(create=True)
    
    # Insertar 10 registros en la tabla Profesor:
    def teacher_create(create=False):
        if create:
            user = User.objects.get(pk=1)
            Teacher.objects.bulk_create(
				[
					Teacher(dni="1719690487", name="Juan Pérez", user=user),
					Teacher(dni="1717430100", name="María Rodríguez", user=user),
					Teacher(dni="1723077382", name="Pedro Martínez", user=user),
					Teacher(dni="1724354459", name="Ana Sánchez", user=user),
					Teacher(dni="400988903", name="Carlos López", user=user),
					Teacher(dni="202412755", name="Sofía Ramírez", user=user),
					Teacher(dni="400966289", name="Jorge González", user=user),
					Teacher(dni="1709839664", name="Laura Torres", user=user),
					Teacher(dni="1708232754", name="Fernando Díaz", user=user),
					Teacher(dni="1710203694", name="Patricia Vásquez", user=user),
				]
			)
    # teacher_create(create=True)
    
    # Insertar 10 registros en la tabla Estudiante:
    def student_create(create=False):
        if create:
            user = User.objects.get(pk=1)
            Student.objects.bulk_create(
				[
					Student(dni="1724309248", name="Nelson Garcia", user=user),
					Student(dni="1714136312", name="Fausto Jaramillo", user=user),
					Student(dni="1708191638", name="Bryan Mina", user=user),
					Student(dni="1720579596", name="Ana Haro", user=user),
					Student(dni="1708459886", name="Sara López", user=user),
					Student(dni="200609691", name="Hugp Rosales", user=user),
					Student(dni="601502008", name="Carlos Segundo", user=user),
					Student(dni="1714020458", name="Sebastian Quiroz", user=user),
					Student(dni="1710747757", name="Elias Díaz", user=user),
					Student(dni="1703445880", name="Rosero Telmo", user=user),
				]
			)
	# student_create(create=True)
	
if __name__ == "__main__":
    probar_orm()