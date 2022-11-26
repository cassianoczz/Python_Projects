from agenda_app.libs.valida_feriados import eh_feriado
from agenda_app.models import Agendamento

from datetime import date, datetime, timezone, timedelta
from typing import Iterable

def get_horarios_disponiveis(data: date) -> Iterable[datetime]:

    try:
        if eh_feriado(data):
            return []
    except ValueError:
        pass

    inicio = datetime(year=data.year, month=data.month, day=data.day, hour=9, minute=0, tzinfo=timezone.utc)
    fim = datetime(year=data.year, month=data.month, day=data.day, hour=17, minute=0, tzinfo=timezone.utc)
    intervalo_agendamentos = timedelta(minutes=30)
    horarios_disponiveis = set()
    while inicio < fim:
        if not Agendamento.objects.filter(data_horario_agendamento=inicio).exists():
            horarios_disponiveis.add(inicio)
        inicio += intervalo_agendamentos
    return horarios_disponiveis
