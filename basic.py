from units import *


def split(data: str):
    if type(data) == str:
        for i in range(len(data)):
            if data[i] != 'e' and data[i].isalpha():
                return (float(data[:i]), data[i:])
    raise SyntaxError("Invalid syntax of inputing a data.")


def transfer(data: str, unit: str):
    original_data, original_unit = split(data)
    if original_unit in length.keys() and unit in length.keys():
        return str(original_data/length[original_unit]*length[unit])+unit
    elif original_unit in mass.keys() and unit in mass.keys():
        return str(original_data/mass[original_unit]*mass[unit])+unit
    elif original_unit in area.keys() and unit in area.keys():
        return str(original_data/area[original_unit]*area[unit])+unit
    elif original_unit in force.keys() and unit in force.keys():
        return str(original_data/force[original_unit]*force[unit])+unit
    else:
        raise TypeError("Cannot transfer "+original_unit+" into "+unit+".")
