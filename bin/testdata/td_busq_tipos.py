import bin.crear_lista as cl
from bin.algoritmos.busqueda import Busqueda
from bin.testdata.testdata import TestData
from bin.testdata.rango import RangoTam, RangoVal

rangot_por_defecto = RangoTam(32)
rangov_por_defecto = RangoVal(16)


class BusquedaLOEquidistante(TestData):

    def __init__(self, algoritmo: Busqueda, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.ordenada_equidistante(self.rangov.vmin, self.rangov.vmax, n)


class BusquedaLAleatoria(TestData):

    def __init__(self, algoritmo: Busqueda, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.aleatoria(self.rangov.vmin, self.rangov.vmax, n)


class BusquedaLOACR(TestData):

    def __init__(self, algoritmo: Busqueda, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.ordenada_aleatoria_con_repeticion(self.rangov.vmin, self.rangov.emax, n)


class BusquedaLOASR(TestData):

    def __init__(self, algoritmo: Busqueda, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.ordenada_aleatoria_sin_repeticion(self.rangov.vmin, self.rangov.emax, n)
