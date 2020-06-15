import unittest

from bin.algoritmos.busq.busquedainterpolacion import BusquedaInterpolacion
from bin.algoritmos.ord.ordenacionquicksort import OrdenacionQuicksort
from bin.testdata.rango import RangoVal, RangoTam

from bin.testdata.td_tipos import TestDataOrdenacionLOEquidistante
from bin.testdata.td_tipos import TestDataBusquedaLOEquidistante


class EditarTestdata(unittest.TestCase):
    oq = OrdenacionQuicksort()
    bi = BusquedaInterpolacion()
    rt = RangoTam(40, 10, 2.5)
    rv = RangoVal(180, 20, 5)

    def test_editar_algoritmo_busqueda_previo_analisis(self):
        td = TestDataBusquedaLOEquidistante(self.bi)
        td.analizar()
        td.editar_algoritmo(self.oq)
        self.assertEqual(len(td.resultados), 0)
        self.assertIs(td.algoritmo, self.oq)

    def test_editar_algoritmo_ordenacion_previo_analisis(self):
        td = TestDataOrdenacionLOEquidistante(self.oq)
        td.analizar()
        td.editar_algoritmo(self.bi)
        self.assertEqual(len(td.resultados), 0)
        self.assertIs(td.algoritmo, self.bi)

    def test_editar_rangot_busqueda_previo_analisis(self):
        td = TestDataBusquedaLOEquidistante(self.bi)
        td.analizar()
        td.editar_rangot(self.rt)
        self.assertEqual(len(td.resultados), 0)
        self.assertIs(td.rangot, self.rt)

    def test_editar_rangot_ordenacion_previo_analisis(self):
        td = TestDataOrdenacionLOEquidistante(self.oq)
        td.analizar()
        td.editar_rangot(self.rt)
        self.assertEqual(len(td.resultados), 0)
        self.assertIs(td.rangot, self.rt)

    def test_editar_rangov_busqueda_previo_analisis(self):
        td = TestDataBusquedaLOEquidistante(self.bi)
        td.analizar()
        td.editar_rangov(self.rv)
        self.assertEqual(len(td.resultados), 0)
        self.assertIs(td.rangov, self.rv)

    def test_editar_rangov_ordenacion_previo_analisis(self):
        td = TestDataOrdenacionLOEquidistante(self.oq)
        td.analizar()
        td.editar_rangov(self.rv)
        self.assertEqual(len(td.resultados), 0)
        self.assertIs(td.rangov, self.rv)


class Recalcular(unittest.TestCase):
    oq = OrdenacionQuicksort()
    bi = BusquedaInterpolacion()
    n_veces = 4

    def test_recalcular_busqueda(self):
        td = TestDataBusquedaLOEquidistante(self.bi)
        td.recalcular(self.n_veces)
        self.assertGreater(len(td.resultados), 0)

    def test_recalcular_ordenacion(self):
        td = TestDataOrdenacionLOEquidistante(self.oq)
        td.recalcular(self.n_veces)
        self.assertGreater(len(td.resultados), 0)

    def test_recalcular_busqueda_previo_analisis(self):
        td = TestDataBusquedaLOEquidistante(self.bi)
        td.analizar()
        td.recalcular(self.n_veces)
        self.assertGreater(len(td.resultados), 0)

    def test_recalcular_ordenacion_previo_analisis(self):
        td = TestDataOrdenacionLOEquidistante(self.oq)
        td.analizar()
        td.recalcular(self.n_veces)
        self.assertGreater(len(td.resultados), 0)
