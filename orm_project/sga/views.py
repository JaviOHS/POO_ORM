from django.shortcuts import render

# ----------------- Vistas de Home -----------------
def home(request):
    data = {"title1": "SGA - Inicio",
            "title2": "Sistema de Gestion Academica"}
    return render(request, 'sga/home.html', data)

