#!/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import configparser

from utils import webcache, webshow

# Config file
config = configparser.ConfigParser()
config.read("ia_testing.config.ini")
confServer = config["PUBLIC"]

# Website Cache
site = webcache(confServer['listen'])

# Webserver Provider
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        code, mimetype, data = webshow(site, self.path)
        self.send_response(code)
        self.send_header("Content-type", mimetype)
        self.end_headers()
        if not data == None:
            self.wfile.write(bytes(data, "utf-8"))

# Start
if __name__ == "__main__":
    # Listener
    webServer = HTTPServer((confServer["host"], int(confServer["port"])), MyServer)
    print("Server listening on http://%s:%s" % (confServer["host"], confServer["port"]))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
