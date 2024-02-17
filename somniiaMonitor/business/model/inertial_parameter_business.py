#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.dao.inertial_parameter_dao import InertialParameterDAO
from somniiaMonitor.dao.inertial_parameter_dao_impl import InertialParameterDAOImpl
from somniiaMonitor.model.action_response import ActionResponse
from somniiaMonitor.model.inertial_parameter_composite import InertialParameterComposite
from somniiaMonitor.model.inertial_parameter_data import InertialParameterData


class InertialParameterBusiness:
    __instance = None

    def __init__(self):
        if InertialParameterBusiness.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            InertialParameterBusiness.__instance = self

    @staticmethod
    def get_instance():
        if InertialParameterBusiness.__instance is None:
            InertialParameterBusiness()
        return InertialParameterBusiness.__instance

    @staticmethod
    def get_inertial_parameters_by_analysis_id(analysis_id: int) -> InertialParameterComposite:
        inertial_parameter_dao: InertialParameterDAO = InertialParameterDAOImpl.get_instance()
        inertial_parameters: InertialParameterComposite = inertial_parameter_dao.find_inertial_parameter_by_analysis_id(analysis_id)
        return inertial_parameters

    @staticmethod
    def save_inertial_parameter(inertial_parameter: InertialParameterData) -> ActionResponse:
        response: ActionResponse = ActionResponse()

        inertial_parameter_dao: InertialParameterDAO = InertialParameterDAOImpl.get_instance()
        result = inertial_parameter_dao.add_inertial_parameter(inertial_parameter)
        if result == 0:
            response.set_message("signin_failure")
            return response

        response.set_message("signin_successful")
        response.set_row_count(result)
        return response
