from agenda_app.models import Agendamento
from agenda_app.serializers import AgendamentoSerializer

from django.shortcuts import get_object_or_404
from django.http import JsonResponse, Http404

from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response


class AgendamentoList(APIView):
    def get(self, request):
        agendamento_qs = Agendamento.objects.all()
        lista_agendamento = AgendamentoSerializer(agendamento_qs, many=True)
        return JsonResponse({'data': lista_agendamento.data})

    def post(self, request):
        dados_serializado = AgendamentoSerializer(data=request.data)
        if dados_serializado.is_valid():
            dados_serializado.save()
            return JsonResponse(dados_serializado.data, status=HTTP_201_CREATED)
        return JsonResponse(dados_serializado.errors, status=HTTP_400_BAD_REQUEST)
     

class AgendamentoDetails(APIView):

    def get(self, request, id):
        agendamento_id = get_object_or_404(Agendamento, id=id)
        agendamento_serializado = AgendamentoSerializer(agendamento_id)
        return JsonResponse(agendamento_serializado.data)

    def patch(self, request, id):
        agendamento_id = get_object_or_404(Agendamento, id=id)
        agendamento_serializado = AgendamentoSerializer(agendamento_id, data=request.data, partial=True)
        if agendamento_serializado.is_valid():
            agendamento_serializado.save()
            return JsonResponse(agendamento_serializado.data, status=HTTP_200_OK)
        return JsonResponse(agendamento_serializado.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        agendamento_id = get_object_or_404(Agendamento, id=id)
        # agendamento_id.cancelando = True AO INVEZ DE DELETAR O ENVENTO PARA MANTER HISTORICO
        agendamento_id.delete()
        return Response(status=204)
