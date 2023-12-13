from app.models import User
from app.db.connection_engine import session_engine
from typing import Optional, List


class CrudUser:

    @staticmethod
    def create_user(name: str, age: int, email: str) -> bool:
        db = None
        try:
            db = session_engine()
            new_user_object = User(name=name, age=age, email=email)
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
    def query_all_users()-> Optional[List[User]]:
        db = None
        try:
            db = session_engine()
            return db.query(User).all()
        except:
            return None
        finally:
            db.close()


    @staticmethod
    def update_existing_user(email: str, fields_to_update: dict) -> Optional[User]:
        db = None
        try:
            db = session_engine()
            user_from_db = db.query(User).filter(User.email == email).first()
            if not user_from_db:
                return None
            print(fields_to_update.keys())
            if 'id' in fields_to_update.keys() or 'email' in fields_to_update.keys():
                return None
            for k,v in fields_to_update.items():
                if k not in user_from_db.__dict__.keys():
                    return None
                setattr(user_from_db, k, v[0]) if getattr(user_from_db, k) != v[0] else None
            user_to_update = user_from_db
            db.add(user_to_update)
            db.commit()
            db.refresh(user_from_db)
            return user_from_db
        except:
            return None
        finally:
            db.close()

    @staticmethod
    def delete_user_object(email: str) -> bool:
        db = None
        try:
            db = session_engine()
            user_object = db.query(User).filter(User.email == email).first()
            if not user_object:
                return True
            db.delete(user_object)
            db.commit()
        except:
            return False
        finally:
            db.close()




user_crud_class = CrudUser
