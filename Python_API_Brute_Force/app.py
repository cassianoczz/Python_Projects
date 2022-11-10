from evento import Evento
from evento_online import EventoOnline

evento_online = EventoOnline("Live de Python")
evento_online2 = EventoOnline("Live de JavaScript")
print(evento_online.to_json())
print(evento_online2.to_json())

evento = Evento("Aula de Python", "Rio de Janeiro")
evento.imprime_informações()
