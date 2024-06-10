from django.contrib import admin
from .models import Period, Subject, Teacher, Note, Student, NoteDetail

admin.site.register(Period)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Note)
admin.site.register(Student)
admin.site.register(NoteDetail)
