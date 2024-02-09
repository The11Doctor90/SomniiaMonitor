#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.dao.user_dao import UserDAO
from somniiaMonitor.dao.user_dao_impl import UserDAOImpl
from somniiaMonitor.model.action_response import ActionResponse
from somniiaMonitor.model.user import User


class UserBusiness:
    __instance = None

    def __init__(self):
        if UserBusiness.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            UserBusiness.__instance = self

    @staticmethod
    def get_instance():
        if UserBusiness.__instance is None:
            UserBusiness()
        return UserBusiness.__instance

    def user_exist(self, tax_id):
        user_dao: UserDAO = UserDAOImpl.get_instance()
        return user_dao.user_exist(tax_id)

    def save_user(self, user: User):
        response: ActionResponse = ActionResponse()

        if user.has_empty_field():
            response.set_message("signin_empty_error")
            return response

        if self.user_exist(user.get_tax_id()):
            response.set_message(f"signin_exist_error \n {user.get_tax_id()}")
            return response

        user_dao: UserDAO = UserDAOImpl.get_instance()
        result = user_dao.add_user(user)
        if result == 0:
            response.set_message("signin_failure")
            return response

        response.set_message("signin_successful")
        user = user_dao.find_user_by_tax_id(user.get_tax_id())
        response.set_object(user)
        response.set_row_count(result)
        return response


"""
    
"""
