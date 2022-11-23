from agenda_app.models import Agendamento
from agenda_app.serializers import AgendamentoSerializer
from rest_framework import generics


class AgendamentoList(generics.ListCreateAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer


class AgendamentoDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
