from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from orm_project.utils import valida_cedula, valida_numero_flotante_positivo, valida_numero_entero_positivo

class ModelBase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Period(ModelBase):
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.start_date.strftime('%Y-%m-%d')} - {self.end_date.strftime('%Y-%m-%d')}"

class Subject(ModelBase):
    description = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.description

class Teacher(ModelBase):
    dni = models.CharField(max_length=10,validators=[valida_cedula],unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.dni}"

class Note(ModelBase):
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject} - {self.period} - {self.teacher}"

class Student(ModelBase):
    dni = models.CharField(max_length=10,validators=[valida_cedula])
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.dni}"

class NoteDetail(ModelBase):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    note1 = models.FloatField(validators=[valida_numero_flotante_positivo])
    note2 = models.FloatField(validators=[valida_numero_flotante_positivo])
    recuperation = models.FloatField(validators=[valida_numero_flotante_positivo])
    observation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.name} - {self.note.subject} - Nota1: {self.note1} - Nota2: {self.note2} - Recuperacion: {self.recuperation}"
