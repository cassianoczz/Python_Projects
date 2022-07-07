from spam.db import Conexao
from spam.modelos import Usuario
import pytest


def test_salvar_usuario(sessao):
    usuario = Usuario(nome="Cassiano", email="Cassiano@github.com.br")
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome="Cassiano", email="Cassiano@github.com.br"), Usuario(nome="Github", email="Github@github.com.br")]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
