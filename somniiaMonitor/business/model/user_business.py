#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.business.model.contact_business import ContactBusiness
from somniiaMonitor.dao.doctor_dao import DoctorDAO
from somniiaMonitor.dao.doctor_dao_impl import DoctorDAOImpl
from somniiaMonitor.dao.sleeper_dao import SleeperDAO
from somniiaMonitor.dao.sleeper_dao_impl import SleeperDAOImpl
from somniiaMonitor.dao.user_dao import UserDAO
from somniiaMonitor.dao.user_dao_impl import UserDAOImpl
from somniiaMonitor.model.action_response import ActionResponse
from somniiaMonitor.model.doctor import Doctor
from somniiaMonitor.model.login_response import LoginResponse
from somniiaMonitor.model.sleeper import Sleeper
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

    @staticmethod
    def get_user(tax_id: str) -> User:
        user_dao: UserDAO = UserDAOImpl.get_instance()
        user: User = user_dao.find_user_by_tax_id(tax_id)
        return user
    @staticmethod
    def get_sleeper(tax_id: str) -> Sleeper:
        sleeper_dao: SleeperDAO = SleeperDAOImpl.get_instance()
        sleeper: Sleeper = sleeper_dao.find_sleeper_by_tax_id(tax_id)
        return sleeper

    @staticmethod
    def get_doctor(tax_id: str) -> Doctor:
        doctor_dao: DoctorDAO = DoctorDAOImpl.get_instance()
        doctor: Doctor = doctor_dao.find_doctor_by_tax_id(tax_id)
        return doctor

    @staticmethod
    def user_exist(tax_id: str) -> bool:
        user_dao: UserDAO = UserDAOImpl.get_instance()
        return user_dao.user_exist(tax_id)

    def save_user(self, user: User) -> ActionResponse:
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

    def save_sleeper(self, sleeper: Sleeper) -> ActionResponse:
        response = self.save_user(sleeper)
        if response.get_row_count() == 0:
            return response
        user: User = response.get_object()
        sleeper.set_user_id(user.get_user_id())

        sleeper_dao: SleeperDAO = SleeperDAOImpl.get_instance()
        result = sleeper_dao.add_sleeper(sleeper)
        if result == 0:
            response.set_message("signin_failure")
            return response

        response.set_message("signin_successful")
        sleeper = sleeper_dao.find_sleeper_by_tax_id(sleeper.get_tax_id())
        response = self.update_user(sleeper)
        return response

    def save_doctor(self, doctor: Doctor) -> ActionResponse:
        response = self.save_user(doctor)
        if response.get_row_count() == 0:
            return response

        user: User = response.get_object()
        doctor.set_user_id(user.get_user_id())
        doctor_dao: DoctorDAO = DoctorDAOImpl.get_instance()

        result = doctor_dao.add_doctor(doctor)
        if result == 0:
            response.set_message("signin_failure")
            return response

        response.set_message("signin_successful")
        doctor = doctor_dao.find_doctor_by_tax_id(doctor.get_tax_id())
        response = self.update_doctor(doctor)
        return response

    @staticmethod
    def update_user(user: User) -> ActionResponse:
        user_dao: UserDAO = UserDAOImpl.get_instance()
        response: ActionResponse = ActionResponse()
        response.set_message("undefined_error")

        result = user_dao.update_user(user)
        if result == 0:
            response.set_message("update_failure")
            return response

        response.set_message("signin_successful")
        user = user_dao.find_user_by_tax_id(user.get_tax_id())
        response.set_object(user)
        response.set_row_count(result)
        return response

    def update_sleeper(self, sleeper: Sleeper) -> ActionResponse:
        sleeper_dao: SleeperDAO = SleeperDAOImpl.get_instance()
        response: ActionResponse = ActionResponse()
        response.set_message("undefined_error")

        response = self.update_user(sleeper)
        result = response.get_row_count()
        if result == 0:
            response.set_message("update_failure")
            return response

        response.set_message("signin_successful")
        sleeper = sleeper_dao.find_sleeper_by_tax_id(sleeper.get_tax_id())
        response.set_object(sleeper)
        response.set_row_count(result)
        return response

    def update_doctor(self, doctor: Doctor) -> ActionResponse:
        doctor_dao: DoctorDAO = DoctorDAOImpl.get_instance()
        response: ActionResponse = ActionResponse()
        response.set_message("undefined_error")

        response = self.update_user(doctor)
        result = response.get_row_count()
        if result == 0:
            response.set_message("update_failure")
            return response

        response.set_message("signin_successful")
        doctor = doctor_dao.find_doctor_by_tax_id(doctor.get_tax_id())
        response.set_object(doctor)
        response.set_row_count(result)
        return response

    @staticmethod
    def delete_user(user: User):
        user_dao: UserDAO = UserDAOImpl.get_instance()
        response: ActionResponse = ActionResponse()
        response.set_message("undefined_error")

        result = user_dao.delete_user(user)
        if result == 0:
            response.set_message("remove_failure this_sleeper")
            return response

        response.set_message("remove_successful")
        response.set_row_count(result)
        return response

    def login(self, email: str, password: str):
        response: LoginResponse = LoginResponse()
        response.set_message("undefine error")

        if not self.email_is_valid(email):
            response.set_message("not a valid email address")
            return response

        if not self.check_password(email, password):
            response.set_message("not a valid password")
        #todo da finire




    @staticmethod
    def is_sleeper(user: User) -> bool:
        sleeper_dao: SleeperDAO = SleeperDAOImpl.get_instance()
        return sleeper_dao.sleeper_exist_by_id(user.get_user_id())

    @staticmethod
    def is_doctor(user: User) -> bool:
        doctor_dao: DoctorDAO = DoctorDAOImpl.get_instance()
        return doctor_dao.doctor_exist_by_id(user.get_user_id())

    @staticmethod
    def email_is_valid(email: str) -> bool:
        contact_business: ContactBusiness = ContactBusiness.get_instance()
        return contact_business.email_is_valid(email)

    @staticmethod
    def check_password(email: str, password: str) -> bool:
        user_dao: UserDAO = UserDAOImpl.get_instance()
        return user_dao.check_password(email, password)
