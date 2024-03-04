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


class UserSessionManager:
    __instance = None
    session: User | None = None

    def __init__(self):
        if UserSessionManager.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            UserSessionManager.__instance = self

    @staticmethod
    def get_instance():
        if UserSessionManager.__instance is None:
            UserSessionManager()
        return UserSessionManager.__instance

    def get_session(self):
        return self.session

    def set_session(self, session: User):
        self.session = session

    def delete_session(self):
        self.session = None
