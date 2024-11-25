# base.py
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent #se agrega .parent tenemos que saltar dentro de los templates un paso mas
SECRET_KEY = 'django-insecure-81v-%mwilgr7lqz4_rp2%5kubp1mqhfqliq8x1a-u9$5x#)2we'
# Configuración por defecto para producción
DEBUG = False  # Por defecto en producción
ALLOWED_HOSTS = ['mi-sitio-en-produccion.com', '127.0.0.1', 'localhost']

# Base de datos por defecto para producción (en este caso PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Usa PostgreSQL en producción
        'NAME': 'empleado_prod',  # Nombre de la base de datos
        'USER': 'usuario',        # Nombre de usuario para la base de datos
        'PASSWORD': 'contraseña', # Contraseña para la base de datos
        'HOST': 'localhost',      # Dirección del servidor de base de datos
        'PORT': '5432',           # Puerto de conexión a la base de datos
    }
}

# Otros ajustes generales que no cambian entre entornos
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #aplicaciones de terceros
    # aplicaciones locales
    'applications.departamentos',
    'applications.empleados',
    'applications.home',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'empleado.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],  # Puedes agregar tus directorios de plantillas aquí
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'empleado.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
