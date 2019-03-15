class SampleHandler(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(200)
       self.send_header('Content-type', 'text/plain; rset=utf-8')
       self.end_headers()
       self.wfile.write("Hello, World!\n".encode())
       
if __name__ == '__main__':
   server_address = ('', 8000)
   httpd = HTTPServer(server_address, SampleHandler)
   httpd.serve_forever()
