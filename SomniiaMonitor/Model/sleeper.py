#  Copyright (c) Matteo Ferreri 2024.
from SomniiaMonitor.Model.address import Address
from SomniiaMonitor.Model.mask import Mask
from SomniiaMonitor.Model.user import User


class Sleeper(User):
    _user_id: int
    _name: str
    _surname: str
    _email: str
    _fiscalCode: str
    _birthday: int
    _birthmonth: int
    _birthyear: int
    _telephoneNumber: str
    _address: Address
    _masks: list[Mask]

    def __init__(self, user_id: int = 0, name: str = "", surname : str = "", email : str = "", fiscalCode: str = "", birthday: int = 1, birthmonth: int = 1, birthyear: int = 1900, telephoneNumber: str = "", address: Address = Address) -> None:
        self._user_id = user_id
        self._name = name
        self._surname = surname
        self._email = email
        self._fiscalCode = fiscalCode
        self._birthday = birthday
        self._birthmonth = birthmonth
        self._birthyear = birthyear
        self._telephoneNumber = telephoneNumber
        self._address = address
        self._masks = []

    def get_user_id(self) -> int:
        return self._user_id

    def get_name(self) -> str:
        return self._name

    def get_surname(self) -> str:
        return self._surname

    def get_email(self) -> str:
        return self._email

    def get_fiscal_code(self) -> str:
        return self._fiscalCode

    def get_birthday(self) -> int:
        return self._birthday

    def get_birthmonth(self) -> int:
        return self._birthmonth

    def get_birthyear(self) -> int:
        return self._birthyear

    def get_telephone_number(self) -> str:
        return self._telephoneNumber

    def get_address(self) -> Address:
        return self._address

    def set_user_id(self, user_id: int) -> None:
        self._user_id = user_id

    def set_name(self, name: str) -> None:
        self._name = name

    def set_surname(self, surname: str) -> None:
        self._surname = surname

    def set_email(self, email: str) -> None:
        self._email = email

    def set_fiscal_code(self, fiscal_code: str) -> None:
        self._fiscalCode = fiscal_code

    def set_birthday(self, birthday: int) -> None:
        self._birthday = birthday

    def set_birthmonth(self, birthmonth: int) -> None:
        self._birthmonth = birthmonth

    def set_birthyear(self, birthyear: int) -> None:
        self._birthyear = birthyear

    def set_telephone_number(self, telephone_number: str) -> None:
        self._telephoneNumber = telephone_number

    def set_address(self, address: Address) -> None:
        self._address = address

    def get_mask_list(self) -> list[Mask]:
        return self._masks

    def add_mask(self, mask: Mask) -> None:
        self._masks.append(mask)

    def remove_mask(self, mask: Mask) -> None:
        self._masks.remove(mask)

    def clear_mask_list(self) -> None:
        self._masks = []

    def add_mask_list(self, mask_list: list[Mask]) -> None:
        if len(mask_list) > 0:
            for mask in mask_list:
                if mask not in self._masks:
                    self._masks.append(mask)
