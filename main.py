from flask import Flask
from spyne.server.wsgi import WsgiApplication
from application import application_implementation

wsg_app = WsgiApplication(application_implementation)
app = Flask(__name__)
app.wsgi_app = wsg_app

