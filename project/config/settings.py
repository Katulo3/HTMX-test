import sys
from pathlib import Path

from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / "apps"))

SECRET_KEY = get_random_secret_key()

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",  # Nuevo
]

SITE_ID = 1  # Nuevo

# Apps de terceros
INSTALLED_APPS += [
    "slippers",
]

# Apps propias
INSTALLED_APPS += [
    "core",
]

if DEBUG:
    INSTALLED_APPS += [
        "django_extensions",
    ]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "builtins": ["slippers.templatetags.slippers"],  # Slippers
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LANGUAGE_CODE = "es"  # Cambiado

TIME_ZONE = "America/Argentina/Mendoza"  # Cambiado

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"  # Nuevo

STATIC_ROOT = BASE_DIR / "static/"  # Nuevo

STATICFILES_DIRS = [
    BASE_DIR / "staticfiles",
    BASE_DIR.parent / "node_modules",
]  # Nuevo

TE_URL = "node_modules/"  # Nuevo


# *****************************
# *** Configuraciones email ***
# *****************************

EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = "ioseph.dev@gmail.com"

if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

from decouple import config

EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")


# ******************************
# *** Configuraciones extras ***
# ******************************

# * debug-tool-bar
if DEBUG:
    from .extra import settings_debug

    INSTALLED_APPS = settings_debug.INSTALLED_APPS_update(INSTALLED_APPS)
    MIDDLEWARE = settings_debug.MIDDLEWARE_update(MIDDLEWARE)
    from .extra.settings_debug import *

# * allauth
from .extra import settings_allauth

INSTALLED_APPS = settings_allauth.INSTALLED_APPS_update(INSTALLED_APPS)
TEMPLATES = settings_allauth.TEMPLATES_update(TEMPLATES)
MIDDLEWARE = settings_allauth.MIDDLEWARE_update(MIDDLEWARE)

# * django-htmx
from .extra import settings_django_htmx
from .extra.settings_allauth import *

INSTALLED_APPS = settings_django_htmx.INSTALLED_APPS_update(INSTALLED_APPS)
MIDDLEWARE = settings_django_htmx.MIDDLEWARE_update(MIDDLEWARE)
