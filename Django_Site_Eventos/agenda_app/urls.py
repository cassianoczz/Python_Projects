from agenda_app.views import listar_eventos, ler_eventos, participar_evento

from django.urls import path

urlpatternsagenda = [
    path("", listar_eventos, name="listar_eventos"),
    path("eventos/<int:id>/", ler_eventos, name="ler_eventos"),
    path("participantes/", participar_evento, name="participar_evento")    
]