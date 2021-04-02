from basic import *


def pressure_fs(force, surface):
    force = transfer(force, "N")
    surface = transfer(surface, "m^2")
    fdata = split(force)[0]
    sdata = split(surface)[0]
    return str(fdata/sdata)+"Pa"
