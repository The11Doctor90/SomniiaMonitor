#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.business.model.eeg_signal_business import EegSignalBusiness
from somniiaMonitor.business.model.ekg_parameter_business import EkgParameterBusiness
from somniiaMonitor.business.model.ekg_signal_business import EkgSignalBusiness
from somniiaMonitor.business.model.ppg_parameter_business import PpgParameterBusiness
from somniiaMonitor.business.model.sleep_stage_business import SleepStageBusiness
from somniiaMonitor.business.model.temperature_business import TemperatureBusiness
from somniiaMonitor.dao.analysis_dao import AnalysisDAO
from somniiaMonitor.dao.analysis_dao_impl import AnalysisDAOImpl
from somniiaMonitor.model.action_response import ActionResponse
from somniiaMonitor.model.analysis import Analysis


class AnalysisBusiness:
    __instance = None

    def __init__(self):
        if AnalysisBusiness.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            AnalysisBusiness.__instance = self

    @staticmethod
    def get_instance():
        if AnalysisBusiness.__instance is None:
            AnalysisBusiness()
        return AnalysisBusiness.__instance

    def get_analysis(self, analysis_id: int) -> Analysis:
        analysis_dao: AnalysisDAO = AnalysisDAOImpl.get_instance()
        analysis: Analysis = analysis_dao.find_analysis_by_id(analysis_id)
        analysis = self.fill_analysis(analysis)
        return analysis

    def get_all_sleeper_analyses(self, sleeper_id: int) -> list[Analysis]:
        analysis_dao: AnalysisDAO = AnalysisDAOImpl.get_instance()
        analyses: list[Analysis] = []
        for analysis in analysis_dao.find_analyses_by_sleeper_id(sleeper_id):
            analysis = self.fill_analysis(analysis)
            analyses.append(analysis)
        return analyses

    def get_all_doctor_analyses(self, doctor_id: int) -> list[Analysis]:
        analysis_dao: AnalysisDAO = AnalysisDAOImpl.get_instance()
        analyses: list[Analysis] = []
        for analysis in analysis_dao.find_analyses_by_doctor_id(doctor_id):
            analysis = self.fill_analysis(analysis)
            analyses.append(analysis)
        return analyses

    def get_all_mask_analyses(self, mask_id: int) -> list[Analysis]:
        analysis_dao: AnalysisDAO = AnalysisDAOImpl.get_instance()
        analyses: list[Analysis] = []
        for analysis in analysis_dao.find_analyses_by_mask_id(mask_id):
            analysis = self.fill_analysis(analysis)
            analyses.append(analysis)
        return analyses

    @staticmethod
    def save_analysis(analysis: Analysis) -> ActionResponse:
        response: ActionResponse = ActionResponse()

        analysis_dao: AnalysisDAO = AnalysisDAOImpl.get_instance()
        result = analysis_dao.add_analysis(analysis)
        if result == 0:
            response.set_message("signin_failure")
            return response

        response.set_message("signin_successful")
        analysis = analysis_dao.find_analysis_by_id(analysis.get_analysis_id())
        response.set_object(analysis)
        response.set_row_count(result)
        return response

    @staticmethod
    def delete_analysis(analysis: Analysis):
        analysis_dao: AnalysisDAO = AnalysisDAOImpl.get_instance()
        response: ActionResponse = ActionResponse()
        response.set_message("undefined_error")

        result = analysis_dao.delete_analysis(analysis)
        if result == 0:
            response.set_message("remove_failure this_sleeper")
            return response

        response.set_message("remove_successful")
        response.set_row_count(result)
        return response

    @staticmethod
    def fill_analysis(analysis: Analysis) -> Analysis:
        analysis_copy = analysis

        component = EegSignalBusiness.get_instance()
        analysis_copy.set_eeg_signal_data(component.get_eeg_signal_data())

        component = EkgSignalBusiness.get_instance()
        analysis_copy.set_ekg_signal_data(component.get_ekg_signal_data())

        component = EkgParameterBusiness.get_instance()
        analysis_copy.set_ekg_parameter_data(component.get_ekg_parameter_data())

        component = PpgParameterBusiness.get_instance()
        analysis_copy.set_ppg_parameter_data(component.get_ppg_parameter_data())

        component = SleepStageBusiness.get_instance()
        analysis_copy.set_sleep_stage_data(component.get_sleep_stage_data())

        component = TemperatureBusiness.get_instance()
        analysis_copy.set_temperature_data(component.get_temperature_data())

        return analysis_copy
