import random
from bin.testdata.rango import RangoVal, RangoTam


def rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec=1):
    tmin = random.randint(1, maxtmin)
    tmax = random.randint(mintmax, maxtmax)
    prec = round((maxprec - 1) * random.random() + 1, 2)
    return RangoTam(tmax, tmin, prec)


def rango_val_aleatorio(maxvmin, maxvmax):
    vmin = random.randint(0, maxvmin)
    vmax = random.randint(vmin, maxvmax)
    return RangoVal(vmax, vmin)
