#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.dao.ekg_parameter_dao import EkgParameterDAO
from somniiaMonitor.dao.ekg_parameter_dao_impl import EkgParameterDAOImpl
from somniiaMonitor.model.action_response import ActionResponse
from somniiaMonitor.model.ekg_parameter_composite import EkgParameterComposite
from somniiaMonitor.model.ekg_parameter_data import EkgParameterData


class EkgParameterBusiness:
    __instance = None

    def __init__(self):
        if EkgParameterBusiness.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            EkgParameterBusiness.__instance = self

    @staticmethod
    def get_instance():
        if EkgParameterBusiness.__instance is None:
            EkgParameterBusiness()
        return EkgParameterBusiness.__instance

    @staticmethod
    def get_ekg_parameters_by_analysis_id(analysis_id: int) -> EkgParameterComposite:
        ekg_parameter_dao: EkgParameterDAO = EkgParameterDAOImpl.get_instance()
        ekg_parameters: EkgParameterComposite = ekg_parameter_dao.find_ekg_parameter_by_analysis_id(analysis_id)
        return ekg_parameters

    @staticmethod
    def save_ekg_parameter(ekg_parameter: EkgParameterData) -> ActionResponse:
        response: ActionResponse = ActionResponse()

        ekg_parameter_dao: EkgParameterDAO = EkgParameterDAOImpl.get_instance()
        result = ekg_parameter_dao.add_ekg_parameter(ekg_parameter)
        if result == 0:
            response.set_message("signin_failure")
            return response

        response.set_message("signin_successful")
        response.set_row_count(result)
        return response
