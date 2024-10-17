# drfsimpletest
Este repositorio contiene una práctica de [Django REST framework](https://www.django-rest-framework.org/) basada en el siguiente video de YouTube: [Django REST Framework, Tu primer REST API mas Despliegue](https://www.youtube.com/watch?v=GE0Q8YNKNgs)

## Descripción
Este proyecto es un CRUD simple para gestionar "proyectos". Permite realizar las operaciones básicas (crear, leer, actualizar y eliminar) sobre proyectos a través de una API REST.

Backend: La persistencia de datos se maneja con PostgreSQL.
Hosting: La aplicación está alojada de forma gratuita en [Render](Render.com).

## Deploy
[Accede a la app aquí](https://drfsimpletest-bm6x.onrender.com/api/projects/). Desde este enlace puedes probar los métodos GET y POST directamente en el navegador. Para probar los métodos PUT, PATCH y DELETE, se recomienda usar Postman o ThunderClient.

## Instrucciones para correr el proyecto localmente
1. Clona el repositorio:
```bash
git clone git@github.com:luismarrer/drfsimpletest.git
cd drfsimpletest
```
2. Configura el entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate  # En Windows
```
3. Instala las dependencias:
```bash
pip install -r requirements.txt
```
4. Aplica las migraciones:
```bash
python manage.py migrate
```
5. Inicia el servidor:
```bash
python manage.py runserver
```
6. Accede a la aplicación desde tu navegador en http://localhost:8000.
