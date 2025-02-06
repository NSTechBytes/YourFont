import http.server
import socketserver
import os

PORT = 2100
DIRECTORY = "documentation"  

os.chdir(DIRECTORY)  
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()