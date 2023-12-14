from spyne import Application
from app.services import user_service
from spyne.protocol.soap import Soap11


"""
Fajl za inicijalizaciju aplikacije

-> Kreiranje aplikacije
-> Slanje niza servisa koji su kreirani
-> Url na kom se aplikacija nalazi
-> Protokol za slanje zahteva
-> Porokol za prihvatanje zahteva

"""
application_implementation = Application(
        [user_service], "http://127.0.0.1:8000",
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11())