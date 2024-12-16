# Django Project: School Management System

## Overview
This Django project is a basic School Management System that demonstrates the use of models, views, custom SQL queries, and integration with PostgreSQL. It manages students and courses, showcasing how to query data using both the ORM and raw SQL.

---

## Features

- **Models:**
  - `Estudiante`: Represents students with attributes such as `nombre`, `apellido`, `correo`, `edad`, and `registro` (date of registration).
  - `Curso`: Represents courses, which can have multiple students associated via a Many-to-Many relationship.
- **Views:**
  - `custom_sql_query`: Executes custom SQL queries using a database cursor.
  - `raw_query_example`: Uses Django ORM's raw queries to fetch data.
- **Database:** PostgreSQL integration for data storage and retrieval.
- **Templates:** Dynamic HTML template to display a list of students.

---

## Installation and Setup

### Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- PostgreSQL (>= 12)
- pip (Python package manager)
- Virtualenv (optional but recommended)

### Steps

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database:**
   Ensure PostgreSQL is running and update the `DATABASES` section in `settings.py` with your credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'Escuela_DB',
           'USER': 'postgres',
           'PASSWORD': 'admin1234',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Load the Server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application:**
   Open a browser and navigate to:
   - Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   - Custom SQL query view: [http://127.0.0.1:8000/custom-query/](http://127.0.0.1:8000/custom-query/)
   - Raw query view: [http://127.0.0.1:8000/raw-query/](http://127.0.0.1:8000/raw-query/)

---

## File Structure
```
project-folder/
|-- school/
|   |-- migrations/
|   |-- templates/
|   |   |-- estudiantes.html
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- views.py
|   |-- urls.py
|-- project-folder/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- manage.py
|-- requirements.txt
```

---

## Models

### Estudiante
```python
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    edad = models.IntegerField()
    registro = models.DateField(auto_now_add=True)
```

### Curso
```python
class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    estudiantes = models.ManyToManyField(Estudiante, related_name='cursos')

    def __str__(self):
        return self.nombre
```

---

## Views

### Custom SQL Query
```python
def custom_sql_query(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM school_estudiante WHERE edad > %s", [18])
        rows = cursor.fetchall()
    return render(request, 'estudiantes.html', {'estudiantes': rows})
```

### Raw Query Example
```python
def raw_query_example(request):
    estudiante = Estudiante.objects.raw('SELECT * FROM school_estudiante WHERE edad > %s', [18])
    return render(request, 'estudiantes.html', {'estudiantes': estudiante})
```

---

## URLs

```python
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom-query/', views.custom_sql_query, name='custom_query'),
    path('raw-query/', views.raw_query_example, name='raw_query'),
]
```

---

## Templates

### estudiantes.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Estudiantes</title>
</head>
<body>
    <h1>Lista de Estudiantes</h1>
    <ul>
        {% for estudiante in estudiantes %}
            <li>{{ estudiante }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

---

## Requirements

### requirements.txt
```plaintext
asgiref==3.8.1
Django==5.1.4
psycopg2==2.9.10
sqlparse==0.5.3
tzdata==2024.2
```

---

## Database
The project uses PostgreSQL. Ensure your database is configured as shown in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Escuela_DB',
        'USER': 'postgres',
        'PASSWORD': 'admin1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## License
This project is licensed under the MIT License.

