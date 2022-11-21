from agenda_app.models import Agendamento

from rest_framework import serializers
from django.utils import timezone

class AgendamentoSerializer(serializers.Serializer):
    nome_cliente = serializers.CharField(max_length=256)
    data_horario_agendamento = serializers.DateTimeField()
    telefone_cliente = serializers.CharField(max_length=14)
    email_cliente = serializers.EmailField()

    def validate(self, attrs):
        telefone_cliente = attrs.get("telefone_cliente", "")
        if not telefone_cliente.startswith("+55"):
            raise serializers.ValidationError("Telefone deve ser brasileiro.")
        return attrs

    def validate_data_horario_agendamento(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Data deve ser maior ou igual a data atual.")
        return value
            

    def create(self, validated_data):
        agendamento = Agendamento.objects.create(
            nome_cliente = validated_data["nome_cliente"],
            data_horario_agendamento = validated_data["data_horario_agendamento"],
            telefone_cliente = validated_data["telefone_cliente"],
            email_cliente = validated_data["email_cliente"],
            )
        return agendamento

    def update(self, instance, validated_data):
        instance.nome_cliente = validated_data.get("nome_cliente", instance.nome_cliente)
        instance.data_horario_agendamento = validated_data.get("data_horario_agendamento", instance.data_horario_agendamento)
        instance.telefone_cliente = validated_data.get("telefone_cliente", instance.telefone_cliente)
        instance.email_cliente = validated_data.get("email_cliente", instance.email_cliente)
        instance.save()
        return instance