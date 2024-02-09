#  Copyright (c) Matteo Ferreri 2024.

class ActionResponse:
    __message: str
    __row_count: int
    __object: object


    def __init__(self):
        pass

    def get_message(self) -> str:
        return self.__message

    def set_message(self, message: str) -> None:
        self.__message = message

    def get_row_count(self) -> int:
        return self.__row_count

    def set_row_count(self, row_count: int) -> None:
        self.__row_count = row_count

    def get_object(self) -> object:
        return self.__object

    def set_object(self, object: object) -> None:
        self.__object = object
