# local.py
from .base import *  # Importa todas las configuraciones de base.py

# Sobrescribe las configuraciones necesarias para el entorno local (desarrollo)

DEBUG = True  # Cambia a True para desarrollo
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Solo en local

# Usa una base de datos SQLite para desarrollo (en lugar de PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbempleado',     # Nombre de la base de datos
        'USER': 'postgres',       # Usuario de la base de datos
        'PASSWORD': 'Root123',    # Contraseña del usuario
        'HOST': 'localhost',      # El servidor de la base de datos
        'PORT': '5432',           # Puerto de PostgreSQL
    }
}

# local.py
STATIC_URL = '/static/'  # Este es el valor estándar para servir archivos estáticos en desarrollo

# Otros ajustes específicos para el entorno de desarrollo pueden ir aquí.
# Asegúrate de que STATICFILES_DIRS esté configurado correctamente
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
#Cuando se guarda una tabla con imagenes, django asume la direccion base como "/media/""
#ahora todo se guarda en la carpeta base llamada media
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / 'media'  # Correcta concatenación con Path