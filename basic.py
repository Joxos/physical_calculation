from units import *


def split(data: str):
    for i in range(len(data)):
        if data[i].isalpha():
            return (float(data[:i]), data[i:])


def transfer(data: str, unit: str):
    original_data, original_unit = split(data)
    if original_unit in lengths.keys() and unit in lengths.keys():
        return original_data/lengths[original_unit]*lengths[unit]
    else:
        raise TypeError("Cannot transfer "+original_unit+" into "+unit+".")
