import agenda_app.views

from django.urls import path

urlpatternsagenda = [
    path("", agenda_app.views.index)    
]