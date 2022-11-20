from agenda_app.models import Agendamento
from agenda_app.serializers import AgendamentoSerializer

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(http_method_names=["GET"])
def agendamento_list(resquest):
    agendamento_qs = Agendamento.objects.all()
    lista_agendamento = AgendamentoSerializer(agendamento_qs, many=True)
    return JsonResponse({'data': lista_agendamento.data})

@api_view(http_method_names=["GET"])
def agendamento_details(request, id):
    agendamento_id = get_object_or_404(Agendamento, id=id)
    agendamento_serializado = AgendamentoSerializer(agendamento_id)
    return JsonResponse(agendamento_serializado.data)

