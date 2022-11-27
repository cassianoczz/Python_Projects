from agenda_app.models import Agendamento
from agenda_app.serializers import AgendamentoSerializer, PrestadorSerializer
from agenda_app.utils import get_horarios_disponiveis


from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.decorators import api_view

from datetime import datetime


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
    return Response(horario_disponiveis, safe=False)


@api_view(http_method_names=['GET'])
def healthcheck(request):
    return Response({"status": "OK"}, status=200)
