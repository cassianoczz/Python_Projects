from agenda_app.models import Agendamento

from rest_framework.test import APITestCase
from datetime import datetime, timezone
import json


class TestListagemAgendamentos(APITestCase):

    def test_listagem_vazia(self):
        resposta = self.client.get('/api/agendamentos/')
        dados_esperados = {'data': []}
        dados_resposta = json.loads(resposta.content)
        self.assertEqual(dados_resposta, dados_esperados)

    def test_listagem_de_agendamentos_criados(self):
        Agendamento.objects.create(
            nome_cliente="Cassiano",
            data_horario_agendamento=datetime(2022, 11, 1, tzinfo=timezone.utc),
            telefone_cliente='+5549',
            email_cliente='meu@com.br'
        )

        agendamento_serializado = {
            "id": 1,
            "nome_cliente": "Cassiano",
            "data_horario_agendamento": "2022-11-01T00:00:00Z",
            "telefone_cliente": '+5549',
            "email_cliente": 'meu@com.br'
        }
        resposta = self.client.get('/api/agendamentos/')
        dados_resposta = json.loads(resposta.content)
        self.assertEqual(dados_resposta['data'][0], agendamento_serializado)


class TestCriacaoAgendamento(APITestCase):
    def test_cria_agendamento(self):
        agendamento_serializado = {
            "nome_cliente": "Cassiano",
            "data_horario_agendamento": "2022-12-01T00:00:00Z",
            "telefone_cliente": '+5549',
            "email_cliente": 'meu@com.br'
        }

        resposta_post = self.client.post('/api/agendamentos/', agendamento_serializado, format='json')
        resposta_get = self.client.get('/api/agendamentos/')
        dados_resposta_post = json.loads(resposta_post.content)
        dados_resposta_get = json.loads(resposta_get.content)
        self.assertEqual(resposta_post.status_code, 201)
        self.assertEqual(dados_resposta_get['data'][0], dados_resposta_post)

    def test_cria_agendamento_vazio_status_400(self):
        agendamento_serializado = {
            "nome_cliente": "Cassiano",
            "data_horario_agendamento": "2022-12-01T00:00:00Z",
            "telefone_cliente": '',
            "email_cliente": 'meu@com.br'
        }

        resposta_post = self.client.post('/api/agendamentos/', agendamento_serializado, format='json')
        self.assertEqual(resposta_post.status_code, 400)

    def test_cria_agendamento_telefone_vazio_status_400(self):
        agendamento_serializado = {
            "nome_cliente": "Cassiano",
            "data_horario_agendamento": "2022-12-01T00:00:00Z",
            "telefone_cliente": '',
            "email_cliente": 'meu@com.br',
        }
        resposta_post = self.client.post('/api/agendamentos/', agendamento_serializado, format='json')
        self.assertEqual(resposta_post.status_code, 400)

    def test_cria_agendamento_telefone_errado_status_400(self):
        agendamento_serializado = {
            "nome_cliente": "Cassiano",
            "data_horario_agendamento": "2022-12-01T00:00:00Z",
            "telefone_cliente": '+5749',
            "email_cliente": 'meu@com.br',
        }
        resposta_post = self.client.post('/api/agendamentos/', agendamento_serializado, format='json')
        self.assertEqual(resposta_post.status_code, 400)

    def test_cria_agendamento_data_passado_status_400(self):
        agendamento_serializado = {
            "nome_cliente": "Cassiano",
            "data_horario_agendamento": "2022-01-01T00:00:00Z",
            "telefone_cliente": '+5749',
            "email_cliente": 'meu@com.br',
        }
        resposta_post = self.client.post('/api/agendamentos/', agendamento_serializado, format='json')
        self.assertEqual(resposta_post.status_code, 400)