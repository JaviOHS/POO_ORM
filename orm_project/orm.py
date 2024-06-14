import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_project.settings")
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from sga.models import Period, Subject, Teacher, Note, Student, NoteDetail
from django.db.models import Q,Window,F,OuterRef,Subquery,Exists,Sum,FloatField,ExpressionWrapper,Max,Min,Avg,Count,Case,When,Value
from django.db.models.functions import Length, Coalesce

red_color = "\033[1;31m"
yellow_color = "\033[1;33m"
purple_color = "\033[1;35m"
reset_color = "\033[0m"


def probar_orm():
    def title(lol):
        print(red_color + lol + reset_color)

    def print_message(lol, add=None):
        if lol:
            if add:
                [print(f"- {add} {i}") for i in lol]
            else:
                [print(f"- {i}") for i in lol]
        else:
            print(f"No hay registros.")
        print(purple_color + "------" * 15 + reset_color)
        
    def note_detail(lol):
        for i in lol:
            print(f"Estudiante: {i.student.name}")
            print(f"Asignatura: {i.note.subject.description}")
            print(f"Período: {i.note.period.start_date} - {i.note.period.end_date}")
            print(f"Profesor: {i.note.teacher.name}")
            print(f"Nota1: {i.note1}")
            print(f"Nota2: {i.note2}")
            print(f"Recuperación: {i.recuperation}")
            print(f"Observación: {i.observation}")
            print(purple_color + "------" * 15 + reset_color)

    print(yellow_color + "\nBulk Create" + reset_color)
    title("1. Insertar 10 registros en la tabla Periodo:")

    def period_create(create=False):
        if create:
            user = User.objects.get(pk=1)
            now = timezone.now()
            Period.objects.bulk_create(
                [
                    Period(
                        start_date="2021-01-01",
                        end_date="2021-06-30",
                        user=user,
                        created_at=now,
                    ),
                    Period(
                        start_date="2021-07-01",
                        end_date="2021-12-31",
                        user=user,
                        created_at=now,
                    ),
                    Period(
                        start_date="2022-01-01",
                        end_date="2022-06-30",
                        user=user,
                        created_at=now,
                    ),
                    Period(
                        start_date="2022-07-01",
                        end_date="2022-12-31",
                        user=user,
                        created_at=now,
                    ),
                    Period(
                        start_date="2023-01-01",
                        end_date="2023-06-30",
                        user=user,
                        created_at=now,
                    ),
                    Period(
                        start_date="2023-07-01",
                        end_date="2023-12-31",
                        user=user,
                        created_at=now,
                    ),
                    Period(
                        start_date="2024-01-01",
                        end_date="2024-06-30",
                        user=user,
                        created_at=now,
                    ),
                    Period(
                        start_date="2024-07-01",
                        end_date="2024-12-31",
                        user=user,
                        created_at=now,
                    ),
                    Period(
                        start_date="2025-01-01",
                        end_date="2025-06-30",
                        user=user,
                        created_at=now,
                    ),
                    Period(
                        start_date="2025-07-01",
                        end_date="2025-12-31",
                        user=user,
                        created_at=now,
                    ),
                ]
            )
            print(reset_color + "Registros creados.")

    # period_create(create=True)

    title("2. Insertar 10 registros en la tabla Asignaturas:")

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

    title("3. Insertar 10 registros en la tabla Profesor:")

    def teacher_create(create=False):
        if create:
            user = User.objects.get(pk=1)
            now = timezone.now()
            Teacher.objects.bulk_create(
                [
                    Teacher(
                        dni="1719690487", name="Juan Pérez", user=user, created_at=now
                    ),
                    Teacher(
                        dni="1717430100",
                        name="María Rodríguez",
                        user=user,
                        created_at=now,
                    ),
                    Teacher(
                        dni="1723077382",
                        name="Pedro Martínez",
                        user=user,
                        created_at=now,
                    ),
                    Teacher(
                        dni="1724354459", name="Ana Sánchez", user=user, created_at=now
                    ),
                    Teacher(
                        dni="400988903", name="Carlos López", user=user, created_at=now
                    ),
                    Teacher(
                        dni="202412755", name="Sofía Ramírez", user=user, created_at=now
                    ),
                    Teacher(
                        dni="400966289",
                        name="Jorge González",
                        user=user,
                        created_at=now,
                    ),
                    Teacher(
                        dni="1709839664", name="Laura Torres", user=user, created_at=now
                    ),
                    Teacher(
                        dni="1708232754",
                        name="Fernando Díaz",
                        user=user,
                        created_at=now,
                    ),
                    Teacher(
                        dni="1710203694",
                        name="Patricia Vásquez",
                        user=user,
                        created_at=now,
                    ),
                ]
            )
            print(reset_color + "Registros creados.")

    # teacher_create(create=True)

    title("4. Insertar 10 registros en la tabla Estudiante:")

    def student_create(create=False):
        if create:
            user = User.objects.get(pk=1)
            now = timezone.now()
            Student.objects.bulk_create(
                [
                    Student(
                        dni="1724309248",
                        name="Nelson Garcia",
                        user=user,
                        created_at=now,
                    ),
                    Student(
                        dni="1714136312",
                        name="Fausto Jaramillo",
                        user=user,
                        created_at=now,
                    ),
                    Student(
                        dni="1708191638", name="Bryan Mina", user=user, created_at=now
                    ),
                    Student(
                        dni="1720579596", name="Ana Haro", user=user, created_at=now
                    ),
                    Student(
                        dni="1708459886", name="Sara López", user=user, created_at=now
                    ),
                    Student(
                        dni="200609691",
                        name="Esteban Rosales",
                        user=user,
                        created_at=now,
                    ),
                    Student(
                        dni="601502008",
                        name="Carlos Segundo",
                        user=user,
                        created_at=now,
                    ),
                    Student(
                        dni="1714020458",
                        name="Sebastian Quiroz",
                        user=user,
                        created_at=now,
                    ),
                    Student(
                        dni="1710747757",
                        name="Estefano Díaz",
                        user=user,
                        created_at=now,
                    ),
                    Student(
                        dni="1703445880", name="Rosero Telmo", user=user, created_at=now
                    ),
                ]
            )
            print(reset_color + "Registros creados.")

    # student_create(create=True)

    title("5. Insertar 10 registros en la tabla Notas (.save, .create):")

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
                    subject=subject,
                )
                note.save()  # .save(): Se utiliza para crear y actualizar instancias
            print(reset_color + "Registros creados.")

    # note_create(create=True)

    title("6. Insertar 10 registros en la tabla DetalleNota: (.save, .create):")

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
                NoteDetail.objects.create(  # .create(): Se utiliza para crear instancias
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
        title("1. Seleccionar todos los estudiantes cuyo nombre comienza con 'Est':")
        students_est = Student.objects.filter(
            name__istartswith="Est"
        )  # __istartswith: Busca los registros que comiencen con 'Est' sin importar si son mayúsculas o minúsculas.
        print_message(students_est)

        title("2. Seleccionar todos los profesores cuyo nombre contiene 'or':")
        teachers_or = Teacher.objects.filter(
            name__icontains="or"
        )  # __icontains: Busca los registros que contengan 'or' sin importar si son mayúsculas o minúsculas.
        print_message(teachers_or)

        title("3. Seleccionar todas las asignaturas cuya descripción termina en '10':")
        assign_10 = Subject.objects.filter(
            description__endswith="10"
        )  # __endswith: Busca los registros que terminen con '10'.
        print_message(assign_10)

        title("4. Seleccionar todas las notas con nota1 mayor que 8.0:")
        notes_8 = NoteDetail.objects.filter(
            note1__gt=8.0
        )  # __gt: Busca los registros con nota1 mayor que 8.0.
        print_message(notes_8)

        title("5. Seleccionar todas las notas con nota2 menor que 9.0:")
        notes_9 = NoteDetail.objects.filter(
            note2__lt=9.0
        )  # __lt: Busca los registros con nota2 menor que 9.0.
        print_message(notes_9)

        title("6. Seleccionar todas las notas con recuperacion igual a 9.5:")
        recuperation_9_5 = NoteDetail.objects.filter(
            recuperation=9.5
        )  # Es el mismo igual.
        print_message(recuperation_9_5)

    basic_queries()

    def conditionals_queries():
        print(yellow_color + "\nConsultas con Condiciones Logicas" + reset_color)
        title(
            "7. Seleccionar todos los estudiantes cuyo nombre comienza con 'Est' y su cedula termina en '1':"
        )
        students = Student.objects.filter(
            Q(name__istartswith="Est")
            & Q(
                dni__iendswith="1"
            )  # Para realizar consultas con condiciones logicas solo se importa Q.
        )
        print_message(students)

        title(
            "8. Seleccionar todas las asignaturas cuya descripción contiene 'Asig' o termina en '5':"
        )
        subjects = Subject.objects.filter(
            Q(description__icontains="Est") | Q(description__endswith="5")
        )
        print_message(subjects)

        title("9. Seleccionar todos los profesores cuyo nombre no contiene 'or':")
        teachers = Teacher.objects.filter(
            ~Q(name__icontains="or")  # Se coloca ~ al principio.
        )
        print_message(teachers)

        title(
            "10. Seleccionar todas las notas con nota1 mayor que 7.0 y nota2 menor que 8.0:"
        )
        notes = NoteDetail.objects.filter(Q(note1__gt=7.0) & Q(note2__lt=8.0))
        print_message(notes)

        title(
            "11. Seleccionar todas las notas con recuperacion igual a None o nota2 mayor que 9.0:"
        )
        notes_2 = NoteDetail.objects.filter(Q(recuperation=None) | Q(note2__gt=9.0))
        print_message(notes_2)

    conditionals_queries()

    def numerical_queries():
        print(yellow_color + "\nConsultas con Funciones Numericas" + reset_color)
        title("12. Seleccionar todas las notas con nota1 entre 7.0 y 9.0:")
        notes_3 = NoteDetail.objects.filter(
            note1__range=(
                7.0,
                9.0,
            )  # __range: Busca los registros con nota1 entre 7.0 y 9.0.
        )
        print_message(notes_3)

        title("13. Seleccionar todas las notas con nota2 fuera del rango 6.0 a 8.0:")
        notes_4 = NoteDetail.objects.filter(~Q(note2__range=(6.0, 8.0)))
        print_message(notes_4)

        title("14. Seleccionar todas las notas cuya recuperacion no sea None:")
        notes_5 = NoteDetail.objects.filter(~Q(recuperation=None))
        print_message(notes_5)

    numerical_queries()

    def date_queries():
        print(yellow_color + "\nConsultas con Funciones de Fecha" + reset_color)
        title("15. Seleccionar todas las notas creadas en el último año:")
        notes = NoteDetail.objects.filter(created_at__year=2024)
        print_message(notes)

        title("16. Seleccionar todas las notas creadas en el último mes:")
        last_month = timezone.now() - timezone.timedelta(days=30)
        notes_2 = NoteDetail.objects.filter(created_at__gte=last_month)
        print_message(notes_2)

        title("17. Seleccionar todas las notas creadas en el último dia:")
        last_day = timezone.now() - timezone.timedelta(days=1)
        notes_3 = NoteDetail.objects.filter(created_at__gte=last_day)
        print_message(notes_3)

        title("18. Seleccionar todas las notas creadas antes del 2023:")
        notes_4 = NoteDetail.objects.filter(created_at__year__lt=2023)
        print_message(notes_4)

        title("19. Seleccionar todas las notas creadas en marzo de cualquier año:")
        march_notes = NoteDetail.objects.filter(created_at__month=3)
        print_message(march_notes)

    date_queries()

    def advances_queries():
        print(yellow_color + "\nConsultas con Funciones Avanzadas" + reset_color)
        title(
            "20. Seleccionar todos los estudiantes cuyo nombre tiene exactamente 10 caracteres:"
        )
        students = Student.objects.annotate(name_length=Length("name")).filter(
            name_length=10
        )  # Se define el campo name con la longitud y luego filtrar por la longitud.
        print_message(students)

        title("21. Seleccionar todas las notas con nota1 y nota2 mayores a 7.5:")
        notes = NoteDetail.objects.filter(
            Q(note1__gt=7.5)
            & Q(
                note2__gt=7.5
            )  # Se puede directamente con (note1__gt=7.5, note2__gt=7.5).
        )
        print_message(notes)

        title(
            "22. Seleccionar todas las notas con recuperacion no nula y nota1 mayor a nota2:"
        )
        notes_2 = NoteDetail.objects.filter(
            ~Q(recuperation=None)
            & Q(note1__gt=F("note2"))  # Se utiliza F para comparar campos.
        )
        print_message(notes_2)

        title(
            "23. Seleccionar todas las notas con nota1 mayor a 8.0 o nota2 igual a 7.5:"
        )
        notes_3 = NoteDetail.objects.filter(Q(note1__gt=8.0) | Q(note2=7.5))
        print_message(notes_3)

        title("24. Seleccionar todas las notas con recuperacion mayor a nota1 y nota2:")
        notes_4 = NoteDetail.objects.filter(
            recuperation__gt=F("note1") + F("note2")  # Se suma los campos.
        )
        print_message(notes_4)

    advances_queries()

    def subqueries_annotations():
        print(yellow_color + "\nConsultas con Subconsultas y Anotaciones" + reset_color)
        title(
            "25. Seleccionar todos los estudiantes con al menos una nota de recuperación:"
        )
        recuperation_notes = NoteDetail.objects.filter(
            student=OuterRef("pk"),
            recuperation__isnull=False,  # OuterRef: para referenciar el campo pk.
        )
        students_recuperation = Student.objects.annotate(
            has_recuperation=Exists(
                recuperation_notes
            )  # Exists: para verificar si existe al menos un registro.
        ).filter(has_recuperation=True)
        print_message(students_recuperation)

        def subject_specific(subject):
            title(
                "26. Seleccionar todos los profesores que han dado una asignatura específica:"
            )
            subject_subquery = Subject.objects.filter(description=subject).values(
                "pk"
            )  # Otener el pk de la asignatura.
            subject_ = Note.objects.filter(
                subject__id=OuterRef("pk"),
                subject__in=subject_subquery,  # Verificar si el pk de la asignatura esta en la subconsulta.
            )
            teachers = Teacher.objects.filter(Exists(subject_))
            print_message(
                teachers, add=f"Docentes que han dado la asignatura de {subject}: "
            )

        subject_specific("Matemáticas")

        title(
            "27. Seleccionar todas las asignaturas que tienen al menos una nota registrada:"
        )
        subject_note = Note.objects.filter(subject=OuterRef("pk"))
        subject_note_register = Subject.objects.annotate(
            note_exist=Exists(subject_note)
        ).filter(
            note_exist=True
        )  # Solo materias que tienen al menos una nota registrada.
        print_message(subject_note_register)

        title("28. Seleccionar todas las asignaturas que no tienen notas registradas:")
        subject_note_register_2 = Subject.objects.annotate(
            note_exist=Exists(subject_note)
        ).filter(note_exist=False)
        print_message(subject_note_register_2)

        title(
            "29. Seleccionar todos los estudiantes que no tienen notas de recuperación:"
        )
        students = Student.objects.annotate(
            recuperation=Exists(recuperation_notes)
        ).filter(recuperation=False)
        print_message(students)

        title(
            "30. Seleccionar todas las notas cuyo promedio de nota1 y nota2 es mayor a 8.0:"
        )
        notes = NoteDetail.objects.annotate(
            average=(F("note1") + F("note2"))
            / 2  # average: Crea un campo calculado con la suma de note1 y note2 en la consulta del ORM.
        ).filter(average__gt=8.0)
        print_message(notes)

        title(
            "31. Seleccionar todas las notas con nota1 menor que 6.0 y nota2 mayor que 7.0:"
        )
        calculte_notes = NoteDetail.objects.filter(note1__lt=6.0, note2__gt=7.0)
        print_message(calculte_notes)

        title("32. Seleccionar todas las notas con nota1 en la lista [7.0, 8.0, 9.0]:")
        note_list = [7.9, 8.0, 9.0]
        notes_in_list = NoteDetail.objects.filter(note1__in=note_list)
        specific_notes = NoteDetail.objects.filter(
            note1__in=Subquery(
                notes_in_list.values("note1")
            )  # Subquery: para obtener los valores de la subconsulta.
        )
        print_message(specific_notes)

        title("33. Seleccionar todas las notas cuyo id está en un rango del 1 al 5:")
        range_notes = Note.objects.filter(id__range=(1, 5))
        specific_notes = Note.objects.filter(id__in=Subquery(range_notes.values("id")))
        (
            [print(f"-ID: {note.id} {note}") for note in specific_notes]
            if specific_notes
            else print(f"{reset_color}No hay registros.")
        )
        print(purple_color + "------" * 15 + reset_color)

        title(
            "34. Seleccionar todas las notas cuyo recuperacion no está en la lista [8.0, 9.0, 10.0]:"
        )
        note_list_2 = [8.0, 9.0, 10.0]
        recuperation_note_in_list = NoteDetail.objects.filter(
            recuperation__in=note_list_2
        )
        specific_notes = NoteDetail.objects.filter(
            recuperation__in=Subquery(recuperation_note_in_list.values("recuperation"))
        )
        print_message(specific_notes)

        def calculate_notes(student):
            title("35. Suma de todas las notas de un estudiante:")
            notes = NoteDetail.objects.filter(student=student)
            total_note1 = (
                notes.aggregate(total_note1=Sum("note1", output_field=FloatField()))[
                    "total_note1"
                ]
                or 0
            )
            total_note2 = (
                notes.aggregate(total_note2=Sum("note2", output_field=FloatField()))[
                    "total_note2"
                ]
                or 0
            )
            total_recuperation = (
                notes.aggregate(
                    total_recuperation=Sum("recuperation", output_field=FloatField())
                )["total_recuperation"]
                or 0
            )
            total = total_note1 + total_note2 + total_recuperation
            print_message(notes)
            print(f"- Suma total de notas: {total}")
            print(purple_color + "------" * 15 + reset_color)

        calculate_notes(Student.objects.get(pk=1))

        def max_note(student):
            title("36. Nota máxima obtenida por un estudiante:")
            note_max = NoteDetail.objects.filter(student=student).aggregate(
                max_note1=Max("note1"),
                max_note2=Max("note2"),
                max_recuperation=Max("recuperation"),
            )
            max_note_values = [
                note_max.get("max_note1", 0),
                note_max.get("max_note2", 0),
                note_max.get("max_recuperation", 0),
            ]
            max_note_values = [value for value in max_note_values if value is not None]
            if max_note_values:
                max_note_value = max(max_note_values)
                print(
                    f"- Nota máxima obtenida por el estudiante {student}: {max_note_value}"
                )
            else:
                print(f"- El estudiante {student} no tiene ninguna nota registrada.")
            print(purple_color + "------" * 15 + reset_color)

        max_note(Student.objects.get(pk=1))

        def min_note(student):
            title("37. Nota mínima obtenida por un estudiante:")
            note_min = NoteDetail.objects.filter(student=student).aggregate(
                min_note1=Min("note1"),
                min_note2=Min("note2"),
                min_recuperation=Min("recuperation"),
            )
            min_note_values = [
                note_min.get("min_note1", 0),
                note_min.get("min_note2", 0),
                note_min.get("min_recuperation", 0),
            ]
            min_note_values = [value for value in min_note_values if value is not None]

            if min_note_values:
                min_note_value = min(min_note_values)
                print(
                    f"- Nota mínima obtenida por el estudiante {student}: {min_note_value}"
                )
            else:
                print(f"- El estudiante {student} no tiene ninguna nota registrada.")
            print(purple_color + "------" * 15 + reset_color)

        min_note(Student.objects.get(pk=1))

        def total_notes(student):
            title("38. Contar el número total de notas de un estudiante:")
            student_notes = NoteDetail.objects.filter(student=student).aggregate(
                total_notes=Count("id")
            )
            print_message(NoteDetail.objects.filter(student=student))
            print(f"- Número total de notas: {student_notes['total_notes']}")
            print(purple_color + "------" * 15 + reset_color)

        total_notes(Student.objects.get(pk=1))

        def average_notes(student):
            title(
                "39. Promedio de todas las notas de un estudiante sin incluir recuperación"
            )
            student_notes = NoteDetail.objects.filter(student=student).aggregate(
                average_note1=Avg("note1"), average_note2=Avg("note2")
            )
            total = round(
                (student_notes["average_note1"] + student_notes["average_note2"]) / 2, 2
            )
            print_message(NoteDetail.objects.filter(student=student))
            print(f"- Promedio de notas del estudiante {student}: {total}")
            print(purple_color + "------" * 15 + reset_color)

        average_notes(Student.objects.get(pk=1))

    subqueries_annotations()

    def subqueries_inverse_relationships():
        print(yellow_color + "\nSubconsultas con modelos relacionados - Aplicar relaciones inversas" + reset_color)
        
        def student_notes():
            title(
                "40. Dado un estudiante obtener todas sus notas con el detalle de todos sus datos relacionados:"
            )
            try:
                student = Student.objects.get(pk=1)
            except Student.DoesNotExist:
                print("El estudiante especificado no existe.")
                return
            notes_details = NoteDetail.objects.filter(student=student).values(
                "note__subject__description",
                "note__period__start_date",
                "note__period__end_date",
                "note__teacher__name",
                "note1",
                "note2",
                "recuperation",
                "observation",
            )
            notes = NoteDetail.objects.filter(student=student).annotate(
                note_subject=Subquery(notes_details.values("note__subject__description")[:1]),
                note_period_start=Subquery(
                    notes_details.values("note__period__start_date")[:1]
                ),
                note_period_end=Subquery(notes_details.values("note__period__end_date")[:1]),
                note_teacher=Subquery(notes_details.values("note__teacher__name")[:1]),
            )
            note_detail(notes)
        student_notes()
        
        def specific_period():
            title("41. Obtener todas las notas de un período específico:")
            try:
                period = Period.objects.get(pk=2)
            except Period.DoesNotExist:
                print("El período especificado no existe.")
                return
            notes = Note.objects.filter(period=period)
            if not notes.exists():
                print("No hay notas para el período especificado.")
                return
            details_note = NoteDetail.objects.filter(note__in=notes)
            if not details_note.exists():
                print("No hay detalles de notas para las notas del período especificado.")
                return
            note_detail(details_note)
        specific_period()
        
        def specific_sucject():
            title("42. Consultar todas las notas de una asignatura dada en un período:")
            try:
                period = Period.objects.get(pk=2)
            except Period.DoesNotExist:
                print("El período especificado no existe.")
                return
            subject = Note.objects.filter(subject__description="Arte", period=period)
            if not subject.exists():
                print("No hay asignaturas para las notas del período especificado.")
                return
            notes = NoteDetail.objects.filter(note__in=subject)
            if not notes.exists():
                print("No hay detalles de notas para las notas del período especificado.")
                return
            note_detail(notes)
        specific_sucject()
        
        def specific_teacher():
            title("43. Obtener todas las notas de un profesor en particular:")
            try:
                teacher = Teacher.objects.get(pk=10)
            except Teacher.DoesNotExist:
                print("El docente especificado no existe.")
                return
            notes = Note.objects.filter(teacher=teacher) # Se puede hacer directamente filtrando: teacher__id=10, teacher__name="...", teacher__dni="...".
            if not notes.exists():
                print("No hay notas para el profesor especificado.")
                return
            details_note = NoteDetail.objects.filter(note__in=notes)
            if not details_note.exists():
                print("No hay detalles de notas para las notas del profesor especificado.")
                return
            note_detail(details_note)
        specific_teacher()
        
        def notes_specific_student():
            title("44. Consultar todas las notas de un estudiante con notas superiores a un valor dado:")
            try:
                student = Student.objects.get(pk=1)
            except Student.DoesNotExist:
                print("El estudiante especificado no existe.")
                return
            notes = NoteDetail.objects.filter(student=student, note1__gt=7.0, note2__gt=7.0)
            if not notes.exists ():
                print("El estudiante no cumple con los requisitos especificados. (Nota 1 y 2 < 7.0 ) ")
                return
            note_detail(notes)
        notes_specific_student()
        
        def period_notes_students_order():
            title("45. Obtener todas las notas de un estudiante ordenadas por período:")
            try:
                student = Student.objects.get(pk=1)
            except Student.DoesNotExist:
                print("El estudiante especificado no existe.")
                return
            notes = NoteDetail.objects.filter(student=student).order_by("note__period__start_date") # order_by: Ordenar por el campo especificado.
            if not notes.exists():
                print("El estudiante no tiene notas registradas.")
                return
            note_detail(notes)
            
        period_notes_students_order()
        
        def count_notes_students():
            title("46. Consultar la cantidad total de notas para un estudiante:")
            try:
                students = Student.objects.get(pk=1)
            except Student.DoesNotExist:
                print("El estudiante especificado no existe.")
                return
            notes = NoteDetail.objects.filter(student=students).count()
            if notes == 0:
                print("El estudiante especificado no tiene notas registradas.")
                return
            print(f"Estudiante: {students.name}\nCantidad total de notas: {notes}\n{purple_color}{"------" * 15}{reset_color}")
        count_notes_students()
        
    subqueries_inverse_relationships()


if __name__ == "__main__":
    probar_orm()
