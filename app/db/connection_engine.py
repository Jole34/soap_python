from app.utils.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Povezivanje na bazu
engine = create_engine(settings.DB_URL)
session_engine = sessionmaker(engine)
