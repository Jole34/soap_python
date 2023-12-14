from flask import Flask
from spyne.server.wsgi import WsgiApplication
from application import application_implementation

"""

Konfigurisanje Flask aplikacije da koristi Spyne WsgiApplication kako bi mogli da pokrenemo SOAP servis sa pomocnim 
alatom (serverom) hupper tako da se na nove izmene automatski server reloaduje.
Naša Spyne aplikacija (koju smo implementirali u application.py) postaje deo Flask aplikacije.

application_implementation je instanca Application klase iz Spyne biblioteke
koju smo kreirali u application.py i koja sadrži definicije naših SOAP servisa.
WsgiApplication koristi ovu instancu kako bi je mogao kreirati kao WSGI aplikaciju
koju Flask koristi za rad sa HTTP zahtevima.

"""

wsg_app = WsgiApplication(application_implementation)
app = Flask(__name__)
app.wsgi_app = wsg_app

