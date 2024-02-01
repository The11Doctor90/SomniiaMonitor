#  Copyright (c) Matteo Ferreri 2024.

import numpy as np


def convert_into_array(string: str):
    """Converte la stringa in ingresso in un array Numpy"""

    array = np.array([number for number in string.split(',')])
    return array


def is_valid(string: str) -> bool:
    shadow_string = ""
    if len(string) == 0:
        return False

    if "," in string:
        shadow_string = string.replace(',', '')
    else:
        shadow_string = string

    if not shadow_string.isnumeric():
        return False

    shadow_string = string.split(",")
    if len(shadow_string) != 10:
        return False

    return True
