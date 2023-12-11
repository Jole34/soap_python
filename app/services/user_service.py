from spyne import ServiceBase, rpc, Unicode, String
from app.crud import user_crud_class


class UserService(ServiceBase):
    @rpc(_returns=Unicode)
    def get_users_all(ctx):
        list_of_users = user_crud_class.query_all_users()
        string_for_response = ''
        if list_of_users:
            string_for_response = ','.join([x.name for x in list_of_users])
        return string_for_response

    @rpc(String,_returns=Unicode)
    def get_user_by_name(ctx, name):
        print("Query called")
        print('change requsted')
        user_object = user_crud_class.query_user_by_name(name=name)
        user_response = 'NAN' if not user_object else user_object.name
        return user_response

user_service = UserService