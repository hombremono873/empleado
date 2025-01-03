# aplicación Empleados

## Descripción
Este es un proyecto academico, con el objetivo de aprender a programar en django

## Requisitos
- Python 3.x
- Django x.x
- Otras dependencias necesarias.

## Instalación
1. Clona el repositorio.
2. Crea un entorno virtual: `python -m venv venv`.
3. Activa el entorno virtual:
   - Linux/Mac: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
4. Instala dependencias: `pip install -r requirements.txt`.

## Uso
1. Ejecuta migraciones: `python manage.py migrate`.
2. Inicia el servidor: `python manage.py runserver`.

## Estructura del Proyecto
- `app/`: Descripción de las aplicaciones del proyecto.
- `media/`: Almacena archivos subidos por los usuarios.
- `static/`: Archivos estáticos como CSS y JavaScript.

## Contribuciones
Pasos para contribuir al proyecto.

## Licencia
Detalles de la licencia del proyecto.

## Aclaraciones generales
### Almacenar imagenes en dajando
Asumiendo que la clase del Modelo empleados debe almacenar una imagen:
1. este sería un ejemplo del campo  imagen = models.ImageField(upload_to="empleado", blank = True,null=True,height_field=None,width_field=None,max_length=None)
2. Esto debe ser configurado en local.py (settings)
- STATIC_URL = '/static/'
- STATICFILES_DIRS = [
    BASE_DIR / "static",
]
- MEDIA_URL = "/media/"
- MEDIA_ROOT = BASE_DIR / 'media'
3. El campo de imagen de la base de datos debe ser registrado en admin.py en la app relacionada

4. En el template para crear un objeto nuevo es fundamental:
 - <enctype="multipart/form-data" fundamental para que se cree la imagen>
 - esto debe estar en la etiqueta form "enctype="multipart/form-data"
 - <form method="POST" class="cell grid-x grid-margin-x" enctype="multipart/form-data">
- ultimo anexo
 
