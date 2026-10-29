import hashlib
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = socket.gethostname()
COLOR = "#" + hashlib.md5(HOST.encode()).hexdigest()[:6]


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = (
            "<body style='background:%s;font-family:sans-serif;color:#fff;"
            "text-align:center;padding-top:20vh;text-shadow:0 0 6px #000'>"
            "<h1>Scale Me</h1><h2>Served by container: %s</h2></body>" % (COLOR, HOST)
        ).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
# tweak
