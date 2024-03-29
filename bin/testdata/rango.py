import math


class RangoTam:
    """Se trata del rango de tamaños que van a tener las distintas listas a analizar en TestData"""
    def __init__(self, maximo: int, minimo=1, precision=1.0):
        self.tmin = minimo
        self.tmax = maximo
        self.prec = min((maximo - minimo) / 2, precision)
        if maximo is not minimo:
            self.tam = int(math.ceil((maximo - minimo + 1) / self.prec))


class RangoVal:
    """Es el rango de valores que va a tener cada lista a analizar. Tiene como atributos el número mínimo que
    encontraremos, además del máximo y el máximo espaciado, necesario en las listas ordenadas aleatorias
    con y sin repectición"""
    def __init__(self, maximo: int, minimo=0, max_espaciado=0):
        self.vmin = minimo
        self.vmax = maximo
        self.emax = max_espaciado
