from evento import Evento
from evento_online import EventoOnline

from flask import Flask, jsonify, abort

evento_online = EventoOnline("Live de Python")
evento_online2 = EventoOnline("Live de JavaScript")
evento = Evento("Aula de Python", "Rio de Janeiro")
eventos = [evento_online,evento_online2, evento]

app = Flask(__name__)

@app.route("/")
def index():
    return "teste"

@app.errorhandler(404)
def error404(erro):
    return jsonify(erro=str(erro)), 404

@app.route("/api/eventos/")
def api_eventos():
    lista_api_eventos = []
    for evento in eventos:
        lista_api_eventos.append(evento.__dict__)
    return jsonify(lista_api_eventos)

@app.route("/api/eventos/<int:id>/")
def api_eventos_id(id):
    for evento in eventos:
        if evento.id == id:
            return jsonify(evento.__dict__)
    abort(404, "Evento nao encontrado")