from django.contrib import admin
from .models import Period, Subject, Teacher, Note, Student, NoteDetail

class ModelBaseAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'user')
    list_display = ('created_at', 'updated_at', 'user', 'state')

class PeriodAdmin(ModelBaseAdmin):
    list_display = ('start_date', 'end_date') + ModelBaseAdmin.list_display

class SubjectAdmin(ModelBaseAdmin):
    list_display = ('description',) + ModelBaseAdmin.list_display

class TeacherAdmin(ModelBaseAdmin):
    list_display = ('dni', 'name') + ModelBaseAdmin.list_display

class NoteAdmin(ModelBaseAdmin):
    list_display = ('period', 'teacher', 'subject') + ModelBaseAdmin.list_display

class StudentAdmin(ModelBaseAdmin):
    list_display = ('dni', 'name') + ModelBaseAdmin.list_display

class NoteDetailAdmin(ModelBaseAdmin):
    list_display = ('note', 'student', 'note1', 'note2', 'recuperation', 'observation') + ModelBaseAdmin.list_display

admin.site.register(Period, PeriodAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(NoteDetail, NoteDetailAdmin)
