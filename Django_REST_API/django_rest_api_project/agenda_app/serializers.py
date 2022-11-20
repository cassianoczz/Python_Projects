from rest_framework import serializers

class AgendamentoSerializer(serializers.Serializer):
    nome_cliente = serializers.CharField(max_length=256)
    data_horario_agendamento = serializers.DateField()
    telefone_cliente = serializers.CharField(max_length=14)
    email_cliente = serializers.EmailField()