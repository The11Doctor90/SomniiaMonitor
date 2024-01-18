#  Copyright (c) Matteo Ferreri 2024.
from SomniiaMonitor.Model.address import Address
from SomniiaMonitor.Model.mask import Mask


class User:
    """
        Interface to be implemented by each application users.
    """

    def get_user_id(self) -> int:
        """
        Returns the id of the user
        :return: id of the user
        """
        raise NotImplementedError("Abstract method")

    def get_name(self) -> str:
        """
        Returns the name of the user
        :return: the name of the user
        """

        raise NotImplementedError("Abstract method")

    def get_surname(self) -> str:
        """
        Returns the surname of the user
        :return: the surname of the user
        """
        raise NotImplementedError("Abstract method")

    def get_email(self) -> str:
        """
        Returns the e-mail of the user
        :return: the e-mail of the user
        """
        raise NotImplementedError("Abstract method")

    def get_fiscal_code(self) -> str:
        """
        Returns the fiscal code of the user
        :return: the fiscal code of the user
        """
        raise NotImplementedError("Abstract method")

    def get_birthday(self) -> int:
        """
        Returns the birthday of the user
        :return: the birtday of the user
        """
        raise NotImplementedError("Abstract method")

    def get_birthmonth(self) -> int:
        """
        Returns the birthmonth of the user
        :return: the birthmonth of the user
        """
        raise NotImplementedError("Abstract method")

    def get_birthyear(self) -> int:
        """
        Returns the birthyear of the user
        :return: the birthyear of the user
        """
        raise NotImplementedError("Abstract method")

    def get_telephone_number(self) -> str:
        """
        Returns the telephone number of the user
        :return: the telephone number of the user
        """
        raise NotImplementedError("Abstract method")

    def get_address(self) -> Address:
        """
        Returns the address of the user
        :return: the address of the user
        """
        raise NotImplementedError("Abstract method")

    def set_user_id(self, user_id: int) -> None:
        """
        Sets the id of the user
        :param user_id: the id of the user
        :return: none
        """
        raise NotImplementedError("Abstract method")

    def set_name(self, name: str) -> None:
        """
        Sets the name of the user
        :param name: the name of the user
        :return: none
        """
        raise NotImplementedError("Abstract method")

    def set_surname(self, surname: str) -> None:
        """
        Sets the surname of the user
        :param surname: the surname of the user
        :return: none
        """
        raise NotImplementedError("Abstract method")

    def set_email(self, email: str) -> None:
        """
        Sets the e-mail of the user
        :param email: the e-mail of the user
        :return: none
        """
        raise NotImplementedError("Abstract method")

    def set_fiscal_code(self, fiscal_code: str) -> None:
        """
        Sets the fiscal code of the user
        :param fiscal_code: the fiscal Code of the user
        :return: none
        """
        raise NotImplementedError("Abstract method")

    def set_birthday(self, birthday: int) -> None:
        """
        Sets the birthday of the user
        :param birthday: the birthday of the user
        :return: none
        """
        raise NotImplementedError("Abstract method")

    def set_birthmonth(self, birthmonth: int) -> None:
        """
        Sets the birthmonth of the user
        :param birthmonth: the birthday of the user
        :return: none
        """
        raise NotImplementedError("Abstract method")

    def set_birthyear(self, birthyear: int) -> None:
        """
        Sets the birthyear of the user
        :param birthyear: the birthday of the user
        :return: none
        """
        raise NotImplementedError("Abstract method")

    def set_telephone_number(self, telephone_number: str) -> None:
        """
        Sets the telephone number of the user
        :param telephone_number: the telephone number of the user
        :return: none
        """
        raise NotImplementedError("Abstract method")

    def set_address(self, address: Address) -> None:
        """
        Sets the address of the user
        :param address: the address of the user
        :return:
        """
        raise NotImplementedError("Abstract method")

    def get_mask_list(self) -> list[Mask]:
        """
        Gets the mask list of the user
        :return: the mask list of the user
        """
        raise NotImplementedError("Abstract method")

    def add_mask(self, mask: Mask) -> None:
        """
        Adds a mask to the list of masks
        :param mask: the mask (object) to add
        :return: none
        """
        raise NotImplementedError("Abstract method")

    def remove_mask(self, mask: Mask) -> None:
        """
        Removes a mask from the list of masks
        :param mask: the mask (object) to remove
        :return: none
        """
        raise NotImplementedError("Abstract method")

    def clear_mask_list(self) -> None:
        """
        Clears the mask list
        :return: none
        """
        raise NotImplementedError("Abstract method")

    def add_mask_list(self, mask_list: list[Mask]) -> None:
        """
        Adds other mask list to the list of masks
        :param mask_list: the mask list to add
        :return: none
        """
        raise NotImplementedError("Abstract method")
