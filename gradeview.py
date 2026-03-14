# Nicholas Norman March 2026
# Use python to host the app and allows JS to fetch

import http.server
import socketserver
import webbrowser
import os

# Generate files

# Serve the file
PORT = 8080
os.chdir("./")

webbrowser.open(f"http://localhost:{PORT}/gradeview.html")

with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()