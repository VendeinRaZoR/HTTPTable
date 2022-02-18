# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import urllib.parse
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from urllib import parse

import table

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
  server_address = ('localhost', 8000)
  httpd = server_class(server_address, handler_class)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()

class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        htmlFile = open("index.html",'r')
        jsFile = open("script.js",'r')
        htmlPage = htmlFile.read()
        jsPage = jsFile.read()
        self.wfile.write(htmlPage.encode("ansi"))
        self.wfile.write(jsPage.encode("ansi"))
        self.wfile.write("</script></body></html>".encode("ansi"))
        htmlFile.close()
        jsFile.close()

    def do_POST(self):
        print("this is POST request")
        contentLen = int(self.headers.get("content-length",0))
        contentFields = urllib.parse.parse_qs(self.rfile.read(contentLen))
        print(contentFields)
        startRow = int(contentFields.get(b'startRow')[0].decode('utf-8'))
        endRow = int(contentFields.get(b'endRow')[0].decode('utf-8'))
        sortBy = contentFields.get(b'sortBy')[0].decode('utf-8')
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(''.join(table.getTableBlock(startRow,endRow)).encode("ansi"))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #table.createTable()
    run(HTTPServer,HttpGetHandler)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
