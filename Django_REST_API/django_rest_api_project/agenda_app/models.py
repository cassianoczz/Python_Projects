from django.db import models


class Agendamento(models.Model):
    prestador = models.ForeignKey(
        'auth.User',
        related_name='agendamentos',
        on_delete=models.CASCADE
        )

    nome_cliente = models.CharField(max_length=256)
    data_horario_agendamento = models.DateTimeField()
    telefone_cliente = models.CharField(max_length=14)
    email_cliente = models.EmailField()

    def __str__(self):
        return f'<{self.id}> {self.nome_cliente}'

    class Meta:
        ordering = ['id']
