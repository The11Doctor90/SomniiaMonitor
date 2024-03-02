#  Copyright (c) Matteo Ferreri 2024.

class LoginResponse:
    __message: str
    __response_object: object

    def __init__(self):
        self.__message = ""
        self.__response_object = None

    def get_message(self) -> str:
        return self.__message

    def set_message(self, message: str) -> None:
        self.__message = message

    def get_object(self):
        return self.__response_object

    def set_object(self, response_object: object) -> None:
        self.__response_object = response_object
