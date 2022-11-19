from agenda_app.models import Evento, Categoria

from django.test import TestCase, Client

from datetime import date

class TestePaginaInicial(TestCase):

    def teste_rota_raiz_lista_eventos(self):
        client = Client()
        response = client.get("/")
        self.assertTemplateUsed(response, "listar_eventos.html")

class TesteListagemEventos(TestCase):

    def teste_listar_evento_com_data_hoje(self):
        categoria = Categoria()
        categoria.nome = "Backend"
        categoria.save()
        
        evento = Evento()
        evento.nome = "Aula de Python"
        evento.categoria = categoria
        evento.local = "Rondonia"
        evento.data = date.today()
        evento.save()

        client = Client()
        response = client.get('/')
        self.assertContains(response, "Aula de Python")
        self.assertEqual(list(response.context['eventos']), [evento])

    def teste_listar_eventos_sem_data(self):
        categoria = Categoria()
        categoria.nome = 'Backend'
        categoria.save()
    
        evento = Evento()
        evento.nome = 'Aula de Python'
        evento.categoria = categoria
        evento.save()
    
        
        cliente = Client()
        resposta = cliente.get('/')
        self.assertContains(resposta, 'Aula de Python')
        self.assertContains(resposta, 'A definir')
        self.assertEqual(list(resposta.context['eventos']), [evento])