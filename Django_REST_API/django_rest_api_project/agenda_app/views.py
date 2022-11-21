from agenda_app.models import Agendamento
from agenda_app.serializers import AgendamentoSerializer

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(http_method_names=["GET", "POST"])
def agendamento_list(resquest):
    if resquest.method == "GET":
        agendamento_qs = Agendamento.objects.all()
        lista_agendamento = AgendamentoSerializer(agendamento_qs, many=True)
        return JsonResponse({'data': lista_agendamento.data})

    if resquest.method == "POST":
        dados_serializado = AgendamentoSerializer(data=resquest.data)
        if dados_serializado.is_valid():
            dados_serializado.save()
            return JsonResponse(dados_serializado.data, status=201)
        return JsonResponse(dados_serializado.errors, status=400)


@api_view(http_method_names=["GET", "PATCH", "DELETE"])
def agendamento_details(request, id):
    agendamento_id = get_object_or_404(Agendamento, id=id)
    if request.method == "GET":
        agendamento_serializado = AgendamentoSerializer(agendamento_id)
        return JsonResponse(agendamento_serializado.data)

    if request.method == "PATCH":
        agendamento_serializado = AgendamentoSerializer(agendamento_id, data=request.data, partial=True)
        if agendamento_serializado.is_valid():
            agendamento_serializado.save()
            return JsonResponse(agendamento_serializado.data, status=200)
        return JsonResponse(agendamento_serializado.errors, status=400)

    if request.method == "DELETE":
        #agendamento_id.cancelando = True AO INVEZ DE DELETAR O ENVENTO PARA MANTER HISTORICO
        agendamento_id.delete()
        return Response(status=204)