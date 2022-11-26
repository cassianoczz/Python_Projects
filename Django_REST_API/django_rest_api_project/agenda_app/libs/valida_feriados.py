from requests import get

from datetime import date


def eh_feriado(data) -> bool:
    resposta_feriados = get(f'https://brasilapi.com.br/api/feriados/v1/{data.year}') 
    if resposta_feriados.status_code != 200:
        raise ValueError('Não foi possivel consultar data feriado')

    feriados = resposta_feriados.json()
    for feriado in feriados:
        data_feriado = date.fromisoformat(feriado['date'])
        if data == data_feriado:
            return True
    return False
