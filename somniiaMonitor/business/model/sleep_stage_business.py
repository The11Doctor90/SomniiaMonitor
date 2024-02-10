#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.dao.sleep_stage_dao import SleepStageDAO
from somniiaMonitor.dao.sleep_stage_dao_impl import SleepStageDAOImpl
from somniiaMonitor.model.action_response import ActionResponse
from somniiaMonitor.model.sleep_stage_composite import SleepStageComposite
from somniiaMonitor.model.sleep_stage_data import SleepStageData


class SleepStageBusiness:
    __instance = None

    def __init__(self):
        if SleepStageBusiness.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            SleepStageBusiness.__instance = self

    @staticmethod
    def get_instance():
        if SleepStageBusiness.__instance is None:
            SleepStageBusiness()
        return SleepStageBusiness.__instance

    @staticmethod
    def get_sleep_stages_by_analysis_id(analysis_id: int) -> SleepStageComposite:
        sleep_stage_dao: SleepStageDAO = SleepStageDAOImpl.get_instance()
        sleep_stages: SleepStageComposite = sleep_stage_dao.find_sleep_stage_by_analysis_id(analysis_id)
        return sleep_stages

    @staticmethod
    def save_sleep_stage(sleep_stage: SleepStageData) -> ActionResponse:
        response: ActionResponse = ActionResponse()

        sleep_stage_dao: SleepStageDAO = SleepStageDAOImpl.get_instance()
        result = sleep_stage_dao.add_sleep_stage(sleep_stage)
        if result == 0:
            response.set_message("signin_failure")
            return response

        response.set_message("signin_successful")
        response.set_row_count(result)
        return response
