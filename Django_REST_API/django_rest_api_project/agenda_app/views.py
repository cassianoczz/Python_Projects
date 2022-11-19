from agenda_app.models import Agendamento

from django.shortcuts import get_object_or_404

def agendamento_details(request, id):
    agendamentos = get_object_or_404(Agendamento, id=id)

