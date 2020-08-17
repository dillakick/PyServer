import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
announce = "Test"


httpd = socketserver.TCPServer(("localhost", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()

# announcements stuff below (e.g; announcement definitions)

def announce():
    f = open("demofile2.txt", "a")
    f.write("<b>" + announce + "</b>")
    f.close()
    print("done!")