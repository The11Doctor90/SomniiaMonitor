#  Copyright (c) Matteo Ferreri 2024.
from enum import Enum


class Stage(Enum):
    AWAKE = 0
    NREM1 = 1
    NREM2 = 2
    NREM3 = 3
    REM = 4


class Staging:
    _staging_id: int
    _time: str
    _stage: Stage

    def __init__(self, staging_id: int = 0, time: str = "", stage: Stage = Stage.AWAKE):
        self._staging_id = staging_id
        self._time = time
        self._stage = stage

    def get_staging_id(self) -> int:
        return self._staging_id

    def get_time(self) -> str:
        return self._time

    def get_stage(self) -> Stage:
        return self._stage

    def set_staging_id(self, staging_id: int) -> None:
        self._staging_id = staging_id

    def set_time(self, time: str) -> None:
        self._time = time

    def set_stage(self, stage: Stage):
        self._stage = stage
