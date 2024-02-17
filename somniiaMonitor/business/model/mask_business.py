#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.dao.mask_dao import MaskDAO
from somniiaMonitor.dao.mask_dao_impl import MaskDAOImpl
from somniiaMonitor.model.action_response import ActionResponse
from somniiaMonitor.model.mask import Mask


class MaskBusiness:
    __instance = None

    def __init__(self):
        if MaskBusiness.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            MaskBusiness.__instance = self

    @staticmethod
    def get_instance():
        if MaskBusiness.__instance is None:
            MaskBusiness()
        return MaskBusiness.__instance

    @staticmethod
    def get_mask(mask_address: str) -> Mask:
        mask_dao: MaskDAO = MaskDAOImpl.get_instance()
        mask: Mask = mask_dao.find_mask_by_mac_address(mask_address)
        return mask

    @staticmethod
    def mask_exist(mac_addr: str) -> bool:
        mask_dao: MaskDAO = MaskDAOImpl.get_instance()
        return mask_dao.mask_exist(mac_addr)

    @staticmethod
    def get_all_mask() -> [Mask]:
        mask_dao: MaskDAO = MaskDAOImpl.get_instance()
        mask: [Mask] = mask_dao.find_all_masks()
        return mask

    def save_mask(self, mask: Mask) -> ActionResponse:
        response: ActionResponse = ActionResponse()

        if self.mask_exist(mask.get_mac_addr()):
            response.set_message(f"signin_exist_error \n {mask.get_mac_addr()}")
            return response

        mask_dao: MaskDAO = MaskDAOImpl.get_instance()
        result = mask_dao.add_mask(mask)
        if result == 0:
            response.set_message("signin_failure")
            return response

        response.set_message("signin_successful")
        mask = mask_dao.find_mask_by_mac_address(mask.get_mac_addr())
        response.set_object(mask)
        response.set_row_count(result)
        return response

    @staticmethod
    def update_mask(mask: Mask) -> ActionResponse:
        mask_dao: MaskDAO = MaskDAOImpl.get_instance()
        response: ActionResponse = ActionResponse()
        response.set_message("undefined_error")

        result = mask_dao.update_mask(mask)
        if result == 0:
            response.set_message("update_failure")
            return response

        response.set_message("signin_successful")
        mask = mask_dao.find_mask_by_mac_address(mask.get_mac_addr())
        response.set_object(mask)
        response.set_row_count(result)
        return response

    @staticmethod
    def delete_mask(mask: Mask):
        mask_dao: MaskDAO = MaskDAOImpl.get_instance()
        response: ActionResponse = ActionResponse()
        response.set_message("undefined_error")

        result = mask_dao.delete_mask(mask)
        if result == 0:
            response.set_message("remove_failure this mask")
            return response

        response.set_message("remove_successful")
        response.set_row_count(result)
        return response
