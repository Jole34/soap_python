from app.utils.config import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models import User

database_url = settings.DB_URL

class CrudUser:

    def __init__(self):
        engine = create_engine(database_url)
        self.active_session = sessionmaker(engine)
        self.__open_db_session__()

    def __open_db_session__(self):
        self.open_session = self.active_session()

    def close_session(self):
        self.open_session.close()

