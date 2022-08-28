from django.urls import path

from .views import home, anuncio_categoria, anuncio

urlpatterns = [
    path('', home, name='home'),
    path('categoria/<int:categoria_id>', anuncio_categoria, name='anuncio_categoria'),
    #name = auxilia arquivo html encotrar a url e passar para a view
    path('anuncio/<int:anuncio_id>', anuncio, name='anuncio')
]