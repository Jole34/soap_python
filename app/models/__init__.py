from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# IMPORT OF MODELS THAT WILL BE USED IN CODE
from .user import User
