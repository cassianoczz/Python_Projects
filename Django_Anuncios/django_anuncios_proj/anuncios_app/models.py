from django.db import models


class Categoria(models.Model):
    titulo = models.CharField(max_length=40)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']


class Anuncios(models.Model):
    titulo = models.CharField(max_length=40)
    descricao = models.TextField(null=True, blank=True)
    preco = models.DecimalField(max_digits=11, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-id']