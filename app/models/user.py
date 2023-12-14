from . import Base
from sqlalchemy import Column, Integer, String, Boolean


"""

declarative_base (importovana Base klasa)  omogucava SQLAlchemy-u da automatski generise SQL izraze koji se koriste
za kreiranje tabela i rad sa podacima, na osnovu definicija modela. 
__tablename__ ce biti naziv tabele u bazi
atributi ove klase jesu kolone u bazi na osnovu definisanih elemenata (Integer itd)

"""
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    email = Column(String, index=True, nullable=True)
    name = Column(String)
    age = Column(Integer)
    active = Column(Boolean, default=False)