from agenda_app.views import index, ler_eventos

from django.urls import path

urlpatternsagenda = [
    path("", index),
    path("eventos/", ler_eventos)    
]