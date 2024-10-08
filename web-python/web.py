import http.server
import logging
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_request(self, code='-', size='-'):
        logging.info('%s %s %s',
                     self.address_string(),
                     self.requestline,
                     code)
        
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello, World!')
        elif self.path == '/about':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'This is the about page.')
        elif self.path == '/v1':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'This is the v1 page.')
        elif self.path == '/v2':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'This is the v2 page.')
        else:
            self.send_error(404)
if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)s %(message)s',
        level=logging.INFO)
    http.server.test(
        HandlerClass=RequestHandler,
        port=8000,
        bind='0.0.0.0')

