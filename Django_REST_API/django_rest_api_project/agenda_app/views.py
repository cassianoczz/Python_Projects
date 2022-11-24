from agenda_app.models import Agendamento
from agenda_app.serializers import AgendamentoSerializer
from rest_framework import generics


class AgendamentoList(generics.ListCreateAPIView):
   
    serializer_class = AgendamentoSerializer

    def get_queryset(self):
        prestador = self.request.query_params.get('prestador', None)
        queryset = Agendamento.objects.filter(prestador__username=prestador)
        return queryset


class AgendamentoDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
