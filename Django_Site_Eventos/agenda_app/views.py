from agenda_app.models import lista_eventos

from django.http.response import HttpResponse
from django.shortcuts import render

def index(response):
    return HttpResponse("Olá Mundo!")

def ler_eventos(response):
    evento = lista_eventos[1]
    return render(response, 'exibir_eventos.html', {'evento': evento})
