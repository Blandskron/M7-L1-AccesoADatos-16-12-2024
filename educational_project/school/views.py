from django.shortcuts import render
from django.db import connection
from .models import Estudiante

# Create your views here.
def custom_sql_query(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM school_estudiante WHERE edad > %s", [18])
        rows = cursor.fetchall()
    
    return render(request, 'estudiantes.html', {'estudiantes': rows})

def raw_query_example(request):
    estudiante = Estudiante.objects.raw('SELECT * FROM school_estudiante WHERE edad > %s', [15])
    return render(request, 'estudiantes.html', {'estudiantes': estudiante})
