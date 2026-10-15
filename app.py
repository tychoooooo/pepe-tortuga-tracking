import http.server
import socketserver

PORT = 5000

class TrackingHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        html = """
        <html>
        <head><title>Transportes Pepe Tortuga S.A.</title></head>
        <body style='font-family: Arial; text-align: center; margin-top: 50px;'>
            <h1>🐢 Panel de Rastreo de Camiones - Pepe Tortuga S.A. 🐢</h1>
            <p style='color: green; font-size: 20px;'>✔ Monitoreo de flotas activo y optimizado.</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))

with socketserver.TCPServer(("", PORT), TrackingHandler) as httpd:
    print(f"Sirviendo panel de rastreo en el puerto {PORT}")
    httpd.serve_forever()
EOF
