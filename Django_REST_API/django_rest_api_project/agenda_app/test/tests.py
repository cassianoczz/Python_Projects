from agenda_app.models import Agendamento
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from datetime import datetime, timezone
import json

from unittest import mock


class AgendamentoAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.prestador = User.objects.create(
            id=1,
            username="admin",
            password='123',
            is_superuser=1,
        )
        self.client.login(username='admin', password=123)
        return super().setUp()


class TestListagemAgendamentos(AgendamentoAPITestCase):

    def test_listagem_vazia(self):
        resposta = self.client.get('/api/agendamentos/')
        dados_resposta = json.loads(resposta.content)
        self.assertEqual(dados_resposta, [])

    def test_listagem_de_agendamentos_criados(self):

        Agendamento.objects.create(
            prestador=self.prestador ,
            nome_cliente="Cassiano",
            data_horario_agendamento=datetime(2022, 11, 1, tzinfo=timezone.utc),
            telefone_cliente='+5549',
            email_cliente='meu@com.br'
        )

        agendamento_serializado = {
            "id": 1,
            "prestador": "admin",
            "nome_cliente": "Cassiano",
            "data_horario_agendamento": "2022-11-01T00:00:00Z",
            "telefone_cliente": '+5549',
            "email_cliente": 'meu@com.br'
        }
        resposta = self.client.get('/api/agendamentos/?prestador=admin')
        dados_resposta = json.loads(resposta.content)
        self.assertEqual(dados_resposta, [agendamento_serializado])


class TestCriacaoAgendamento(AgendamentoAPITestCase):
    def test_cria_agendamento(self):

        agendamento_serializado = {
            "id": 1,
            "prestador": "admin",
            "nome_cliente": "Cassiano",
            "data_horario_agendamento": "2022-12-01T00:00:00Z",
            "telefone_cliente": '+5549',
            "email_cliente": 'meu@com.br'
        }

        resposta_post = self.client.post('/api/agendamentos/', agendamento_serializado, format='json')
        resposta_get = self.client.get('/api/agendamentos/?prestador=admin')
        dados_resposta_post = json.loads(resposta_post.content)
        dados_resposta_get = json.loads(resposta_get.content)
        self.assertEqual(resposta_post.status_code, 201)
        self.assertEqual(dados_resposta_get, [dados_resposta_post])

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


class TestGetHorarios(APITestCase):
    @mock.patch('agenda_app.libs.valida_feriados.eh_feriado', return_value=True)
    def test_quando_e_data_feriado(self, _):
        resposta = self.client.get('/api/horarios/?data=2022-12-25')
        self.assertEqual(resposta.data, [])

    @mock.patch('agenda_app.libs.valida_feriados.eh_feriado', return_value=False)
    def test_quando_data_dia_comum_retorna_lista_com_horarios(self, _):
        resposta = self.client.get('/api/horarios/?data=2022-12-24')
        self.assertNotEqual(resposta.data, [])
        self.assertEqual(resposta.data, datetime(2022, 12, 24, 9, tzinfo=timezone.utc))
        self.assertEqual(resposta.data, datetime(2022, 12, 24, 16, 30, tzinfo=timezone.utc))
