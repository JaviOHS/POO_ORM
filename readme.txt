Para instalar las dependencias:
    pip install -r requirements.txt

<- ORM ->
Ejecutar para guardar datos: 
    python orm.py

Pasos para consultar datos en en Shell de Django:
1. Abrir Shell de Django:
    python manage.py shell_plus --print-sql
    
2. Importar los modulos:
    from sga.models import Period, Subject, Teacher, Note, Student, NoteDetail

3. Consultar datos:
    periods = Period.objects.all()
        for period in periods:
            print(period)

<- WEB ->
Ejecutar para realizar cambios:
    py manage.py livereload
    npm run watch
    py manage.py runserver

    
