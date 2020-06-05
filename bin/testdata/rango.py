
class RangoTam:
    """Se trata del rango de tamaños que van a tener las distintas listas a analizar en TestData"""
    def __init__(self, maximo: int, minimo=1, precision=1.0):
        self.tmin = minimo
        self.tmax = maximo
        self.tam = int((maximo - minimo + 1) // precision)
        self.prec = min(self.tam / 2, precision)


class RangoVal:
    """Es el rango de valores que va a tener cada lista a analizar. Tiene como atributos el número mínimo que
    encontraremos, además del máximo y el modificador de necesitarlos. El modificador valdrá para espaciar"""
    def __init__(self, maximo: int, minimo=0, modificador=1.0):
        self.vmin = minimo
        self.vmax = maximo
        self.modif = modificador
