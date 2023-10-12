"""
Documentación de project.apps.core.views dsdsw
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """
    Args:
        request: Una solicitud HTTP.
    Returns:
        Renderiza la plantilla index.html y la devuelve como respuesta
    Plantilla de herencia:
        index.html extiende de base.html
    URL:
        /
    """
    return render(request, "index.html")
