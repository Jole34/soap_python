from app.models import User
from app.db.connection_engine import session_engine
from typing import Optional


class CrudUser:

    @staticmethod
    def create_user(name: str, age: int) -> bool:
        db = None
        try:
            db = session_engine()
            new_user_object = User(name=name, age=age)
            db.add(new_user_object)
            db.commit()
            db.flush()
            return True
        except:
            return False
        finally:
            db.close()

    @staticmethod
    def query_user_by_name(name: str)-> Optional[User]:
        db = None
        try:
            db = session_engine()
            return db.query(User).filter(User.name == name).first()
        except:
            return None
        finally:
            db.close()

    @staticmethod
    def query_all_users()-> Optional[User]:
        db = None
        try:
            db = session_engine()
            return db.query(User).all()
        except:
            return None
        finally:
            db.close()


user_crud_class = CrudUser
