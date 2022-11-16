from agenda_app.views import listar_eventos, ler_eventos

from django.urls import path

urlpatternsagenda = [
    path("", listar_eventos),
    path("eventos/", ler_eventos)    
]