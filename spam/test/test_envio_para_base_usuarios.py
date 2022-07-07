from unittest.mock import Mock

import pytest

from spam.modelos import Usuario
from test_enviador_email import Enviador
from spam.main import EnviadorSpam
from spam.test.conftest import sessao


@pytest.mark.parametrize(
    "usuarios",
    [
        [Usuario(nome="Cassiano", email="Cassiano@github.com.br"),
         Usuario(nome="Github", email="Github@github.com.br")],
        [Usuario(nome="Cassiano", email="Cassiano@github.com.br")]
    ]
)
def test_qtd_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)

    enviador = Mock()
    enviador_spam = EnviadorSpam(sessao, enviador)
    enviador_spam.enviar_emails(
        "cassi.zucco@github.com",
        "Curso Python Pro",
        "Confira os codigos no GitHub"
    )
    assert len(usuarios) == enviador.enviar.call_count


class EnviadorMock(Enviador):
    def __init__(self):
        self.parametros_enviados = None
        self.qtd_spam_enviados = 0

    def enviar(self, remetente, destinaratio, assunto, corpo):
        self.parametros_enviados = (remetente, destinaratio, assunto, corpo)
        self.qtd_spam_enviados += 1


def test_parametros_spam(sessao):
    usuario = Usuario(nome="Cassiano", email="Cassiano@github.com.br")
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_spam = EnviadorSpam(sessao, enviador)
    enviador_spam.enviar_emails(
        "cassi.zucco@github.com",
        "Curso Python Pro",
        "Confira os codigos no GitHub"
    )
    enviador.assert_called_once_with(
        "cassi.zucco@github.com",
        "Cassiano@github.com.br",
        "Curso Python Pro",
        "Confira os codigos no GitHub"
    )