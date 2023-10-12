"""
django-htmx

Configuración para settings.py
"""


def INSTALLED_APPS_update(INSTALLED_APPS: list[str]):
    INSTALLED_APPS += [
        "django_htmx",
    ]
    return INSTALLED_APPS


def MIDDLEWARE_update(MIDDLEWARE: list):
    MIDDLEWARE += ["django_htmx.middleware.HtmxMiddleware"]
    return MIDDLEWARE
