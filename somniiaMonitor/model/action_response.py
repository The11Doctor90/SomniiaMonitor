#  Copyright (c) Matteo Ferreri 2024.

class ActionResponse:
    __message: str
    __row_count: int
    __response_object: object

    def __init__(self):
        self.__message = ""
        self.__row_count = 0
        self.__response_object = None

    def get_message(self) -> str:
        return self.__message

    def set_message(self, message: str) -> None:
        self.__message = message

    def get_row_count(self) -> int:
        return self.__row_count

    def set_row_count(self, row_count: int) -> None:
        self.__row_count = row_count

    def get_object(self) -> object:
        return self.__response_object

    def set_object(self, response_object: object) -> None:
        self.__response_object = response_object
