from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()

        self.wfile.write("{}\n\n".format(self.requestline).encode())

        self.wfile.write("client_address: {}\n".format(self.address_string()).encode())

        self.wfile.write("path: {}\n".format(self.path).encode())
        self.wfile.write("parsed path: {}, query: {}\n".format(parsed_path.path, parse_qs(parsed_path.query)).encode())
        self.wfile.write("\n[Headers]\n".encode())
        for k, v in self.headers.items():
            self.wfile.write("{}: {}\n".format(k, v).encode())
        return

with HTTPServer(('', 8000), MyHTTPRequestHandler) as server:
    server.serve_forever()
