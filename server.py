from evento_online import EventoOnline

from http.server import HTTPServer, BaseHTTPRequestHandler



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
            data = f"""
            <html>
                <head>
                    <title> Eventos </title>
                </head>
                <body>

                </body>
            </html>
            """
            self.wfile.write(data.encode())

server = HTTPServer(('localhost', 80), SimpleHandler)
server.serve_forever()
