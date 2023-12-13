from spyne import ServiceBase, rpc, Unicode, String, Integer, AnyDict
from app.schemas import UserToReturn
from app.crud import user_crud_class


class UserService(ServiceBase):
    @rpc(_returns=Unicode)
    def get_users_all(ctx):
        list_of_users = user_crud_class.query_all_users()
        string_for_response = ''
        if list_of_users:
            string_for_response = ','.join([x.name for x in list_of_users])
        return string_for_response

    @rpc(String, Integer, String, _returns=Unicode)
    def create_new_user(ctx, name, age, email):
        user_object = user_crud_class.create_user(name=name, age=age, email=email)
        if user_object:
            return "Uspeh"
        return "Nesto je poslo po zlu"

    @rpc(String,_returns=Unicode)
    def get_user_by_name(ctx, name):
        print("Query called")
        print('change requsted')
        user_object = user_crud_class.query_user_by_name(name=name)
        user_response = 'NAN' if not user_object else user_object.name
        return user_response

    @rpc(String, AnyDict, _returns=AnyDict)
    def update_user(ctx, email, user_dict):
        print(email)
        print(user_dict)
        user_updated = user_crud_class.update_existing_user(email=email, fields_to_update=user_dict)
        if not user_updated:
            return {"error": "Korisnik nije lepo azuriran"}
        return UserToReturn(**user_updated.__dict__).dict()

    @rpc(String, _returns=Unicode)
    def delete_user(ctx, email):
        print(email)
        user_deleted = user_crud_class.delete_user_object(email=email)
        if not user_deleted:
            return "Nismo uspesno obrisali korisnika"
        return "Korisnik je uspesno obrisan"

user_service = UserService
