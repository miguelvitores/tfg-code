import bin.excepciones as ex
from bin.testdata.rango import RangoTam, RangoVal


def comprobar_rango(rangot: RangoTam, rangov: RangoVal):
    if rangot.tmax <= rangot.tmin:
        raise ex.RangoNoValido("La cota superior del rango de tamaño no puede ser menor o igual que la cota inferior")
    if rangot.tmin < 1:
        raise ex.RangoNoValido("La cota inferior del rango de tamaño no puede ser menor que 1")
    if rangot.tam < 2:
        raise ex.RangoNoValido("La precisión del rango de tamaño debe ser un valor entre 1 y la mitad del tamaño del "
                               "rango")
    if rangov.vmax <= rangov.vmin:
        raise ex.RangoNoValido("La cota superior del rango de valores no puede ser menor o igual que la cota inferior")
    if rangov.vmin < 0:
        raise ex.RangoNoValido("La cota inferior del rango de valores no puede ser menor que 0")
    if rangov.modif < 0:
        raise ex.RangoNoValido("El modificador del rango de valores debe ser un valor positivo")
