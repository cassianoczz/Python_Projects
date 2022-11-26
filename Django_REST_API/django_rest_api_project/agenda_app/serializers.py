from agenda_app.models import Agendamento

from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.models import User


class AgendamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agendamento
        fields = '__all__'
        # fields = ["id", "nome_cliente", "data_horario_agendamento", "telefone_cliente", "email_cliente"]

    prestador = serializers.CharField()

    def validate_prestador(self, value):
        try:
            prestador = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("prestador não existe.")
        return prestador

    def validate_data_horario_agendamento(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Data deve ser maior ou igual a data atual.")
        return value

    def validate(self, attrs):
        telefone_cliente = attrs.get("telefone_cliente", "")
        if not telefone_cliente.startswith("+55"):
            raise serializers.ValidationError("Telefone deve ser brasileiro.")
        return attrs


class PrestadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'agendamentos']
  
    agendamentos = AgendamentoSerializer(many=True, read_only=True)
