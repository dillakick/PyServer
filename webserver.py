import http.server
import socketserver
import os

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
announce = "Test"


httpd = socketserver.TCPServer(("localhost", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()

# announcements stuff below (e.g; announcement definitions)

def announce():
    f = open("index.html", "a")
    f.write("<b>" + announce + "</b>")
    f.close()
    print("done!")
    
def panic():
    os.remove("index.html")
    f = open("index.html", "x")
    
