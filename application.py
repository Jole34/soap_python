from spyne import Application
from app.services import user_service
from spyne.protocol.soap import Soap11

application_implementation = Application(
        [user_service], "http://127.0.0.1:8000",
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11())