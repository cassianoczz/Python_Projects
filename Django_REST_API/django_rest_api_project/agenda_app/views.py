from agenda_app.models import Agendamento
from agenda_app.serializers import AgendamentoSerializer, PrestadorSerializer
from agenda_app.utils import get_horarios_disponiveis

from django.http.response import HttpResponse 
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes

import csv
from datetime import date, datetime


class IsOwnerOrCreateOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        prestador = request.query_params.get('prestador', None)
        if request.method == 'POST':
            return True
        if request.user.username == prestador:
            return True
        return False


class IsPrestador(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.prestador == request.user:
            return True
        return False


class PrestadorList(generics.ListAPIView):

    permission_classes = [permissions.IsAdminUser]
    serializer_class = PrestadorSerializer
    queryset = User.objects.all()


@api_view(http_method_names=["GET"])
@permission_classes([permissions.IsAdminUser])
def relatorio_prestador(request):
    relatorio_csv = request.query_params.get('formato')
    prestadores = User.objects.all()
    serializer = PrestadorSerializer(prestadores, many=True)
    if relatorio_csv == 'csv':
        resposta_csv = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': f'attachment; filename="relatorio_prestador_{date.today()}.csv"'},
        )
        arquivo_csv = csv.writer(resposta_csv)
        for prestador in serializer.data:
            agendamentos = prestador['agendamentos']
            for agendamento in agendamentos:
                arquivo_csv.writerow([
                    agendamento['prestador'],
                    agendamento['nome_cliente'],
                    agendamento['data_horario_agendamento'],
                    agendamento['telefone_cliente'],
                    agendamento['email_cliente']
                ])
        return resposta_csv
    else:
        return Response(serializer.data)


class AgendamentoList(generics.ListCreateAPIView):

    permission_classes = [IsOwnerOrCreateOnly]
    serializer_class = AgendamentoSerializer

    def get_queryset(self):
        prestador = self.request.query_params.get('prestador', None)
        queryset = Agendamento.objects.filter(prestador__username=prestador)
        return queryset


class AgendamentoDetails(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsPrestador]
    serializer_class = AgendamentoSerializer
    queryset = Agendamento.objects.all()


@api_view(http_method_names=["GET"])
def get_horarios(request):
    data = request.query_params.get('data')
    if not data:
        data = datetime.now().date()
    else:
        data = datetime.fromisoformat(data).date()
    horario_disponiveis = sorted(list(get_horarios_disponiveis(data)))
    return Response(horario_disponiveis)


@api_view(http_method_names=['GET'])
def healthcheck(request):
    return Response({"status": "OK"}, status=200)
