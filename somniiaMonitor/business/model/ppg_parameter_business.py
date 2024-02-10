#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.dao.ppg_parameter_dao import PpgParameterDAO
from somniiaMonitor.dao.ppg_parameter_dao_impl import PpgParameterDAOImpl
from somniiaMonitor.model.action_response import ActionResponse
from somniiaMonitor.model.ppg_parameter_composite import PpgParameterComposite
from somniiaMonitor.model.ppg_parameter_data import PpgParameterData


class PpgParameterBusiness:
    __instance = None

    def __init__(self):
        if PpgParameterBusiness.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            PpgParameterBusiness.__instance = self

    @staticmethod
    def get_instance():
        if PpgParameterBusiness.__instance is None:
            PpgParameterBusiness()
        return PpgParameterBusiness.__instance

    @staticmethod
    def get_ppg_parameters_by_analysis_id(analysis_id: int) -> PpgParameterComposite:
        ppg_parameter_dao: PpgParameterDAO = PpgParameterDAOImpl.get_instance()
        ppg_parameters: PpgParameterComposite = ppg_parameter_dao.find_ppg_parameter_by_analysis_id(analysis_id)
        return ppg_parameters

    @staticmethod
    def save_ppg_parameter(ppg_parameter: PpgParameterData) -> ActionResponse:
        response: ActionResponse = ActionResponse()

        ppg_parameter_dao: PpgParameterDAO = PpgParameterDAOImpl.get_instance()
        result = ppg_parameter_dao.add_ppg_parameter(ppg_parameter)
        if result == 0:
            response.set_message("signin_failure")
            return response

        response.set_message("signin_successful")
        response.set_row_count(result)
        return response
