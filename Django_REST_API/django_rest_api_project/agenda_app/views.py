from agenda_app.models import Agendamento
from agenda_app.serializers import AgendamentoSerializer

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(http_method_names=["GET", "POST"])
def agendamento_list(resquest):
    if resquest.method == "GET":
        agendamento_qs = Agendamento.objects.all()
        lista_agendamento = AgendamentoSerializer(agendamento_qs, many=True)
        return JsonResponse({'data': lista_agendamento.data})
    if resquest.method == "POST":
        dados_serializado = AgendamentoSerializer(data=resquest.data)
        if dados_serializado.is_valid():
            Agendamento.objects.create(
                nome_cliente = dados_serializado.validated_data["nome_cliente"],
                data_horario_agendamento = dados_serializado.validated_data["data_horario_agendamento"],
                telefone_cliente = dados_serializado.validated_data["telefone_cliente"],
                email_cliente = dados_serializado.validated_data["email_cliente"],
            )
            return JsonResponse(dados_serializado.data, status=201)
        return JsonResponse(dados_serializado.errors, status=400)


@api_view(http_method_names=["GET"])
def agendamento_details(request, id):
    agendamento_id = get_object_or_404(Agendamento, id=id)
    agendamento_serializado = AgendamentoSerializer(agendamento_id)
    return JsonResponse(agendamento_serializado.data)

