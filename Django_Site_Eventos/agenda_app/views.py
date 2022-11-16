from agenda_app.models import Evento

from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import date

def listar_eventos(response):
    eventos = Evento.objects.filter(data__gte=date.today()).order_by("data")
    return render(response, 'listar_eventos.html', {'eventos': eventos})

def ler_eventos(response):
    #evento = lista_eventos[1]
    return render(response, 'exibir_eventos.html', {'evento': evento})
