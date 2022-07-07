class Enviador:

    def enviar(self, remetente, destinaratio, assunto, corpo):
        if "@" not in remetente:
            raise EmailInvalido(f"Email de Remetente inválido: {remetente}")
        return remetente


class EmailInvalido(Exception):
    pass
