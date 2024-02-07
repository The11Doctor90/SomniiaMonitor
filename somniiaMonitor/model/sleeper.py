#  Copyright (c) Matteo Ferreri 2024.

from somniiaMonitor.model.contact import Contact
from somniiaMonitor.model.user import User


class Sleeper(User):
    # __analyses = list[Analyses]

    def __init__(self) -> None:
        super().__init__()
