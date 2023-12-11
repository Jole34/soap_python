from . import Base
from sqlalchemy import Column, Integer, String, Boolean

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    email = Column(String, index=True, nullable=True)
    name = Column(String)
    age = Column(Integer)
    active = Column(Boolean, default=False)