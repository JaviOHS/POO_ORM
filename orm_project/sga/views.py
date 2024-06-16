from django.shortcuts import render

# ----------------- Vistas de Home -----------------
def home(request):
    data = {"title1": "SGA - Inicio",
            "title2": "Sistema de Gestion Academica"}
    return render(request, 'sga/home.html', data)

def period_list(request):
    data = {"title1": "SGA - Periodos",
            "title2": "Listado de Periodos"}
    return render(request, 'sga/periods.html', data)

def teacher_list(request):
    data = {"title1": "SGA - Docentes",
            "title2": "Listado de Docentes"}
    return render(request, 'sga/teachers.html', data)

def student_list(request):
    data = {"title1": "SGA - Estudiantes",
            "title2": "Listado de Estudiantes"}
    return render(request, 'sga/students.html', data)

def subject_list(request):
    data = {"title1": "SGA - Materias",
            "title2": "Listado de Materias"}
    return render(request, 'sga/subjects.html', data)

def notes_list(request):
    data = {"title1": "SGA - Notas",
            "title2": "Listado de Notas"}
    return render(request, 'sga/notes.html', data)

def notes_detail_list(request):
    data = {"title1": "SGA - Notas Detalle",
            "title2": "Listado de Notas Detalle"}
    return render(request, 'sga/notes_detail.html', data)