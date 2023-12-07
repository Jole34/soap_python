from wsgiref.simple_server import make_server
from spyne.server.wsgi import WsgiApplication
from application import application_implementation

## Run server
wsg_app = WsgiApplication(application_implementation)
server = make_server('127.0.0.1', 8000, wsg_app)
server.serve_forever()
