from django.urls import path

from .views import home, anuncio_categoria

urlpatterns = [
    path('', home, name='home'),
    path('categoria/<int:categoria_id>', anuncio_categoria, name='anuncio_categoria')
]