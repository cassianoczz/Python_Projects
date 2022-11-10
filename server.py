from evento_online import EventoOnline
from evento import Evento

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

evento_online = EventoOnline("Live de Python")
evento_online2 = EventoOnline("Live de JavaScript")
evento = Evento("Aula de Python", "Rio de Janeiro")

eventos = [evento_online,evento_online2, evento]

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            data = f"""
            <html>
                <head>
                    <title> Olá Mundo </title>
                </head>
                <body>
                    <p>Testando o Server</p>
                    <p>Diretorio: {self.path}</p>
                </body>
            </html>
            """
            self.wfile.write(data.encode())
        elif self.path == "/eventos":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()

            css = """
            <style>
                table {
                    bordr-collapse: collapse;
                }
                td, th {
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                }
            </style>
            """
            
            html = ""
            for evento in eventos:
                html += f"""
                <tr>
                    <td>{evento.id}</td>
                    <td>{evento.nome}</td>
                    <td>{evento.local}</td>
                </tr>"""
            
            data = f"""
            <html>
                <head>
                    <title> Eventos </title> 
                    {css}
                </head>
                <body>
                    <table>
                        <tr>
                            <th>ID</th>
                            <th>Nome</th>
                            <th>Local</th>
                        </tr>
                        {html}
                    </table>
                </body>
            </html>
            """
            self.wfile.write(data.encode())
        elif self.path == "/api/eventos":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()

            list_dict_json_eventos = []
            for evento in eventos:
                list_dict_json_eventos.append({
                    "id": evento.id,
                    "nome": evento.nome,
                    "local": evento.local,
                })
            data = json.dumps(list_dict_json_eventos).encode()
            self.wfile.write(data)

server = HTTPServer(('localhost', 80), SimpleHandler)
server.serve_forever()
