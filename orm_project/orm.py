import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm_project.settings')
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from sga.models import Period, Subject, Teacher, Note, Student, NoteDetail
from django.db.models import Q, Window, F
from django.db.models.functions import Length 

red_color = "\033[1;31m"
yellow_color = "\033[1;33m"
reset_color = "\033[0m"

def probar_orm():
    print(yellow_color + '\nBulk Create' + reset_color)
    print(red_color + '1. Insertar 10 registros en la tabla Periodo:')
    def period_create(create=False):
        if create:
            user = User.objects.get(pk=1)
            now = timezone.now()
            Period.objects.bulk_create(
                [
                    Period(start_date="2021-01-01", end_date="2021-06-30", user=user, created_at=now),
                    Period(start_date="2021-07-01", end_date="2021-12-31", user=user, created_at=now),
                    Period(start_date="2022-01-01", end_date="2022-06-30", user=user, created_at=now),
                    Period(start_date="2022-07-01", end_date="2022-12-31", user=user, created_at=now),
                    Period(start_date="2023-01-01", end_date="2023-06-30", user=user, created_at=now),
                    Period(start_date="2023-07-01", end_date="2023-12-31", user=user, created_at=now),
                    Period(start_date="2024-01-01", end_date="2024-06-30", user=user, created_at=now),
                    Period(start_date="2024-07-01", end_date="2024-12-31", user=user, created_at=now),
                    Period(start_date="2025-01-01", end_date="2025-06-30", user=user, created_at=now),
                    Period(start_date="2025-07-01", end_date="2025-12-31", user=user, created_at=now),
                ]
            )
            print(reset_color + "Registros creados.")
    # period_create(create=True)
    
    print(red_color + "2. Insertar 10 registros en la tabla Asignaturas:")
    def subject_create(create=False):
        if create:
            user = User.objects.get(pk=1)
            now = timezone.now()
            Subject.objects.bulk_create(
                [
                    Subject(description="Matemáticas", user=user, created_at=now),
                    Subject(description="Física", user=user, created_at=now),
                    Subject(description="Química", user=user, created_at=now),
                    Subject(description="Biología", user=user, created_at=now),
                    Subject(description="Inglés", user=user, created_at=now),
                    Subject(description="Historia", user=user, created_at=now),
                    Subject(description="Geografía", user=user, created_at=now),
                    Subject(description="Educación Física", user=user, created_at=now),
                    Subject(description="Arte", user=user, created_at=now),
                    Subject(description="Música", user=user, created_at=now),
                ]
            )
            print(reset_color + "Registros creados.")
    # subject_create(create=True)
    
    print(red_color + "3. Insertar 10 registros en la tabla Profesor:")
    def teacher_create(create=False):
        if create:
            user = User.objects.get(pk=1)
            now = timezone.now()
            Teacher.objects.bulk_create(
                [
                    Teacher(dni="1719690487", name="Juan Pérez", user=user, created_at=now),
                    Teacher(dni="1717430100", name="María Rodríguez", user=user, created_at=now),
                    Teacher(dni="1723077382", name="Pedro Martínez", user=user, created_at=now),
                    Teacher(dni="1724354459", name="Ana Sánchez", user=user, created_at=now),
                    Teacher(dni="400988903", name="Carlos López", user=user, created_at=now),
                    Teacher(dni="202412755", name="Sofía Ramírez", user=user, created_at=now),
                    Teacher(dni="400966289", name="Jorge González", user=user, created_at=now),
                    Teacher(dni="1709839664", name="Laura Torres", user=user, created_at=now),
                    Teacher(dni="1708232754", name="Fernando Díaz", user=user, created_at=now),
                    Teacher(dni="1710203694", name="Patricia Vásquez", user=user, created_at=now),
                ]
            )
            print(reset_color + "Registros creados.")
    # teacher_create(create=True)
    
    print(red_color + "4. Insertar 10 registros en la tabla Estudiante:")
    def student_create(create=False):
        if create:
            user = User.objects.get(pk=1)
            now = timezone.now()
            Student.objects.bulk_create(
                [
                    Student(dni="1724309248", name="Nelson Garcia", user=user, created_at=now),
                    Student(dni="1714136312", name="Fausto Jaramillo", user=user, created_at=now),
                    Student(dni="1708191638", name="Bryan Mina", user=user, created_at=now),
                    Student(dni="1720579596", name="Ana Haro", user=user, created_at=now),
                    Student(dni="1708459886", name="Sara López", user=user, created_at=now),
                    Student(dni="200609691", name="Esteban Rosales", user=user, created_at=now),
                    Student(dni="601502008", name="Carlos Segundo", user=user, created_at=now),
                    Student(dni="1714020458", name="Sebastian Quiroz", user=user, created_at=now),
                    Student(dni="1710747757", name="Estefano Díaz", user=user, created_at=now),
                    Student(dni="1703445880", name="Rosero Telmo", user=user, created_at=now),
                ]
            )
            print(reset_color + "Registros creados.")
    # student_create(create=True)
    
    print(red_color + "5. Insertar 10 registros en la tabla Notas (.save, .create):")
    def note_create(create=False):
        if create:
            user = User.objects.get(pk=1)
            now = timezone.now()
            created_at = now
            for _ in range(10):
                period = random.choice(Period.objects.all())
                teacher = random.choice(Teacher.objects.all())
                subject = random.choice(Subject.objects.all())
                note = Note(
                    user=user,
                    created_at=created_at,
                    period=period,
                    teacher=teacher,
                    subject=subject
                )
                note.save() # .save(): Se utiliza para crear y actualizar instancias 
            print(reset_color + "Registros creados.")  
    # note_create(create=True)
    
    print(red_color + "6. Insertar 10 registros en la tabla DetalleNota: (.save, .create):")
    def note_detail_create(create=False):
        if create:
            user = User.objects.get(pk=1)
            now = timezone.now()
            created_at = now
            for _ in range(10):
                note = random.choice(Note.objects.all())
                student = random.choice(Student.objects.all())
                note1 = round(random.uniform(0, 10), 2)
                note2 = round(random.uniform(0, 10), 2)
                if random.choice([True, False]):
                    recuperation = round(random.uniform(0, 10), 2)
                else:
                    recuperation = None
                observation = "Sin comentarios."
                NoteDetail.objects.create( # .create(): Se utiliza para crear instancias
                    user=user,
                    created_at=created_at,
                    note=note,
                    student=student,
                    note1=note1,
                    note2=note2,
                    recuperation=recuperation,
                    observation=observation,
                )
            print(reset_color + "Registros creados.\n")
    # note_detail_create(create=True)
    
    def basic_queries():
        print(yellow_color + "\nConsultas" + reset_color)
        print(red_color + "1. Seleccionar todos los estudiantes cuyo nombre comienza con 'Est':")
        students_est = Student.objects.filter(name__istartswith='Est') # __istartswith: Busca los registros que comiencen con 'Est' sin importar si son mayúsculas o minúsculas.
        [print(f"{reset_color}- {student}") for student in students_est] if students_est else print(f"{reset_color}No hay registros.")
        
        print(red_color + "2. Seleccionar todos los profesores cuyo nombre contiene 'or':")
        teachers_or = Teacher.objects.filter(name__icontains='or') # __icontains: Busca los registros que contengan 'or' sin importar si son mayúsculas o minúsculas.
        [print(f"{reset_color}- {teacher}") for teacher in teachers_or] if teachers_or else print(f"{reset_color}No hay registros.")
        
        print(red_color + "3. Seleccionar todas las asignaturas cuya descripción termina en '10':")
        assign_10 = Subject.objects.filter(description__endswith='10') # __endswith: Busca los registros que terminen con '10'.
        [print(f"{reset_color}- {subject}") for subject in assign_10] if assign_10 else print(f"{reset_color}No hay registros.")	
        
        print(red_color + "4. Seleccionar todas las notas con nota1 mayor que 8.0:")
        notes_8 = NoteDetail.objects.filter(note1__gt=8.0) # __gt: Busca los registros con nota1 mayor que 8.0.
        [print(f"{reset_color}- {note}") for note in notes_8] if notes_8 else print(f"{reset_color}No hay registros.")
        
        print(red_color + "5. Seleccionar todas las notas con nota2 menor que 9.0:")
        notes_9 = NoteDetail.objects.filter(note2__lt=9.0) # __lt: Busca los registros con nota2 menor que 9.0.
        [print(f"{reset_color}- {note}") for note in notes_9] if notes_9 else print(f"{reset_color}No hay registros.")
        
        print(red_color + "6. Seleccionar todas las notas con recuperacion igual a 9.5:")
        recuperation_9_5 = NoteDetail.objects.filter(recuperation=9.5) # Es el mismo igual.
        [print(f"{reset_color}- {note}") for note in recuperation_9_5] if recuperation_9_5 else print(f"{reset_color}No hay registros.")
    #basic_queries()
    
    def conditionals_queries():
        print(yellow_color + "\nConsultas con Condiciones Logicas" + reset_color)
        print(red_color + "7. Seleccionar todos los estudiantes cuyo nombre comienza con 'Est' y su cedula termina en '1':")
        students = Student.objects.filter(
            Q(name__istartswith='Est') & Q(dni__iendswith="1") # Para realizar consultas con condiciones logicas solo se importa Q.
        )
        [print(f"{reset_color}- {student}") for student in students] if students else print(f"{reset_color}No hay registros.")
        
        print(red_color + "8. Seleccionar todas las asignaturas cuya descripción contiene 'Asig' o termina en '5':")
        subjects = Subject.objects.filter(
            Q(description__icontains='Est') | Q(description__endswith="5")
        )
        [print(f"{reset_color}- {subject}") for subject in subjects] if subjects else print(f"{reset_color}No hay registros.")
        
        print(red_color + "9. Seleccionar todos los profesores cuyo nombre no contiene 'or':")
        teachers = Teacher.objects.filter(
            ~Q(name__icontains='or') # Se coloca ~ al principio.
        )
        [print(f"{reset_color}- {teacher}") for teacher in teachers] if teachers else print(f"{reset_color}No hay registros.")
        
        print(red_color + "10. Seleccionar todas las notas con nota1 mayor que 7.0 y nota2 menor que 8.0:")
        notes = NoteDetail.objects.filter(
            Q(note1__gt=7.0) & Q(note2__lt=8.0)
        )
        [print(f"{reset_color}- {note}") for note in notes] if notes else print(f"{reset_color}No hay registros.")
        
        print(red_color + "11. Seleccionar todas las notas con recuperacion igual a None o nota2 mayor que 9.0:")
        notes_2 = NoteDetail.objects.filter(
            Q(recuperation=None) | Q(note2__gt=9.0)
        )
        [print(f"{reset_color}- {note}") for note in notes_2] if notes_2 else print(f"{reset_color}No hay registros.")
    # conditionals_queries()
    
    def numerical_queries():
        print(yellow_color + "\nConsultas con Funciones Numericas" + reset_color)
        print(red_color + "12. Seleccionar todas las notas con nota1 entre 7.0 y 9.0:")
        notes_3 = NoteDetail.objects.filter(
            note1__range=(7.0,9.0) # __range: Busca los registros con nota1 entre 7.0 y 9.0.
        )
        [print(f"{reset_color}- {note}") for note in notes_3] if notes_3 else print(f"{reset_color}No hay registros.")
    
        print(red_color + "13. Seleccionar todas las notas con nota2 fuera del rango 6.0 a 8.0:")
        notes_4 = NoteDetail.objects.filter(
            ~Q(note2__range=(6.0,8.0))
        )
        [print(f"{reset_color}- {note}") for note in notes_4] if notes_4 else print(f"{reset_color}No hay registros.")
        
        print(red_color + "14. Seleccionar todas las notas cuya recuperacion no sea None:")
        notes_5 = NoteDetail.objects.filter(
            ~Q(recuperation=None) 
        )
        [print(f"{reset_color}- {note}") for note in notes_5] if notes_5 else print(f"{reset_color}No hay registros.")
    # numerical_queries()
    
    def date_queries():
        print(yellow_color + "\nConsultas con Funciones de Fecha" + reset_color)
        print(red_color + "15. Seleccionar todas las notas creadas en el último año:")
        notes = NoteDetail.objects.filter(
            created_at__year=2024
        )
        [print(f"{reset_color}- {note}") for note in notes] if notes else print(f"{reset_color}No hay registros.")
        
        print(red_color + "16. Seleccionar todas las notas creadas en el último mes:")
        last_month = timezone.now() - timezone.timedelta(days=30)
        notes_2 = NoteDetail.objects.filter(
            created_at__gte=last_month
        )
        [print(f"{reset_color}- {note}") for note in notes_2] if notes_2 else print(f"{reset_color}No hay registros.")
        
        print(red_color + "17. Seleccionar todas las notas creadas en el último dia:")
        last_day = timezone.now() - timezone.timedelta(days=1)
        notes_3 = NoteDetail.objects.filter(
            created_at__gte=last_day
        )
        [print(f"{reset_color}- {note}") for note in notes_3] if notes_3 else print(f"{reset_color}No hay registros.")
        
        print(red_color + "18. Seleccionar todas las notas creadas antes del 2023:")
        notes_4 = NoteDetail.objects.filter(
            created_at__year__lt=2023
        )
        [print(f"{reset_color}- {note}") for note in notes_4] if notes_4 else print(f"{reset_color}No hay registros.")
        
        print(red_color + "19. Seleccionar todas las notas creadas en marzo de cualquier año:")    
        march_notes = NoteDetail.objects.filter(
            created_at__month=3
        )
        [print(f"{reset_color}- {note}") for note in march_notes] if march_notes else print(f"{reset_color}No hay registros.")
    # date_queries()
    
    def advances_queries():
        print(yellow_color + "\nConsultas con Funciones Avanzadas" + reset_color)
        print(red_color + "20. Seleccionar todos los estudiantes cuyo nombre tiene exactamente 10 caracteres:")
        students = Student.objects.annotate(name_length=Length('name')).filter(name_length=10) # Se define el campo name con la longitud y luego filtrar por la longitud.
        [print(f"{reset_color}- {student}") for student in students] if students else print(f"{reset_color}No hay registros.")
        
        print(red_color + "21. Seleccionar todas las notas con nota1 y nota2 mayores a 7.5:")
        notes = NoteDetail.objects.filter(
            Q(note1__gt=7.5) & Q(note2__gt=7.5) # Se puede directamente con (note1__gt=7.5, note2__gt=7.5).
        )
        [print(f"{reset_color}- {note}") for note in notes] if notes else print(f"{reset_color}No hay registros.")
        
        print(red_color + "22. Seleccionar todas las notas con recuperacion no nula y nota1 mayor a nota2:")
        notes_2 = NoteDetail.objects.filter(
            ~Q(recuperation=None) & Q(note1__gt=F('note2')) # Se utiliza F para comparar campos.
        )
        [print(f"{reset_color}- {note}") for note in notes_2] if notes_2 else print(f"{reset_color}No hay registros.")
        
        print(red_color + "23. Seleccionar todas las notas con nota1 mayor a 8.0 o nota2 igual a 7.5:")
        notes_3 = NoteDetail.objects.filter(
            Q(note1__gt=8.0) | Q(note2=7.5)
        )
        [print(f"{reset_color}- {note}") for note in notes_3] if notes_3 else print(f"{reset_color}No hay registros.")
        
        print(red_color + "24. Seleccionar todas las notas con recuperacion mayor a nota1 y nota2:")
        notes_4 = NoteDetail.objects.filter(
            recuperation__gt=F('note1') + F('note2') # Se suma los campos.
        )
        [print(f"{reset_color}- {note}") for note in notes_4] if notes_4 else print(f"{reset_color}No hay registros.")
    advances_queries()
        
    
if __name__ == "__main__":
    probar_orm()