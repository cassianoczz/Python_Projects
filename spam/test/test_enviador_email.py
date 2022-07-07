import pytest
from spam.enviador_email import Enviador, EmailInvalido


def test_criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    "destinatario",
    ["Cassiano@github.com","email@github.com"])

def test_remetente_email(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(destinatario,
                                "Z@github.com",
                                "Envio inicial de email",
                                "Primeiro email enviado pelo Enviador")
    assert destinatario in resultado


@pytest.mark.parametrize(
    "remetente",
    ["","email"])

def test_remetente_email(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(remetente,
                        "Z@github.com",
                        "Envio inicial de email",
                        "Primeiro email enviado pelo Enviador")
