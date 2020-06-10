import bin.crear_lista as cl
from bin.algoritmos.busqueda import Busqueda
from bin.algoritmos.ordenacion import Ordenacion
from bin.testdata.testdata import TestDataBusqueda, TestDataOrdenacion
from bin.testdata.rango import RangoTam, RangoVal

rangot_por_defecto = RangoTam(32)
rangov_por_defecto = RangoVal(16)


class TestDataBusquedaLOEquidistante(TestDataBusqueda):

    def __init__(self, algoritmo: Busqueda, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.ordenada_equidistante(self.rangov.vmin, self.rangov.vmax, n)


class TestDataBusquedaLAleatoria(TestDataBusqueda):

    def __init__(self, algoritmo: Busqueda, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.aleatoria(self.rangov.vmin, self.rangov.vmax, n)


class TestDataBusquedaLOACR(TestDataBusqueda):

    def __init__(self, algoritmo: Busqueda, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.ordenada_aleatoria_con_repeticion(self.rangov.vmin, self.rangov.emax, n)


class TestDataBusquedaLOASR(TestDataBusqueda):

    def __init__(self, algoritmo: Busqueda, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.ordenada_aleatoria_sin_repeticion(self.rangov.vmin, self.rangov.emax, n)


class TestDataOrdenacionLOEquidistante(TestDataOrdenacion):

    def __init__(self, algoritmo: Ordenacion, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.ordenada_equidistante(self.rangov.vmin, self.rangov.vmax, n)


class TestDataOrdenacionLAleatoria(TestDataOrdenacion):

    def __init__(self, algoritmo: Ordenacion, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.aleatoria(self.rangov.vmin, self.rangov.vmax, n)


class TestDataOrdenacionLOACR(TestDataOrdenacion):

    def __init__(self, algoritmo: Ordenacion, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.ordenada_aleatoria_con_repeticion(self.rangov.vmin, self.rangov.emax, n)


class TestDataOrdenacionLOASR(TestDataOrdenacion):

    def __init__(self, algoritmo: Ordenacion, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.ordenada_aleatoria_sin_repeticion(self.rangov.vmin, self.rangov.emax, n)


class TestDataOrdenacionLAleatoriaSR(TestDataOrdenacion):

    def __init__(self, algoritmo: Ordenacion, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def crear_lista(self, n):
        return cl.aleatoria_sin_repeticion(self.rangov.vmin, self.rangov.emax, n)
