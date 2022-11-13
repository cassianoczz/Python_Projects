from agenda_app.models import lista_eventos

from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Olá Mundo!")

def ler_eventos(request):
    evento = lista_eventos[1]
    return HttpResponse(f"""
    <html><h1>Evento: {evento.nome}</h1>
    <p>Categoria: {evento.categoria}</p>
    <p>local: {evento.local}</p>
    <p>Link: {evento.link}</p>
    """)

