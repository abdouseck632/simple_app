import http.server
import socketserver

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Réponse HTTP 200 OK
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        # Contenu de la réponse
        self.wfile.write(b"Hello, World!")
        
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
