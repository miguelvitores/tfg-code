import math
import random
import bin.crear_lista as cl
from bin.algoritmos.busqueda import Busqueda
from bin.analysis import Analysis

from bin.testdata.testdata import TestData
from bin.testdata.rango import RangoTam, RangoVal

rangot_por_defecto = RangoTam(32)
rangov_por_defecto = RangoVal(16)


class BusquedaLOEquidistante(TestData):

    def __init__(self, algoritmo: Busqueda, rangot=rangot_por_defecto, rangov=rangov_por_defecto, repet=1):
        super().__init__(algoritmo, rangot, rangov, repet)

    def analizar(self):
        suma = self.rangot.tmin
        while suma < self.rangot.tmax + 1:
            num = math.floor(suma)
            an = Analysis()
            lista = cl.ordenada_equidistante(self.rangov.vmin, self.rangov.vmax, num)

            for i in range(self.repet):
                r = random.randint(0, num-1)
                self.algoritmo.analizar(lista, an, lista[r])

            an.media(self.repet)
            self.resultados[num] = an
            suma += self.rangot.prec
