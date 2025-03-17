from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'sub_dir' 
BASE_DIR = Path(__file__).resolve().parent

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = "6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa"

# Use BigAutoField for Default Primary Key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEBUG=True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cjones',
        'USER': 'cjones',
        'PASSWORD': os.getenv("PGPASSWORD"),
        'HOST': 'dbserver.gctaa.net',
        'PORT': '5432',
    }
}

LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/debug.log',
        },

    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['file','console'],
        }
    }
}

INSTALLED_APPS = ("db",)
