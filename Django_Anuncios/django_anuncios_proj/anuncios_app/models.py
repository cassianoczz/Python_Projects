from django.db import models


class Categoria(models.Model):
    titulo = models.CharField(max_length=40)
