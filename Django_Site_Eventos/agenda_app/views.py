from agenda_app.models import Evento

from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from datetime import date

def listar_eventos(response):
    eventos = Evento.objects.filter(data__gte=date.today()).order_by("data")
    return render(response, 'listar_eventos.html', {'eventos': eventos})

def ler_eventos(response, id):
    evento = get_object_or_404(Evento, id=id)
    return render(response, 'ler_eventos.html', {'evento': evento})

def participar_evento(resquest):
    evento_id = resquest.POST.get("evento_id")
    evento = get_object_or_404(Evento, id=evento_id)
    evento.participantes += 1
    evento.save()
    return HttpResponseRedirect(reverse('ler_eventos', args=(evento_id,)))