# Nicholas Norman March 2026
# Use python to host the app and allows JS to fetch

import http.server
import socketserver
import webbrowser
import os

# open TKinter

# ask for root directory (for input files)
# generate gradeview button

# Generate files
def generate_files():
    # overwrite current gradeview.html file
    gradeviewFile = open("gradeview.html", "w")
    
    
    # ask which folder to generate for
    # for each subfolder (student names)
        # add folder name to student folders list
        # add folder title
        # add folder id

        # for each file
            # add first html file to bottom of JS file
            # add other files below
    pass

def setupServer():
    # Serve the file
    PORT = 8080
    os.chdir("./")

    webbrowser.open(f"http://localhost:{PORT}/gradeview.html")

    with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()