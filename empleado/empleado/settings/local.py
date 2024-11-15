# local.py
from .base import *  # Importa todas las configuraciones de base.py

# Sobrescribe las configuraciones necesarias para el entorno local (desarrollo)

DEBUG = True  # Cambia a True para desarrollo
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Solo en local

# Usa una base de datos SQLite para desarrollo (en lugar de PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Usa SQLite en desarrollo
    }
}
# local.py
STATIC_URL = '/static/'  # Este es el valor estándar para servir archivos estáticos en desarrollo

# Otros ajustes específicos para el entorno de desarrollo pueden ir aquí.
