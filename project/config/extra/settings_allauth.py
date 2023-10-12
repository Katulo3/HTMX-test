"""
django-allauth

Configuración para settings.py

https://django-allauth.readthedocs.io/en/latest/configuration.html
"""
from django.urls import reverse_lazy


def MIDDLEWARE_update(MIDDLEWARE: list):
    MIDDLEWARE += ["allauth.account.middleware.AccountMiddleware"]
    return MIDDLEWARE


def TEMPLATES_update(TEMPLATES: list[dict[str, dict[str, list]]]):
    TEMPLATES[0]["OPTIONS"]["context_processors"].append("django.template.context_processors.request")
    return TEMPLATES


def INSTALLED_APPS_update(INSTALLED_APPS: list[str]):
    INSTALLED_APPS += [
        "allauth",
        "allauth.account",
        "allauth.socialaccount",
        "allauth.socialaccount.providers.google",
    ]
    return INSTALLED_APPS


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
LOGIN_REDIRECT_URL = reverse_lazy("index")
LOGOUT_REDIRECT_URL = reverse_lazy("account_login")
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
SOCIALACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_UNIQUE_EMAIL = True

# https://github.com/mdrhmn/dj-social-auth
# link documentacion para logearse con cuentas de google.

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "OAUTH_PKCE_ENABLED": True,
    }
}
