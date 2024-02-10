#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.dao.ekg_signal_dao import EkgSignalDAO
from somniiaMonitor.dao.ekg_signal_dao_impl import EkgSignalDAOImpl
from somniiaMonitor.model.action_response import ActionResponse
from somniiaMonitor.model.ekg_signal_composite import EkgSignalComposite
from somniiaMonitor.model.ekg_signal_data import EkgSignalData


class EkgSignalBusiness:
    __instance = None

    def __init__(self):
        if EkgSignalBusiness.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            EkgSignalBusiness.__instance = self

    @staticmethod
    def get_instance():
        if EkgSignalBusiness.__instance is None:
            EkgSignalBusiness()
        return EkgSignalBusiness.__instance

    @staticmethod
    def get_ekg_signals_by_analysis_id(analysis_id: int) -> EkgSignalComposite:
        ekg_signal_dao: EkgSignalDAO = EkgSignalDAOImpl.get_instance()
        ekg_signals: EkgSignalComposite = ekg_signal_dao.find_ekg_signal_by_analysis_id(analysis_id)
        return ekg_signals

    @staticmethod
    def save_ekg_signal(ekg_signal: EkgSignalData) -> ActionResponse:
        response: ActionResponse = ActionResponse()

        ekg_signal_dao: EkgSignalDAO = EkgSignalDAOImpl.get_instance()
        result = ekg_signal_dao.add_ekg_signal(ekg_signal)
        if result == 0:
            response.set_message("signin_failure")
            return response

        response.set_message("signin_successful")
        response.set_row_count(result)
        return response
