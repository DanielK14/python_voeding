
# endpoints maken voor andere applicaties om informatie uit op te vragen


from http.server import HTTPServer, BaseHTTPRequestHandler

class defgh:
    def hoi(self):
        return "Welkom"


class abc(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/andere":
            q = defgh()
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            self.wfile.write(q.hoi().encode())
        else:
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            self.wfile.write("doei".encode())

# hieronder wordt een server gestart

def main():
    PORT = 8000
    server = HTTPServer(('', PORT), abc)
    print('Server running 8000')
    server.serve_forever()

# als je het main runnend script bent wordt de main functie aanroepen
# die hierboven geschreven staat.

if __name__ =='__main__':
    main()