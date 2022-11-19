from django.db import models

class Agendamento(models.Model):
    nome = models.CharField(max_length=256)
    data_horario = models.DateField()
    telefone = models.CharField(max_length=14)
    email = models.EmailField()