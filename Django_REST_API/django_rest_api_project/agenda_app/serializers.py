from agenda_app.models import Agendamento

from rest_framework import serializers
from django.utils import timezone

class AgendamentoSerializer(serializers.Serializer):

    class Meta:
        model = Agendamento
        fields = ["id", "nome_cliente", "data_horario_agendamento", "telefone_cliente", "email_cliente"]

    def validate(self, attrs):
        telefone_cliente = attrs.get("telefone_cliente", "")
        if not telefone_cliente.startswith("+55"):
            raise serializers.ValidationError("Telefone deve ser brasileiro.")
        return attrs

    def validate_data_horario_agendamento(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Data deve ser maior ou igual a data atual.")
        return value