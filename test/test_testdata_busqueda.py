import unittest
import bin.excepciones as ex

from bin.testdata.busquedaLOEquidistante import BusquedaLOEquidistante

from bin.testdata.rango import RangoVal, RangoTam

from bin.algoritmos.busq.busquedalineal import BusquedaLineal
from bin.algoritmos.busq.busquedabinaria import BusquedaBinaria
from bin.algoritmos.busq.busquedasalto import BusquedaSalto
from bin.algoritmos.busq.busquedainterpolacion import BusquedaInterpolacion
from bin.algoritmos.busq.busquedaexponencial import BusquedaExponencial
from bin.algoritmos.busq.busquedafibonacci import BusquedaFibonacci


class ListaOrdenadaEquidistante(unittest.TestCase):
    rangot = RangoTam(10, 50, 2.7)
    rangov = RangoVal(4, 12, 1.26)

    def test_busqueda_lineal_rangos_por_defecto(self):
        bl = BusquedaLineal()
        td = BusquedaLOEquidistante(bl)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)

    def test_busqueda_lineal_rangos_conocidos(self):
        bl = BusquedaLineal()
        td = BusquedaLOEquidistante(bl, self.rangot, self.rangov)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
