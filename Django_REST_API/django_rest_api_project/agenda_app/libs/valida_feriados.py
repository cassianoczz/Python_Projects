from requests import get

from django.conf import settings

from datetime import date


def eh_feriado(data) -> bool:
    if settings.TESTING:
        if data.day == 25 and data.month == 12:
            return True
        return False

    resposta_feriados = get(f'https://brasilapi.com.br/api/feriados/v1/{data.year}') 
    if resposta_feriados.status_code != 200:
        raise ValueError('Não foi possivel consultar data feriado')

    feriados = resposta_feriados.json()
    for feriado in feriados:
        data_feriado = date.fromisoformat(feriado['date'])
        if data == data_feriado:
            return True
    return False
