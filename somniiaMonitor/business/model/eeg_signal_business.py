#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.dao.eeg_signal_dao import EegSignalDAO
from somniiaMonitor.dao.eeg_signal_dao_impl import EegSignalDAOImpl
from somniiaMonitor.model.action_response import ActionResponse
from somniiaMonitor.model.eeg_signal_composite import EegSignalComposite
from somniiaMonitor.model.eeg_signal_data import EegSignalData


class EegSignalBusiness:
    __instance = None

    def __init__(self):
        if EegSignalBusiness.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            EegSignalBusiness.__instance = self

    @staticmethod
    def get_instance():
        if EegSignalBusiness.__instance is None:
            EegSignalBusiness()
        return EegSignalBusiness.__instance

    @staticmethod
    def get_eeg_signals_by_analysis_id(analysis_id: int) -> EegSignalComposite:
        eeg_signal_dao: EegSignalDAO = EegSignalDAOImpl.get_instance()
        eeg_signals: EegSignalComposite = eeg_signal_dao.find_eeg_signal_by_analysis_id(analysis_id)
        return eeg_signals

    @staticmethod
    def save_eeg_signal(eeg_signal: EegSignalData) -> ActionResponse:
        response: ActionResponse = ActionResponse()

        eeg_signal_dao: EegSignalDAO = EegSignalDAOImpl.get_instance()
        result = eeg_signal_dao.add_eeg_signal(eeg_signal)
        if result == 0:
            response.set_message("signin_failure")
            return response

        response.set_message("signin_successful")
        response.set_row_count(result)
        return response
