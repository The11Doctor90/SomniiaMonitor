#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.dao.contact_dao import ContactDAO
from somniiaMonitor.dao.contact_dao_impl import ContactDAOImpl
from somniiaMonitor.model.action_response import ActionResponse
from somniiaMonitor.model.contact import Contact


class ContactBusiness:
    __instance = None

    def __init__(self):
        if ContactBusiness.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ContactBusiness.__instance = self

    @staticmethod
    def get_instance():
        if ContactBusiness.__instance is None:
            ContactBusiness()
        return ContactBusiness.__instance

    @staticmethod
    def get_contact(tax_id: str) -> Contact:
        contact_dao: ContactDAO = ContactDAOImpl.get_instance()
        contact: Contact = contact_dao.find_contact_by_tax_id(tax_id)
        return contact

    @staticmethod
    def contact_exist(tax_id: str) -> bool:
        contact_dao: ContactDAO = ContactDAOImpl.get_instance()
        return contact_dao.contact_exist(tax_id)

    def save_contact(self, contact: Contact) -> ActionResponse:
        response: ActionResponse = ActionResponse()

        if contact.has_empty_field():
            response.set_message("signin_empty_error")
            return response

        if self.contact_exist(contact.get_tax_id()):
            response.set_message(f"signin_exist_error \n {contact.get_tax_id()}")
            return response

        contact_dao: ContactDAO = ContactDAOImpl.get_instance()
        result = contact_dao.add_contact(contact)
        if result == 0:
            response.set_message("signin_failure")
            return response

        response.set_message("signin_successful")
        contact = contact_dao.find_contact_by_tax_id(contact.get_tax_id())
        response.set_object(contact)
        response.set_row_count(result)
        return response

    @staticmethod
    def update_contact(contact: Contact) -> ActionResponse:
        contact_dao: ContactDAO = ContactDAOImpl.get_instance()
        response: ActionResponse = ActionResponse()
        response.set_message("undefined_error")

        result = contact_dao.update_contact(contact)

        if result == 0:
            response.set_message("update_failure")
            return response

        response.set_message("signin_successful")
        contact = contact_dao.find_contact_by_tax_id(contact.get_tax_id())
        response.set_object(contact)
        response.set_row_count(result)
        return response

    @staticmethod
    def delete_contact(contact: Contact):
        contact_dao: ContactDAO = ContactDAOImpl.get_instance()
        response: ActionResponse = ActionResponse()
        response.set_message("undefined_error")

        result = contact_dao.delete_contact(contact)
        if result == 0:
            response.set_message("remove_failure this_contact")
            return response

        response.set_message("remove_successful")
        response.set_row_count(result)
        return response
