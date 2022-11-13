from evento import Evento
from evento_online import EventoOnline

from flask import Flask, jsonify, abort, json, request

evento_online = EventoOnline("Live de Python")
evento_online2 = EventoOnline("Live de JavaScript")
evento = Evento("Aula de Python", "Rio de Janeiro")
db_eventos = [evento_online,evento_online2, evento]

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask Funcionando"

@app.errorhandler(400)
def error400(erro):
    return jsonify(erro=str(erro)), 400

@app.errorhandler(404)
def error404(erro):
    return jsonify(erro=str(erro)), 404

@app.route("/api/eventos/", methods=['POST'])
def cria_eventos():
    dados_request = json.loads(request.data)
    nome = dados_request.get("nome")
    local = dados_request.get("local")
    if not nome:
        abort(400, "'nome' precisa ser informado")
    if local:
        evento = Evento(nome, local)
    else:
        evento = EventoOnline(nome)

    db_eventos.append(evento)
    return {
        "id": evento.id,
        "url": f"/api/eventos/{evento.id}" 
    }

@app.route("/api/eventos/")
def ler_eventos():
    lista_api_eventos = []
    for evento in db_eventos:
        lista_api_eventos.append(evento.__dict__)
    return jsonify(lista_api_eventos)

def pegar_eventos_ou_404(id):
    for evento in db_eventos:
        if evento.id == id:
            return evento
    abort(404, "Evento nao encontrado")

@app.route("/api/eventos/<int:id>/")
def ler_eventos_id(id):
    evento = pegar_eventos_ou_404(id)
    return jsonify(evento.__dict__)

@app.route("/api/eventos/<int:id>/", methods=['PUT'])
def atualizar_eventos_id(id):

    dados_request = request.get_json()
    nome = dados_request.get("nome")
    local = dados_request.get("local")
    if not nome:
        abort(400, "'nome' precisa ser informado")
    if not local:
        abort(400, "'local' precisa ser informado")
        
    evento = pegar_eventos_ou_404(id)
    evento.nome = nome
    evento.local = local
    return jsonify(evento.__dict__)


@app.route("/api/eventos/<int:id>/", methods=['DELETE'])
def deletar_eventos_id(id):
    evento = pegar_eventos_ou_404(id)
    db_eventos.remove(evento)
    return jsonify(id=id)

    