from django.test import TestCase, Client

class TestePaginaInicial(TestCase):

    def teste_rota_raiz_lista_eventos(self):
        client = Client()
        response = client.get("/")
        self.assertTemplateUsed(response, "listar_eventos.html")
