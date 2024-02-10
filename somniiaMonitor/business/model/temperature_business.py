#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.dao.temperature_dao import TemperatureDAO
from somniiaMonitor.dao.temperature_dao_impl import TemperatureDAOImpl
from somniiaMonitor.model.action_response import ActionResponse
from somniiaMonitor.model.temperature_composite import TemperatureComposite
from somniiaMonitor.model.temperature_data import TemperatureData


class TemperatureBusiness:
    __instance = None

    def __init__(self):
        if TemperatureBusiness.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            TemperatureBusiness.__instance = self

    @staticmethod
    def get_instance():
        if TemperatureBusiness.__instance is None:
            TemperatureBusiness()
        return TemperatureBusiness.__instance

    @staticmethod
    def get_temperatures_by_analysis_id(analysis_id: int) -> TemperatureComposite:
        temperature_dao: TemperatureDAO = TemperatureDAOImpl.get_instance()
        temperatures: TemperatureComposite = temperature_dao.find_temperature_by_analysis_id(analysis_id)
        return temperatures

    @staticmethod
    def save_temperature(temperature: TemperatureData) -> ActionResponse:
        response: ActionResponse = ActionResponse()

        temperature_dao: TemperatureDAO = TemperatureDAOImpl.get_instance()
        result = temperature_dao.add_temperature(temperature)
        if result == 0:
            response.set_message("signin_failure")
            return response

        response.set_message("signin_successful")
        response.set_row_count(result)
        return response
