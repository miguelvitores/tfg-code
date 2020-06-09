import bin.crear_lista as cl
from bin.algoritmos.busqueda import Busqueda
from bin.testdata.testdata import TestData
from bin.testdata.rango import RangoTam, RangoVal

rangot_por_defecto = RangoTam(32)
rangov_por_defecto = RangoVal(16)


class TestDataLOEquidistante(TestData):

    def __init__(self, algoritmo: Busqueda, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.ordenada_equidistante(self.rangov.vmin, self.rangov.vmax, n)


class TestDataLAleatoria(TestData):

    def __init__(self, algoritmo: Busqueda, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.aleatoria(self.rangov.vmin, self.rangov.vmax, n)


class TestDataLAleatoriaSR(TestData):

    def __init__(self, algoritmo: Busqueda, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.aleatoria_sin_repeticion(self.rangov.vmin, self.rangov.emax, n)


class TestDataLOACR(TestData):

    def __init__(self, algoritmo: Busqueda, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.ordenada_aleatoria_con_repeticion(self.rangov.vmin, self.rangov.emax, n)


class TestDataLOASR(TestData):

    def __init__(self, algoritmo: Busqueda, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.ordenada_aleatoria_sin_repeticion(self.rangov.vmin, self.rangov.emax, n)
