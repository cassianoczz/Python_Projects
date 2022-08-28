from django.shortcuts import render, get_object_or_404

from anuncios_app import models


def home(response):

    categorias = models.Categoria.objects.all()
    ultimos_anuncios = models.Anuncios.objects.all()[:12]

    return render(response, 'home.html', {'categorias': categorias, 'anuncios': ultimos_anuncios})


def anuncio_categoria(response, categoria_id):
    categoria_anuncio = get_object_or_404(models.Categoria, id=categoria_id)

    categorias = models.Categoria.objects.all()

    filtro_anuncios = models.Anuncios.objects.filter(categoria=categoria_anuncio)

    return render(response, 'home.html', {'categorias': categorias, 'anuncios': filtro_anuncios})


def anuncio(response, anuncio_id):
    anuncio = get_object_or_404(models.Anuncios, id=anuncio_id)

    categorias = models.Categoria.objects.all()

    return render(response, 'anuncio.html', {'categorias': categorias, 'anuncio': anuncio})