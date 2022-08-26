from django.shortcuts import render

from anuncios_app import models


def home(response):

    categorias = models.Categoria.objects.all()
    ultimos_anuncios = models.Anuncios.objects.all()[:12]

    return render(response, 'home.html', {'categorias': categorias, 'ultimos_anuncios': ultimos_anuncios})
